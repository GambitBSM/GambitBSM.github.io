---
title: "file Elements/virtual_higgs.hpp"

description: "[No description available]"

---

# file Elements/virtual_higgs.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |

## Detailed Description


**Author**: 

  * Christoph Weniger [c.weniger@uva.nl](mailto:c.weniger@uva.nl)
  * Pat Scott [p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)


**Date**: 

  * Dec 2014
  * 2015 May


Simple function for returning SM Higgs partial and total widths as a function of virtuality, as read from data files from CERN Yellow Paper arXiv:1101.0593.



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Simple function for returning SM Higgs partial
///  and total widths as a function of virtuality,
///  as read from data files from CERN Yellow 
///  Paper arXiv:1101.0593.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Christoph Weniger
///          <c.weniger@uva.nl>
///  \date Dec 2014
///
///  \author Pat Scott
///          <p.scott@imperial.ac.uk>
///  \date 2015 May
///
///  *********************************************


#include "gambit/cmake/cmake_variables.hpp"
#include "gambit/Elements/daFunk.hpp"
#include "gambit/Utils/util_types.hpp"

namespace Gambit
{
  
  /// Higgs branching ratios and total width Gamma [GeV], as function of mass [GeV] (90 - 300 GeV)
  double virtual_SMHiggs_widths(str, double);
  
}
```


-------------------------------

Updated on 2022-09-08 at 03:17:36 +0000
