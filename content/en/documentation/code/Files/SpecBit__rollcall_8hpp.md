---
title: "file SpecBit/SpecBit_rollcall.hpp"

description: "[No description available]"

---

# file SpecBit/SpecBit_rollcall.hpp

[No description available] [More...](#detailed-description)

## Functions

|                | Name           |
| -------------- | -------------- |
| [START_CAPABILITY](/documentation/code/files/module__macros__incore_8hpp/#define-module-macros-incore-hpp-start-capability) | **[QUICK_FUNCTION](/documentation/code/files/specbit__rollcall_8hpp/#function-specbit-rollcall-hpp-quick-function)**([MODULE](/documentation/code/files/examplebit__b__rollcall_8hpp/#define-examplebit-b-rollcall-hpp-module) , SM_spectrum , OLD_CAPABILITY , convert_MSSM_to_SM , Spectrum , (MSSM63atQ, MSSM63atMGUT) , (MSSM_spectrum, Spectrum) )<br>Module function declarations for [SpecBit_SM.cpp]().  |

## Attributes

|                | Name           |
| -------------- | -------------- |
| [START_CAPABILITY](/documentation/code/files/module__macros__incore_8hpp/#define-module-macros-incore-hpp-start-capability) | **[SM_spectrum](/documentation/code/files/specbit__rollcall_8hpp/#variable-specbit-rollcall-hpp-sm-spectrum)**  |
| [START_CAPABILITY](/documentation/code/files/module__macros__incore_8hpp/#define-module-macros-incore-hpp-start-capability) | **[OLD_CAPABILITY](/documentation/code/files/specbit__rollcall_8hpp/#variable-specbit-rollcall-hpp-old-capability)**  |
| [START_CAPABILITY](/documentation/code/files/module__macros__incore_8hpp/#define-module-macros-incore-hpp-start-capability) | **[convert_NMSSM_to_SM](/documentation/code/files/specbit__rollcall_8hpp/#variable-specbit-rollcall-hpp-convert-nmssm-to-sm)**  |
| [START_CAPABILITY](/documentation/code/files/module__macros__incore_8hpp/#define-module-macros-incore-hpp-start-capability) | **[Spectrum](/documentation/code/files/specbit__rollcall_8hpp/#variable-specbit-rollcall-hpp-spectrum)**  |
| [START_CAPABILITY](/documentation/code/files/module__macros__incore_8hpp/#define-module-macros-incore-hpp-start-capability) | **[NMSSM_does_not_exist_yet](/documentation/code/files/specbit__rollcall_8hpp/#variable-specbit-rollcall-hpp-nmssm-does-not-exist-yet)**  |
| [START_CAPABILITY](/documentation/code/files/module__macros__incore_8hpp/#define-module-macros-incore-hpp-start-capability) | **[NMSSM_spectrum](/documentation/code/files/specbit__rollcall_8hpp/#variable-specbit-rollcall-hpp-nmssm-spectrum)**  |

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODULE](/documentation/code/files/specbit__rollcall_8hpp/#define-specbit-rollcall-hpp-module)**  |
|  | **[REFERENCE](/documentation/code/files/specbit__rollcall_8hpp/#define-specbit-rollcall-hpp-reference)**  |
|  | **[CAPABILITY](/documentation/code/files/specbit__rollcall_8hpp/#define-specbit-rollcall-hpp-capability)**  |

## Detailed Description


**Author**: 

  * Ben Farmer ([benjamin.farmer@fysik.su.se](mailto:benjamin.farmer@fysik.su.se)) 
  * Ankit Beniwal ([ankit.beniwal@adelaide.edu.au](mailto:ankit.beniwal@adelaide.edu.au)) 


**Date**: 

  * 2014 Sep - Dec, 2015 Jan - Mar
  * 2016 Aug


Rollcall header for module SpecBit

These functions link ModelParameters to Spectrum objects in various ways.



------------------

Authors (add name and date if you modify):



------------------


## Functions Documentation

### function QUICK_FUNCTION

```
START_CAPABILITY QUICK_FUNCTION(
    MODULE ,
    SM_spectrum ,
    OLD_CAPABILITY ,
    convert_MSSM_to_SM ,
    Spectrum ,
    (MSSM63atQ, MSSM63atMGUT) ,
    (MSSM_spectrum, Spectrum) 
)
```

Module function declarations for [SpecBit_SM.cpp](). 

Module function declarations for [SpecBit_MSSM.cpp](/documentation/code/files/specbit__mssm_8cpp/#file-src-specbit-mssm-cpp) Module function declarations for [SpecBit_ScalarSingletDM.cpp](/documentation/code/files/specbit__scalarsingletdm_8cpp/#file-src-specbit-scalarsingletdm-cpp) Module function declarations for SpecBit_VectorSingletDM_Z2.cpp Module function declarations for SpecBit_MajoranaSingletDM_Z2.cpp Module function declarations for SpecBit_DiracSingletDM_Z2.cpp Module function declarations for [SpecBit_MDM.cpp](/documentation/code/files/specbit__mdm_8cpp/#file-src-specbit-mdm-cpp) Module function declarations for SpecBit_tests.cpp (new tests) Module function declarations for [SpecBit_DMEFT.cpp](/documentation/code/files/specbit__dmeft_8cpp/#file-src-specbit-dmeft-cpp) For SpecBit testing only Functions to change the capability associated with a Spectrum object to "SM_spectrum" 



## Attributes Documentation

### variable SM_spectrum

```
START_CAPABILITY SM_spectrum;
```


### variable OLD_CAPABILITY

```
START_CAPABILITY OLD_CAPABILITY;
```


### variable convert_NMSSM_to_SM

```
START_CAPABILITY convert_NMSSM_to_SM;
```


### variable Spectrum

```
START_CAPABILITY Spectrum;
```


### variable NMSSM_does_not_exist_yet

```
START_CAPABILITY NMSSM_does_not_exist_yet;
```


### variable NMSSM_spectrum

```
START_CAPABILITY NMSSM_spectrum;
```



## Macros Documentation

### define MODULE

```
#define MODULE SpecBit
```


### define REFERENCE

```
#define REFERENCE GAMBITModelsWorkgroup:2017ilg
```


### define CAPABILITY

```
#define CAPABILITY Higgs_Couplings
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Rollcall header for module SpecBit
///
///  These functions link ModelParameters to
///  Spectrum objects in various ways.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Ben Farmer
///          (benjamin.farmer@fysik.su.se)
///    \date 2014 Sep - Dec, 2015 Jan - Mar
///
///  \author Ankit Beniwal
///          (ankit.beniwal@adelaide.edu.au)
///    \date 2016 Aug
///
///  *********************************************

#ifndef __SpecBit_rollcall_hpp__
#define __SpecBit_rollcall_hpp__

#include "gambit/SpecBit/SpecBit_types.hpp"

#define MODULE SpecBit
#define REFERENCE GAMBITModelsWorkgroup:2017ilg
START_MODULE

  // Capabilities used in more than one of the headers
  // below need to be declared up-front (and then not
  // declared in the header)

  // Generalised Higgs couplings
  #define CAPABILITY Higgs_Couplings
  START_CAPABILITY
  #undef CAPABILITY

  /// Module function declarations for SpecBit_SM.cpp
  #include "gambit/SpecBit/SpecBit_SM_rollcall.hpp"

  /// Module function declarations for SpecBit_MSSM.cpp
  #include "gambit/SpecBit/SpecBit_MSSM_rollcall.hpp"

  #include "gambit/SpecBit/SpecBit_VS_rollcall.hpp"
  
  /// Module function declarations for SpecBit_ScalarSingletDM.cpp
  #include "gambit/SpecBit/SpecBit_ScalarSingletDM_rollcall.hpp"

  /// Module function declarations for SpecBit_VectorSingletDM_Z2.cpp
  #include "gambit/SpecBit/SpecBit_VectorSingletDM_rollcall.hpp"

  /// Module function declarations for SpecBit_MajoranaSingletDM_Z2.cpp
  #include "gambit/SpecBit/SpecBit_MajoranaSingletDM_rollcall.hpp"

  /// Module function declarations for SpecBit_DiracSingletDM_Z2.cpp
  #include "gambit/SpecBit/SpecBit_DiracSingletDM_rollcall.hpp"

  /// Module function declarations for SpecBit_MDM.cpp
  #include "gambit/SpecBit/SpecBit_MDM_rollcall.hpp"

  /// Module function declarations for SpecBit_tests.cpp (new tests)
  #include "gambit/SpecBit/SpecBit_tests_rollcall.hpp"

  /// Module function declarations for SpecBit_DMEFT.cpp
  #include "gambit/SpecBit/SpecBit_DMEFT_rollcall.hpp"

// TODO: Temporarily disabled until project is ready
/*
  /// Module function declarations for SpecBit_SuperRenormHP.cpp
  #include "gambit/SpecBit/SpecBit_SuperRenormHP_rollcall.hpp"
*/
  /// For SpecBit testing only
  //#include "gambit/SpecBit/SpecBit_sandbox_rollcall.hpp"

  /// Functions to change the capability associated with a Spectrum object to "SM_spectrum"
  /// @{
  QUICK_FUNCTION(MODULE, SM_spectrum, OLD_CAPABILITY, convert_MSSM_to_SM,  Spectrum, (MSSM63atQ, MSSM63atMGUT), (MSSM_spectrum, Spectrum))
  QUICK_FUNCTION(MODULE, SM_spectrum, OLD_CAPABILITY, convert_NMSSM_to_SM,  Spectrum, (NMSSM_does_not_exist_yet), (NMSSM_spectrum, Spectrum))
  QUICK_FUNCTION(MODULE, SM_spectrum, OLD_CAPABILITY, convert_E6MSSM_to_SM, Spectrum, (E6MSSM_does_not_exist_yet), (E6MSSM_spectrum, Spectrum))
  /// @}

  // 'Convenience' functions to retrieve certain particle properities in a simple format

  // #define CAPABILITY LSP_mass   // Supplies the mass of the lightest supersymmetric particle
  // START_CAPABILITY

  //   #define FUNCTION get_LSP_mass                      // Retrieves the LSP mass from a Spectrum object
  //   START_FUNCTION(double)
  //   DEPENDENCY(particle_spectrum, SpectrumPtr)            // Takes a Spectrum object and returns an SLHAstruct
  //   ALLOW_MODELS(MSSM24, CMSSM)
  //   #undef FUNCTION

  // #undef CAPABILITY

#undef REFERENCE
#undef MODULE

#endif /* defined(__SpecBit_rollcall_hpp__) */
```


-------------------------------

Updated on 2022-09-08 at 02:00:50 +0000
