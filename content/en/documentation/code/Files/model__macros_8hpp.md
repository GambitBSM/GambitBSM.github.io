---
title: "file Models/model_macros.hpp"

description: "[No description available]"

---

# file Models/model_macros.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[CORE_DEFINEPARS](/documentation/code/files/model__macros_8hpp/#define-core-definepars)**(...)  |
|  | **[DO_LINK](/documentation/code/files/model__macros_8hpp/#define-do-link)**(r, data, elem)  |
|  | **[INTERPRET_AS_PARENT_DEPENDENCY](/documentation/code/files/model__macros_8hpp/#define-interpret-as-parent-dependency)**(DEP, TYPE)  |
|  | **[CORE_INTERPRET_AS_PARENT_FUNCTION](/documentation/code/files/model__macros_8hpp/#define-core-interpret-as-parent-function)**(FUNC)  |
|  | **[MAKE_PRIMARY_MODEL_FUNCTOR_MAIN](/documentation/code/files/model__macros_8hpp/#define-make-primary-model-functor-main)**(FUNCTION, CAPABILITY, ORIGIN) <br>Main version of MAKE_FUNCTOR modified to build primary_parameters functors.  |
|  | **[MAKE_PRIMARY_MODEL_FUNCTOR_SUPP](/documentation/code/files/model__macros_8hpp/#define-make-primary-model-functor-supp)**(FUNCTION) <br>Supplementary version of MAKE_FUNCTOR modded for primary_parameters functors.  |
|  | **[START_MODEL](/documentation/code/files/model__macros_8hpp/#define-start-model)**  |
|  | **[DEFINEPARS](/documentation/code/files/model__macros_8hpp/#define-definepars)**(...)  |
|  | **[MAP_TO_CAPABILITY](/documentation/code/files/model__macros_8hpp/#define-map-to-capability)**(PARAMETER, CAPABILITY)  |
|  | **[INTERPRET_AS_X_FUNCTION](/documentation/code/files/model__macros_8hpp/#define-interpret-as-x-function)**(MODEL_X, FUNC)  |
|  | **[INTERPRET_AS_PARENT_FUNCTION](/documentation/code/files/model__macros_8hpp/#define-interpret-as-parent-function)**(FUNC)  |
|  | **[INTERPRET_AS_X_DEPENDENCY](/documentation/code/files/model__macros_8hpp/#define-interpret-as-x-dependency)**(MODEL_X, DEP, TYPE)  |
|  | **[START_CAPABILITY](/documentation/code/files/model__macros_8hpp/#define-start-capability)**  |
|  | **[LONG_START_CAPABILITY](/documentation/code/files/model__macros_8hpp/#define-long-start-capability)**(MODULE, C)  |
|  | **[DECLARE_FUNCTION](/documentation/code/files/model__macros_8hpp/#define-declare-function)**(TYPE, CAN_MANAGE)  |
|  | **[LONG_DECLARE_FUNCTION](/documentation/code/files/model__macros_8hpp/#define-long-declare-function)**(MODULE, C, FUNCTION, TYPE, CAN_MANAGE)  |
|  | **[DEPENDENCY](/documentation/code/files/model__macros_8hpp/#define-dependency)**(DEP, TYPE)  |
|  | **[LONG_DEPENDENCY](/documentation/code/files/model__macros_8hpp/#define-long-dependency)**(MODULE, FUNCTION, DEP, TYPE)  |
|  | **[NEEDS_MANAGER](/documentation/code/files/model__macros_8hpp/#define-needs-manager)**(...)  |
|  | **[ALLOWED_MODEL](/documentation/code/files/model__macros_8hpp/#define-allowed-model)**(MODULE, FUNCTION, MODEL)  |
|  | **[ALLOWED_MODEL_DEPENDENCE](/documentation/code/files/model__macros_8hpp/#define-allowed-model-dependence)**(MODULE, FUNCTION, MODEL)  |
|  | **[ALLOW_MODEL_COMBINATION](/documentation/code/files/model__macros_8hpp/#define-allow-model-combination)**(...)  |
|  | **[MODEL_GROUP](/documentation/code/files/model__macros_8hpp/#define-model-group)**(GROUPNAME, GROUP)  |
|  | **[BE_GROUP](/documentation/code/files/model__macros_8hpp/#define-be-group)**(GROUP)  |
|  | **[DECLARE_BACKEND_REQ](/documentation/code/files/model__macros_8hpp/#define-declare-backend-req)**(GROUP, REQUIREMENT, TAGS, TYPE, ARGS, IS_VARIABLE)  |
|  | **[LONG_DECLARE_BACKEND_REQ](/documentation/code/files/model__macros_8hpp/#define-long-declare-backend-req)**(MODULE, C, FUNCTION, GROUP, REQUIREMENT, TAGS, TYPE, ARGS, IS_VARIABLE)  |
|  | **[ACTIVATE_BACKEND_REQ_FOR_MODELS](/documentation/code/files/model__macros_8hpp/#define-activate-backend-req-for-models)**(MODELS, TAGS)  |
|  | **[START_CONDITIONAL_DEPENDENCY](/documentation/code/files/model__macros_8hpp/#define-start-conditional-dependency)**(TYPE)  |
|  | **[ACTIVATE_DEP_BE](/documentation/code/files/model__macros_8hpp/#define-activate-dep-be)**(BACKEND_REQ, BACKEND, VERSTRING)  |
|  | **[ACTIVATE_FOR_MODELS](/documentation/code/files/model__macros_8hpp/#define-activate-for-models)**(...)  |
|  | **[MODEL_CONDITIONAL_DEPENDENCY](/documentation/code/files/model__macros_8hpp/#define-model-conditional-dependency)**(DEP, TYPE, ...)  |
|  | **[BACKEND_OPTION](/documentation/code/files/model__macros_8hpp/#define-backend-option)**(BACKEND_AND_VERSIONS, TAGS)  |
|  | **[LONG_BACKEND_OPTION](/documentation/code/files/model__macros_8hpp/#define-long-backend-option)**(MODULE, CAPABILITY, FUNCTION, BACKEND_AND_VERSIONS, TAGS)  |
|  | **[FORCE_SAME_BACKEND](/documentation/code/files/model__macros_8hpp/#define-force-same-backend)**(...)  |
|  | **[CLASSLOAD_NEEDED](/documentation/code/files/model__macros_8hpp/#define-classload-needed)**(...)  |
|  | **[ALLOW_MODELS](/documentation/code/files/model__macros_8hpp/#define-allow-models)**(...)  |
|  | **[MAKE_PRIMARY_MODEL_FUNCTOR](/documentation/code/files/model__macros_8hpp/#define-make-primary-model-functor)**(FUNCTION, CAPABILITY, ORIGIN)  |
|  | **[MODULE_INTERPRET_AS_X_FUNCTION](/documentation/code/files/model__macros_8hpp/#define-module-interpret-as-x-function)**(MODEL_X, FUNC) <br>"In module" version of the INTERPRET_AS_X_FUNCTION macro  |
|  | **[MODULE_INTERPRET_AS_X_DEPENDENCY](/documentation/code/files/model__macros_8hpp/#define-module-interpret-as-x-dependency)**(MODEL_X, DEP, TYPE) <br>"In module" version of the INTERPRET_AS_X_DEPENDENCY macro  |
|  | **[CORE_START_MODEL](/documentation/code/files/model__macros_8hpp/#define-core-start-model)**  |
|  | **[CORE_MAP_TO_CAPABILITY](/documentation/code/files/model__macros_8hpp/#define-core-map-to-capability)**(PARAMETER, CAPABILITY)  |
|  | **[DEFINEPAR](/documentation/code/files/model__macros_8hpp/#define-definepar)**(PARAMETER)  |
|  | **[CORE_INTERPRET_AS_X_FUNCTION](/documentation/code/files/model__macros_8hpp/#define-core-interpret-as-x-function)**(MODEL_X, FUNC) <br>Real declaration macro for INTERPRET_AS_X functions.  |
|  | **[INTERPRET_AS_X_FUNCTION_FULL](/documentation/code/files/model__macros_8hpp/#define-interpret-as-x-function-full)**(MODEL_X, FUNC, ADD_FRIEND) <br>Generic declaration macro for INTERPRET_AS_ functions.  |
|  | **[CORE_INTERPRET_AS_X_DEPENDENCY](/documentation/code/files/model__macros_8hpp/#define-core-interpret-as-x-dependency)**(MODEL_X, DEP, TYPE) <br>Add a dependency to an interpret-as-X function.  |
|  | **[MODEL_NAMESPACE](/documentation/code/files/model__macros_8hpp/#define-model-namespace)** <br>Macro to get to model namespace easily.  |
|  | **[USE_MODEL_PIPE](/documentation/code/files/model__macros_8hpp/#define-use-model-pipe)**(MODEL_X)  |

## Detailed Description


**Author**: 

  * Ben Farmer ([benjamin.farmer@monash.edu.au](mailto:benjamin.farmer@monash.edu.au)) 
  * Pat Scott ([patscott@physics.mcgill.ca](mailto:patscott@physics.mcgill.ca)) 


**Date**: 

  * 2013 May, June, July
  * 2013 July, Aug 
  * 2014 Jan, Nov 
  * 2015 Feb


Helper macros for model definitions.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define CORE_DEFINEPARS

```
#define CORE_DEFINEPARS(
    ...
)
  BOOST_PP_SEQ_FOR_EACH(DO_LINK, _, BOOST_PP_TUPLE_TO_SEQ((__VA_ARGS__)))
```


Define multiple model parameters 


### define DO_LINK

```
#define DO_LINK(
    r,
    data,
    elem
)
DEFINEPAR(elem)
```


### define INTERPRET_AS_PARENT_DEPENDENCY

```
#define INTERPRET_AS_PARENT_DEPENDENCY(
    DEP,
    TYPE
)
  INTERPRET_AS_X_DEPENDENCY(PARENT, DEP, TYPE)
```


Wrappers to convert INTERPRET_AS_X macros to INTERPRET_AS_PARENT macros. 


### define CORE_INTERPRET_AS_PARENT_FUNCTION

```
#define CORE_INTERPRET_AS_PARENT_FUNCTION(
    FUNC
)
INTERPRET_AS_X_FUNCTION_FULL(PARENT,FUNC,0)
```


### define MAKE_PRIMARY_MODEL_FUNCTOR_MAIN

```
#define MAKE_PRIMARY_MODEL_FUNCTOR_MAIN(
    FUNCTION,
    CAPABILITY,
    ORIGIN
)
  /* Create the function wrapper object (functor) */                           \
  namespace Functown                                                           \
  {                                                                            \
    primary_model_functor FUNCTION                                             \
     (&ORIGIN::FUNCTION, STRINGIFY(FUNCTION), STRINGIFY(CAPABILITY),           \
     "ModelParameters", STRINGIFY(ORIGIN), ModelDB());                         \
  }                                                                            \
```

Main version of MAKE_FUNCTOR modified to build primary_parameters functors. 

Macros to create and register primary model functors.

We need this extra wrapper in order to define these special functors and add them to the Core's primary model functor list (no other functors allowed here). 


### define MAKE_PRIMARY_MODEL_FUNCTOR_SUPP

```
#define MAKE_PRIMARY_MODEL_FUNCTOR_SUPP(
    FUNCTION
)
  /* Register the functor with the Core. */                                    \
  int CAT(coreg_,FUNCTION) = register_model_functor_core(Functown::FUNCTION);  \
```

Supplementary version of MAKE_FUNCTOR modded for primary_parameters functors. 

### define START_MODEL

```
#define START_MODEL /* Do nothing */
```


### define DEFINEPARS

```
#define DEFINEPARS(
    ...
)
/* Do nothing */
```


### define MAP_TO_CAPABILITY

```
#define MAP_TO_CAPABILITY(
    PARAMETER,
    CAPABILITY
)
/* Do nothing */
```


### define INTERPRET_AS_X_FUNCTION

```
#define INTERPRET_AS_X_FUNCTION(
    MODEL_X,
    FUNC
)
MODULE_INTERPRET_AS_X_FUNCTION(MODEL_X,FUNC)
```


### define INTERPRET_AS_PARENT_FUNCTION

```
#define INTERPRET_AS_PARENT_FUNCTION(
    FUNC
)
MODULE_INTERPRET_AS_X_FUNCTION(PARENT,FUNC)
```


### define INTERPRET_AS_X_DEPENDENCY

```
#define INTERPRET_AS_X_DEPENDENCY(
    MODEL_X,
    DEP,
    TYPE
)
MODULE_INTERPRET_AS_X_DEPENDENCY(MODEL_X, DEP, TYPE)
```


### define START_CAPABILITY

```
#define START_CAPABILITY MODULE_START_CAPABILITY(MODEL)
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
MODULE_DECLARE_FUNCTION(MODEL, FUNCTION, TYPE, CAN_MANAGE, IS_MODEL)
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
MODULE_DECLARE_FUNCTION(MODULE, FUNCTION, TYPE, CAN_MANAGE, IS_MODEL)
```


### define DEPENDENCY

```
#define DEPENDENCY(
    DEP,
    TYPE
)
MODULE_DEPENDENCY(DEP, TYPE, MODEL, FUNCTION, IS_MODEL)
```


### define LONG_DEPENDENCY

```
#define LONG_DEPENDENCY(
    MODULE,
    FUNCTION,
    DEP,
    TYPE
)
MODULE_DEPENDENCY(DEP, TYPE, MODEL, FUNCTION, IS_MODEL)
```


### define NEEDS_MANAGER

```
#define NEEDS_MANAGER(
    ...
)
MODULE_NEEDS_MANAGER_REDIRECT(__VA_ARGS__)
```


### define ALLOWED_MODEL

```
#define ALLOWED_MODEL(
    MODULE,
    FUNCTION,
    MODEL
)
MODULE_ALLOWED_MODEL(MODULE,FUNCTION,MODEL,IS_MODEL)
```


### define ALLOWED_MODEL_DEPENDENCE

```
#define ALLOWED_MODEL_DEPENDENCE(
    MODULE,
    FUNCTION,
    MODEL
)
MODULE_ALLOWED_MODEL(MODULE,FUNCTION,MODEL,IS_MODEL)
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
MODULE_BE_GROUP(GROUP,IS_MODEL)
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
MODULE_BACKEND_REQ(MODEL, FUNCTION, GROUP, REQUIREMENT, TAGS, TYPE, ARGS, IS_VARIABLE, IS_MODEL)
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
MODULE_BACKEND_REQ(MODULE, FUNCTION, GROUP, REQUIREMENT, TAGS, TYPE, ARGS, IS_VARIABLE, IS_MODEL)
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
MODULE_DEPENDENCY(CONDITIONAL_DEPENDENCY, TYPE, MODEL, FUNCTION, IS_MODEL)
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
MODULE_DEPENDENCY(DEP, TYPE, MODEL, FUNCTION, IS_MODEL)
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


### define ALLOW_MODELS

```
#define ALLOW_MODELS(
    ...
)
ALLOW_MODELS_AB(MODEL, FUNCTION, __VA_ARGS__)
```


### define MAKE_PRIMARY_MODEL_FUNCTOR

```
#define MAKE_PRIMARY_MODEL_FUNCTOR(
    FUNCTION,
    CAPABILITY,
    ORIGIN
)
MAKE_PRIMARY_MODEL_FUNCTOR_MAIN(FUNCTION,CAPABILITY,ORIGIN) \
                                                                  MAKE_PRIMARY_MODEL_FUNCTOR_SUPP(FUNCTION)
```


### define MODULE_INTERPRET_AS_X_FUNCTION

```
#define MODULE_INTERPRET_AS_X_FUNCTION(
    MODEL_X,
    FUNC
)
  namespace Gambit                                                             \
  {                                                                            \
    namespace Models                                                           \
    {                                                                          \
      namespace MODEL                                                          \
      {                                                                        \
        /* Declare the user-defined function as defined elsewhere */           \
        extern void FUNC (const ModelParameters&, ModelParameters&);           \
                                                                               \
        /* Let the module source know that this functor is declared*/          \
        namespace Functown { extern module_functor<ModelParameters>            \
                                            CAT(MODEL_X,_parameters); }        \
                                                                               \
        namespace Pipes                                                        \
        {                                                                      \
          namespace CAT(MODEL_X,_parameters)                                   \
          {                                                                    \
            /* Declare the parameters safe-pointer map as external. */         \
            extern std::map<str, const safe_ptr<const double> > Param;                     \
            /* Declare the safe-pointer to the models vector as external. */   \
            extern safe_ptr< std::vector<str> > Models;                        \
            /* Declare the safe pointer to the run options as external. */     \
            extern safe_ptr<Options> runOptions;                               \
          }                                                                    \
        }                                                                      \
      }                                                                        \
    }                                                                          \
  }                                                                            \
```

"In module" version of the INTERPRET_AS_X_FUNCTION macro 

"Rollcall" macros. These are lifted straight from [module_macros_incore.hpp](/documentation/code/files/module__macros__incore_8hpp/#file-elements-module-macros-incore-hpp) but are modified here and there to suit the role of models. 


### define MODULE_INTERPRET_AS_X_DEPENDENCY

```
#define MODULE_INTERPRET_AS_X_DEPENDENCY(
    MODEL_X,
    DEP,
    TYPE
)
MODULE_DEPENDENCY(DEP, TYPE, MODEL, CAT(MODEL_X,_parameters), IS_MODEL)
```

"In module" version of the INTERPRET_AS_X_DEPENDENCY macro 

### define CORE_START_MODEL

```
#define CORE_START_MODEL 
```


Piggybacks off the CORE_START_MODULE_COMMON macro, as we need all the same machinery. 


### define CORE_MAP_TO_CAPABILITY

```
#define CORE_MAP_TO_CAPABILITY(
    PARAMETER,
    CAPABILITY
)

```


Tells the core that the current parameter corresponds to the specified CAPABILITY, so that module functions can then draw upon them like any other capabilities. Draws from CORE_START_CAPABILITY macro. So far we only allow parameters of type double (currently the parameter object cannot store anything else anyway). If we really want to allow integer or maybe complex parameters later we could extend some things in here. 


### define DEFINEPAR

```
#define DEFINEPAR(
    PARAMETER
)
  namespace Gambit                                                             \
  {                                                                            \
    namespace Models                                                           \
    {                                                                          \
      namespace MODEL                                                          \
      {                                                                        \
        /* Tell the functor holding the ModelParameters object to add the new  \
           parameter to its [parameter name, value] map. */                    \
        int CAT(added_,PARAMETER) =                                            \
         add_parameter(Functown::primary_parameters,STRINGIFY(PARAMETER));     \
      }                                                                        \
    }                                                                          \
  }                                                                            \
```


Macro to define parameter. Does not create a corresponding CAPABILITY; use MAP_TO_CAPABILITY to do this after calling [DEFINEPAR(S)](/documentation/code/files/model__macros_8hpp/#define-definepar). 


### define CORE_INTERPRET_AS_X_FUNCTION

```
#define CORE_INTERPRET_AS_X_FUNCTION(
    MODEL_X,
    FUNC
)
INTERPRET_AS_X_FUNCTION_FULL(MODEL_X,FUNC,1)                           \
```

Real declaration macro for INTERPRET_AS_X functions. 

### define INTERPRET_AS_X_FUNCTION_FULL

```
#define INTERPRET_AS_X_FUNCTION_FULL(
    MODEL_X,
    FUNC,
    ADD_FRIEND
)

```

Generic declaration macro for INTERPRET_AS_ functions. 

### define CORE_INTERPRET_AS_X_DEPENDENCY

```
#define CORE_INTERPRET_AS_X_DEPENDENCY(
    MODEL_X,
    DEP,
    TYPE
)
CORE_DEPENDENCY(DEP, TYPE, MODEL, CAT(MODEL_X,_parameters), IS_MODEL)        \
```

Add a dependency to an interpret-as-X function. 

### define MODEL_NAMESPACE

```
#define MODEL_NAMESPACE Gambit::Models::MODEL
```

Macro to get to model namespace easily. 

### define USE_MODEL_PIPE

```
#define USE_MODEL_PIPE(
    MODEL_X
)
  using namespace MODEL_NAMESPACE::Pipes::CAT(MODEL_X,_parameters);             \
```


Macro to easily get the Pipes for an INTERPRET_AS_X function, for retrieving dependencies 


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Helper macros for model definitions.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Ben Farmer
///          (benjamin.farmer@monash.edu.au)
///  \date 2013 May, June, July
///
///  \author Pat Scott
///          (patscott@physics.mcgill.ca)
///  \date 2013 July, Aug
///  \date 2014 Jan, Nov
///  \date 2015 Feb
///
///  *********************************************

#ifndef __model_macros_hpp__
#define __model_macros_hpp__

#include "gambit/Models/orphan.hpp"
#include "gambit/Models/claw_singleton.hpp"
#include "gambit/Utils/util_macros.hpp"
#include "gambit/Utils/boost_fallbacks.hpp"
#include "gambit/Elements/ini_functions.hpp"

#include <boost/preprocessor/seq/for_each.hpp>

#ifdef __model_rollcall_hpp__
  #include "gambit/Elements/module_macros_incore_defs.hpp"
  #ifndef STANDALONE
    #include "gambit/Core/ini_functions.hpp"
  #endif
  #define START_MODEL                                             CORE_START_MODEL
  #define DEFINEPARS(...)                                         CORE_DEFINEPARS(__VA_ARGS__)
  #define MAP_TO_CAPABILITY(PARAMETER,CAPABILITY)                 CORE_MAP_TO_CAPABILITY(PARAMETER,CAPABILITY)
  #define INTERPRET_AS_X_FUNCTION(MODEL_X,FUNC)                   CORE_INTERPRET_AS_X_FUNCTION(MODEL_X,FUNC)
  #define INTERPRET_AS_PARENT_FUNCTION(FUNC)                      CORE_INTERPRET_AS_PARENT_FUNCTION(FUNC)
  #define INTERPRET_AS_X_DEPENDENCY(MODEL_X, DEP, TYPE)           CORE_INTERPRET_AS_X_DEPENDENCY(MODEL_X, DEP, TYPE)
  // "Traditional" module macros
  // These are just copy/pasted from the module versions with small adjustments, like MODULE->MODEL and NOT_MODEL->IS_MODEL
  // (Note: MODULE left as MODULE where it is just a function argument)
  #define START_CAPABILITY                                  CORE_START_CAPABILITY(MODEL, CAPABILITY, IS_MODEL)
  #define LONG_START_CAPABILITY(MODULE, CAPABILITY)         CORE_START_CAPABILITY(MODULE, CAPABILITY, IS_MODEL)
  #define DECLARE_FUNCTION(TYPE, FLAG)                      CORE_DECLARE_FUNCTION(MODEL, CAPABILITY, FUNCTION, TYPE, FLAG, IS_MODEL)
  #define LONG_DECLARE_FUNCTION(MODULE, CAPABILITY, FUNCTION, TYPE, FLAG) CORE_DECLARE_FUNCTION(MODULE, CAPABILITY, FUNCTION, TYPE, FLAG, IS_MODEL)
  #define NEEDS_MANAGER(...)                                CORE_NEEDS_MANAGER(__VA_ARGS__)
  #define DEPENDENCY(DEP, TYPE)                             CORE_DEPENDENCY(DEP, TYPE, MODEL, FUNCTION, IS_MODEL)
  #define LONG_DEPENDENCY(MODULE, FUNCTION, DEP, TYPE)      CORE_DEPENDENCY(DEP, TYPE, MODULE, FUNCTION, IS_MODEL)
  #define ALLOW_MODELS(...)                                 ALLOW_MODELS_AB(MODEL, FUNCTION, __VA_ARGS__)
  #define ALLOWED_MODEL(MODULE,FUNCTION,MODEL)              CORE_ALLOWED_MODEL(MODULE,FUNCTION,MODEL,IS_MODEL)
  #define ALLOWED_MODEL_DEPENDENCE(MODULE,FUNCTION,MODEL)   CORE_ALLOW_MODEL_DEPENDENCE(MODULE,FUNCTION,MODEL,IS_MODEL)
  #define ALLOW_MODEL_COMBINATION(...)                      CORE_ALLOW_MODEL_COMBINATION(MODEL,FUNCTION,IS_MODEL,(__VA_ARGS__))
  #define MODEL_GROUP(GROUPNAME,GROUP)                      CORE_MODEL_GROUP(MODEL,FUNCTION,GROUPNAME,GROUP,IS_MODEL)
  #define DECLARE_BACKEND_REQ(GROUP, REQUIREMENT, TAGS, TYPE, ARGS, IS_VARIABLE) \
                                                            CORE_BACKEND_REQ(MODEL, CAPABILITY, FUNCTION, GROUP, REQUIREMENT, TAGS, TYPE, ARGS, IS_VARIABLE, IS_MODEL)
  #define LONG_DECLARE_BACKEND_REQ(MODULE, CAPABILITY, FUNCTION, GROUP, REQUIREMENT, TAGS, TYPE, ARGS, IS_VARIABLE) \
                                                            CORE_BACKEND_REQ(MODULE, CAPABILITY, FUNCTION, GROUP, REQUIREMENT, TAGS, TYPE, ARGS, IS_VARIABLE, IS_MODEL)
  #define BE_GROUP(GROUP)                                   CORE_BE_GROUP(GROUP,IS_MODEL)
  #define ACTIVATE_BACKEND_REQ_FOR_MODELS(MODELS,TAGS)      CORE_BE_MODEL_RULE(MODELS,TAGS,IS_MODEL)
  #define BACKEND_OPTION(BACKEND_AND_VERSIONS,TAGS)         LONG_BACKEND_OPTION(MODEL, CAPABILITY, FUNCTION, BACKEND_AND_VERSIONS,TAGS)
  #define LONG_BACKEND_OPTION(MODULE, CAPABILITY, FUNCTION, BACKEND_AND_VERSIONS,TAGS) \
                                                            CORE_BACKEND_OPTION(MODULE, CAPABILITY, FUNCTION, BACKEND_AND_VERSIONS,TAGS, IS_MODEL)
  #define FORCE_SAME_BACKEND(...)                           CORE_FORCE_SAME_BACKEND(IS_MODEL,__VA_ARGS__)
  #define START_CONDITIONAL_DEPENDENCY(TYPE)                CORE_START_CONDITIONAL_DEPENDENCY(MODEL, CAPABILITY, \
                                                             FUNCTION, CONDITIONAL_DEPENDENCY, TYPE, IS_MODEL)
  #define ACTIVATE_DEP_BE(BACKEND_REQ, BACKEND, VERSTRING)  CORE_ACTIVATE_DEP_BE(BACKEND_REQ, BACKEND, VERSTRING, IS_MODEL)
  #define ACTIVATE_FOR_MODELS(...)                          ACTIVATE_DEP_MODEL(MODEL, CAPABILITY, FUNCTION, CONDITIONAL_DEPENDENCY, IS_MODEL, #__VA_ARGS__)
  #define MODEL_CONDITIONAL_DEPENDENCY(DEP, TYPE, ...)      CORE_START_CONDITIONAL_DEPENDENCY(MODEL, CAPABILITY, FUNCTION, DEP, TYPE, IS_MODEL) \
                                                            ACTIVATE_DEP_MODEL(MODEL, CAPABILITY, FUNCTION, DEP, IS_MODEL #__VA_ARGS__)
  #define CLASSLOAD_NEEDED(BACKEND, VERSION)               CORE_CLASSLOAD_NEEDED(BACKEND, VERSION, IS_MODEL)
#else
  #include "gambit/Elements/module_macros_inmodule_defs.hpp"
  #define START_MODEL                                       /* Do nothing */
  #define DEFINEPARS(...)                                   /* Do nothing */
  #define MAP_TO_CAPABILITY(PARAMETER,CAPABILITY)           /* Do nothing */
  #define INTERPRET_AS_X_FUNCTION(MODEL_X,FUNC)             MODULE_INTERPRET_AS_X_FUNCTION(MODEL_X,FUNC)
  #define INTERPRET_AS_PARENT_FUNCTION(FUNC)                MODULE_INTERPRET_AS_X_FUNCTION(PARENT,FUNC)
  #define INTERPRET_AS_X_DEPENDENCY(MODEL_X, DEP, TYPE)     MODULE_INTERPRET_AS_X_DEPENDENCY(MODEL_X, DEP, TYPE)
  // "Traditional" module macros
  #define START_CAPABILITY                                  MODULE_START_CAPABILITY(MODEL)
  #define LONG_START_CAPABILITY(MODULE, C)                  MODULE_START_CAPABILITY(MODULE)
  #define DECLARE_FUNCTION(TYPE, CAN_MANAGE)                MODULE_DECLARE_FUNCTION(MODEL, FUNCTION, TYPE, CAN_MANAGE, IS_MODEL)
  #define LONG_DECLARE_FUNCTION(MODULE, C, FUNCTION, TYPE, CAN_MANAGE) \
                                                            MODULE_DECLARE_FUNCTION(MODULE, FUNCTION, TYPE, CAN_MANAGE, IS_MODEL)
  #define DEPENDENCY(DEP, TYPE)                             MODULE_DEPENDENCY(DEP, TYPE, MODEL, FUNCTION, IS_MODEL)
  #define LONG_DEPENDENCY(MODULE, FUNCTION, DEP, TYPE)      MODULE_DEPENDENCY(DEP, TYPE, MODEL, FUNCTION, IS_MODEL)
  #define NEEDS_MANAGER(...)                                MODULE_NEEDS_MANAGER_REDIRECT(__VA_ARGS__)
  #define ALLOWED_MODEL(MODULE,FUNCTION,MODEL)              MODULE_ALLOWED_MODEL(MODULE,FUNCTION,MODEL,IS_MODEL)
  #define ALLOWED_MODEL_DEPENDENCE(MODULE,FUNCTION,MODEL)   MODULE_ALLOWED_MODEL(MODULE,FUNCTION,MODEL,IS_MODEL)
  #define ALLOW_MODEL_COMBINATION(...)                      DUMMYARG(__VA_ARGS__)
  #define MODEL_GROUP(GROUPNAME, GROUP)                     DUMMYARG(GROUPNAME, GROUP)

  #define BE_GROUP(GROUP)                                   MODULE_BE_GROUP(GROUP,IS_MODEL)
  #define DECLARE_BACKEND_REQ(GROUP, REQUIREMENT, TAGS, TYPE, ARGS, IS_VARIABLE) \
                                                            MODULE_BACKEND_REQ(MODEL, FUNCTION, GROUP, REQUIREMENT, TAGS, TYPE, ARGS, IS_VARIABLE, IS_MODEL)
  #define LONG_DECLARE_BACKEND_REQ(MODULE, C, FUNCTION, GROUP, REQUIREMENT, TAGS, TYPE, ARGS, IS_VARIABLE) \
                                                            MODULE_BACKEND_REQ(MODULE, FUNCTION, GROUP, REQUIREMENT, TAGS, TYPE, ARGS, IS_VARIABLE, IS_MODEL)
  #define ACTIVATE_BACKEND_REQ_FOR_MODELS(MODELS,TAGS)      DUMMYARG(MODELS,TAGS)
  #define START_CONDITIONAL_DEPENDENCY(TYPE)                MODULE_DEPENDENCY(CONDITIONAL_DEPENDENCY, TYPE, MODEL, FUNCTION, IS_MODEL)
  #define ACTIVATE_DEP_BE(BACKEND_REQ, BACKEND, VERSTRING)  DUMMYARG(BACKEND_REQ, BACKEND, VERSTRING)
  #define ACTIVATE_FOR_MODELS(...)                          DUMMYARG(__VA_ARGS__)
  #define MODEL_CONDITIONAL_DEPENDENCY(DEP, TYPE, ...)      MODULE_DEPENDENCY(DEP, TYPE, MODEL, FUNCTION, IS_MODEL)
  #define BACKEND_OPTION(BACKEND_AND_VERSIONS,TAGS)         DUMMYARG(BACKEND_AND_VERSIONS,TAGS)
  #define LONG_BACKEND_OPTION(MODULE, CAPABILITY, FUNCTION, BACKEND_AND_VERSIONS,TAGS) \
                                                            DUMMYARG(BACKEND_AND_VERSIONS,TAGS)
  #define FORCE_SAME_BACKEND(...)                           DUMMYARG(__VA_ARGS__)
  #define CLASSLOAD_NEEDED(...)                             DUMMYARG(__VA_ARGS__)

#endif
#define ALLOW_MODELS(...)                                   ALLOW_MODELS_AB(MODEL, FUNCTION, __VA_ARGS__)

#ifndef STANDALONE
  #define MAKE_PRIMARY_MODEL_FUNCTOR(FUNCTION,CAPABILITY,ORIGIN)  MAKE_PRIMARY_MODEL_FUNCTOR_MAIN(FUNCTION,CAPABILITY,ORIGIN) \
                                                                  MAKE_PRIMARY_MODEL_FUNCTOR_SUPP(FUNCTION)
#else
  #define MAKE_PRIMARY_MODEL_FUNCTOR(FUNCTION,CAPABILITY,ORIGIN)  MAKE_PRIMARY_MODEL_FUNCTOR_MAIN(FUNCTION,CAPABILITY,ORIGIN)
#endif

// MACRO DEFINITIONS.

//  ****************************************************************************
/// "Rollcall" macros. These are lifted straight from module_macros_incore.hpp
/// but are modified here and there to suit the role of models.

/// "In module" version of the INTERPRET_AS_X_FUNCTION macro
#define MODULE_INTERPRET_AS_X_FUNCTION(MODEL_X,FUNC)                           \
  namespace Gambit                                                             \
  {                                                                            \
    namespace Models                                                           \
    {                                                                          \
      namespace MODEL                                                          \
      {                                                                        \
        /* Declare the user-defined function as defined elsewhere */           \
        extern void FUNC (const ModelParameters&, ModelParameters&);           \
                                                                               \
        /* Let the module source know that this functor is declared*/          \
        namespace Functown { extern module_functor<ModelParameters>            \
                                            CAT(MODEL_X,_parameters); }        \
                                                                               \
        namespace Pipes                                                        \
        {                                                                      \
          namespace CAT(MODEL_X,_parameters)                                   \
          {                                                                    \
            /* Declare the parameters safe-pointer map as external. */         \
            extern std::map<str, const safe_ptr<const double> > Param;                     \
            /* Declare the safe-pointer to the models vector as external. */   \
            extern safe_ptr< std::vector<str> > Models;                        \
            /* Declare the safe pointer to the run options as external. */     \
            extern safe_ptr<Options> runOptions;                               \
          }                                                                    \
        }                                                                      \
      }                                                                        \
    }                                                                          \
  }                                                                            \

/// "In module" version of the INTERPRET_AS_X_DEPENDENCY macro
#define MODULE_INTERPRET_AS_X_DEPENDENCY(MODEL_X, DEP, TYPE)                  \
  MODULE_DEPENDENCY(DEP, TYPE, MODEL, CAT(MODEL_X,_parameters), IS_MODEL)


/// Piggybacks off the CORE_START_MODULE_COMMON macro, as we need all the same
/// machinery.
#define CORE_START_MODEL                                                       \
                                                                               \
  namespace Gambit                                                             \
  {                                                                            \
    ADD_TAG_IN_CURRENT_NAMESPACE(primary_parameters)                           \
    ADD_TAG_IN_CURRENT_NAMESPACE(CAT(MODEL,_parameters))                       \
    namespace Models                                                           \
    {                                                                          \
      ADD_MODEL_TAG_IN_CURRENT_NAMESPACE(MODEL)                                \
                                                                               \
      namespace MODEL                                                          \
      {                                                                        \
                                                                               \
        /* Basic machinery, same as for modules                                \
           (macro from module_macros_incore.hpp) */                            \
        CORE_START_MODULE_COMMON_MAIN(MODEL)                                   \
                                                                               \
        /* Add the model to GAMBIT model database */                           \
        int model_rego = add_model(STRINGIFY(MODEL), STRINGIFY(PARENT));       \
                                                                               \
        /* Functor's actual "calculate" function.  Doesn't do anything. */     \
        void primary_parameters (ModelParameters&) {}                          \
                                                                               \
        /* Wrap it up in a primary_model_functor */                            \
        MAKE_PRIMARY_MODEL_FUNCTOR(primary_parameters, CAT(MODEL,_parameters), \
                                   MODEL)                                      \
                                                                               \
        /* Ini-function to set the name of the model hosted by the
           ModelParameters object  */                                          \
        int added_model_name =                                                 \
         set_model_name(Functown::primary_parameters,STRINGIFY(MODEL));        \
      }                                                                        \
                                                                               \
      /* Make the functor exclusive to this model and its descendants */       \
      CORE_ALLOW_MODEL(MODEL,primary_parameters,MODEL)                         \
                                                                               \
    }                                                                          \
  }                                                                            \



/// Tells the core that the current parameter corresponds to the specified
/// CAPABILITY, so that module functions can then draw upon them like any
/// other capabilities. Draws from CORE_START_CAPABILITY macro.
/// So far we only allow parameters of type double (currently the parameter
/// object cannot store anything else anyway). If we really want to allow
/// integer or maybe complex parameters later we could extend some things in
/// here.
#define CORE_MAP_TO_CAPABILITY(PARAMETER,CAPABILITY)                           \
                                                                               \
  namespace Gambit                                                             \
  {                                                                            \
                                                                               \
    /* Add CAPABILITY to global set of tags of known module capabilities/deps*/\
    ADD_TAG_IN_CURRENT_NAMESPACE(CAPABILITY)                                   \
                                                                               \
    namespace Models                                                           \
    {                                                                          \
                                                                               \
      namespace MODEL                                                          \
      {                                                                        \
                                                                               \
        /* Add PARAMETER to set of tags of known module functions.*/           \
        ADD_TAG_IN_CURRENT_NAMESPACE(PARAMETER)                                \
                                                                               \
        /* The wrapper function which extracts the value of PARAMETER from     \
           the parameter object. This is the analogue of a module function,    \
           and is what will be wrapped in a functor for processing by the      \
           core */                                                             \
        /* Just the prototype here: defined a bit later on */                  \
        void PARAMETER (double &);                                             \
                                                                               \
        /* Wrap it up in a functor (macro from module_macros_incore.hpp) */    \
        MAKE_FUNCTOR(PARAMETER,double,CAPABILITY,MODEL,0)                      \
                                                                               \
      }                                                                        \
                                                                               \
      /* Make the functor exclusive to this model and its descendants */       \
      CORE_ALLOW_MODEL(MODEL,PARAMETER,MODEL)                                  \
                                                                               \
      /* Create dependency on the parameters of MODEL */                       \
      /* TODO: Check whether there is a more elegant solution */               \
      CORE_ALLOWED_MODEL_ARRANGE_DEP(MODEL,PARAMETER,MODEL)                    \
                                                                               \
    }                                                                          \
                                                                               \
  }                                                                            \
                                                                               \
  /* Define the actual parameter setting function, now that we have the
     functor and its dependency */                                             \
  namespace Gambit                                                             \
  {                                                                            \
                                                                               \
    namespace Models                                                           \
    {                                                                          \
                                                                               \
      namespace MODEL                                                          \
      {                                                                        \
                                                                               \
        /* The wrapper function which extracts the value of PARAMETER from
           the parameter object. This is the analogue of a module function,
           and is what will be wrapped in a functor for processing by the
           core */                                                             \
        void PARAMETER (double &result)                                        \
        {                                                                      \
          result = *Pipes::PARAMETER::Param.at(STRINGIFY(PARAMETER));          \
        }                                                                      \
                                                                               \
      }                                                                        \
                                                                               \
    }                                                                          \
                                                                               \
  }                                                                            \

/// Macro to define parameter.  Does not create a corresponding CAPABILITY;
/// use MAP_TO_CAPABILITY to do this after calling DEFINEPAR(S).
#define DEFINEPAR(PARAMETER)                                                   \
  namespace Gambit                                                             \
  {                                                                            \
    namespace Models                                                           \
    {                                                                          \
      namespace MODEL                                                          \
      {                                                                        \
        /* Tell the functor holding the ModelParameters object to add the new  \
           parameter to its [parameter name, value] map. */                    \
        int CAT(added_,PARAMETER) =                                            \
         add_parameter(Functown::primary_parameters,STRINGIFY(PARAMETER));     \
      }                                                                        \
    }                                                                          \
  }                                                                            \

/// Define multiple model parameters
/// @{
#define CORE_DEFINEPARS(...)                                                   \
  BOOST_PP_SEQ_FOR_EACH(DO_LINK, _, BOOST_PP_TUPLE_TO_SEQ((__VA_ARGS__)))
#define DO_LINK(r,data,elem) DEFINEPAR(elem)
/// @}

/// Real declaration macro for INTERPRET_AS_X functions.
#define CORE_INTERPRET_AS_X_FUNCTION(MODEL_X,FUNC)                             \
        INTERPRET_AS_X_FUNCTION_FULL(MODEL_X,FUNC,1)                           \

/// Generic declaration macro for INTERPRET_AS_ functions.
#define INTERPRET_AS_X_FUNCTION_FULL(MODEL_X,FUNC,ADD_FRIEND)                  \
  namespace Gambit                                                             \
  {                                                                            \
                                                                               \
    /* Add tags which specify that MODEL_X_parameters is a known capability/dep\
    in GAMBIT. */                                                              \
    ADD_TAG_IN_CURRENT_NAMESPACE(CAT(MODEL_X,_parameters))                     \
                                                                               \
    namespace Models                                                           \
    {                                                                          \
                                                                               \
      namespace MODEL                                                          \
      {                                                                        \
                                                                               \
        /* Add MODEL_X_parameters to the set of tags of known functions        \
        provided by this model. */                                             \
        ADD_TAG_IN_CURRENT_NAMESPACE(CAT(MODEL_X,_parameters))                 \
        ADD_TAG_IN_CURRENT_NAMESPACE(FUNC)                                     \
                                                                               \
        /* The function which computes the MODEL_X_parameters object. This     \
           is the analogue of a module function, and is what will be wrapped   \
           in a functor for processing by the core                             \
           Note: CODE must be enclosed in braces. */                           \
        /* Register (prototype) the function */                                \
        void CAT(MODEL_X,_parameters) (ModelParameters &);                     \
                                                                               \
        /* Wrap it up in a functor (macro from module_macros_incore.hpp) */    \
        MAKE_FUNCTOR(CAT(MODEL_X,_parameters),ModelParameters,                 \
         CAT(MODEL_X,_parameters),MODEL,0)                                     \
                                                                               \
        /* Call a function that tells the functor to take its parameter        \
           definition from MODEL_X's primary_parameters functor, and           \
           adds MODEL_X as a friend of MODEL if it is not a parent. */         \
        const int CAT(pars_for_,MODEL_X) =                                     \
         copy_parameters(MODEL_X::Functown::primary_parameters,                \
          Functown::CAT(MODEL_X,_parameters),                                  \
          BOOST_PP_IIF(ADD_FRIEND,true,false),                                 \
          STRINGIFY(MODEL), STRINGIFY(MODEL_X));                               \
                                                                               \
      }                                                                        \
                                                                               \
    }                                                                          \
                                                                               \
  }                                                                            \
                                                                               \
  /* Automatically add a dependency on the host model's parameters */          \
  INTERPRET_AS_X_DEPENDENCY(MODEL_X,CAT(MODEL,_parameters),ModelParameters)    \
                                                                               \
  namespace Gambit                                                             \
  {                                                                            \
                                                                               \
    namespace Models                                                           \
    {                                                                          \
                                                                               \
      namespace MODEL                                                          \
      {                                                                        \
                                                                               \
        /* Prototype the user-defined function */                              \
        void FUNC (const ModelParameters&, ModelParameters&);                  \
                                                                               \
        /* The actual definition of the interpret_as_X "module" function */    \
        void CAT(MODEL_X,_parameters) (ModelParameters &model_x_params)        \
        {                                                                      \
          /* Collect MODEL's parameters via dependency system */               \
          using namespace Pipes::CAT(MODEL_X,_parameters);                     \
          const ModelParameters& model_params = *Dep::CAT(MODEL,_parameters);  \
                                                                               \
          /* Run user-supplied code (which must take result as an
             argument, and set the parameters it contains as desired) */       \
          FUNC (model_params,model_x_params);                                  \
        }                                                                      \
                                                                               \
      }                                                                        \
                                                                               \
      /* Make the functor exclusive to this model and its descendants */       \
      CORE_ALLOW_MODEL(MODEL,CAT(MODEL_X,_parameters),MODEL)                   \
                                                                               \
    }                                                                          \
                                                                               \
  }                                                                            \


/// Add a dependency to an interpret-as-X function.
#define CORE_INTERPRET_AS_X_DEPENDENCY(MODEL_X, DEP, TYPE)                     \
  CORE_DEPENDENCY(DEP, TYPE, MODEL, CAT(MODEL_X,_parameters), IS_MODEL)        \

/// Wrappers to convert INTERPRET_AS_X macros to INTERPRET_AS_PARENT macros.
/// @{
#define INTERPRET_AS_PARENT_DEPENDENCY(DEP, TYPE)                              \
  INTERPRET_AS_X_DEPENDENCY(PARENT, DEP, TYPE)
#define CORE_INTERPRET_AS_PARENT_FUNCTION(FUNC)                                \
  INTERPRET_AS_X_FUNCTION_FULL(PARENT,FUNC,0)
/// @}

/// Macro to get to model namespace easily
#define MODEL_NAMESPACE Gambit::Models::MODEL

/// Macro to easily get the Pipes for an INTERPRET_AS_X function, for retrieving
/// dependencies
#define USE_MODEL_PIPE(MODEL_X)                                                 \
  using namespace MODEL_NAMESPACE::Pipes::CAT(MODEL_X,_parameters);             \


/// Macros to create and register primary model functors.
///
/// We need this extra wrapper in order to define these special functors and add
/// them to the Core's primary model functor list (no other functors allowed here).
/// @{

/// Main version of MAKE_FUNCTOR modified to build primary_parameters functors.
#define MAKE_PRIMARY_MODEL_FUNCTOR_MAIN(FUNCTION,CAPABILITY,ORIGIN)            \
  /* Create the function wrapper object (functor) */                           \
  namespace Functown                                                           \
  {                                                                            \
    primary_model_functor FUNCTION                                             \
     (&ORIGIN::FUNCTION, STRINGIFY(FUNCTION), STRINGIFY(CAPABILITY),           \
     "ModelParameters", STRINGIFY(ORIGIN), ModelDB());                         \
  }                                                                            \

/// Supplementary version of MAKE_FUNCTOR modded for primary_parameters functors.
#define MAKE_PRIMARY_MODEL_FUNCTOR_SUPP(FUNCTION)                              \
  /* Register the functor with the Core. */                                    \
  int CAT(coreg_,FUNCTION) = register_model_functor_core(Functown::FUNCTION);  \

/// @}

#endif /* defined(__model_macros_hpp__) */
```


-------------------------------

Updated on 2025-02-12 at 16:10:34 +0000
