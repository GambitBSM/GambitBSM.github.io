---
title: "file diver_1.3.0/diver_1.3.0/diver.hpp"

description: "[No description available]"

---

# file diver_1.3.0/diver_1.3.0/diver.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::Diver_1_3_0](/documentation/code/namespaces/namespacegambit_1_1diver__1__3__0/)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| struct | **[Gambit::Diver_1_3_0::diverScanData](/documentation/code/classes/structgambit_1_1diver__1__3__0_1_1diverscandata/)** <br>Structure for passing likelihood and printer data through Diver to the objective function.  |

## Functions

|                | Name           |
| -------------- | -------------- |
| double | **[cdiver](/documentation/code/files/diver__1_83_80_2diver_8hpp/#function-cdiver)**(double(*)(double[], const int, int &, bool &, const bool, void *&) , int , const double [], const double [], const char [], int , double [], double [], int , const int [], bool , int , int , int , const double [], double , double , bool , bool , int , bool , bool , double , int , bool , int , bool , bool , bool , bool , int , int , const double [], bool , int , double , int , void *& , int ) |

## Detailed Description


**Author**: Pat Scott ([patrickcolinscott@gmail.com](mailto:patrickcolinscott@gmail.com)) 

**Date**: 2025 Apr

ScannerBit interface to Diver 1.3.0

Header file



------------------

Authors (add name and date if you modify):



------------------


## Functions Documentation

### function cdiver

```
double cdiver(
    double(*)(double[], const int, int &, bool &, const bool, void *&) ,
    int ,
    const double [],
    const double [],
    const char [],
    int ,
    double [],
    double [],
    int ,
    const int [],
    bool ,
    int ,
    int ,
    int ,
    const double [],
    double ,
    double ,
    bool ,
    bool ,
    int ,
    bool ,
    bool ,
    double ,
    int ,
    bool ,
    int ,
    bool ,
    bool ,
    bool ,
    bool ,
    int ,
    int ,
    const double [],
    bool ,
    int ,
    double ,
    int ,
    void *& ,
    int 
)
```




## Source code

```
//  GAMBIT: Global and Modular BSM Inference Tool
//  *********************************************
///  \file
///
///  ScannerBit interface to Diver 1.3.0
///
///  Header file
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Pat Scott
///          (patrickcolinscott@gmail.com)
///  \date 2025 Apr
///
///  *********************************************

#pragma once

#include "gambit/ScannerBit/scanner_plugin.hpp"

// C++ prototype of the main run_de function for Diver.
extern "C" double cdiver(double (*)(double[], const int, int&, bool&, const bool, void*&), int, const double[], const double[],
           const char[], int, double[], double[], int, const int[], bool, int, int, int, const double[], double, double, bool,
           bool, int, bool, bool, double, int, bool, int, bool, bool, bool, bool, int, int, const double[], bool, int, double, int,
           void*&, int);

namespace Gambit
{

  namespace Diver_1_3_0
  {

    /// Structure for passing likelihood and printer data through Diver to the objective function.
    struct diverScanData
    {
      Scanner::like_ptr likelihood_function;
      Scanner::printer_interface* printer;
    };

    /// Function to be minimised by Diver
    double objective(double params[], const int param_dim, int &fcall, bool &quit, const bool validvector, void*& context);

  }

}
```


-------------------------------

Updated on 2026-11-03 at 14:50:45 +0000
