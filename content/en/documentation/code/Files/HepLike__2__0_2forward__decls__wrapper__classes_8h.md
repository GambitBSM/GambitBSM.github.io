---
title: "file HepLike_2_0/HepLike_2_0/forward_decls_wrapper_classes.h"

description: "[No description available]"

---

# file HepLike_2_0/HepLike_2_0/forward_decls_wrapper_classes.h

[No description available]

## Functions

|                | Name           |
| -------------- | -------------- |
| namespace | **[CAT_3](/documentation/code/files/heplike__2__0_2forward__decls__wrapper__classes_8h/#function-cat-3)**(BACKENDNAME , _ , SAFE_VERSION ) |


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
#ifndef __forward_decls_wrapper_classes_HepLike_2_0_h__
#define __forward_decls_wrapper_classes_HepLike_2_0_h__


#include "identification.hpp"

namespace CAT_3(BACKENDNAME,_,SAFE_VERSION)
{
   
   
   class HL_Gaussian;
   class HL_BifurGaussian;
   class HL_ProfLikelihood;
   class HL_nDimBifurGaussian;
   class HL_nDimGaussian;
   class HL_nDimLikelihood;
   
   
}


#include "gambit/Backends/backend_undefs.hpp"

#endif /* __forward_decls_wrapper_classes_HepLike_2_0_h__ */
```


-------------------------------

Updated on 2023-06-26 at 21:36:57 +0000
