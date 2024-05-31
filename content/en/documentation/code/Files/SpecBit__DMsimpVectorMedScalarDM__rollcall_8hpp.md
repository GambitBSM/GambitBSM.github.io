---
title: "file SpecBit/SpecBit_DMsimpVectorMedScalarDM_rollcall.hpp"

description: "[No description available]"

---

# file SpecBit/SpecBit_DMsimpVectorMedScalarDM_rollcall.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[CAPABILITY](/documentation/code/files/specbit__dmsimpvectormedscalardm__rollcall_8hpp/#define-capability)**  |
|  | **[FUNCTION](/documentation/code/files/specbit__dmsimpvectormedscalardm__rollcall_8hpp/#define-function)**  |
|  | **[FUNCTION](/documentation/code/files/specbit__dmsimpvectormedscalardm__rollcall_8hpp/#define-function)**  |

## Detailed Description


**Author**: The GAMBIT Collaboration 

**Date**: 03:28PM on June 07, 2022

Rollcall declarations for routines declared in [SpecBit_DMsimpVectorMedScalarDM.cpp](/documentation/code/files/specbit__dmsimpvectormedscalardm_8cpp/#file-src-specbit-dmsimpvectormedscalardm-cpp).

Authors (add name and date if you modify): 

 *** Automatically created by GUM *** 


------------------




## Macros Documentation

### define CAPABILITY

```
#define CAPABILITY DMsimpVectorMedScalarDM_spectrum
```


### define FUNCTION

```
#define FUNCTION get_DMsimpVectorMedScalarDM_spectrum
```


### define FUNCTION

```
#define FUNCTION get_DMsimpVectorMedScalarDM_spectrum
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Rollcall declarations for routines declared 
///  in SpecBit_DMsimpVectorMedScalarDM.cpp.
///
///  Authors (add name and date if you modify):    
///       *** Automatically created by GUM ***     
///                                                
///  \author The GAMBIT Collaboration             
///  \date 03:28PM on June 07, 2022
///                                                
///  ********************************************* 

#ifndef __SpecBit_DMsimpVectorMedScalarDM_hpp__
#define __SpecBit_DMsimpVectorMedScalarDM_hpp__

  // Spectrum object
  #define CAPABILITY DMsimpVectorMedScalarDM_spectrum
  START_CAPABILITY

    // Create simple object from SMInputs & new params.
    #define FUNCTION get_DMsimpVectorMedScalarDM_spectrum
    START_FUNCTION(Spectrum)
    DEPENDENCY(SMINPUTS, SMInputs)
    ALLOW_MODEL_DEPENDENCE(StandardModel_Higgs, DMsimpVectorMedScalarDM)
    MODEL_GROUP(higgs, (StandardModel_Higgs))
    MODEL_GROUP(DMsimpVectorMedScalarDM_group, (DMsimpVectorMedScalarDM))
    ALLOW_MODEL_COMBINATION(higgs, DMsimpVectorMedScalarDM_group)
    #undef FUNCTION
    
    // Map for Spectrum, for printing.
    #define FUNCTION get_DMsimpVectorMedScalarDM_spectrum_as_map
    START_FUNCTION(map_str_dbl)
    DEPENDENCY(DMsimpVectorMedScalarDM_spectrum, Spectrum)
    ALLOW_MODELS(DMsimpVectorMedScalarDM)
    #undef FUNCTION

  #undef CAPABILITY

#endif
```


-------------------------------

Updated on 2024-05-31 at 15:12:05 +0000
