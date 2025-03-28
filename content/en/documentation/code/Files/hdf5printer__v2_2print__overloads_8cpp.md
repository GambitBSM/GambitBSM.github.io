---
title: "file hdf5printer_v2/hdf5printer_v2/print_overloads.cpp"

description: "[No description available]"

---

# file hdf5printer_v2/hdf5printer_v2/print_overloads.cpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::Printers](/documentation/code/namespaces/namespacegambit_1_1printers/)** <br>Forward declaration.  |

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[PRINT](/documentation/code/files/hdf5printer__v2_2print__overloads_8cpp/#define-print)**(TYPE) <br>Simple print functions.  |
|  | **[PRINTAS](/documentation/code/files/hdf5printer__v2_2print__overloads_8cpp/#define-printas)**(INTYPE, OUTTYPE)  |

## Detailed Description


**Author**: 

  * Ben Farmer ([b.farmer@imperial.ac.uk](mailto:b.farmer@imperial.ac.uk)) 
  * Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 


**Date**: 

  * 2015 May, 2019 Jan
  * 2017 March


HDF5Printer print function overloads. Add a new overload of the _print function in this file if you want to be able to print a new type.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define PRINT

```
#define PRINT(
    TYPE
)
       _print(TYPE const& value, const std::string& label, const int /*vID*/, const uint rank, const ulong pID) \
       { basic_print(value,label,rank,pID); }
```

Simple print functions. 

PRINT FUNCTIONS Need to define one of these for every type we want to print! 


### define PRINTAS

```
#define PRINTAS(
    INTYPE,
    OUTTYPE
)
    _print(INTYPE const& value, const std::string& label, const int vID, const uint rank, const ulong pID) \
    { _print((OUTTYPE)value,label,vID,rank,pID); }
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  HDF5Printer print function
///  overloads.  Add a new overload of the _print
///  function in this file if you want to be able
///  to print a new type.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Ben Farmer
///          (b.farmer@imperial.ac.uk)
///  \date 2015 May, 2019 Jan
///
///  \author Pat Scott
///          (p.scott@imperial.ac.uk)
///  \date 2017 March
///
///  *********************************************

#include "gambit/Printers/printers/hdf5printer_v2.hpp"
#include "gambit/Printers/printers/common_print_overloads.hpp"

namespace Gambit
{
  namespace Printers
  {

    /// @{ PRINT FUNCTIONS
    /// Need to define one of these for every type we want to print!

    /// Simple print functions
    #define PRINT(TYPE) _print(TYPE const& value, const std::string& label, const int /*vID*/, const uint rank, const ulong pID) \
       { basic_print(value,label,rank,pID); }
    void HDF5Printer2::PRINT(int)
    void HDF5Printer2::PRINT(uint)
    void HDF5Printer2::PRINT(long)
    void HDF5Printer2::PRINT(ulong)
    void HDF5Printer2::PRINT(float)
    void HDF5Printer2::PRINT(double)
    #undef PRINT

    // longlongs can lead to ambiguity problems matching C++ to HDF5 types, since they are sometimes the same as longs. So just stick
    // with longs in the printer, they are long enough
    #define PRINTAS(INTYPE,OUTTYPE) _print(INTYPE const& value, const std::string& label, const int vID, const uint rank, const ulong pID) \
    { _print((OUTTYPE)value,label,vID,rank,pID); }
    void HDF5Printer2::PRINTAS(longlong, long)
    void HDF5Printer2::PRINTAS(ulonglong, ulong)
    #undef PRINTAS

    /// Bools can't quite use the template print function directly, since there
    /// are some issues with bools and MPI/HDF5 types. Easier to just convert
    /// the bool to an int first.
    void HDF5Printer2::_print(bool const& value, const std::string& label, const int vID, const unsigned int mpirank, const unsigned long pointID)
    {
      unsigned int val_as_uint = value;
      _print(val_as_uint,label,vID,mpirank,pointID);
    }

    // Piggyback off existing print functions to build standard overloads
    USE_COMMON_PRINT_OVERLOAD(HDF5Printer2, std::vector<double>)
    USE_COMMON_PRINT_OVERLOAD(HDF5Printer2, map_str_dbl)
    USE_COMMON_PRINT_OVERLOAD(HDF5Printer2, map_str_str)
    USE_COMMON_PRINT_OVERLOAD(HDF5Printer2, map_const_str_dbl)
    USE_COMMON_PRINT_OVERLOAD(HDF5Printer2, map_str_map_str_dbl)
    USE_COMMON_PRINT_OVERLOAD(HDF5Printer2, map_const_str_map_const_str_dbl)
    USE_COMMON_PRINT_OVERLOAD(HDF5Printer2, map_intpair_dbl)
    USE_COMMON_PRINT_OVERLOAD(HDF5Printer2, ModelParameters)
    USE_COMMON_PRINT_OVERLOAD(HDF5Printer2, triplet<double>)
    USE_COMMON_PRINT_OVERLOAD(HDF5Printer2, flav_prediction)
    #ifndef SCANNER_STANDALONE
      USE_COMMON_PRINT_OVERLOAD(HDF5Printer2, DM_nucleon_couplings)
      USE_COMMON_PRINT_OVERLOAD(HDF5Printer2, BBN_container)
    #endif

    /// @}

  }
}
```


-------------------------------

Updated on 2025-02-12 at 16:10:34 +0000
