---
title: "file Rivet_4_1_0/include/gambit/Backends/backend_types/Rivet_4_1_0/identification.hpp"

description: "[No description available]"

---

# file Rivet_4_1_0/include/gambit/Backends/backend_types/Rivet_4_1_0/identification.hpp

[No description available]

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[BACKENDNAME](/documentation/code/files/include_2gambit_2backends_2backend__types_2rivet__4__1__0_2identification_8hpp/#define-backendname)**  |
|  | **[BACKENDLANG](/documentation/code/files/include_2gambit_2backends_2backend__types_2rivet__4__1__0_2identification_8hpp/#define-backendlang)**  |
|  | **[VERSION](/documentation/code/files/include_2gambit_2backends_2backend__types_2rivet__4__1__0_2identification_8hpp/#define-version)**  |
|  | **[SAFE_VERSION](/documentation/code/files/include_2gambit_2backends_2backend__types_2rivet__4__1__0_2identification_8hpp/#define-safe-version)**  |
|  | **[REFERENCE](/documentation/code/files/include_2gambit_2backends_2backend__types_2rivet__4__1__0_2identification_8hpp/#define-reference)**  |
|  | **[DO_CLASSLOADING](/documentation/code/files/include_2gambit_2backends_2backend__types_2rivet__4__1__0_2identification_8hpp/#define-do-classloading)**  |




## Macros Documentation

### define BACKENDNAME

```
#define BACKENDNAME Rivet
```


### define BACKENDLANG

```
#define BACKENDLANG CXX
```


### define VERSION

```
#define VERSION 4.1.0
```


### define SAFE_VERSION

```
#define SAFE_VERSION 4_1_0
```


### define REFERENCE

```
#define REFERENCE Bierlich:2019rhm
```


### define DO_CLASSLOADING

```
#define DO_CLASSLOADING 1
```


## Source code

```
// Identify backend and set macro flags

#include "gambit/Utils/cats.hpp"

#define BACKENDNAME Rivet
#define BACKENDLANG CXX
#define VERSION 4.1.0
#define SAFE_VERSION 4_1_0
#define REFERENCE Bierlich:2019rhm

#undef DO_CLASSLOADING
#define DO_CLASSLOADING 1
```


-------------------------------

Updated on 2026-11-03 at 14:50:48 +0000
