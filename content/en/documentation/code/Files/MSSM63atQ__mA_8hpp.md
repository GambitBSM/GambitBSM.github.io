---
title: "file models/MSSM63atQ_mA.hpp"

description: "[No description available]"

---

# file models/MSSM63atQ_mA.hpp

[No description available]

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |

## Functions

|                | Name           |
| -------------- | -------------- |
| START_MODEL | **[DEFINEPARS](/documentation/code/files/mssm63atq__ma_8hpp/#function-definepars)**(Qin , TanBeta , mA , mu , M1 , M2 , M3 )<br>Can translate this model into MSSM63atQ.  |
| START_MODEL mq2_33 | **[DEFINEPARS](/documentation/code/files/mssm63atq__ma_8hpp/#function-definepars)**(ml2_11 , ml2_12 , ml2_13 , ml2_22 , ml2_23 , ml2_33 ) |
| START_MODEL mq2_33 md2_33 | **[DEFINEPARS](/documentation/code/files/mssm63atq__ma_8hpp/#function-definepars)**(mu2_11 , mu2_12 , mu2_13 , mu2_22 , mu2_23 , mu2_33 ) |
| START_MODEL mq2_33 md2_33 me2_33 | **[DEFINEPARS](/documentation/code/files/mssm63atq__ma_8hpp/#function-definepars)**(Ae_11 , Ae_12 , Ae_13 , Ae_21 , Ae_22 , Ae_23 , Ae_31 , Ae_32 , Ae_33 ) |

## Attributes

|                | Name           |
| -------------- | -------------- |
| START_MODEL | **[mq2_12](/documentation/code/files/mssm63atq__ma_8hpp/#variable-mq2-12)**  |
| START_MODEL | **[mq2_13](/documentation/code/files/mssm63atq__ma_8hpp/#variable-mq2-13)**  |
| START_MODEL | **[mq2_22](/documentation/code/files/mssm63atq__ma_8hpp/#variable-mq2-22)**  |
| START_MODEL | **[mq2_23](/documentation/code/files/mssm63atq__ma_8hpp/#variable-mq2-23)**  |
| START_MODEL mq2_33 | **[md2_12](/documentation/code/files/mssm63atq__ma_8hpp/#variable-md2-12)**  |
| START_MODEL mq2_33 | **[md2_13](/documentation/code/files/mssm63atq__ma_8hpp/#variable-md2-13)**  |
| START_MODEL mq2_33 | **[md2_22](/documentation/code/files/mssm63atq__ma_8hpp/#variable-md2-22)**  |
| START_MODEL mq2_33 | **[md2_23](/documentation/code/files/mssm63atq__ma_8hpp/#variable-md2-23)**  |
| START_MODEL mq2_33 md2_33 | **[me2_12](/documentation/code/files/mssm63atq__ma_8hpp/#variable-me2-12)**  |
| START_MODEL mq2_33 md2_33 | **[me2_13](/documentation/code/files/mssm63atq__ma_8hpp/#variable-me2-13)**  |
| START_MODEL mq2_33 md2_33 | **[me2_22](/documentation/code/files/mssm63atq__ma_8hpp/#variable-me2-22)**  |
| START_MODEL mq2_33 md2_33 | **[me2_23](/documentation/code/files/mssm63atq__ma_8hpp/#variable-me2-23)**  |
| START_MODEL mq2_33 md2_33 me2_33 | **[Ad_12](/documentation/code/files/mssm63atq__ma_8hpp/#variable-ad-12)**  |
| START_MODEL mq2_33 md2_33 me2_33 | **[Ad_13](/documentation/code/files/mssm63atq__ma_8hpp/#variable-ad-13)**  |
| START_MODEL mq2_33 md2_33 me2_33 | **[Ad_21](/documentation/code/files/mssm63atq__ma_8hpp/#variable-ad-21)**  |
| START_MODEL mq2_33 md2_33 me2_33 | **[Ad_22](/documentation/code/files/mssm63atq__ma_8hpp/#variable-ad-22)**  |
| START_MODEL mq2_33 md2_33 me2_33 | **[Ad_23](/documentation/code/files/mssm63atq__ma_8hpp/#variable-ad-23)**  |
| START_MODEL mq2_33 md2_33 me2_33 | **[Ad_31](/documentation/code/files/mssm63atq__ma_8hpp/#variable-ad-31)**  |
| START_MODEL mq2_33 md2_33 me2_33 | **[Ad_32](/documentation/code/files/mssm63atq__ma_8hpp/#variable-ad-32)**  |

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/mssm63atq__ma_8hpp/#define-model)** <br>FlexibleSUSY compatible general (63 parameters plus sign, plus input scale) MSSM parameterisation.  |
|  | **[PARENT](/documentation/code/files/mssm63atq__ma_8hpp/#define-parent)**  |


## Functions Documentation

### function DEFINEPARS

```
START_MODEL DEFINEPARS(
    Qin ,
    TanBeta ,
    mA ,
    mu ,
    M1 ,
    M2 ,
    M3 
)
```

Can translate this model into MSSM63atQ. 

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
#define MODEL MSSM63atQ_mA
```

FlexibleSUSY compatible general (63 parameters plus sign, plus input scale) MSSM parameterisation. 

### define PARENT

```
#define PARENT MSSM63atQ
```


## Source code

```
///  GAMBIT: Global and Modular BSM Inference Tool
///  *********************************************
///
///  MSSM input parameter definition, with A pole
///  mass and mu as explicit input parameters
///  instead of mHu2 and mHd2.
///
///  *********************************************
///
///  Authors
///  =======
///
///  (add name and date if you modify)
///
///  \author Pat Scott
///          (p.scott@imperial.ac.uk)
///  \date 2017 Aug
///
///  *********************************************

#ifndef __MSSM63atQ_mA_hpp__
#define __MSSM63atQ_mA_hpp__

#include "gambit/Models/models/MSSM63atQ.hpp" // Must include models which are targets of translation functions

// Forward declaration of needed types
// Also declare a helper function for translating 'mA' MSSM parameterisations into the primary parameterisations,
// and another for translating from scales MGUT and MSUSY to arbitrary scale Q
// (function definition in MSSM63atX_mA.cpp and MSSM63atX.cpp respectively)

namespace Gambit
{
   class Spectrum;
   class SubSpectrum;

   // Translation function for mA,mu parameterisation to mHu2,mHd2 parameterisation
   void MSSM_mA_to_MSSM_mhud(const ModelParameters &myP, ModelParameters &targetP, const SubSpectrum& HE);

   // Translation function for MSSM defined at RGE-determined scale (e.g. GUT, SUSY) to arbitrary scale Q
   void MSSMatX_to_MSSMatQ(const ModelParameters &myP, ModelParameters &targetP, const SubSpectrum& HE);
}

/// FlexibleSUSY compatible general (63 parameters plus sign, plus input scale) MSSM parameterisation
#define MODEL MSSM63atQ_mA
#define PARENT MSSM63atQ
  START_MODEL

  /// Can translate this model into MSSM63atQ
  INTERPRET_AS_PARENT_FUNCTION(MSSM63atQ_mA_to_MSSM63atQ)
  /// Depends on an MSSM spectrum, since RGEs must run in order to determine MGUT
  INTERPRET_AS_PARENT_DEPENDENCY(unimproved_MSSM_spectrum, Spectrum)

  DEFINEPARS(Qin,TanBeta,
             mA,mu,M1,M2,M3)

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

Updated on 2022-09-08 at 03:08:05 +0000
