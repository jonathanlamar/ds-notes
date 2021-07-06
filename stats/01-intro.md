# Introduction

## Probability Spaces

### Definitions

* A _probability space_ is a triple $(\Omega, \mathcal{F}, P)$, where
  $\Omega$ is a set of _outcomes_, $\mathcal{F}$ is a $\sigma$-algebra of
  measurable subsets of $\Omega$ called _events_, and $P$ is a measure on
  $\mathcal{F}$ such that $P(\Omega) = 1$.
* A function between two measure spaces is called _measurable_ if the preimages
    of measurable sets in the target are measurable in the source.
* Let $(\Omega, \mathcal{F}, P)$ be a probability space.  A _random variable_ is
    a real-valued measurable function $X:\Omega\to \mathbb{R}$.
* Let $X$ be a random variable.  Then $X$ induces a probability measure on
    $\mathbb{R}$ called its _distribution_ defined by setting
$$
\mu(A) = P(X\in A)
$$
    for any Borel set $A$.
* Let $X$ be a random variable.  The distribution is usually described by its
    _cumulative distribution function_ $F_X(x)$, which is defined as
$$
F_X(x) = P(X \leq x).
$$

## Convergence

### Definitions

* The strongest mode of convergence is actually weaker than pointwise.  We say
   a sequence of random variables $X_1, X_2, \ldots$ converges _almost surely_
   to $L$ and write $X_n\overset{(a.s.)}{\to} L$ if
$$
\mathbb{P}(X_n \to L) = 1,
$$
i.e., the set of points for which the sequence does _not_ converge is negligible.
* We say a sequence of random variables $X_1, X_2, \ldots$ converges _in
   probability_ to $L$ and write $X_n\overset{(p)}{\to} L$ if for all $\epsilon >0$,
$$
\mathbb{P}(\lvert X_n - L \rvert > \epsilon) \to 0,
$$
where here convergence is that of real numbers.  Almost sure convergence implies
convergence in probability.
* We say $X_n \to L$ _in distribution_ if the sequence of CDF functions
   $F_{X_n}$ converges pointwise to $F_L$.  Convergence in probability implies
   convergence in distribution.  The converse is true when $L$ is a point mass.

### Examples

* Strong Law of Large Numbers: If $X_1,X_2\ldots$ are a sequence of iid random
    variables with mean $\mu$.  Define the sample average
    $$
    \overline{X}_n = \frac{1}{n}\sum_{i=1}^nX_i.
    $$
    Then $\overline{X}_n \to \mu$ almost surely.
* Weak Law of Large Numbers: Same assumptions (actually weaker), the sequence
    converges in probability.
* Central Limit Theorem:  Suppose $X_1,X_2,\ldots$ is a sequence of iid random
    variables with mean $\mu$ and finite variance $\sigma^2$.  Then
    $$
    \sqrt{n}(\overline{X}_n - \mu) \overset{(d)}{\to} N(0, \sigma^2).
    $$

## Distributions

In probability theory, almost sure convergence and convergence in probability
are considered fairly strong.  Although convergence in distribution is the
weakest, it is typically all we really need.  The following theorem states that
CDFs capture random variables well enough.

**Theorem** (Durrett, Theorems 1.2.1 and 1.2.2): A function
$F:\mathbb{R}\to\mathbb{R}$ is a distribution function if and only if it
satisfies the following definitions:
* $F$ is nondecreasing;
* $\lim_{x\to\infty}F(x) = 1$ and $\lim_{x\to-\infty}F(x)=0$;
* $F$ is right continuous, i.e., $\lim_{y\downarrow x}F(y) = F(x)$;

**A note about the proof**: The interesting direction of the above theorem is
proven by taking the set of outcomes to be the Borel sets of $\mathbb{R}$.  In
this sense, we can always assume that Borel sets are the set of outcomes of any
random variable we may be studying, as long as the properties we are studying
are only up to equality in distribution.

### Nifty examples of distribution functions

* (Durrett Example 1.2.4) Uniform distribution on the Cantor set.
* (Durrett Example 1.2.6) Let $q_1,q_2,\ldots$ be an enumeration of the
    rationals.  Let $\{\alpha_i\}$ be any sequence whose infinite series sums to
    1, and let
    $$
    F(x) = \sum_{i=1}^\infty \alpha_i\mathbb{1}_{[q_i, \infty)}
    $$

### Notes about the set of outcomes of a random variable

As mentioned above, the set of outcomes of a random variable are a bit skippery.
 In fact, the set $\Omega$ is almost never explicitly specified.
