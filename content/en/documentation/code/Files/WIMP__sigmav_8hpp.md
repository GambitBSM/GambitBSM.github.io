---
title: "file models/WIMP_sigmav.hpp"

description: "[No description available]"

---

# file models/WIMP_sigmav.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/wimp__sigmav_8hpp/#define-model)**  |

## Detailed Description


**Author**: Ben Farmer ([b.farmer@imperial.ac.uk](mailto:b.farmer@imperial.ac.uk)) 

**Date**: 2019 Aug

WIMP_sigmav model declarations. A simple parameterisation of generic WIMP self-annihilation to two-body SM final states. Basic s + p wave expansion, i.e. sigma v = A + B v^2 for each channel



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define MODEL

```
#define MODEL WIMP_sigmav
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  WIMP_sigmav model declarations. 
///  A simple parameterisation of generic WIMP
///  self-annihilation to two-body SM final states.
///  Basic s + p wave expansion, i.e.
///  sigma v = A + B v^2
///  for each channel
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///   
///  \author Ben Farmer
///          (b.farmer@imperial.ac.uk)
///  \date 2019 Aug
///
///  *********************************************


#ifndef __WIMP_sigmav_hpp__
#define __WIMP_sigmav_hpp__

#define MODEL WIMP_sigmav
  START_MODEL
  DEFINEPARS(A_bb, B_bb) 
  DEFINEPARS(A_WW, B_WW) 
  DEFINEPARS(A_cc, B_cc)
  DEFINEPARS(A_tautau, B_tautau)
  DEFINEPARS(A_ZZ, B_ZZ) 
  DEFINEPARS(A_tt, B_tt)
  DEFINEPARS(A_hh, B_hh)
#undef MODEL

#endif
```


-------------------------------

Updated on 2024-05-31 at 15:12:06 +0000
