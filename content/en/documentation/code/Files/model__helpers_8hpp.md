---
title: 'file Models/model_helpers.hpp'

description: "[No description available]"

---

# Models/model_helpers.hpp



[No description available]

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::Models](/documentation/code/namespaces/namespacegambit_1_1models/)** <br>Forward declaration of [Models::ModelFunctorClaw]() class for use in constructors.  |




## Source code

```
//  GAMBIT: Global and Modular BSM Inference Tool
//  *********************************************
//
//  Helper functions used in Model definitions
//  and translation functions
//
//  *********************************************
//
//  Authors
//  =======
//
//  (add name and date if you modify)
//
//  Ben Farmer
//  2014 Dec
//
//  *********************************************

#ifndef __model_helpers_hpp__
#define __model_helpers_hpp__

#include <vector>
#include "gambit/Utils/model_parameters.hpp" 

namespace Gambit
{

  namespace Models
  {
  
    // Set many string-named ModelParameters to a single value
    inline void set_many_to_one(ModelParameters &myP, const std::vector<std::string>& v, const double value)
    {
       for(std::vector<std::string>::const_iterator it = v.begin(); it != v.end(); ++it)
       {
         myP.setValue(*it, value);
       }       
    }

  }
  
}

#endif
```


-------------------------------

Updated on 2022-09-07 at 13:49:53 +0000
