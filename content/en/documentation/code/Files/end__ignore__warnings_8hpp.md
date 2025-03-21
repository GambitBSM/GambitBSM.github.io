---
title: "file Utils/end_ignore_warnings.hpp"

description: "[No description available]"

---

# file Utils/end_ignore_warnings.hpp

[No description available] [More...](#detailed-description)

## Detailed Description


**Author**: 

  * Anders Kvellestad ([anders.kvellestad@fys.uio.no](mailto:anders.kvellestad@fys.uio.no)) 
  * Tomas Gonzalo ([gonzalo@physik.rwth-aachen.de](mailto:gonzalo@physik.rwth-aachen.de)) 


**Date**: 

  * 2021 Jul
  * 2022 Apr


Simple header file for turning compiler warnings back on after having included one of the begin_ignore_warnings_*.hpp files.



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Simple header file for turning compiler 
///  warnings back on after having included
///  one of the begin_ignore_warnings_*.hpp files.
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


// SUPPRESS_LIBRARY_WARNINGS is defined by gambit/cmake/cmake_variables.hpp
// which will have been included by the begin_ignore_warnings_*.hpp file.
#ifdef SUPPRESS_LIBRARY_WARNINGS

  // GCC:
  // clang also depfines __GNUC__ so make sure it is only GCC
  #if defined(__GNUC__) && !defined(__clang__)
    // Turn warnings back on
    #pragma GCC diagnostic pop
  #endif

  // Clang:
  // icpc apparently also defines __clang__ 
  #if defined(__clang__) && !defined(__ICC)
    // Turn warnings back on
    #pragma clang diagnostic pop
  #endif
  
#endif
```


-------------------------------

Updated on 2025-02-12 at 16:10:33 +0000
