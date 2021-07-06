# Confidence Intervals

## The basic idea

Suppose we have an estimator $\hat{\theta}$ for a parameter $\theta$.  We want
to compute a confidence interval for $\hat{\theta}$ with level $1-\alpha$.  That
is, an interval which contains $1-\alpha$ of the probability mass of the
estimator.  If $\hat{\theta}$ is a nice enough estimator (e.g. consistent and
with a well behaved symmatric density function) and that the bounds of the
interval are constructed appropriately (often so that the interval is centered
around $\hat{\theta})$, then we can think of the confidence interval as a
statement of guarantee about the precision of the estimate, i.e, that there is
only an $\alpha$ probability that the "true" parameter $\theta$ lies outside of
the confidence interval.

## Motivating example

Let $X_1,X_2,\ldots$ be a sequence of iid random variables with distribution
$N(\mu, 1)$.

* Let $\hat{\mu}$ be the sample average $\overline{X}_n$.
* By LLN, $\hat{\mu}$ converges to $\mu$ in probability, so it is a consistent
    estimator.
* By direct calculation, $\hat{\mu} \sim N(\mu, 1/n^2)$, so we know its
    distribution.
* So we compute a $1-\alpha$ interval by _pivoting_ $\hat{\mu}$, that is,
    performing a transformation on $\mu$ whose output has a known distribution
    that does not depend on any unknown quantities.  In this case, we state
    $\sqrt{n}(\hat{\mu} - \mu) \sim N(0,1)$.
* We find an interval based on the pivot distribution.  In this case,
$$
\begin{aligned}
P(\lvert \sqrt{n}(\hat{\mu} - \mu)\rvert > z_{\alpha/2}) < \alpha \\
P(\lvert \mu - \hat{\mu}\rvert > z_{\alpha/2} / \sqrt{n}) < \alpha,
\end{aligned}
$$
and therefore there is a $1-\alpha$ chance that $\mu$ lies in the interval
$[\hat{\mu} - z_{\alpha/2}/\sqrt{n}, \hat{\mu} + z_{\alpha/2} / \sqrt{n}]$.

### The one-sided version

Suppose we want to punish overestimates only (For instance if the cost with
overestimates is higher than that for underestimates, as is often the case in
biostats or certain business data science).  Then we follow a similar procedure,
only to find an interval of the form $(-\infty, \hat{\mu} + s)$ or $(\hat{\mu} -
s, \infty)$.  Thus, as in the above example, we calculate the one sided
$1-\alpha$ confidence interval for the mean of a Gaussian (with known variance)
as $(-\infty, \hat{\mu} + z_\alpha / \sqrt{n})$.
