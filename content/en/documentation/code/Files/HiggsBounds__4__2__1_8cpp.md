---
title: "file frontends/HiggsBounds_4_2_1.cpp"

description: "[No description available]"

---

# file frontends/HiggsBounds_4_2_1.cpp

[No description available]

## Functions

|                | Name           |
| -------------- | -------------- |
| | **[if](/documentation/code/files/higgsbounds__4__2__1_8cpp/#function-if)**(scan_level ) |

## Attributes

|                | Name           |
| -------------- | -------------- |
| | **[BE_INI_FUNCTION](/documentation/code/files/higgsbounds__4__2__1_8cpp/#variable-be-ini-function)**  |


## Functions Documentation

### function if

```
if(
    scan_level 
)
```



## Attributes Documentation

### variable BE_INI_FUNCTION

```
BE_INI_FUNCTION {

  
  static bool scan_level = true;
```



## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file HiggsBounds.cpp
///
///  Frontend source for the HiggsBounds backend.
///
///  Actual implementation of HiggsBounds ini function.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Christopher S. Rogan
///          (crogan@cern.ch)
///  \date 2015 Sept
///
///  \author Pat Scott
///          (p.scott@imperial.ac.uk)
///  \date 2016 Feb
///
///  *********************************************

#include "gambit/Backends/frontend_macros.hpp"
#include "gambit/Backends/frontends/HiggsBounds_4_2_1.hpp"
#include "gambit/Utils/file_lock.hpp"

BE_INI_FUNCTION
{

  // Scan-level initialisation
  static bool scan_level = true;
  if(scan_level)
  {
    int nHneut = 3; // number of neutral higgses
    int nHplus = 1; // number of charged higgses
    int ANA = 1;    // indicates LEP-only analysis
    // Initialize HiggsBounds. Do this one-by-one for each MPI process with
    // locks, as HB writes files here then reads them back in later (crazy).
    Utils::ProcessLock mylock("HiggsBounds_" STRINGIFY(SAFE_VERSION) "_init");
    mylock.get_lock();
    // --braces just for dramatic effect--
    {
      // initialize LEP chisq tables
      initialize_HiggsBounds_chisqtables();
      // initialize HiggsBounds to LEP only
      initialize_HiggsBounds_int(nHneut,nHplus,ANA);
    }
    mylock.release_lock();
    scan_level = false;
  }

}
END_BE_INI_FUNCTION
```


-------------------------------

Updated on 2025-02-12 at 16:10:36 +0000
