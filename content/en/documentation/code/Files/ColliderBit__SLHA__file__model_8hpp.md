---
title: "file models/ColliderBit_SLHA_file_model.hpp"

description: "[No description available]"

---

# file models/ColliderBit_SLHA_file_model.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/colliderbit__slha__file__model_8hpp/#define-model)**  |

## Detailed Description


**Author**: Anders Kvellestad ([anders.kvellestad@fys.uio.no](mailto:anders.kvellestad@fys.uio.no)) 

**Date**: 

  * 2019 Jul 
  * 2020 Dec


Dummy model for doing a ColliderBit-only scan over a set of SLHA files



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define MODEL

```
#define MODEL ColliderBit_SLHA_file_model
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Dummy model for doing a ColliderBit-only 
///  scan over a set of SLHA files
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Anders Kvellestad
///          (anders.kvellestad@fys.uio.no)
///  \date 2019 Jul
///  \date 2020 Dec
///
///  *********************************************


#ifndef __colliderbit_slha_file_model_hpp__
#define __colliderbit_slha_file_model_hpp__

#define MODEL ColliderBit_SLHA_file_model
  START_MODEL
  DEFINEPARS(dummy)
#undef MODEL

#endif /* defined(__colliderbit_slha_file_model_hpp__) */
```


-------------------------------

Updated on 2022-09-08 at 03:17:36 +0000
