---
title: "file coutprinter/coutprinter/print_overloads.cpp"

description: "[No description available]"

---

# file coutprinter/coutprinter/print_overloads.cpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::Printers](/documentation/code/namespaces/namespacegambit_1_1printers/)** <br>Forward declaration.  |

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[PRINT](/documentation/code/files/coutprinter_2print__overloads_8cpp/#define-print)**(TYPE) <br>Templatable print functions.  |

## Detailed Description


**Author**: Ben Farmer ([b.farmer@imperial.ac.uk](mailto:b.farmer@imperial.ac.uk)) 

**Date**: 2018 Apr

cout interface printer class print function overloads. Add a new overload of the _print function in this file if you want to be able to print a new type.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define PRINT

```
#define PRINT(
    TYPE
)
       _print(TYPE const& value, const std::string& label, const int vID, const uint rank, const ulong pID) \
       { template_print(value,label,vID,rank,pID); }
```

Templatable print functions. 

## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  cout interface printer class print function
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
///  \date 2018 Apr
///
///  *********************************************


#include "gambit/Printers/printers/coutprinter.hpp"
#include "gambit/Printers/printers/common_print_overloads.hpp"

namespace Gambit
{
  namespace Printers
  {

    /// @{ PRINT FUNCTIONS
    /// Need to define one of these for every type we want to print!
    typedef unsigned short int ushort;

    /// Templatable print functions
    #define PRINT(TYPE) _print(TYPE const& value, const std::string& label, const int vID, const uint rank, const ulong pID) \
       { template_print(value,label,vID,rank,pID); }
    void coutPrinter::PRINT(int      )
    void coutPrinter::PRINT(uint     )
    void coutPrinter::PRINT(short    )
    void coutPrinter::PRINT(ushort   )
    void coutPrinter::PRINT(long     )
    void coutPrinter::PRINT(ulong    )
    void coutPrinter::PRINT(longlong )
    void coutPrinter::PRINT(ulonglong)
    void coutPrinter::PRINT(float    )
    void coutPrinter::PRINT(double   )
    void coutPrinter::PRINT(bool     )
    void coutPrinter::PRINT(std::vector<int      >)
    void coutPrinter::PRINT(std::vector<uint     >)
    void coutPrinter::PRINT(std::vector<short    >)
    void coutPrinter::PRINT(std::vector<ushort   >)
    void coutPrinter::PRINT(std::vector<long     >)
    void coutPrinter::PRINT(std::vector<ulong    >)
    void coutPrinter::PRINT(std::vector<longlong >)
    void coutPrinter::PRINT(std::vector<ulonglong>)
    void coutPrinter::PRINT(std::vector<float    >)
    void coutPrinter::PRINT(std::vector<double   >)
    void coutPrinter::PRINT(std::vector<bool     >)
    #undef PRINT

    // Piggyback off existing print functions to build standard overloads
    USE_COMMON_PRINT_OVERLOAD(coutPrinter, map_str_dbl)
    USE_COMMON_PRINT_OVERLOAD(coutPrinter, map_str_str)
    USE_COMMON_PRINT_OVERLOAD(coutPrinter, map_intpair_dbl)
    USE_COMMON_PRINT_OVERLOAD(coutPrinter, ModelParameters)
    USE_COMMON_PRINT_OVERLOAD(coutPrinter, triplet<double>)
    USE_COMMON_PRINT_OVERLOAD(coutPrinter, map_const_str_dbl)
    USE_COMMON_PRINT_OVERLOAD(coutPrinter, map_const_str_map_const_str_dbl)
    USE_COMMON_PRINT_OVERLOAD(coutPrinter, flav_prediction)
    #ifndef SCANNER_STANDALONE
      USE_COMMON_PRINT_OVERLOAD(coutPrinter, DM_nucleon_couplings)
      USE_COMMON_PRINT_OVERLOAD(coutPrinter, BBN_container)
    #endif

    /// @}

  }
}
```


-------------------------------

Updated on 2025-02-12 at 16:10:34 +0000
