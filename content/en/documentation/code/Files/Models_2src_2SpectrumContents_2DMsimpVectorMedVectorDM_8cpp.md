---
title: "file SpectrumContents/Models/src/SpectrumContents/DMsimpVectorMedVectorDM.cpp"

description: "[No description available]"

---

# file SpectrumContents/Models/src/SpectrumContents/DMsimpVectorMedVectorDM.cpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[__DMsimpVectorMedVectorDM_contents_hpp__](/documentation/code/files/models_2src_2spectrumcontents_2dmsimpvectormedvectordm_8cpp/#define-dmsimpvectormedvectordm-contents-hpp)**  |

## Detailed Description


**Author**: The GAMBIT Collaboration 

**Date**: 03:49PM on February 07, 2023

Class defining the parameters that SubSpectrum objects providing DMsimpVectorMedVectorDM spectrum data must provide.

Authors (add name and date if you modify): 

 *** Automatically created by GUM *** 


------------------




## Macros Documentation

### define __DMsimpVectorMedVectorDM_contents_hpp__

```
#define __DMsimpVectorMedVectorDM_contents_hpp__ 
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Class defining the parameters that SubSpectrum
///  objects providing DMsimpVectorMedVectorDM
///  spectrum data must provide.
///
///  Authors (add name and date if you modify):    
///       *** Automatically created by GUM ***     
///                                                
///  \author The GAMBIT Collaboration             
///  \date 03:49PM on February 07, 2023
///                                                
///  ********************************************* 

#ifndef __DMsimpVectorMedVectorDM_contents_hpp__
#define __DMsimpVectorMedVectorDM_contents_hpp__

#include "gambit/Models/SpectrumContents/RegisteredSpectra.hpp"

namespace Gambit
{
  SpectrumContents::DMsimpVectorMedVectorDM::DMsimpVectorMedVectorDM()
  {
    setName("DMsimpVectorMedVectorDM");

    std::vector<int> scalar = initVector(1); // i.e. get(Par::Tag, "name")
    std::vector<int> m3x3  = initVector(3,3); // i.e. get(Par::Tag, "name", i, j)

    addParameter(Par::dimensionless, "gVXv", scalar, "DMINT", 1);
    addParameter(Par::dimensionless, "gVq", scalar, "DMINT", 2);
    addParameter(Par::mass1, "vev", scalar, "VEVS", 1);
    addParameter(Par::dimensionless, "g1", scalar, "GAUGE", 1);
    addParameter(Par::dimensionless, "g2", scalar, "GAUGE", 2);
    addParameter(Par::dimensionless, "g3", scalar, "GAUGE", 3);
    addParameter(Par::dimensionless, "sinW2", scalar, "SINTHETAW", 1);
    addParameter(Par::dimensionless, "Yd", m3x3, "YD", 1);
    addParameter(Par::dimensionless, "Yu", m3x3, "YU", 1);
    addParameter(Par::dimensionless, "Ye", m3x3, "YE", 1);
    addParameter(Par::Pole_Mass, "h0_1", scalar, "MASS", 25);
    addParameter(Par::Pole_Mass, "~Xv", scalar, "MASS", 5000523);
    addParameter(Par::Pole_Mass, "Y1", scalar, "MASS", 5000001);

  } // namespace Models
} // namespace Gambit
#endif
```


-------------------------------

Updated on 2024-07-18 at 13:53:33 +0000
