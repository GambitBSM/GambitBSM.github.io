---
title: "file Elements/type_equivalency.hpp"

description: "[No description available]"

---

# file Elements/type_equivalency.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::Utils](/documentation/code/namespaces/namespacegambit_1_1utils/)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| struct | **[Gambit::Utils::type_equivalency](/documentation/code/classes/structgambit_1_1utils_1_1type__equivalency/)** <br>Structure providing type equivalency classes to the dep resolver.  |

## Detailed Description


**Author**: Pat Scott 

 ([patscott@physics.mcgill.ca](mailto:patscott@physics.mcgill.ca)) 

**Date**: 2014 Oct, Dec

Simple container used for storing info about which types have been defined as equivalent for depencency resolution purposes.



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Simple container used for storing info about
///  which types have been defined as equivalent
///  for depencency resolution purposes.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///   
///  \author Pat Scott  
///          (patscott@physics.mcgill.ca)
///  \date 2014 Oct, Dec
///
///  *********************************************

#ifndef __type_equivalency_hpp__
#define __type_equivalency_hpp__

#include <set>
#include <vector>
#include "gambit/Utils/util_types.hpp"

namespace Gambit
{

  namespace Utils
  {

    /// Clean out whitespace and strip Gambit and default BOSSed class namespaces
    str fix_type(str);

    /// Structure providing type equivalency classes to the dep resolver.
    struct type_equivalency
    {
      public:
        /// Define a new equivalency relation
        /// {@
        void add(str,str);
        void add(str,str,str);
        void add(str,str,str,str);
        void add(str,str,str,str,str);
        void add(str,str,str,str,str,str);
        void add(std::vector<str>);
        /// }@
        /// The total set of equivalency classes
        std::set< std::set<str> > equivalency_classes;
        /// Constructor
        type_equivalency();
      private:
        str filename;
    };

  }

}


#endif // defined __type_equivalency_hpp__
```


-------------------------------

Updated on 2022-09-08 at 02:00:52 +0000
