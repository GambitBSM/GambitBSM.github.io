---
title: "file Utils/static_members.hpp"

description: "[No description available]"

---

# file Utils/static_members.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |

## Detailed Description


**Author**: Pat Scott ([patscott@physics.mcgill.ca](mailto:patscott@physics.mcgill.ca)) 

**Date**: 2014 Mar

Initialisation of static member variables in utility classes.



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Initialisation of static member variables in 
///  utility classes.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///   
///  \author Pat Scott 
///          (patscott@physics.mcgill.ca)
///  \date 2014 Mar
///
///  *********************************************

#ifndef __static_members_hpp__
#define __static_members_hpp__

#include "gambit/Utils/threadsafe_rng.hpp"
#include "gambit/Utils/exceptions.hpp"

namespace Gambit
{

  /// Pointer to chosen random number generation engine
  Utils::threadsafe_rng* Random::local_rng = NULL;

  /// Shared string indicating the current values of the paramters.
  str exception::parameters = "";

}

#endif //#ifndef __static_members_hpp__
```


-------------------------------

Updated on 2022-09-08 at 02:27:28 +0000
