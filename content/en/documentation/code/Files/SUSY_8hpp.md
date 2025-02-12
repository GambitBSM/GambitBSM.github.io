---
title: "file models/SUSY.hpp"

description: "[No description available]"

---

# file models/SUSY.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODULE](/documentation/code/files/susy_8hpp/#define-module)**  |
|  | **[CAPABILITY](/documentation/code/files/susy_8hpp/#define-capability)**  |
|  | **[FUNCTION](/documentation/code/files/susy_8hpp/#define-function)**  |
|  | **[CAPABILITY](/documentation/code/files/susy_8hpp/#define-capability)**  |
|  | **[FUNCTION](/documentation/code/files/susy_8hpp/#define-function)**  |
|  | **[FUNCTION](/documentation/code/files/susy_8hpp/#define-function)**  |
|  | **[CAPABILITY](/documentation/code/files/susy_8hpp/#define-capability)**  |
|  | **[FUNCTION](/documentation/code/files/susy_8hpp/#define-function)**  |
|  | **[FUNCTION](/documentation/code/files/susy_8hpp/#define-function)**  |
|  | **[FUNCTION](/documentation/code/files/susy_8hpp/#define-function)**  |

## Detailed Description


**Author**: 

  * Abram Krislock ([a.m.b.krislock@fys.uio.no](mailto:a.m.b.krislock@fys.uio.no))
  * Aldo Saavedra
  * Christopher Rogan ([christophersrogan@gmail.com](mailto:christophersrogan@gmail.com)) 
  * Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 
  * Andy Buckley ([andy.buckley@cern.ch](mailto:andy.buckley@cern.ch)) 
  * Tomas Gonzalo ([tomas.gonzalo@monash.edu](mailto:tomas.gonzalo@monash.edu)) 
  * Anders Kvellestad ([anders.kvellestad@fys.uio.no](mailto:anders.kvellestad@fys.uio.no)) 


**Date**: 

  * 2015 Apr
  * 2015 Jul 
  * 2018 Jan
  * 2017 Jun
  * 2019 Oct
  * 2019 
  * 2021 Jul


Rollcall header for SUSY models in ColliderBit.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define MODULE

```
#define MODULE ColliderBit
```


### define CAPABILITY

```
#define CAPABILITY SpectrumAndDecaysForPythia
```


### define FUNCTION

```
#define FUNCTION getSpectrumAndDecaysForPythia
```


### define CAPABILITY

```
#define CAPABILITY SpectrumAndDecaysForPythia
```


### define FUNCTION

```
#define FUNCTION getSpectrumAndDecaysForPythia
```


### define FUNCTION

```
#define FUNCTION getSpectrumAndDecaysForPythia
```


### define CAPABILITY

```
#define CAPABILITY SpectrumAndDecaysForPythia
```


### define FUNCTION

```
#define FUNCTION getSpectrumAndDecaysForPythia
```


### define FUNCTION

```
#define FUNCTION getSpectrumAndDecaysForPythia
```


### define FUNCTION

```
#define FUNCTION getSpectrumAndDecaysForPythia
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Rollcall header for SUSY models in
///  ColliderBit.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Abram Krislock
///          (a.m.b.krislock@fys.uio.no)
///
///  \author Aldo Saavedra
///
///  \author Christopher Rogan
///          (christophersrogan@gmail.com)
///  \date 2015 Apr
///
///  \author Pat Scott
///          (p.scott@imperial.ac.uk)
///  \date 2015 Jul
///  \date 2018 Jan
///
///  \author Andy Buckley
///          (andy.buckley@cern.ch)
///  \date 2017 Jun
///
///  \author Tomas Gonzalo
///          (tomas.gonzalo@monash.edu)
///  \date 2019 Oct
///
///  \author Anders Kvellestad
///          (anders.kvellestad@fys.uio.no)
///  \date 2019
///  \date 2021 Jul
///
///  *********************************************

#pragma once

#include "gambit/ColliderBit/models/SUSY_extras.hpp"

#define MODULE ColliderBit


  // Construct an SLHAea object with spectrum and decays for Pythia
  #define CAPABILITY SpectrumAndDecaysForPythia

    #define FUNCTION getSpectrumAndDecaysForPythia
    START_FUNCTION(SLHAstruct)
    DEPENDENCY(decay_rates, DecayTable)
    DEPENDENCY(MSSM_spectrum, Spectrum)
    DEPENDENCY(SLHA_pseudonyms, mass_es_pseudonyms)
    ALLOW_MODELS(MSSM63atQ, MSSM63atQ_mG, MSSM63atQ_mA, MSSM63atQ_mA_mG, MSSM63atMGUT, MSSM63atMGUT_mG, MSSM63atMGUT_mA, MSSM63atMGUT_mA_mG)
    #undef FUNCTION

  #undef CAPABILITY


  // Get Monte Carlo event generator
  #define CAPABILITY HardScatteringSim

    #define FUNCTION getPythia
    START_FUNCTION(Py8Collider_defaultversion)
    NEEDS_MANAGER(RunMC, MCLoopInfo)
    NEEDS_CLASSES_FROM(Pythia, default)
    ALLOW_MODELS(MSSM63atQ, MSSM63atQ_mG, MSSM63atQ_mA, MSSM63atQ_mA_mG, MSSM63atMGUT, MSSM63atMGUT_mG, MSSM63atMGUT_mA, MSSM63atMGUT_mA_mG)
    DEPENDENCY(SpectrumAndDecaysForPythia, SLHAstruct)
    #undef FUNCTION

    #define FUNCTION getPythiaAsBase
    START_FUNCTION(const BaseCollider*)
    NEEDS_MANAGER(RunMC, MCLoopInfo)
    NEEDS_CLASSES_FROM(Pythia, default)
    DEPENDENCY(HardScatteringSim, Py8Collider_defaultversion)
    ALLOW_MODELS(MSSM63atQ, MSSM63atQ_mG, MSSM63atQ_mA, MSSM63atQ_mA_mG, MSSM63atMGUT, MSSM63atMGUT_mG, MSSM63atMGUT_mA, MSSM63atMGUT_mA_mG)
    ALLOW_MODELS(ColliderBit_SLHA_file_model, ColliderBit_SLHA_scan_model)
    #undef FUNCTION

  #undef CAPABILITY


  // Run event generator
  #define CAPABILITY HardScatteringEvent
    #define FUNCTION generateEventPythia
    START_FUNCTION(Pythia_default::Pythia8::Event)
    NEEDS_MANAGER(RunMC, MCLoopInfo)
    NEEDS_CLASSES_FROM(Pythia, default)
    DEPENDENCY(HardScatteringSim, Py8Collider_defaultversion)
    DEPENDENCY(EventWeighterFunction, EventWeighterFunctionType)
    ALLOW_MODELS(MSSM63atQ, MSSM63atQ_mG, MSSM63atQ_mA, MSSM63atQ_mA_mG, MSSM63atMGUT, MSSM63atMGUT_mG, MSSM63atMGUT_mA, MSSM63atMGUT_mA_mG)
    ALLOW_MODELS(ColliderBit_SLHA_file_model, ColliderBit_SLHA_scan_model)
    #undef FUNCTION

    #define FUNCTION generateEventPythia_HEPUtils
    START_FUNCTION(HEPUtils::Event)
    NEEDS_MANAGER(RunMC, MCLoopInfo)
    NEEDS_CLASSES_FROM(Pythia, default)
    DEPENDENCY(HardScatteringSim, Py8Collider_defaultversion)
    DEPENDENCY(HardScatteringEvent, Pythia_default::Pythia8::Event)
    DEPENDENCY(EventWeighterFunction, EventWeighterFunctionType)
    #undef FUNCTION

    #ifndef EXCLUDE_HEPMC
      #define FUNCTION generateEventPythia_HepMC
      START_FUNCTION(HepMC3::GenEvent)
      NEEDS_MANAGER(RunMC, MCLoopInfo)
      NEEDS_CLASSES_FROM(Pythia, default)
      DEPENDENCY(HardScatteringSim, Py8Collider_defaultversion)
      DEPENDENCY(HardScatteringEvent, Pythia_default::Pythia8::Event)
      #undef FUNCTION
    #endif

  #undef CAPABILITY

#undef MODULE
```


-------------------------------

Updated on 2025-02-12 at 16:10:35 +0000
