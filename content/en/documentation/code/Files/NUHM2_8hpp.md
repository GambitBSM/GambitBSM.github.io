---
title: "file models/NUHM2.hpp"

description: "[No description available]"

---

# file models/NUHM2.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/nuhm2_8hpp/#define-model)**  |
|  | **[PARENT](/documentation/code/files/nuhm2_8hpp/#define-parent)**  |

## Detailed Description


**Author**: Pat Scott 

 ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 

**Date**: 2015 Sep

NUHM2 model declaration.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define MODEL

```
#define MODEL NUHM2
```


### define PARENT

```
#define PARENT MSSM63atMGUT
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  NUHM2 model declaration. 
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///   
///  \author Pat Scott  
///          (p.scott@imperial.ac.uk)
///  \date 2015 Sep
///
///  *********************************************

#ifndef __NUHM2_hpp__
#define __NUHM2_hpp__

// Must include models which are targets of translation functions
#include "gambit/Models/models/MSSM30atMGUT.hpp" 

#define MODEL NUHM2
#define PARENT MSSM63atMGUT
  START_MODEL
  DEFINEPARS(M0,M12,mHu,mHd,A0,TanBeta,SignMu)
  INTERPRET_AS_PARENT_FUNCTION(NUHM2_to_MSSM63atMGUT)
  // Translation functions defined in NUHM2.cpp
#undef PARENT
#undef MODEL


#endif
```


-------------------------------

Updated on 2022-09-08 at 03:17:36 +0000
