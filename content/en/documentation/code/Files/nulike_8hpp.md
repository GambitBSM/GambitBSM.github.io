---
title: "file backend_types/nulike.hpp"

description: "[No description available]"

---

# file backend_types/nulike.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |

## Detailed Description


**Author**: Pat Scott [p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)

**Date**: 2015 Aug

Helper types for nulike backend.



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Helper types for nulike backend.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Pat Scott
///          p.scott@imperial.ac.uk
///  \date 2015 Aug
///
///  *************************

#ifndef __nulike_types_hpp__
#define __nulike_types_hpp__

namespace Gambit
{

  // Neutrino yield function signature
  typedef double(*nuyield_function_pointer)(const double&, const int&, void*&);

}

#endif /* defined __nulike_types_hpp__ */
```


-------------------------------

Updated on 2025-02-12 at 16:10:36 +0000
