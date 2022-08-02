---
title: 'file DecayBit/decay_utils.hpp'

description: "[No description available]"

---






[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/colliderbit_development/namespaces/namespacegambit/)** <br>Simulation of "Search for photonic signatures of gauge-mediated supersymmetry in 13 TeV pp collisions with the ATLAS detector".  |
| **[Gambit::DecayBit](/documentation/code/colliderbit_development/namespaces/namespacegambit_1_1decaybit/)**  |

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

#include "gambit/Elements/decay_table.hpp"

namespace Gambit
{

  namespace DecayBit
  {
      
    DecayTable::Entry CP_conjugate(const DecayTable::Entry&);
    
  }

}
```


-------------------------------

Updated on 2022-08-02 at 18:18:37 +0000