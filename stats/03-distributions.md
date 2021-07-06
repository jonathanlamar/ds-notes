# Notes on Common Distributions

## Intuition for each distribution

### Discrete Distributions

#### Bernoulli

* Written $Ber(p)$.
* Any coin toss, or any event with precisely two outcomes.

#### Binomial

* Written $Binom(N, p)$.
* Estimating the parameter of Bernoulli distribution through trials.
* Evidently $Binom(n, p)$ can be approximated by a normal distribution for large
  $n$ (by CLT for Bernoulli sample mean).
* There is a similar approximation of Poisson by Binomial.

#### Geometric distribution

* Written $Geom(p)$.
* Closely related to Bernoulli.  It is the Distribution of flipping a coin until
  the first success.

#### Negative Binomial

* Written $NegBin(r, p)$.
* Distribution of the number of failures _until the rth success_.

#### Poisson

* Written $Poisson(\lambda)$.
* Limit of $Binom(n, \lambda/n)$.

### Continuous Distributions

#### Uniform

* Written $Unif([a, b])$.

#### Exponential

* Written $Exp(\lambda)$.

#### Gamma

* Written $\Gamma(r, \lambda)$.

#### Chi-Square

* Written $\chi^2_k$.

#### Normal

* Written $N(\mu, \sigma^2)$.


### Interesting Relationships

* Bernoulli to Binomial
* Binomial to Gaussian
* Binomial to Poisson
* Poisson to Exponential
