---
title: "file models/SUSY.cpp"

description: "[No description available]"

---

# file models/SUSY.cpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::ColliderBit](/documentation/code/namespaces/namespacegambit_1_1colliderbit/)**  |

## Detailed Description


**Author**: 

  * Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 
  * Tomas Gonzalo ([tomas.gonzalo@monash.edu](mailto:tomas.gonzalo@monash.edu)) 
  * Anders Kvellestad ([anders.kvellestad@fys.uio.no](mailto:anders.kvellestad@fys.uio.no)) 


**Date**: 

  * 2019 Jan
  * 2019 Oct
  * 2019


SUSY-specific sources for ColliderBit.



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  SUSY-specific sources for ColliderBit.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Pat Scott
///          (p.scott@imperial.ac.uk)
///  \date 2019 Jan
///
///  \author Tomas Gonzalo
///          (tomas.gonzalo@monash.edu)
///  \date 2019 Oct
///
///  \author Anders Kvellestad
///          (anders.kvellestad@fys.uio.no)
///  \date 2019
///
///  *********************************************

#include "gambit/ColliderBit/getPy8Collider.hpp"
#include "gambit/ColliderBit/generateEventPy8Collider.hpp"

namespace Gambit
{
  namespace ColliderBit
  {

    // Get spectrum and decays for Pythia
    GET_SPECTRUM_AND_DECAYS_FOR_PYTHIA_SUSY(getSpectrumAndDecaysForPythia, MSSM_spectrum)

    // Get Monte Carlo event generator
    GET_SPECIFIC_PYTHIA(getPythia, Pythia_default, /* blank MODEL_EXTENSION argument */ )
    GET_PYTHIA_AS_BASE_COLLIDER(getPythiaAsBase)

    // Run event generator
    GET_PYTHIA_EVENT(generateEventPythia, Pythia_default::Pythia8::Event)

  }
}
```


-------------------------------

Updated on 2025-02-12 at 16:10:35 +0000
