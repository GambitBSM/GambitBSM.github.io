---
title: "file Core/resolution_utilities.hpp"

description: "[No description available]"

---

# file Core/resolution_utilities.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::DRes](/documentation/code/namespaces/namespacegambit_1_1dres/)** <br>Forward declaration of [Rule]() and Observables classes for saving pointers to ignored and matched examples.  |

## Detailed Description


**Author**: Pat Scott ([patrickcolinscott@gmail.com](mailto:patrickcolinscott@gmail.com)) 

**Date**: 2022 Nov

Utilities useful during dependency resolution.



------------------

Authors (add name and date if you modify): 

------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Utilities useful during dependency resolution.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///  \author Pat Scott
///          (patrickcolinscott@gmail.com)
///  \date 2022 Nov
///
///  *********************************************

#pragma once

#include "gambit/Utils/util_types.hpp"
#include "gambit/Elements/type_equivalency.hpp"

namespace Gambit
{

  namespace DRes
  {

    /// Check whether s1 (wildcard + regex allowed) matches s2
    bool stringComp(const str & s1, const str & s2);

    /// Check whether type 1 (wildcard + regex allowed) matches type 2, taking into account equivalence classes.
    bool typeComp(str s1, str s2, const Utils::type_equivalency & eq);

  }

}
```


-------------------------------

Updated on 2025-02-12 at 16:10:35 +0000
