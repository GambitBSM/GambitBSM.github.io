---
title: "file vevacious_1_0/wrapper_VevaciousPlusPlus_decl.hpp"

description: "[No description available]"

---

# file vevacious_1_0/wrapper_VevaciousPlusPlus_decl.hpp

[No description available]

## Functions

|                | Name           |
| -------------- | -------------- |
| namespace | **[CAT_3](/documentation/code/files/wrapper__vevaciousplusplus__decl_8hpp/#function-cat-3)**(BACKENDNAME , _ , SAFE_VERSION ) |


## Functions Documentation

### function CAT_3

```
namespace CAT_3(
    BACKENDNAME ,
    _ ,
    SAFE_VERSION 
)
```




## Source code

```
#ifndef __wrapper_VevaciousPlusPlus_decl_vevacious_1_0_hpp__
#define __wrapper_VevaciousPlusPlus_decl_vevacious_1_0_hpp__

#include <cstddef>
#include <string>
#include <utility>
#include <vector>
#include "forward_decls_wrapper_classes.hpp"
#include "gambit/Backends/wrapperbase.hpp"
#include "abstract_VevaciousPlusPlus.hpp"

#include "identification.hpp"

namespace CAT_3(BACKENDNAME,_,SAFE_VERSION)
{
    
    namespace VevaciousPlusPlus
    {
        
        class VevaciousPlusPlus : public WrapperBase
        {
                // Member variables: 
            public:
                // -- Static factory pointers: 
                static Abstract_VevaciousPlusPlus* (*__factory0)(const std::string&);
        
                // -- Other member variables: 
        
                // Member functions: 
            public:
                void RunPoint(const std::string& newInput);
        
                ::std::pair<std::vector<double>, std::vector<double>> GetPanicVacua();
        
                ::std::pair<std::vector<double>, std::vector<double>> RunVacua(const std::string& newInput);
        
                void ReadLhaBlock(const std::string& uppercaseBlockName, const double scale, const std::vector<std::pair<int, double>>& parameters, const int dimension);
        
                void WriteResultsAsXmlFile(const std::string& xmlFilename);
        
                ::std::string GetResultsAsString();
        
                double GetLifetimeInSeconds();
        
                double GetThermalProbability();
        
                double GetThermalDecayWidth();
        
                ::std::vector<double> GetThresholdAndActions();
        
                ::std::vector<double> GetThermalThresholdAndActions();
        
                void AppendResultsToLhaFile(const std::string& lhaFilename, const bool writeWarnings);
        
                void AppendResultsToLhaFile(const std::string& lhaFilename);
        
        
                // Wrappers for original constructors: 
            public:
                VevaciousPlusPlus(const std::string& initializationFileName);
        
                // Special pointer-based constructor: 
                VevaciousPlusPlus(Abstract_VevaciousPlusPlus* in);
        
                // Destructor: 
                ~VevaciousPlusPlus();
        
                // Returns correctly casted pointer to Abstract class: 
                Abstract_VevaciousPlusPlus* get_BEptr() const;
        
        };
    }
    
}


#include "gambit/Backends/backend_undefs.hpp"

#endif /* __wrapper_VevaciousPlusPlus_decl_vevacious_1_0_hpp__ */
```


-------------------------------

Updated on 2025-02-12 at 16:10:36 +0000
