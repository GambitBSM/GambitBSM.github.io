---
title: "file src/stream_overloads.cpp"

description: "[No description available]"

---

# file src/stream_overloads.cpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |

## Detailed Description


**Author**: 

  * Pat Scott ([patscott@physics.mcgill.ca](mailto:patscott@physics.mcgill.ca)) 
  * Ben Farmer ([benjamin.farmer@monash.edu](mailto:benjamin.farmer@monash.edu)) 


**Date**: 

  * 2013 Jan, Dec
  * 2013 Jun, 2016, Jan


Define overloadings of the stream operator for various containers. (Should really be templated eventually)



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Define overloadings of the stream operator for
///  various containers.
///  (Should really be templated eventually)
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Pat Scott
///          (patscott@physics.mcgill.ca)
///  \date 2013 Jan, Dec
///
///  \author Ben Farmer
///          (benjamin.farmer@monash.edu)
///  \date 2013 Jun, 2016, Jan
///
///  *********************************************

#include "gambit/Utils/stream_overloads.hpp"

namespace Gambit
{

  /// Spacing utility for stream overloads
  std::string spacing(int len, int maxlen)
  {
    int offset = 0;
    if (len < maxlen) {offset=maxlen-len;}
    return std::string(offset+5,' ');
  }

}
```


-------------------------------

Updated on 2022-09-08 at 03:08:04 +0000
