---
title: 'file models/MSSM7atQ.cpp'

description: "[No description available]"

---

# models/MSSM7atQ.cpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/mssm7atq_8cpp/#define-model)**  |

## Detailed Description


**Author**: Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 

**Date**: 2015 Sep

MSSM7atQ translation function definitions.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define MODEL

```
#define MODEL MSSM7atQ
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  MSSM7atQ translation function definitions.
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
#include "gambit/Models/models/MSSM7atQ.hpp"
#include "gambit/Logs/logger.hpp"
#include "gambit/Utils/numerical_constants.hpp"
#include "gambit/Elements/sminputs.hpp"

// Activate debug output
//#define MSSM7atQ_DBUG

#define MODEL MSSM7atQ

  void MODEL_NAMESPACE::MSSM7atQ_to_MSSM9atQ (const ModelParameters &myP, ModelParameters &targetP)
  {
     USE_MODEL_PIPE(MSSM9atQ)

     logger()<<"Running interpret_as_parent calculations for " STRINGIFY(MODEL) " --> MSSM9atQ."<<LogTags::info<<EOM;

     // Send all parameter values upstream to matching parameters in parent.
     // Ignore that some parameters don't exist in the parent, as these are set below.
     targetP.setValues(myP,false);

     // Gaugino masses
     double mz = Dep::SMINPUTS->mZ;
     double am1 = Dep::SMINPUTS->alphainv;
     /// At tree level
     /// 0.25* ( sin(2\theta_W) )^2 = pi / (root2*mz*mz*am1*Dep::SMINPUTS->GF)
     /// solve quadratic eqn for (sin \theta_W)^2 = sin2thetaW_tree
     double sin2thetaW_tree = 0.5 - sqrt(0.25 - pi / (root2*mz*mz*am1*Dep::SMINPUTS->GF));
     targetP.setValue("M1", myP["M2"] * 5.0/3.0 * sin2thetaW_tree / (1.0-sin2thetaW_tree));
     targetP.setValue("M3", myP["M2"] * Dep::SMINPUTS->alphaS * am1 * sin2thetaW_tree);

     // Done
     #ifdef MSSM7atQ_DBUG
       std::cout << STRINGIFY(MODEL) " parameters:" << myP << std::endl;
       std::cout << "MSSM9atQ parameters:" << targetP << std::endl;
     #endif
  }

#undef MODEL
```


-------------------------------

Updated on 2022-09-07 at 14:07:48 +0000