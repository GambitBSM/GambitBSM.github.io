---
title: "file gm2calc_1_3_0/include/gambit/Backends/backend_types/gm2calc_1_3_0/identification.hpp"

description: "[No description available]"

---

# file gm2calc_1_3_0/include/gambit/Backends/backend_types/gm2calc_1_3_0/identification.hpp

[No description available]

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[BACKENDNAME](/documentation/code/files/include_2gambit_2backends_2backend__types_2gm2calc__1__3__0_2identification_8hpp/#define-include-gambit-backends-backend-types-gm2calc-1-3-0-identification-hpp-backendname)**  |
|  | **[BACKENDLANG](/documentation/code/files/include_2gambit_2backends_2backend__types_2gm2calc__1__3__0_2identification_8hpp/#define-include-gambit-backends-backend-types-gm2calc-1-3-0-identification-hpp-backendlang)**  |
|  | **[VERSION](/documentation/code/files/include_2gambit_2backends_2backend__types_2gm2calc__1__3__0_2identification_8hpp/#define-include-gambit-backends-backend-types-gm2calc-1-3-0-identification-hpp-version)**  |
|  | **[SAFE_VERSION](/documentation/code/files/include_2gambit_2backends_2backend__types_2gm2calc__1__3__0_2identification_8hpp/#define-include-gambit-backends-backend-types-gm2calc-1-3-0-identification-hpp-safe-version)**  |
|  | **[REFERENCE](/documentation/code/files/include_2gambit_2backends_2backend__types_2gm2calc__1__3__0_2identification_8hpp/#define-include-gambit-backends-backend-types-gm2calc-1-3-0-identification-hpp-reference)**  |
|  | **[DO_CLASSLOADING](/documentation/code/files/include_2gambit_2backends_2backend__types_2gm2calc__1__3__0_2identification_8hpp/#define-include-gambit-backends-backend-types-gm2calc-1-3-0-identification-hpp-do-classloading)**  |




## Macros Documentation

### define BACKENDNAME

```
#define BACKENDNAME gm2calc
```


### define BACKENDLANG

```
#define BACKENDLANG CXX
```


### define VERSION

```
#define VERSION 1.3.0
```


### define SAFE_VERSION

```
#define SAFE_VERSION 1_3_0
```


### define REFERENCE

```
#define REFERENCE Athron:2015rva
```


### define DO_CLASSLOADING

```
#define DO_CLASSLOADING 1
```


## Source code

```
// Identify backend and set macro flags

#include "gambit/Utils/cats.hpp"

#define BACKENDNAME gm2calc
#define BACKENDLANG CXX
#define VERSION 1.3.0
#define SAFE_VERSION 1_3_0
#define REFERENCE Athron:2015rva

#undef DO_CLASSLOADING
#define DO_CLASSLOADING 1
```


-------------------------------

Updated on 2022-09-08 at 02:00:54 +0000
