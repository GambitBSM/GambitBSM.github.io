---
title: "file models/MSSM9atQ.hpp"

description: "[No description available]"

---

# file models/MSSM9atQ.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/mssm9atq_8hpp/#define-model)**  |
|  | **[PARENT](/documentation/code/files/mssm9atq_8hpp/#define-parent)**  |

## Detailed Description


**Author**: Pat Scott 

 ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 

**Date**: 2015 Sep

MSSM9atQ model definition.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define MODEL

```
#define MODEL MSSM9atQ
```


### define PARENT

```
#define PARENT MSSM10atQ
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  MSSM9atQ model definition. 
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

#ifndef __MSSM9atQ_hpp__
#define __MSSM9atQ_hpp__

// Parent and friend models must be declared first! Include them here to ensure that this happens.
#include "gambit/Models/models/MSSM10atQ.hpp" 
#include "gambit/Models/models/MSSM10batQ.hpp" 

#define MODEL MSSM9atQ
#define PARENT MSSM10atQ
  START_MODEL

  DEFINEPARS(Qin,TanBeta,SignMu,
             mHu2,mHd2,M1,M2,M3)

  DEFINEPARS(mf2)
 
  DEFINEPARS(Ad_3)

  DEFINEPARS(Au_3)

  INTERPRET_AS_PARENT_FUNCTION(MSSM9atQ_to_MSSM10atQ)
  INTERPRET_AS_X_FUNCTION(MSSM10batQ, MSSM9atQ_to_MSSM10batQ)

#undef PARENT
#undef MODEL

#endif
```


-------------------------------

Updated on 2022-09-08 at 03:17:36 +0000
