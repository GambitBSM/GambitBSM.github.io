---
title: "file Printers/printermanager.hpp"

description: "[No description available]"

---

# file Printers/printermanager.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::Printers](/documentation/code/namespaces/namespacegambit_1_1printers/)** <br>Forward declaration.  |

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Gambit::Printers::PrinterManager](/documentation/code/classes/classgambit_1_1printers_1_1printermanager/)** <br>Manager class for creating printer objects  |

## Detailed Description


**Author**: Ben Farmer ([benjamin.farmer@monash.edu.au](mailto:benjamin.farmer@monash.edu.au)) 

**Date**: 2014 May

Manager class for printers. Creates printer object according to inifile instructions, and cleans them up on exit.



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Manager class for printers.
///  Creates printer object according to inifile
///  instructions, and cleans them up on exit.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///   
///  \author Ben Farmer
///          (benjamin.farmer@monash.edu.au)
///  \date 2014 May
///
///  *********************************************

#ifndef __printermanager_hpp__
#define __printermanager_hpp__

#include <string>
#include <map>
#include "gambit/Printers/baseprintermanager.hpp"
#include "gambit/Utils/yaml_options.hpp"
#include "gambit/Utils/mpiwrapper.hpp" // for debugging

namespace Gambit
{
  namespace Printers 
  {

    /// Forward declaration of base printer classes (Declared fully in baseprinter.hpp and basebaseprinter.hpp)
    class BaseBasePrinter; 
    class BaseBaseReader; 
    class BasePrinter; 
    class BaseReader;
    class PrinterManager;
  }

  // Global manager setter/retriever
  Printers::BaseReader& get_pp_reader();
  void set_global_printer_manager(Printers::PrinterManager* pm);
  Printers::PrinterManager* get_global_printer_manager();

  namespace Printers
  {
    /// Manager class for creating printer objects  
    class PrinterManager: public BasePrinterManager
    {
      private:
        /// Map containing pointers to auxiliary printer objects
        std::map<std::string, BasePrinter*> auxprinters;

        /// Map containing pointers to reader objects
        std::map<std::string, BaseReader*> readers;

        /// Name specifying the printer type
        std::string tag;
    
        /// Storage for printer options (needed for creating new streams)
        Options options;

      public:
        /// Pointer to main printer object 
        BasePrinter* printerptr;

        /// Constructor
        PrinterManager(const Options&, bool resume_mode);
  
        /// Destructor
        ~PrinterManager();

        /// Create auxiliary printer object
        void new_stream(const std::string&, const Options&);

        /// Create reader object
        void new_reader(const std::string&, const Options&);

        /// Create for reader object for previous print output ("resume reader")
        void create_resume_reader();

        /// Getter for auxiliary printer objects
        BaseBasePrinter* get_stream(const std::string& = "");
  
        /// Getter for reader objects
        BaseBaseReader* get_reader(const std::string&);

        /// Retrieve non-basebase version of reader object (for use in module functions rather than ScannerBit)
        BaseReader* get_full_reader(const std::string& readername);
 
        /// Checker for existence of reader object
        bool reader_exists(const std::string&);
         
        /// Destruct printer/reader objects
        void delete_stream(const std::string& = "");
        void delete_reader(const std::string&);
 
        /// Instruct printers that scan has finished and to perform cleanup
        void finalise(bool abnormal=false);

  };


  }
}

#endif //__printermanager_hpp__
```


-------------------------------

Updated on 2022-09-08 at 02:27:29 +0000
