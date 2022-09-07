---
title: 'file models/StandardModel_SLHA2.hpp'

description: "[No description available]"

---

# models/StandardModel_SLHA2.hpp



[No description available] [More...](#detailed-description)

## Functions

|                | Name           |
| -------------- | -------------- |
| START_MODEL | **[DEFINEPARS](/documentation/code/files/standardmodel__slha2_8hpp/#function-definepars)**(alphainv , GF , alphaS ) |
| START_MODEL mTau | **[DEFINEPARS](/documentation/code/files/standardmodel__slha2_8hpp/#function-definepars)**(mNu1 , mNu2 , mNu3 ) |
| START_MODEL mTau mU | **[DEFINEPARS](/documentation/code/files/standardmodel__slha2_8hpp/#function-definepars)**(mS , mCmC ) |

## Attributes

|                | Name           |
| -------------- | -------------- |
| START_MODEL | **[mMu](/documentation/code/files/standardmodel__slha2_8hpp/#variable-mmu)**  |

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/standardmodel__slha2_8hpp/#define-model)**  |

## Detailed Description


**Author**: Ben Farmer ([benjamin.farmer@fysik.su.se](mailto:benjamin.farmer@fysik.su.se)) 

**Date**: 2014 Sep - Dec, 2015 Jan - Mar

Standard Model parameters, defined in SLHA2 conventions. Corresponds directly to the SLHA2 "SMINPUTS" block.

SMINPUTS is also a CAPABILITY that module writers may be interested in using.

SLHA2 conventions:

SMINPUTS block description:

// SLHA1 alphainv; // 1: Inverse electromagnetic coupling at the Z pole in the MSbar scheme (with 5 active flavours) GF; // 2: Fermi constant (in units of GeV^-2) alphaS; // 3: Strong coupling at the Z pole in the MSbar scheme (with 5 active flavours). mZ; // 4: Z pole mass mBmB; // 5: b quark running mass in the MSbar scheme (at mB) mT; // 6: Top quark pole mass mTau; // 7: Tau pole mass

// SLHA2 mNu3; // 8: Heaviest neutrino pole mass

mE; // 11: Electron pole mass mNu1; // 12: Lightest neutrino pole mass mMu; // 13: Muon pole mass mNu2; // 14: Second lightest neutrino pole mass

mD; // 21: d quark running mass in the MSbar scheme at 2 GeV 

 mU; // 22: u quark running mass in the MSbar scheme at 2 GeV 

 mS; // 23: s quark running mass in the MSbar scheme at 2 GeV 

 mCmC; // 24: c quark running mass in the MSbar scheme at mC 


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
    mNu1 ,
    mNu2 ,
    mNu3 
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
#define MODEL StandardModel_SLHA2
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///  
///  Standard Model parameters, defined in SLHA2
///  conventions. Corresponds directly to the
///  SLHA2 "SMINPUTS" block.
///
///  SMINPUTS is also a CAPABILITY that module
///  writers may be interested in using.
///
///  SLHA2 conventions:
///
///  SMINPUTS block description: 
///
///    // SLHA1
///    alphainv;  // 1: Inverse electromagnetic coupling at the Z pole in the MSbar scheme (with 5 active flavours)
///    GF;        // 2: Fermi constant (in units of GeV^-2)
///    alphaS;    // 3: Strong coupling at the Z pole in the MSbar scheme (with 5 active flavours). 
///    mZ;        // 4: Z pole mass
///    mBmB;      // 5: b quark running mass in the MSbar scheme (at mB)
///    mT;        // 6: Top quark pole mass
///    mTau;      // 7: Tau pole mass
///    
///    // SLHA2
///    mNu3;      // 8: Heaviest neutrino pole mass
///    
///    mE;        // 11: Electron pole mass
///    mNu1;      // 12: Lightest neutrino pole mass
///    mMu;       // 13: Muon pole mass
///    mNu2;      // 14: Second lightest neutrino pole mass
///    
///    mD;        // 21: d quark running mass in the MSbar scheme at 2 GeV        
///    mU;        // 22: u quark running mass in the MSbar scheme at 2 GeV        
///    mS;        // 23: s quark running mass in the MSbar scheme at 2 GeV        
///    mCmC;      // 24: c quark running mass in the MSbar scheme at mC      
///    
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Ben Farmer
///          (benjamin.farmer@fysik.su.se)
///    \date 2014 Sep - Dec, 2015 Jan - Mar
///  
///  *********************************************


#ifndef __StandardModel_SLHA2_hpp__
#define __StandardModel_SLHA2_hpp__

// Standard Model parameterisation in SLHA2 conventions
#define MODEL StandardModel_SLHA2
  START_MODEL

  DEFINEPARS(alphainv, GF, alphaS) // 1,2,3
  DEFINEPARS(mZ)                   // 4
        
  DEFINEPARS(mE, mMu, mTau)        // 11,13,7
  DEFINEPARS(mNu1, mNu2, mNu3)     // 12,14,8

  DEFINEPARS(mD, mU)               // 21,22
  DEFINEPARS(mS, mCmC)             // 23,24
  DEFINEPARS(mBmB, mT)             // 5,6

  // CKM parameters
  DEFINEPARS(CKM_lambda, CKM_A, CKM_rhobar, CKM_etabar)

  // PMNS parameters
  DEFINEPARS(theta12, theta23, theta13)
  DEFINEPARS(delta13, alpha1, alpha2)

 #undef MODEL
#endif 
```


-------------------------------

Updated on 2022-09-07 at 13:49:53 +0000
