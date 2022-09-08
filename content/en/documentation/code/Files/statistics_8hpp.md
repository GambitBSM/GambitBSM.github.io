---
title: "file Utils/statistics.hpp"

description: "[No description available]"

---

# file Utils/statistics.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::Stats](/documentation/code/namespaces/namespacegambit_1_1stats/)**  |

## Detailed Description


**Author**: Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 

**Date**: 2015 Aug

Declarations of statistical utilities.



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Declarations of statistical utilities.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///   
///  \author Pat Scott
///          (p.scott@imperial.ac.uk)
///  \date 2015 Aug
///
///  *********************************************

#include "gambit/Utils/util_types.hpp" 


namespace Gambit
{
  
  namespace Stats
  {

    /// Use a detection to compute a simple chi-square-like log likelihood, for the case when obs is Gaussian distributed.
    double gaussian_loglikelihood(double theory, double obs, double theoryerr, double obserr, bool profile_systematics);

    /// Use a detection to compute a simple chi-square-like log likelihood, for the case when obs is log-normal distributed.
    /// Version that takes absolute errors.
    double lognormal_loglikelihood(double theory, double obs, double theoryerr, double obserr, bool profile_systematics);

    /// Use a detection to compute a simple chi-square-like log likelihood, for the case when obs is log-normal distributed.
    /// Version that takes fractional (relative) errors.
    double lognormal_loglikelihood_relerror(double theory, double obs, double reltheoryerr, double relobserr, bool profile_systematics);
    
    /// Use a detection to compute a gaussian log-likelihood for an upper limit
    double gaussian_upper_limit(double theory, double obs, double theoryerr, double obserr, bool profile_systematics);

    /// Use a detection to compute a gaussian log-likelihood for a lower limit
    double gaussian_lower_limit(double theory, double obs, double theoryerr, double obserr, bool profile_systematics);

  }

}
```


-------------------------------

Updated on 2022-09-08 at 00:43:02 +0000
