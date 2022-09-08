---
title: "file vevacious_1_0/include/gambit/Backends/backend_types/vevacious_1_0/identification.hpp"

description: "[No description available]"

---

# file vevacious_1_0/include/gambit/Backends/backend_types/vevacious_1_0/identification.hpp

[No description available]

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[BACKENDNAME](/documentation/code/files/include_2gambit_2backends_2backend__types_2vevacious__1__0_2identification_8hpp/#define-include-gambit-backends-backend-types-vevacious-1-0-identification-hpp-backendname)**  |
|  | **[BACKENDLANG](/documentation/code/files/include_2gambit_2backends_2backend__types_2vevacious__1__0_2identification_8hpp/#define-include-gambit-backends-backend-types-vevacious-1-0-identification-hpp-backendlang)**  |
|  | **[VERSION](/documentation/code/files/include_2gambit_2backends_2backend__types_2vevacious__1__0_2identification_8hpp/#define-include-gambit-backends-backend-types-vevacious-1-0-identification-hpp-version)**  |
|  | **[SAFE_VERSION](/documentation/code/files/include_2gambit_2backends_2backend__types_2vevacious__1__0_2identification_8hpp/#define-include-gambit-backends-backend-types-vevacious-1-0-identification-hpp-safe-version)**  |
|  | **[REFERENCE](/documentation/code/files/include_2gambit_2backends_2backend__types_2vevacious__1__0_2identification_8hpp/#define-include-gambit-backends-backend-types-vevacious-1-0-identification-hpp-reference)**  |
|  | **[DO_CLASSLOADING](/documentation/code/files/include_2gambit_2backends_2backend__types_2vevacious__1__0_2identification_8hpp/#define-include-gambit-backends-backend-types-vevacious-1-0-identification-hpp-do-classloading)**  |




## Macros Documentation

### define BACKENDNAME

```
#define BACKENDNAME vevacious
```


### define BACKENDLANG

```
#define BACKENDLANG CXX
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
#define REFERENCE Camargo-Molina:2013qva
```


### define DO_CLASSLOADING

```
#define DO_CLASSLOADING 1
```


## Source code

```
// Identify backend and set macro flags

#include "gambit/Utils/cats.hpp"

#define BACKENDNAME vevacious
#define BACKENDLANG CXX
#define VERSION 1.0
#define SAFE_VERSION 1_0
#define REFERENCE Camargo-Molina:2013qva

#undef DO_CLASSLOADING
#define DO_CLASSLOADING 1
```


-------------------------------

Updated on 2022-09-08 at 02:00:54 +0000
