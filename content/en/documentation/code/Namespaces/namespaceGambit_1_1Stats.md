---
title: "namespace Gambit::Stats"

description: "[No description available]"

---

# namespace Gambit::Stats

[No description available]

## Functions

|                | Name           |
| -------------- | -------------- |
| double | **[gaussian_loglikelihood](/documentation/code/namespaces/namespacegambit_1_1stats/#function-gaussian-loglikelihood)**(double theory, double obs, double theoryerr, double obserr, bool profile_systematics)<br>Use a detection to compute a simple chi-square-like log likelihood, for the case when obs is Gaussian distributed.  |
| double | **[lognormal_loglikelihood](/documentation/code/namespaces/namespacegambit_1_1stats/#function-lognormal-loglikelihood)**(double theory, double obs, double theoryerr, double obserr, bool profile_systematics) |
| double | **[lognormal_loglikelihood_relerror](/documentation/code/namespaces/namespacegambit_1_1stats/#function-lognormal-loglikelihood-relerror)**(double theory, double obs, double reltheoryerr, double relobserr, bool profile_systematics) |
| double | **[gaussian_upper_limit](/documentation/code/namespaces/namespacegambit_1_1stats/#function-gaussian-upper-limit)**(double theory, double obs, double theoryerr, double obserr, bool profile_systematics)<br>Use a detection to compute a gaussian log-likelihood for an upper limit.  |
| double | **[gaussian_lower_limit](/documentation/code/namespaces/namespacegambit_1_1stats/#function-gaussian-lower-limit)**(double theory, double obs, double theoryerr, double obserr, bool profile_systematics)<br>Use a detection to compute a gaussian log-likelihood for a lower limit.  |
| void | **[test_likelihoods](/documentation/code/namespaces/namespacegambit_1_1stats/#function-test-likelihoods)**()<br>A simple tester routine for the likelihood functions.  |

## Attributes

|                | Name           |
| -------------- | -------------- |
| const double | **[logmin](/documentation/code/namespaces/namespacegambit_1_1stats/#variable-logmin)** <br>Minimum finite result returnable from log(double x);.  |


## Functions Documentation

### function gaussian_loglikelihood

```
double gaussian_loglikelihood(
    double theory,
    double obs,
    double theoryerr,
    double obserr,
    bool profile_systematics
)
```

Use a detection to compute a simple chi-square-like log likelihood, for the case when obs is Gaussian distributed. 

### function lognormal_loglikelihood

```
double lognormal_loglikelihood(
    double theory,
    double obs,
    double theoryerr,
    double obserr,
    bool profile_systematics
)
```


Use a detection to compute a simple chi-square-like log likelihood, for the case when obs is log-normal distributed. Version that takes absolute errors. 


### function lognormal_loglikelihood_relerror

```
double lognormal_loglikelihood_relerror(
    double theory,
    double obs,
    double reltheoryerr,
    double relobserr,
    bool profile_systematics
)
```


Use a detection to compute a simple chi-square-like log likelihood, for the case when obs is log-normal distributed. Version that takes fractional (relative) errors. 


### function gaussian_upper_limit

```
double gaussian_upper_limit(
    double theory,
    double obs,
    double theoryerr,
    double obserr,
    bool profile_systematics
)
```

Use a detection to compute a gaussian log-likelihood for an upper limit. 

### function gaussian_lower_limit

```
double gaussian_lower_limit(
    double theory,
    double obs,
    double theoryerr,
    double obserr,
    bool profile_systematics
)
```

Use a detection to compute a gaussian log-likelihood for a lower limit. 

### function test_likelihoods

```
void test_likelihoods()
```

A simple tester routine for the likelihood functions. 


## Attributes Documentation

### variable logmin

```
const double logmin = log(std::numeric_limits<double>::min());
```

Minimum finite result returnable from log(double x);. 




-------------------------------

Updated on 2025-02-12 at 15:36:40 +0000