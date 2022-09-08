---
title: "file models/MSSM15atQ_mA.cpp"

description: "[No description available]"

---

# file models/MSSM15atQ_mA.cpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/mssm15atq__ma_8cpp/#define-mssm15atq-ma-cpp-model)**  |

## Detailed Description


**Author**: Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 

**Date**: 2017 Aug

MSSM15atQ_mA translation function definitions.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define MODEL

```
#define MODEL MSSM15atQ_mA
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  MSSM15atQ_mA translation function definitions.
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

#include "gambit/Models/model_macros.hpp"
#include "gambit/Models/model_helpers.hpp"
#include "gambit/Logs/logger.hpp"

#include "gambit/Models/models/MSSM15atQ_mA.hpp"


// Activate debug output
//#define MSSM15atQ_mA_DBUG

#define MODEL MSSM15atQ_mA

  void MODEL_NAMESPACE::MSSM15atQ_mA_to_MSSM16atQ_mA (const ModelParameters &myP, ModelParameters &targetP)
  {
     logger()<<"Running interpret_as_parent calculations for " STRINGIFY(MODEL) " --> MSSM16atQ_mA."<<LogTags::info<<EOM;

     // Send all parameter values upstream to matching parameters in parent.
     // Ignore that some parameters don't exist in the parent, as these are set below.
     targetP.setValues(myP,false);

     // 3rd gen trilinear couplings.
     targetP.setValue("Ae_3", myP["A0"]);
     targetP.setValue("Ad_3", myP["A0"]);
     targetP.setValue("Au_3", myP["Au_3"]);

     // Done
     #ifdef MSSM15atQ_mA_DBUG
       std::cout << STRINGIFY(MODEL) " parameters:" << myP << std::endl;
       std::cout << "MSSM16atQ_mA parameters:" << targetP << std::endl;
     #endif
  }

#undef MODEL
```


-------------------------------

Updated on 2022-09-08 at 01:48:58 +0000
