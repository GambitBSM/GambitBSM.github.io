---
title: "file Utils/standalone_utils.hpp"

description: "[No description available]"

---

# file Utils/standalone_utils.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |

## Detailed Description


**Author**: Pat Scott 

 ([patscott@physics.mcgill.ca](mailto:patscott@physics.mcgill.ca)) 

**Date**: 2014 Feb

Utilities needed to use a GAMBIT module as a standalone analysis code.



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Utilities needed to use a GAMBIT
///  module as a standalone analysis code.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///   
///  \author Pat Scott  
///          (patscott@physics.mcgill.ca)
///  \date 2014 Feb
///
///  *********************************************

#ifndef __standalone_utils_hpp__
#define __standalone_utils_hpp__

#include "gambit/Utils/util_functions.hpp"

namespace Gambit
{

  /// Logger setup standalone utility function
  void initialise_standalone_logs(str);

}


#endif //__standalone_utils_hpp__
```


-------------------------------

Updated on 2023-06-26 at 21:36:53 +0000
