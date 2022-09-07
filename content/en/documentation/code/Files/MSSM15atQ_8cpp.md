---
title: 'file models/MSSM15atQ.cpp'

description: "[No description available]"

---

# models/MSSM15atQ.cpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/mssm15atq_8cpp/#define-model)**  |

## Detailed Description


**Author**: Pat Scott 

 ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 

**Date**: 2015 Sep

MSSM15atQ translation function definitions.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define MODEL

```
#define MODEL MSSM15atQ
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  MSSM15atQ translation function definitions. 
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

#include "gambit/Models/models/MSSM15atQ.hpp"


// Activate debug output
//#define MSSM15atQ_DBUG

#define MODEL MSSM15atQ

  void MODEL_NAMESPACE::MSSM15atQ_to_MSSM16atQ (const ModelParameters &myP, ModelParameters &targetP)
  {
     logger()<<"Running interpret_as_parent calculations for " STRINGIFY(MODEL) " --> MSSM16atQ."<<LogTags::info<<EOM;

     // Send all parameter values upstream to matching parameters in parent.
     // Ignore that some parameters don't exist in the parent, as these are set below.
     targetP.setValues(myP,false);

     // 3rd gen trilinear couplings.
     targetP.setValue("Ae_3", myP["A0"]);
     targetP.setValue("Ad_3", myP["A0"]);
     targetP.setValue("Au_3", myP["Au_3"]);
     
     // Done
     #ifdef MSSM15atQ_DBUG
       std::cout << STRINGIFY(MODEL) " parameters:" << myP << std::endl;
       std::cout << "MSSM16atQ parameters:" << targetP << std::endl;
     #endif
  }
  
#undef MODEL
```


-------------------------------

Updated on 2022-09-07 at 14:07:48 +0000