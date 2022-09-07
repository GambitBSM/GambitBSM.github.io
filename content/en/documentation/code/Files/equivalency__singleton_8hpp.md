---
title: "file Elements/equivalency_singleton.hpp"

description: "[No description available]"

---

# file Elements/equivalency_singleton.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::Utils](/documentation/code/namespaces/namespacegambit_1_1utils/)**  |

## Detailed Description


**Author**: Pat Scott 

**Date**: 2014 Aug

GAMBIT backend info object accessor function.



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  GAMBIT backend info object accessor function.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///   
///  \author Pat Scott
///  \date 2014 Aug
///
///  *********************************************

#ifndef __equivalency_singleton_hpp__
#define __equivalency_singleton_hpp__

#include "gambit/Elements/type_equivalency.hpp"


namespace Gambit
{

  namespace Utils
  {

    /// Backend info accessor function
    type_equivalency& typeEquivalencies();

  }

}


#endif // defined __equivalency_singleton_hpp__
```


-------------------------------

Updated on 2022-09-07 at 23:22:09 +0000
