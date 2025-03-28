---
title: "file priors/doublelogflatjoin.hpp"

description: "[No description available]"

---

# file priors/doublelogflatjoin.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::Priors](/documentation/code/namespaces/namespacegambit_1_1priors/)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Gambit::Priors::DoubleLogFlatJoin](/documentation/code/classes/classgambit_1_1priors_1_1doublelogflatjoin/)**  |

## Detailed Description


**Author**: Ben Farmer ([benjamin.farmer@fysik.su.se](mailto:benjamin.farmer@fysik.su.se)) 

**Date**: 2016 Jun

Prior function made up of two log priors (positive and negative branch) joined across zero by a flat region.



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//  GAMBIT: Global and Modular BSM Inference Tool
//  *********************************************
///  \file
///
///  Prior function made up of two log priors
///  (positive and negative branch) joined across
///  zero by a flat region.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///   
///  \author Ben Farmer
///          (benjamin.farmer@fysik.su.se)
///  \date 2016 Jun
///
///  *********************************************

#ifndef PRIOR_DOUBLELOGFLATJOIN_HPP
#define PRIOR_DOUBLELOGFLATJOIN_HPP

#include "gambit/ScannerBit/priors.hpp"
#include "gambit/Utils/yaml_options.hpp"

#include <vector>
  
namespace Gambit
{
   namespace Priors
   {
      /// 1D double log prior with flat bridge over zero.
      /// (for creating a prior similar to log that works across positive and negative values continuously).
      /// Takes the arguments: [minval : flat_start : flat_end : maxval]
      class DoubleLogFlatJoin : public BasePrior
      {
      private:
         /// Name of the parameter that this prior is supposed to transform
         const std::string &myparameter;
         /// Variables controlling the prior range etc.
         /// @{
         double lower;
         double flat_start;
         double flat_end;
         double upper;
         /// @}
         /// Useful quantities
         /// @{
         double C; 
         double P01;
         double P12;
         double P23;
         /// @}

         /// Flags to register if special cases are active.
         /// @{
         bool no_lower_log;
         bool no_upper_log;
         /// @}
     
         /// Try to get options for double log-flat joined prior
         double get_option(const str&, const Options&);

      public: 
         /// Constructor defined in doublelogflatjoin.cpp
         DoubleLogFlatJoin(const std::vector<std::string>& param, const Options&); 

         /// Transformation from unit interval to the double log + flat join (inverse prior transform)
         void transform(hyper_cube_ref<double> unitpars, std::unordered_map <std::string, double> &output) const override;
         void inverse_transform(const std::unordered_map<std::string, double> &, hyper_cube_ref<double>) const override;

         /// Probability density function
         double log_prior_density(const std::unordered_map<std::string, double> &) const override;
      };
  
      LOAD_PRIOR(double_log_flat_join, DoubleLogFlatJoin)
   }
}

#endif
```


-------------------------------

Updated on 2025-02-12 at 16:10:33 +0000
