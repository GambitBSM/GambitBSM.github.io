---
title: "file models/SUSY_extras.hpp"

description: "[No description available]"

---

# file models/SUSY_extras.hpp

[No description available] [More...](#detailed-description)

## Functions

|                | Name           |
| -------------- | -------------- |
| | **[BACKEND_REQ](/documentation/code/files/susy__extras_8hpp/#function-backend-req)**(prospino_run , (libprospino) , map_str_dbl , (const PID_pair &, const Options &) ) |

## Attributes

|                | Name           |
| -------------- | -------------- |
| | **[libprospino](/documentation/code/files/susy__extras_8hpp/#variable-libprospino)**  |
| | **[void](/documentation/code/files/susy__extras_8hpp/#variable-void)**  |

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[CAPABILITY](/documentation/code/files/susy__extras_8hpp/#define-capability)** <br>A map between PID pairs and cross-sections.  |
|  | **[FUNCTION](/documentation/code/files/susy__extras_8hpp/#define-function)** <br>Get the PIDPairCrossSectionsMap using the Prospino backend.  |
|  | **[CAPABILITY](/documentation/code/files/susy__extras_8hpp/#define-capability)** <br>A map between PID pairs and cross-sections.  |
|  | **[FUNCTION](/documentation/code/files/susy__extras_8hpp/#define-function)** <br>Get the PIDPairCrossSectionsMap using the Prospino backend.  |
|  | **[CAPABILITY](/documentation/code/files/susy__extras_8hpp/#define-capability)** <br>A map between PID pairs and cross-sections.  |
|  | **[FUNCTION](/documentation/code/files/susy__extras_8hpp/#define-function)** <br>Get the PIDPairCrossSectionsMap using the Prospino backend.  |
|  | **[FUNCTION](/documentation/code/files/susy__extras_8hpp/#define-function)** <br>Get the PIDPairCrossSectionsMap using the Prospino backend.  |
|  | **[CAPABILITY](/documentation/code/files/susy__extras_8hpp/#define-capability)** <br>A map between PID pairs and cross-sections.  |
|  | **[FUNCTION](/documentation/code/files/susy__extras_8hpp/#define-function)** <br>Get the PIDPairCrossSectionsMap using the Prospino backend.  |
|  | **[CAPABILITY](/documentation/code/files/susy__extras_8hpp/#define-capability)** <br>A map between PID pairs and cross-sections.  |
|  | **[FUNCTION](/documentation/code/files/susy__extras_8hpp/#define-function)** <br>Get the PIDPairCrossSectionsMap using the Prospino backend.  |
|  | **[CAPABILITY](/documentation/code/files/susy__extras_8hpp/#define-capability)** <br>A map between PID pairs and cross-sections.  |
|  | **[FUNCTION](/documentation/code/files/susy__extras_8hpp/#define-function)** <br>Get the PIDPairCrossSectionsMap using the Prospino backend.  |
|  | **[CAPABILITY](/documentation/code/files/susy__extras_8hpp/#define-capability)** <br>A map between PID pairs and cross-sections.  |
|  | **[FUNCTION](/documentation/code/files/susy__extras_8hpp/#define-function)** <br>Get the PIDPairCrossSectionsMap using the Prospino backend.  |
|  | **[CAPABILITY](/documentation/code/files/susy__extras_8hpp/#define-capability)** <br>A map between PID pairs and cross-sections.  |
|  | **[FUNCTION](/documentation/code/files/susy__extras_8hpp/#define-function)** <br>Get the PIDPairCrossSectionsMap using the Prospino backend.  |
|  | **[MODULE](/documentation/code/files/susy__extras_8hpp/#define-module)**  |

## Detailed Description


**Author**: Anders Kvellestad ([anders.kvellestad@fys.uio.no](mailto:anders.kvellestad@fys.uio.no)) 

**Date**: 2020 Dec 2021 Jul

Rollcall header for ColliderBit module; extra things for SUSY models



------------------

Authors (add name and date if you modify):



------------------


## Functions Documentation

### function BACKEND_REQ

```
BACKEND_REQ(
    prospino_run ,
    (libprospino) ,
    map_str_dbl ,
    (const PID_pair &, const Options &) 
)
```


**Todo**: Extend to also allow models ColliderBit_SLHA_file_model, ColliderBit_SLHA_scan_model 


## Attributes Documentation

### variable libprospino

```
libprospino;
```


### variable void

```
void;
```



## Macros Documentation

### define CAPABILITY

```
#define CAPABILITY HardScatteringSim
```

A map between PID pairs and cross-sections. 

Cross-sections for weighting events by production process

Get SLHA content from one or more SLHA files

Extract SLHA file elements (for model ColliderBit_SLHA_file_model)

Extract an SLHAstruct with the spectrum

A dummy loglike function to ensure that points with failed mass spectrum and/or decay calculations can be invalidated aslo in "observables-only" scans 


### define FUNCTION

```
#define FUNCTION getPythia_SLHA
```

Get the PIDPairCrossSectionsMap using the Prospino backend. 

Get the next SLHA filename and content (for model ColliderBit_SLHA_file_model)

Read single SLHA file and replace some entries (for use with the model ColliderBit_SLHA_scan_model) 


### define CAPABILITY

```
#define CAPABILITY HardScatteringSim
```

A map between PID pairs and cross-sections. 

Cross-sections for weighting events by production process

Get SLHA content from one or more SLHA files

Extract SLHA file elements (for model ColliderBit_SLHA_file_model)

Extract an SLHAstruct with the spectrum

A dummy loglike function to ensure that points with failed mass spectrum and/or decay calculations can be invalidated aslo in "observables-only" scans 


### define FUNCTION

```
#define FUNCTION getPythia_SLHA
```

Get the PIDPairCrossSectionsMap using the Prospino backend. 

Get the next SLHA filename and content (for model ColliderBit_SLHA_file_model)

Read single SLHA file and replace some entries (for use with the model ColliderBit_SLHA_scan_model) 


### define CAPABILITY

```
#define CAPABILITY HardScatteringSim
```

A map between PID pairs and cross-sections. 

Cross-sections for weighting events by production process

Get SLHA content from one or more SLHA files

Extract SLHA file elements (for model ColliderBit_SLHA_file_model)

Extract an SLHAstruct with the spectrum

A dummy loglike function to ensure that points with failed mass spectrum and/or decay calculations can be invalidated aslo in "observables-only" scans 


### define FUNCTION

```
#define FUNCTION getPythia_SLHA
```

Get the PIDPairCrossSectionsMap using the Prospino backend. 

Get the next SLHA filename and content (for model ColliderBit_SLHA_file_model)

Read single SLHA file and replace some entries (for use with the model ColliderBit_SLHA_scan_model) 


### define FUNCTION

```
#define FUNCTION getPythia_SLHA
```

Get the PIDPairCrossSectionsMap using the Prospino backend. 

Get the next SLHA filename and content (for model ColliderBit_SLHA_file_model)

Read single SLHA file and replace some entries (for use with the model ColliderBit_SLHA_scan_model) 


### define CAPABILITY

```
#define CAPABILITY HardScatteringSim
```

A map between PID pairs and cross-sections. 

Cross-sections for weighting events by production process

Get SLHA content from one or more SLHA files

Extract SLHA file elements (for model ColliderBit_SLHA_file_model)

Extract an SLHAstruct with the spectrum

A dummy loglike function to ensure that points with failed mass spectrum and/or decay calculations can be invalidated aslo in "observables-only" scans 


### define FUNCTION

```
#define FUNCTION getPythia_SLHA
```

Get the PIDPairCrossSectionsMap using the Prospino backend. 

Get the next SLHA filename and content (for model ColliderBit_SLHA_file_model)

Read single SLHA file and replace some entries (for use with the model ColliderBit_SLHA_scan_model) 


### define CAPABILITY

```
#define CAPABILITY HardScatteringSim
```

A map between PID pairs and cross-sections. 

Cross-sections for weighting events by production process

Get SLHA content from one or more SLHA files

Extract SLHA file elements (for model ColliderBit_SLHA_file_model)

Extract an SLHAstruct with the spectrum

A dummy loglike function to ensure that points with failed mass spectrum and/or decay calculations can be invalidated aslo in "observables-only" scans 


### define FUNCTION

```
#define FUNCTION getPythia_SLHA
```

Get the PIDPairCrossSectionsMap using the Prospino backend. 

Get the next SLHA filename and content (for model ColliderBit_SLHA_file_model)

Read single SLHA file and replace some entries (for use with the model ColliderBit_SLHA_scan_model) 


### define CAPABILITY

```
#define CAPABILITY HardScatteringSim
```

A map between PID pairs and cross-sections. 

Cross-sections for weighting events by production process

Get SLHA content from one or more SLHA files

Extract SLHA file elements (for model ColliderBit_SLHA_file_model)

Extract an SLHAstruct with the spectrum

A dummy loglike function to ensure that points with failed mass spectrum and/or decay calculations can be invalidated aslo in "observables-only" scans 


### define FUNCTION

```
#define FUNCTION getPythia_SLHA
```

Get the PIDPairCrossSectionsMap using the Prospino backend. 

Get the next SLHA filename and content (for model ColliderBit_SLHA_file_model)

Read single SLHA file and replace some entries (for use with the model ColliderBit_SLHA_scan_model) 


### define CAPABILITY

```
#define CAPABILITY HardScatteringSim
```

A map between PID pairs and cross-sections. 

Cross-sections for weighting events by production process

Get SLHA content from one or more SLHA files

Extract SLHA file elements (for model ColliderBit_SLHA_file_model)

Extract an SLHAstruct with the spectrum

A dummy loglike function to ensure that points with failed mass spectrum and/or decay calculations can be invalidated aslo in "observables-only" scans 


### define FUNCTION

```
#define FUNCTION getPythia_SLHA
```

Get the PIDPairCrossSectionsMap using the Prospino backend. 

Get the next SLHA filename and content (for model ColliderBit_SLHA_file_model)

Read single SLHA file and replace some entries (for use with the model ColliderBit_SLHA_scan_model) 


### define CAPABILITY

```
#define CAPABILITY HardScatteringSim
```

A map between PID pairs and cross-sections. 

Cross-sections for weighting events by production process

Get SLHA content from one or more SLHA files

Extract SLHA file elements (for model ColliderBit_SLHA_file_model)

Extract an SLHAstruct with the spectrum

A dummy loglike function to ensure that points with failed mass spectrum and/or decay calculations can be invalidated aslo in "observables-only" scans 


### define FUNCTION

```
#define FUNCTION getPythia_SLHA
```

Get the PIDPairCrossSectionsMap using the Prospino backend. 

Get the next SLHA filename and content (for model ColliderBit_SLHA_file_model)

Read single SLHA file and replace some entries (for use with the model ColliderBit_SLHA_scan_model) 


### define MODULE

```
#define MODULE ColliderBit
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Rollcall header for ColliderBit module;
///  extra things for SUSY models
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Anders Kvellestad
///          (anders.kvellestad@fys.uio.no)
///  \date 2020 Dec
///        2021 Jul
///
///  *********************************************

#pragma once

#define MODULE ColliderBit

  // Get Monte Carlo event generator based on SLHA file input
  #define CAPABILITY HardScatteringSim

    #define FUNCTION getPythia_SLHA
    START_FUNCTION(Py8Collider_defaultversion)
    NEEDS_MANAGER(RunMC, MCLoopInfo)
    NEEDS_CLASSES_FROM(Pythia, default)
    ALLOW_MODELS(ColliderBit_SLHA_file_model, ColliderBit_SLHA_scan_model)
    DEPENDENCY(SLHAFileNameAndContent, pair_str_SLHAstruct)
    #undef FUNCTION

  #undef CAPABILITY




  /// Cross-sections for weighting events by production process
  /// @{

  /// A map between PID pairs and cross-sections
  #define CAPABILITY PIDPairCrossSectionsMap

    #ifdef HAVE_PYBIND11
      //Simple_xs
      #define FUNCTION getPIDPairCrossSectionsMap_simplexs
      START_FUNCTION(map_PID_pair_PID_pair_xsec)
      NEEDS_MANAGER(RunMC, MCLoopInfo)
      DEPENDENCY(ActivePIDPairs, vec_PID_pair)
      DEPENDENCY(SLHA1Spectrum, SLHAstruct)
      ALLOW_MODELS(ColliderBit_SLHA_file_model, ColliderBit_SLHA_scan_model)
      BACKEND_REQ(simplexs_init, (), void, (PyDict&))
      BACKEND_REQ(simplexs_get_xsection, (), PyDict, (PyDict&, PyDict&))
      #undef FUNCTION
    #endif

    #ifdef HAVE_PYBIND11
      /// Get the PIDPairCrossSectionsMap using the 'xsec' backend
      /// @todo 1. Replace SLHA1Spectrum dependency with SpectrumAndDecaysForPythia (to ensure same spectrum)
      /// @todo 2. Add a CB utility function that checks if a SLHAstruct is SLHA1 or SLHA2, and use it in this function
      #define FUNCTION getPIDPairCrossSectionsMap_xsecBE
      START_FUNCTION(map_PID_pair_PID_pair_xsec)
      NEEDS_MANAGER(RunMC, MCLoopInfo)
      DEPENDENCY(ActivePIDPairs, vec_PID_pair)
      DEPENDENCY(SLHA1Spectrum, SLHAstruct)
      ALLOW_MODELS(MSSM63atQ, MSSM63atQ_mG, MSSM63atQ_mA, MSSM63atQ_mA_mG, MSSM63atMGUT, MSSM63atMGUT_mG, MSSM63atMGUT_mA, MSSM63atMGUT_mA_mG)
      ALLOW_MODELS(ColliderBit_SLHA_file_model, ColliderBit_SLHA_scan_model)
      BACKEND_REQ(xsecBE_import_slha_string, (), void, (std::string&))
      BACKEND_REQ(xsecBE_set_parameters, (), void, (PyDict&))
      BACKEND_REQ(xsecBE_get_xsection, (), PyDict, (iipair&))
      #undef FUNCTION
    #endif

    /// Get the PIDPairCrossSectionsMap using the Prospino backend
    #define FUNCTION getPIDPairCrossSectionsMap_prospino
    START_FUNCTION(map_PID_pair_PID_pair_xsec)
    NEEDS_MANAGER(RunMC, MCLoopInfo)
    DEPENDENCY(ActivePIDPairs, vec_PID_pair)
    DEPENDENCY(SLHA1Spectrum, SLHAstruct)
    ALLOW_MODELS(MSSM63atQ, MSSM63atQ_mG, MSSM63atQ_mA, MSSM63atQ_mA_mG, MSSM63atMGUT, MSSM63atMGUT_mG, MSSM63atMGUT_mA, MSSM63atMGUT_mA_mG)
    /// @todo Extend to also allow models ColliderBit_SLHA_file_model, ColliderBit_SLHA_scan_model
    BACKEND_REQ(prospino_run, (libprospino), map_str_dbl, (const PID_pair&, const Options&))
    BACKEND_REQ(prospino_read_slha1_input, (libprospino), void, (const SLHAstruct&))
    #undef FUNCTION

    #ifdef HAVE_PYBIND11
      /// Get the PIDPairCrossSectionsMap using the 'salami' backend
      /// @todo 1. Replace SLHA1Spectrum dependency with SpectrumAndDecaysForPythia (to ensure same spectrum)
      /// @todo 2. Add a CB utility function that checks if a SLHAstruct is SLHA1 or SLHA2, and use it in this function
      #define FUNCTION getPIDPairCrossSectionsMap_salami
      START_FUNCTION(map_PID_pair_PID_pair_xsec)
      NEEDS_MANAGER(RunMC, MCLoopInfo)
      DEPENDENCY(ActivePIDPairs, vec_PID_pair)
      DEPENDENCY(SLHA1Spectrum, SLHAstruct)
      ALLOW_MODELS(MSSM63atQ, MSSM63atQ_mG, MSSM63atQ_mA, MSSM63atQ_mA_mG, MSSM63atMGUT, MSSM63atMGUT_mG, MSSM63atMGUT_mA, MSSM63atMGUT_mA_mG)
      ALLOW_MODELS(ColliderBit_SLHA_file_model, ColliderBit_SLHA_scan_model)
      BACKEND_REQ(salami_import_slha_string, (), void, (std::string&))
      BACKEND_REQ(salami_set_parameters, (), void, (PyDict&))
      BACKEND_REQ(salami_get_xsection, (), PyDict, (iipair&, double&, double&))
      // Needs Prospino to get LO cross-section
      BACKEND_REQ(prospino_run_alloptions, (libprospino), map_str_dbl, (const PID_pair&, const int&, const int&, const int&, const double&, const int&, const bool&))
      BACKEND_REQ(prospino_read_slha1_input, (libprospino), void, (const SLHAstruct&))
      #undef FUNCTION
    #endif

  #undef CAPABILITY
  /// @}


  /// Get SLHA content from one or more SLHA files
  /// @{
  #define CAPABILITY SLHAFileNameAndContent
  START_CAPABILITY

    /// Get the next SLHA filename and content (for model ColliderBit_SLHA_file_model)
    #define FUNCTION getNextSLHAFileNameAndContent
    START_FUNCTION(pair_str_SLHAstruct)
    ALLOW_MODELS(ColliderBit_SLHA_file_model)
    #undef FUNCTION

    /// Read single SLHA file and replace some entries
    /// (for use with the model ColliderBit_SLHA_scan_model)
    #define FUNCTION getAndReplaceSLHAContent
    START_FUNCTION(pair_str_SLHAstruct)
    ALLOW_MODELS(ColliderBit_SLHA_scan_model)
    #undef FUNCTION

  #undef CAPABILITY
  /// @}


  /// Extract SLHA file elements (for model ColliderBit_SLHA_file_model)
  /// @{
  #define CAPABILITY SLHAFileElements
  START_CAPABILITY
    #define FUNCTION getSLHAFileElements
    START_FUNCTION(map_str_dbl)
    ALLOW_MODELS(ColliderBit_SLHA_file_model, ColliderBit_SLHA_scan_model)
    DEPENDENCY(SLHAFileNameAndContent, pair_str_SLHAstruct)
    #undef FUNCTION
  #undef CAPABILITY
  /// @}


  /// Extract an SLHAstruct with the spectrum
  /// @{
  #define CAPABILITY SLHA1Spectrum
  START_CAPABILITY
    #define FUNCTION getSLHA1Spectrum
    START_FUNCTION(SLHAstruct)
    ALLOW_MODELS(MSSM63atQ, MSSM63atQ_mG, MSSM63atQ_mA, MSSM63atQ_mA_mG, MSSM63atMGUT, MSSM63atMGUT_mG, MSSM63atMGUT_mA, MSSM63atMGUT_mA_mG)
    ALLOW_MODELS(ColliderBit_SLHA_file_model, ColliderBit_SLHA_scan_model)
    MODEL_CONDITIONAL_DEPENDENCY(SLHAFileNameAndContent, pair_str_SLHAstruct, ColliderBit_SLHA_file_model, ColliderBit_SLHA_scan_model)
    MODEL_CONDITIONAL_DEPENDENCY(MSSM_spectrum, Spectrum, MSSM63atQ, MSSM63atMGUT, MSSM63atQ_mA, MSSM63atMGUT_mA)
    #undef FUNCTION
  #undef CAPABILITY

  #define CAPABILITY SLHA2Spectrum
  START_CAPABILITY
    #define FUNCTION getSLHA2Spectrum
    START_FUNCTION(SLHAstruct)
    ALLOW_MODELS(MSSM63atQ, MSSM63atQ_mG, MSSM63atQ_mA, MSSM63atQ_mA_mG, MSSM63atMGUT, MSSM63atMGUT_mG, MSSM63atMGUT_mA, MSSM63atMGUT_mA_mG)
    ALLOW_MODELS(ColliderBit_SLHA_file_model, ColliderBit_SLHA_scan_model)
    MODEL_CONDITIONAL_DEPENDENCY(SLHAFileNameAndContent, pair_str_SLHAstruct, ColliderBit_SLHA_file_model, ColliderBit_SLHA_scan_model)
    MODEL_CONDITIONAL_DEPENDENCY(MSSM_spectrum, Spectrum, MSSM63atQ, MSSM63atMGUT, MSSM63atQ_mA, MSSM63atMGUT_mA)
    #undef FUNCTION
  #undef CAPABILITY
  /// @}


  #define CAPABILITY susy_spectrum_scan_guide
  START_CAPABILITY
    #define FUNCTION calc_susy_spectrum_scan_guide
    START_FUNCTION(double)
    ALLOW_MODELS(MSSM63atQ, MSSM63atQ_mG, MSSM63atQ_mA, MSSM63atQ_mA_mG, MSSM63atMGUT, MSSM63atMGUT_mG, MSSM63atMGUT_mA, MSSM63atMGUT_mA_mG)
    DEPENDENCY(SLHA_pseudonyms, mass_es_pseudonyms)
    MODEL_CONDITIONAL_DEPENDENCY(MSSM_spectrum, Spectrum, MSSM63atQ, MSSM63atMGUT, MSSM63atQ_mA, MSSM63atMGUT_mA)
    #undef FUNCTION
  #undef CAPABILITY

  /// A dummy loglike function to ensure that points with failed mass spectrum
  /// and/or decay calculations can be invalidated aslo in "observables-only" scans
  #define CAPABILITY susy_spectrum_validation_loglike
    #define FUNCTION get_susy_spectrum_validation_loglike
    START_FUNCTION(double)
    DEPENDENCY(decay_rates, DecayTable)
    DEPENDENCY(MSSM_spectrum, Spectrum)
    DEPENDENCY(SLHA_pseudonyms, mass_es_pseudonyms)
    ALLOW_MODELS(MSSM63atQ, MSSM63atQ_mG, MSSM63atQ_mA, MSSM63atQ_mA_mG, MSSM63atMGUT, MSSM63atMGUT_mG, MSSM63atMGUT_mA, MSSM63atMGUT_mA_mG)
    #undef FUNCTION
  #undef CAPABILITY

#undef MODULE
```


-------------------------------

Updated on 2024-07-18 at 13:53:34 +0000
