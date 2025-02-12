---
title: "file Elements/wimp_types.hpp"

description: "[No description available]"

---

# file Elements/wimp_types.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |

## Classes

|                | Name           |
| -------------- | -------------- |
| struct | **[Gambit::WIMPprops](/documentation/code/classes/structgambit_1_1wimpprops/)**  |
| class | **[Gambit::WIMP_annihilation](/documentation/code/classes/classgambit_1_1wimp__annihilation/)**  |

## Detailed Description


**Author**: 

  * Ben Farmer ([b.farmer@imperial.ac.uk](mailto:b.farmer@imperial.ac.uk)) 
  * Tomas Gonzalo ([gonzalo@physik.rwth-aachen.de](mailto:gonzalo@physik.rwth-aachen.de)) 
  * Torsten Bringmann ([torsten.bringmann@fys.uio.no](mailto:torsten.bringmann@fys.uio.no)) 


**Date**: 

  * 2019 Sep
  * 2021 Sep
  * 2023 Nov


Various container for WIMP particle and annihilation properties



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Various container for WIMP particle  and
///  annihilation properties
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Ben Farmer
///          (b.farmer@imperial.ac.uk)
///  \date 2019 Sep
///
///  \author Tomas Gonzalo
///          (gonzalo@physik.rwth-aachen.de)
///  \date 2021 Sep
///
///  \author Torsten Bringmann
///          (torsten.bringmann@fys.uio.no)
///  \date 2023 Nov
///
///  *********************************************

#ifndef __wimp_types_hpp__
#define __wimp_types_hpp__

#include <string>
#include <map>

namespace Gambit
{
    // Basic properties of generic WIMP
    struct WIMPprops
    {
      double mass;
      unsigned int spinx2;
      double etaDM; // primordial asymmetry
      bool sc; // Self-conjugate?
      std::string name; // Name in the particle database
      std::string conjugate; // Name of conjugate in the particle database
    };

    /// Contain for generic parameterisation of WIMP annihilation to various two-body final states,
    /// with <sigma v> expanded as a simple power series in v^2
    class WIMP_annihilation
    {
        public:
            WIMP_annihilation();
            double A(const std::string& channel) const;
            double B(const std::string& channel) const;

            void setA(const std::string& channel, double val);
            void setB(const std::string& channel, double val);
        private:
            std::map<std::string,double> a;
            std::map<std::string,double> b;
    };

}

#endif //__wimp_types_hpp__
```


-------------------------------

Updated on 2025-02-12 at 16:10:34 +0000
