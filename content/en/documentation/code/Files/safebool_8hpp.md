---
title: "file Utils/safebool.hpp"

description: "[No description available]"

---

# file Utils/safebool.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Gambit::SafeBool](/documentation/code/classes/classgambit_1_1safebool/)**  |

## Detailed Description


**Author**: 

  * Ben Farmer ([benjamin.farmer@fysik.su.se](mailto:benjamin.farmer@fysik.su.se)) 
  * Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 


**Date**: 

  * 2015 Oct
  * 2019 Mar


A replacement type for 'bool' which does not allow automatic conversion to/from 'int' etc.

Doesn't do fancy stuff like allow comparisons, but can use as the condition in 'if' statements, and supports automatic conversion to (but not from) bool.

Currently used in the SubSpectrum class to resolve overload ambiguities between int and bool arguments due to automatic conversions.



------------------

Authors:



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  A replacement type for 'bool' which does not
///  allow automatic conversion to/from 'int' etc.
///
///  Doesn't do fancy stuff like allow comparisons,
///  but can use as the condition in 'if'
///  statements, and supports automatic conversion
///  to (but not from) bool.
///
///  Currently used in the SubSpectrum class to
///  resolve overload ambiguities between int and
///  bool arguments due to automatic conversions.
///
///  *********************************************
///
///  Authors:
///  <!-- add name and date if you modify -->
///
///  \author Ben Farmer
///          (benjamin.farmer@fysik.su.se)
///  \date 2015 Oct
///
///  \author Pat Scott
///          (p.scott@imperial.ac.uk)
///  \date 2019 Mar
///
///  *********************************************

#pragma once

namespace Gambit
{

  class SafeBool
  {
    bool _ok;
    public:
      explicit SafeBool(bool ok): _ok(ok) {}
      explicit operator bool() const { return _ok; }
  };

}
```


-------------------------------

Updated on 2022-09-08 at 00:43:02 +0000
