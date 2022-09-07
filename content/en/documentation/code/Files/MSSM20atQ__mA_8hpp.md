---
title: "file models/MSSM20atQ_mA.hpp"

description: "[No description available]"

---

# file models/MSSM20atQ_mA.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/mssm20atq__ma_8hpp/#define-model)**  |
|  | **[PARENT](/documentation/code/files/mssm20atq__ma_8hpp/#define-parent)**  |

## Detailed Description


**Author**: Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 

**Date**: 2017 Aug

MSSM20atQ_mA model definition.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define MODEL

```
#define MODEL MSSM20atQ_mA
```


### define PARENT

```
#define PARENT MSSM25atQ_mA
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  MSSM20atQ_mA model definition.
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

#ifndef __MSSM20atQ_mA_hpp__
#define __MSSM20atQ_mA_hpp__

// Parent model must be declared first! Include it here to ensure that this happens.
#include "gambit/Models/models/MSSM25atQ_mA.hpp"
#include "gambit/Models/models/MSSM20atQ.hpp"

#define MODEL MSSM20atQ_mA
#define PARENT MSSM25atQ_mA
  START_MODEL

  DEFINEPARS(Qin,TanBeta,
             mA,mu,M1,M2,M3)

  DEFINEPARS(mq2_12, mq2_3)

  DEFINEPARS(ml2_12, ml2_3)

  DEFINEPARS(md2_12, md2_3)

  DEFINEPARS(mu2_12, mu2_3)

  DEFINEPARS(me2_12, me2_3)

  DEFINEPARS(Ae_12, Ae_3)

  DEFINEPARS(Ad_3)

  DEFINEPARS(Au_3)

  INTERPRET_AS_PARENT_FUNCTION(MSSM20atQ_mA_to_MSSM25atQ_mA)
  INTERPRET_AS_X_FUNCTION(MSSM20atQ, MSSM20atQ_mA_to_MSSM20atQ)
  INTERPRET_AS_X_DEPENDENCY(MSSM20atQ, unimproved_MSSM_spectrum, Spectrum)

#undef PARENT
#undef MODEL

#endif
```


-------------------------------

Updated on 2022-09-07 at 23:22:09 +0000
