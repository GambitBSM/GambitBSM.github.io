---
title: "file Elements/module_macros_inmodule.hpp"

description: "[No description available]"

---

# file Elements/module_macros_inmodule.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[START_MODULE](/documentation/code/files/module__macros__inmodule_8hpp/#define-start-module)**  |
|  | **[START_CAPABILITY](/documentation/code/files/module__macros__inmodule_8hpp/#define-start-capability)**  |
|  | **[LONG_START_CAPABILITY](/documentation/code/files/module__macros__inmodule_8hpp/#define-long-start-capability)**(MODULE, C)  |
|  | **[DECLARE_FUNCTION](/documentation/code/files/module__macros__inmodule_8hpp/#define-declare-function)**(TYPE, CAN_MANAGE)  |
|  | **[LONG_DECLARE_FUNCTION](/documentation/code/files/module__macros__inmodule_8hpp/#define-long-declare-function)**(MODULE, C, FUNCTION, TYPE, CAN_MANAGE)  |
|  | **[DEPENDENCY](/documentation/code/files/module__macros__inmodule_8hpp/#define-dependency)**(DEP, TYPE)  |
|  | **[LONG_DEPENDENCY](/documentation/code/files/module__macros__inmodule_8hpp/#define-long-dependency)**(MODULE, FUNCTION, DEP, TYPE)  |
|  | **[NEEDS_MANAGER](/documentation/code/files/module__macros__inmodule_8hpp/#define-needs-manager)**(...)  |
|  | **[ALLOW_MODELS](/documentation/code/files/module__macros__inmodule_8hpp/#define-allow-models)**(...)  |
|  | **[ALLOWED_MODEL](/documentation/code/files/module__macros__inmodule_8hpp/#define-allowed-model)**(MODULE, FUNCTION, MODEL)  |
|  | **[ALLOWED_MODEL_DEPENDENCE](/documentation/code/files/module__macros__inmodule_8hpp/#define-allowed-model-dependence)**(MODULE, FUNCTION, MODEL)  |
|  | **[ALLOW_MODEL_COMBINATION](/documentation/code/files/module__macros__inmodule_8hpp/#define-allow-model-combination)**(...)  |
|  | **[MODEL_GROUP](/documentation/code/files/module__macros__inmodule_8hpp/#define-model-group)**(GROUPNAME, GROUP)  |
|  | **[BE_GROUP](/documentation/code/files/module__macros__inmodule_8hpp/#define-be-group)**(GROUP)  |
|  | **[DECLARE_BACKEND_REQ](/documentation/code/files/module__macros__inmodule_8hpp/#define-declare-backend-req)**(GROUP, REQUIREMENT, TAGS, TYPE, ARGS, IS_VARIABLE)  |
|  | **[LONG_DECLARE_BACKEND_REQ](/documentation/code/files/module__macros__inmodule_8hpp/#define-long-declare-backend-req)**(MODULE, C, FUNCTION, GROUP, REQUIREMENT, TAGS, TYPE, ARGS, IS_VARIABLE)  |
|  | **[ACTIVATE_BACKEND_REQ_FOR_MODELS](/documentation/code/files/module__macros__inmodule_8hpp/#define-activate-backend-req-for-models)**(MODELS, TAGS)  |
|  | **[START_CONDITIONAL_DEPENDENCY](/documentation/code/files/module__macros__inmodule_8hpp/#define-start-conditional-dependency)**(TYPE)  |
|  | **[ACTIVATE_DEP_BE](/documentation/code/files/module__macros__inmodule_8hpp/#define-activate-dep-be)**(BACKEND_REQ, BACKEND, VERSTRING)  |
|  | **[ACTIVATE_FOR_MODELS](/documentation/code/files/module__macros__inmodule_8hpp/#define-activate-for-models)**(...)  |
|  | **[MODEL_CONDITIONAL_DEPENDENCY](/documentation/code/files/module__macros__inmodule_8hpp/#define-model-conditional-dependency)**(DEP, TYPE, ...)  |
|  | **[BACKEND_OPTION](/documentation/code/files/module__macros__inmodule_8hpp/#define-backend-option)**(BACKEND_AND_VERSIONS, TAGS)  |
|  | **[LONG_BACKEND_OPTION](/documentation/code/files/module__macros__inmodule_8hpp/#define-long-backend-option)**(MODULE, CAPABILITY, FUNCTION, BACKEND_AND_VERSIONS, TAGS)  |
|  | **[FORCE_SAME_BACKEND](/documentation/code/files/module__macros__inmodule_8hpp/#define-force-same-backend)**(...)  |
|  | **[CLASSLOAD_NEEDED](/documentation/code/files/module__macros__inmodule_8hpp/#define-classload-needed)**(...)  |

## Detailed Description


**Author**: 

  * Pat Scott ([patscott@physics.mcgill.ca](mailto:patscott@physics.mcgill.ca)) 
  * Abram Krislock ([abram.krislock@fysik.su.se](mailto:abram.krislock@fysik.su.se)) 


**Date**: 

  * 2012 Nov 
  * 2013 All year 
  * 2014 Foreverrrrr
  * 2013 Jan, Feb 


Redirection macros for generic observable and likelihood function macro definitions, for inclusion from actual module source code.



------------------

Authors (add name and date if you modify):




## Macros Documentation

### define START_MODULE

```
#define START_MODULE MODULE_START_MODULE
```


### define START_CAPABILITY

```
#define START_CAPABILITY MODULE_START_CAPABILITY(MODULE)
```


### define LONG_START_CAPABILITY

```
#define LONG_START_CAPABILITY(
    MODULE,
    C
)
MODULE_START_CAPABILITY(MODULE)
```


### define DECLARE_FUNCTION

```
#define DECLARE_FUNCTION(
    TYPE,
    CAN_MANAGE
)
MODULE_DECLARE_FUNCTION(MODULE, FUNCTION, TYPE, CAN_MANAGE, NOT_MODEL)
```


### define LONG_DECLARE_FUNCTION

```
#define LONG_DECLARE_FUNCTION(
    MODULE,
    C,
    FUNCTION,
    TYPE,
    CAN_MANAGE
)
MODULE_DECLARE_FUNCTION(MODULE, FUNCTION, TYPE, CAN_MANAGE, NOT_MODEL)
```


### define DEPENDENCY

```
#define DEPENDENCY(
    DEP,
    TYPE
)
MODULE_DEPENDENCY(DEP, TYPE, MODULE, FUNCTION, NOT_MODEL)
```


### define LONG_DEPENDENCY

```
#define LONG_DEPENDENCY(
    MODULE,
    FUNCTION,
    DEP,
    TYPE
)
MODULE_DEPENDENCY(DEP, TYPE, MODULE, FUNCTION, NOT_MODEL)
```


### define NEEDS_MANAGER

```
#define NEEDS_MANAGER(
    ...
)
MODULE_NEEDS_MANAGER_REDIRECT(__VA_ARGS__)
```


### define ALLOW_MODELS

```
#define ALLOW_MODELS(
    ...
)
ALLOW_MODELS_AB(MODULE, FUNCTION, __VA_ARGS__)
```


### define ALLOWED_MODEL

```
#define ALLOWED_MODEL(
    MODULE,
    FUNCTION,
    MODEL
)
MODULE_ALLOWED_MODEL(MODULE,FUNCTION,MODEL,NOT_MODEL)
```


### define ALLOWED_MODEL_DEPENDENCE

```
#define ALLOWED_MODEL_DEPENDENCE(
    MODULE,
    FUNCTION,
    MODEL
)
MODULE_ALLOWED_MODEL(MODULE,FUNCTION,MODEL,NOT_MODEL)
```


### define ALLOW_MODEL_COMBINATION

```
#define ALLOW_MODEL_COMBINATION(
    ...
)
DUMMYARG(__VA_ARGS__)
```


### define MODEL_GROUP

```
#define MODEL_GROUP(
    GROUPNAME,
    GROUP
)
DUMMYARG(GROUPNAME, GROUP)
```


### define BE_GROUP

```
#define BE_GROUP(
    GROUP
)
MODULE_BE_GROUP(GROUP,NOT_MODEL)
```


### define DECLARE_BACKEND_REQ

```
#define DECLARE_BACKEND_REQ(
    GROUP,
    REQUIREMENT,
    TAGS,
    TYPE,
    ARGS,
    IS_VARIABLE
)
MODULE_BACKEND_REQ(MODULE, FUNCTION, GROUP, REQUIREMENT, TAGS, TYPE, ARGS, IS_VARIABLE, NOT_MODEL)
```


### define LONG_DECLARE_BACKEND_REQ

```
#define LONG_DECLARE_BACKEND_REQ(
    MODULE,
    C,
    FUNCTION,
    GROUP,
    REQUIREMENT,
    TAGS,
    TYPE,
    ARGS,
    IS_VARIABLE
)
MODULE_BACKEND_REQ(MODULE, FUNCTION, GROUP, REQUIREMENT, TAGS, TYPE, ARGS, IS_VARIABLE, NOT_MODEL)
```


### define ACTIVATE_BACKEND_REQ_FOR_MODELS

```
#define ACTIVATE_BACKEND_REQ_FOR_MODELS(
    MODELS,
    TAGS
)
DUMMYARG(MODELS,TAGS)
```


### define START_CONDITIONAL_DEPENDENCY

```
#define START_CONDITIONAL_DEPENDENCY(
    TYPE
)
MODULE_DEPENDENCY(CONDITIONAL_DEPENDENCY, TYPE, MODULE, FUNCTION, NOT_MODEL)
```


### define ACTIVATE_DEP_BE

```
#define ACTIVATE_DEP_BE(
    BACKEND_REQ,
    BACKEND,
    VERSTRING
)
DUMMYARG(BACKEND_REQ, BACKEND, VERSTRING)
```


### define ACTIVATE_FOR_MODELS

```
#define ACTIVATE_FOR_MODELS(
    ...
)
DUMMYARG(__VA_ARGS__)
```


### define MODEL_CONDITIONAL_DEPENDENCY

```
#define MODEL_CONDITIONAL_DEPENDENCY(
    DEP,
    TYPE,
    ...
)
MODULE_DEPENDENCY(DEP, TYPE, MODULE, FUNCTION, NOT_MODEL)
```


### define BACKEND_OPTION

```
#define BACKEND_OPTION(
    BACKEND_AND_VERSIONS,
    TAGS
)
DUMMYARG(BACKEND_AND_VERSIONS,TAGS)
```


### define LONG_BACKEND_OPTION

```
#define LONG_BACKEND_OPTION(
    MODULE,
    CAPABILITY,
    FUNCTION,
    BACKEND_AND_VERSIONS,
    TAGS
)
                                                          DUMMYARG(BACKEND_AND_VERSIONS,TAGS)
```


### define FORCE_SAME_BACKEND

```
#define FORCE_SAME_BACKEND(
    ...
)
DUMMYARG(__VA_ARGS__)
```


### define CLASSLOAD_NEEDED

```
#define CLASSLOAD_NEEDED(
    ...
)
DUMMYARG(__VA_ARGS__)
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Redirection macros for generic observable and 
///  likelihood function macro definitions, for 
///  inclusion from actual module source code.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Pat Scott
///          (patscott@physics.mcgill.ca)
///  \date 2012 Nov
///  \date 2013 All year
///  \date 2014 Foreverrrrr
///
///  \author Abram Krislock
///          (abram.krislock@fysik.su.se)
///  \date 2013 Jan, Feb
//
///  \author Christoph Weniger
///          (c.weniger@uva.nl)
///  \date 2013 Jan, Feb, 2014 Jan
///
///  \author Anders Kvellestad
///          (anders.kvellestad@fys.uio.no)
///  \date 2013 Nov
///
///  \author Ben Farmer
///          (b.farmer@imperial.ac.uk)
///  \date 2015 Apr, 2019 Jul
///
///  *********************************************

#ifndef __module_macros_inmodule_hpp__
#define __module_macros_inmodule_hpp__

#include "gambit/Elements/module_macros_inmodule_defs.hpp"

/// \name Rollcall macros
/// These are called from within rollcall headers in each module to
/// register module functions, their capabilities, return types, dependencies,
/// and backend requirements.
/// @{
// Redirect the rollcall macros to their in-module variants
#define START_MODULE                                      MODULE_START_MODULE
#define START_CAPABILITY                                  MODULE_START_CAPABILITY(MODULE)
#define LONG_START_CAPABILITY(MODULE, C)                  MODULE_START_CAPABILITY(MODULE)
#define DECLARE_FUNCTION(TYPE, CAN_MANAGE)                MODULE_DECLARE_FUNCTION(MODULE, FUNCTION, TYPE, CAN_MANAGE, NOT_MODEL)
#define LONG_DECLARE_FUNCTION(MODULE, C, FUNCTION, TYPE, CAN_MANAGE) \
                                                          MODULE_DECLARE_FUNCTION(MODULE, FUNCTION, TYPE, CAN_MANAGE, NOT_MODEL)
#define DEPENDENCY(DEP, TYPE)                             MODULE_DEPENDENCY(DEP, TYPE, MODULE, FUNCTION, NOT_MODEL)
#define LONG_DEPENDENCY(MODULE, FUNCTION, DEP, TYPE)      MODULE_DEPENDENCY(DEP, TYPE, MODULE, FUNCTION, NOT_MODEL)
#define NEEDS_MANAGER(...)                                MODULE_NEEDS_MANAGER_REDIRECT(__VA_ARGS__)
#define ALLOW_MODELS(...)                                 ALLOW_MODELS_AB(MODULE, FUNCTION, __VA_ARGS__)
#define ALLOWED_MODEL(MODULE,FUNCTION,MODEL)              MODULE_ALLOWED_MODEL(MODULE,FUNCTION,MODEL,NOT_MODEL)
#define ALLOWED_MODEL_DEPENDENCE(MODULE,FUNCTION,MODEL)   MODULE_ALLOWED_MODEL(MODULE,FUNCTION,MODEL,NOT_MODEL)
#define ALLOW_MODEL_COMBINATION(...)                      DUMMYARG(__VA_ARGS__)
#define MODEL_GROUP(GROUPNAME, GROUP)                     DUMMYARG(GROUPNAME, GROUP)

#define BE_GROUP(GROUP)                                   MODULE_BE_GROUP(GROUP,NOT_MODEL)
#define DECLARE_BACKEND_REQ(GROUP, REQUIREMENT, TAGS, TYPE, ARGS, IS_VARIABLE) \
                                                          MODULE_BACKEND_REQ(MODULE, FUNCTION, GROUP, REQUIREMENT, TAGS, TYPE, ARGS, IS_VARIABLE, NOT_MODEL)
#define LONG_DECLARE_BACKEND_REQ(MODULE, C, FUNCTION, GROUP, REQUIREMENT, TAGS, TYPE, ARGS, IS_VARIABLE) \
                                                          MODULE_BACKEND_REQ(MODULE, FUNCTION, GROUP, REQUIREMENT, TAGS, TYPE, ARGS, IS_VARIABLE, NOT_MODEL)
#define ACTIVATE_BACKEND_REQ_FOR_MODELS(MODELS,TAGS)      DUMMYARG(MODELS,TAGS)
#define START_CONDITIONAL_DEPENDENCY(TYPE)                MODULE_DEPENDENCY(CONDITIONAL_DEPENDENCY, TYPE, MODULE, FUNCTION, NOT_MODEL)
#define ACTIVATE_DEP_BE(BACKEND_REQ, BACKEND, VERSTRING)  DUMMYARG(BACKEND_REQ, BACKEND, VERSTRING)
#define ACTIVATE_FOR_MODELS(...)                          DUMMYARG(__VA_ARGS__)
#define MODEL_CONDITIONAL_DEPENDENCY(DEP, TYPE, ...)      MODULE_DEPENDENCY(DEP, TYPE, MODULE, FUNCTION, NOT_MODEL)
#define BACKEND_OPTION(BACKEND_AND_VERSIONS,TAGS)         DUMMYARG(BACKEND_AND_VERSIONS,TAGS)
#define LONG_BACKEND_OPTION(MODULE, CAPABILITY, FUNCTION, BACKEND_AND_VERSIONS,TAGS) \
                                                          DUMMYARG(BACKEND_AND_VERSIONS,TAGS)
#define FORCE_SAME_BACKEND(...)                           DUMMYARG(__VA_ARGS__)
#define CLASSLOAD_NEEDED(...)                             DUMMYARG(__VA_ARGS__)
/// @}

#endif // defined __module_macros_inmodule_hpp__
```


-------------------------------

Updated on 2025-02-12 at 16:10:34 +0000
