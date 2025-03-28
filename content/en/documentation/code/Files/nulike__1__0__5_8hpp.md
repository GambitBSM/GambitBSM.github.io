---
title: "file frontends/nulike_1_0_5.hpp"

description: "[No description available]"

---

# file frontends/nulike_1_0_5.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[BACKENDNAME](/documentation/code/files/nulike__1__0__5_8hpp/#define-backendname)**  |
|  | **[BACKENDLANG](/documentation/code/files/nulike__1__0__5_8hpp/#define-backendlang)**  |
|  | **[VERSION](/documentation/code/files/nulike__1__0__5_8hpp/#define-version)**  |
|  | **[SAFE_VERSION](/documentation/code/files/nulike__1__0__5_8hpp/#define-safe-version)**  |
|  | **[REFERENCE](/documentation/code/files/nulike__1__0__5_8hpp/#define-reference)**  |

## Detailed Description


**Author**: Pat Scott ([patscott@physics.mcgill.ca](mailto:patscott@physics.mcgill.ca)) 

**Date**: 

  * 2013 May 
  * 2014 March 
  * 2015 Aug


Frontend header for the nulike backend.

Compile-time registration of available functions and variables from this backend.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define BACKENDNAME

```
#define BACKENDNAME nulike
```


### define BACKENDLANG

```
#define BACKENDLANG Fortran
```


### define VERSION

```
#define VERSION 1.0.5
```


### define SAFE_VERSION

```
#define SAFE_VERSION 1_0_5
```


### define REFERENCE

```
#define REFERENCE IceCube:2012fvn,IceCube:2016yoy
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Frontend header for the nulike backend.
///
///  Compile-time registration of available
///  functions and variables from this backend.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Pat Scott
///          (patscott@physics.mcgill.ca)
///  \date 2013 May
///  \date 2014 March
///  \date 2015 Aug
///
///  *********************************************

#define BACKENDNAME nulike
#define BACKENDLANG Fortran
#define VERSION 1.0.5
#define SAFE_VERSION 1_0_5
#define REFERENCE IceCube:2012fvn,IceCube:2016yoy

// Load it
LOAD_LIBRARY

// Declare the relevant functions
#include "gambit/Backends/frontends/shared_includes/nulike_1_0.hpp"

// Undefine macros to avoid conflict with other backends
#include "gambit/Backends/backend_undefs.hpp"
```


-------------------------------

Updated on 2025-02-12 at 16:10:36 +0000
