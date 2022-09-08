---
title: "file models/mSUGRA.hpp"

description: "[No description available]"

---

# file models/mSUGRA.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/msugra_8hpp/#define-model)**  |
|  | **[PARENT](/documentation/code/files/msugra_8hpp/#define-parent)**  |

## Detailed Description


**Author**: Pat Scott 

 ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 

**Date**: 2015 Sep

mSUGRA model declaration. Basically just an alias for the CMSSM. See mSUGRA_nonstandard for a more constrained definition that some people prefer.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define MODEL

```
#define MODEL mSUGRA
```


### define PARENT

```
#define PARENT CMSSM
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  mSUGRA model declaration.  Basically just an
///  alias for the CMSSM.  See mSUGRA_nonstandard
///  for a more constrained definition that some
///  people prefer. 
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


#ifndef __mSUGRA_hpp__
#define __mSUGRA_hpp__

// Must include models which are targets of translation functions
#include "gambit/Models/models/CMSSM.hpp" 

#define MODEL mSUGRA
#define PARENT CMSSM
  START_MODEL
  DEFINEPARS(M0,M12,A0,TanBeta,SignMu)
  INTERPRET_AS_PARENT_FUNCTION(mSUGRA_to_CMSSM)
  // Translation functions defined in mSUGRA.cpp
#undef PARENT
#undef MODEL


#endif
```


-------------------------------

Updated on 2022-09-08 at 00:43:04 +0000
