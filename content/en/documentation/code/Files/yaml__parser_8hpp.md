---
title: "file Core/yaml_parser.hpp"

description: "[No description available]"

---

# file Core/yaml_parser.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::IniParser](/documentation/code/namespaces/namespacegambit_1_1iniparser/)**  |
| **[YAML](/documentation/code/namespaces/namespaceyaml/)** <br>[YAML]() overloads for mass cut and mass cut ratio constituents.  |

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Gambit::IniParser::IniFile](/documentation/code/classes/classgambit_1_1iniparser_1_1inifile/)** <br>Main inifile class.  |
| struct | **[YAML::convert< Gambit::DRes::Observable >](/documentation/code/classes/structyaml_1_1convert_3_01gambit_1_1dres_1_1observable_01_4/)**  |
| struct | **[YAML::convert< Gambit::DRes::ModuleRule >](/documentation/code/classes/structyaml_1_1convert_3_01gambit_1_1dres_1_1modulerule_01_4/)**  |
| struct | **[YAML::convert< Gambit::DRes::BackendRule >](/documentation/code/classes/structyaml_1_1convert_3_01gambit_1_1dres_1_1backendrule_01_4/)**  |

## Detailed Description


**Author**: 

  * Christoph Weniger ([c.weniger@uva.nl](mailto:c.weniger@uva.nl)) 
  * Gregory Martinez ([gregory.david.martinez@gmail.com](mailto:gregory.david.martinez@gmail.com)) 
  * Pat Scott ([patscott@physics.mcgill.ca](mailto:patscott@physics.mcgill.ca)) 


**Date**: 

  * 2013 June
  * 2014 Feb
  * 2014 Mar 
  * 2015 Mar 
  * 2020 Apr 
  * 2022 Nov


Ini-file parser based on yaml-cpp



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Ini-file parser based on yaml-cpp
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Christoph Weniger
///          (c.weniger@uva.nl)
///  \date 2013 June
///
///  \author Gregory Martinez
///          (gregory.david.martinez@gmail.com)
///  \date 2014 Feb
///
///  \author Pat Scott
///          (patscott@physics.mcgill.ca)
///  \date 2014 Mar
///  \date 2015 Mar
///  \date 2020 Apr
///  \date 2022 Nov
///
///  *********************************************

#pragma once

#include "gambit/Core/observable.hpp"
#include "gambit/Core/rule.hpp"
#include "gambit/Utils/yaml_parser_base.hpp"
#include "gambit/Utils/util_functions.hpp"

#include "yaml-cpp/yaml.h"


namespace Gambit
{

  namespace IniParser
  {

    /// Main inifile class
    class IniFile : public Parser
    {

      public:

        /// Return the filename
        const str filename() const;

        /// Read in the YAML file
        virtual void readFile(str);

        /// Getters for private observable and rules entries
        /// @{
        const std::vector<DRes::Observable>& getObservables() const;
        const std::vector<DRes::ModuleRule>& getModuleRules() const;
        const std::vector<DRes::BackendRule>& getBackendRules() const;
        /// @}

      private:

        str _filename;
        std::vector<DRes::Observable> observables;
        std::vector<DRes::ModuleRule> module_rules;
        std::vector<DRes::BackendRule> backend_rules;

    };

  }

}


namespace YAML
{

  /// Rules for inifile --> observable/rule mapping
  /// @{

  template<>
  struct convert<Gambit::DRes::Observable>
  {
    static bool decode(const Node&, Gambit::DRes::Observable&);
  };

  template<>
  struct convert<Gambit::DRes::ModuleRule>
  {
    static bool decode(const Node&, Gambit::DRes::ModuleRule&);
  };

  template<>
  struct convert<Gambit::DRes::BackendRule>
  {
    static bool decode(const Node&, Gambit::DRes::BackendRule&);
  };

  /// @}

}
```


-------------------------------

Updated on 2024-07-18 at 13:53:34 +0000
