---
title: "file ColliderBit/PoissonCalculators.hpp"

description: "[No description available]"

---

# file ColliderBit/PoissonCalculators.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::ColliderBit](/documentation/code/namespaces/namespacegambit_1_1colliderbit/)**  |
| **[Gambit::ColliderBit::PoissonCalculators](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1poissoncalculators/)**  |

## Detailed Description


**Author**: 

  * Chris Chang 
  * Andrew Fowlie 


**Date**: 

  * 2024 Oct
  * 2024 Oct


Functions for working with an unbiased Poisson likelihood estimator.



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Functions for working with an unbiased 
///  Poisson likelihood estimator.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Chris Chang
///  \date   2024 Oct
///
///  \author Andrew Fowlie
///  \date   2024 Oct
///
///  *********************************************

#pragma once

/**
Unbiased likelihood estimator
*/

#include <iostream>
#include <algorithm>
#include <cmath>
#include <random>

#include "gambit/Utils/threadsafe_rng.hpp"

namespace Gambit
{
  namespace ColliderBit
  {
    namespace PoissonCalculators
    {

      double log_factorial(double k);
      double beta(double x, double y);
      double binom(double n, double k);

      template <typename engine_type>
      int umvue_draw_n_mc(double n_mc, engine_type engine);

      int umvue_draw_n_mc(double n_mc);

      int umvue_draw_n_mc_threadsafe(double n_mc);

      double umvue_poisson_like(int k, double b, int o, int n_mc, double n_exp);

      double mle_poisson_loglike(double s, double b, int o);

    }  // end namespace PoissonCalculators
  }  // end namespace ColliderBit
}  // end namespace Gambit
```


-------------------------------

Updated on 2025-02-12 at 15:36:42 +0000
