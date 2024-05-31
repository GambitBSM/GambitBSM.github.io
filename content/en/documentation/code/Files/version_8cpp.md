---
title: "file src/version.cpp"

description: "[No description available]"

---

# file src/version.cpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |

## Detailed Description


**Author**: Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 

**Date**: 2017 Apr

Version command



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Version command
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Pat Scott
///          (p.scott@imperial.ac.uk)
///  \date 2017 Apr
///
///  *********************************************

#include "gambit/Utils/version.hpp"

namespace Gambit
{

  /// Construct a string containing the full GAMBIT version information.
  str get_gambit_version()
  {
    std::ostringstream ss;
    ss << gambit_version_major << "." << gambit_version_minor << "." << gambit_version_revision;
    if (!gambit_version_patch.empty()) ss << "-" << gambit_version_patch;
    return ss.str();
  }

  /// Statically construct a string containing the full GAMBIT version information and return a reference to it.
  str& gambit_version()
  {
    static str local = get_gambit_version();
    return local;
  }

}
```


-------------------------------

Updated on 2024-05-31 at 15:12:05 +0000
