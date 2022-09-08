---
title: "file Models/safe_param_map.hpp"

description: "[No description available]"

---

# file Models/safe_param_map.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::Models](/documentation/code/namespaces/namespacegambit_1_1models/)** <br>Forward declaration of [Models::ModelFunctorClaw]() class for use in constructors.  |

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Gambit::Models::safe_param_map](/documentation/code/classes/classgambit_1_1models_1_1safe__param__map/)**  |

## Detailed Description


**Author**: 

  * Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 
  * Ben Farmer ([b.farmer@imperial.ac.uk](mailto:b.farmer@imperial.ac.uk)) 


**Date**: 

  * 2014 Dec
  * 2019 Jul


Simple overlay of std::map that makes [] act like .at(), so that Param map in module functors can give a more customised error.



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Simple overlay of std::map that makes [] act
///  like .at(), so that Param map in module
///  functors can give a more customised error.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Pat Scott
///          (p.scott@imperial.ac.uk)
///  \date 2014 Dec
///
///  \author Ben Farmer
///          (b.farmer@imperial.ac.uk)
///  \date 2019 Jul
///
///  *********************************************


#ifndef __safe_param_map_hpp__
#define __safe_param_map_hpp__

#include "gambit/Utils/standalone_error_handlers.hpp"

#include <map>
#include <string>
#include <stdexcept>

namespace Gambit
{

  namespace Models
  {

    template<typename T>
    class safe_param_map : public std::map<std::string,T>
    {
      public:
        T operator[](std::string key) const
        {
          try
          {
            T temp(this->at(key));
            return temp;
          }
          catch(std::out_of_range&)
          {
            model_error().raise("call to [] operator of Param map in a module function", "Requested parameter \""+key+"\" is not available. \n"
                                "Generally this happens because you have requested a parameter of a model that\n"
                                "is not being scanned (check that you are using the ModelInUse() function), or\n"
                                "because you have failed to declare the dependency on the model's parameters  \n"
                                "in your rollcall header using ALLOW_MODEL(S) or ALLOW_MODEL_DEPENDENCE.");
          }
          T temp2(this->at(key)); // Will only get here if someone has turned model errors into warnings.  If so, they get what they deserve.
          return temp2;
        }
    };

  }

}


#endif //#defined __safe_param_map_hpp
```


-------------------------------

Updated on 2022-09-08 at 02:00:51 +0000
