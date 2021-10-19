# A Statistical Test for Difference of Two Rates

## Setup

### The Scenario

Suppose we are a subscription service, and we want to A/B test a new campaign to
reduce churn.  Suppose also we do not have good information on expected churn
rate from month to month (e.g, because we have not collected data previously to
establish a baseline population churn rate).  In this scenario, we will need to
use separate test and control groups, and test the difference between test and
control group's churn rates after the intervention.  To make things concrete,
let's say we measure the churn rate at the end of every month, and the
intervention is a push notification or something that fires sometime during the
month of study.  Moreover, and these devices have been chosen because they are
at a relatively high risk of churning.

### Notation

* Let the subscript $i\in\{t, c\}$ denote that a quantity is calculated for the
test or control group, respectively.
* Let $P_i$ denote churn rate.
* Let $Q_i = 1-P_i$ denote survival rate.
* Let $N_i$ denote the observed number of churners in group $i$.
* Let $n$ be the sample size for the test and control groups (i.e., there are
    $2n$ total participants).
* Let $\alpha$ and $\beta$ be the usual definitions of type I and II error,
    respectively.
* For any real number $\gamma$, let $z_{1-\gamma}$ be the usual standard normal
    cutoff quantile.

### Objective

Note that $N_i \simeq Binom(n, P_i)$.  Assuming $n$ is large, then 
$Binom(n, P_i) \sim N(N_i, n\cdot P_i\cdot Q_i)$.  Since we are dealing with a
lot of customers and there is little risk in using large samples, we may assume
$n$ is large and the differences are negligible.  Therefore, we can use a
suitable $z$ statistic to test the difference $N_t - N_c$, which is
approximately distributed as $N(n(P_t - P_c), n(P_tQ_t - P_cQ_c))$.

Since we hope to reduce churn with this campaign, let's assume the null
hypothesis is that $P_t \geq P_c$, and the alternative hypothesis is $P_t<P_c$.

## Calculating the $z$-Statistic

Let 
$$z = \frac{N_t - N_c - n(P_t - P_c)}{\sqrt{n(P_tQ_t - P_cQ_c)}}$$

Assuming the null hypothesis, we reject if $z < -z_{\alpha}$.  Under the null
hypothesis, $P_t - P_c \geq 0$.  In fact, we can assume $P_t = P_c$ under the
null, so that our rejection region is as small as possible.  In other words,
define
$$z_{H_0} = \frac{N_t - N_c}{\sqrt{2nP_cQ_c}}$$
and define the rejection region as
$$ R = \{z_{H_0} < z_{\alpha}\} = \{N_t - N_c < z_\alpha\sqrt{2nP_cQ_c}\}$$.

## Deciding Sample Size

Power is defined to be
$$\begin{aligned}
1 - \beta &\geq \mathbb{P}(R\ \vert\ H_a) \\
&= \mathbb{P}( N_t - N_c < z_\alpha\sqrt{2nP_cQ_c}\ \vert\ P_t < P_c) \\
&= \mathbb{P}\left( z < \frac{z_\alpha\sqrt{2nP_cQ_c} - n(P_t - P_c)}{\sqrt{n(P_tQ_t + P_cQ_c)}} \right).
\end{aligned}$$
But this expression is true if and only if the right hand side is $z_{1-\beta}$.
Therefore, we have
$$\begin{aligned}
z_{1-\beta}\sqrt{n(P_tQ_t + P_cQ_c)} &< z_\alpha\sqrt{2nP_cQ_c} - n(P_t-P_c) \\
\sqrt{n}(P_t - P_c) &< z_\alpha\sqrt{2P_cQ_c} + z_\beta\sqrt{P_tQ_t + P_cQ_c} \\
n &> \left(\frac{z_\alpha\sqrt{2P_cQ_c} + z_\beta\sqrt{P_tQ_t + P_cQ_c}}{P_c - P_t}\right)^2.
\end{aligned}$$
