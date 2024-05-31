---
title: "file models/MSSMatMGUT_mA.cpp"

description: "[No description available]"

---

# file models/MSSMatMGUT_mA.cpp

[No description available]

## Functions

|                | Name           |
| -------------- | -------------- |
| | **[MSSM_mA_to_MSSM_mhud](/documentation/code/files/mssmatmgut__ma_8cpp/#function-mssm-ma-to-mssm-mhud)**(myP , targetP , HE ) |
| | **[MSSM30atX_to_MSSM63atX](/documentation/code/files/mssmatmgut__ma_8cpp/#function-mssm30atx-to-mssm63atx)**(myP , targetP ) |
| | **[USE_MODEL_PIPE](/documentation/code/files/mssmatmgut__ma_8cpp/#function-use-model-pipe)**(FRIEND ) const |
| | **[MSSM25atX_to_MSSM30atX](/documentation/code/files/mssmatmgut__ma_8cpp/#function-mssm25atx-to-mssm30atx)**(myP , targetP ) |
| | **[MSSM20atX_to_MSSM25atX](/documentation/code/files/mssmatmgut__ma_8cpp/#function-mssm20atx-to-mssm25atx)**(myP , targetP ) |

## Attributes

|                | Name           |
| -------------- | -------------- |
| void ModelParameters & | **[targetP](/documentation/code/files/mssmatmgut__ma_8cpp/#variable-targetp)**  |
| const SubSpectrum & | **[HE](/documentation/code/files/mssmatmgut__ma_8cpp/#variable-he)**  |

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/mssmatmgut__ma_8cpp/#define-model)**  |
|  | **[PARENT](/documentation/code/files/mssmatmgut__ma_8cpp/#define-parent)**  |
|  | **[MODEL](/documentation/code/files/mssmatmgut__ma_8cpp/#define-model)**  |
|  | **[PARENT](/documentation/code/files/mssmatmgut__ma_8cpp/#define-parent)**  |
|  | **[FRIEND](/documentation/code/files/mssmatmgut__ma_8cpp/#define-friend)**  |
|  | **[MODEL](/documentation/code/files/mssmatmgut__ma_8cpp/#define-model)**  |
|  | **[PARENT](/documentation/code/files/mssmatmgut__ma_8cpp/#define-parent)**  |
|  | **[MODEL](/documentation/code/files/mssmatmgut__ma_8cpp/#define-model)**  |
|  | **[PARENT](/documentation/code/files/mssmatmgut__ma_8cpp/#define-parent)**  |
|  | **[FRIEND](/documentation/code/files/mssmatmgut__ma_8cpp/#define-friend)**  |


## Functions Documentation

### function MSSM_mA_to_MSSM_mhud

```
MSSM_mA_to_MSSM_mhud(
    myP ,
    targetP ,
    HE 
)
```


### function MSSM30atX_to_MSSM63atX

```
MSSM30atX_to_MSSM63atX(
    myP ,
    targetP 
)
```


### function USE_MODEL_PIPE

```
USE_MODEL_PIPE(
    FRIEND 
) const
```


### function MSSM25atX_to_MSSM30atX

```
MSSM25atX_to_MSSM30atX(
    myP ,
    targetP 
)
```


### function MSSM20atX_to_MSSM25atX

```
MSSM20atX_to_MSSM25atX(
    myP ,
    targetP 
)
```



## Attributes Documentation

### variable targetP

```
void ModelParameters & targetP {
     logger()<<"Running interpret_as_parent calculations for " STRINGIFY(MODEL) " --> " STRINGIFY(PARENT) "."<<LogTags::info<<EOM;
```


### variable HE

```
const SubSpectrum & HE = Dep::unimproved_MSSM_spectrum->get_HE();
```



## Macros Documentation

### define MODEL

```
#define MODEL MSSM63atMGUT_mA
```


Translation function definitions for the MSSM models with boundary conditions at scale MGUT and with A pole mass and mu as explicit input parameters instead of mHu2 and mHd2.

Contains the interpret-as-parent translation functions for:

MSSM63atMGUT_mA --> MSSM63atMGUT MSSM30atMGUT_mA --> MSSM63atMGUT_mA MSSM25atMGUT_mA --> MSSM30atMGUT_mA MSSM20atMGUT_mA --> MSSM25atMGUT_mA

As well as the interpret-as-friend translation functions for:

MSSM30atMGUT_mA --> MSSM30atMGUT MSSM20atMGUT_mA --> MSSM20atMGUT



------------------


# Authors

(add name and date if you modify)

Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 

2015 Sep 

2017 Aug

Ben Farmer ([benjamin.farmer@fysik.su.se](mailto:benjamin.farmer@fysik.su.se)) 

2017 Sep, Oct

Tomas Gonzalo ([tomas.gonzalo@kit.edu](mailto:tomas.gonzalo@kit.edu)) 

2022 Sept



------------------


### define PARENT

```
#define PARENT MSSM63atMGUT
```


### define MODEL

```
#define MODEL MSSM63atMGUT_mA
```


Translation function definitions for the MSSM models with boundary conditions at scale MGUT and with A pole mass and mu as explicit input parameters instead of mHu2 and mHd2.

Contains the interpret-as-parent translation functions for:

MSSM63atMGUT_mA --> MSSM63atMGUT MSSM30atMGUT_mA --> MSSM63atMGUT_mA MSSM25atMGUT_mA --> MSSM30atMGUT_mA MSSM20atMGUT_mA --> MSSM25atMGUT_mA

As well as the interpret-as-friend translation functions for:

MSSM30atMGUT_mA --> MSSM30atMGUT MSSM20atMGUT_mA --> MSSM20atMGUT



------------------


# Authors

(add name and date if you modify)

Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 

2015 Sep 

2017 Aug

Ben Farmer ([benjamin.farmer@fysik.su.se](mailto:benjamin.farmer@fysik.su.se)) 

2017 Sep, Oct

Tomas Gonzalo ([tomas.gonzalo@kit.edu](mailto:tomas.gonzalo@kit.edu)) 

2022 Sept



------------------


### define PARENT

```
#define PARENT MSSM63atMGUT
```


### define FRIEND

```
#define FRIEND MSSM30atMGUT
```


### define MODEL

```
#define MODEL MSSM63atMGUT_mA
```


Translation function definitions for the MSSM models with boundary conditions at scale MGUT and with A pole mass and mu as explicit input parameters instead of mHu2 and mHd2.

Contains the interpret-as-parent translation functions for:

MSSM63atMGUT_mA --> MSSM63atMGUT MSSM30atMGUT_mA --> MSSM63atMGUT_mA MSSM25atMGUT_mA --> MSSM30atMGUT_mA MSSM20atMGUT_mA --> MSSM25atMGUT_mA

As well as the interpret-as-friend translation functions for:

MSSM30atMGUT_mA --> MSSM30atMGUT MSSM20atMGUT_mA --> MSSM20atMGUT



------------------


# Authors

(add name and date if you modify)

Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 

2015 Sep 

2017 Aug

Ben Farmer ([benjamin.farmer@fysik.su.se](mailto:benjamin.farmer@fysik.su.se)) 

2017 Sep, Oct

Tomas Gonzalo ([tomas.gonzalo@kit.edu](mailto:tomas.gonzalo@kit.edu)) 

2022 Sept



------------------


### define PARENT

```
#define PARENT MSSM63atMGUT
```


### define MODEL

```
#define MODEL MSSM63atMGUT_mA
```


Translation function definitions for the MSSM models with boundary conditions at scale MGUT and with A pole mass and mu as explicit input parameters instead of mHu2 and mHd2.

Contains the interpret-as-parent translation functions for:

MSSM63atMGUT_mA --> MSSM63atMGUT MSSM30atMGUT_mA --> MSSM63atMGUT_mA MSSM25atMGUT_mA --> MSSM30atMGUT_mA MSSM20atMGUT_mA --> MSSM25atMGUT_mA

As well as the interpret-as-friend translation functions for:

MSSM30atMGUT_mA --> MSSM30atMGUT MSSM20atMGUT_mA --> MSSM20atMGUT



------------------


# Authors

(add name and date if you modify)

Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 

2015 Sep 

2017 Aug

Ben Farmer ([benjamin.farmer@fysik.su.se](mailto:benjamin.farmer@fysik.su.se)) 

2017 Sep, Oct

Tomas Gonzalo ([tomas.gonzalo@kit.edu](mailto:tomas.gonzalo@kit.edu)) 

2022 Sept



------------------


### define PARENT

```
#define PARENT MSSM63atMGUT
```


### define FRIEND

```
#define FRIEND MSSM30atMGUT
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///
///  Translation function definitions for the
///  MSSM models with boundary conditions at
///  scale MGUT and with A pole mass and mu
///  as explicit input parameters instead of mHu2 and mHd2.
///
///  Contains the interpret-as-parent translation
///  functions for:
///
///  MSSM63atMGUT_mA  --> MSSM63atMGUT
///  MSSM30atMGUT_mA  --> MSSM63atMGUT_mA
///  MSSM25atMGUT_mA  --> MSSM30atMGUT_mA
///  MSSM20atMGUT_mA  --> MSSM25atMGUT_mA
///
///  As well as the interpret-as-friend translation
///  functions for:
///
///  MSSM30atMGUT_mA  --> MSSM30atMGUT
///  MSSM20atMGUT_mA  --> MSSM20atMGUT
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
///  \date 2015 Sep
///  \date 2017 Aug
///
///  \author Ben Farmer
///          (benjamin.farmer@fysik.su.se)
///  \date 2017 Sep, Oct
///
///  \author Tomas Gonzalo
///          (tomas.gonzalo@kit.edu)
///  \date 2022 Sept
///
///  *********************************************

#include "gambit/Models/model_macros.hpp"
#include "gambit/Models/model_helpers.hpp"
#include "gambit/Logs/logger.hpp"
#include "gambit/Utils/numerical_constants.hpp"
#include "gambit/Elements/sminputs.hpp"
#include "gambit/Elements/spectrum.hpp"

#include "gambit/Models/models/MSSMatMGUT_mA.hpp"
#include "gambit/Models/models/MSSM_translation_helpers.hpp"

// Activate debug output
//#define MSSMatMGUT_mA_DBUG

// MSSM63atMGUT_mA --> MSSM63atMGUTA
#define MODEL MSSM63atMGUT_mA
#define PARENT MSSM63atMGUT
  void MODEL_NAMESPACE::CAT_3(MODEL,_to_,PARENT) (const ModelParameters &myP, ModelParameters &targetP)
  {
     logger()<<"Running interpret_as_parent calculations for " STRINGIFY(MODEL) " --> " STRINGIFY(PARENT) "."<<LogTags::info<<EOM;

     USE_MODEL_PIPE(PARENT)
     const SubSpectrum& HE = Dep::unimproved_MSSM_spectrum->get_HE();
     MSSM_mA_to_MSSM_mhud(myP, targetP, HE);

     // Done
     #ifdef MSSMatMGUT_mA_DBUG
       std::cout << STRINGIFY(MODEL) " parameters:" << myP << std::endl;
       std::cout << STRINGIFY(PARENT) " parameters:" << targetP << std::endl;
     #endif
  }
#undef PARENT
#undef MODEL

// MSSM30atMGUT_mA --> MSSM63atMGUT_mA
#define MODEL MSSM30atMGUT_mA
#define PARENT MSSM63atMGUT_mA
  void MODEL_NAMESPACE::CAT_3(MODEL,_to_,PARENT) (const ModelParameters &myP, ModelParameters &targetP)
  {
     logger()<<"Running interpret_as_parent calculations for " STRINGIFY(MODEL) " --> " STRINGIFY(PARENT) "."<<LogTags::info<<EOM;

     MSSM30atX_to_MSSM63atX(myP, targetP);

     // Done
     #ifdef MSSMatMGUT_mA_DBUG
       std::cout << STRINGIFY(MODEL) " parameters:" << myP << std::endl;
       std::cout << STRINGIFY(PARENT) " parameters:" << targetP << std::endl;
     #endif
  }
#undef PARENT

// MSSM30atMGUT_mA --> MSSM30atMGUT
#define FRIEND MSSM30atMGUT
  void MODEL_NAMESPACE::CAT_3(MODEL,_to_,FRIEND) (const ModelParameters &myP, ModelParameters &targetP)
  {
     logger()<<"Running interpret_as_X calculations for " STRINGIFY(MODEL) " --> " STRINGIFY(FRIEND) "."<<LogTags::info<<EOM;

     USE_MODEL_PIPE(FRIEND) // Need the pipe for the TARGET model
     const SubSpectrum& HE = Dep::unimproved_MSSM_spectrum->get_HE();
     MSSM_mA_to_MSSM_mhud(myP, targetP, HE);

     // Done
     #ifdef MSSMatMGUT_mA_DBUG
       std::cout << STRINGIFY(MODEL) " parameters:" << myP << std::endl;
       std::cout << STRINGIFY(FRIEND) " parameters:" << targetP << std::endl;
     #endif
  }
#undef FRIEND
#undef MODEL

// MSSM25atMGUT_mA --> MSSM30atMGUT_mA
#define MODEL MSSM25atMGUT_mA
#define PARENT MSSM30atMGUT_mA
  void MODEL_NAMESPACE::CAT_3(MODEL,_to_,PARENT) (const ModelParameters &myP, ModelParameters &targetP)
  {
     logger()<<"Running interpret_as_parent calculations for " STRINGIFY(MODEL) " --> " STRINGIFY(PARENT) "."<<LogTags::info<<EOM;

     MSSM25atX_to_MSSM30atX(myP, targetP);

     // Done
     #ifdef MSSMatMGUT_mA_DBUG
       std::cout << STRINGIFY(MODEL) " parameters:" << myP << std::endl;
       std::cout << STRINGIFY(PARENT) " parameters:" << targetP << std::endl;
     #endif
  }
#undef PARENT
#undef MODEL

// MSSM20atMGUT_mA --> MSSM25atMGUT_mA
#define MODEL MSSM20atMGUT_mA
#define PARENT MSSM25atMGUT_mA
  void MODEL_NAMESPACE::CAT_3(MODEL,_to_,PARENT) (const ModelParameters &myP, ModelParameters &targetP)
  {
     logger()<<"Running interpret_as_parent calculations for " STRINGIFY(MODEL) " --> " STRINGIFY(PARENT) "."<<LogTags::info<<EOM;

     MSSM20atX_to_MSSM25atX(myP, targetP);

     // Done
     #ifdef MSSMatMGUT_mA_DBUG
       std::cout << STRINGIFY(MODEL) " parameters:" << myP << std::endl;
       std::cout << STRINGIFY(PARENT) " parameters:" << targetP << std::endl;
     #endif
  }
#undef PARENT

// MSSM20atMGUT_mA --> MSSM20atMGUT
#define FRIEND MSSM20atMGUT
  void MODEL_NAMESPACE::CAT_3(MODEL,_to_,FRIEND) (const ModelParameters &myP, ModelParameters &targetP)
  {
     logger()<<"Running interpret_as_X calculations for " STRINGIFY(MODEL) " --> " STRINGIFY(FRIEND) "."<<LogTags::info<<EOM;

     USE_MODEL_PIPE(FRIEND) // Need the pipe for the TARGET model
     const SubSpectrum& HE = Dep::unimproved_MSSM_spectrum->get_HE();
     MSSM_mA_to_MSSM_mhud(myP, targetP, HE);

     // Done
     #ifdef MSSMatMGUT_mA_DBUG
       std::cout << STRINGIFY(MODEL) " parameters:" << myP << std::endl;
       std::cout << STRINGIFY(FRIEND) " parameters:" << targetP << std::endl;
     #endif
  }
#undef FRIEND
#undef MODEL
```


-------------------------------

Updated on 2024-05-31 at 15:12:06 +0000
