---
title: "file SpectrumContents/SpectrumContents/SubGeVDM.cpp"

description: "[No description available]"

---

# file SpectrumContents/SpectrumContents/SubGeVDM.cpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |

## Detailed Description


**Author**: Felix Kahlhoefer ([kahlhoefer@kit.edu](mailto:kahlhoefer@kit.edu)) 

**Date**: 2022 June

Class defining the parameters that SubSpectrum objects providing SubGeVDM spectrum data must provide.

Authors (add name and date if you modify): 

 *** Automatically created by GUM *** 


------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Class defining the parameters that SubSpectrum
///  objects providing SubGeVDM
///  spectrum data must provide.
///
///  Authors (add name and date if you modify):    
///       *** Automatically created by GUM ***     
///                                                
///  \author Felix Kahlhoefer
///          (kahlhoefer@kit.edu)
///  \date 2022 June
///                                                
///  ********************************************* 

#include "gambit/Models/SpectrumContents/RegisteredSpectra.hpp"

namespace Gambit
{
  SpectrumContents::SubGeVDM::SubGeVDM()
  {
    setName("SubGeVDM");
    
    std::vector<int> scalar = initVector(1); // i.e. get(Par::Tag, "name")
    std::vector<int> m3x3   = initVector(3,3); // i.e. get(Par::Tag, "name", i, j)
 
    addParameter(Par::Pole_Mass, "DM");
    addParameter(Par::Pole_Mass, "Ap");
    addParameter(Par::dimensionless, "gDM");
    addParameter(Par::dimensionless, "kappa");

    addParameter(Par::mass1, "vev");

    addParameter(Par::dimensionless, "g1");
    addParameter(Par::dimensionless, "g2");
    addParameter(Par::dimensionless, "g3");

    addParameter(Par::dimensionless, "sinW2");

    addParameter(Par::dimensionless, "Yd", m3x3);
    addParameter(Par::dimensionless, "Yu", m3x3);
    addParameter(Par::dimensionless, "Ye", m3x3);
    
  } // namespace Models
} // namespace Gambit
```


-------------------------------

Updated on 2025-02-12 at 16:10:34 +0000
