---
title: "file models/Models/src/models/DiracSingletDM.cpp"

description: "[No description available]"

---

# file models/Models/src/models/DiracSingletDM.cpp

[No description available]

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/models_2src_2models_2diracsingletdm_8cpp/#define-model)**  |
|  | **[PARENT](/documentation/code/files/models_2src_2models_2diracsingletdm_8cpp/#define-parent)**  |




## Macros Documentation

### define MODEL

```
#define MODEL DiracSingletDM_Z2_sps
```


### define PARENT

```
#define PARENT DiracSingletDM_Z2
```


## Source code

```
///  GAMBIT: Global and Modular BSM Inference Tool
///  *********************************************
///
///  DiracSingletDM_Z2 model source file.
///
///  *********************************************
///
///  Authors
///  =======
///
///  (add name and date if you modify)
///
///  \author Ankit Beniwal
///          (ankit.beniwal@adelaide.edu.com)
///  \date 2016 Aug, 2017 Jun
///
///  \author Sebastian Wild
///          (sebastian.wild@desy.de)
///  \date 2018, Feb
///
///  \author Sanjay Bloor
///          (sanjay.bloor12@imperial.ac.uk)
///  \date 2018 Aug
///        2020 May
///
///  *********************************************

#include <string>
#include <vector>

#include "gambit/Models/model_macros.hpp"
#include "gambit/Models/model_helpers.hpp"
#include "gambit/Logs/logger.hpp"
#include "gambit/Utils/util_functions.hpp"

#include "gambit/Models/models/DiracSingletDM_Z2.hpp"

using namespace Gambit::Utils;

// Translation function
#define MODEL DiracSingletDM_Z2_sps
#define PARENT DiracSingletDM_Z2
  void MODEL_NAMESPACE::DiracSingletDM_Z2_sps_to_DiracSingletDM_Z2 (const ModelParameters &myparams, ModelParameters &parentparams)
  {
    double mF = myparams["mF"];
    double lF_s = myparams["lF_s"];
    double lF_ps = myparams["lF_ps"];
    double lF = sqrt(lF_s*lF_s + lF_ps*lF_ps);
    double xi = std::acos(lF_s/lF);
    parentparams.setValue("mF", mF);
    parentparams.setValue("lF", lF);
    parentparams.setValue("xi", xi);
  }
#undef PARENT
#undef MODEL
```


-------------------------------

Updated on 2025-02-12 at 16:10:34 +0000
