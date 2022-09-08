---
title: "file models/MSSM11atQ_mA.hpp"

description: "[No description available]"

---

# file models/MSSM11atQ_mA.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/mssm11atq__ma_8hpp/#define-mssm11atq-ma-hpp-model)**  |
|  | **[PARENT](/documentation/code/files/mssm11atq__ma_8hpp/#define-mssm11atq-ma-hpp-parent)**  |

## Detailed Description


**Author**: Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 

**Date**: 2017 Aug

MSSM11atQ_mA model definition.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define MODEL

```
#define MODEL MSSM11atQ_mA
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
///  MSSM11atQ_mA model definition.
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

#ifndef __MSSM11atQ_mA_hpp__
#define __MSSM11atQ_mA_hpp__

// Parent model must be declared first! Include it here to ensure that this happens.
#include "gambit/Models/models/MSSM16atQ_mA.hpp"

#define MODEL MSSM11atQ_mA
#define PARENT MSSM16atQ_mA
  START_MODEL

  DEFINEPARS(Qin,TanBeta,
             mA,mu,M1,M2,M3)

  DEFINEPARS(mq2)

  DEFINEPARS(ml2)

  DEFINEPARS(Ae_3)

  DEFINEPARS(Ad_3)

  DEFINEPARS(Au_3)

  INTERPRET_AS_PARENT_FUNCTION(MSSM11atQ_mA_to_MSSM16atQ_mA)

#undef PARENT
#undef MODEL

#endif
```


-------------------------------

Updated on 2022-09-08 at 02:00:51 +0000
