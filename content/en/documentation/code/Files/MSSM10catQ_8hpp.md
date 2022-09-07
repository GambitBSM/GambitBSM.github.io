---
title: "file models/MSSM10catQ.hpp"

description: "[No description available]"

---

# file models/MSSM10catQ.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/mssm10catq_8hpp/#define-model)**  |
|  | **[PARENT](/documentation/code/files/mssm10catq_8hpp/#define-parent)**  |

## Detailed Description


**Author**: Pat Scott 

 ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 

**Date**: 2015 Sep

MSSM10catQ model definition. This model matches the one explored in arXiv:1504.03260 and referred to as 'pMSSM10'.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define MODEL

```
#define MODEL MSSM10catQ
```


### define PARENT

```
#define PARENT MSSM15atQ
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  MSSM10catQ model definition. 
///  This model matches the one explored in 
///  arXiv:1504.03260 and referred to as 'pMSSM10'.
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

#ifndef __MSSM10catQ_hpp__
#define __MSSM10catQ_hpp__

// Parent model must be declared first! Include it here to ensure that this happens.
#include "gambit/Models/models/MSSM15atQ.hpp" 

#define MODEL MSSM10catQ
#define PARENT MSSM15atQ
  START_MODEL

  DEFINEPARS(Qin,TanBeta,SignMu,
             mHu2,mHd2,M1,M2,M3)

  DEFINEPARS(mq2_12, mq2_3)
 
  DEFINEPARS(ml2)

  DEFINEPARS(A0)

  INTERPRET_AS_PARENT_FUNCTION(MSSM10catQ_to_MSSM15atQ)

#undef PARENT
#undef MODEL

#endif
```


-------------------------------

Updated on 2022-09-07 at 23:22:09 +0000
