---
title: "file priors/lognormal.hpp"

description: "[No description available]"

---

# file priors/lognormal.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::Priors](/documentation/code/namespaces/namespacegambit_1_1priors/)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Gambit::Priors::LogNormal](/documentation/code/classes/classgambit_1_1priors_1_1lognormal/)** <br>Multi-dimensional Log-Normal prior.  |

## Detailed Description


**Author**: 

  * Ben Farmer ([benjamin.farmer@monash.edu.au](mailto:benjamin.farmer@monash.edu.au)) 
  * Gregory Martinez ([gregory.david.martinez@gmail.com](mailto:gregory.david.martinez@gmail.com)) 
  * Andrew Fowlie ([andrew.j.fowlie@qq.com](mailto:andrew.j.fowlie@qq.com)) 


**Date**: 

  * 2013 Dec
  * Feb 2014
  * August 2020


Multivariate Log-Normal prior



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//  GAMBIT: Global and Modular BSM Inference Tool
//  *********************************************
///  \file
///
///  Multivariate Log-Normal prior
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Ben Farmer
///  (benjamin.farmer@monash.edu.au)
///  \date 2013 Dec
///
///  \author Gregory Martinez
///  (gregory.david.martinez@gmail.com)
///  \date Feb 2014
///
///  \author Andrew Fowlie
///    (andrew.j.fowlie@qq.com)
///  \date August 2020
///
///  *********************************************

#ifndef __PRIOR_LOGNORMAL_HPP__
#define __PRIOR_LOGNORMAL_HPP__

#include <algorithm>
#include <cmath>
#include <numeric>
#include <string>
#include <unordered_map>
#include <vector>

#include "gambit/ScannerBit/cholesky.hpp"
#include "gambit/ScannerBit/priors.hpp"
#include "gambit/Utils/yaml_options.hpp"

#include <boost/math/special_functions/erf.hpp>

namespace Gambit
{
    namespace Priors
    {
        /**
        * @brief  Multi-dimensional Log-Normal prior
        *
        * Defined by a covariance matrix and mean of \f$\log x\f$.
        *
        * If the covariance matrix is diagonal, it may instead be specified by the square-roots of its
        * diagonal entries, denoted \f$\sigma\f$.
        *
        * The base is by default 10.
        */
        class LogNormal : public BasePrior
        {
        private:
            std::vector <double> mu;
            double base{10.};
            mutable Cholesky col;

        public:
            // Constructor defined in LogNormal.cpp
            LogNormal(const std::vector<std::string>&, const Options&);

            // Transformation from unit interval to the Log-Normal
            void transform(hyper_cube_ref<double> unitpars, std::unordered_map<std::string, double> &outputMap) const override
            {
                std::vector<double> vec(unitpars.size());
                for (int i = 0, end = vec.size(); i < end; ++i)
                    vec[i] = M_SQRT2 * boost::math::erf_inv(2. * unitpars[i] - 1.);

                col.ElMult(vec);

                auto v_it = vec.begin();
                auto m_it = mu.begin();
                for (auto str_it = param_names.begin(), str_end = param_names.end(); str_it != str_end; str_it++)
                {
                    outputMap[*str_it] = std::pow(base, *(v_it++) + *(m_it++));
                }
            }

            void inverse_transform(const std::unordered_map<std::string, double> &physical, hyper_cube_ref<double> unit) const override
            {
                // undo exponentiation
                std::vector<double> log_physical;
                for (int i = 0, n = this->size(); i < n; i++)
                {
                    log_physical.push_back(std::log(physical.at(param_names[i])) / std::log(base));
                }

                // subtract mean
                std::vector<double> central;
                for (int i = 0, n = this->size(); i < n; i++)
                {
                    central.push_back(log_physical[i] - mu[i]);
                }

                // invert rotation by Cholesky matrix
                std::vector<double> rotated = col.invElMult(central);

                // now diagonal; invert Gaussian CDF
                for (int i = 0, end = rotated.size(); i < end; ++i)
                    unit[i] = 0.5 * (boost::math::erf(rotated[i] / M_SQRT2) + 1.0);
            }

            double log_prior_density(const std::unordered_map<std::string, double> &physical) const
            {
                static double norm = 0.5 * std::log(2. * M_PI * std::pow(col.DetSqrt(), 2));
                std::vector<double> log_vec(param_names.size());
                for (int i = 0, end = param_names.size(); i < end; ++i)
                {
                    log_vec[i] = std::log(physical.at(param_names[i])) / std::log(base);
                }
                const double log_prod = std::accumulate(log_vec.begin(), log_vec.end(), 0.);
                
                return -0.5 * col.Square(log_vec, mu) - norm - log_prod;
            }
        };

        LOAD_PRIOR(lognormal, LogNormal)

    }  // namespace Priors

}  // namespace Gambit

#endif  // __PRIOR_LOGNORMAL_HPP__
```


-------------------------------

Updated on 2025-02-12 at 16:10:33 +0000
