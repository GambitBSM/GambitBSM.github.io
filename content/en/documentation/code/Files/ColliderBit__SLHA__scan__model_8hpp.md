---
title: "file models/ColliderBit_SLHA_scan_model.hpp"

description: "[No description available]"

---

# file models/ColliderBit_SLHA_scan_model.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/colliderbit__slha__scan__model_8hpp/#define-model)**  |

## Detailed Description


**Author**: Anders Kvellestad ([anders.kvellestad@fys.uio.no](mailto:anders.kvellestad@fys.uio.no)) 

**Date**: 

  * 2019 Jul 
  * 2020 Dec


Dummy model for doing a ColliderBit-only scan based on replacing SLHA file entries



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define MODEL

```
#define MODEL ColliderBit_SLHA_scan_model
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Dummy model for doing a ColliderBit-only 
///  scan based on replacing SLHA file entries
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


#ifndef __colliderbit_slha_scan_model_hpp__
#define __colliderbit_slha_scan_model_hpp__

#define MODEL ColliderBit_SLHA_scan_model
  START_MODEL
  DEFINEPARS(m1,m2,cross_section_fb,cross_section_uncert_fb,br1,br2)
#undef MODEL

#endif /* defined(__colliderbit_slha_scan_model_hpp__) */
```


-------------------------------

Updated on 2024-05-31 at 15:12:06 +0000
