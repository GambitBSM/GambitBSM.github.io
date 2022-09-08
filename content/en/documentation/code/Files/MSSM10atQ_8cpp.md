---
title: "file models/MSSM10atQ.cpp"

description: "[No description available]"

---

# file models/MSSM10atQ.cpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/mssm10atq_8cpp/#define-model)**  |

## Detailed Description


**Author**: Pat Scott 

 ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 

**Date**: 2015 Sep

MSSM10atQ translation function definitions.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define MODEL

```
#define MODEL MSSM10atQ
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  MSSM10atQ translation function definitions. 
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

#include "gambit/Models/models/MSSM10atQ.hpp"


// Activate debug output
//#define MSSM10atQ_DBUG

#define MODEL MSSM10atQ

  void MODEL_NAMESPACE::MSSM10atQ_to_MSSM11atQ (const ModelParameters &myP, ModelParameters &targetP)
  {
     logger()<<"Running interpret_as_parent calculations for " STRINGIFY(MODEL) " --> MSSM11atQ."<<LogTags::info<<EOM;

     // Send all parameter values upstream to matching parameters in parent.
     targetP.setValues(myP);
     
     // Charged slepton trilinear coupling
     targetP.setValue("Ae_3", 0.0);

     // Done
     #ifdef MSSM11atQ_DBUG
       std::cout << STRINGIFY(MODEL) " parameters:" << myP << std::endl;
       std::cout << "MSSM16atQ parameters:" << targetP << std::endl;
     #endif
  }
  
#undef MODEL
```


-------------------------------

Updated on 2022-09-08 at 02:27:29 +0000
