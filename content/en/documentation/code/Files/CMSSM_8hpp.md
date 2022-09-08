---
title: "file models/CMSSM.hpp"

description: "[No description available]"

---

# file models/CMSSM.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/cmssm_8hpp/#define-model)**  |
|  | **[PARENT](/documentation/code/files/cmssm_8hpp/#define-parent)**  |

## Detailed Description


**Author**: 

  * Ben Farmer 
  * Pat Scott 

 ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 


**Date**: 

  * 2015 Jan
  * 2015 Sep


CMSSM model declaration.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define MODEL

```
#define MODEL CMSSM
```


### define PARENT

```
#define PARENT NUHM1
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  CMSSM model declaration. 
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///   
///  \author Ben Farmer 
///  \date 2015 Jan
///   
///  \author Pat Scott  
///          (p.scott@imperial.ac.uk)
///  \date 2015 Sep
///
///  *********************************************


#ifndef __CMSSM_hpp__
#define __CMSSM_hpp__

// Must include models which are targets of translation functions
#include "gambit/Models/models/NUHM1.hpp" 

#define MODEL CMSSM
#define PARENT NUHM1
  START_MODEL
  DEFINEPARS(M0,M12,A0,TanBeta,SignMu)
  INTERPRET_AS_PARENT_FUNCTION(CMSSM_to_NUHM1)
  // Translation functions defined in CMSSM.cpp
#undef PARENT
#undef MODEL


#endif
```


-------------------------------

Updated on 2022-09-08 at 02:27:29 +0000
