---
title: "file Elements/slhaea_spec_helpers.hpp"

description: "[No description available]"

---

# file Elements/slhaea_spec_helpers.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |

## Detailed Description


**Author**: 

  * Ben Farmer ([benjamin.farmer@monash.edu](mailto:benjamin.farmer@monash.edu)) 
  * Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 
  * Tomas Gonzalo ([tomas.gonzalo@monash.edu](mailto:tomas.gonzalo@monash.edu)) 


**Date**: 

  * 2015
  * 2015
  * 2020


SLHAea helper functions using spectrum objects



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  SLHAea helper functions using spectrum objects
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Ben Farmer
///          (benjamin.farmer@monash.edu)
///  \date 2015
///
///  \author Pat Scott
///          (p.scott@imperial.ac.uk)
///  \date 2015
///
///  \author Tomas Gonzalo
///          (tomas.gonzalo@monash.edu)
///  \date 2020
///
///  *********************************************

#ifndef __slha_spec_helpers_hpp__
#define __slha_spec_helpers_hpp__

#include "gambit/Utils/standalone_error_handlers.hpp"
#include "gambit/Utils/util_types.hpp"
#include "gambit/Utils/slhaea_helpers.hpp"
#include "gambit/Elements/spectrum_helpers.hpp"
#include "gambit/Models/SpectrumContents/subspectrum_contents.hpp"

#include "SLHAea/slhaea.h"

#include <boost/serialization/strong_typedef.hpp>

namespace Gambit
{
  /// Forward declare SubSpectrum class
  class SubSpectrum;

  /// Add an entry from a subspectrum getter to an SLHAea object; SLHA index given by pdg code
  void SLHAea_add_from_subspec(SLHAstruct& slha /*modify*/, const str local_info, const SubSpectrum& subspec,
   const Par::Tags partype, const std::pair<int, int>& pdg_pair, const str& block, const str& comment,
   const bool error_if_missing = true, const double rescale = 1.0);

  /// Add an entry from a subspectrum getter to an SLHAea object; 1 SLHA index
  void SLHAea_add_from_subspec(SLHAstruct& slha /*modify*/, const str local_info, const SubSpectrum& subspec,
   const Par::Tags partype, const str& name, const str& block, const int slha_index,
   const str& comment, const bool error_if_missing = true, const double rescale = 1.0);

  /// Add an entry from a subspectrum getter to an SLHAea object; two SubSpectrum getter indices, two SLHA indices
  void SLHAea_add_from_subspec(SLHAstruct& slha /*modify*/, const str local_info, const SubSpectrum& subspec,
   const Par::Tags partype, const str& name, const int index1, const int index2, const str& block,
   const int slha_index1, const int slha_index2, const str& comment, const bool error_if_missing = true, const double rescale = 1.0);

  /// Write a SimpleSpectrum to an SLHAea object.
  void add_SimpleSpec_to_SLHAea(const SubSpectrum&, SLHAstruct&, const SubSpectrumContents&);

}

#endif //defined __slhaea_spec_helpers_hpp__
```


-------------------------------

Updated on 2025-02-12 at 16:10:34 +0000
