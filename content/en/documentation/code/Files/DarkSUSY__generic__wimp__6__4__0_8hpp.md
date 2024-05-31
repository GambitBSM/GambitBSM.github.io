---
title: "file frontends/DarkSUSY_generic_wimp_6_4_0.hpp"

description: "[No description available]"

---

# file frontends/DarkSUSY_generic_wimp_6_4_0.hpp

[No description available] [More...](#detailed-description)

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

// Undefine macros to avoid conflict with other backends
#include "gambit/Backends/backend_undefs.hpp"
```


-------------------------------

Updated on 2024-05-31 at 15:12:08 +0000
