---
title: "file detectors/BuckFast.cpp"

description: "[No description available]"

---

# file detectors/BuckFast.cpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::ColliderBit](/documentation/code/namespaces/namespacegambit_1_1colliderbit/)**  |

## Detailed Description


**Author**: 

  * Andy Buckley 
  * Abram Krislock 
  * Anders Kvellestad 
  * Pat Scott 
  * Martin White


BuckFast smearing functions.



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//  *********************************************
///  \file
///
///  BuckFast smearing functions.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Andy Buckley
///  \author Abram Krislock
///  \author Anders Kvellestad
///  \author Pat Scott
///  \author Martin White
///
///  *********************************************

#include "gambit/ColliderBit/detectors/BuckFast.hpp"

namespace Gambit
{

  namespace ColliderBit
  {

    /// Process an event with BuckFast
    void BuckFast::processEvent(HEPUtils::Event& event) const
    {
      // Electron smearing
      /// @todo Run-dependence?
      if (smearElectronEnergy != NULL) smearElectronEnergy(event.electrons());

      // Muon smearing
      /// @todo Run-dependence?
      if (smearMuonMomentum != NULL) smearMuonMomentum(event.muons());

      // Smear taus
      if (smearTaus != NULL) smearTaus(event.taus());

      // Smear jet momenta
      if (smearJets != NULL) smearJets(event.jets());

      // Unset b-tags outside |eta|=2.5
      for (HEPUtils::Jet* j : event.jets())
      {
        if (j->abseta() > 2.5) j->set_btag(false);
      }
    }

  }

}
```


-------------------------------

Updated on 2022-09-07 at 23:22:11 +0000
