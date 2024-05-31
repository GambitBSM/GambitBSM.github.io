---
title: "file SpecBit/SpecBit_DMsimpVectorMedDiracDM_rollcall.hpp"

description: "[No description available]"

---

# file SpecBit/SpecBit_DMsimpVectorMedDiracDM_rollcall.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[CAPABILITY](/documentation/code/files/specbit__dmsimpvectormeddiracdm__rollcall_8hpp/#define-capability)**  |
|  | **[FUNCTION](/documentation/code/files/specbit__dmsimpvectormeddiracdm__rollcall_8hpp/#define-function)**  |
|  | **[FUNCTION](/documentation/code/files/specbit__dmsimpvectormeddiracdm__rollcall_8hpp/#define-function)**  |
|  | **[CAPABILITY](/documentation/code/files/specbit__dmsimpvectormeddiracdm__rollcall_8hpp/#define-capability)**  |
|  | **[FUNCTION](/documentation/code/files/specbit__dmsimpvectormeddiracdm__rollcall_8hpp/#define-function)**  |

## Detailed Description


**Author**: 

  * The GAMBIT Collaboration 
  * Chris Chang 


**Date**: 

  * 03:26PM on June 07, 2022
  * Jun 2022


Rollcall declarations for routines declared in [SpecBit_DMsimpVectorMedDiracDM.cpp](/documentation/code/files/specbit__dmsimpvectormeddiracdm_8cpp/#file-src-specbit-dmsimpvectormeddiracdm-cpp).

Authors (add name and date if you modify): 

 *** Automatically created by GUM *** 


------------------




## Macros Documentation

### define CAPABILITY

```
#define CAPABILITY DMsimpVectorMedDiracDM_spectrum
```


### define FUNCTION

```
#define FUNCTION get_DMsimpVectorMedDiracDM_spectrum
```


### define FUNCTION

```
#define FUNCTION get_DMsimpVectorMedDiracDM_spectrum
```


### define CAPABILITY

```
#define CAPABILITY DMsimpVectorMedDiracDM_spectrum
```


### define FUNCTION

```
#define FUNCTION get_DMsimpVectorMedDiracDM_spectrum
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Rollcall declarations for routines declared 
///  in SpecBit_DMsimpVectorMedDiracDM.cpp.
///
///  Authors (add name and date if you modify):    
///       *** Automatically created by GUM ***     
///                                                
///  \author The GAMBIT Collaboration             
///  \date 03:26PM on June 07, 2022
///
///  \author Chris Chang
///  \date Jun 2022
///                                                
///  ********************************************* 

#ifndef __SpecBit_DMsimpVectorMedDiracDM_hpp__
#define __SpecBit_DMsimpVectorMedDiracDM_hpp__

  // Spectrum object
  #define CAPABILITY DMsimpVectorMedDiracDM_spectrum
  START_CAPABILITY

    // Create simple object from SMInputs & new params.
    #define FUNCTION get_DMsimpVectorMedDiracDM_spectrum
    START_FUNCTION(Spectrum)
    DEPENDENCY(SMINPUTS, SMInputs)
    ALLOW_MODEL_DEPENDENCE(StandardModel_Higgs, DMsimpVectorMedDiracDM)
    MODEL_GROUP(higgs, (StandardModel_Higgs))
    MODEL_GROUP(DMsimpVectorMedDiracDM_group, (DMsimpVectorMedDiracDM))
    ALLOW_MODEL_COMBINATION(higgs, DMsimpVectorMedDiracDM_group)
    #undef FUNCTION
    
    // Map for Spectrum, for printing.
    #define FUNCTION get_DMsimpVectorMedDiracDM_spectrum_as_map
    START_FUNCTION(map_str_dbl)
    DEPENDENCY(DMsimpVectorMedDiracDM_spectrum, Spectrum)
    ALLOW_MODELS(DMsimpVectorMedDiracDM)
    #undef FUNCTION

  #undef CAPABILITY
  
  // Test against a known unitarity bound
  #define CAPABILITY Unitarity_Bound_DMsimpVectorMedDiracDM
    #define FUNCTION Unitarity_Bound_DMsimpVectorMedDiracDM
    START_FUNCTION(double)
    DEPENDENCY(DMsimpVectorMedDiracDM_spectrum, Spectrum)
    ALLOW_MODELS(DMsimpVectorMedDiracDM)
    #undef FUNCTION
  #undef CAPABILITY

#endif
```


-------------------------------

Updated on 2024-05-31 at 15:12:05 +0000
