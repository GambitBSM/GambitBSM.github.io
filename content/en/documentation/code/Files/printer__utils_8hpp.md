---
title: "file Printers/printer_utils.hpp"

description: "[No description available]"

---

# file Printers/printer_utils.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |

## Detailed Description


**Author**: Chris Chang 

**Date**: Dec 2023

Functions that require printing capabilities that can be run from within module functions.

Authors:



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Functions that require printing capabilities
///  that can be run from within module functions.
///
///  Authors:
///
///  \author Chris Chang          
///  \date Dec 2023
///
///  *********************************************

#ifndef __printer_utils_hpp__
#define __printer_utils_hpp__

#include <map>
#include <set>
#include <string>
#include <exception>
#include <vector>
#include <utility>

#include "gambit/Utils/util_macros.hpp"
#include "gambit/Logs/log_tags.hpp"
#include "gambit/Printers/baseprinter.hpp"
#include "gambit/Printers/printermanager.hpp"

namespace Gambit
{

  /// Postprocessor reader retrieve function
  template<typename T>
  bool pp_reader_retrieve(T& result, str dataset)
  {
    return get_pp_reader().retrieve(result, dataset);
  }
}

#endif
```


-------------------------------

Updated on 2024-07-18 at 13:53:33 +0000
