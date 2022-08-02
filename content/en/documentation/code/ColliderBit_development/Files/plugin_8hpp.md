---
title: 'file priors/plugin.hpp'

description: "[No description available]"

---






[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/colliderbit_development/namespaces/namespacegambit/)** <br>Simulation of "Search for photonic signatures of gauge-mediated supersymmetry in 13 TeV pp collisions with the ATLAS detector".  |
| **[Gambit::Priors](/documentation/code/colliderbit_development/namespaces/namespacegambit_1_1priors/)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Gambit::Priors::Plugin](/documentation/code/colliderbit_development/classes/classgambit_1_1priors_1_1plugin/)**  |

## Detailed Description


declaration for scanner module



------------------

Authors (add name and date if you modify): 




## Source code

```
//  GAMBIT: Global and Modular BSM Inference Tool
//  *********************************************
//

#ifndef PLUGIN_PRIOR_HPP
#define PLUGIN_PRIOR_HPP

#include "gambit/ScannerBit/priors.hpp"
#include "gambit/ScannerBit/plugin_interface.hpp"

namespace Gambit
{
    namespace Priors
    {
        class Plugin : public BasePrior
        {
        private:
            typedef Scanner::Plugins::Plugin_Interface<double (const std::vector<double> &), void (const std::vector<double> &, std::unordered_map<std::string,double> &)> plugin_type;
            mutable plugin_type *plugin;
                
        public:
            Plugin(const std::vector<std::string>& params, const Options& options) : BasePrior(params)
            {
                std::string plugin_name;
                if (options.hasKey("plugin"))
                {
                    plugin_name = options.getValue<std::string>("plugin");
                }
                else
                {
                    scan_err << "Plugin prior:  need to specify plugin with \"plugin\" tag." << scan_end;
                    plugin_name = "";
                }
                plugin = new plugin_type("objective", plugin_name, param_names, sizeRef());
            }
                
            void transform(const std::vector<double> &unitpars, std::unordered_map<std::string,double> &outputMap) const override
            {
                return (*plugin)(unitpars, outputMap);
            }

            std::vector<double> inverse_transform(const std::unordered_map<std::string, double> &) const override
            {
                scan_err << "inverse transform not supported in plugin prior" << scan_end;
                return {};
            }
            
            double operator()(const std::vector<double>& vec) const override
            {
                return (*plugin)(vec);
            }
            
            ~Plugin()
            {
                delete plugin;
            }
        };
        
        LOAD_PRIOR(plugin, Plugin)
    }
}

#endif
```


-------------------------------

Updated on 2022-08-02 at 18:18:37 +0000