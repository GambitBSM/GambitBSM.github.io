---
title: "file models/Models/src/models/DMEFT.cpp"

description: "[No description available]"

---

# file models/Models/src/models/DMEFT.cpp

[No description available]

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/models_2src_2models_2dmeft_8cpp/#define-model)**  |




## Macros Documentation

### define MODEL

```
#define MODEL DMEFT
```


GAMBIT: Global and Modular BSM Inference Tool 

------------------

Model translation functions for the DMEFT model



------------------


# Authors

(add name and date if you modify)

Patrick Stöcker ([stoecker@physik.rwth-aachen.de](mailto:stoecker@physik.rwth-aachen.de)) 

2021 Mar

Tomas Gonzalo ([gonzalo@physik.rwth-aachen.de](mailto:gonzalo@physik.rwth-aachen.de)) 

2021 Sep



------------------


## Source code

```
///  GAMBIT: Global and Modular BSM Inference Tool
///  *********************************************
///
///  Model translation functions for the DMEFT model
///
///  *********************************************
///
///  Authors
///  =======
///
///  (add name and date if you modify)
///
///  \author Patrick Stöcker
///          (stoecker@physik.rwth-aachen.de)
///  \date 2021 Mar
///
///  \author Tomas Gonzalo
///          (gonzalo@physik.rwth-aachen.de)
///  \date 2021 Sep
///
///  *********************************************


#include "gambit/Models/model_macros.hpp"
#include "gambit/Models/model_helpers.hpp"
#include "gambit/Logs/logger.hpp"

#include "gambit/Models/models/DMEFT.hpp"

#define MODEL DMEFT
  void MODEL_NAMESPACE::DMEFT_to_AnnihilatingDM_general (const ModelParameters& /*myparams*/, ModelParameters &friendparams)
  {
    USE_MODEL_PIPE(AnnihilatingDM_general) // get pipe for "interpret as friend" function
    logger()<<"Running interpret_as_friend calculations for DMEFT -> AnnihilatingDM_general ..."<<EOM;

    const double k = (*Dep::wimp_sc) ? 1. : 0.5;
    const double f = *Dep::RD_fraction;

    friendparams.setValue("mass", *Dep::mwimp);
    // In AnnihilatingDM_general the parameter "sigmav" is assumed to already include
    // (RD_fraction)^2 and the factor k
    friendparams.setValue("sigmav", k*f*f*(*Dep::sigmav));
  }
#undef MODEL
```


-------------------------------

Updated on 2022-09-08 at 03:42:01 +0000
