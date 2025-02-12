---
title: "file ScannerBit/scanner_util_types.hpp"

description: "[No description available]"

---

# file ScannerBit/scanner_util_types.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::Scanner](/documentation/code/namespaces/namespacegambit_1_1scanner/)**  |

## Detailed Description


Utility Functions for the [Gambit](/documentation/code/namespaces/namespacegambit/) Scanner



------------------


# Authors

(add name and date if you modify)

Gregory Martinez ([gregory.david.martinez@gmail.com](mailto:gregory.david.martinez@gmail.com)) 

2023 Jan



------------------




## Source code

```
//  GAMBIT: Global and Modular BSM Inference Tool
//  *********************************************
/// \file
///  Utility Functions for the Gambit Scanner
///
///  *********************************************
///
///  Authors
///  =======
///
///  (add name and date if you modify)
///
///  \author Gregory Martinez
///          (gregory.david.martinez@gmail.com)
///  \date 2023 Jan
///
///  *********************************************

#ifndef __scanner_util_types_hpp__
#define __scanner_util_types_hpp__

#include <Eigen/Dense>

namespace Gambit
{
    
    namespace Scanner
    {

        /****************************************/
        /********* Eigen3 definitions ***********/
        /****************************************/
        
        /// \brief A vector.
        ///
        template <typename T>
        using vector = Eigen::Matrix<T, Eigen::Dynamic, 1>;
        
        /// \brief A row vector.
        ///
        template <typename T>
        using row_vector = Eigen::Matrix<T, 1, Eigen::Dynamic>;
        
        /// \brief A matrix.
        ///
        template <typename T>
        using matrix = Eigen::Matrix<T, Eigen::Dynamic, Eigen::Dynamic>;
        
        /// \brief Represents the unit hypercube.
        ///
        template <typename T>
        using hyper_cube_ref = Eigen::Ref<vector<T>, 0, Eigen::Stride<Eigen::Dynamic, Eigen::Dynamic>>;
        
        /// \brief Vector using raw data.
        ///
        template <typename T>
        using map_vector = Eigen::Map<vector<T>, Eigen::Unaligned, Eigen::Stride<1, 1>>;
        
    }
    
}

#endif
```


-------------------------------

Updated on 2025-02-12 at 15:36:40 +0000
