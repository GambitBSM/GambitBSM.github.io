---
title: "file gm2calc_1_2_0/gm2calc_1_2_0/wrapper_EInvalidInput_decl.hpp"

description: "[No description available]"

---

# file gm2calc_1_2_0/gm2calc_1_2_0/wrapper_EInvalidInput_decl.hpp

[No description available]

## Functions

|                | Name           |
| -------------- | -------------- |
| namespace | **[CAT_3](/documentation/code/files/gm2calc__1__2__0_2wrapper__einvalidinput__decl_8hpp/#function-cat-3)**(BACKENDNAME , _ , SAFE_VERSION ) |


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
#ifndef __wrapper_EInvalidInput_decl_gm2calc_1_2_0_hpp__
#define __wrapper_EInvalidInput_decl_gm2calc_1_2_0_hpp__

#include <cstddef>
#include <string>
#include "forward_decls_wrapper_classes.hpp"
#include "gambit/Backends/wrapperbase.hpp"
#include "abstract_EInvalidInput.hpp"
#include "wrapper_Error_decl.hpp"

#include "identification.hpp"

namespace CAT_3(BACKENDNAME,_,SAFE_VERSION)
{
   
   namespace gm2calc
   {
      
      class EInvalidInput : public Error
      {
            // Member variables: 
         public:
            // -- Static factory pointers: 
            static Abstract_EInvalidInput* (*__factory0)(const std::string&);
      
            // -- Other member variables: 
      
            // Member functions: 
         public:
            ::std::string what() const;
      
      
            // Wrappers for original constructors: 
         public:
            EInvalidInput(const std::string& message_);
      
            // Special pointer-based constructor: 
            EInvalidInput(Abstract_EInvalidInput* in);
      
            // Copy constructor: 
            EInvalidInput(const EInvalidInput& in);
      
            // Assignment operator: 
            EInvalidInput& operator=(const EInvalidInput& in);
      
            // Destructor: 
            ~EInvalidInput();
      
            // Returns correctly casted pointer to Abstract class: 
            Abstract_EInvalidInput* get_BEptr() const;
      
      };
   }
   
}


#include "gambit/Backends/backend_undefs.hpp"

#endif /* __wrapper_EInvalidInput_decl_gm2calc_1_2_0_hpp__ */
```


-------------------------------

Updated on 2025-02-12 at 16:10:36 +0000
