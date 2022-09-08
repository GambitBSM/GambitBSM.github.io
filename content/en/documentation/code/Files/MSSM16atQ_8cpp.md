---
title: "file models/MSSM16atQ.cpp"

description: "[No description available]"

---

# file models/MSSM16atQ.cpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/mssm16atq_8cpp/#define-mssm16atq-cpp-model)**  |

## Detailed Description


**Author**: 

  * Pat Scott 

 ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 
  * Ben Farmer ([benjamin.farmer@fysik.su.se](mailto:benjamin.farmer@fysik.su.se)) 


**Date**: 

  * 2015 Sep
  * 2017 Oct


MSSM16atX translation function definitions.

This file contains the interpret-as-parent function definitions for MSSM16atQ --> MSSM19atQ MSSM16atQ_mA --> MSSM19atQ_mA



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define MODEL

```
#define MODEL MSSM16atQ
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  MSSM16atX translation function definitions. 
///
///  This file contains the interpret-as-parent
///  function definitions for
///    MSSM16atQ     --> MSSM19atQ
///    MSSM16atQ_mA  --> MSSM19atQ_mA
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///   
///  \author Pat Scott  
///          (p.scott@imperial.ac.uk)
///  \date 2015 Sep
///
///  \author Ben Farmer
///          (benjamin.farmer@fysik.su.se)
///  \date 2017 Oct
///
///  *********************************************

#include "gambit/Models/model_macros.hpp"
#include "gambit/Models/model_helpers.hpp"
#include "gambit/Logs/logger.hpp"

#include "gambit/Models/models/MSSM16atQ.hpp"
#include "gambit/Models/models/MSSM16atQ.hpp"
#include "gambit/Models/models/MSSM16atQ.hpp"


// Activate debug output
//#define MSSM16atQ_DBUG

#define MODEL MSSM16atQ

  void MODEL_NAMESPACE::MSSM16atQ_to_MSSM19atQ (const ModelParameters &myP, ModelParameters &targetP)
  {
     logger()<<"Running interpret_as_parent calculations for " STRINGIFY(MODEL) " --> MSSM19atQ."<<LogTags::info<<EOM;

     // Send all parameter values upstream to matching parameters in parent.
     targetP.setValues(myP);

     // LH first and second gen down-type squark, up-type squark and charged slepton soft masses
     targetP.setValue("md2_12", myP["mq2_12"]);
     targetP.setValue("mu2_12", myP["mq2_12"]);
     targetP.setValue("me2_12", myP["ml2_12"]);
     
     // Done
     #ifdef MSSM16atQ_DBUG
       std::cout << STRINGIFY(MODEL) " parameters:" << myP << std::endl;
       std::cout << "MSSM19atQ parameters:" << targetP << std::endl;
     #endif
  }
  
#undef MODEL
```


-------------------------------

Updated on 2022-09-08 at 02:00:51 +0000
