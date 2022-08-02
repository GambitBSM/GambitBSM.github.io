---
title: 'file Core/error_handlers.hpp'

description: "[No description available]"

---






[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/colliderbit_development/namespaces/namespacegambit/)** <br>Simulation of "Search for photonic signatures of gauge-mediated supersymmetry in 13 TeV pp collisions with the ATLAS detector".  |
| **[Gambit::DRes](/documentation/code/colliderbit_development/namespaces/namespacegambit_1_1dres/)**  |

## Detailed Description


**Author**: Pat Scott ([patscott@physics.mcgill.ca](mailto:patscott@physics.mcgill.ca)) 

**Date**: 2014 Mar

Exception object declarations.



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************

#ifndef __error_handlers_hpp__
#define __error_handlers_hpp__

#include "gambit/Utils/standalone_error_handlers.hpp"
#include "gambit/Utils/local_info.hpp"

namespace Gambit
{

  error& core_error();
  warning& core_warning();

  namespace DRes
  {
    error& dependency_resolver_error();
    warning& dependency_resolver_warning();
  }
    
}

#endif //#ifndef error_handlers_hpp
```


-------------------------------

Updated on 2022-08-02 at 18:18:38 +0000