---
title: "file frontends/simplexs_1_0.hpp"

description: "[No description available]"

---

# file frontends/simplexs_1_0.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[BACKENDNAME](/documentation/code/files/simplexs__1__0_8hpp/#define-backendname)**  |
|  | **[BACKENDLANG](/documentation/code/files/simplexs__1__0_8hpp/#define-backendlang)**  |
|  | **[VERSION](/documentation/code/files/simplexs__1__0_8hpp/#define-version)**  |
|  | **[SAFE_VERSION](/documentation/code/files/simplexs__1__0_8hpp/#define-safe-version)**  |

## Detailed Description


**Author**: Christopher Chang ([christopher.chang@uqconnect.edu.au](mailto:christopher.chang@uqconnect.edu.au)) 

**Date**: 2020 Feb

Frontend header for the simplexs backend



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define BACKENDNAME

```
#define BACKENDNAME simple_xs
```


### define BACKENDLANG

```
#define BACKENDLANG Python
```


### define VERSION

```
#define VERSION 1.0
```


### define SAFE_VERSION

```
#define SAFE_VERSION 1_0
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Frontend header for the simplexs backend
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Christopher Chang
///          (christopher.chang@uqconnect.edu.au)
///  \date 2020 Feb
///
///  *********************************************


#define BACKENDNAME simple_xs
#define BACKENDLANG Python
#define VERSION 1.0
#define SAFE_VERSION 1_0


LOAD_LIBRARY

#ifdef HAVE_PYBIND11

  BE_FUNCTION(init, void, (PyDict&), "init", "simplexs_init")
  BE_FUNCTION(get_xsection, PyDict, (PyDict&, PyDict&), "get_xsection", "simplexs_get_xsection")
  
#endif

#include "gambit/Backends/backend_undefs.hpp"
```


-------------------------------

Updated on 2024-05-31 at 15:12:08 +0000
