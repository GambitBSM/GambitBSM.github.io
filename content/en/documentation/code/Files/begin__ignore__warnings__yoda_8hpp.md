---
title: "file Utils/begin_ignore_warnings_yoda.hpp"

description: "[No description available]"

---

# file Utils/begin_ignore_warnings_yoda.hpp

[No description available] [More...](#detailed-description)

## Detailed Description


**Author**: Anders Kvellestad ([anders.kvellestad@fys.uio.no](mailto:anders.kvellestad@fys.uio.no)) 

**Date**: 2023 Feb

Pragma directives to suppress compiler warnings coming from including YODA headers.



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Pragma directives to suppress compiler warnings
///  coming from including YODA headers.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Anders Kvellestad
///          (anders.kvellestad@fys.uio.no)
///  \date 2023 Feb
///
///  *********************************************


#include "gambit/cmake/cmake_variables.hpp"

#ifdef SUPPRESS_LIBRARY_WARNINGS

  // GCC:
  // clang also depfines __GNUC__ so make sure it is only GCC
  #if defined(__GNUC__) && !defined(__clang__)
    // Save diagnostic state
    #pragma GCC diagnostic push 
    // Don't care if an old compiler version doesn't recognize all the pragmas
    #pragma GCC diagnostic ignored "-Wpragmas"
    // Turn off some warnings
    #pragma GCC diagnostic ignored "-Wdeprecated-copy"
  #endif

  // Clang:
  // icpc apparently also defines __clang__ 
  #if defined(__clang__) && !defined(__ICC)
    // Save diagnostic state
    #pragma clang diagnostic push 
    // Don't care if an old compiler version doesn't recognize all the pragmas
    #pragma clang diagnostic ignored "-Wpragmas"
    // Turn off some warnings
    #pragma clang diagnostic ignored "-Wdeprecated-copy"
  #endif

#endif
```


-------------------------------

Updated on 2023-06-26 at 21:36:53 +0000