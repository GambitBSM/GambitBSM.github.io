---
title: "file frontends/pbarlike_1_0.hpp"

description: "[No description available]"

---

# file frontends/pbarlike_1_0.hpp

[No description available]

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[BACKENDNAME](/documentation/code/files/pbarlike__1__0_8hpp/#define-backendname)**  |
|  | **[BACKENDLANG](/documentation/code/files/pbarlike__1__0_8hpp/#define-backendlang)**  |
|  | **[VERSION](/documentation/code/files/pbarlike__1__0_8hpp/#define-version)**  |
|  | **[SAFE_VERSION](/documentation/code/files/pbarlike__1__0_8hpp/#define-safe-version)**  |
|  | **[REFERENCE](/documentation/code/files/pbarlike__1__0_8hpp/#define-reference)**  |




## Macros Documentation

### define BACKENDNAME

```
#define BACKENDNAME pbarlike
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
#define REFERENCE DarkRayNet:2021
```


## Source code

```
#define BACKENDNAME pbarlike
#define BACKENDLANG Python
#define VERSION 1.0
#define SAFE_VERSION 1_0
#define REFERENCE DarkRayNet:2021

LOAD_LIBRARY

#ifdef HAVE_PYBIND11
    BE_CONV_FUNCTION(c_pbarlike_initialization,pybind11::list,(const bool& ,const std::string& ,const mat_dbl& ), "pbarlike_initialization")
    BE_CONV_FUNCTION(c_pbar_logLikes,map_str_dbl,(double&,  map_str_dbl&, double& ), "drn_pbar_logLikes")
#endif

#include "gambit/Backends/backend_undefs.hpp"
```


-------------------------------

Updated on 2023-06-26 at 21:36:57 +0000
