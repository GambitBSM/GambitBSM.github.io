---
title: "file HepLike_2_0/HepLike_2_0/loaded_types.hpp"

description: "[No description available]"

---

# file HepLike_2_0/HepLike_2_0/loaded_types.hpp

[No description available]

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[HepLike_2_0_all_data](/documentation/code/files/heplike__2__0_2loaded__types_8hpp/#define-heplike-2-0-all-data)**  |




## Macros Documentation

### define HepLike_2_0_all_data

```
#define HepLike_2_0_all_data   (( /*class*/(HL_Gaussian),    /*constructors*/((("Factory_HL_Gaussian_0__BOSS_1","_Factory_HL_Gaussian_0__BOSS_1"),())) ((("Factory_HL_Gaussian_1__BOSS_2","_Factory_HL_Gaussian_1__BOSS_2"),(std::string))) )) \
  (( /*class*/(HL_BifurGaussian),    /*constructors*/((("Factory_HL_BifurGaussian_0__BOSS_3","_Factory_HL_BifurGaussian_0__BOSS_3"),())) ((("Factory_HL_BifurGaussian_1__BOSS_4","_Factory_HL_BifurGaussian_1__BOSS_4"),(std::string))) )) \
  (( /*class*/(HL_ProfLikelihood),    /*constructors*/((("Factory_HL_ProfLikelihood_0__BOSS_5","_Factory_HL_ProfLikelihood_0__BOSS_5"),())) ((("Factory_HL_ProfLikelihood_1__BOSS_6","_Factory_HL_ProfLikelihood_1__BOSS_6"),(std::string))) )) \
  (( /*class*/(HL_nDimBifurGaussian),    /*constructors*/((("Factory_HL_nDimBifurGaussian_0__BOSS_7","_Factory_HL_nDimBifurGaussian_0__BOSS_7"),())) ((("Factory_HL_nDimBifurGaussian_1__BOSS_8","_Factory_HL_nDimBifurGaussian_1__BOSS_8"),(std::string))) )) \
  (( /*class*/(HL_nDimGaussian),    /*constructors*/((("Factory_HL_nDimGaussian_0__BOSS_9","_Factory_HL_nDimGaussian_0__BOSS_9"),())) ((("Factory_HL_nDimGaussian_1__BOSS_10","_Factory_HL_nDimGaussian_1__BOSS_10"),(std::string))) )) \
  (( /*class*/(HL_nDimLikelihood),    /*constructors*/((("Factory_HL_nDimLikelihood_0__BOSS_11","_Factory_HL_nDimLikelihood_0__BOSS_11"),())) ((("Factory_HL_nDimLikelihood_1__BOSS_12","_Factory_HL_nDimLikelihood_1__BOSS_12"),(std::string))) )) \
```


## Source code

```
#ifndef __loaded_types_HepLike_2_0_hpp__
#define __loaded_types_HepLike_2_0_hpp__ 1

#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#include "wrapper_HL_Gaussian.h"
#include "wrapper_HL_BifurGaussian.h"
#include "wrapper_HL_ProfLikelihood.h"
#include "wrapper_HL_nDimBifurGaussian.h"
#include "wrapper_HL_nDimGaussian.h"
#include "wrapper_HL_nDimLikelihood.h"
#include "identification.hpp"
#pragma GCC diagnostic pop

// Indicate which types are provided by this backend, and what the symbols of their factories are.
#define HepLike_2_0_all_data \
  (( /*class*/(HL_Gaussian),    /*constructors*/((("Factory_HL_Gaussian_0__BOSS_1","_Factory_HL_Gaussian_0__BOSS_1"),())) ((("Factory_HL_Gaussian_1__BOSS_2","_Factory_HL_Gaussian_1__BOSS_2"),(std::string))) )) \
  (( /*class*/(HL_BifurGaussian),    /*constructors*/((("Factory_HL_BifurGaussian_0__BOSS_3","_Factory_HL_BifurGaussian_0__BOSS_3"),())) ((("Factory_HL_BifurGaussian_1__BOSS_4","_Factory_HL_BifurGaussian_1__BOSS_4"),(std::string))) )) \
  (( /*class*/(HL_ProfLikelihood),    /*constructors*/((("Factory_HL_ProfLikelihood_0__BOSS_5","_Factory_HL_ProfLikelihood_0__BOSS_5"),())) ((("Factory_HL_ProfLikelihood_1__BOSS_6","_Factory_HL_ProfLikelihood_1__BOSS_6"),(std::string))) )) \
  (( /*class*/(HL_nDimBifurGaussian),    /*constructors*/((("Factory_HL_nDimBifurGaussian_0__BOSS_7","_Factory_HL_nDimBifurGaussian_0__BOSS_7"),())) ((("Factory_HL_nDimBifurGaussian_1__BOSS_8","_Factory_HL_nDimBifurGaussian_1__BOSS_8"),(std::string))) )) \
  (( /*class*/(HL_nDimGaussian),    /*constructors*/((("Factory_HL_nDimGaussian_0__BOSS_9","_Factory_HL_nDimGaussian_0__BOSS_9"),())) ((("Factory_HL_nDimGaussian_1__BOSS_10","_Factory_HL_nDimGaussian_1__BOSS_10"),(std::string))) )) \
  (( /*class*/(HL_nDimLikelihood),    /*constructors*/((("Factory_HL_nDimLikelihood_0__BOSS_11","_Factory_HL_nDimLikelihood_0__BOSS_11"),())) ((("Factory_HL_nDimLikelihood_1__BOSS_12","_Factory_HL_nDimLikelihood_1__BOSS_12"),(std::string))) )) \

// If the default version has been loaded, set it as default.
#if ALREADY_LOADED(CAT_3(BACKENDNAME,_,CAT(Default_,BACKENDNAME)))
  SET_DEFAULT_VERSION_FOR_LOADING_TYPES(BACKENDNAME,SAFE_VERSION,CAT(Default_,BACKENDNAME))
#endif

// Undefine macros to avoid conflict with other backends.
#include "gambit/Backends/backend_undefs.hpp"

#endif /* __loaded_types_HepLike_2_0_hpp__ */
```


-------------------------------

Updated on 2024-07-18 at 13:53:35 +0000
