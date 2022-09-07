---
title: 'file models/MSSM15atQ_mA.hpp'

description: "[No description available]"

---

# models/MSSM15atQ_mA.hpp



[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/mssm15atq__ma_8hpp/#define-model)**  |
|  | **[PARENT](/documentation/code/files/mssm15atq__ma_8hpp/#define-parent)**  |

## Detailed Description


**Author**: Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 

**Date**: 2017 Aug

MSSM15atQ_mA model definition. This model matches the one explored in arXiv:1405.0622.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define MODEL

```
#define MODEL MSSM15atQ_mA
```


### define PARENT

```
#define PARENT MSSM16atQ_mA
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  MSSM15atQ_mA model definition.
///  This model matches the one explored in
///  arXiv:1405.0622.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Pat Scott
///          (p.scott@imperial.ac.uk)
///  \date 2017 Aug
///
///  *********************************************

#ifndef __MSSM15atQ_mA_hpp__
#define __MSSM15atQ_mA_hpp__

// Parent model must be declared first! Include it here to ensure that this happens.
#include "gambit/Models/models/MSSM16atQ_mA.hpp"

#define MODEL MSSM15atQ_mA
#define PARENT MSSM16atQ_mA
  START_MODEL

  DEFINEPARS(Qin,TanBeta,
             mA,mu,M1,M2,M3)

  DEFINEPARS(mq2_12, mq2_3, mu2_3, md2_3)

  DEFINEPARS(ml2_12, ml2_3, me2_3)

  DEFINEPARS(A0, Au_3)

  INTERPRET_AS_PARENT_FUNCTION(MSSM15atQ_mA_to_MSSM16atQ_mA)

#undef PARENT
#undef MODEL

#endif
```


-------------------------------

Updated on 2022-09-07 at 13:49:53 +0000
