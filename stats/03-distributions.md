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
* If $X = \sum_{i=1}^rY_i$, where $Y_i$ are iid $Geom(p)$, then $X\sim NegBin(r, p)$

#### Poisson

* Written $Poisson(\lambda)$.
* Models the probability of a given number of events occurring in a fixed
  interval of time or space if these events occur with a known constant mean
  rate and independently of the time since the last event, for example
  estimating the number of calls to a call center in one hour.
* Limit of $Binom(n, \lambda/n)$.  This is interesting in light of the above
    description.  We can think of a binomial model as modeling a similar even
    but with finitely many time steps, and such that at most one event "occurs"
    during a given time step (so that the maximum number of events is finite).

### Continuous Distributions

#### Uniform

* Written $Unif([a, b])$.
* Models any experiment where only the range is known.  It is the no-information
    model.

#### Exponential

* Written $Exp(\lambda)$.
* It is the continuous analogue of the geometric distribution. Why?  It models
    time until an event.  How?  Is there a similar limit identity as with
    Binomial/Poisson?
* It is memoryless, in the sense that if $X$ is an exponential random variable,
    then $P(X>x+y \vert X>y) = P(X>x)$.
* There must be some connection to the Poisson distribution, but I don't know
    what that is.

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
