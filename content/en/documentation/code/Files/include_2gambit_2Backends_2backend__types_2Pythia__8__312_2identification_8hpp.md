---
title: "file Pythia_8_312/include/gambit/Backends/backend_types/Pythia_8_312/identification.hpp"

description: "[No description available]"

---

# file Pythia_8_312/include/gambit/Backends/backend_types/Pythia_8_312/identification.hpp

[No description available]

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[BACKENDNAME](/documentation/code/files/include_2gambit_2backends_2backend__types_2pythia__8__312_2identification_8hpp/#define-backendname)**  |
|  | **[BACKENDLANG](/documentation/code/files/include_2gambit_2backends_2backend__types_2pythia__8__312_2identification_8hpp/#define-backendlang)**  |
|  | **[VERSION](/documentation/code/files/include_2gambit_2backends_2backend__types_2pythia__8__312_2identification_8hpp/#define-version)**  |
|  | **[SAFE_VERSION](/documentation/code/files/include_2gambit_2backends_2backend__types_2pythia__8__312_2identification_8hpp/#define-safe-version)**  |
|  | **[REFERENCE](/documentation/code/files/include_2gambit_2backends_2backend__types_2pythia__8__312_2identification_8hpp/#define-reference)**  |
|  | **[DO_CLASSLOADING](/documentation/code/files/include_2gambit_2backends_2backend__types_2pythia__8__312_2identification_8hpp/#define-do-classloading)**  |




## Macros Documentation

### define BACKENDNAME

```
#define BACKENDNAME Pythia
```


### define BACKENDLANG

```
#define BACKENDLANG CXX
```


### define VERSION

```
#define VERSION 8.312
```


### define SAFE_VERSION

```
#define SAFE_VERSION 8_312
```


### define REFERENCE

```
#define REFERENCE Bierlich:2022pfr
```


### define DO_CLASSLOADING

```
#define DO_CLASSLOADING 1
```


## Source code

```
// Identify backend and set macro flags

#include "gambit/Utils/cats.hpp"

#define BACKENDNAME Pythia
#define BACKENDLANG CXX
#define VERSION 8.312
#define SAFE_VERSION 8_312
#define REFERENCE Bierlich:2022pfr

#undef DO_CLASSLOADING
#define DO_CLASSLOADING 1
```


-------------------------------

Updated on 2025-02-12 at 15:36:43 +0000
