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


**Author**: 

  * Pat Scott 

 ([patscott@physics.mcgill.ca](mailto:patscott@physics.mcgill.ca)) 
  * Chris Chang 


**Date**: 

  * 2014 Feb
  * 2023 Dec


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
///  \author Chris Chang
///  \date 2023 Dec
///
///  *********************************************

#ifndef __standalone_utils_hpp__
#define __standalone_utils_hpp__

#include "gambit/Utils/util_functions.hpp"
#include "gambit/Utils/yaml_node_utility.hpp"

namespace Gambit
{

  /// Logger setup standalone utility function
  void initialise_standalone_logs(str);

  /// Initialise the printers (required for suspicious point raises)
  YAML::Node get_standalone_printer(str, str, str);

}


#endif //__standalone_utils_hpp__
```


-------------------------------

Updated on 2025-02-12 at 15:36:40 +0000
