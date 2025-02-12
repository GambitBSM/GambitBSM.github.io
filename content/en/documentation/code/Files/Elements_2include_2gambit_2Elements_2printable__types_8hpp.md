---
title: "file Elements/Elements/include/gambit/Elements/printable_types.hpp"

description: "[No description available]"

---

# file Elements/Elements/include/gambit/Elements/printable_types.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[PRINTABLE_TYPES](/documentation/code/files/elements_2include_2gambit_2elements_2printable__types_8hpp/#define-printable-types)**  |
|  | **[RETRIEVABLE_TYPES](/documentation/code/files/elements_2include_2gambit_2elements_2printable__types_8hpp/#define-retrievable-types)**  |

## Detailed Description


**Author**: Ben Farmer ([benjamin.farmer@fysik.su.se](mailto:benjamin.farmer@fysik.su.se)) 

**Date**: 2016 Jan

List of types printable by GAMBIT printers. Make sure to manually update this list when you want to add a new printable type.



------------------

Authors:



------------------




## Macros Documentation

### define PRINTABLE_TYPES

```
#define PRINTABLE_TYPES   SCANNER_PRINTABLE_TYPES             \
  (map_const_str_dbl)                 \
  (map_str_map_str_dbl)               \
  (map_const_str_map_const_str_dbl)   \
  (map_intpair_dbl)                   \
  (triplet<double>)                   \
  (flav_prediction)                   \
  (DM_nucleon_couplings)              \
  (BBN_container)
```


### define RETRIEVABLE_TYPES

```
#define RETRIEVABLE_TYPES   PRINTABLE_TYPES \
  (MSSM_SLHAstruct) \
  (SMslha_SLHAstruct)
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  List of types printable by GAMBIT printers.
///  Make sure to manually update this list
///  when you want to add a new printable type.
///
///  *********************************************
///
///  Authors:
///
///  \author Ben Farmer
///          (benjamin.farmer@fysik.su.se)
///  \date 2016 Jan
///
///  *********************************************

#ifndef __printable_types_hpp__
#define __printable_types_hpp__

#include "gambit/Elements/types_rollcall.hpp"
#include "gambit/ScannerBit/printable_types.hpp"

// Types that Gambit printers can output (if printer plugin is properly equipped)
#define PRINTABLE_TYPES               \
  SCANNER_PRINTABLE_TYPES             \
  (map_const_str_dbl)                 \
  (map_str_map_str_dbl)               \
  (map_const_str_map_const_str_dbl)   \
  (map_intpair_dbl)                   \
  (triplet<double>)                   \
  (flav_prediction)                   \
  (DM_nucleon_couplings)              \
  (BBN_container)

// Types that can be retrieved from Gambit printer output (if printer plugin is properly equipped)
// Generally needs to be the same as the printable types, i.e. should be able to retrieve everything.
#define RETRIEVABLE_TYPES \
  PRINTABLE_TYPES \
  (MSSM_SLHAstruct) \
  (SMslha_SLHAstruct)

#endif // defined __printable_types_hpp__
```


-------------------------------

Updated on 2025-02-12 at 15:36:41 +0000
