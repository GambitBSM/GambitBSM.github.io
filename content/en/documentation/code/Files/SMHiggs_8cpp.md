---
title: "file SpectrumContents/SMHiggs.cpp"

description: "[No description available]"

---

# file SpectrumContents/SMHiggs.cpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |

## Detailed Description


**Author**: Ben Farmer ([benjamin.farmer@fysik.su.se](mailto:benjamin.farmer@fysik.su.se)) 

**Date**: 2016 Feb

Class defining the parameters that SubSpectrum objects providing the Standard Model Higgs sector parameters must provide



------------------

Authors:



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Class defining the parameters that SubSpectrum
///  objects providing the Standard Model Higgs
///  sector parameters must provide
///
///  *********************************************
///
///  Authors:
///  <!-- add name and date if you modify -->
///
///  \author Ben Farmer
///          (benjamin.farmer@fysik.su.se)
///  \date 2016 Feb
///
///  *********************************************

#include "gambit/Models/SpectrumContents/RegisteredSpectra.hpp"

namespace Gambit {

  /// Only have to define the constructor
  SpectrumContents::SMHiggs::SMHiggs()
  {
     setName("SMHiggs");
     addParameter(Par::mass1,     "vev");
     addParameter(Par::Pole_Mass, "h0_1" );
  }

}
```


-------------------------------

Updated on 2022-09-07 at 23:22:09 +0000
