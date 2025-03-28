---
title: "file models/StandardModel_Higgs.hpp"

description: "[No description available]"

---

# file models/StandardModel_Higgs.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/standardmodel__higgs_8hpp/#define-model)**  |
|  | **[PARENT](/documentation/code/files/standardmodel__higgs_8hpp/#define-parent)**  |

## Detailed Description


**Author**: 

  * Ben Farmer ([benjamin.farmer@fysik.su.se](mailto:benjamin.farmer@fysik.su.se)) 
  * Jonathan Cornell ([jmcornell@gmail.com](mailto:jmcornell@gmail.com)) 


**Date**: 

  * 2015 May
  * 2015 September


Standard Model Higgs sector parameters.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define MODEL

```
#define MODEL StandardModel_Higgs
```


### define PARENT

```
#define PARENT StandardModel_Higgs_running
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Standard Model Higgs sector parameters.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Ben Farmer
///          (benjamin.farmer@fysik.su.se)
///    \date 2015 May
///
///  \author Jonathan Cornell
///          (jmcornell@gmail.com)
///    \date 2015 September
///
///  *********************************************


#include "gambit/Models/models/StandardModel_Higgs_running.hpp"

#ifndef __StandardModel_Higgs_hpp__
#define __StandardModel_Higgs_hpp__


#define MODEL StandardModel_Higgs
#define PARENT StandardModel_Higgs_running
  START_MODEL
  INTERPRET_AS_PARENT_FUNCTION(StandardModel_Higgs_to_StandardModel_Higgs_running)

  DEFINEPARS(mH)

#undef PARENT
#undef MODEL

#endif /* __StandardModel_Higgs_hpp__ */
```


-------------------------------

Updated on 2025-02-12 at 16:10:34 +0000
