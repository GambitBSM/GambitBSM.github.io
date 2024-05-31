---
title: "file printers/asciitypes.hpp"

description: "[No description available]"

---

# file printers/asciitypes.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[ASCII_TYPES](/documentation/code/files/asciitypes_8hpp/#define-ascii-types)**  |
|  | **[ASCII_BACKEND_TYPES](/documentation/code/files/asciitypes_8hpp/#define-ascii-backend-types)**  |

## Detailed Description


**Author**: Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 

**Date**: 2017 Mar

Sequence of all types printable by the ASCII printer.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define ASCII_TYPES

```
#define ASCII_TYPES   SCANNER_PRINTABLE_TYPES                   \
  (std::string)                             \
  (triplet<double>)                         \
  (map_intpair_dbl)                         \
  (map_const_str_dbl)                       \
  (map_const_str_map_const_str_dbl)         \
  (flav_prediction)                         \
```


### define ASCII_BACKEND_TYPES

```
#define ASCII_BACKEND_TYPES   (DM_nucleon_couplings)                    \
  (BBN_container)                           \
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Sequence of all types printable by the ASCII
///  printer.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Pat Scott
///          (p.scott@imperial.ac.uk)
///  \date 2017 Mar
///
///  *********************************************

#ifndef __ASCIITYPES__
#define __ASCIITYPES__

#include "gambit/ScannerBit/printable_types.hpp"

#define ASCII_TYPES                         \
  SCANNER_PRINTABLE_TYPES                   \
  (std::string)                             \
  (triplet<double>)                         \
  (map_intpair_dbl)                         \
  (map_const_str_dbl)                       \
  (map_const_str_map_const_str_dbl)         \
  (flav_prediction)                         \


#define ASCII_BACKEND_TYPES                 \
  (DM_nucleon_couplings)                    \
  (BBN_container)                           \

#endif
```


-------------------------------

Updated on 2024-05-31 at 15:12:05 +0000
