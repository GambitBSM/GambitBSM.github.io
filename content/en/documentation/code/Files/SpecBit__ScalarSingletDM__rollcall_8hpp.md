---
title: "file SpecBit/SpecBit_ScalarSingletDM_rollcall.hpp"

description: "[No description available]"

---

# file SpecBit/SpecBit_ScalarSingletDM_rollcall.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[CAPABILITY](/documentation/code/files/specbit__scalarsingletdm__rollcall_8hpp/#define-capability)**  |
|  | **[FUNCTION](/documentation/code/files/specbit__scalarsingletdm__rollcall_8hpp/#define-function)**  |
|  | **[FUNCTION](/documentation/code/files/specbit__scalarsingletdm__rollcall_8hpp/#define-function)**  |
|  | **[CAPABILITY](/documentation/code/files/specbit__scalarsingletdm__rollcall_8hpp/#define-capability)**  |
|  | **[FUNCTION](/documentation/code/files/specbit__scalarsingletdm__rollcall_8hpp/#define-function)**  |
|  | **[FUNCTION](/documentation/code/files/specbit__scalarsingletdm__rollcall_8hpp/#define-function)**  |
|  | **[CAPABILITY](/documentation/code/files/specbit__scalarsingletdm__rollcall_8hpp/#define-capability)**  |
|  | **[FUNCTION](/documentation/code/files/specbit__scalarsingletdm__rollcall_8hpp/#define-function)**  |
|  | **[CAPABILITY](/documentation/code/files/specbit__scalarsingletdm__rollcall_8hpp/#define-capability)**  |

## Detailed Description


**Author**: 

  * Ben Farmer ([benjamin.farmer@fysik.su.se](mailto:benjamin.farmer@fysik.su.se)) 
  * James McKay ([j.mckay14@imperial.ac.uk](mailto:j.mckay14@imperial.ac.uk)) 


**Date**: 

  * 2014 Sep - Dec, 2015 Jan - Mar
  * 2016 Mar


Rollcall declarations for module functions contained in SpecBit_SingletDM.cpp



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define CAPABILITY

```
#define CAPABILITY ScalarSingletDM_Z2_spectrum
```


### define FUNCTION

```
#define FUNCTION get_ScalarSingletDM_Z2_spectrum
```


### define FUNCTION

```
#define FUNCTION get_ScalarSingletDM_Z2_spectrum
```


### define CAPABILITY

```
#define CAPABILITY ScalarSingletDM_Z2_spectrum
```


### define FUNCTION

```
#define FUNCTION get_ScalarSingletDM_Z2_spectrum
```


### define FUNCTION

```
#define FUNCTION get_ScalarSingletDM_Z2_spectrum
```


### define CAPABILITY

```
#define CAPABILITY ScalarSingletDM_Z2_spectrum
```


### define FUNCTION

```
#define FUNCTION get_ScalarSingletDM_Z2_spectrum
```


### define CAPABILITY

```
#define CAPABILITY ScalarSingletDM_Z2_spectrum
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Rollcall declarations for module functions
///  contained in SpecBit_SingletDM.cpp
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Ben Farmer
///          (benjamin.farmer@fysik.su.se)
///    \date 2014 Sep - Dec, 2015 Jan - Mar
///
///
///  \author James McKay
///          (j.mckay14@imperial.ac.uk)
///  \date 2016 Mar
///
///  *********************************************

#ifndef __SpecBit_ScalarSingletDM_hpp__
#define __SpecBit_ScalarSingletDM_hpp__

  // Spectrum object for ScalarSingletDM_Z2 model  (tree-level masses)
  #define CAPABILITY ScalarSingletDM_Z2_spectrum
  START_CAPABILITY

    // Create Spectrum object from SMInputs structs, SM Higgs parameters,
    // and the ScalarSingletDM_Z2 parameters
    #define FUNCTION get_ScalarSingletDM_Z2_spectrum
    START_FUNCTION(Spectrum)
    DEPENDENCY(SMINPUTS, SMInputs)
    ALLOW_MODEL_DEPENDENCE(StandardModel_Higgs, ScalarSingletDM_Z2)
    MODEL_GROUP(higgs,   (StandardModel_Higgs))
    MODEL_GROUP(singlet, (ScalarSingletDM_Z2))
    ALLOW_MODEL_COMBINATION(higgs, singlet)
    #undef FUNCTION

    #if(FS_MODEL_ScalarSingletDM_Z2_IS_BUILT)
    #define FUNCTION get_ScalarSingletDM_Z2_spectrum_pole
    START_FUNCTION(Spectrum)
    DEPENDENCY(SMINPUTS, SMInputs)
    ALLOW_MODEL_DEPENDENCE(StandardModel_Higgs_running, ScalarSingletDM_Z2_running)
    MODEL_GROUP(higgs_running,   (StandardModel_Higgs_running))
    MODEL_GROUP(singlet_running, (ScalarSingletDM_Z2_running))
    ALLOW_MODEL_COMBINATION(higgs_running, singlet_running)
    #undef FUNCTION
    #endif

    // Convert spectrum into a standard map so that it can be printed
    #define FUNCTION get_ScalarSingletDM_Z2_spectrum_as_map
    START_FUNCTION(map_str_dbl) // Just a string to double map. Can't have commas in macro input
    DEPENDENCY(ScalarSingletDM_Z2_spectrum, Spectrum)
    #undef FUNCTION

  #undef CAPABILITY


  #define CAPABILITY ScalarSingletDM_Z3_spectrum
  START_CAPABILITY

    #if(FS_MODEL_ScalarSingletDM_Z3_IS_BUILT)

    #define FUNCTION get_ScalarSingletDM_Z3_spectrum_pole
    START_FUNCTION(Spectrum)
    DEPENDENCY(SMINPUTS, SMInputs)
    ALLOW_MODEL_DEPENDENCE(StandardModel_Higgs_running, ScalarSingletDM_Z3_running)
    MODEL_GROUP(higgs,   (StandardModel_Higgs_running))
    MODEL_GROUP(singlet, (ScalarSingletDM_Z3_running))
    ALLOW_MODEL_COMBINATION(higgs, singlet)
    #undef FUNCTION
    #endif

    #define FUNCTION get_ScalarSingletDM_Z3_spectrum
    START_FUNCTION(Spectrum)
    DEPENDENCY(SMINPUTS, SMInputs)
    ALLOW_MODEL_DEPENDENCE(StandardModel_Higgs, ScalarSingletDM_Z3)
    MODEL_GROUP(higgs,   (StandardModel_Higgs))
    MODEL_GROUP(singlet, (ScalarSingletDM_Z3))
    ALLOW_MODEL_COMBINATION(higgs, singlet)
    #undef FUNCTION

    // Convert spectrum into a standard map so that it can be printed
    #define FUNCTION get_ScalarSingletDM_Z3_spectrum_as_map
    START_FUNCTION(map_str_dbl) // Just a string to double map. Can't have commas in macro input
    DEPENDENCY(ScalarSingletDM_Z3_spectrum, Spectrum)
    #undef FUNCTION

  #undef CAPABILITY


  // Generalised Higgs couplings
  #define CAPABILITY Higgs_Couplings

    #define FUNCTION ScalarSingletDM_higgs_couplings_pwid
    START_FUNCTION(HiggsCouplingsTable)
    DEPENDENCY(Reference_SM_Higgs_decay_rates, DecayTable::Entry)
    DEPENDENCY(Higgs_decay_rates, DecayTable::Entry)
    MODEL_CONDITIONAL_DEPENDENCY(ScalarSingletDM_Z2_spectrum, Spectrum, ScalarSingletDM_Z2, ScalarSingletDM_Z2_running)
    MODEL_CONDITIONAL_DEPENDENCY(ScalarSingletDM_Z3_spectrum, Spectrum, ScalarSingletDM_Z3, ScalarSingletDM_Z3_running)
    ALLOW_MODELS(ScalarSingletDM_Z2, ScalarSingletDM_Z2_running, ScalarSingletDM_Z3, ScalarSingletDM_Z3_running)
    #undef FUNCTION

  #undef CAPABILITY

  // Find scale at which spectrum becomes non-perturbative
  #define CAPABILITY scale_of_nonperturbativity
  START_CAPABILITY
#if(FS_MODEL_ScalarSingletDM_Z3_IS_BUILT)
    #define FUNCTION find_non_perturb_scale_ScalarSingletDM_Z3
    START_FUNCTION(double)
    DEPENDENCY(ScalarSingletDM_Z3_spectrum, Spectrum)
    ALLOW_MODELS(ScalarSingletDM_Z3_running)
    #undef FUNCTION
#endif

#if(FS_MODEL_ScalarSingletDM_Z2_IS_BUILT)
    #define FUNCTION find_non_perturb_scale_ScalarSingletDM_Z2
    START_FUNCTION(double)
    DEPENDENCY(ScalarSingletDM_Z2_spectrum, Spectrum)
    ALLOW_MODELS(ScalarSingletDM_Z2,ScalarSingletDM_Z2_running)
    #undef FUNCTION
#endif

  #undef CAPABILITY


#endif
```


-------------------------------

Updated on 2024-05-31 at 15:12:05 +0000
