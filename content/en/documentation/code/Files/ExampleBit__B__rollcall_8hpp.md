---
title: "file ExampleBit_B/ExampleBit_B_rollcall.hpp"

description: "[No description available]"

---

# file ExampleBit_B/ExampleBit_B_rollcall.hpp

[No description available] [More...](#detailed-description)

## Functions

|                | Name           |
| -------------- | -------------- |
| | **[START_FUNCTION](/documentation/code/files/examplebit__b__rollcall_8hpp/#function-examplebit-b-rollcall-hpp-start-function)**(double ) |
| | **[START_FUNCTION](/documentation/code/files/examplebit__b__rollcall_8hpp/#function-examplebit-b-rollcall-hpp-start-function)**(int ) |
| double | **[DEPENDENCY](/documentation/code/files/examplebit__b__rollcall_8hpp/#function-examplebit-b-rollcall-hpp-dependency)**(function_pointer , fptr ) |
| double int | **[BACKEND_REQ](/documentation/code/files/examplebit__b__rollcall_8hpp/#function-examplebit-b-rollcall-hpp-backend-req)**(refex , (common_be) , double , (double &) ) |
| double int double double | **[BACKEND_REQ](/documentation/code/files/examplebit__b__rollcall_8hpp/#function-examplebit-b-rollcall-hpp-backend-req)**(varex , (common_be) , double , (int, etc) ) |
| double int double double etc | **[BACKEND_REQ](/documentation/code/files/examplebit__b__rollcall_8hpp/#function-examplebit-b-rollcall-hpp-backend-req)**(runMe , () , void , (double(*)(int &), int &) ) |
| double int double double etc | **[ACTIVATE_BACKEND_REQ_FOR_MODELS](/documentation/code/files/examplebit__b__rollcall_8hpp/#function-examplebit-b-rollcall-hpp-activate-backend-req-for-models)**((CMSSM, demo_B, nonexistent_model) , (model_dependent_reqs) ) |
| double int double double etc lib123 | **[BACKEND_OPTION](/documentation/code/files/examplebit__b__rollcall_8hpp/#function-examplebit-b-rollcall-hpp-backend-option)**((LibFirst, 1.1) , (not_libfirst10) ) |

## Attributes

|                | Name           |
| -------------- | -------------- |
| double | **[lib123](/documentation/code/files/examplebit__b__rollcall_8hpp/#variable-examplebit-b-rollcall-hpp-lib123)**  |
| double | **[double](/documentation/code/files/examplebit__b__rollcall_8hpp/#variable-examplebit-b-rollcall-hpp-double)**  |
| double int | **[common_be](/documentation/code/files/examplebit__b__rollcall_8hpp/#variable-examplebit-b-rollcall-hpp-common-be)**  |
| double int | **[void](/documentation/code/files/examplebit__b__rollcall_8hpp/#variable-examplebit-b-rollcall-hpp-void)**  |
| double int double double | **[int](/documentation/code/files/examplebit__b__rollcall_8hpp/#variable-examplebit-b-rollcall-hpp-int)**  |
| double int double double etc | **[not_libfirst10](/documentation/code/files/examplebit__b__rollcall_8hpp/#variable-examplebit-b-rollcall-hpp-not-libfirst10)**  |

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODULE](/documentation/code/files/examplebit__b__rollcall_8hpp/#define-examplebit-b-rollcall-hpp-module)**  |
|  | **[CAPABILITY](/documentation/code/files/examplebit__b__rollcall_8hpp/#define-examplebit-b-rollcall-hpp-capability)**  |
|  | **[FUNCTION](/documentation/code/files/examplebit__b__rollcall_8hpp/#define-examplebit-b-rollcall-hpp-function)**  |
|  | **[FUNCTION](/documentation/code/files/examplebit__b__rollcall_8hpp/#define-examplebit-b-rollcall-hpp-function)**  |
|  | **[CAPABILITY](/documentation/code/files/examplebit__b__rollcall_8hpp/#define-examplebit-b-rollcall-hpp-capability)**  |
|  | **[FUNCTION](/documentation/code/files/examplebit__b__rollcall_8hpp/#define-examplebit-b-rollcall-hpp-function)**  |
|  | **[CAPABILITY](/documentation/code/files/examplebit__b__rollcall_8hpp/#define-examplebit-b-rollcall-hpp-capability)**  |
|  | **[FUNCTION](/documentation/code/files/examplebit__b__rollcall_8hpp/#define-examplebit-b-rollcall-hpp-function)**  |
|  | **[CONDITIONAL_DEPENDENCY](/documentation/code/files/examplebit__b__rollcall_8hpp/#define-examplebit-b-rollcall-hpp-conditional-dependency)**  |
|  | **[CAPABILITY](/documentation/code/files/examplebit__b__rollcall_8hpp/#define-examplebit-b-rollcall-hpp-capability)**  |
|  | **[FUNCTION](/documentation/code/files/examplebit__b__rollcall_8hpp/#define-examplebit-b-rollcall-hpp-function)**  |
|  | **[CAPABILITY](/documentation/code/files/examplebit__b__rollcall_8hpp/#define-examplebit-b-rollcall-hpp-capability)**  |
|  | **[FUNCTION](/documentation/code/files/examplebit__b__rollcall_8hpp/#define-examplebit-b-rollcall-hpp-function)**  |
|  | **[CAPABILITY](/documentation/code/files/examplebit__b__rollcall_8hpp/#define-examplebit-b-rollcall-hpp-capability)**  |
|  | **[FUNCTION](/documentation/code/files/examplebit__b__rollcall_8hpp/#define-examplebit-b-rollcall-hpp-function)**  |

## Detailed Description


**Author**: 

  * Pat Scott 
  * Anders Kvellestad ([anders.kvellestad@fys.uio.no](mailto:anders.kvellestad@fys.uio.no)) 


**Date**: 

  * 2012 Nov 
  * 2013 Jan, Feb, April, May
  * 2013 Nov 

------------------


Rollcall header for module ExampleBit_B.

Compile-time registration of available observables and likelihoods, as well as their dependencies.

Add to this if you want to add an observable or likelihood to this module.

Don't put typedefs or other type definitions in this file; see [Elements/include/gambit/Elements/types_rollcall.hpp](/documentation/code/files/types__rollcall_8hpp/#file-elements-types-rollcall-hpp) for further instructions on how to add new types.



------------------

Authors (add name and date if you modify):


## Functions Documentation

### function START_FUNCTION

```
START_FUNCTION(
    double 
)
```


### function START_FUNCTION

```
START_FUNCTION(
    int 
)
```


### function DEPENDENCY

```
double DEPENDENCY(
    function_pointer ,
    fptr 
)
```


### function BACKEND_REQ

```
double int BACKEND_REQ(
    refex ,
    (common_be) ,
    double ,
    (double &) 
)
```


### function BACKEND_REQ

```
double int double double BACKEND_REQ(
    varex ,
    (common_be) ,
    double ,
    (int, etc) 
)
```


### function BACKEND_REQ

```
double int double double etc BACKEND_REQ(
    runMe ,
    () ,
    void ,
    (double(*)(int &), int &) 
)
```


### function ACTIVATE_BACKEND_REQ_FOR_MODELS

```
double int double double etc ACTIVATE_BACKEND_REQ_FOR_MODELS(
    (CMSSM, demo_B, nonexistent_model) ,
    (model_dependent_reqs) 
)
```


### function BACKEND_OPTION

```
double int double double etc lib123 BACKEND_OPTION(
    (LibFirst, 1.1) ,
    (not_libfirst10) 
)
```



## Attributes Documentation

### variable lib123

```
double lib123;
```


### variable double

```
double double;
```


### variable common_be

```
double int common_be;
```


### variable void

```
double int void;
```


### variable int

```
double int double double int;
```


### variable not_libfirst10

```
double int double double etc not_libfirst10;
```



## Macros Documentation

### define MODULE

```
#define MODULE ExampleBit_B
```


Specifies that this is the MODULE named ExampleBit_B. 


### define CAPABILITY

```
#define CAPABILITY xsection
```


Specifies that ExampleBit_B (this MODULE) is capable of providing the service CAPABILITY. Usually a CAPABILITY means that the MODULE can compute some physical or statistical quantity referred to by CAPABILITY. 


### define FUNCTION

```
#define FUNCTION sigma_example
```


Specifies that ExampleBit_B (this MODULE) contains a function named FUNCTION that can execute the commands required to provided the current CAPABILITY. 


### define FUNCTION

```
#define FUNCTION sigma_example
```


Specifies that ExampleBit_B (this MODULE) contains a function named FUNCTION that can execute the commands required to provided the current CAPABILITY. 


### define CAPABILITY

```
#define CAPABILITY xsection
```


Specifies that ExampleBit_B (this MODULE) is capable of providing the service CAPABILITY. Usually a CAPABILITY means that the MODULE can compute some physical or statistical quantity referred to by CAPABILITY. 


### define FUNCTION

```
#define FUNCTION sigma_example
```


Specifies that ExampleBit_B (this MODULE) contains a function named FUNCTION that can execute the commands required to provided the current CAPABILITY. 


### define CAPABILITY

```
#define CAPABILITY xsection
```


Specifies that ExampleBit_B (this MODULE) is capable of providing the service CAPABILITY. Usually a CAPABILITY means that the MODULE can compute some physical or statistical quantity referred to by CAPABILITY. 


### define FUNCTION

```
#define FUNCTION sigma_example
```


Specifies that ExampleBit_B (this MODULE) contains a function named FUNCTION that can execute the commands required to provided the current CAPABILITY. 


### define CONDITIONAL_DEPENDENCY

```
#define CONDITIONAL_DEPENDENCY particle_id
```


Specifies that the current FUNCTION in ExampleBit_B (this MODULE) has a CONDITIONAL_DEPENDENCY that is only active under certain conditions. These conditions may include:

* a specific backend is in use in order to fill a certain BACKEND_REQ
* a certain model is under analysis 


### define CAPABILITY

```
#define CAPABILITY xsection
```


Specifies that ExampleBit_B (this MODULE) is capable of providing the service CAPABILITY. Usually a CAPABILITY means that the MODULE can compute some physical or statistical quantity referred to by CAPABILITY. 


### define FUNCTION

```
#define FUNCTION sigma_example
```


Specifies that ExampleBit_B (this MODULE) contains a function named FUNCTION that can execute the commands required to provided the current CAPABILITY. 


### define CAPABILITY

```
#define CAPABILITY xsection
```


Specifies that ExampleBit_B (this MODULE) is capable of providing the service CAPABILITY. Usually a CAPABILITY means that the MODULE can compute some physical or statistical quantity referred to by CAPABILITY. 


### define FUNCTION

```
#define FUNCTION sigma_example
```


Specifies that ExampleBit_B (this MODULE) contains a function named FUNCTION that can execute the commands required to provided the current CAPABILITY. 


### define CAPABILITY

```
#define CAPABILITY xsection
```


Specifies that ExampleBit_B (this MODULE) is capable of providing the service CAPABILITY. Usually a CAPABILITY means that the MODULE can compute some physical or statistical quantity referred to by CAPABILITY. 


### define FUNCTION

```
#define FUNCTION sigma_example
```


Specifies that ExampleBit_B (this MODULE) contains a function named FUNCTION that can execute the commands required to provided the current CAPABILITY. 


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Rollcall header for module ExampleBit_B.
///
///  Compile-time registration of available
///  observables and likelihoods, as well as their
///  dependencies.
///
///  Add to this if you want to add an observable
///  or likelihood to this module.
///
///  Don't put typedefs or other type definitions
///  in this file; see
///  Elements/include/gambit/Elements/types_rollcall.hpp
///  for further instructions on how to add new
///  types.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Pat Scott
///  \date 2012 Nov
///  \date 2013 Jan, Feb, April, May
///
///  \author Anders Kvellestad
///          (anders.kvellestad@fys.uio.no)
///  \date 2013 Nov
///  *********************************************
///
/// \def MODULE
/// Specifies that this is the MODULE named ExampleBit_B.
///
/// \def CAPABILITY
/// Specifies that ExampleBit_B (this MODULE) is
/// capable of providing the service CAPABILITY.
/// Usually a CAPABILITY means that the MODULE can
/// compute some physical or statistical quantity
/// referred to by CAPABILITY.
///
/// \def FUNCTION
/// Specifies that ExampleBit_B (this MODULE) contains
/// a function named FUNCTION that can execute the
/// commands required to provided the current CAPABILITY.
///
/// \def BACKEND_REQ
/// Specifies that the current FUNCTION in
/// ExampleBit_B (this MODULE) requires BACKEND_REQ from
/// a backend code.  The requirement BACKEND_REQ corresponds
/// to a capability that a valid backend function
/// is expected to report in its corresponding
/// registration header file.
///
/// \def CONDITIONAL_DEPENDENCY
/// Specifies that the current FUNCTION in
/// ExampleBit_B (this MODULE) has a CONDITIONAL_DEPENDENCY
/// that is only active under certain conditions.
/// These conditions may include:
///  - a specific backend is in use in order to fill
///    a certain BACKEND_REQ
///  - a certain model is under analysis


#ifndef __ExampleBit_B_rollcall_hpp__
#define __ExampleBit_B_rollcall_hpp__

#define MODULE ExampleBit_B
START_MODULE

  #define CAPABILITY xsection               // Observable: cross-section for some hypothetical process
  START_CAPABILITY

    #define FUNCTION sigma_example          // Name of specific function providing the observable
    START_FUNCTION(double)                  // Function calculates a double precision variable
    ALLOW_MODELS(NormalDist)
    #undef FUNCTION

    #define FUNCTION sigma_example_req_pars // As sigma_example, however it obtains model parameters
    START_FUNCTION(double)                  // as an "ordinary" dependency, rather than using ALLOW_MODELS
    DEPENDENCY(NormalDist_parameters, ModelParameters)
    #undef FUNCTION

  #undef CAPABILITY


  #define CAPABILITY charge                 // Observable: charge of some particle
  START_CAPABILITY

    #define FUNCTION q_example              // Name of specific function providing the observable
    START_FUNCTION(int)                     // Function calculates an integer variable
    ALLOW_MODEL(NormalDist)
    ALLOW_MODELS(demo_B, nonexistent_model) // Function is only allowed to be used with models NormalDist, demo_B, nonexistent_model and their descendents
    #undef FUNCTION

  #undef CAPABILITY


  #define CAPABILITY nevents_postcuts       // Observable: predicted number of events for process after cuts
  START_CAPABILITY
  //LATEX_LABEL($n_{\rm events, cut}$)      // Specify the LaTeX label of this quantity.  Not implemented yet...

    #define FUNCTION predicted_events       // Name of specific function providing the observable
    START_FUNCTION(int)                     // Function calculates an integer variable
    DEPENDENCY(nevents, double)             // Dependency: post-cut events needs pre-cut events
    DEPENDENCY(function_pointer, fptr)      // Dependency: some function pointer

    BACKEND_REQ(awesomeness, (lib123), double, (int))
    BACKEND_REQ(refex, (common_be), double, (double&))
    BACKEND_REQ(refex2, (common_be), void, (double&, double))
    BACKEND_REQ(varex, (common_be), double, (int, etc))
    BACKEND_REQ(varex2, (common_be), double, (int, etc))
    BACKEND_REQ(runMe, (), void, (double (*)(int&), int&))
    BACKEND_REQ(SomeInt, (model_dependent_reqs, not_libfirst10), python_variable<int>)
    BACKEND_REQ(someFunction, (not_libfirst10), void, ())

    ACTIVATE_BACKEND_REQ_FOR_MODELS( (CMSSM, demo_B, nonexistent_model), (model_dependent_reqs) )
    BACKEND_OPTION( (LibFirst), (lib123) )
    BACKEND_OPTION( (LibFirst, 1.1), (not_libfirst10) )
    BACKEND_OPTION( (LibSecond), (not_libfirst10, lib123) )
    BACKEND_OPTION( (LibThird), (not_libfirst10, lib123) )
    FORCE_SAME_BACKEND(common_be)

    #define CONDITIONAL_DEPENDENCY particle_id             // A dependency that only counts under certain conditions (must come after all BACKEND_REQs)
    START_CONDITIONAL_DEPENDENCY(std::string)              // Type of the dependency; one type permitted per CONDITIONAL_DEPENDENCY.
    ACTIVATE_FOR_BACKEND(awesomeness, LibFirst, 1.1, 1.2)  // Dependency counts if awesomeness comes from LibFirst v1.1 or 1.2
    ACTIVATE_FOR_BACKEND(awesomeness, LibThird)            // Dependency counts when any version of LibThird is used for awesomeness
    ACTIVATE_FOR_MODEL(CMSSM)                              // Dependency counts when scanning CMSSM or one of its sub-models
    #undef CONDITIONAL_DEPENDENCY

    #undef FUNCTION

  #undef CAPABILITY


  #define CAPABILITY nevents
  START_CAPABILITY

    #define FUNCTION event_count            // Observable: observed number of events
    START_FUNCTION(int)                     // Function calculates an integer variable
    #undef FUNCTION

  #undef CAPABILITY


  #define CAPABILITY particle_id
  START_CAPABILITY

    #define FUNCTION particle_identity     // Observable: name of a particle
    START_FUNCTION(std::string)
    #undef FUNCTION

  #undef CAPABILITY


  #define CAPABILITY ptr_arr_tests
  START_CAPABILITY
    #define FUNCTION ptrArrTester
    START_FUNCTION(int)
    DEPENDENCY(test_vector, std::vector<double>)
    BACKEND_REQ(test_vector, (), std::vector<double>)
    BACKEND_REQ(SomeArray, (), dblarr)
    #undef FUNCTION
  #undef CAPABILITY


#undef MODULE


// QUICK_FUNCTION examples
// Arguments: MODULE, CAPABILITY, NEW_CAPABILITY_FLAG, FUNCTION, TYPE, (n x ALLOWED_MODEL), m x (DEPENDENCY, DEPENDENCY_TYPE)
//            The last two arguments are optional, and n and m can be anything from 0 to 10.
QUICK_FUNCTION(ExampleBit_B, test_vector, NEW_CAPABILITY, exampleVec, std::vector<double>)                    // Observable: test vector of doubles
QUICK_FUNCTION(ExampleBit_B, Example_lnL_B, NEW_CAPABILITY, example_lnL, double, (), (nevents_postcuts, int)) // Likelihood of type double that depends on postcuts

// Equivalent to:
//   #define CAPABILITY test_vector
//   START_CAPABILITY
//     #define FUNCTION exampleVec
//     START_FUNCTION(std::vector<double>)
//     #undef FUNCTION
//   #undef CAPABILITY
//   #define CAPABILITY lnL_ExampleBitB
//   START_CAPABILITY
//     #define FUNCTION lnL_ExampleBitB
//     START_FUNCTION(double)
//     DEPENDENCY(nevents_postcuts, int)
//   #undef FUNCTION
//   #undef CAPABILITY


#endif // defined(__ExampleBit_B_rollcall_hpp__)
```


-------------------------------

Updated on 2022-09-08 at 02:00:51 +0000
