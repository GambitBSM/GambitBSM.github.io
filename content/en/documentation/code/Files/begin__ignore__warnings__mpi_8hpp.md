---
title: "file Utils/begin_ignore_warnings_mpi.hpp"

description: "[No description available]"

---

# file Utils/begin_ignore_warnings_mpi.hpp

[No description available] [More...](#detailed-description)

## Detailed Description


**Author**: 

  * Anders Kvellestad ([anders.kvellestad@fys.uio.no](mailto:anders.kvellestad@fys.uio.no)) 
  * Tomas Gonzalo ([gonzalo@physik.rwth-aachen.de](mailto:gonzalo@physik.rwth-aachen.de)) 


**Date**: 

  * 2021 Jul
  * 2022 Apr


Pragma directives to suppress compiler warnings coming from including MPI library headers.



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
///  coming from including MPI library headers.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Anders Kvellestad
///          (anders.kvellestad@fys.uio.no)
///  \date 2021 Jul
///
///  \author Tomas Gonzalo
///          (gonzalo@physik.rwth-aachen.de)
///  \date 2022 Apr
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
    #pragma GCC diagnostic ignored "-Wcast-function-type"
  #endif

  // Clang:
  // icpc apparently also defines __clang__ 
  #if defined(__clang__) && !defined(__ICC)
    // Save diagnostic state
    #pragma clang diagnostic push 
    // Don't care if an old compiler version doesn't recognize all the pragmas
    #pragma clang diagnostic ignored "-Wpragmas"
    // This only exists from clang 13.0
    #if __clang__ > 13
      #pragma clang diagnostic ignored "-Wcast-function-type"
    #endif
  #endif

#endif
```


-------------------------------

Updated on 2025-02-12 at 16:10:33 +0000
