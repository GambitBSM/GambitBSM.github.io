---
title: "file Utils/standalone_error_handlers.hpp"

description: "[No description available]"

---

# file Utils/standalone_error_handlers.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::Printers](/documentation/code/namespaces/namespacegambit_1_1printers/)** <br>Forward declaration.  |
| **[Gambit::IniParser](/documentation/code/namespaces/namespacegambit_1_1iniparser/)**  |

## Detailed Description


**Author**: Pat Scott ([patscott@physics.mcgill.ca](mailto:patscott@physics.mcgill.ca)) 

**Date**: 2014 Mar

Exception objects required for standalone compilation.



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Exception objects required for standalone
///  compilation.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Pat Scott
///          (patscott@physics.mcgill.ca)
///  \date 2014 Mar
///
///  *********************************************

#ifndef __standalone_error_handlers_hpp__
#define __standalone_error_handlers_hpp__

#include "gambit/Utils/util_macros.hpp"
#include "gambit/Utils/exceptions.hpp"

namespace Gambit
{

  /// Utility errors
  EXPORT_SYMBOLS error& utils_error();
  /// Utility warnings
  EXPORT_SYMBOLS warning& utils_warning();

  /// Backend errors
  error& backend_error();
  /// Backend warnings
  warning& backend_warning();

  /// Logging errors
  error& logging_error();
  /// Logging warnings
  warning& logging_warning();

  /// Model errors
  error& model_error();
  /// Model warnings
  warning& model_warning();

  /// Invalid point exceptions
  invalid_point_exception& invalid_point();

  namespace Printers
  {
    /// Printer errors
    EXPORT_SYMBOLS error& printer_error();
    /// Printer warnings
    EXPORT_SYMBOLS warning& printer_warning();
  }

  namespace IniParser
  {
    /// IniFile errors
    error& inifile_error();
    /// IniFile warnings
    warning& inifile_warning();
  }

}

#endif //#ifndef __standalone_error_handlers_hpp__
```


-------------------------------

Updated on 2022-09-08 at 02:00:50 +0000
