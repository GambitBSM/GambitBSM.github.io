---
title: 'file Elements/halo_types.hpp'

description: "[No description available]"

---

# Elements/halo_types.hpp



[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |

## Classes

|                | Name           |
| -------------- | -------------- |
| struct | **[Gambit::LocalMaxwellianHalo](/documentation/code/classes/structgambit_1_1localmaxwellianhalo/)**  |
| struct | **[Gambit::GalacticHaloProperties](/documentation/code/classes/structgambit_1_1galactichaloproperties/)**  |

## Detailed Description


**Author**: Sebastian Wild ([sebastian.wild@ph.tum.de](mailto:sebastian.wild@ph.tum.de)) 

**Date**: 2016 Aug

Data types for accessing local and global properties of the distribution of dark matter in the Galaxy.



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Data types for accessing local and global properties of the
///  distribution of dark matter in the Galaxy.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///   
///  \author Sebastian Wild
///          (sebastian.wild@ph.tum.de)
///  \date 2016 Aug
///
///  *********************************************

#ifndef __halo_types_hpp__
#define __halo_types_hpp__

#include <map>
#include <set>

#include "gambit/Utils/standalone_error_handlers.hpp"
#include "gambit/cmake/cmake_variables.hpp"
#include "gambit/Elements/daFunk.hpp"
#include "gambit/Utils/util_types.hpp"

namespace Gambit
{

    // structure describing the local properties of a maxwellian halo
    struct LocalMaxwellianHalo
    {
      double rho0, v0, vesc, vrot;
    };

    // structure describing the density profile of DM in the Milky Way
    struct GalacticHaloProperties
    {
      daFunk::Funk DensityProfile;
      double r_sun;
    };

}


#endif
```


-------------------------------

Updated on 2022-09-07 at 13:49:53 +0000
