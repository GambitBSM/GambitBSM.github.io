---
title: "file Elements/ini_catch.hpp"

description: "[No description available]"

---

# file Elements/ini_catch.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |

## Detailed Description


Micro function useful from all sorts of other initialisation codes.



------------------


# Authors

(add name and date if you modify)

Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 

2015 Feb



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Micro function useful from all sorts of other
///  initialisation codes.
///
///  *********************************************
///
///  Authors
///  =======
///
///  (add name and date if you modify)
///
///  \author Pat Scott
///          (p.scott@imperial.ac.uk)
///  \date 2015 Feb
///
///  *********************************************

#include <exception>

namespace Gambit
{

  /// Catch initialisation exceptions
  void ini_catch(std::exception&);

}
```


-------------------------------

Updated on 2022-09-08 at 01:48:58 +0000
