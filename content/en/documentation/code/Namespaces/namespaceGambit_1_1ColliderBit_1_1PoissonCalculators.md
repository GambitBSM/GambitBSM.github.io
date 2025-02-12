---
title: "namespace Gambit::ColliderBit::PoissonCalculators"

description: "[No description available]"

---

# namespace Gambit::ColliderBit::PoissonCalculators

[No description available]

## Functions

|                | Name           |
| -------------- | -------------- |
| double | **[log_factorial](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1poissoncalculators/#function-log-factorial)**(double k) |
| double | **[beta](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1poissoncalculators/#function-beta)**(double x, double y) |
| double | **[binom](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1poissoncalculators/#function-binom)**(double n, double k) |
| template <typename engine_type \> <br>int | **[umvue_draw_n_mc](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1poissoncalculators/#function-umvue-draw-n-mc)**(double n_mc, engine_type engine) |
| int | **[umvue_draw_n_mc](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1poissoncalculators/#function-umvue-draw-n-mc)**(double n_mc) |
| int | **[umvue_draw_n_mc_threadsafe](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1poissoncalculators/#function-umvue-draw-n-mc-threadsafe)**(double n_mc) |
| double | **[umvue_poisson_like](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1poissoncalculators/#function-umvue-poisson-like)**(int k, double b, int o, int n_mc, double n_exp) |
| double | **[mle_poisson_loglike](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1poissoncalculators/#function-mle-poisson-loglike)**(double s, double b, int o) |


## Functions Documentation

### function log_factorial

```
double log_factorial(
    double k
)
```


### function beta

```
double beta(
    double x,
    double y
)
```


### function binom

```
double binom(
    double n,
    double k
)
```


### function umvue_draw_n_mc

```
template <typename engine_type >
int umvue_draw_n_mc(
    double n_mc,
    engine_type engine
)
```


Unbiased likelihood estimator 


### function umvue_draw_n_mc

```
int umvue_draw_n_mc(
    double n_mc
)
```


### function umvue_draw_n_mc_threadsafe

```
int umvue_draw_n_mc_threadsafe(
    double n_mc
)
```


### function umvue_poisson_like

```
double umvue_poisson_like(
    int k,
    double b,
    int o,
    int n_mc,
    double n_exp
)
```


### function mle_poisson_loglike

```
double mle_poisson_loglike(
    double s,
    double b,
    int o
)
```


Regular likelihood estimator 






-------------------------------

Updated on 2025-02-12 at 15:36:39 +0000