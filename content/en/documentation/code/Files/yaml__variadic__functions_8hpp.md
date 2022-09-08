---
title: "file Utils/yaml_variadic_functions.hpp"

description: "[No description available]"

---

# file Utils/yaml_variadic_functions.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |

## Detailed Description


**Author**: Gregory Martinez ([gregory.david.martinez@gmail.com](mailto:gregory.david.martinez@gmail.com)) 

**Date**: Feb 2014 

Variadic utilty functions which work with [YAML](/documentation/code/namespaces/namespaceyaml/) objects.

Separated from [variadic_functions.hpp](/documentation/code/files/variadic__functions_8hpp/#file-utils-variadic-functions-hpp) to avoid having the [YAML](/documentation/code/namespaces/namespaceyaml/) headers included everywhere.



------------------

Authors (add name and date if you modify):




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Variadic utilty functions which work with
///  YAML objects.
///
///  Separated from variadic_functions.hpp to
///  avoid having the YAML headers included
///  everywhere.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Gregory Martinez
///          (gregory.david.martinez@gmail.com)
///  \date Feb 2014
//
///  \author Christoph Weniger
///          <c.weniger@uva.nl>
///  \date Dec 2014
///
///  \author Ben Farmer
///          <benjamin.farmer@fysik.su.se>
///  \date Jan 2016
///
///  *********************************************

#ifndef YAML_VARIADIC_FUNCTIONS_HPP
#define YAML_VARIADIC_FUNCTIONS_HPP

#include <string>

#include "yaml-cpp/yaml.h"

namespace Gambit
{       
        //////////////////////////////////////
        //Variadic Node functions
        //////////////////////////////////////
        
        inline const YAML::Node getVariadicNode(const YAML::Node &node)
        {
                return node;
        }
        
        inline const YAML::Node getVariadicNode(const YAML::Node &node, std::string key) 
        {
                return node[key];
        }

        template <typename... args>
        inline const YAML::Node getVariadicNode(const YAML::Node &node, const std::string &key, const args&... keys)
        {
                if(not node[key]) return node[key];
                else return getVariadicNode(node[key], keys...);
        }
        
}

#endif
```


-------------------------------

Updated on 2022-09-08 at 03:08:04 +0000
