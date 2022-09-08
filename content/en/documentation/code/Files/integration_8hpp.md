---
title: "file Utils/integration.hpp"

description: "[No description available]"

---

# file Utils/integration.hpp

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


Helper functions for numerical integration



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Helper functions for numerical integration
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

#include "gambit/Utils/util_functions.hpp"
#include <functional>

namespace Gambit
{

  namespace Utils
  {

    /// Unwrapper for passing std::function to GSL integrator
    /// Based on example from https://martin-ueding.de/articles/cpp-lambda-into-gsl/index.html
    double unwrap(double x, void *p);
 
    /// Integrate a std::function using GSL cquad
    double integrate_cquad(std::function<double(double)> ftor, double a, double b, double abseps, double releps);

  }

}
```


-------------------------------

Updated on 2022-09-08 at 03:17:34 +0000
