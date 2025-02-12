---
title: "file models/MSSMatMSUSY.cpp"

description: "[No description available]"

---

# file models/MSSMatMSUSY.cpp

[No description available]

## Functions

|                | Name           |
| -------------- | -------------- |
| | **[USE_MODEL_PIPE](/documentation/code/files/mssmatmsusy_8cpp/#function-use-model-pipe)**(PARENT ) const |
| | **[MSSMatX_to_MSSMatQ](/documentation/code/files/mssmatmsusy_8cpp/#function-mssmatx-to-mssmatq)**(myP , targetP , HE ) |
| | **[MSSM30atX_to_MSSM63atX](/documentation/code/files/mssmatmsusy_8cpp/#function-mssm30atx-to-mssm63atx)**(myP , targetP ) |
| | **[USE_MODEL_PIPE](/documentation/code/files/mssmatmsusy_8cpp/#function-use-model-pipe)**(FRIEND ) const |
| | **[MSSM25atX_to_MSSM30atX](/documentation/code/files/mssmatmsusy_8cpp/#function-mssm25atx-to-mssm30atx)**(myP , targetP ) |
| | **[MSSM20atX_to_MSSM25atX](/documentation/code/files/mssmatmsusy_8cpp/#function-mssm20atx-to-mssm25atx)**(myP , targetP ) |

## Attributes

|                | Name           |
| -------------- | -------------- |
| void ModelParameters & | **[targetP](/documentation/code/files/mssmatmsusy_8cpp/#variable-targetp)**  |

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/mssmatmsusy_8cpp/#define-model)**  |
|  | **[PARENT](/documentation/code/files/mssmatmsusy_8cpp/#define-parent)**  |
|  | **[MODEL](/documentation/code/files/mssmatmsusy_8cpp/#define-model)**  |
|  | **[PARENT](/documentation/code/files/mssmatmsusy_8cpp/#define-parent)**  |
|  | **[FRIEND](/documentation/code/files/mssmatmsusy_8cpp/#define-friend)**  |
|  | **[MODEL](/documentation/code/files/mssmatmsusy_8cpp/#define-model)**  |
|  | **[PARENT](/documentation/code/files/mssmatmsusy_8cpp/#define-parent)**  |
|  | **[MODEL](/documentation/code/files/mssmatmsusy_8cpp/#define-model)**  |
|  | **[PARENT](/documentation/code/files/mssmatmsusy_8cpp/#define-parent)**  |
|  | **[FRIEND](/documentation/code/files/mssmatmsusy_8cpp/#define-friend)**  |


## Functions Documentation

### function USE_MODEL_PIPE

```
USE_MODEL_PIPE(
    PARENT 
) const
```


### function MSSMatX_to_MSSMatQ

```
MSSMatX_to_MSSMatQ(
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



## Macros Documentation

### define MODEL

```
#define MODEL MSSM63atMSUSY
```


Translation function definitions for the MSSM models with boundary conditions at scale MSUSY

Contains the interpret-as-parent translation functions for:

MSSM63atMSUSY --> MSSM63atQ MSSM30atMSUSY --> MSSM63atMSUSY MSSM25atMSUSY --> MSSM30atMSUSY MSSM20atMSUSY --> MSSM25atMSUSY

As well as the interpret-as-friend translation functions for:

MSSM30atMSUSY --> MSSM30atQ MSSM20atMSUSY --> MSSM20atQ



------------------


# Authors

(add name and date if you modify)

Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 

2015 Sep

Ben Farmer ([benjamin.farmer@fysik.su.se](mailto:benjamin.farmer@fysik.su.se)) 

2015 Aug 

2017 Oct

Tomas Gonzalo ([tomas.gonzalo@kit.edu](mailto:tomas.gonzalo@kit.edu)) 

2022 Sept



------------------


### define PARENT

```
#define PARENT MSSM63atQ
```


### define MODEL

```
#define MODEL MSSM63atMSUSY
```


Translation function definitions for the MSSM models with boundary conditions at scale MSUSY

Contains the interpret-as-parent translation functions for:

MSSM63atMSUSY --> MSSM63atQ MSSM30atMSUSY --> MSSM63atMSUSY MSSM25atMSUSY --> MSSM30atMSUSY MSSM20atMSUSY --> MSSM25atMSUSY

As well as the interpret-as-friend translation functions for:

MSSM30atMSUSY --> MSSM30atQ MSSM20atMSUSY --> MSSM20atQ



------------------


# Authors

(add name and date if you modify)

Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 

2015 Sep

Ben Farmer ([benjamin.farmer@fysik.su.se](mailto:benjamin.farmer@fysik.su.se)) 

2015 Aug 

2017 Oct

Tomas Gonzalo ([tomas.gonzalo@kit.edu](mailto:tomas.gonzalo@kit.edu)) 

2022 Sept



------------------


### define PARENT

```
#define PARENT MSSM63atQ
```


### define FRIEND

```
#define FRIEND MSSM30atQ
```


### define MODEL

```
#define MODEL MSSM63atMSUSY
```


Translation function definitions for the MSSM models with boundary conditions at scale MSUSY

Contains the interpret-as-parent translation functions for:

MSSM63atMSUSY --> MSSM63atQ MSSM30atMSUSY --> MSSM63atMSUSY MSSM25atMSUSY --> MSSM30atMSUSY MSSM20atMSUSY --> MSSM25atMSUSY

As well as the interpret-as-friend translation functions for:

MSSM30atMSUSY --> MSSM30atQ MSSM20atMSUSY --> MSSM20atQ



------------------


# Authors

(add name and date if you modify)

Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 

2015 Sep

Ben Farmer ([benjamin.farmer@fysik.su.se](mailto:benjamin.farmer@fysik.su.se)) 

2015 Aug 

2017 Oct

Tomas Gonzalo ([tomas.gonzalo@kit.edu](mailto:tomas.gonzalo@kit.edu)) 

2022 Sept



------------------


### define PARENT

```
#define PARENT MSSM63atQ
```


### define MODEL

```
#define MODEL MSSM63atMSUSY
```


Translation function definitions for the MSSM models with boundary conditions at scale MSUSY

Contains the interpret-as-parent translation functions for:

MSSM63atMSUSY --> MSSM63atQ MSSM30atMSUSY --> MSSM63atMSUSY MSSM25atMSUSY --> MSSM30atMSUSY MSSM20atMSUSY --> MSSM25atMSUSY

As well as the interpret-as-friend translation functions for:

MSSM30atMSUSY --> MSSM30atQ MSSM20atMSUSY --> MSSM20atQ



------------------


# Authors

(add name and date if you modify)

Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 

2015 Sep

Ben Farmer ([benjamin.farmer@fysik.su.se](mailto:benjamin.farmer@fysik.su.se)) 

2015 Aug 

2017 Oct

Tomas Gonzalo ([tomas.gonzalo@kit.edu](mailto:tomas.gonzalo@kit.edu)) 

2022 Sept



------------------


### define PARENT

```
#define PARENT MSSM63atQ
```


### define FRIEND

```
#define FRIEND MSSM30atQ
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///
///  Translation function definitions for the
///  MSSM models with boundary conditions at
///  scale MSUSY
///
///  Contains the interpret-as-parent translation
///  functions for:
///
///  MSSM63atMSUSY  --> MSSM63atQ
///  MSSM30atMSUSY  --> MSSM63atMSUSY
///  MSSM25atMSUSY  --> MSSM30atMSUSY
///  MSSM20atMSUSY  --> MSSM25atMSUSY
///
///  As well as the interpret-as-friend translation
///  functions for:
///
///  MSSM30atMSUSY  --> MSSM30atQ
///  MSSM20atMSUSY  --> MSSM20atQ
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
///
///  \author Ben Farmer
///          (benjamin.farmer@fysik.su.se)
///  \date 2015 Aug
///  \date 2017 Oct
///
///  \author Tomas Gonzalo
///          (tomas.gonzalo@kit.edu)
///  \date 2022 Sept
///
///  *********************************************

#include "gambit/Models/model_macros.hpp"
#include "gambit/Models/model_helpers.hpp"
#include "gambit/Logs/logger.hpp"
#include "gambit/Elements/spectrum.hpp"

#include "gambit/Models/models/MSSMatMSUSY.hpp"
#include "gambit/Models/models/MSSMatQ.hpp"
#include "gambit/Models/models/MSSM_translation_helpers.hpp"

// Activate debug output
//#define MSSMatMSUSY_DBUG

// MSSM63atMSUSY --> MSSM63atQ
#define MODEL MSSM63atMSUSY
#define PARENT MSSM63atQ
  void MODEL_NAMESPACE::CAT_3(MODEL,_to_,PARENT) (const ModelParameters &myP, ModelParameters &targetP)
  {
     logger()<<"Running interpret_as_parent calculations for " STRINGIFY(MODEL) " --> " STRINGIFY(PARENT) "."<<LogTags::info<<EOM;

     USE_MODEL_PIPE(PARENT) // get pipe for "interpret as PARENT" function
     const SubSpectrum& HE = Dep::unimproved_MSSM_spectrum->get_HE();
     MSSMatX_to_MSSMatQ(myP, targetP, HE);

     // Done
     #ifdef MSSMatMSUSY_DBUG
       std::cout << STRINGIFY(MODEL) " parameters:" << myP << std::endl;
       std::cout << STRINGIFY(PARENT) " parameters:" << targetP << std::endl;
     #endif
  }
#undef PARENT
#undef MODEL

// MSSM30atMSUSY --> MSSM63atMSUSY
#define MODEL MSSM30atMSUSY
#define PARENT MSSM63atMSUSY
  void MODEL_NAMESPACE::CAT_3(MODEL,_to_,PARENT) (const ModelParameters &myP, ModelParameters &targetP)
  {
     logger()<<"Running interpret_as_parent calculations for " STRINGIFY(MODEL) " --> " STRINGIFY(PARENT) "."<<LogTags::info<<EOM;

     MSSM30atX_to_MSSM63atX(myP, targetP);

     // Done
     #ifdef MSSMatMSUSY_DBUG
       std::cout << STRINGIFY(MODEL) " parameters:" << myP << std::endl;
       std::cout << STRINGIFY(PARENT) " parameters:" << targetP << std::endl;
     #endif
  }
#undef PARENT

// MSSM30atMSUSY --> MSSM30atQ
#define FRIEND MSSM30atQ
  void MODEL_NAMESPACE::CAT_3(MODEL,_to_,FRIEND) (const ModelParameters &myP, ModelParameters &targetP)
  {
     logger()<<"Running interpret_as_X calculations for " STRINGIFY(MODEL) " --> " STRINGIFY(FRIEND) "."<<LogTags::info<<EOM;

     USE_MODEL_PIPE(FRIEND) // Need the pipe for the TARGET model
     const SubSpectrum& HE = Dep::unimproved_MSSM_spectrum->get_HE();
     MSSMatX_to_MSSMatQ(myP, targetP, HE);

     // Done
     #ifdef MSSMatMSUSY_DBUG
       std::cout << STRINGIFY(MODEL) " parameters:" << myP << std::endl;
       std::cout << STRINGIFY(FRIEND) " parameters:" << targetP << std::endl;
     #endif
  }
#undef FRIEND
#undef MODEL

// MSSM25atMSUSY --> MSSM30atMSUSY
#define MODEL MSSM25atMSUSY
#define PARENT MSSM30atMSUSY
  void MODEL_NAMESPACE::CAT_3(MODEL,_to_,PARENT) (const ModelParameters &myP, ModelParameters &targetP)
  {
     logger()<<"Running interpret_as_parent calculations for " STRINGIFY(MODEL) " --> " STRINGIFY(PARENT) "."<<LogTags::info<<EOM;

     MSSM25atX_to_MSSM30atX(myP, targetP);

     // Done
     #ifdef MSSMatMSUSY_DBUG
       std::cout << STRINGIFY(MODEL) " parameters:" << myP << std::endl;
       std::cout << STRINGIFY(PARENT) " parameters:" << targetP << std::endl;
     #endif
  }
#undef PARENT
#undef MODEL

// MSSM20atMSUSY --> MSSM25atMSUSY
#define MODEL MSSM20atMSUSY
#define PARENT MSSM25atMSUSY
  void MODEL_NAMESPACE::CAT_3(MODEL,_to_,PARENT) (const ModelParameters &myP, ModelParameters &targetP)
  {
     logger()<<"Running interpret_as_parent calculations for " STRINGIFY(MODEL) " --> " STRINGIFY(PARENT) "."<<LogTags::info<<EOM;

     MSSM20atX_to_MSSM25atX(myP, targetP);

     // Done
     #ifdef MSSMatMSUSY_DBUG
       std::cout << STRINGIFY(MODEL) " parameters:" << myP << std::endl;
       std::cout << STRINGIFY(PARENT) " parameters:" << targetP << std::endl;
     #endif
  }
#undef PARENT

// MSSM20atMSUSY --> MSSM20atQ
#define FRIEND MSSM20atQ
  void MODEL_NAMESPACE::CAT_3(MODEL,_to_,FRIEND) (const ModelParameters &myP, ModelParameters &targetP)
  {
     logger()<<"Running interpret_as_X calculations for " STRINGIFY(MODEL) " --> " STRINGIFY(FRIEND) "."<<LogTags::info<<EOM;

     USE_MODEL_PIPE(FRIEND) // Need the pipe for the TARGET model
     const SubSpectrum& HE = Dep::unimproved_MSSM_spectrum->get_HE();
     MSSMatX_to_MSSMatQ(myP, targetP, HE);

     // Done
     #ifdef MSSMatMSUSY_DBUG
       std::cout << STRINGIFY(MODEL) " parameters:" << myP << std::endl;
       std::cout << STRINGIFY(FRIEND) " parameters:" << targetP << std::endl;
     #endif
  }
#undef FRIEND
#undef MODEL
```


-------------------------------

Updated on 2025-02-12 at 15:36:41 +0000
