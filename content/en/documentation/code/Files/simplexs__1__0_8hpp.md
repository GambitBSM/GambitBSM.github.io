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
|  | **[REFERENCE](/documentation/code/files/simplexs__1__0_8hpp/#define-reference)**  |

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


### define REFERENCE

```
#define REFERENCE Bozzi:2007qr,Fuks:2013vua,Fuks:2013lya,Fiaschi:2019zgh,Debove:2010kf,Fuks:2012qx,Fiaschi:2018hgm,Beenakker:2016lwe
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
#define REFERENCE Bozzi:2007qr,Fuks:2013vua,Fuks:2013lya,Fiaschi:2019zgh,Debove:2010kf,Fuks:2012qx,Fiaschi:2018hgm,Beenakker:2016lwe


LOAD_LIBRARY

#ifdef HAVE_PYBIND11

  BE_FUNCTION(init, void, (PyDict&), "init", "simplexs_init")
  BE_FUNCTION(get_xsection, PyDict, (PyDict&, PyDict&), "get_xsection", "simplexs_get_xsection")
  
#endif

#include "gambit/Backends/backend_undefs.hpp"
```


-------------------------------

Updated on 2025-02-12 at 16:10:36 +0000
