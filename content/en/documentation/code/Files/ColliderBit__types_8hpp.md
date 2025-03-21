---
title: "file ColliderBit/ColliderBit_types.hpp"

description: "[No description available]"

---

# file ColliderBit/ColliderBit_types.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::ColliderBit](/documentation/code/namespaces/namespacegambit_1_1colliderbit/)**  |

## Detailed Description


**Author**: 

  * Abram Krislock ([a.m.b.krislock@fys.uio.no](mailto:a.m.b.krislock@fys.uio.no))
  * Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 
  * Tomas Gonzalo ([t.e.gonzalo@fys.uio.no](mailto:t.e.gonzalo@fys.uio.no)) 
  * Anders Kvellestad ([anders.kvellestad@fys.uio.no](mailto:anders.kvellestad@fys.uio.no)) 


**Date**: 

  * 2018 Jan 
  * 2019 Jan, May
  * 2018 Feb
  * 2021 Jun


Type definition header for module ColliderBit.

Compile-time registration of type definitions required for the rest of the code to communicate with ColliderBit.

Add to this if you want to define a new type for the functions in ColliderBit to return, but you don't expect that type to be needed by any other modules.



------------------

Authors (add name if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Type definition header for module
///  ColliderBit.
///
///  Compile-time registration of type definitions
///  required for the rest of the code to
///  communicate with ColliderBit.
///
///  Add to this if you want to define a new type
///  for the functions in ColliderBit to return,
///  but you don't expect that type to be needed
///  by any other modules.
///
///  *********************************************
///
///  Authors (add name if you modify):
///
///  \author Abram Krislock
///          (a.m.b.krislock@fys.uio.no)
///
///  \author Pat Scott
///          (p.scott@imperial.ac.uk)
///  \date 2018 Jan
///  \date 2019 Jan, May
///
///  \author Tomas Gonzalo
///          (t.e.gonzalo@fys.uio.no)
///  \date 2018 Feb
///
///  \author Anders Kvellestad
///          (anders.kvellestad@fys.uio.no)
///  \date 2021 Jun
///
///  *********************************************


#ifndef __ColliderBit_types_hpp__
#define __ColliderBit_types_hpp__

#include <vector>
#include <chrono>

#include "gambit/Utils/PID_pair.hpp"
#include "gambit/ColliderBit/MCLoopInfo.hpp"
#include "gambit/ColliderBit/MC_convergence.hpp"
#include "gambit/ColliderBit/xsec.hpp"
#include "gambit/ColliderBit/colliders/Pythia8/Py8Collider.hpp"
#include "gambit/ColliderBit/colliders/Pythia8/Py8Collider_typedefs.hpp"
#include "gambit/ColliderBit/detectors/BuckFast.hpp"
#include "gambit/ColliderBit/analyses/AnalysisContainer.hpp"
#include "gambit/ColliderBit/analyses/AnalysisData.hpp"
#include "gambit/ColliderBit/analyses/AnalysisLogLikes.hpp"

#include "gambit/ColliderBit/limits/ALEPHSleptonLimits.hpp"
#include "gambit/ColliderBit/limits/L3GauginoLimits.hpp"
#include "gambit/ColliderBit/limits/L3SleptonLimits.hpp"
#include "gambit/ColliderBit/limits/OPALGauginoLimits.hpp"
#include "gambit/ColliderBit/limits/OPALDegenerateCharginoLimits.hpp"
/// TODO: see if we can use this one:
//#include "gambit/ColliderBit/limits/L3SmallDeltaMGauginoLimits.hpp"

#include "HEPUtils/Event.h"

namespace Gambit
{

  namespace ColliderBit
  {

    /// @brief Container for data from multiple analyses and SRs
    typedef std::vector<AnalysisData*> AnalysisDataPointers;

    /// @brief Typedef for a string-to-AnalysisLogLikes map
    typedef std::map<std::string,AnalysisLogLikes> map_str_AnalysisLogLikes;

    /// @brief Container for multiple analysis containers
    typedef std::vector<AnalysisContainer> AnalysisContainers;

    typedef std::chrono::milliseconds ms;
    typedef std::chrono::steady_clock steady_clock;
    typedef std::chrono::steady_clock::time_point tp;
    typedef std::map<std::string,double> timer_map_type;

    /// @brief Typedef for a str-SLHAstruct pair, to pass around SLHA filenames + content
    typedef std::pair<std::string,SLHAstruct> pair_str_SLHAstruct;

    /// @brief Typedefs related to cross-sections 
    // Note: 
    // The 'iipair' name below refers to the typedef std::pair<int,int> iipair 
    // declared in Utils/include/gambit/Utils/util_types.hpp

    typedef std::vector<std::pair<int,int>> vec_iipair;
    typedef std::vector<PID_pair> vec_PID_pair;

    typedef std::multimap<int,std::pair<int,int>> multimap_int_iipair;
    typedef std::multimap<int,PID_pair> multimap_int_PID_pair;

    typedef std::multimap<PID_pair,int> multimap_PID_pair_int;

    typedef std::map<int,xsec_container> map_int_xsec;
    typedef std::map<int,process_xsec_container> map_int_process_xsec;

    typedef std::map<std::pair<int,int>,PID_pair_xsec_container> map_iipair_PID_pair_xsec;
    typedef std::map<PID_pair,PID_pair_xsec_container> map_PID_pair_PID_pair_xsec;

    /// @brief Typedef for a std::function that sets the weight for the input HEPUtils::Event
    typedef HEPUtils::Event HEPUtils_Event;  // Extra typedef to avoid macro problem with namespaces
    typedef std::function<void(HEPUtils_Event&, const BaseCollider*)> EventWeighterFunctionType;
  }
}



#endif /* defined __ColliderBit_types_hpp__ */
```


-------------------------------

Updated on 2025-02-12 at 16:10:35 +0000
