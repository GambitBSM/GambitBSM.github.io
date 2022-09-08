---
title: "file Utils/citation_keys.hpp"

description: "[No description available]"

---

# file Utils/citation_keys.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |

## Detailed Description


**Author**: Tomas Gonzalo ([gonzalo@physik.rwth-aachen.de](mailto:gonzalo@physik.rwth-aachen.de)) 

**Date**: 2021 Sep

Citation keys for GAMBIT.



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Citation keys for GAMBIT.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Tomas Gonzalo
///          (gonzalo@physik.rwth-aachen.de)
///  \date 2021 Sep
///
///  *********************************************

#ifndef __citation_keys_hpp__
#define __citation_keys_hpp__

#include "gambit/Utils/util_types.hpp"

namespace Gambit
{

  // GAMBIT citation keys
  const std::vector<str> gambit_citation_keys = 
  {
    "GAMBIT:2017yxo", // GAMBIT Core paper
    "Kvellestad:2019vxm", // GAMBIT review
      // GUM additions
  };
}

#endif // defined __citation_keys_hpp__
```


-------------------------------

Updated on 2022-09-08 at 02:23:02 +0000
