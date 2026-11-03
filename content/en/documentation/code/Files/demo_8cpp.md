---
title: "file models/demo.cpp"

description: "[No description available]"

---

# file models/demo.cpp

[No description available]

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/demo_8cpp/#define-model)**  |




## Macros Documentation

### define MODEL

```
#define MODEL NormalDist
```


GAMBIT: Global and Modular BSM Inference Tool 

------------------

Model consistency function for NormalDist



------------------


# Authors

(add name and date if you modify)

Patrick Stoecker ([stoecker@physik.rwth-aachen.de](mailto:stoecker@physik.rwth-aachen.de)) 

2026 Oct



------------------


## Source code

```
///  GAMBIT: Global and Modular BSM Inference Tool
///  *********************************************
///
///  Model consistency function for NormalDist
///
///  *********************************************
///
///  Authors
///  =======
///
///  (add name and date if you modify)
///
///  \author Patrick Stoecker
///          (stoecker@physik.rwth-aachen.de)
///  \date 2026 Oct
///
///  *********************************************


#include "gambit/Models/model_macros.hpp"
#include "gambit/Models/model_helpers.hpp"
#include "gambit/Logs/logger.hpp"

#include "gambit/Models/models/demo.hpp"

#define MODEL NormalDist
  bool MODEL_NAMESPACE::NormalDist_ensure_positive_sigma (const ModelParameters& modelparams)
  {
    logger() << "Running model_consistency_check for NormalDist ..." << EOM;

    return modelparams["sigma"] > 0.0;
  }
#undef MODEL
```


-------------------------------

Updated on 2026-11-03 at 14:50:46 +0000
