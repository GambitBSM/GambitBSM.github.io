---
title: "file src/ScannerBit/python/src/diagnostics.cpp"

description: "[No description available]"

---

# file src/ScannerBit/python/src/diagnostics.cpp

[No description available]

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::Scanner](/documentation/code/namespaces/namespacegambit_1_1scanner/)**  |
| **[Gambit::Scanner::Python](/documentation/code/namespaces/namespacegambit_1_1scanner_1_1python/)**  |




## Source code

```

#include <vector>
#include <sstream>
#include "gambit/Utils/screen_print_utils.hpp"
#include "gambit/ScannerBit/plugin_loader.hpp"
#include "gambit/ScannerBit/scanner_utils.hpp"
#include "interface.hpp"


namespace Gambit
{
    
    namespace Scanner
    {
        
        namespace Python
        {

            inline void scanner_diagnostic()
            {
                std::string output = Scanner::Plugins::plugin_info().print_all("scanner");
                if (output.length() > 0)
                    print_to_screen(output, "scanners");
            }

            inline void test_function_diagnostic()
            {
                std::string output = Scanner::Plugins::plugin_info().print_all("objective");
                if (output.length() > 0)
                    print_to_screen(output, "objectives");
            }

            inline void prior_diagnostic()
            {
                std::string output = Scanner::Plugins::plugin_info().print_priors("priors");
                if (output.length() > 0)
                    print_to_screen(output, "priors");
            }

            inline void ff_prior_diagnostic(const std::string& command)
            {
                if (command != "priors")
                {
                    std::string output = Scanner::Plugins::plugin_info().print_priors(command);
                    if (output.length() > 0)
                        print_to_screen(output, command);
                }
            }

            inline void ff_scanner_diagnostic(const std::string& command)
            {
                std::string output = Scanner::Plugins::plugin_info().print_plugin("scanner", command);
                if (output.length() > 0)
                    print_to_screen(output, command);
            }

            inline void ff_test_function_diagnostic(const std::string& command)
            {
                std::string output = Scanner::Plugins::plugin_info().print_plugin("objective", command);
                if (output.length() > 0)
                    print_to_screen(output, command);
            }

            diagnostics::diagnostics()
            {
                std::vector<std::string> scanner_names = Scanner::Plugins::plugin_info().print_plugin_names("scanner");
                std::vector<std::string> objective_names = Scanner::Plugins::plugin_info().print_plugin_names("objective");
                std::vector<std::string> prior_groups = Scanner::Plugins::plugin_info().list_prior_groups();
                valid_commands.insert(scanner_names.begin(), scanner_names.end());
                valid_commands.insert(objective_names.begin(), objective_names.end());
                valid_commands.insert(prior_groups.begin(), prior_groups.end());
                valid_commands.insert("priors");
                valid_commands.insert("objectives");
                valid_commands.insert("test-functions");
                valid_commands.insert("scanners");
            }

            void diagnostics::operator()(const std::vector<std::string> &args)
            {
                for (auto &&command : args)
                {
                    if (valid_commands.find(command) != valid_commands.end())
                    {
                        if (command == "scanners") scanner_diagnostic();
                        if (command == "test-functions" || command == "objectives") test_function_diagnostic();
                        if (command == "priors") prior_diagnostic();
                        ff_scanner_diagnostic(command);
                        ff_test_function_diagnostic(command);
                        ff_prior_diagnostic(command);
                    }
                }
            }
                    
            void diagnostics::operator()(const std::string &command)
            {
                if (valid_commands.find(command) != valid_commands.end())
                {
                    if (command == "scanners") scanner_diagnostic();
                    if (command == "test-functions" || command == "objectives") test_function_diagnostic();
                    if (command == "priors") prior_diagnostic();
                    ff_scanner_diagnostic(command);
                    ff_test_function_diagnostic(command);
                    ff_prior_diagnostic(command);
                }
            }

        }
        
    }
    
}
```


-------------------------------

Updated on 2025-02-12 at 15:36:40 +0000
