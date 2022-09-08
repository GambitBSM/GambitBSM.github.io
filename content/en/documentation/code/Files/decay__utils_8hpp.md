---
title: "file DecayBit/decay_utils.hpp"

description: "[No description available]"

---

# file DecayBit/decay_utils.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::DecayBit](/documentation/code/namespaces/namespacegambit_1_1decaybit/)**  |

## Detailed Description


**Author**: Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 

**Date**: 2015 May

Function definitions for DecayBit decay utilities.



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Function definitions for DecayBit decay
///  utilities.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///   
///  \author Pat Scott
///          (p.scott@imperial.ac.uk)
///  \date 2015 May
///
///  *********************************************

#include "gambit/Elements/decay_table.hpp"

namespace Gambit
{

  namespace DecayBit
  {
      
    /// Construct a decay table entry for a particle from the entry for its antiparticle
    DecayTable::Entry CP_conjugate(const DecayTable::Entry&);
    
  }

}
```


-------------------------------

Updated on 2022-09-08 at 01:48:58 +0000
