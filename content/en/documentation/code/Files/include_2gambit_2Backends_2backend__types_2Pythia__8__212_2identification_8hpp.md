---
title: "file Pythia_8_212/include/gambit/Backends/backend_types/Pythia_8_212/identification.hpp"

description: "[No description available]"

---

# file Pythia_8_212/include/gambit/Backends/backend_types/Pythia_8_212/identification.hpp

[No description available]

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[BACKENDNAME](/documentation/code/files/include_2gambit_2backends_2backend__types_2pythia__8__212_2identification_8hpp/#define-include-gambit-backends-backend-types-pythia-8-212-identification-hpp-backendname)**  |
|  | **[BACKENDLANG](/documentation/code/files/include_2gambit_2backends_2backend__types_2pythia__8__212_2identification_8hpp/#define-include-gambit-backends-backend-types-pythia-8-212-identification-hpp-backendlang)**  |
|  | **[VERSION](/documentation/code/files/include_2gambit_2backends_2backend__types_2pythia__8__212_2identification_8hpp/#define-include-gambit-backends-backend-types-pythia-8-212-identification-hpp-version)**  |
|  | **[SAFE_VERSION](/documentation/code/files/include_2gambit_2backends_2backend__types_2pythia__8__212_2identification_8hpp/#define-include-gambit-backends-backend-types-pythia-8-212-identification-hpp-safe-version)**  |
|  | **[REFERENCE](/documentation/code/files/include_2gambit_2backends_2backend__types_2pythia__8__212_2identification_8hpp/#define-include-gambit-backends-backend-types-pythia-8-212-identification-hpp-reference)**  |
|  | **[DO_CLASSLOADING](/documentation/code/files/include_2gambit_2backends_2backend__types_2pythia__8__212_2identification_8hpp/#define-include-gambit-backends-backend-types-pythia-8-212-identification-hpp-do-classloading)**  |




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
#define VERSION 8.212
```


### define SAFE_VERSION

```
#define SAFE_VERSION 8_212
```


### define REFERENCE

```
#define REFERENCE Sjostrand:2014zea
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
#define VERSION 8.212
#define SAFE_VERSION 8_212
#define REFERENCE Sjostrand:2014zea

#undef DO_CLASSLOADING
#define DO_CLASSLOADING 1
```


-------------------------------

Updated on 2022-09-08 at 01:49:00 +0000
