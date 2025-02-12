---
title: "file SpectrumContents/Models/src/SpectrumContents/DMsimpVectorMedScalarDM.cpp"

description: "[No description available]"

---

# file SpectrumContents/Models/src/SpectrumContents/DMsimpVectorMedScalarDM.cpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[__DMsimpVectorMedScalarDM_contents_hpp__](/documentation/code/files/models_2src_2spectrumcontents_2dmsimpvectormedscalardm_8cpp/#define-dmsimpvectormedscalardm-contents-hpp)**  |

## Detailed Description


**Author**: The GAMBIT Collaboration 

**Date**: 03:28PM on June 07, 2022

Class defining the parameters that SubSpectrum objects providing DMsimpVectorMedScalarDM spectrum data must provide.

Authors (add name and date if you modify): 

 *** Automatically created by GUM *** 


------------------




## Macros Documentation

### define __DMsimpVectorMedScalarDM_contents_hpp__

```
#define __DMsimpVectorMedScalarDM_contents_hpp__ 
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Class defining the parameters that SubSpectrum
///  objects providing DMsimpVectorMedScalarDM
///  spectrum data must provide.
///
///  Authors (add name and date if you modify):    
///       *** Automatically created by GUM ***     
///                                                
///  \author The GAMBIT Collaboration             
///  \date 03:28PM on June 07, 2022
///                                                
///  ********************************************* 

#ifndef __DMsimpVectorMedScalarDM_contents_hpp__
#define __DMsimpVectorMedScalarDM_contents_hpp__

#include "gambit/Models/SpectrumContents/RegisteredSpectra.hpp"

namespace Gambit
{
  SpectrumContents::DMsimpVectorMedScalarDM::DMsimpVectorMedScalarDM()
  {
    setName("DMsimpVectorMedScalarDM");
    
    std::vector<int> scalar = initVector(1); // i.e. get(Par::Tag, "name")
    std::vector<int> m3x3  = initVector(3,3); // i.e. get(Par::Tag, "name", i, j)
    
    addParameter(Par::dimensionless, "gVXc", scalar, "DMINPUTS", 1);
    addParameter(Par::dimensionless, "gVq", scalar, "DMINPUTS", 2);
    addParameter(Par::mass1, "vev", scalar, "VEVS", 1);
    addParameter(Par::dimensionless, "g1", scalar, "GAUGE", 1);
    addParameter(Par::dimensionless, "g2", scalar, "GAUGE", 2);
    addParameter(Par::dimensionless, "g3", scalar, "GAUGE", 3);
    addParameter(Par::dimensionless, "sinW2", scalar, "SINTHETAW", 1);
    addParameter(Par::dimensionless, "Yd", m3x3, "YD", 1);
    addParameter(Par::dimensionless, "Yu", m3x3, "YU", 1);
    addParameter(Par::dimensionless, "Ye", m3x3, "YE", 1);
    addParameter(Par::Pole_Mass, "h0_1", scalar, "MASS", 25);
    addParameter(Par::Pole_Mass, "Xc", scalar, "MASS", 5000520);
    addParameter(Par::Pole_Mass, "Y1", scalar, "MASS", 5000001);
    
  } // namespace Models
} // namespace Gambit
#endif
```


-------------------------------

Updated on 2025-02-12 at 16:10:34 +0000
