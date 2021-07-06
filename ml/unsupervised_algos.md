# Unsupervised Machine Learning Models

Here is a list of quick, memorizable descriptions of various unsupervised
algorithms that can be used for analysis, dimension reduction, and data
cleaning.

## PCA

### Theory

#### The Covariance Matrix

Let $X$ be an $n\times m$ dataset and let $\mu_X$ be the matrix with entries
$(\mu_X)_{i,j} = \mu_{X_j} = \frac{1}{n}\sum_kX_{k,j}$ (i.e., the column means
repeated over each column). The covariance matrix of $X$ is defined to be

$$
\Sigma = (1/n)(X-\mu_X)^T(X-\mu_X).
$$

This is ultimately due to the identity

$$
\begin{aligned}
\frac{1}{n}((X-\mu_X)^T(X-\mu_X))_{i,j}
&= \frac{1}{n}\sum_k(X-\mu_X)^T_{i,k}(X-\mu_X)_{k,j} \\
&= \frac{1}{n}\sum_k(X-\mu_X)_{k, i}(X-\mu_X)_{k,j} \\
&= \frac{1}{n}\sum_k\big[X_{k,i}X_{k,j} - \mu_{X_j}X_{k,i} - \mu_{X_i}X_{k,j} +
\mu_{X_i}\mu_{X_j}\big] \\
&= \frac{1}{n}\sum_kX_{k,i}X_{k,j} - \mu_{X_i}\mu_{X_j} \\
&= \widehat{\mathbb{E}}(X_{\cdot, i}X_{\cdot, j}) - \mu_{X_i}\mu_{X_j} \\
&= \text{Cov}(X_{\cdot, i}, X_{\cdot, j})
\end{aligned}
$$

where the estimated expectation in the last line is viewing the columns as
univariate random variables (so that isn't meant to be a dot product, although
the expectation itself is). Thus, the entries of the covariance matrix are the
pairwise covariances of the column vectors of $X$.

#### Eigenvalues of the Covariance Matrix

Now, assume that $\mu_X = 0$. All of this is still true otherwise, but the
calculations are more annoying. Because $\Sigma$ is symmetric, it is
diagonalizable. Consider the eigendecomposition

$$
\Sigma = Q\Lambda Q^{-1},
$$

where $Q$ is the matrix whose columns are the eigenvectors of $\Sigma$.

Consider the first principal component. By definition, this is the unit vector
linear combination of the features $X_{\cdot, i}$ which _maximizes_ variance.
So if we write

$$
Z_1 = \sum_{i=1}^m\phi_{i, 1}X_i,
$$

Then the vector $\phi = (\phi_{1,1}, \ldots, \phi_{m, 1})^T$ maximizes the
equation

$$
\begin{aligned}
\frac{1}{n}\langle Z_1, Z_1\rangle &= \frac{1}{n}\langle\sum_i\phi_{i, 1}X_i,
\sum_j\phi_{j, 1}X_j\rangle \\
&= \sum_{i,j}\phi_i\phi_j\cdot\frac{1}{n}\langle X_i, X_j\rangle \\
&= \sum_{i,j}\phi_i\phi_j\cdot \Sigma_{i,j} \\
&= \phi^T\Sigma\phi \\
&= \lVert\phi\rVert\cdot\lVert\Sigma\phi\rVert\cdot\cos(\theta) \\
&= \lVert\Sigma\phi\rVert\cdot\cos(\theta) \\
&\leq \lVert\Sigma\rVert.
\end{aligned}
$$

Now, it is a fact that I looked up on the internet that the $L2$-norm of a
matrix is equal to the largest singular value of that matrix (why?). It is also
a fact that the singular values and eigenvalues coincide for a symmetric matrix
(this is a straightforward computation). Thus, the final line in the above
equation is equal to the largest eigenvalue of $\Sigma$, and therefore the
eigenvector of $\Sigma$ corresponding to this eigenvalue is in fact the first
principal component.

The rest of the eigenvectors of $\Sigma$ are called the other principal
components of $X$

## Singular Value Decomposition

## K Means

## Robust Covariance

## One Clas SVM

## Isolation Forest
