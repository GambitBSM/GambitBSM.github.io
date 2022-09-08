---
title: "file sqliteprinter/sqliteprinter/print_overloads.cpp"

description: "[No description available]"

---

# file sqliteprinter/sqliteprinter/print_overloads.cpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::Printers](/documentation/code/namespaces/namespacegambit_1_1printers/)** <br>Forward declaration.  |

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[PRINT](/documentation/code/files/sqliteprinter_2print__overloads_8cpp/#define-print)**(TYPE, SQLTYPE) <br>Templatable print functions.  |

## Detailed Description


**Author**: Ben Farmer ([b.farmer@imperial.ac.uk](mailto:b.farmer@imperial.ac.uk)) 

**Date**: 2018 Dec

SQLite interface printer class print function overloads. Add a new overload of the _print function in this file if you want to be able to print a new type.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define PRINT

```
#define PRINT(
    TYPE,
    SQLTYPE
)
       _print(TYPE const& value, const std::string& label, const int vID, const uint rank, const ulong pID) \
       { template_print(value,label,vID,rank,pID,SQLTYPE); }
```

Templatable print functions. 

PRINT FUNCTIONS Need to define one of these for every type we want to print! 


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  SQLite interface printer class print function
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
///  \date 2018 Dec
///
///  *********************************************


#include "gambit/Printers/printers/sqliteprinter.hpp"
#include "gambit/Printers/printers/common_print_overloads.hpp"

namespace Gambit
{
  namespace Printers
  {

    /// @{ PRINT FUNCTIONS
    /// Need to define one of these for every type we want to print!

    /// Templatable print functions
    #define PRINT(TYPE,SQLTYPE) _print(TYPE const& value, const std::string& label, const int vID, const uint rank, const ulong pID) \
       { template_print(value,label,vID,rank,pID,SQLTYPE); }
    void SQLitePrinter::PRINT(bool     ,"INTEGER")
    void SQLitePrinter::PRINT(int      ,"INTEGER")
    void SQLitePrinter::PRINT(uint     ,"INTEGER")
    void SQLitePrinter::PRINT(long     ,"INTEGER")
    void SQLitePrinter::PRINT(ulong    ,"INTEGER")
    void SQLitePrinter::PRINT(longlong ,"INTEGER")
    void SQLitePrinter::PRINT(ulonglong,"INTEGER")
    void SQLitePrinter::PRINT(float    ,"REAL")
    void SQLitePrinter::PRINT(double   ,"REAL")
    #undef PRINT

    // Piggyback off existing print functions to build standard overloads
    USE_COMMON_PRINT_OVERLOAD(SQLitePrinter, std::vector<double>)
    USE_COMMON_PRINT_OVERLOAD(SQLitePrinter, map_str_dbl)
    USE_COMMON_PRINT_OVERLOAD(SQLitePrinter, map_intpair_dbl)
    USE_COMMON_PRINT_OVERLOAD(SQLitePrinter, ModelParameters)
    USE_COMMON_PRINT_OVERLOAD(SQLitePrinter, triplet<double>)
    #ifndef SCANNER_STANDALONE
      USE_COMMON_PRINT_OVERLOAD(SQLitePrinter, DM_nucleon_couplings)
      USE_COMMON_PRINT_OVERLOAD(SQLitePrinter, BBN_container)
    #endif

    /// @}

  }
}
```


-------------------------------

Updated on 2022-09-08 at 00:43:04 +0000
