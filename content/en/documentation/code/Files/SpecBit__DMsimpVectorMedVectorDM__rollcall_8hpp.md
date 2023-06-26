---
title: "file SpecBit/SpecBit_DMsimpVectorMedVectorDM_rollcall.hpp"

description: "[No description available]"

---

# file SpecBit/SpecBit_DMsimpVectorMedVectorDM_rollcall.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[CAPABILITY](/documentation/code/files/specbit__dmsimpvectormedvectordm__rollcall_8hpp/#define-capability)**  |
|  | **[FUNCTION](/documentation/code/files/specbit__dmsimpvectormedvectordm__rollcall_8hpp/#define-function)**  |
|  | **[FUNCTION](/documentation/code/files/specbit__dmsimpvectormedvectordm__rollcall_8hpp/#define-function)**  |
|  | **[CAPABILITY](/documentation/code/files/specbit__dmsimpvectormedvectordm__rollcall_8hpp/#define-capability)**  |
|  | **[FUNCTION](/documentation/code/files/specbit__dmsimpvectormedvectordm__rollcall_8hpp/#define-function)**  |

## Detailed Description


**Author**: The GAMBIT Collaboration 

**Date**: 03:49PM on February 07, 2023

Rollcall declarations for routines declared in [SpecBit_DMsimpVectorMedVectorDM.cpp](/documentation/code/files/specbit__dmsimpvectormedvectordm_8cpp/#file-src-specbit-dmsimpvectormedvectordm-cpp).

Authors (add name and date if you modify): 

 *** Automatically created by GUM *** 


------------------




## Macros Documentation

### define CAPABILITY

```
#define CAPABILITY DMsimpVectorMedVectorDM_spectrum
```


### define FUNCTION

```
#define FUNCTION get_DMsimpVectorMedVectorDM_spectrum
```


### define FUNCTION

```
#define FUNCTION get_DMsimpVectorMedVectorDM_spectrum
```


### define CAPABILITY

```
#define CAPABILITY DMsimpVectorMedVectorDM_spectrum
```


### define FUNCTION

```
#define FUNCTION get_DMsimpVectorMedVectorDM_spectrum
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Rollcall declarations for routines declared 
///  in SpecBit_DMsimpVectorMedVectorDM.cpp.
///
///  Authors (add name and date if you modify):    
///       *** Automatically created by GUM ***     
///                                                
///  \author The GAMBIT Collaboration             
///  \date 03:49PM on February 07, 2023
///                                                
///  ********************************************* 

#ifndef __SpecBit_DMsimpVectorMedVectorDM_hpp__
#define __SpecBit_DMsimpVectorMedVectorDM_hpp__

  // Spectrum object
  #define CAPABILITY DMsimpVectorMedVectorDM_spectrum
  START_CAPABILITY

    // Create simple object from SMInputs & new params.
    #define FUNCTION get_DMsimpVectorMedVectorDM_spectrum
    START_FUNCTION(Spectrum)
    DEPENDENCY(SMINPUTS, SMInputs)
    ALLOW_MODEL_DEPENDENCE(StandardModel_Higgs, DMsimpVectorMedVectorDM)
    MODEL_GROUP(higgs, (StandardModel_Higgs))
    MODEL_GROUP(DMsimpVectorMedVectorDM_group, (DMsimpVectorMedVectorDM))
    ALLOW_MODEL_COMBINATION(higgs, DMsimpVectorMedVectorDM_group)
    #undef FUNCTION

    // Map for Spectrum, for printing.
    #define FUNCTION get_DMsimpVectorMedVectorDM_spectrum_as_map
    START_FUNCTION(map_str_dbl)
    DEPENDENCY(DMsimpVectorMedVectorDM_spectrum, Spectrum)
    ALLOW_MODELS(DMsimpVectorMedVectorDM)
    #undef FUNCTION

  #undef CAPABILITY

  // Test whether the decay width becomes nonperturbative
  #define CAPABILITY DecayWidthPerturbativity_DMsimpVectorMedVectorDM
    #define FUNCTION DecayWidthPerturbativity_DMsimpVectorMedVectorDM
    START_FUNCTION(double)
    DEPENDENCY(DMsimpVectorMedVectorDM_spectrum, Spectrum)
    DEPENDENCY(Y1_decay_rates, DecayTable::Entry)
    ALLOW_MODELS(DMsimpVectorMedVectorDM)
    #undef FUNCTION
  #undef CAPABILITY

#endif
```


-------------------------------

Updated on 2023-06-26 at 21:36:53 +0000
