---
title: "file Pythia_8_312/wrapper_LHdecayChannel_decl.h"

description: "[No description available]"

---

# file Pythia_8_312/wrapper_LHdecayChannel_decl.h

[No description available]

## Functions

|                | Name           |
| -------------- | -------------- |
| namespace | **[CAT_3](/documentation/code/files/wrapper__lhdecaychannel__decl_8h/#function-cat-3)**(BACKENDNAME , _ , SAFE_VERSION ) |


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
#ifndef __wrapper_LHdecayChannel_decl_Pythia_8_312_h__
#define __wrapper_LHdecayChannel_decl_Pythia_8_312_h__

#include <cstddef>
#include <vector>
#include <string>
#include "forward_decls_wrapper_classes.h"
#include "gambit/Backends/wrapperbase.hpp"
#include "abstract_LHdecayChannel.h"

#include "identification.hpp"

namespace CAT_3(BACKENDNAME,_,SAFE_VERSION)
{
    
    namespace Pythia8
    {
        
        class LHdecayChannel : public WrapperBase
        {
                // Member variables: 
            public:
                // -- Static factory pointers: 
                static Abstract_LHdecayChannel* (*__factory0)();
                static Abstract_LHdecayChannel* (*__factory1)(double, int, std::vector<int>, std::string);
                static Abstract_LHdecayChannel* (*__factory2)(double, int, std::vector<int>);
        
                // -- Other member variables: 
        
                // Member functions: 
            public:
                void setChannel(double bratIn, int nDaIn, std::vector<int> idDaIn, std::string cIn);
        
                void setChannel(double bratIn, int nDaIn, std::vector<int> idDaIn);
        
                void setBrat(double bratIn);
        
                void setIdDa(std::vector<int> idDaIn);
        
                double getBrat();
        
                int getNDa();
        
                ::std::vector<int> getIdDa();
        
                ::std::string getComment();
        
        
                // Wrappers for original constructors: 
            public:
                LHdecayChannel();
                LHdecayChannel(double bratIn, int nDaIn, std::vector<int> idDaIn, std::string cIn);
                LHdecayChannel(double bratIn, int nDaIn, std::vector<int> idDaIn);
        
                // Special pointer-based constructor: 
                LHdecayChannel(Abstract_LHdecayChannel* in);
        
                // Copy constructor: 
                LHdecayChannel(const LHdecayChannel& in);
        
                // Assignment operator: 
                LHdecayChannel& operator=(const LHdecayChannel& in);
        
                // Destructor: 
                ~LHdecayChannel();
        
                // Returns correctly casted pointer to Abstract class: 
                Abstract_LHdecayChannel* get_BEptr() const;
        
        };
    }
    
}


#include "gambit/Backends/backend_undefs.hpp"

#endif /* __wrapper_LHdecayChannel_decl_Pythia_8_312_h__ */
```


-------------------------------

Updated on 2025-02-12 at 15:36:43 +0000
