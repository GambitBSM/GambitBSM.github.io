---
title: "file models/RightHandedNeutrinos_diff.cpp"

description: "[No description available]"

---

# file models/RightHandedNeutrinos_diff.cpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/righthandedneutrinos__diff_8cpp/#define-model)**  |

## Detailed Description


**Author**: Tomas Gonzao 

 ([t.e.gonzalo@fys.uio.no](mailto:t.e.gonzalo@fys.uio.no)) 

**Date**: 2017 December

RH Neutrino Model with differential masses



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define MODEL

```
#define MODEL RightHandedNeutrinos_diff
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  RH Neutrino Model with differential masses
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///   
///  \author Tomas Gonzao  
///          (t.e.gonzalo@fys.uio.no)
///  \date 2017 December
///
///  *********************************************

#include "gambit/Models/model_macros.hpp"
#include "gambit/Models/model_helpers.hpp"
#include "gambit/Logs/logger.hpp"

#include "gambit/Models/models/RightHandedNeutrinos_diff.hpp"


#define MODEL RightHandedNeutrinos_diff 
  void MODEL_NAMESPACE::RightHandedNeutrinos_diff_to_RightHandedNeutrinos (const ModelParameters &myP, ModelParameters &targetP)
  {

     logger()<<"Running interpret_as_parent calculations for RightHandedNeutrinos_diff --> RightHandedNeutrinos."<<LogTags::info<<EOM;
     
     // Send all parameter values upstream to matching parameters in parent.
     // Ignore that some parameters don't exist in the parent, as these are set below.
     targetP.setValues(myP,false);

     // M2
     targetP.setValue("M_2", myP["M_1"]+myP["delta_M21"]);
  }

#undef MODEL
```


-------------------------------

Updated on 2022-09-08 at 02:23:03 +0000
