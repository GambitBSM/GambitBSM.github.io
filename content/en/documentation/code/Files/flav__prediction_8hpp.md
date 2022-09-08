---
title: "file Elements/flav_prediction.hpp"

description: "[No description available]"

---

# file Elements/flav_prediction.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |

## Classes

|                | Name           |
| -------------- | -------------- |
| struct | **[Gambit::flav_prediction](/documentation/code/classes/structgambit_1_1flav__prediction/)** <br>Flavour observables structure holding central values and covariances.  |

## Detailed Description


**Author**: 

  * Markus Prim ([markus.prim@kit.edu](mailto:markus.prim@kit.edu)) 
  * Pat Scott ([pat.scott@uq.edu.au](mailto:pat.scott@uq.edu.au)) 


**Date**: 

  * 2019 Nov 2020 Feb
  * 2022 May


Flavour prediction container type



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Flavour prediction container type
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Markus Prim
///          (markus.prim@kit.edu)
///  \date 2019 Nov
///        2020 Feb
///
///  \author Pat Scott
///          (pat.scott@uq.edu.au)
///  \date 2022 May
///
///  *********************************************

#pragma once

#include <string>
#include <map>


namespace Gambit
{

  /// Maps for holding observables and covariance matrix.
  typedef std::map<const std::string, double> flav_observable_map;
  typedef std::map<const std::string, std::map<const std::string, double>> flav_covariance_map;

  /// Flavour observables structure holding central values and covariances.
  struct flav_prediction
  {
    flav_observable_map central_values;
    flav_covariance_map covariance;
  };

}
```


-------------------------------

Updated on 2022-09-08 at 03:17:36 +0000
