---
title: "file gm2calc_1_2_0/gm2calc_1_2_0/wrapper_ESetupError_decl.hpp"

description: "[No description available]"

---

# file gm2calc_1_2_0/gm2calc_1_2_0/wrapper_ESetupError_decl.hpp

[No description available]

## Functions

|                | Name           |
| -------------- | -------------- |
| namespace | **[CAT_3](/documentation/code/files/gm2calc__1__2__0_2wrapper__esetuperror__decl_8hpp/#function-cat-3)**(BACKENDNAME , _ , SAFE_VERSION ) |


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
#ifndef __wrapper_ESetupError_decl_gm2calc_1_2_0_hpp__
#define __wrapper_ESetupError_decl_gm2calc_1_2_0_hpp__

#include <cstddef>
#include <string>
#include "forward_decls_wrapper_classes.hpp"
#include "gambit/Backends/wrapperbase.hpp"
#include "abstract_ESetupError.hpp"
#include "wrapper_Error_decl.hpp"

#include "identification.hpp"

namespace CAT_3(BACKENDNAME,_,SAFE_VERSION)
{
   
   namespace gm2calc
   {
      
      class ESetupError : public Error
      {
            // Member variables: 
         public:
            // -- Static factory pointers: 
            static Abstract_ESetupError* (*__factory0)(const std::string&);
      
            // -- Other member variables: 
      
            // Member functions: 
         public:
            ::std::string what() const;
      
      
            // Wrappers for original constructors: 
         public:
            ESetupError(const std::string& message_);
      
            // Special pointer-based constructor: 
            ESetupError(Abstract_ESetupError* in);
      
            // Copy constructor: 
            ESetupError(const ESetupError& in);
      
            // Assignment operator: 
            ESetupError& operator=(const ESetupError& in);
      
            // Destructor: 
            ~ESetupError();
      
            // Returns correctly casted pointer to Abstract class: 
            Abstract_ESetupError* get_BEptr() const;
      
      };
   }
   
}


#include "gambit/Backends/backend_undefs.hpp"

#endif /* __wrapper_ESetupError_decl_gm2calc_1_2_0_hpp__ */
```


-------------------------------

Updated on 2025-02-12 at 16:10:36 +0000
