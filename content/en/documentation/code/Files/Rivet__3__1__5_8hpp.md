---
title: "file frontends/Rivet_3_1_5.hpp"

description: "[No description available]"

---

# file frontends/Rivet_3_1_5.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::Backends](/documentation/code/namespaces/namespacegambit_1_1backends/)**  |
| **[Gambit::Backends::Rivet_3_1_5](/documentation/code/namespaces/namespacegambit_1_1backends_1_1rivet__3__1__5/)**  |
| **[Gambit::Backends::Rivet_3_1_5::Rivet](/documentation/code/namespaces/namespacegambit_1_1backends_1_1rivet__3__1__5_1_1rivet/)**  |

## Detailed Description


**Author**: The GAMBIT Collaboration

Frontend header generated by BOSS for GAMBIT backend Rivet 3.1.5.



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Frontend header generated by BOSS for GAMBIT backend Rivet 3.1.5.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author The GAMBIT Collaboration
///
///  *********************************************

#ifndef EXCLUDE_YODA
#ifndef EXCLUDE_HEPMC

#include "gambit/Backends/backend_types/Rivet_3_1_5/identification.hpp"

LOAD_LIBRARY

namespace Gambit
{
   namespace Backends
   {
      namespace Rivet_3_1_5
      {
         namespace Rivet
         {
            typedef ::Rivet_3_1_5::Rivet::AnalysisHandler AnalysisHandler;
         }
      }
   }
}

// Functions
BE_FUNCTION(addAnalysisLibPath, void, (const std::string&), ("addAnalysisLibPath__BOSS_3","_addAnalysisLibPath__BOSS_3"), "addAnalysisLibPath")
// Variables

// Initialisation function (dependencies)

// Convenience functions (registration)


// Convenience functions (definitions)

// End
#include "gambit/Backends/backend_undefs.hpp"
 
#endif
#endif
```


-------------------------------

Updated on 2025-02-12 at 16:10:36 +0000
