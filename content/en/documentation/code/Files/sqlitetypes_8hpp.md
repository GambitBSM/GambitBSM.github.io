---
title: "file printers/sqlitetypes.hpp"

description: "[No description available]"

---

# file printers/sqlitetypes.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[SQL_TYPES](/documentation/code/files/sqlitetypes_8hpp/#define-sql-types)**  |
|  | **[SQL_BACKEND_TYPES](/documentation/code/files/sqlitetypes_8hpp/#define-sql-backend-types)**  |

## Detailed Description


**Author**: Ben Farmer ([b.farmer@imperial.ac.uk](mailto:b.farmer@imperial.ac.uk)) 

**Date**: 2018 Dec

Sequence of all types printable by the HDF5 printer.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define SQL_TYPES

```
#define SQL_TYPES   (int)                     \
  (uint)                    \
  (long)                    \
  (ulong)                   \
  (longlong)                \
  (ulonglong)               \
  (float)                   \
  (double)                  \
  (std::vector<double>)     \
  (bool)                    \
  (map_str_dbl)             \
  (ModelParameters)         \
  (triplet<double>)         \
  (map_intpair_dbl)         \
```


### define SQL_BACKEND_TYPES

```
#define SQL_BACKEND_TYPES   (DM_nucleon_couplings)              \
  (BBN_container)                     \
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Sequence of all types printable by the HDF5
///  printer.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Ben Farmer
///          (b.farmer@imperial.ac.uk)
///  \date 2018 Dec
///
///  *********************************************

#ifndef __SQLITETYPES__
#define __SQLITETYPES__

#define SQL_TYPES           \
  (int)                     \
  (uint)                    \
  (long)                    \
  (ulong)                   \
  (longlong)                \
  (ulonglong)               \
  (float)                   \
  (double)                  \
  (std::vector<double>)     \
  (bool)                    \
  (map_str_dbl)             \
  (ModelParameters)         \
  (triplet<double>)         \
  (map_intpair_dbl)         \


#define SQL_BACKEND_TYPES             \
  (DM_nucleon_couplings)              \
  (BBN_container)                     \


#endif
```


-------------------------------

Updated on 2022-09-08 at 00:43:03 +0000
