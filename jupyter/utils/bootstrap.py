from __future__ import annotations
from pandas.core.series import Series

from sklearn.base import BaseEstimator
from sklearn.ensemble import GradientBoostingRegressor
import sklearn.datasets as data
from pandas import DataFrame
import numpy as np
from IPython import embed


class Bootstrap:
    def __init__(
        self,
        model: BaseEstimator,
        X: DataFrame | np.ndarray,
        y: Series | np.ndarray,
    ) -> None:
        self.model = model
        self.X = X
        self.y = y

    def get_conf_int(
        self,
        idx: int,
        num_subsamples: int = 100,
        num_rows: int = 100,
        quantile: float = 0.95,
    ) -> (float, float):
        ys = np.zeros(num_subsamples)

        for i in range(num_subsamples):
            print(f"at row {i}")
            idxs = self._bootstrap_sample(num_rows)

            # Make sure we are not training on idx
            while idx in idxs:
                print("trying again")
                idxs = self._bootstrap_sample(num_rows)

            df = self.X[idxs]
            target = self.y[idxs]

            self.model.fit(df, target)
            ys[i] = self.model.predict(self.X[idx].reshape(1, -1))

        return np.quantile(ys, (1 - quantile) / 2), np.quantile(ys, (1 + quantile) / 2)

    def _bootstrap_sample(self, num_rows: int) -> np.ndarray:
        """Sample num_rows of self.dataset with replacement"""

        print("getting a sample")

        if type(self.X) == DataFrame:
            idxs = np.random.choice(self.X.index, num_rows, replace=True)
        else:
            idxs = np.random.choice(range(self.X.shape[0]), num_rows, replace=True)

        return idxs


if __name__ == "__main__":
    model = GradientBoostingRegressor()
    db = data.load_diabetes()
    boot = Bootstrap(model, db["data"], db["target"])
