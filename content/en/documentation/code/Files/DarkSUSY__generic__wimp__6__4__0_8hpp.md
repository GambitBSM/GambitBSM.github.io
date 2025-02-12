---
title: "file frontends/DarkSUSY_generic_wimp_6_4_0.hpp"

description: "[No description available]"

---

# file frontends/DarkSUSY_generic_wimp_6_4_0.hpp

[No description available] [More...](#detailed-description)

## Functions

|                | Name           |
| -------------- | -------------- |
| [LOAD_LIBRARY](/documentation/code/files/frontend__macros_8hpp/#define-load-library) | **[BE_VARIABLE](/documentation/code/files/darksusy__generic__wimp__6__4__0_8hpp/#function-be-variable)**(rdpars , DS_RDPARS , "rdpars_" , "rdpars" ) |
| [LOAD_LIBRARY](/documentation/code/files/frontend__macros_8hpp/#define-load-library) rdlims | **[BE_VARIABLE](/documentation/code/files/darksusy__generic__wimp__6__4__0_8hpp/#function-be-variable)**(rd20opt , DS_RD20OPT , "rd20opt_" , "rd20opt" ) |

## Attributes

|                | Name           |
| -------------- | -------------- |
| [LOAD_LIBRARY](/documentation/code/files/frontend__macros_8hpp/#define-load-library) | **[DS_RDLIMS](/documentation/code/files/darksusy__generic__wimp__6__4__0_8hpp/#variable-ds-rdlims)**  |
| [LOAD_LIBRARY](/documentation/code/files/frontend__macros_8hpp/#define-load-library) | **[rdlims_](/documentation/code/files/darksusy__generic__wimp__6__4__0_8hpp/#variable-rdlims)**  |
| [LOAD_LIBRARY](/documentation/code/files/frontend__macros_8hpp/#define-load-library) rdlims | **[DS_ADM_COM](/documentation/code/files/darksusy__generic__wimp__6__4__0_8hpp/#variable-ds-adm-com)**  |
| [LOAD_LIBRARY](/documentation/code/files/frontend__macros_8hpp/#define-load-library) rdlims | **[adm_com_](/documentation/code/files/darksusy__generic__wimp__6__4__0_8hpp/#variable-adm-com)**  |

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[BACKENDNAME](/documentation/code/files/darksusy__generic__wimp__6__4__0_8hpp/#define-backendname)**  |
|  | **[BACKENDLANG](/documentation/code/files/darksusy__generic__wimp__6__4__0_8hpp/#define-backendlang)**  |
|  | **[VERSION](/documentation/code/files/darksusy__generic__wimp__6__4__0_8hpp/#define-version)**  |
|  | **[SAFE_VERSION](/documentation/code/files/darksusy__generic__wimp__6__4__0_8hpp/#define-safe-version)**  |
|  | **[REFERENCE](/documentation/code/files/darksusy__generic__wimp__6__4__0_8hpp/#define-reference)**  |

## Detailed Description


**Author**: Torsten Bringmann ([torsten.bringmann@fys.uio.no](mailto:torsten.bringmann@fys.uio.no)) 

**Date**: 2022 January, 2023

Frontend header for the DarkSUSY backend

Compile-time registration of available functions and variables from this backend.



------------------

Authors (add name and date if you modify):



------------------


## Functions Documentation

### function BE_VARIABLE

```
LOAD_LIBRARY BE_VARIABLE(
    rdpars ,
    DS_RDPARS ,
    "rdpars_" ,
    "rdpars" 
)
```


### function BE_VARIABLE

```
LOAD_LIBRARY rdlims BE_VARIABLE(
    rd20opt ,
    DS_RD20OPT ,
    "rd20opt_" ,
    "rd20opt" 
)
```



## Attributes Documentation

### variable DS_RDLIMS

```
LOAD_LIBRARY DS_RDLIMS;
```


### variable rdlims_

```
LOAD_LIBRARY rdlims_;
```


### variable DS_ADM_COM

```
LOAD_LIBRARY rdlims DS_ADM_COM;
```


### variable adm_com_

```
LOAD_LIBRARY rdlims adm_com_;
```



## Macros Documentation

### define BACKENDNAME

```
#define BACKENDNAME DarkSUSY_generic_wimp
```


### define BACKENDLANG

```
#define BACKENDLANG FORTRAN
```


### define VERSION

```
#define VERSION 6.4.0
```


### define SAFE_VERSION

```
#define SAFE_VERSION 6_4_0
```


### define REFERENCE

```
#define REFERENCE Gondolo:2004sc,Bringmann:2018lay
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Frontend header for the DarkSUSY backend
///
///  Compile-time registration of available
///  functions and variables from this backend.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Torsten Bringmann
///          (torsten.bringmann@fys.uio.no)
///  \date 2022 January, 2023
///
///  *********************************************

#define BACKENDNAME DarkSUSY_generic_wimp
#define BACKENDLANG FORTRAN
#define VERSION 6.4.0
#define SAFE_VERSION 6_4_0
#define REFERENCE Gondolo:2004sc,Bringmann:2018lay

// Load the library
LOAD_LIBRARY

// Include common DarkSUSY frontend declarations shared across all model-specific versions of the backend
#include "gambit/Backends/frontends/shared_includes/DarkSUSY_6.hpp"

// Common blocks in the DarkSUSY core library that are not identical for all DS6 versions
BE_VARIABLE(rdpars, DS_RDPARS,     "rdpars_",    "rdpars")    // gRD Parameters
BE_VARIABLE(rdlims, DS_RDLIMS,     "rdlims_",    "rdlims")    // new Boltzmann routines
BE_VARIABLE(rd20opt, DS_RD20OPT,     "rd20opt_",    "rd20opt")  // new Boltzmann routines
BE_VARIABLE(adm_com, DS_ADM_COM,     "adm_com_",    "adm_com")  // asymmetric DM

// Undefine macros to avoid conflict with other backends
#include "gambit/Backends/backend_undefs.hpp"
```


-------------------------------

Updated on 2025-02-12 at 15:36:43 +0000
