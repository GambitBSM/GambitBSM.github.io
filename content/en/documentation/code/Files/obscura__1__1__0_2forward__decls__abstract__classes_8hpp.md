---
title: "file obscura_1_1_0/obscura_1_1_0/forward_decls_abstract_classes.hpp"

description: "[No description available]"

---

# file obscura_1_1_0/obscura_1_1_0/forward_decls_abstract_classes.hpp

[No description available]

## Functions

|                | Name           |
| -------------- | -------------- |
| namespace | **[CAT_3](/documentation/code/files/obscura__1__1__0_2forward__decls__abstract__classes_8hpp/#function-cat-3)**(BACKENDNAME , _ , SAFE_VERSION ) |


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
#ifndef __forward_decls_abstract_classes_obscura_1_1_0_hpp__
#define __forward_decls_abstract_classes_obscura_1_1_0_hpp__


#include "identification.hpp"

namespace CAT_3(BACKENDNAME,_,SAFE_VERSION)
{
    
    
    
    namespace obscura
    {
        class Abstract_DM_Distribution;
        class Abstract_Standard_Halo_Model;
    }
    
    namespace obscura
    {
        class Abstract_DM_Particle_Standard;
        class Abstract_DM_Particle_SI;
        class Abstract_DM_Particle;
    }
    
    namespace obscura
    {
        class Abstract_DM_Detector;
    }
    
    namespace obscura
    {
        class Abstract_DM_Detector_Crystal;
    }
    
    namespace obscura
    {
        class Abstract_DM_Detector_Ionization_ER;
        class Abstract_DM_Detector_Ionization;
    }
    
    
    namespace obscura
    {
        class Abstract_DM_Detector_Ionization_Migdal;
    }
    
    
    
}


#include "gambit/Backends/backend_undefs.hpp"

#endif /* __forward_decls_abstract_classes_obscura_1_1_0_hpp__ */
```


-------------------------------

Updated on 2025-02-12 at 16:10:36 +0000
