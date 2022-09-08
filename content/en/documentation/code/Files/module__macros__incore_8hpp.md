---
title: "file Elements/module_macros_incore.hpp"

description: "[No description available]"

---

# file Elements/module_macros_incore.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[START_MODULE](/documentation/code/files/module__macros__incore_8hpp/#define-start-module)** <br>Registers the current [MODULE].  |
|  | **[START_CAPABILITY](/documentation/code/files/module__macros__incore_8hpp/#define-start-capability)**  |
|  | **[LONG_START_CAPABILITY](/documentation/code/files/module__macros__incore_8hpp/#define-long-start-capability)**(MODULE, CAPABILITY) <br>Long (all argument) version of [START_CAPABILITY](/documentation/code/files/module__macros__incore_8hpp/#define-start-capability).  |
|  | **[DECLARE_FUNCTION](/documentation/code/files/module__macros__incore_8hpp/#define-declare-function)**(TYPE, FLAG)  |
|  | **[LONG_DECLARE_FUNCTION](/documentation/code/files/module__macros__incore_8hpp/#define-long-declare-function)**(MODULE, CAPABILITY, FUNCTION, TYPE, FLAG) <br>Long (all argument) version of [DECLARE_FUNCTION](/documentation/code/files/module__macros__incore_8hpp/#define-declare-function).  |
|  | **[NEEDS_MANAGER](/documentation/code/files/module__macros__incore_8hpp/#define-needs-manager)**(...)  |
|  | **[DEPENDENCY](/documentation/code/files/module__macros__incore_8hpp/#define-dependency)**(DEP, TYPE)  |
|  | **[LONG_DEPENDENCY](/documentation/code/files/module__macros__incore_8hpp/#define-long-dependency)**(MODULE, FUNCTION, DEP, TYPE) <br>Long (all argument) version of [DEPENDENCY](/documentation/code/files/module__macros__incore_8hpp/#define-dependency).  |
|  | **[ALLOW_MODELS](/documentation/code/files/module__macros__incore_8hpp/#define-allow-models)**(...)  |
|  | **[ALLOWED_MODEL](/documentation/code/files/module__macros__incore_8hpp/#define-allowed-model)**(MODULE, FUNCTION, MODEL)  |
|  | **[ALLOWED_MODEL_DEPENDENCE](/documentation/code/files/module__macros__incore_8hpp/#define-allowed-model-dependence)**(MODULE, FUNCTION, MODEL)  |
|  | **[ALLOW_MODEL_COMBINATION](/documentation/code/files/module__macros__incore_8hpp/#define-allow-model-combination)**(...)  |
|  | **[MODEL_GROUP](/documentation/code/files/module__macros__incore_8hpp/#define-model-group)**(GROUPNAME, GROUP) <br>Define a model GROUP of name GROUPNAME for use with ALLOW_MODEL_COMBINATION.  |
|  | **[DECLARE_BACKEND_REQ](/documentation/code/files/module__macros__incore_8hpp/#define-declare-backend-req)**(GROUP, REQUIREMENT, TAGS, TYPE, ARGS, IS_VARIABLE)  |
|  | **[LONG_DECLARE_BACKEND_REQ](/documentation/code/files/module__macros__incore_8hpp/#define-long-declare-backend-req)**(MODULE, CAPABILITY, FUNCTION, GROUP, REQUIREMENT, TAGS, TYPE, ARGS, IS_VARIABLE)  |
|  | **[BE_GROUP](/documentation/code/files/module__macros__incore_8hpp/#define-be-group)**(GROUP) <br>Declare a backend group, from which one backend requirement must be activated.  |
|  | **[ACTIVATE_BACKEND_REQ_FOR_MODELS](/documentation/code/files/module__macros__incore_8hpp/#define-activate-backend-req-for-models)**(MODELS, TAGS)  |
|  | **[BACKEND_OPTION](/documentation/code/files/module__macros__incore_8hpp/#define-backend-option)**(BACKEND_AND_VERSIONS, TAGS)  |
|  | **[LONG_BACKEND_OPTION](/documentation/code/files/module__macros__incore_8hpp/#define-long-backend-option)**(MODULE, CAPABILITY, FUNCTION, BACKEND_AND_VERSIONS, TAGS)  |
|  | **[FORCE_SAME_BACKEND](/documentation/code/files/module__macros__incore_8hpp/#define-force-same-backend)**(...)  |
|  | **[START_CONDITIONAL_DEPENDENCY](/documentation/code/files/module__macros__incore_8hpp/#define-start-conditional-dependency)**(TYPE)  |
|  | **[ACTIVATE_DEP_BE](/documentation/code/files/module__macros__incore_8hpp/#define-activate-dep-be)**(BACKEND_REQ, BACKEND, VERSTRING)  |
|  | **[ACTIVATE_FOR_MODELS](/documentation/code/files/module__macros__incore_8hpp/#define-activate-for-models)**(...)  |
|  | **[MODEL_CONDITIONAL_DEPENDENCY](/documentation/code/files/module__macros__incore_8hpp/#define-model-conditional-dependency)**(DEP, TYPE, ...) <br>Quick, one-line declaration of model-conditional dependencies.  |
|  | **[CLASSLOAD_NEEDED](/documentation/code/files/module__macros__incore_8hpp/#define-classload-needed)**(BACKEND, VERSION)  |

## Detailed Description


**Author**: 

  * Pat Scott ([patscott@physics.mcgill.ca](mailto:patscott@physics.mcgill.ca)) 
  * Abram Krislock ([abram.krislock@fysik.su.se](mailto:abram.krislock@fysik.su.se)) 
  * Christoph Weniger ([c.weniger@uva.nl](mailto:c.weniger@uva.nl)) 
  * Anders Kvellestad ([anders.kvellestad@fys.uio.no](mailto:anders.kvellestad@fys.uio.no)) 
  * Ben Farmer ([b.farmer@imperial.ac.uk](mailto:b.farmer@imperial.ac.uk)) 


**Date**: 

  * 2012 Nov 
  * 2013,14 Foreverrrrr
  * 2013 Jan, Feb
  * 2013 Jan, Feb, 2014 Jan
  * 2013 Nov
  * 2019 Jul


Redirection macros for generic observable and likelihood function macro definitions, for inclusion from the Core.

Note here that [FUNCTION ] is the actual module function name, whereas both [CAPABILITY ] and all _DEPs_ refer to the abstract physical quantities that functions may provide or require. Thus, the provides() methods expect a quantity input (i.e. corresponding to a [CAPABILITY]), the requires() methods expect a quantity input for the dependency but a function name input (i.e. corresponding to a [FUNCTION]) for the actual dependent function, and all other things operate on the basis of the function name, not the quantity that is calculated.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define START_MODULE

```
#define START_MODULE CORE_START_MODULE
```

Registers the current [MODULE]. 

### define START_CAPABILITY

```
#define START_CAPABILITY CORE_START_CAPABILITY(MODULE, CAPABILITY, NOT_MODEL)
```


Registers the current [CAPABILITY] of the current [MODULE]. 


### define LONG_START_CAPABILITY

```
#define LONG_START_CAPABILITY(
    MODULE,
    CAPABILITY
)
CORE_START_CAPABILITY(MODULE, CAPABILITY, NOT_MODEL)
```

Long (all argument) version of [START_CAPABILITY](/documentation/code/files/module__macros__incore_8hpp/#define-start-capability). 

### define DECLARE_FUNCTION

```
#define DECLARE_FUNCTION(
    TYPE,
    FLAG
)
CORE_DECLARE_FUNCTION(MODULE, CAPABILITY, FUNCTION, TYPE, FLAG, NOT_MODEL)
```


Registers the current [FUNCTION] of the current [MODULE] as a provider of the current [CAPABILITY], returning a result of type _TYPE_. 


### define LONG_DECLARE_FUNCTION

```
#define LONG_DECLARE_FUNCTION(
    MODULE,
    CAPABILITY,
    FUNCTION,
    TYPE,
    FLAG
)
CORE_DECLARE_FUNCTION(MODULE, CAPABILITY, FUNCTION, TYPE, FLAG, NOT_MODEL)
```

Long (all argument) version of [DECLARE_FUNCTION](/documentation/code/files/module__macros__incore_8hpp/#define-declare-function). 

### define NEEDS_MANAGER

```
#define NEEDS_MANAGER(
    ...
)
CORE_NEEDS_MANAGER(__VA_ARGS__)
```


Indicates that the current [FUNCTION] of the current [MODULE] must be managed by another function (in the same module or another) that calls it from within a loop. May be called with one or two arguments: _LOOPMAN_ (capability of the required manager; required) and _TYPE_ (type of the required manager; not required). Will provide a dependency pipe within the function if and only if _TYPE_ is present and non-void. 


### define DEPENDENCY

```
#define DEPENDENCY(
    DEP,
    TYPE
)
CORE_DEPENDENCY(DEP, TYPE, MODULE, FUNCTION, NOT_MODEL)
```


Indicate that the current [FUNCTION] depends on the presence of another module function that can supply capability _DEP_, with return type _TYPE_. 


### define LONG_DEPENDENCY

```
#define LONG_DEPENDENCY(
    MODULE,
    FUNCTION,
    DEP,
    TYPE
)
CORE_DEPENDENCY(DEP, TYPE, MODULE, FUNCTION, NOT_MODEL)
```

Long (all argument) version of [DEPENDENCY](/documentation/code/files/module__macros__incore_8hpp/#define-dependency). 

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
CORE_ALLOWED_MODEL(MODULE,FUNCTION,MODEL,NOT_MODEL)
```


Indicate that the current [FUNCTION] may only be used with specific model _MODEL_, or combinations given via ALLOW_MODEL_COMBINATION. If both this and ALLOW_MODEL_COMBINATION are absent, all models are allowed, but model parameters will not generally be accessible from within the module funtion. 


### define ALLOWED_MODEL_DEPENDENCE

```
#define ALLOWED_MODEL_DEPENDENCE(
    MODULE,
    FUNCTION,
    MODEL
)
CORE_ALLOW_MODEL_DEPENDENCE(MODULE,FUNCTION,MODEL,NOT_MODEL)
```


Indicate that the current [FUNCTION] may be used with a specific model _MODEL_, but only in combination with others given via ALLOW_MODEL_COMBINATION. 


### define ALLOW_MODEL_COMBINATION

```
#define ALLOW_MODEL_COMBINATION(
    ...
)
CORE_ALLOW_MODEL_COMBINATION(MODULE,FUNCTION,NOT_MODEL,(__VA_ARGS__))
```


Indicate that the current [FUNCTION] may only be used with the specific model combination given, with other combinations passed in the same way, or with individual models speficied via [ALLOW_MODEL(S)](/documentation/code/files/module__macros__common_8hpp/#define-allow-model). If both this and [ALLOW_MODEL(s)](/documentation/code/files/module__macros__common_8hpp/#define-allow-model) are absent, all models are allowed but no model parameters will be accessible from within the module funtion. 


### define MODEL_GROUP

```
#define MODEL_GROUP(
    GROUPNAME,
    GROUP
)
CORE_MODEL_GROUP(MODULE,FUNCTION,GROUPNAME,GROUP,NOT_MODEL)
```

Define a model GROUP of name GROUPNAME for use with ALLOW_MODEL_COMBINATION. 

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
CORE_BACKEND_REQ(MODULE, CAPABILITY, FUNCTION, GROUP, REQUIREMENT, TAGS, TYPE, ARGS, IS_VARIABLE, NOT_MODEL)
```


BACKEND_REQ indicates that the current [FUNCTION] requires one backend variable or function to be available from a capability group _GROUP_, and then declares a viable member of that group, with capability _REQUIREMENT_, type _TYPE_ and (in the case of functions) arguments _ARGS_. BACKEND_REQ also allows the user to specify a list of _TAGS_ that apply to this specific group member, which can then be used for easily implementing rules for choosing between different members of the same _GROUP_. Note that _GROUPs_ are automatically declared the first time that they are mentioned in a BACKEND_REQ statement. 


### define LONG_DECLARE_BACKEND_REQ

```
#define LONG_DECLARE_BACKEND_REQ(
    MODULE,
    CAPABILITY,
    FUNCTION,
    GROUP,
    REQUIREMENT,
    TAGS,
    TYPE,
    ARGS,
    IS_VARIABLE
)
CORE_BACKEND_REQ(MODULE, CAPABILITY, FUNCTION, GROUP, REQUIREMENT, TAGS, TYPE, ARGS, IS_VARIABLE, NOT_MODEL)
```


### define BE_GROUP

```
#define BE_GROUP(
    GROUP
)
CORE_BE_GROUP(GROUP,NOT_MODEL)
```

Declare a backend group, from which one backend requirement must be activated. 

### define ACTIVATE_BACKEND_REQ_FOR_MODELS

```
#define ACTIVATE_BACKEND_REQ_FOR_MODELS(
    MODELS,
    TAGS
)
CORE_BE_MODEL_RULE(MODELS,TAGS,NOT_MODEL)
```


Define a rule that uses TAGS to determine which backend requirements of the current [FUNCTION] are explicitly activated when one or more models from the set MODELS are being scanned. Declaring this rule makes backend requirements that match one or more TAGS conditional on the model being scanned. Backend requirements that do not match any such rule are considered unconditional, and are activated regardless of the model(s) being scanned. Note that all rules have _immediate_ effect, so only apply to BACKEND_REQs of the current FUNCTION that have already been declared! 


### define BACKEND_OPTION

```
#define BACKEND_OPTION(
    BACKEND_AND_VERSIONS,
    TAGS
)
LONG_BACKEND_OPTION(MODULE, CAPABILITY, FUNCTION, BACKEND_AND_VERSIONS,TAGS)
```


Define a rule that uses TAGS to determine a set of backend requirements of the current [FUNCTION] that are permitted to be fulfilled by the indicated BACKEND_AND_VERSIONS. If no versions are given, all versions of the stated backend are considered allowed. Declaring this rule makes all backend requirements that match the rule resolvable _only_ by the backend-version pairs passed into [BACKEND_OPTION](/documentation/code/files/module__macros__incore_8hpp/#define-backend-option). Additional options provided by subsequent calls to [BACKEND_OPTION](/documentation/code/files/module__macros__incore_8hpp/#define-backend-option) are added to the options provided by each previous declaration. In the case of multiple contradictory calls to [BACKEND_OPTION](/documentation/code/files/module__macros__incore_8hpp/#define-backend-option), the rule defined by the latest call takes precedence. Note that all rules have _immediate_ effect, so only apply to BACKEND_REQs of the current FUNCTION that have already been declared! 


### define LONG_BACKEND_OPTION

```
#define LONG_BACKEND_OPTION(
    MODULE,
    CAPABILITY,
    FUNCTION,
    BACKEND_AND_VERSIONS,
    TAGS
)
CORE_BACKEND_OPTION(MODULE, CAPABILITY, FUNCTION, BACKEND_AND_VERSIONS,TAGS, NOT_MODEL)
```


### define FORCE_SAME_BACKEND

```
#define FORCE_SAME_BACKEND(
    ...
)
CORE_FORCE_SAME_BACKEND(NOT_MODEL,__VA_ARGS__)
```


Define a rule that certain sets of backend requirements need to be resolved by the same backend. The sets are identified by tags, any number of which can be passed to FORCE_SAME_BACKEND. All backend requirements with a given tag passed into FORCE_SAME_BACKEND will be forced by the dependency resolver to use functions from the same backend. Note that all rules have _immediate_ effect, so only apply to BACKEND_REQs of the current FUNCTION that have already been declared! 


### define START_CONDITIONAL_DEPENDENCY

```
#define START_CONDITIONAL_DEPENDENCY(
    TYPE
)
CORE_START_CONDITIONAL_DEPENDENCY(MODULE, CAPABILITY, \
                                                           FUNCTION, CONDITIONAL_DEPENDENCY, TYPE, NOT_MODEL)
```


Indicate that the current [FUNCTION] may depend on the presence of another module function that can supply capability [CONDITIONAL_DEPENDENCY](/documentation/code/files/examplebit__b__rollcall_8hpp/#define-conditional-dependency), with return type _TYPE_. 


### define ACTIVATE_DEP_BE

```
#define ACTIVATE_DEP_BE(
    BACKEND_REQ,
    BACKEND,
    VERSTRING
)
CORE_ACTIVATE_DEP_BE(BACKEND_REQ, BACKEND, VERSTRING, NOT_MODEL)
```


Indicate that the current [CONDITIONAL_DEPENDENCY](/documentation/code/files/examplebit__b__rollcall_8hpp/#define-conditional-dependency) should be activated if the backend requirement _BACKEND_REQ_ of the current [FUNCTION] is filled by a backend function from _BACKEND_. The versions of _BACKEND_ that this applies to are passed in _VERSTRING_. 


### define ACTIVATE_FOR_MODELS

```
#define ACTIVATE_FOR_MODELS(
    ...
)
ACTIVATE_DEP_MODEL(MODULE, CAPABILITY, FUNCTION, CONDITIONAL_DEPENDENCY, NOT_MODEL, #__VA_ARGS__)
```


Indicate that the current [CONDITIONAL_DEPENDENCY](/documentation/code/files/examplebit__b__rollcall_8hpp/#define-conditional-dependency) should be activated if the model being scanned matches one of the models passed as an argument. 


### define MODEL_CONDITIONAL_DEPENDENCY

```
#define MODEL_CONDITIONAL_DEPENDENCY(
    DEP,
    TYPE,
    ...
)
CORE_START_CONDITIONAL_DEPENDENCY(MODULE, CAPABILITY, FUNCTION, DEP, TYPE, NOT_MODEL) \
                                                          ACTIVATE_DEP_MODEL(MODULE, CAPABILITY, FUNCTION, DEP, NOT_MODEL, #__VA_ARGS__)
```

Quick, one-line declaration of model-conditional dependencies. 

### define CLASSLOAD_NEEDED

```
#define CLASSLOAD_NEEDED(
    BACKEND,
    VERSION
)
CORE_CLASSLOAD_NEEDED(BACKEND, VERSION, NOT_MODEL)
```


Indicate that the current [FUNCTION] requires classes that must be loaded from _BACKEND_, version _VERSION_. 


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Redirection macros for generic observable and 
///  likelihood function macro definitions, for 
///  inclusion from the Core.
///
///
///  Note here that \link FUNCTION() FUNCTION
///  \endlink is the actual module function name,
///  whereas both \link CAPABILITY() CAPABILITY
///  \endlink and all \em DEPs refer to the
///  abstract physical quantities that functions
///  may provide or require.  Thus, the provides()
///  methods expect a quantity input (i.e.
///  corresponding to a \link CAPABILITY()
///  CAPABILITY\endlink), the requires() methods
///  expect a quantity input for the dependency but a
///  function name input (i.e. corresponding to a
///  \link FUNCTION() FUNCTION\endlink) for
///  the actual dependent function, and all other
///  things operate on the basis of the function
///  name, not the quantity that is calculated.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Pat Scott
///          (patscott@physics.mcgill.ca)
///  \date 2012 Nov
///  \date 2013,14 Foreverrrrr
///
///  \author Abram Krislock
///          (abram.krislock@fysik.su.se)
///  \date 2013 Jan, Feb
///
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
///  \date 2019 Jul
///
///  *********************************************

#ifndef __module_macros_incore_hpp__
#define __module_macros_incore_hpp__

#include "gambit/Elements/module_macros_incore_defs.hpp"

/// Models and Modules define different versions of these redirections macros.
/// So we need to undef them in case they have already been defined.
/// (by the time this header is included they should have done their job)
/// We could just overwrite them, but this way avoids compiler warnings.
#undef START_CAPABILITY                  
#undef LONG_START_CAPABILITY  
#undef DECLARE_FUNCTION
#undef LONG_DECLARE_FUNCTION
#undef DEPENDENCY                             
#undef LONG_DEPENDENCY
#undef NEEDS_MANAGER                                
#undef ALLOW_MODELS
#undef ALLOWED_MODEL
#undef ALLOWED_MODEL_DEPENDENCE
#undef ALLOW_MODEL_COMBINATION                      
#undef MODEL_GROUP
#undef BE_GROUP
#undef DECLARE_BACKEND_REQ
#undef LONG_DECLARE_BACKEND_REQ
#undef ACTIVATE_BACKEND_REQ_FOR_MODELS
#undef START_CONDITIONAL_DEPENDENCY                
#undef ACTIVATE_DEP_BE
#undef ACTIVATE_FOR_MODELS                          
#undef MODEL_CONDITIONAL_DEPENDENCY      
#undef BACKEND_OPTION         
#undef LONG_BACKEND_OPTION
#undef FORCE_SAME_BACKEND                           
#undef CLASSLOAD_NEEDED                             

/// \name Rollcall macros (redirection within the Core).
/// These are called from within rollcall headers in each module to
/// register module functions, their capabilities, return types, dependencies,
/// and backend requirements.
/// @{

/// Registers the current \link MODULE() MODULE\endlink.
#define START_MODULE                                      CORE_START_MODULE

/// Registers the current \link CAPABILITY() CAPABILITY\endlink of the current
/// \link MODULE() MODULE\endlink.
#define START_CAPABILITY                                  CORE_START_CAPABILITY(MODULE, CAPABILITY, NOT_MODEL)
/// Long (all argument) version of \link START_CAPABILITY() START_CAPABILITY\endlink.
#define LONG_START_CAPABILITY(MODULE, CAPABILITY)         CORE_START_CAPABILITY(MODULE, CAPABILITY, NOT_MODEL)

/// Registers the current \link FUNCTION() FUNCTION\endlink of the current
/// \link MODULE() MODULE\endlink as a provider
/// of the current \link CAPABILITY() CAPABILITY\endlink, returning a result of
/// type \em TYPE.
#define DECLARE_FUNCTION(TYPE, FLAG)                      CORE_DECLARE_FUNCTION(MODULE, CAPABILITY, FUNCTION, TYPE, FLAG, NOT_MODEL)
/// Long (all argument) version of \link DECLARE_FUNCTION() DECLARE_FUNCTION\endlink.
#define LONG_DECLARE_FUNCTION(MODULE, CAPABILITY, FUNCTION, TYPE, FLAG) CORE_DECLARE_FUNCTION(MODULE, CAPABILITY, FUNCTION, TYPE, FLAG, NOT_MODEL)

/// Indicates that the current \link FUNCTION() FUNCTION\endlink of the current
/// \link MODULE() MODULE\endlink must be managed by another function (in the same
/// module or another) that calls it from within a loop.  May be called with one or
/// two arguments: \em LOOPMAN (capability of the required manager; required) and
/// \em TYPE (type of the required manager; not required).  Will provide a dependency
/// pipe within the function if and only if \em TYPE is present and non-void.
#define NEEDS_MANAGER(...)                                CORE_NEEDS_MANAGER(__VA_ARGS__)

/// Indicate that the current \link FUNCTION() FUNCTION\endlink depends on the
/// presence of another module function that can supply capability \em DEP, with
/// return type \em TYPE.
#define DEPENDENCY(DEP, TYPE)                             CORE_DEPENDENCY(DEP, TYPE, MODULE, FUNCTION, NOT_MODEL)
/// Long (all argument) version of \link DEPENDENCY() DEPENDENCY\endlink.
#define LONG_DEPENDENCY(MODULE, FUNCTION, DEP, TYPE)      CORE_DEPENDENCY(DEP, TYPE, MODULE, FUNCTION, NOT_MODEL)

#define ALLOW_MODELS(...)                                 ALLOW_MODELS_AB(MODULE, FUNCTION, __VA_ARGS__)

/// Indicate that the current \link FUNCTION() FUNCTION\endlink may only be used with
/// specific model \em MODEL, or combinations given via ALLOW_MODEL_COMBINATION.
/// If both this and ALLOW_MODEL_COMBINATION are absent, all models are allowed, but
/// model parameters will not generally be accessible from within the module funtion.
#define ALLOWED_MODEL(MODULE,FUNCTION,MODEL)              CORE_ALLOWED_MODEL(MODULE,FUNCTION,MODEL,NOT_MODEL)

/// Indicate that the current \link FUNCTION() FUNCTION\endlink may be used with a
/// specific model \em MODEL, but only in combination with others given via ALLOW_MODEL_COMBINATION.
#define ALLOWED_MODEL_DEPENDENCE(MODULE,FUNCTION,MODEL)   CORE_ALLOW_MODEL_DEPENDENCE(MODULE,FUNCTION,MODEL,NOT_MODEL)

/// Indicate that the current \link FUNCTION() FUNCTION\endlink may only be used with
/// the specific model combination given, with other combinations passed in the same
/// way, or with individual models speficied via ALLOW_MODEL(S).  If both this and
/// ALLOW_MODEL(s) are absent, all models are allowed but no model parameters will be
/// accessible from within the module funtion.
#define ALLOW_MODEL_COMBINATION(...)                      CORE_ALLOW_MODEL_COMBINATION(MODULE,FUNCTION,NOT_MODEL,(__VA_ARGS__))

/// Define a model GROUP of name GROUPNAME for use with ALLOW_MODEL_COMBINATION.
#define MODEL_GROUP(GROUPNAME,GROUP)                      CORE_MODEL_GROUP(MODULE,FUNCTION,GROUPNAME,GROUP,NOT_MODEL)

/// BACKEND_REQ indicates that the current \link FUNCTION() FUNCTION\endlink requires one
/// backend variable or function to be available from a capability group \em GROUP,
/// and then declares a viable member of that group, with capability \em REQUIREMENT,
/// type \em TYPE and (in the case of functions) arguments \em ARGS.  BACKEND_REQ also
/// allows the user to specify a list of \em TAGS that apply to this specific group member,
/// which can then be used for easily implementing rules for choosing between different
/// members of the same \em GROUP.  Note that \em GROUPs are automatically declared the
/// first time that they are mentioned in a BACKEND_REQ statement.
#define DECLARE_BACKEND_REQ(GROUP, REQUIREMENT, TAGS, TYPE, ARGS, IS_VARIABLE) \
                                                          CORE_BACKEND_REQ(MODULE, CAPABILITY, FUNCTION, GROUP, REQUIREMENT, TAGS, TYPE, ARGS, IS_VARIABLE, NOT_MODEL)
#define LONG_DECLARE_BACKEND_REQ(MODULE, CAPABILITY, FUNCTION, GROUP, REQUIREMENT, TAGS, TYPE, ARGS, IS_VARIABLE) \
                                                          CORE_BACKEND_REQ(MODULE, CAPABILITY, FUNCTION, GROUP, REQUIREMENT, TAGS, TYPE, ARGS, IS_VARIABLE, NOT_MODEL)

/// Declare a backend group, from which one backend requirement must be activated.
#define BE_GROUP(GROUP)                                   CORE_BE_GROUP(GROUP,NOT_MODEL)

/// Define a rule that uses TAGS to determine which backend requirements of the current
/// \link FUNCTION() FUNCTION\endlink are explicitly activated when one or more models
/// from the set MODELS are being scanned.  Declaring this rule makes backend requirements
/// that match one or more TAGS conditional on the model being scanned.  Backend
/// requirements that do not match any such rule are considered unconditional, and are
/// activated regardless of the model(s) being scanned.  Note that all rules have
/// _immediate_ effect, so only apply to BACKEND_REQs of the current FUNCTION that have
/// already been declared!
#define ACTIVATE_BACKEND_REQ_FOR_MODELS(MODELS,TAGS)      CORE_BE_MODEL_RULE(MODELS,TAGS,NOT_MODEL)

/// Define a rule that uses TAGS to determine a set of backend requirements of the current
/// \link FUNCTION() FUNCTION\endlink that are permitted to be fulfilled by the indicated
/// BACKEND_AND_VERSIONS.  If no versions are given, all versions of the stated backend are
/// considered allowed.  Declaring this rule makes all backend requirements that match
/// the rule resolvable _only_ by the backend-version pairs passed into
/// \link BACKEND_OPTION() BACKEND_OPTION\endlink. Additional options provided by subsequent
/// calls to \link BACKEND_OPTION() BACKEND_OPTION\endlink are added to the options provided
/// by each previous declaration. In the case of multiple contradictory calls to
/// \link BACKEND_OPTION() BACKEND_OPTION\endlink, the rule defined by the latest call takes
/// precedence.  Note that all rules have _immediate_ effect, so only apply to BACKEND_REQs
/// of the current FUNCTION that have already been declared!
#define BACKEND_OPTION(BACKEND_AND_VERSIONS,TAGS)         LONG_BACKEND_OPTION(MODULE, CAPABILITY, FUNCTION, BACKEND_AND_VERSIONS,TAGS)
#define LONG_BACKEND_OPTION(MODULE, CAPABILITY, FUNCTION, BACKEND_AND_VERSIONS,TAGS) \
                                                          CORE_BACKEND_OPTION(MODULE, CAPABILITY, FUNCTION, BACKEND_AND_VERSIONS,TAGS, NOT_MODEL)

/// Define a rule that certain sets of backend requirements need to be resolved by the same backend.
/// The sets are identified by tags, any number of which can be passed to FORCE_SAME_BACKEND.
/// All backend requirements with a given tag passed into FORCE_SAME_BACKEND will be forced
/// by the dependency resolver to use functions from the same backend.  Note that all rules have
/// _immediate_ effect, so only apply to BACKEND_REQs of the current FUNCTION that have
/// already been declared!
#define FORCE_SAME_BACKEND(...)                           CORE_FORCE_SAME_BACKEND(NOT_MODEL,__VA_ARGS__)

/// Indicate that the current \link FUNCTION() FUNCTION\endlink may depend on the
/// presence of another module function that can supply capability
/// \link CONDITIONAL_DEPENDENCY() CONDITIONAL_DEPENDENCY\endlink, with return type
/// \em TYPE.
#define START_CONDITIONAL_DEPENDENCY(TYPE)                CORE_START_CONDITIONAL_DEPENDENCY(MODULE, CAPABILITY, \
                                                           FUNCTION, CONDITIONAL_DEPENDENCY, TYPE, NOT_MODEL)

/// Indicate that the current \link CONDITIONAL_DEPENDENCY() CONDITIONAL_DEPENDENCY\endlink
/// should be activated if the backend requirement \em BACKEND_REQ of the current
/// \link FUNCTION() FUNCTION\endlink is filled by a backend function from \em BACKEND.
/// The versions of \em BACKEND that this applies to are passed in \em VERSTRING.
#define ACTIVATE_DEP_BE(BACKEND_REQ, BACKEND, VERSTRING)  CORE_ACTIVATE_DEP_BE(BACKEND_REQ, BACKEND, VERSTRING, NOT_MODEL)

/// Indicate that the current \link CONDITIONAL_DEPENDENCY() CONDITIONAL_DEPENDENCY\endlink
/// should be activated if the model being scanned matches one of the models passed as an argument.
#define ACTIVATE_FOR_MODELS(...)                          ACTIVATE_DEP_MODEL(MODULE, CAPABILITY, FUNCTION, CONDITIONAL_DEPENDENCY, NOT_MODEL, #__VA_ARGS__)

/// Quick, one-line declaration of model-conditional dependencies
#define MODEL_CONDITIONAL_DEPENDENCY(DEP, TYPE, ...)      CORE_START_CONDITIONAL_DEPENDENCY(MODULE, CAPABILITY, FUNCTION, DEP, TYPE, NOT_MODEL) \
                                                          ACTIVATE_DEP_MODEL(MODULE, CAPABILITY, FUNCTION, DEP, NOT_MODEL, #__VA_ARGS__)

/// Indicate that the current \link FUNCTION() FUNCTION\endlink requires classes that
/// must be loaded from \em BACKEND, version \em VERSION.
#define CLASSLOAD_NEEDED(BACKEND, VERSION)               CORE_CLASSLOAD_NEEDED(BACKEND, VERSION, NOT_MODEL)
/// @}

#endif // defined __core_module_macros_incore_hpp__
```


-------------------------------

Updated on 2022-09-08 at 00:43:04 +0000
