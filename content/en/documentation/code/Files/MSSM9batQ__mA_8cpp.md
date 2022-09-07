---
title: "file models/MSSM9batQ_mA.cpp"

description: "[No description available]"

---

# file models/MSSM9batQ_mA.cpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/mssm9batq__ma_8cpp/#define-model)**  |

## Detailed Description


**Author**: Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 

**Date**: 2017 Aug

MSSM9batQ_mA translation function definitions.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define MODEL

```
#define MODEL MSSM9batQ_mA
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  MSSM9batQ_mA translation function definitions.
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

#include "gambit/Models/models/MSSM9batQ_mA.hpp"


// Activate debug output
//#define MSSM9batQ_mA_DBUG

#define MODEL MSSM9batQ_mA

  void MODEL_NAMESPACE::MSSM9batQ_mA_to_MSSM15atQ_mA (const ModelParameters &myP, ModelParameters &targetP)
  {
     logger()<<"Running interpret_as_parent calculations for " STRINGIFY(MODEL) " --> MSSM15atQ_mA."<<LogTags::info<<EOM;

     // Send all parameter values upstream to matching parameters in parent.
     // Ignore that some parameters don't exist in the parent, as these are set below.
     targetP.setValues(myP,false);

     // most Sfermion soft masses squared
     set_many_to_one(targetP, initVector<str>("md2_3", "me2_3", "ml2_12", "ml2_3", "mq2_12"), myP["msf2"]);
     // stop soft masses squared
     targetP.setValue("mu2_3", myP["mq2_3"]);
     // set all trilinear coupling except Au_3 to zero
     targetP.setValue("A0", 0.0);

     // Done
     #ifdef MSSM15atQ_mA_DBUG
       std::cout << STRINGIFY(MODEL) " parameters:" << myP << std::endl;
       std::cout << "MSSM15atQ_mA parameters:" << targetP << std::endl;
     #endif
  }

#undef MODEL
```


-------------------------------

Updated on 2022-09-07 at 23:22:09 +0000
