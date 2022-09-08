---
title: "file models/MSSM11atQ.cpp"

description: "[No description available]"

---

# file models/MSSM11atQ.cpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/mssm11atq_8cpp/#define-mssm11atq-cpp-model)**  |

## Detailed Description


**Author**: Pat Scott 

 ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 

**Date**: 2015 Sep

MSSM11atQ translation function definitions.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define MODEL

```
#define MODEL MSSM11atQ
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  MSSM11atQ translation function definitions. 
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///   
///  \author Pat Scott  
///          (p.scott@imperial.ac.uk)
///  \date 2015 Sep
///
///  *********************************************

#include "gambit/Models/model_macros.hpp"
#include "gambit/Models/model_helpers.hpp"
#include "gambit/Logs/logger.hpp"

#include "gambit/Models/models/MSSM11atQ.hpp"


// Activate debug output
//#define MSSM11atQ_DBUG

#define MODEL MSSM11atQ

  void MODEL_NAMESPACE::MSSM11atQ_to_MSSM16atQ (const ModelParameters &myP, ModelParameters &targetP)
  {
     logger()<<"Running interpret_as_parent calculations for " STRINGIFY(MODEL) " --> MSSM16atQ."<<LogTags::info<<EOM;

     // Send all parameter values upstream to matching parameters in parent.
     // Ignore that some parameters don't exist in the parent, as these are set below.
     targetP.setValues(myP,false);

     // Sfermion mass matrix entries.
     targetP.setValue("mq2_12", myP["mq2"]);
     targetP.setValue("mq2_3",  myP["mq2"]);
     targetP.setValue("mu2_3",  myP["mq2"]);
     targetP.setValue("md2_3",  myP["mq2"]);
     targetP.setValue("ml2_12", myP["ml2"]);
     targetP.setValue("ml2_3",  myP["ml2"]);
     targetP.setValue("me2_3",  myP["ml2"]);
     
     // Done
     #ifdef MSSM11atQ_DBUG
       std::cout << STRINGIFY(MODEL) " parameters:" << myP << std::endl;
       std::cout << "MSSM16atQ parameters:" << targetP << std::endl;
     #endif
  }
  
#undef MODEL
```


-------------------------------

Updated on 2022-09-08 at 02:00:51 +0000
