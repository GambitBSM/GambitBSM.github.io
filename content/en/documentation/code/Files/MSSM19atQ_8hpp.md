---
title: "file models/MSSM19atQ.hpp"

description: "[No description available]"

---

# file models/MSSM19atQ.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/mssm19atq_8hpp/)**  |
|  | **[PARENT](/documentation/code/files/mssm19atq_8hpp/)**  |

## Detailed Description


**Author**: Pat Scott 

 ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 

**Date**: 2015 Sep

MSSM19atQ ('pMSSM') model definition.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define MODEL

```
#define MODEL MSSM19atQ
```


### define PARENT

```
#define PARENT MSSM24atQ
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  MSSM19atQ ('pMSSM') model definition. 
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

#ifndef __MSSM19atQ_hpp__
#define __MSSM19atQ_hpp__

// Parent and friend models must be declared first! Include them here to ensure that this happens.
#include "gambit/Models/models/MSSM24atQ.hpp"
#include "gambit/Models/models/MSSM20atQ.hpp"

#define MODEL MSSM19atQ
#define PARENT MSSM24atQ
  START_MODEL

  DEFINEPARS(Qin,TanBeta,SignMu,
             mHu2,mHd2,M1,M2,M3)

  DEFINEPARS(mq2_12, mq2_3)
 
  DEFINEPARS(ml2_12, ml2_3)

  DEFINEPARS(md2_12, md2_3)

  DEFINEPARS(mu2_12, mu2_3)

  DEFINEPARS(me2_12, me2_3)

  DEFINEPARS(Ae_3)
  
  DEFINEPARS(Ad_3)

  DEFINEPARS(Au_3)

  INTERPRET_AS_PARENT_FUNCTION(MSSM19atQ_to_MSSM24atQ)
  INTERPRET_AS_X_FUNCTION(MSSM20atQ, MSSM19atQ_to_MSSM20atQ)

#undef PARENT
#undef MODEL

#endif
```


-------------------------------

Updated on 2022-09-08 at 01:05:20 +0000
