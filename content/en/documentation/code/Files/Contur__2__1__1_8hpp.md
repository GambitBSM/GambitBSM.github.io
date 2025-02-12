---
title: "file frontends/Contur_2_1_1.hpp"

description: "[No description available]"

---

# file frontends/Contur_2_1_1.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[BACKENDNAME](/documentation/code/files/contur__2__1__1_8hpp/#define-backendname)**  |
|  | **[BACKENDLANG](/documentation/code/files/contur__2__1__1_8hpp/#define-backendlang)**  |
|  | **[VERSION](/documentation/code/files/contur__2__1__1_8hpp/#define-version)**  |
|  | **[SAFE_VERSION](/documentation/code/files/contur__2__1__1_8hpp/#define-safe-version)**  |
|  | **[REFERENCE](/documentation/code/files/contur__2__1__1_8hpp/#define-reference)**  |

## Detailed Description


**Author**: 

  * Tomas Gonzalo ([tomas.gonzalo@monash.edu](mailto:tomas.gonzalo@monash.edu)) 
  * Tomasz Procter ([t.procter.1@research.gla.ac.uk](mailto:t.procter.1@research.gla.ac.uk)) 


**Date**: 

  * 2019 Oct, 2020 Mar 
  * 2021 Mar
  * 2021 June


Fronted header for the Contur backend

Compile-time registration of available functions and variables from this backend.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define BACKENDNAME

```
#define BACKENDNAME Contur
```


### define BACKENDLANG

```
#define BACKENDLANG Python3
```


### define VERSION

```
#define VERSION 2.1.1
```


### define SAFE_VERSION

```
#define SAFE_VERSION 2_1_1
```


### define REFERENCE

```
#define REFERENCE Butterworth:2016sqg
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Fronted header for the Contur backend
///
///  Compile-time registration of available
///  functions and variables from this backend.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Tomas Gonzalo
///          (tomas.gonzalo@monash.edu)
///  \date 2019 Oct, 2020 Mar
///  \date 2021 Mar
///
/// \author Tomasz Procter
///          (t.procter.1@research.gla.ac.uk)
/// \date 2021 June
///
///  *********************************************

#define BACKENDNAME Contur
#define BACKENDLANG Python3
#define VERSION 2.1.1
#define SAFE_VERSION 2_1_1
#define REFERENCE Butterworth:2016sqg

LOAD_LIBRARY

#ifdef HAVE_PYBIND11

  BE_CONV_FUNCTION(Contur_LogLike_from_stream, Contur_output, (std::shared_ptr<std::ostringstream>, std::vector<std::string>&), "Contur_Measurements")
  BE_CONV_FUNCTION(Contur_LogLike_from_file, Contur_output, (str &, std::vector<std::string>&), "Contur_Measurements")
  BE_CONV_FUNCTION(Contur_get_analyses_from_beam, void, (std::vector<std::string>&, std::string&), "Contur_GetAnalyses")

#endif

// Undefine macros to avoid conflict with other backends
#include "gambit/Backends/backend_undefs.hpp"
```


-------------------------------

Updated on 2025-02-12 at 16:10:36 +0000
