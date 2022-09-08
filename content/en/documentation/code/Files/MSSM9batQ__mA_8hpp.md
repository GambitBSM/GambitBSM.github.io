---
title: "file models/MSSM9batQ_mA.hpp"

description: "[No description available]"

---

# file models/MSSM9batQ_mA.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/mssm9batq__ma_8hpp/#define-mssm9batq-ma-hpp-model)**  |
|  | **[PARENT](/documentation/code/files/mssm9batq__ma_8hpp/#define-mssm9batq-ma-hpp-parent)**  |

## Detailed Description


**Author**: Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 

**Date**: 2017 Aug

MSSM9batQ_mA model definition.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define MODEL

```
#define MODEL MSSM9batQ_mA
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
///  MSSM9batQ_mA model definition.
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

#ifndef __MSSM9batQ_mA_hpp__
#define __MSSM9batQ_mA_hpp__

// Parent model must be declared first! Include it here to ensure that this happens.
#include "gambit/Models/models/MSSM15atQ_mA.hpp"

#define MODEL MSSM9batQ_mA
#define PARENT MSSM15atQ_mA
  START_MODEL

  DEFINEPARS(Qin,TanBeta,
             mA,mu,M1,M2,M3)

  DEFINEPARS(mq2_3)

  DEFINEPARS(msf2)

  DEFINEPARS(Au_3)

  INTERPRET_AS_PARENT_FUNCTION(MSSM9batQ_mA_to_MSSM15atQ_mA)

#undef PARENT
#undef MODEL

#endif
```


-------------------------------

Updated on 2022-09-08 at 01:48:58 +0000
