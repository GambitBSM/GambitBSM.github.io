---
title: "file src/equivalency_singleton.cpp"

description: "[No description available]"

---

# file src/equivalency_singleton.cpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::Utils](/documentation/code/namespaces/namespacegambit_1_1utils/)**  |

## Detailed Description


**Author**: Pat Scott 

**Date**: 2014 Oct

GAMBIT type equivalency object accessor function.



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  GAMBIT type equivalency object accessor function.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///   
///  \author Pat Scott
///  \date 2014 Oct
///
///  *********************************************

#include "gambit/Elements/equivalency_singleton.hpp"

namespace Gambit
{

  namespace Utils
  {

    /// Type equivalency accessor function
    type_equivalency& typeEquivalencies()
    {
      static type_equivalency local;
      return local;
    }

  }

}
```


-------------------------------

Updated on 2022-09-08 at 03:17:36 +0000
