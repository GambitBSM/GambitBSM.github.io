---
title: "file Elements/smlike_higgs.hpp"

description: "[No description available]"

---

# file Elements/smlike_higgs.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |

## Detailed Description


**Author**: 

  * Peter Athron ([peter.athron@coepp.org.au](mailto:peter.athron@coepp.org.au)) 
  * Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 


**Date**: 

  * 2017
  * 2017


Helper function to determine which Higgs is most SM-like.



------------------

Authors:



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Helper function to determine which Higgs is
///  most SM-like.
///
///  *********************************************
///
///  Authors:
///  <!-- add name and date if you modify -->
///
///  \author Peter Athron
///          (peter.athron@coepp.org.au)
///  \date 2017
///
///  \author Pat Scott
///          (p.scott@imperial.ac.uk)
///  \date 2017
///
///  *********************************************

#include "gambit/Elements/subspectrum.hpp"

namespace Gambit
{

  /// Determine which MSSM higgs is most SM-like.
  /// Needs expansion to work with non-MSSM (e.g. *HDM) models
  int SMlike_higgs_PDG_code(const SubSpectrum&);

}
```


-------------------------------

Updated on 2022-09-08 at 03:17:36 +0000
