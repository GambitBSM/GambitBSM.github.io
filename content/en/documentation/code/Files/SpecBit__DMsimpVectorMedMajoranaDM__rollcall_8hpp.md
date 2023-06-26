---
title: "file SpecBit/SpecBit_DMsimpVectorMedMajoranaDM_rollcall.hpp"

description: "[No description available]"

---

# file SpecBit/SpecBit_DMsimpVectorMedMajoranaDM_rollcall.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[CAPABILITY](/documentation/code/files/specbit__dmsimpvectormedmajoranadm__rollcall_8hpp/#define-capability)**  |
|  | **[FUNCTION](/documentation/code/files/specbit__dmsimpvectormedmajoranadm__rollcall_8hpp/#define-function)**  |
|  | **[FUNCTION](/documentation/code/files/specbit__dmsimpvectormedmajoranadm__rollcall_8hpp/#define-function)**  |
|  | **[CAPABILITY](/documentation/code/files/specbit__dmsimpvectormedmajoranadm__rollcall_8hpp/#define-capability)**  |
|  | **[FUNCTION](/documentation/code/files/specbit__dmsimpvectormedmajoranadm__rollcall_8hpp/#define-function)**  |

## Detailed Description


**Author**: 

  * The GAMBIT Collaboration 
  * Chris Chang 


**Date**: 

  * 03:27PM on June 07, 2022
  * Jun 2022


Rollcall declarations for routines declared in [SpecBit_DMsimpVectorMedMajoranaDM.cpp](/documentation/code/files/specbit__dmsimpvectormedmajoranadm_8cpp/#file-src-specbit-dmsimpvectormedmajoranadm-cpp).

Authors (add name and date if you modify): 

 *** Automatically created by GUM *** 


------------------




## Macros Documentation

### define CAPABILITY

```
#define CAPABILITY DMsimpVectorMedMajoranaDM_spectrum
```


### define FUNCTION

```
#define FUNCTION get_DMsimpVectorMedMajoranaDM_spectrum
```


### define FUNCTION

```
#define FUNCTION get_DMsimpVectorMedMajoranaDM_spectrum
```


### define CAPABILITY

```
#define CAPABILITY DMsimpVectorMedMajoranaDM_spectrum
```


### define FUNCTION

```
#define FUNCTION get_DMsimpVectorMedMajoranaDM_spectrum
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Rollcall declarations for routines declared 
///  in SpecBit_DMsimpVectorMedMajoranaDM.cpp.
///
///  Authors (add name and date if you modify):    
///       *** Automatically created by GUM ***     
///                                                
///  \author The GAMBIT Collaboration             
///  \date 03:27PM on June 07, 2022
///
///  \author Chris Chang
///  \date Jun 2022
///                                                
///  ********************************************* 

#ifndef __SpecBit_DMsimpVectorMedMajoranaDM_hpp__
#define __SpecBit_DMsimpVectorMedMajoranaDM_hpp__

  // Spectrum object
  #define CAPABILITY DMsimpVectorMedMajoranaDM_spectrum
  START_CAPABILITY

    // Create simple object from SMInputs & new params.
    #define FUNCTION get_DMsimpVectorMedMajoranaDM_spectrum
    START_FUNCTION(Spectrum)
    DEPENDENCY(SMINPUTS, SMInputs)
    ALLOW_MODEL_DEPENDENCE(StandardModel_Higgs, DMsimpVectorMedMajoranaDM)
    MODEL_GROUP(higgs, (StandardModel_Higgs))
    MODEL_GROUP(DMsimpVectorMedMajoranaDM_group, (DMsimpVectorMedMajoranaDM))
    ALLOW_MODEL_COMBINATION(higgs, DMsimpVectorMedMajoranaDM_group)
    #undef FUNCTION
    
    // Map for Spectrum, for printing.
    #define FUNCTION get_DMsimpVectorMedMajoranaDM_spectrum_as_map
    START_FUNCTION(map_str_dbl)
    DEPENDENCY(DMsimpVectorMedMajoranaDM_spectrum, Spectrum)
    ALLOW_MODELS(DMsimpVectorMedMajoranaDM)
    #undef FUNCTION

  #undef CAPABILITY
  
  // Test against a known unitarity bound
  #define CAPABILITY Unitarity_Bound_DMsimpVectorMedMajoranaDM
    #define FUNCTION Unitarity_Bound_DMsimpVectorMedMajoranaDM
    START_FUNCTION(double)
    DEPENDENCY(DMsimpVectorMedMajoranaDM_spectrum, Spectrum)
    ALLOW_MODELS(DMsimpVectorMedMajoranaDM)
    #undef FUNCTION
  #undef CAPABILITY

#endif
```


-------------------------------

Updated on 2023-06-26 at 21:36:53 +0000
