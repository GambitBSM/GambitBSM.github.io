---
title: "file SpecBit/SpecBit_SubGeVDM_rollcall.hpp"

description: "[No description available]"

---

# file SpecBit/SpecBit_SubGeVDM_rollcall.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[CAPABILITY](/documentation/code/files/specbit__subgevdm__rollcall_8hpp/#define-capability)**  |
|  | **[FUNCTION](/documentation/code/files/specbit__subgevdm__rollcall_8hpp/#define-function)**  |
|  | **[FUNCTION](/documentation/code/files/specbit__subgevdm__rollcall_8hpp/#define-function)**  |

## Detailed Description


**Author**: Felix Kahlhoefer ([kahlhoefer@kit.edu](mailto:kahlhoefer@kit.edu)) 

**Date**: 2022 May

Rollcall declarations for module functions contained in [SpecBit_SubGeVDM.cpp](/documentation/code/files/specbit__subgevdm_8cpp/#file-src-specbit-subgevdm-cpp)



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define CAPABILITY

```
#define CAPABILITY SubGeVDM_spectrum
```


### define FUNCTION

```
#define FUNCTION get_SubGeVDM_spectrum
```


### define FUNCTION

```
#define FUNCTION get_SubGeVDM_spectrum
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Rollcall declarations for module functions
///  contained in SpecBit_SubGeVDM.cpp
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Felix Kahlhoefer
///          (kahlhoefer@kit.edu)
///    \date 2022 May
///
///  *********************************************

#ifndef __SpecBit_SubGeVDM_hpp__
#define __SpecBit_SubGeVDM_hpp__

  // Spectrum object for SubGeVDM model 
  #define CAPABILITY SubGeVDM_spectrum
  START_CAPABILITY

    // Create simple object from SMInputs & new params.
    #define FUNCTION get_SubGeVDM_spectrum
    START_FUNCTION(Spectrum)
    DEPENDENCY(SMINPUTS, SMInputs)
    ALLOW_MODEL_DEPENDENCE(StandardModel_Higgs, SubGeVDM_scalar, SubGeVDM_fermion)
    MODEL_GROUP(higgs,   (StandardModel_Higgs))
    MODEL_GROUP(SubGeVDM_group, (SubGeVDM_scalar, SubGeVDM_fermion))
    ALLOW_MODEL_COMBINATION(higgs, SubGeVDM_group)
    #undef FUNCTION

    // Convert spectrum into a standard map so that it can be printed
    #define FUNCTION get_SubGeVDM_spectrum_as_map
    START_FUNCTION(map_str_dbl) // Just a string to double map. Can't have commas in macro input
    DEPENDENCY(SubGeVDM_spectrum, Spectrum)
    #undef FUNCTION

  #undef CAPABILITY

#endif
```


-------------------------------

Updated on 2025-02-12 at 15:36:40 +0000
