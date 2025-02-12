---
title: "file include/interface.hpp"

description: "[No description available]"

---

# file include/interface.hpp

[No description available]

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::Scanner](/documentation/code/namespaces/namespacegambit_1_1scanner/)**  |
| **[Gambit::Scanner::Python](/documentation/code/namespaces/namespacegambit_1_1scanner_1_1python/)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Gambit::Scanner::Python::diagnostics](/documentation/code/classes/classgambit_1_1scanner_1_1python_1_1diagnostics/)**  |
| class | **[Gambit::Scanner::Python::printer_wrapper](/documentation/code/classes/classgambit_1_1scanner_1_1python_1_1printer__wrapper/)**  |
| class | **[Gambit::Scanner::Python::scan_interface](/documentation/code/classes/classgambit_1_1scanner_1_1python_1_1scan__interface/)**  |




## Source code

```
#ifndef __SCANNERBIT_PYTHON_DIAGOSTICS_HPP__
#define __SCANNERBIT_PYTHON_DIAGOSTICS_HPP__

#include <string>
#include <unordered_set>
#include <vector>
#include <yaml-cpp/yaml.h>

#include "gambit/Printers/printermanager.hpp"
#include "gambit/Utils/yaml_parser_base.hpp"
#include "gambit/ScannerBit/base_prior.hpp"

namespace Gambit
{
    
    namespace Scanner
    {
        
        class Factory_Base;
        
        namespace Python
        {

            class diagnostics
            {
            private:
                std::unordered_set<std::string> valid_commands;
                
            public:
                diagnostics();
                void operator()(const std::vector<std::string> &args);
                void operator()(const std::string &command);
                ~diagnostics(){}
            };
            
            class scan_interface;
            
            class printer_wrapper
            {
            private:
                scan_interface *scanner;
                
            public:
                printer_wrapper(scan_interface *scanner) : scanner(scanner) {}
                void main_printer(std::unordered_map<std::string, double> &);
                void main_printer(const std::string &, const double &);
                void aux_printer(const std::string &, const double &);
                ~printer_wrapper(){}
            };
            
            class scan_interface
            {
            private:
                Printers::PrinterManager *global_printer;
                #ifdef WITH_MPI
                const bool init_mpi;
                #endif  
            public:
                scan_interface(bool);
                Printers::PrinterManager &get_printer_manager() const
                {
                    return *global_printer;
                }
                std::shared_ptr<printer_wrapper> get_printer();
                int run_scan(Gambit::IniParser::Parser &, const Gambit::Scanner::Factory_Base *, Gambit::Priors::BasePrior *, bool );
                int run_scan_node(YAML::Node *, const Gambit::Scanner::Factory_Base *, Gambit::Priors::BasePrior *, bool);
                int run_scan_str(std::string *, const Gambit::Scanner::Factory_Base *, Gambit::Priors::BasePrior *, bool);
                ~scan_interface(){}
            };
            
        }
        
    }
    
}

#endif
```


-------------------------------

Updated on 2025-02-12 at 15:36:40 +0000
