---
title: "file HepLike_2_0/wrapper_HL_nDimBifurGaussian_decl.h"

description: "[No description available]"

---

# file HepLike_2_0/wrapper_HL_nDimBifurGaussian_decl.h

[No description available]

## Functions

|                | Name           |
| -------------- | -------------- |
| namespace | **[CAT_3](/documentation/code/files/wrapper__hl__ndimbifurgaussian__decl_8h/#function-cat-3)**(BACKENDNAME , _ , SAFE_VERSION ) |


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
#ifndef __wrapper_HL_nDimBifurGaussian_decl_HepLike_2_0_h__
#define __wrapper_HL_nDimBifurGaussian_decl_HepLike_2_0_h__

#include <cstddef>
#include <string>
#include <vector>
#include "forward_decls_wrapper_classes.h"
#include "gambit/Backends/wrapperbase.hpp"
#include "abstract_HL_nDimBifurGaussian.h"
#include <boost/numeric/ublas/matrix.hpp>

#include "identification.hpp"

namespace CAT_3(BACKENDNAME,_,SAFE_VERSION)
{
   
   
   class HL_nDimBifurGaussian : public WrapperBase
   {
         // Member variables: 
      public:
         // -- Static factory pointers: 
         static Abstract_HL_nDimBifurGaussian* (*__factory0)();
         static Abstract_HL_nDimBifurGaussian* (*__factory1)(std::string);
   
         // -- Other member variables: 
   
         // Member functions: 
      public:
         void Read();
   
         double GetChi2(std::vector<double> theory);
   
         double GetLikelihood(std::vector<double> theory);
   
         double GetLogLikelihood(std::vector<double> theory);
   
         double GetChi2(std::vector<double> theory, boost::numeric::ublas::matrix<double> theory_cov);
   
         double GetLikelihood(std::vector<double> theory, boost::numeric::ublas::matrix<double> theory_cov);
   
         double GetLogLikelihood(std::vector<double> theory, boost::numeric::ublas::matrix<double> theory_cov);
   
         bool Restrict(std::vector<std::string> arg_1);
   
         ::std::vector<std::string> GetObservables();
   
   
         // Wrappers for original constructors: 
      public:
         HL_nDimBifurGaussian();
         HL_nDimBifurGaussian(std::string s);
   
         // Special pointer-based constructor: 
         HL_nDimBifurGaussian(Abstract_HL_nDimBifurGaussian* in);
   
         // Copy constructor: 
         HL_nDimBifurGaussian(const HL_nDimBifurGaussian& in);
   
         // Assignment operator: 
         HL_nDimBifurGaussian& operator=(const HL_nDimBifurGaussian& in);
   
         // Destructor: 
         ~HL_nDimBifurGaussian();
   
         // Returns correctly casted pointer to Abstract class: 
         Abstract_HL_nDimBifurGaussian* get_BEptr() const;
   
   };
   
}


#include "gambit/Backends/backend_undefs.hpp"

#endif /* __wrapper_HL_nDimBifurGaussian_decl_HepLike_2_0_h__ */
```


-------------------------------

Updated on 2025-02-12 at 16:10:36 +0000
