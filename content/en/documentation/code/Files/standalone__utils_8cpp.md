---
title: "file src/standalone_utils.cpp"

description: "[No description available]"

---

# file src/standalone_utils.cpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |

## Detailed Description


**Author**: 

  * Pat Scott 

 ([patscott@physics.mcgill.ca](mailto:patscott@physics.mcgill.ca)) 
  * Chris Chang 


**Date**: 

  * 2016 Jun
  * 2023 Dec


Includes implementations needed to use a GAMBIT module as a standalone analysis code.



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Includes implementations needed to use a GAMBIT
///  module as a standalone analysis code.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///   
///  \author Pat Scott  
///          (patscott@physics.mcgill.ca)
///  \date 2016 Jun
///
///  \author Chris Chang
///  \date 2023 Dec
///
///  *********************************************

#include "gambit/Utils/standalone_utils.hpp"
#include "gambit/Logs/logger.hpp"
#include "gambit/Logs/logmaster.hpp"

namespace Gambit
{

  /// Logger setup standalone utility function
  void initialise_standalone_logs(str prefix)
  {
    // Make a logging object
    std::map<std::string, std::string> loggerinfo;

    // Ensure that the desired output directory exists
    Utils::ensure_path_exists(prefix);

    // Add entries to the loggerinfo map
    loggerinfo["Default"]  = prefix+"default.log";
    loggerinfo["Debug"]   = prefix+"debug.log";
    loggerinfo["Warning"] = prefix+"warnings.log";
    loggerinfo["Error"]   = prefix+"errors.log";

    // Initialise global LogMaster object
    logger().initialise(loggerinfo);
  }

  /// Initialise the printers (required for suspicious point raises)
  YAML::Node get_standalone_printer(str printer, str prefix, str filename)
  {
    // Set the minimum required settings by the printer
    YAML::Node printerNode;
    printerNode["printer"] = printer;
    printerNode["options"]["default_output_path"] = Utils::ensure_path_exists(prefix);
    printerNode["options"]["output_file"] = filename;
    return printerNode;
  }

}
```


-------------------------------

Updated on 2025-02-12 at 16:10:33 +0000
