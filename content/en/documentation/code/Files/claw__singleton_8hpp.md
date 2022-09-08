---
title: "file Models/claw_singleton.hpp"

description: "[No description available]"

---

# file Models/claw_singleton.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::Models](/documentation/code/namespaces/namespacegambit_1_1models/)** <br>Forward declaration of [Models::ModelFunctorClaw]() class for use in constructors.  |

## Detailed Description


**Author**: Pat Scott 

**Date**: 2014 Aug

GAMBIT model claw object accessor function.



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  GAMBIT model claw object accessor function.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///   
///  \author Pat Scott
///  \date 2014 Aug
///
///  *********************************************

#ifndef __claw_singleton_hpp__
#define __claw_singleton_hpp__

#include "gambit/Models/models.hpp"


namespace Gambit
{

  namespace Models
  {

    /// Claw accessor function
    ModelFunctorClaw& ModelDB();

  }

}

#endif // defined __claw_singleton_hpp__
```


-------------------------------

Updated on 2022-09-08 at 02:23:03 +0000
