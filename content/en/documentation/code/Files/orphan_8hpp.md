---
title: "file Models/orphan.hpp"

description: "[No description available]"

---

# file Models/orphan.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::Models](/documentation/code/namespaces/namespacegambit_1_1models/)** <br>Forward declaration of [Models::ModelFunctorClaw]() class for use in constructors.  |
| **[Gambit::Models::PARENT](/documentation/code/namespaces/namespacegambit_1_1models_1_1parent/)**  |

## Detailed Description


**Author**: Pat Scott ([patscott@physics.mcgill.ca](mailto:patscott@physics.mcgill.ca)) 

**Date**: 2014 Aug

Base lineage for starting orphan models.



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Base lineage for starting orphan models.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///   
///  \author Pat Scott
///          (patscott@physics.mcgill.ca)
///  \date 2014 Aug
///
///  *********************************************

#ifndef __orphan_hpp__
#define __orphan_hpp__


//#include "gambit/Utils/util_types.hpp" // Obsolete dependence?

#include <vector>
#include <string>

namespace Gambit
{
          
  namespace Models
  {  

    namespace PARENT
    {
      // Base lineage that all parentless models copy
      const std::vector<std::string> lineage;
    }
         
  }

}

#endif /* defined(__orphan_hpp__) */
```


-------------------------------

Updated on 2022-09-08 at 03:42:01 +0000
