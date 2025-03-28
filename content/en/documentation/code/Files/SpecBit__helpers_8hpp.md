---
title: "file SpecBit/SpecBit_helpers.hpp"

description: "[No description available]"

---

# file SpecBit/SpecBit_helpers.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::SpecBit](/documentation/code/namespaces/namespacegambit_1_1specbit/)**  |

## Detailed Description


**Author**: 

  * Ben Farmer ([benjamin.farmer@fysik.su.se](mailto:benjamin.farmer@fysik.su.se)) 
  * Tomas Gonzalo ([tomas.gonzalo@monash.edu](mailto:tomas.gonzalo@monash.edu)) 


**Date**: 

  * 2014 Sep - Dec, 2015 Jan - May
  * Jul 2020


Declarations of convenience (i.e. non-Gambit) functions used by more than one SpecBit source file.



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Declarations of convenience (i.e. non-Gambit)
///  functions used by more than one SpecBit 
///  source file.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Ben Farmer
///          (benjamin.farmer@fysik.su.se)
///    \date 2014 Sep - Dec, 2015 Jan - May
///
///  \author Tomas Gonzalo
///          (tomas.gonzalo@monash.edu)
///  \date Jul 2020
///  
///  *********************************************

#ifndef __SpecBit_helpers_hpp__
#define __SpecBit_helpers_hpp__

#include "gambit/Elements/sminputs.hpp"

// Flexible SUSY stuff (should not be needed by the rest of gambit)
//#include "flexiblesusy/src/ew_input.hpp"
#include "flexiblesusy/src/lowe.h" // From softsusy; used by flexiblesusy
//#include "flexiblesusy/src/numerics.hpp"

namespace Gambit
{

  namespace SpecBit
  {

    /// @{

    /// Non-Gambit helper functions
    //  =======================================================================
    //  These are not known to Gambit, but perform helper tasks used by the
    //  Gambit module functions.

    /// Initialise QedQcd object from SMInputs data
    void setup_QedQcd(softsusy::QedQcd& oneset /*output*/, const SMInputs& sminputs /*input*/);

    /// Check that the spectrum has a neutralino LSP.
    bool has_neutralino_LSP(const Spectrum& result);

    /// Helper to work with pointer
    bool has_neutralino_LSP(const Spectrum* result);

    /// @}

  }
}
 
#endif
```


-------------------------------

Updated on 2025-02-12 at 16:10:33 +0000
