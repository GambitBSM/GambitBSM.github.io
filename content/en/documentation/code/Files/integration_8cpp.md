---
title: "file src/integration.cpp"

description: "[No description available]"

---

# file src/integration.cpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::Utils](/documentation/code/namespaces/namespacegambit_1_1utils/)**  |

## Detailed Description


**Author**: 

  * Anders Kvellestad ([anders.kvellestad@fys.uio.no](mailto:anders.kvellestad@fys.uio.no)) 
  * Tomas Gonzalo ([tomas.gonzalo@monash.edu](mailto:tomas.gonzalo@monash.edu)) 


**Date**: 

  * 2018 Jan
  * 2020 Feb


Definition of functions for numerical integration



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Definition of functions for numerical integration
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Anders Kvellestad
///          (anders.kvellestad@fys.uio.no)
///  \date 2018 Jan
///
///  \author Tomas Gonzalo
///          (tomas.gonzalo@monash.edu)
///  \date 2020 Feb
///
///  *********************************************

#include "gambit/Utils/integration.hpp"
#include <gsl/gsl_integration.h>
#include <functional>

namespace Gambit
{

  namespace Utils
  {

    /// Unwrapper for passing std::function to GSL integrator
    /// Based on example from https://martin-ueding.de/articles/cpp-lambda-into-gsl/index.html
    double unwrap(double x, void *p)
    {
      auto fp = static_cast<std::function<double(double)> *>(p);
      return (*fp)(x);
    }

    /// Integrate a std::function using GSL cquad
    double integrate_cquad(std::function<double(double)> ftor, double a, double b, double abseps, double releps)
    {

      double result = 0.0;
      gsl_integration_cquad_workspace * gsl_ws = gsl_integration_cquad_workspace_alloc(100);

      gsl_function F;
      F.function = unwrap;
      F.params = &ftor;

      gsl_integration_cquad(&F, a, b, abseps, releps, gsl_ws, &result, NULL, NULL);
      gsl_integration_cquad_workspace_free(gsl_ws);

      // Check result
      if (Utils::isnan(result))
      {
        invalid_point().raise("Integration returned NaN.");
      }

      return result;
    }



  }

}
```


-------------------------------

Updated on 2022-09-08 at 02:23:02 +0000
