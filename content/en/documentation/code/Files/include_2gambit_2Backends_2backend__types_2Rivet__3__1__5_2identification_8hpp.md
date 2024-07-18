---
title: "file Rivet_3_1_5/include/gambit/Backends/backend_types/Rivet_3_1_5/identification.hpp"

description: "[No description available]"

---

# file Rivet_3_1_5/include/gambit/Backends/backend_types/Rivet_3_1_5/identification.hpp

[No description available]

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[BACKENDNAME](/documentation/code/files/include_2gambit_2backends_2backend__types_2rivet__3__1__5_2identification_8hpp/#define-backendname)**  |
|  | **[BACKENDLANG](/documentation/code/files/include_2gambit_2backends_2backend__types_2rivet__3__1__5_2identification_8hpp/#define-backendlang)**  |
|  | **[VERSION](/documentation/code/files/include_2gambit_2backends_2backend__types_2rivet__3__1__5_2identification_8hpp/#define-version)**  |
|  | **[SAFE_VERSION](/documentation/code/files/include_2gambit_2backends_2backend__types_2rivet__3__1__5_2identification_8hpp/#define-safe-version)**  |
|  | **[REFERENCE](/documentation/code/files/include_2gambit_2backends_2backend__types_2rivet__3__1__5_2identification_8hpp/#define-reference)**  |
|  | **[DO_CLASSLOADING](/documentation/code/files/include_2gambit_2backends_2backend__types_2rivet__3__1__5_2identification_8hpp/#define-do-classloading)**  |




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
#define VERSION 3.1.5
```


### define SAFE_VERSION

```
#define SAFE_VERSION 3_1_5
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
#define VERSION 3.1.5
#define SAFE_VERSION 3_1_5
#define REFERENCE Bierlich:2019rhm

#undef DO_CLASSLOADING
#define DO_CLASSLOADING 1
```


-------------------------------

Updated on 2024-07-18 at 13:53:35 +0000
