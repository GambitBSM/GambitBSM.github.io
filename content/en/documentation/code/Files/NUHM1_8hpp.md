---
title: "file models/NUHM1.hpp"

description: "[No description available]"

---

# file models/NUHM1.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/nuhm1_8hpp/#define-model)**  |
|  | **[PARENT](/documentation/code/files/nuhm1_8hpp/#define-parent)**  |

## Detailed Description


**Author**: Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 

**Date**: 2015 Sep

NUHM1 model definition.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define MODEL

```
#define MODEL NUHM1
```


### define PARENT

```
#define PARENT NUHM2
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  NUHM1 model definition.
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

#ifndef __NUHM1_hpp__
#define __NUHM1_hpp__

// Must include models that are targets of translation functions
#include "gambit/Models/models/NUHM2.hpp"

#define MODEL NUHM1
#define PARENT NUHM2
  START_MODEL
  DEFINEPARS(M0,M12,mH,A0,TanBeta,SignMu)
  INTERPRET_AS_PARENT_FUNCTION(NUHM1_to_NUHM2)
  // Translation functions defined in NUHM1.cpp
#undef PARENT
#undef MODEL


#endif
```


-------------------------------

Updated on 2022-09-08 at 02:27:29 +0000
