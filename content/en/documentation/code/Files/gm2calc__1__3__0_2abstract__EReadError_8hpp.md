---
title: "file gm2calc_1_3_0/gm2calc_1_3_0/abstract_EReadError.hpp"

description: "[No description available]"

---

# file gm2calc_1_3_0/gm2calc_1_3_0/abstract_EReadError.hpp

[No description available]

## Functions

|                | Name           |
| -------------- | -------------- |
| namespace | **[CAT_3](/documentation/code/files/gm2calc__1__3__0_2abstract__ereaderror_8hpp/#function-cat-3)**(BACKENDNAME , _ , SAFE_VERSION ) |


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
#ifndef __abstract_EReadError_gm2calc_1_3_0_hpp__
#define __abstract_EReadError_gm2calc_1_3_0_hpp__

#include <cstddef>
#include <iostream>
#include <string>
#include "gambit/Backends/abstractbase.hpp"
#include "forward_decls_abstract_classes.hpp"
#include "forward_decls_wrapper_classes.hpp"
#include "wrapper_Error_decl.hpp"

#include "identification.hpp"

namespace CAT_3(BACKENDNAME,_,SAFE_VERSION)
{
   
   
   namespace gm2calc
   {
      class Abstract_EReadError : virtual public gm2calc::Abstract_Error
      {
         public:
   
            virtual ::std::string what() const =0;
   
         public:
            using gm2calc::Abstract_Error::pointer_assign__BOSS;
            virtual void pointer_assign__BOSS(Abstract_EReadError*) =0;
            virtual Abstract_EReadError* pointer_copy__BOSS() =0;
   
         private:
            EReadError* wptr;
            bool delete_wrapper;
         public:
            EReadError* get_wptr() { return wptr; }
            void set_wptr(EReadError* wptr_in) { wptr = wptr_in; }
            bool get_delete_wrapper() { return delete_wrapper; }
            void set_delete_wrapper(bool del_wrp_in) { delete_wrapper = del_wrp_in; }
   
         public:
            Abstract_EReadError()
            {
               wptr = 0;
               delete_wrapper = false;
            }
   
            Abstract_EReadError(const Abstract_EReadError& in) : 
               gm2calc::Abstract_Error(in)
            {
               wptr = 0;
               delete_wrapper = false;
            }
   
            Abstract_EReadError& operator=(const Abstract_EReadError&) { return *this; }
   
            virtual void init_wrapper() =0;
   
            EReadError* get_init_wptr()
            {
               init_wrapper();
               return wptr;
            }
   
            EReadError& get_init_wref()
            {
               init_wrapper();
               return *wptr;
            }
   
            virtual ~Abstract_EReadError() =0;
      };
   }
   
}


#include "gambit/Backends/backend_undefs.hpp"


#endif /* __abstract_EReadError_gm2calc_1_3_0_hpp__ */
```


-------------------------------

Updated on 2025-02-12 at 16:10:36 +0000
