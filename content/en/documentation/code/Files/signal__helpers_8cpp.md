---
title: "file src/signal_helpers.cpp"

description: "[No description available]"

---

# file src/signal_helpers.cpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |

## Detailed Description


**Author**: Ben Farmer ([benjamin.farmer@fysik.su.se](mailto:benjamin.farmer@fysik.su.se)) 

**Date**: 2015 Oct

Function definitions for signal helper functions.



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Function definitions for signal helper 
///  functions.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///   
///  \author Ben Farmer
///          (benjamin.farmer@fysik.su.se)
///  \date 2015 Oct
///
///  *********************************************

#include "gambit/Utils/signal_helpers.hpp"
#include <cstddef> // for NULL

namespace Gambit
{
   /// Getter for global signal set
   sigset_t* signal_mask()
   {
      static sigset_t mask;
      return &mask;
   }

   /// @{ Signal blocking/unblocking
   void block_signals()
   {
      sigprocmask(SIG_BLOCK, signal_mask(), NULL);
   }

   void unblock_signals()
   {
      sigprocmask(SIG_UNBLOCK, signal_mask(), NULL);
   }
   /// @}
   
}
```


-------------------------------

Updated on 2022-09-07 at 23:22:08 +0000
