---
title: "file frontends/DarkCast_1_1.hpp"

description: "[No description available]"

---

# file frontends/DarkCast_1_1.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[BACKENDNAME](/documentation/code/files/darkcast__1__1_8hpp/#define-backendname)**  |
|  | **[BACKENDLANG](/documentation/code/files/darkcast__1__1_8hpp/#define-backendlang)**  |
|  | **[VERSION](/documentation/code/files/darkcast__1__1_8hpp/#define-version)**  |
|  | **[SAFE_VERSION](/documentation/code/files/darkcast__1__1_8hpp/#define-safe-version)**  |
|  | **[REFERENCE](/documentation/code/files/darkcast__1__1_8hpp/#define-reference)**  |

## Detailed Description


**Author**: Quan Huynh ([qhuy0003@student.monash.edu](mailto:qhuy0003@student.monash.edu)) 

**Date**: 2022 Apr

Frontend header for the DarkCast backend

Compile-time registration of available functions and variables from this backend.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define BACKENDNAME

```
#define BACKENDNAME DarkCast
```


### define BACKENDLANG

```
#define BACKENDLANG Python
```


### define VERSION

```
#define VERSION 1.1
```


### define SAFE_VERSION

```
#define SAFE_VERSION 1_1
```


### define REFERENCE

```
#define REFERENCE Ilten:2018crw
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Frontend header for the DarkCast backend
///
///  Compile-time registration of available
///  functions and variables from this backend.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Quan Huynh
///          (qhuy0003@student.monash.edu)
///  \date 2022 Apr
///
///  *********************************************


#define BACKENDNAME DarkCast
#define BACKENDLANG Python
#define VERSION 1.1
#define SAFE_VERSION 1_1
#define REFERENCE Ilten:2018crw

LOAD_LIBRARY

#ifdef HAVE_PYBIND11
  //Single final state
  BE_CONV_FUNCTION(dark_photon_decay_width, double, (double&, std::string, double&), "dark_photon_decay_width")
  BE_CONV_FUNCTION(dark_photon_branching_fraction, double, (std::string, double&), "dark_photon_branching_fraction")

  //Multiple final states
  BE_CONV_FUNCTION(dark_photon_decay_width_multi, double, (double&, std::vector<std::string>, double&), "dark_photon_decay_width_multi")
  BE_CONV_FUNCTION(dark_photon_branching_fraction_multi, double, (std::vector<std::string>, double&), "dark_photon_branching_fraction_multi")
#endif

#include "gambit/Backends/backend_undefs.hpp"
```


-------------------------------

Updated on 2025-02-12 at 15:36:43 +0000
