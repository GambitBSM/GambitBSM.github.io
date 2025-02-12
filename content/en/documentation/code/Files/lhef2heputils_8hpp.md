---
title: "file ColliderBit/lhef2heputils.hpp"

description: "[No description available]"

---

# file ColliderBit/lhef2heputils.hpp

[No description available]

## Namespaces

| Name           |
| -------------- |
| **[LHEF](/documentation/code/namespaces/namespacelhef/)** <br>Forward declaration to cut down on includes.  |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::ColliderBit](/documentation/code/namespaces/namespacegambit_1_1colliderbit/)**  |




## Source code

```
// -*- C++ -*-
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///
///  lhef2heputils: a Les Houches Event Format (LHEF)
///  -> HEPUtils::Event MC generator event file
///  converter, based on lhef2hepmc.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Andy Buckley
///  (andy.buckley@cern.ch)
///  \date May 2019
///
///  \author Pat Scott
///  (p.scott@imperial.ac.uk)
///  \date May 2019
///
///  Hat tip: Leif Lonnblad for writing the LHEF
///  parser that actually makes this possible!
///
///  *********************************************

#include "gambit/cmake/cmake_variables.hpp"
#include "gambit/ColliderBit/Utils.hpp"

#ifndef EXCLUDE_HEPMC

#include "HEPUtils/Event.h"

/// Forward declaration to cut down on includes
namespace LHEF { class Reader; }

namespace Gambit
{

  namespace ColliderBit
  {

    /// Extract an LHE event as a HEPUtils::Event
    void get_HEPUtils_event(const LHEF::Reader&, HEPUtils::Event&, double, std::vector<Gambit::ColliderBit::jet_collection_settings>);

  }

}

#endif
```


-------------------------------

Updated on 2025-02-12 at 15:36:42 +0000
