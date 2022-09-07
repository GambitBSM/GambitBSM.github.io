---
title: "file models/MSSM10catQ_mA.hpp"

description: "[No description available]"

---

# file models/MSSM10catQ_mA.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/mssm10catq__ma_8hpp/#define-model)**  |
|  | **[PARENT](/documentation/code/files/mssm10catq__ma_8hpp/#define-parent)**  |

## Detailed Description


**Author**: Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 

**Date**: 2017 Aug

MSSM10catQ_mA model definition. This model matches the one explored in arXiv:1504.03260 and referred to as 'pMSSM10'.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define MODEL

```
#define MODEL MSSM10catQ_mA
```


### define PARENT

```
#define PARENT MSSM15atQ_mA
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  MSSM10catQ_mA model definition.
///  This model matches the one explored in
///  arXiv:1504.03260 and referred to as 'pMSSM10'.
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

#ifndef __MSSM10catQ_mA_hpp__
#define __MSSM10catQ_mA_hpp__

// Parent model must be declared first! Include it here to ensure that this happens.
#include "gambit/Models/models/MSSM15atQ_mA.hpp"

#define MODEL MSSM10catQ_mA
#define PARENT MSSM15atQ_mA
  START_MODEL

  DEFINEPARS(Qin,TanBeta,
             mA,mu,M1,M2,M3)

  DEFINEPARS(mq2_12, mq2_3)

  DEFINEPARS(ml2)

  DEFINEPARS(A0)

  INTERPRET_AS_PARENT_FUNCTION(MSSM10catQ_mA_to_MSSM15atQ_mA)

#undef PARENT
#undef MODEL

#endif
```


-------------------------------

Updated on 2022-09-07 at 23:22:09 +0000
