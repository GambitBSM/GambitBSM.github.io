---
title: "file HepLike_2_0/wrapper_HL_nDimBifurGaussian_def.h"

description: "[No description available]"

---

# file HepLike_2_0/wrapper_HL_nDimBifurGaussian_def.h

[No description available]

## Functions

|                | Name           |
| -------------- | -------------- |
| namespace | **[CAT_3](/documentation/code/files/wrapper__hl__ndimbifurgaussian__def_8h/#function-cat-3)**(BACKENDNAME , _ , SAFE_VERSION ) |


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
#ifndef __wrapper_HL_nDimBifurGaussian_def_HepLike_2_0_h__
#define __wrapper_HL_nDimBifurGaussian_def_HepLike_2_0_h__

#include <string>
#include <vector>
#include <boost/numeric/ublas/matrix.hpp>

#include "identification.hpp"

namespace CAT_3(BACKENDNAME,_,SAFE_VERSION)
{
   
   
   // Member functions: 
   inline void HL_nDimBifurGaussian::Read()
   {
      get_BEptr()->Read();
   }
   
   inline double HL_nDimBifurGaussian::GetChi2(std::vector<double> theory)
   {
      return get_BEptr()->GetChi2(theory);
   }
   
   inline double HL_nDimBifurGaussian::GetLikelihood(std::vector<double> theory)
   {
      return get_BEptr()->GetLikelihood(theory);
   }
   
   inline double HL_nDimBifurGaussian::GetLogLikelihood(std::vector<double> theory)
   {
      return get_BEptr()->GetLogLikelihood(theory);
   }
   
   inline double HL_nDimBifurGaussian::GetChi2(std::vector<double> theory, boost::numeric::ublas::matrix<double> theory_cov)
   {
      return get_BEptr()->GetChi2(theory, theory_cov);
   }
   
   inline double HL_nDimBifurGaussian::GetLikelihood(std::vector<double> theory, boost::numeric::ublas::matrix<double> theory_cov)
   {
      return get_BEptr()->GetLikelihood(theory, theory_cov);
   }
   
   inline double HL_nDimBifurGaussian::GetLogLikelihood(std::vector<double> theory, boost::numeric::ublas::matrix<double> theory_cov)
   {
      return get_BEptr()->GetLogLikelihood(theory, theory_cov);
   }
   
   inline bool HL_nDimBifurGaussian::Restrict(std::vector<std::string> arg_1)
   {
      return get_BEptr()->Restrict(arg_1);
   }
   
   inline ::std::vector<std::string> HL_nDimBifurGaussian::GetObservables()
   {
      return get_BEptr()->GetObservables();
   }
   
   
   // Wrappers for original constructors: 
   inline HL_nDimBifurGaussian::HL_nDimBifurGaussian() :
      WrapperBase(__factory0())
   {
      get_BEptr()->set_wptr(this);
      get_BEptr()->set_delete_wrapper(false);
   }
   
   inline HL_nDimBifurGaussian::HL_nDimBifurGaussian(std::string s) :
      WrapperBase(__factory1(s))
   {
      get_BEptr()->set_wptr(this);
      get_BEptr()->set_delete_wrapper(false);
   }
   
   // Special pointer-based constructor: 
   inline HL_nDimBifurGaussian::HL_nDimBifurGaussian(Abstract_HL_nDimBifurGaussian* in) :
      WrapperBase(in)
   {
      get_BEptr()->set_wptr(this);
      get_BEptr()->set_delete_wrapper(false);
   }
   
   // Copy constructor: 
   inline HL_nDimBifurGaussian::HL_nDimBifurGaussian(const HL_nDimBifurGaussian& in) :
      WrapperBase(in.get_BEptr()->pointer_copy__BOSS())
   {
      get_BEptr()->set_wptr(this);
      get_BEptr()->set_delete_wrapper(false);
   }
   
   // Assignment operator: 
   inline HL_nDimBifurGaussian& HL_nDimBifurGaussian::operator=(const HL_nDimBifurGaussian& in)
   {
      if (this != &in)
      {
         get_BEptr()->pointer_assign__BOSS(in.get_BEptr());
      }
      return *this;
   }
   
   
   // Destructor: 
   inline HL_nDimBifurGaussian::~HL_nDimBifurGaussian()
   {
      if (get_BEptr() != 0)
      {
         get_BEptr()->set_delete_wrapper(false);
         if (can_delete_BEptr())
         {
            delete BEptr;
            BEptr = 0;
         }
      }
      set_delete_BEptr(false);
   }
   
   // Returns correctly casted pointer to Abstract class: 
   inline Abstract_HL_nDimBifurGaussian* HL_nDimBifurGaussian::get_BEptr() const
   {
      return dynamic_cast<Abstract_HL_nDimBifurGaussian*>(BEptr);
   }
   
}


#include "gambit/Backends/backend_undefs.hpp"

#endif /* __wrapper_HL_nDimBifurGaussian_def_HepLike_2_0_h__ */
```


-------------------------------

Updated on 2025-02-12 at 16:10:36 +0000
