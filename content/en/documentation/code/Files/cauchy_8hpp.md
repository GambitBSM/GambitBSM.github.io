---
title: "file priors/cauchy.hpp"

description: "[No description available]"

---

# file priors/cauchy.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::Priors](/documentation/code/namespaces/namespacegambit_1_1priors/)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Gambit::Priors::Cauchy](/documentation/code/classes/classgambit_1_1priors_1_1cauchy/)** <br>Multi-dimensional [Cauchy]() prior.  |

## Detailed Description


**Author**: 

  * Ben Farmer ([benjamin.farmer@monash.edu.au](mailto:benjamin.farmer@monash.edu.au)) 
  * Gregory Martinez ([gregory.david.martinez@gmail.com](mailto:gregory.david.martinez@gmail.com)) 
  * Andrew Fowlie ([andrew.j.fowlie@qq.com](mailto:andrew.j.fowlie@qq.com)) 


**Date**: 

  * 2013 Dec
  * Feb 2014
  * August 2020


Multivariate Cauchy prior



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//  GAMBIT: Global and Modular BSM Inference Tool
//  *********************************************
///  \file
///
///  Multivariate Cauchy prior
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Ben Farmer
///    (benjamin.farmer@monash.edu.au)
///  \date 2013 Dec
///
///  \author Gregory Martinez
///    (gregory.david.martinez@gmail.com)
///  \date Feb 2014
///
///  \author Andrew Fowlie
///    (andrew.j.fowlie@qq.com)
///  \date August 2020
///
///  *********************************************

#ifndef __PRIOR_CAUCHY_HPP__
#define __PRIOR_CAUCHY_HPP__

#include <algorithm>
#include <cmath>
#include <string>
#include <unordered_map>
#include <vector>

#include "gambit/ScannerBit/cholesky.hpp"
#include "gambit/ScannerBit/priors.hpp"
#include "gambit/ScannerBit/scanner_utils.hpp"

namespace Gambit 
{

    namespace Priors 
    {
        /**
        * @brief  Multi-dimensional Cauchy prior
        *
        * This is a [multivariate \f$t\f$-distribution](https://en.wikipedia.org/wiki/Multivariate_t-distribution)
        * with \f$\nu = 1\f$ degree of freedom. 
        *
        * Defined by a scale matrix, \f$\Sigma\f$, and a location vector.
        *
        * If the scale matrix is diagonal,it may instead be specified by the square-roots of its 
        * diagonal entries, denoted \f$\gamma\f$.
        */
        class Cauchy : public BasePrior
        {
        private:
            std::vector<double> location;
            mutable Cholesky col;

        public:
            // Constructor defined in cauchy.cpp
            Cauchy(const std::vector<std::string>& param, const Options& options);

            /** @brief Transformation from unit interval to the Cauchy */
            void transform(hyper_cube_ref<double> unitpars, std::unordered_map<std::string, double>& outputMap) const
            {
                std::vector<double> vec(unitpars.size());

                for (int i = 0, end = vec.size(); i < end; ++i)
                    vec[i] = std::tan(M_PI * (unitpars[i] - 0.5));

                col.ElMult(vec);

                auto v_it = vec.begin();
                auto m_it = location.begin();
                for (auto str_it = param_names.begin(), str_end = param_names.end(); str_it != str_end; str_it++)
                {
                    outputMap[*str_it] = *(v_it++) + *(m_it++);
                }
            }

            void inverse_transform(const std::unordered_map<std::string, double> &physical, hyper_cube_ref<double> unit) const override
            {
                // subtract location
                std::vector<double> central;
                for (int i = 0, n = this->size(); i < n; i++)
                {
                    central.push_back(physical.at(param_names[i]) - location[i]);
                }

                // invert rotation by Cholesky matrix
                std::vector<double> rotated = col.invElMult(central);

                // now diagonal; invert Cauchy CDF
                for (int i = 0, end = rotated.size(); i < end; ++i)
                    unit[i] = std::atan(rotated[i]) / M_PI + 0.5;
            }

            double log_prior_density(const std::unordered_map<std::string, double> &physical) const override
            {
                static double norm = std::log(M_PI * col.DetSqrt());
                std::vector<double> vec(param_names.size());
                
                for (int i = 0, end = param_names.size(); i < end; ++i)
                    vec[i] = physical.at(param_names[i]);
                
                return -std::log1p(col.Square(vec, location)) - norm;
            }
        };

        LOAD_PRIOR(cauchy, Cauchy)

    }  // namespace Priors

}  // namespace Gambit

#endif  // __PRIOR_CAUCHY_HPP__
```


-------------------------------

Updated on 2025-02-12 at 16:10:33 +0000
