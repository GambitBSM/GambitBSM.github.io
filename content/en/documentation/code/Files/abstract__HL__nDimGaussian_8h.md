---
title: "file HepLike_2_0/abstract_HL_nDimGaussian.h"

description: "[No description available]"

---

# file HepLike_2_0/abstract_HL_nDimGaussian.h

[No description available]

## Functions

|                | Name           |
| -------------- | -------------- |
| namespace | **[CAT_3](/documentation/code/files/abstract__hl__ndimgaussian_8h/#function-cat-3)**(BACKENDNAME , _ , SAFE_VERSION ) |


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
#ifndef __abstract_HL_nDimGaussian_HepLike_2_0_h__
#define __abstract_HL_nDimGaussian_HepLike_2_0_h__

#include <cstddef>
#include <iostream>
#include <string>
#include <vector>
#include "gambit/Backends/abstractbase.hpp"
#include "forward_decls_abstract_classes.h"
#include "forward_decls_wrapper_classes.h"
#include <boost/numeric/ublas/matrix.hpp>

#include "identification.hpp"

namespace CAT_3(BACKENDNAME,_,SAFE_VERSION)
{
   
   
   class Abstract_HL_nDimGaussian : public virtual AbstractBase
   {
      public:
   
         virtual void Read() =0;
   
         virtual double GetChi2(std::vector<double>) =0;
   
         virtual double GetLikelihood(std::vector<double>) =0;
   
         virtual double GetLogLikelihood(std::vector<double>) =0;
   
         virtual double GetChi2(std::vector<double>, boost::numeric::ublas::matrix<double>) =0;
   
         virtual double GetLikelihood(std::vector<double>, boost::numeric::ublas::matrix<double>) =0;
   
         virtual double GetLogLikelihood(std::vector<double>, boost::numeric::ublas::matrix<double>) =0;
   
         virtual bool Restrict(std::vector<std::string>) =0;
   
         virtual ::std::vector<std::string> GetObservables() =0;
   
      public:
         virtual void pointer_assign__BOSS(Abstract_HL_nDimGaussian*) =0;
         virtual Abstract_HL_nDimGaussian* pointer_copy__BOSS() =0;
   
      private:
         HL_nDimGaussian* wptr;
         bool delete_wrapper;
      public:
         HL_nDimGaussian* get_wptr() { return wptr; }
         void set_wptr(HL_nDimGaussian* wptr_in) { wptr = wptr_in; }
         bool get_delete_wrapper() { return delete_wrapper; }
         void set_delete_wrapper(bool del_wrp_in) { delete_wrapper = del_wrp_in; }
   
      public:
         Abstract_HL_nDimGaussian()
         {
            wptr = 0;
            delete_wrapper = false;
         }
   
         Abstract_HL_nDimGaussian(const Abstract_HL_nDimGaussian&)
         {
            wptr = 0;
            delete_wrapper = false;
         }
   
         Abstract_HL_nDimGaussian& operator=(const Abstract_HL_nDimGaussian&) { return *this; }
   
         virtual void init_wrapper() =0;
   
         HL_nDimGaussian* get_init_wptr()
         {
            init_wrapper();
            return wptr;
         }
   
         HL_nDimGaussian& get_init_wref()
         {
            init_wrapper();
            return *wptr;
         }
   
         virtual ~Abstract_HL_nDimGaussian() =0;
   };
   
}


#include "gambit/Backends/backend_undefs.hpp"


#endif /* __abstract_HL_nDimGaussian_HepLike_2_0_h__ */
```


-------------------------------

Updated on 2025-02-12 at 16:10:36 +0000
