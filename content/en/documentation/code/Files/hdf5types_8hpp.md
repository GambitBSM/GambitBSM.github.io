---
title: "file printers/hdf5types.hpp"

description: "[No description available]"

---

# file printers/hdf5types.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[HDF5_TYPES](/documentation/code/files/hdf5types_8hpp/#define-hdf5-types)**  |
|  | **[HDF5_RETRIEVABLE_TYPES](/documentation/code/files/hdf5types_8hpp/#define-hdf5-retrievable-types)**  |
|  | **[HDF5_BACKEND_TYPES](/documentation/code/files/hdf5types_8hpp/#define-hdf5-backend-types)**  |

## Detailed Description


**Author**: 

  * Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 
  * Ben Farmer ([b.farmer@imperial.ac.uk](mailto:b.farmer@imperial.ac.uk)) 


**Date**: 

  * 2017 Mar
  * 2019 Nov


Sequence of all types printable by the HDF5 printer.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define HDF5_TYPES

```
#define HDF5_TYPES   (int)                                \
  (uint)                               \
  (long)                               \
  (ulong)                              \
  (longlong)                           \
  (ulonglong)                          \
  (float)                              \
  (double)                             \
  (std::vector<double>)                \
  (bool)                               \
  (map_str_dbl)                        \
  (map_str_str)                        \
  (map_str_map_str_dbl)                \
  (map_const_str_dbl)                  \
  (map_const_str_map_const_str_dbl)    \
  (ModelParameters)                    \
  (triplet<double>)                    \
  (map_intpair_dbl)                    \
  (flav_prediction)                    \
```


### define HDF5_RETRIEVABLE_TYPES

```
#define HDF5_RETRIEVABLE_TYPES   HDF5_TYPES \
  (MSSM_SLHAstruct) \
  (SMslha_SLHAstruct)
```


### define HDF5_BACKEND_TYPES

```
#define HDF5_BACKEND_TYPES   (DM_nucleon_couplings)               \
  (BBN_container)                      \
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
///  \author Pat Scott
///          (p.scott@imperial.ac.uk)
///  \date 2017 Mar
///
///  \author Ben Farmer
///          (b.farmer@imperial.ac.uk)
///  \date 2019 Nov
///
///  *********************************************

#ifndef __HDF5TYPES__
#define __HDF5TYPES__

#include "gambit/Elements/module_types_rollcall.hpp"

#define HDF5_TYPES                     \
  (int)                                \
  (uint)                               \
  (long)                               \
  (ulong)                              \
  (longlong)                           \
  (ulonglong)                          \
  (float)                              \
  (double)                             \
  (std::vector<double>)                \
  (bool)                               \
  (map_str_dbl)                        \
  (map_str_str)                        \
  (map_str_map_str_dbl)                \
  (map_const_str_dbl)                  \
  (map_const_str_map_const_str_dbl)    \
  (ModelParameters)                    \
  (triplet<double>)                    \
  (map_intpair_dbl)                    \
  (flav_prediction)                    \

#define HDF5_RETRIEVABLE_TYPES \
  HDF5_TYPES \
  (MSSM_SLHAstruct) \
  (SMslha_SLHAstruct)

#define HDF5_BACKEND_TYPES             \
  (DM_nucleon_couplings)               \
  (BBN_container)                      \

#endif
```


-------------------------------

Updated on 2024-07-18 at 13:53:33 +0000
