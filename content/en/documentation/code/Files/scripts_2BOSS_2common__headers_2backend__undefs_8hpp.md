---
title: "file common_headers/scripts/BOSS/common_headers/backend_undefs.hpp"

description: "[No description available]"

---

# file common_headers/scripts/BOSS/common_headers/backend_undefs.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[DO_CLASSLOADING](/documentation/code/files/scripts_2boss_2common__headers_2backend__undefs_8hpp/#define-do-classloading)**  |

## Detailed Description


**Author**: 

  * Pat Scott ([patscott@physics.mcgill.ca](mailto:patscott@physics.mcgill.ca)) 
  * Tomas Gonzalo ([t.e.gonzalo@fys.uio.no](mailto:t.e.gonzalo@fys.uio.no)) 


**Date**: 

  * 2014 Sep
  * 2016 Sep


Undef backend identification things to prevent clashes with other backends.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define DO_CLASSLOADING

```
#define DO_CLASSLOADING 0
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Undef backend identification things to prevent
///  clashes with other backends.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///   
///  \author Pat Scott 
///          (patscott@physics.mcgill.ca)
///  \date 2014 Sep
///
///  \author Tomas Gonzalo
///          (t.e.gonzalo@fys.uio.no)
///  \date 2016 Sep
///
///  *********************************************

#undef LIBPATH 
#undef BACKENDNAME
#undef BACKENDLANG
#undef VERSION
#undef SAFE_VERSION
#undef REFERENCE
#undef DO_CLASSLOADING
#define DO_CLASSLOADING 0
```


-------------------------------

Updated on 2024-07-18 at 13:53:35 +0000
