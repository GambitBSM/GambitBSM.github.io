---
title: "file models/mSUGRA.cpp"

description: "[No description available]"

---

# file models/mSUGRA.cpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/msugra_8cpp/#define-model)**  |

## Detailed Description


**Author**: Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 

**Date**: 2015 Sep

mSUGRA model definition. Basically just an alias for the CMSSM. See mSUGRAb for a more constrained definition that some people prefer.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define MODEL

```
#define MODEL mSUGRA
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  mSUGRA model definition.  Basically just an
///  alias for the CMSSM.  See mSUGRAb for a more
///  constrained definition that some people prefer.
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
#include "gambit/Models/models/mSUGRA.hpp"
#include "gambit/Logs/logger.hpp"


#define MODEL mSUGRA
  void MODEL_NAMESPACE::mSUGRA_to_CMSSM (const ModelParameters &myP, ModelParameters &targetP)
  {
     // Send all parameter values upstream to matching parameters in parent.  That's all folks.
     targetP.setValues(myP);
  }

#undef MODEL
```


-------------------------------

Updated on 2022-09-08 at 00:43:04 +0000
