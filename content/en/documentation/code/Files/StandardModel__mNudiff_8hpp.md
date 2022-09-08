---
title: "file models/StandardModel_mNudiff.hpp"

description: "[No description available]"

---

# file models/StandardModel_mNudiff.hpp

[No description available] [More...](#detailed-description)

## Functions

|                | Name           |
| -------------- | -------------- |
| START_MODEL | **[DEFINEPARS](/documentation/code/files/standardmodel__mnudiff_8hpp/#function-standardmodel-mnudiff-hpp-definepars)**(alphainv , GF , alphaS ) |
| START_MODEL mTau | **[DEFINEPARS](/documentation/code/files/standardmodel__mnudiff_8hpp/#function-standardmodel-mnudiff-hpp-definepars)**(mNu_light , dmNu21 , dmNu3l ) |
| START_MODEL mTau mU | **[DEFINEPARS](/documentation/code/files/standardmodel__mnudiff_8hpp/#function-standardmodel-mnudiff-hpp-definepars)**(mS , mCmC ) |

## Attributes

|                | Name           |
| -------------- | -------------- |
| START_MODEL | **[mMu](/documentation/code/files/standardmodel__mnudiff_8hpp/#variable-standardmodel-mnudiff-hpp-mmu)**  |

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/standardmodel__mnudiff_8hpp/#define-standardmodel-mnudiff-hpp-model)**  |
|  | **[PARENT](/documentation/code/files/standardmodel__mnudiff_8hpp/#define-standardmodel-mnudiff-hpp-parent)**  |

## Detailed Description


**Author**: Tomas Gonzalo ([tomas.gonzalo@monash.edu](mailto:tomas.gonzalo@monash.edu)) 

**Date**: 2018

Standard Model parameters, inhereting from SLHA2 model, but using differential neutrino masses



------------------

Authors (add name and date if you modify):



------------------


## Functions Documentation

### function DEFINEPARS

```
START_MODEL DEFINEPARS(
    alphainv ,
    GF ,
    alphaS 
)
```


### function DEFINEPARS

```
START_MODEL mTau DEFINEPARS(
    mNu_light ,
    dmNu21 ,
    dmNu3l 
)
```


### function DEFINEPARS

```
START_MODEL mTau mU DEFINEPARS(
    mS ,
    mCmC 
)
```



## Attributes Documentation

### variable mMu

```
START_MODEL mMu;
```



## Macros Documentation

### define MODEL

```
#define MODEL StandardModel_mNudiff
```


### define PARENT

```
#define PARENT StandardModel_SLHA2
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///  
///  Standard Model parameters, inhereting from SLHA2
///  model, but using differential neutrino masses
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Tomas Gonzalo
///          (tomas.gonzalo@monash.edu)
///  \date 2018
///  
///  *********************************************


#ifndef __StandardModel_mNudiff_hpp__
#define __StandardModel_mNudiff_hpp__

#include "gambit/Models/models/StandardModel_SLHA2.hpp"

// Standard Model parameterisation in SLHA2 conventions
#define MODEL StandardModel_mNudiff
#define PARENT StandardModel_SLHA2
  START_MODEL

  DEFINEPARS(alphainv, GF, alphaS) // 1,2,3
  DEFINEPARS(mZ)                   // 4
        
  DEFINEPARS(mE, mMu, mTau)        // 11,13,7
  DEFINEPARS(mNu_light, dmNu21, dmNu3l)  // Differential neutrino masses

  DEFINEPARS(mD, mU)               // 21,22
  DEFINEPARS(mS, mCmC)             // 23,24
  DEFINEPARS(mBmB, mT)             // 5,6

  // CKM parameters
  DEFINEPARS(CKM_lambda, CKM_A, CKM_rhobar, CKM_etabar)

  // PMNS parameters
  DEFINEPARS(theta12, theta23, theta13)
  DEFINEPARS(delta13, alpha1, alpha2)

  INTERPRET_AS_PARENT_FUNCTION(StandardModel_mNudiff_to_StandardModel_SLHA2)

#undef PARENT
#undef MODEL
#endif 
```


-------------------------------

Updated on 2022-09-08 at 01:48:58 +0000
