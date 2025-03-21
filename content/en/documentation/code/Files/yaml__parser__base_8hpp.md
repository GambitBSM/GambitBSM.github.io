---
title: "file Utils/yaml_parser_base.hpp"

description: "[No description available]"

---

# file Utils/yaml_parser_base.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::IniParser](/documentation/code/namespaces/namespacegambit_1_1iniparser/)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Gambit::IniParser::Parser](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/)** <br>Inifile parser base class.  |

## Detailed Description


**Author**: 

  * Christoph Weniger ([c.weniger@uva.nl](mailto:c.weniger@uva.nl)) 
  * Gregory Martinez ([gregory.david.martinez@gmail.com](mailto:gregory.david.martinez@gmail.com)) 
  * Pat Scott ([patscott@physics.mcgill.ca](mailto:patscott@physics.mcgill.ca)) 
  * Markus Prim ([markus.prim@kit.edu](mailto:markus.prim@kit.edu)) 
  * Tomas Gonzalo ([tomas.gonzalo@monash.edu](mailto:tomas.gonzalo@monash.edu)) 


**Date**: 

  * 2013 June 2013
  * 2014 Feb
  * 2014 Mar 
  * 2015 Mar
  * 2020 May
  * 2020 June


Base class for ini-file parsers using yaml-cpp



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Base class for ini-file parsers using yaml-cpp
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///   
///  \author Christoph Weniger
///          (c.weniger@uva.nl)
///  \date 2013 June 2013
///
///  \author Gregory Martinez
///          (gregory.david.martinez@gmail.com)
///  \date 2014 Feb
///
///  \author Pat Scott
///          (patscott@physics.mcgill.ca)
///  \date 2014 Mar
///  \date 2015 Mar
///
///  \author Markus Prim
///          (markus.prim@kit.edu)
///  \date 2020 May
///
///  \author Tomas Gonzalo
///          (tomas.gonzalo@monash.edu)
///  \date 2020 June
///
///  *********************************************

#ifndef __yaml_parser_base_hpp__
#define __yaml_parser_base_hpp__

#include "gambit/Utils/standalone_error_handlers.hpp"
#include "gambit/Utils/util_types.hpp"
#include "gambit/Utils/yaml_options.hpp"

#include "yaml-cpp/yaml.h"
#include <limits>


namespace Gambit
{

  namespace IniParser
  {

    /// Inifile parser base class
    class Parser
    {

      public:

        /// Read in the YAML file
        virtual void readFile(str filename);

        /// Getter for the full YAML node
        YAML::Node getYAMLNode() const;

        /// Getters for key/value section
        /// @{
        YAML::Node getParametersNode() const;
        YAML::Node getPriorsNode() const;
        YAML::Node getPrinterNode() const;
        YAML::Node getScannerNode() const;
        YAML::Node getLoggerNode() const;
        YAML::Node getKeyValuePairNode() const;
        
        template <typename... args>
        bool hasKey(args... keys) const
        {
          return getVariadicNode(keyValuePairNode, keys...);
        }

        template<typename TYPE, typename... args> TYPE getValue(args... keys) const
        {
          const YAML::Node node = getVariadicNode(keyValuePairNode, keys...);
          if (not node) inifile_error().raise(LOCAL_INFO,"No inifile entry for [" + stringifyVariadic(keys...) + "]");
          return NodeUtility::getNode<TYPE>(node);
        }

        template<typename TYPE, typename... args> TYPE getValueOrDef(TYPE def, const args&... keys) const
        {
          const YAML::Node node = getVariadicNode(keyValuePairNode, keys...);
          if (not node)
          {
              return def;
          }
          return NodeUtility::getNode<TYPE>(node);
        }
        /// @}

        /// Getters for model/parameter section
        /// @{
        template<typename TYPE> TYPE getModelParameterEntry(str model, str param, str key) const
        {
          if (not parametersNode[model][param][key]) inifile_error().raise(LOCAL_INFO,model + "." + param + "." + key + "not found in inifile.");
          return parametersNode[model][param][key].as<TYPE>();
        }
        bool hasModelParameterEntry(str model, str param, str key) const;
        /// Return list of model names (without "adhoc" model!)
        const std::set<str> getModelNames() const;
        const std::vector<str> getModelParameters(str model) const;
        /// @}

        /// Getter for options
        const Options getOptions(str key) const;

     protected:

        /// Read in the actual YAML file
        YAML::Node filename_to_node(str);
        
        /// Do the basic parsing of the YAML file
        void basicParse(YAML::Node,str);

        /// Print a node to file
        void printNode(YAML::Node,str,bool);
        
      private:     

        YAML::Node YAMLNode;
        YAML::Node keyValuePairNode;
        YAML::Node parametersNode;
        YAML::Node priorsNode;
        YAML::Node printerNode;
        YAML::Node scannerNode;
        YAML::Node logNode;
    };


  }

}

#endif /* defined(__yaml_parser_base_hpp__) */
```


-------------------------------

Updated on 2025-02-12 at 16:10:33 +0000
