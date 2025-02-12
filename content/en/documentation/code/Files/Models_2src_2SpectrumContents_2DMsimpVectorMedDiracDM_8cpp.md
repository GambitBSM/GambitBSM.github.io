---
title: "file SpectrumContents/Models/src/SpectrumContents/DMsimpVectorMedDiracDM.cpp"

description: "[No description available]"

---

# file SpectrumContents/Models/src/SpectrumContents/DMsimpVectorMedDiracDM.cpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[__DMsimpVectorMedDiracDM_contents_hpp__](/documentation/code/files/models_2src_2spectrumcontents_2dmsimpvectormeddiracdm_8cpp/#define-dmsimpvectormeddiracdm-contents-hpp)**  |

## Detailed Description


**Author**: The GAMBIT Collaboration 

**Date**: 03:26PM on June 07, 2022

Class defining the parameters that SubSpectrum objects providing DMsimpVectorMedDiracDM spectrum data must provide.

Authors (add name and date if you modify): 

 *** Automatically created by GUM *** 


------------------




## Macros Documentation

### define __DMsimpVectorMedDiracDM_contents_hpp__

```
#define __DMsimpVectorMedDiracDM_contents_hpp__ 
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Class defining the parameters that SubSpectrum
///  objects providing DMsimpVectorMedDiracDM
///  spectrum data must provide.
///
///  Authors (add name and date if you modify):    
///       *** Automatically created by GUM ***     
///                                                
///  \author The GAMBIT Collaboration             
///  \date 03:26PM on June 07, 2022
///                                                
///  ********************************************* 

#ifndef __DMsimpVectorMedDiracDM_contents_hpp__
#define __DMsimpVectorMedDiracDM_contents_hpp__

#include "gambit/Models/SpectrumContents/RegisteredSpectra.hpp"

namespace Gambit
{
  SpectrumContents::DMsimpVectorMedDiracDM::DMsimpVectorMedDiracDM()
  {
    setName("DMsimpVectorMedDiracDM");
    
    std::vector<int> scalar = initVector(1); // i.e. get(Par::Tag, "name")
    std::vector<int> m3x3  = initVector(3,3); // i.e. get(Par::Tag, "name", i, j)
    
    addParameter(Par::dimensionless, "gVXd", scalar, "DMINPUTS", 1);
    addParameter(Par::dimensionless, "gAXd", scalar, "DMINPUTS", 2);
    addParameter(Par::dimensionless, "gVq", scalar, "DMINPUTS", 3);
    addParameter(Par::mass1, "vev", scalar, "VEVS", 1);
    addParameter(Par::dimensionless, "g1", scalar, "GAUGE", 1);
    addParameter(Par::dimensionless, "g2", scalar, "GAUGE", 2);
    addParameter(Par::dimensionless, "g3", scalar, "GAUGE", 3);
    addParameter(Par::dimensionless, "sinW2", scalar, "SINTHETAW", 1);
    addParameter(Par::dimensionless, "Yd", m3x3, "YD", 1);
    addParameter(Par::dimensionless, "Yu", m3x3, "YU", 1);
    addParameter(Par::dimensionless, "Ye", m3x3, "YE", 1);
    addParameter(Par::Pole_Mass, "h0_1", scalar, "MASS", 25);
    addParameter(Par::Pole_Mass, "Xd", scalar, "MASS", 5000521);
    addParameter(Par::Pole_Mass, "Y1", scalar, "MASS", 5000001);
    
  } // namespace Models
} // namespace Gambit
#endif
```


-------------------------------

Updated on 2025-02-12 at 15:36:41 +0000
