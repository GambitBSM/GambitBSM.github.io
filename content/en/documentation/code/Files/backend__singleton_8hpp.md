---
title: "file Backends/backend_singleton.hpp"

description: "[No description available]"

---

# file Backends/backend_singleton.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::Backends](/documentation/code/namespaces/namespacegambit_1_1backends/)**  |

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

#ifndef __backend_singleton_hpp__
#define __backend_singleton_hpp__

#include "gambit/Backends/backend_info.hpp"


namespace Gambit
{

  namespace Backends
  {

    /// Backend info accessor function
    backend_info& backendInfo();

  }

}


#endif // defined __backend_singleton_hpp__
```


-------------------------------

Updated on 2025-02-12 at 16:10:36 +0000
