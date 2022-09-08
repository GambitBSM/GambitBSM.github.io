---
title: "file models/StandardModel_mNudiff.cpp"

description: "[No description available]"

---

# file models/StandardModel_mNudiff.cpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/standardmodel__mnudiff_8cpp/#define-standardmodel-mnudiff-cpp-model)**  |

## Detailed Description


**Author**: 

  * Tomas Gonzao 

 ([t.e.gonzalo@fys.uio.no](mailto:t.e.gonzalo@fys.uio.no)) 
  * Patrick Stoecker ([stoecker@physik.rwth-aachen.de](mailto:stoecker@physik.rwth-aachen.de)) 


**Date**: 

  * 2017 December
  * 2020 February


RH Neutrino Model with differential masses



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define MODEL

```
#define MODEL StandardModel_mNudiff
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
///  \author Patrick Stoecker
///          (stoecker@physik.rwth-aachen.de)
///  \date 2020 February
///
///  *********************************************

#include "gambit/Models/model_macros.hpp"
#include "gambit/Models/model_helpers.hpp"
#include "gambit/Logs/logger.hpp"

#include "gambit/Models/models/StandardModel_mNudiff.hpp"

#define MODEL StandardModel_mNudiff
  void MODEL_NAMESPACE::StandardModel_mNudiff_to_StandardModel_SLHA2 (const ModelParameters &myP, ModelParameters &targetP)
  {

     logger()<<"Running interpret_as_parent calculations for StandardModel_mNudiff --> StandardModel_SLHA2."<<LogTags::info<<EOM;
     
     // Send all parameter values upstream to matching parameters in parent.
     // Ignore that some parameters don't exist in the parent, as these are set below.
     targetP.setValues(myP,false);

     if (myP["dmNu3l"] > 0.)  // normal hierarchy, l = 1
     {
       targetP.setValue("mNu1", myP["mNu_light"]*1e-9);
       targetP.setValue("mNu2",
           pow(myP["mNu_light"]*myP["mNu_light"]+myP["dmNu21"], 0.5)*1e-9);
       targetP.setValue("mNu3",
           pow(myP["mNu_light"]*myP["mNu_light"]+myP["dmNu3l"], 0.5)*1e-9);
     }
     else // inverted hierarchy, l = 2
     {
       targetP.setValue("mNu3", myP["mNu_light"]*1e-9);
       targetP.setValue("mNu2",
           pow(myP["mNu_light"]*myP["mNu_light"]-myP["dmNu3l"], 0.5)*1e-9);
       targetP.setValue("mNu1",
           pow(myP["mNu_light"]*myP["mNu_light"]-myP["dmNu3l"]-myP["dmNu21"], 0.5)*1e-9);
     }

     // When "mNu_light", "dmNu21", and "dmNu3l" are badly chosen, the neutrino mases in
     // "StandardModel_SLHA2" cannot be set properly.
     // Invalidate this point, since it is clearly non-physical.
     if (std::isnan(targetP["mNu1"]) || std::isnan(targetP["mNu2"]) || std::isnan(targetP["mNu3"]))
     {
       std::string ErrMssg = "There is a conflicting parameter choice of ";
       ErrMssg += "\"mNu_light\", \"dmNu21\", and \"dmNu3l\"   in \"StandardModel_mNudiff\" ";
       ErrMssg +=  "such that the neutrino masses in \"StandardModel_SLHA2\" cannot be set properly.";
       invalid_point().raise(ErrMssg.c_str());
     }
  }

#undef MODEL
```


-------------------------------

Updated on 2022-09-08 at 02:00:51 +0000
