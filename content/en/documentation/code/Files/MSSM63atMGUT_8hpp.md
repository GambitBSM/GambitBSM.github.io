---
title: 'file models/MSSM63atMGUT.hpp'

description: "[No description available]"

---

# models/MSSM63atMGUT.hpp

[No description available]

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |

## Functions

|                | Name           |
| -------------- | -------------- |
| START_MODEL | **[DEFINEPARS](/documentation/code/files/mssm63atmgut_8hpp/#function-definepars)**(TanBeta , SignMu , mHu2 , mHd2 , M1 , M2 , M3 )<br>Can translate this model into MSSM63atQ (where Q will then be set to MGUT)  |
| START_MODEL mq2_33 | **[DEFINEPARS](/documentation/code/files/mssm63atmgut_8hpp/#function-definepars)**(ml2_11 , ml2_12 , ml2_13 , ml2_22 , ml2_23 , ml2_33 ) |
| START_MODEL mq2_33 md2_33 | **[DEFINEPARS](/documentation/code/files/mssm63atmgut_8hpp/#function-definepars)**(mu2_11 , mu2_12 , mu2_13 , mu2_22 , mu2_23 , mu2_33 ) |
| START_MODEL mq2_33 md2_33 me2_33 | **[DEFINEPARS](/documentation/code/files/mssm63atmgut_8hpp/#function-definepars)**(Ae_11 , Ae_12 , Ae_13 , Ae_21 , Ae_22 , Ae_23 , Ae_31 , Ae_32 , Ae_33 ) |

## Attributes

|                | Name           |
| -------------- | -------------- |
| START_MODEL | **[mq2_12](/documentation/code/files/mssm63atmgut_8hpp/#variable-mq2-12)**  |
| START_MODEL | **[mq2_13](/documentation/code/files/mssm63atmgut_8hpp/#variable-mq2-13)**  |
| START_MODEL | **[mq2_22](/documentation/code/files/mssm63atmgut_8hpp/#variable-mq2-22)**  |
| START_MODEL | **[mq2_23](/documentation/code/files/mssm63atmgut_8hpp/#variable-mq2-23)**  |
| START_MODEL mq2_33 | **[md2_12](/documentation/code/files/mssm63atmgut_8hpp/#variable-md2-12)**  |
| START_MODEL mq2_33 | **[md2_13](/documentation/code/files/mssm63atmgut_8hpp/#variable-md2-13)**  |
| START_MODEL mq2_33 | **[md2_22](/documentation/code/files/mssm63atmgut_8hpp/#variable-md2-22)**  |
| START_MODEL mq2_33 | **[md2_23](/documentation/code/files/mssm63atmgut_8hpp/#variable-md2-23)**  |
| START_MODEL mq2_33 md2_33 | **[me2_12](/documentation/code/files/mssm63atmgut_8hpp/#variable-me2-12)**  |
| START_MODEL mq2_33 md2_33 | **[me2_13](/documentation/code/files/mssm63atmgut_8hpp/#variable-me2-13)**  |
| START_MODEL mq2_33 md2_33 | **[me2_22](/documentation/code/files/mssm63atmgut_8hpp/#variable-me2-22)**  |
| START_MODEL mq2_33 md2_33 | **[me2_23](/documentation/code/files/mssm63atmgut_8hpp/#variable-me2-23)**  |
| START_MODEL mq2_33 md2_33 me2_33 | **[Ad_12](/documentation/code/files/mssm63atmgut_8hpp/#variable-ad-12)**  |
| START_MODEL mq2_33 md2_33 me2_33 | **[Ad_13](/documentation/code/files/mssm63atmgut_8hpp/#variable-ad-13)**  |
| START_MODEL mq2_33 md2_33 me2_33 | **[Ad_21](/documentation/code/files/mssm63atmgut_8hpp/#variable-ad-21)**  |
| START_MODEL mq2_33 md2_33 me2_33 | **[Ad_22](/documentation/code/files/mssm63atmgut_8hpp/#variable-ad-22)**  |
| START_MODEL mq2_33 md2_33 me2_33 | **[Ad_23](/documentation/code/files/mssm63atmgut_8hpp/#variable-ad-23)**  |
| START_MODEL mq2_33 md2_33 me2_33 | **[Ad_31](/documentation/code/files/mssm63atmgut_8hpp/#variable-ad-31)**  |
| START_MODEL mq2_33 md2_33 me2_33 | **[Ad_32](/documentation/code/files/mssm63atmgut_8hpp/#variable-ad-32)**  |

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/mssm63atmgut_8hpp/#define-model)** <br>FlexibleSUSY compatible general (63 parameters plus sign) GUT scale MSSM parameterisation.  |
|  | **[PARENT](/documentation/code/files/mssm63atmgut_8hpp/#define-parent)**  |


## Functions Documentation

### function DEFINEPARS

```
START_MODEL DEFINEPARS(
    TanBeta ,
    SignMu ,
    mHu2 ,
    mHd2 ,
    M1 ,
    M2 ,
    M3 
)
```

Can translate this model into MSSM63atQ (where Q will then be set to MGUT) 

Depends on an MSSM spectrum, since RGEs must run in order to determine MGUT Mass matrices are symmetric (Hermitian, and we are restricted to real entries at the moment) so only one 'triangle' needed. 


### function DEFINEPARS

```
START_MODEL mq2_33 DEFINEPARS(
    ml2_11 ,
    ml2_12 ,
    ml2_13 ,
    ml2_22 ,
    ml2_23 ,
    ml2_33 
)
```


### function DEFINEPARS

```
START_MODEL mq2_33 md2_33 DEFINEPARS(
    mu2_11 ,
    mu2_12 ,
    mu2_13 ,
    mu2_22 ,
    mu2_23 ,
    mu2_33 
)
```


### function DEFINEPARS

```
START_MODEL mq2_33 md2_33 me2_33 DEFINEPARS(
    Ae_11 ,
    Ae_12 ,
    Ae_13 ,
    Ae_21 ,
    Ae_22 ,
    Ae_23 ,
    Ae_31 ,
    Ae_32 ,
    Ae_33 
)
```



## Attributes Documentation

### variable mq2_12

```
START_MODEL mq2_12;
```


### variable mq2_13

```
START_MODEL mq2_13;
```


### variable mq2_22

```
START_MODEL mq2_22;
```


### variable mq2_23

```
START_MODEL mq2_23;
```


### variable md2_12

```
START_MODEL mq2_33 md2_12;
```


### variable md2_13

```
START_MODEL mq2_33 md2_13;
```


### variable md2_22

```
START_MODEL mq2_33 md2_22;
```


### variable md2_23

```
START_MODEL mq2_33 md2_23;
```


### variable me2_12

```
START_MODEL mq2_33 md2_33 me2_12;
```


### variable me2_13

```
START_MODEL mq2_33 md2_33 me2_13;
```


### variable me2_22

```
START_MODEL mq2_33 md2_33 me2_22;
```


### variable me2_23

```
START_MODEL mq2_33 md2_33 me2_23;
```


### variable Ad_12

```
START_MODEL mq2_33 md2_33 me2_33 Ad_12;
```


### variable Ad_13

```
START_MODEL mq2_33 md2_33 me2_33 Ad_13;
```


### variable Ad_21

```
START_MODEL mq2_33 md2_33 me2_33 Ad_21;
```


### variable Ad_22

```
START_MODEL mq2_33 md2_33 me2_33 Ad_22;
```


### variable Ad_23

```
START_MODEL mq2_33 md2_33 me2_33 Ad_23;
```


### variable Ad_31

```
START_MODEL mq2_33 md2_33 me2_33 Ad_31;
```


### variable Ad_32

```
START_MODEL mq2_33 md2_33 me2_33 Ad_32;
```



## Macros Documentation

### define MODEL

```
#define MODEL MSSM63atMGUT
```

FlexibleSUSY compatible general (63 parameters plus sign) GUT scale MSSM parameterisation. 

### define PARENT

```
#define PARENT MSSM63atQ
```


## Source code

```
//  GAMBIT: Global and Modular BSM Inference Tool
//  *********************************************
//
//  MSSM63 model declaration
//
//
//  *********************************************
//
//  Authors
//  =======
//
//  (add name and date if you modify)
//
//  Ben Farmer
//  2013 May, ???, 2014 Mar, 2015 Jan
//  Pat Scott
//  2013 Sep
//
//  *********************************************

#ifndef __MSSM63atMGUT_hpp__
#define __MSSM63atMGUT_hpp__

#include "gambit/Models/models/MSSM63atQ.hpp" // Must include models which are targets of translation functions

// Forward declaration of needed types
namespace Gambit
{
   class Spectrum;
}

// General GUT boundary condition parameterisation of the MSSM
// There are several of these, compatible with different spectrum generators
// To use a constrained GUT model like the CMSSM, there needs to be an
// "interpret_as_X" function which translates the CMSSM parameters into
// the appropriate general GUT parameterisation for the spectrum generator
// being used.

/// FlexibleSUSY compatible general (63 parameters plus sign) GUT scale MSSM parameterisation
#define MODEL  MSSM63atMGUT
#define PARENT MSSM63atQ
  START_MODEL

  /// Can translate this model into MSSM63atQ (where Q will then be set to MGUT)
  INTERPRET_AS_PARENT_FUNCTION(MSSM63atMGUT_to_MSSM63atQ)
  /// Depends on an MSSM spectrum, since RGEs must run in order to determine MGUT
  INTERPRET_AS_PARENT_DEPENDENCY(unimproved_MSSM_spectrum, Spectrum)

  DEFINEPARS(TanBeta,SignMu,
             mHu2,mHd2,M1,M2,M3)

  /// Mass matrices are symmetric (Hermitian, and we are restricted to real entries at the moment)
  /// so only one 'triangle' needed.
  DEFINEPARS(mq2_11, mq2_12, mq2_13,
                     mq2_22, mq2_23,
                             mq2_33)

  DEFINEPARS(ml2_11, ml2_12, ml2_13,
                     ml2_22, ml2_23,
                             ml2_33)

  DEFINEPARS(md2_11, md2_12, md2_13,
                     md2_22, md2_23,
                             md2_33)

  DEFINEPARS(mu2_11, mu2_12, mu2_13,
                     mu2_22, mu2_23,
                             mu2_33)

  DEFINEPARS(me2_11, me2_12, me2_13,
                     me2_22, me2_23,
                             me2_33)

  DEFINEPARS(Ae_11, Ae_12, Ae_13,
             Ae_21, Ae_22, Ae_23,
             Ae_31, Ae_32, Ae_33)

  DEFINEPARS(Ad_11, Ad_12, Ad_13,
             Ad_21, Ad_22, Ad_23,
             Ad_31, Ad_32, Ad_33)

  DEFINEPARS(Au_11, Au_12, Au_13,
             Au_21, Au_22, Au_23,
             Au_31, Au_32, Au_33)
#undef PARENT
#undef MODEL

#endif
```


-------------------------------

Updated on 2022-09-07 at 14:07:48 +0000
