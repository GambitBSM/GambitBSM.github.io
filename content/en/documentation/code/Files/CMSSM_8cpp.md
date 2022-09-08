---
title: "file models/CMSSM.cpp"

description: "[No description available]"

---

# file models/CMSSM.cpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/cmssm_8cpp/#define-model)**  |

## Detailed Description


**Author**: 

  * Ben Farmer 
  * Pat Scott 

 ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 


**Date**: 

  * 2015 Jan
  * 2015 Sep


CMSSM model definitions.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define MODEL

```
#define MODEL CMSSM
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  CMSSM model definitions. 
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///   
///  \author Ben Farmer 
///  \date 2015 Jan
///   
///  \author Pat Scott  
///          (p.scott@imperial.ac.uk)
///  \date 2015 Sep
///
///  *********************************************


#include "gambit/Models/model_macros.hpp"
#include "gambit/Models/model_helpers.hpp"
#include "gambit/Logs/logger.hpp"

#include "gambit/Models/models/CMSSM.hpp"


#define MODEL CMSSM 
  void MODEL_NAMESPACE::CMSSM_to_NUHM1 (const ModelParameters &myP, ModelParameters &targetP)
  {

     logger()<<"Running interpret_as_parent calculations for CMSSM --> NUHM1."<<LogTags::info<<EOM;
     
     // Send all parameter values upstream to matching parameters in parent.
     targetP.setValues(myP);

     // MH2
     targetP.setValue("mH", myP["M0"]);

  }

#undef MODEL
```


-------------------------------

Updated on 2022-09-08 at 02:27:29 +0000
