---
title: 'file models/HaloModels_Einasto.hpp'

description: "[No description available]"

---

# models/HaloModels_Einasto.hpp

[No description available]

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/halomodels__einasto_8hpp/#define-model)**  |
|  | **[MODEL](/documentation/code/files/halomodels__einasto_8hpp/#define-model)**  |
|  | **[PARENT](/documentation/code/files/halomodels__einasto_8hpp/#define-parent)**  |
|  | **[MODEL](/documentation/code/files/halomodels__einasto_8hpp/#define-model)**  |
|  | **[PARENT](/documentation/code/files/halomodels__einasto_8hpp/#define-parent)**  |




## Macros Documentation

### define MODEL

```
#define MODEL Halo_Einasto
```


### define MODEL

```
#define MODEL Halo_Einasto
```


### define PARENT

```
#define PARENT Halo_Einasto
```


### define MODEL

```
#define MODEL Halo_Einasto
```


### define PARENT

```
#define PARENT Halo_Einasto
```


## Source code

```
//  GAMBIT: Global and Modular BSM Inference Tool
//  *********************************************
//
//  Local and global Milky Way Halo Model 
//  (Einasto profile, local Maxwellian halo)
//
//  *********************************************
//
//  Authors
//  =======
//
//  (add name and date if you modify)
//
//  Sebastian Wild
//  2016 Aug
//
//  *********************************************

#ifndef __HaloModels_Einasto_hpp__
#define __HaloModels_Einasto_hpp__

#define MODEL Halo_Einasto
  START_MODEL
  DEFINEPARS(rho0, rhos, vrot, v0, vesc, rs, r_sun, alpha)
#undef MODEL

#define MODEL Halo_Einasto_rho0
#define PARENT Halo_Einasto
  START_MODEL
  DEFINEPARS(rho0, vrot, v0, vesc, rs, r_sun, alpha)
  INTERPRET_AS_PARENT_FUNCTION(Halo_Einasto_rho0_to_Halo_Einasto)
#undef PARENT
#undef MODEL

#define MODEL Halo_Einasto_rhos
#define PARENT Halo_Einasto
  START_MODEL
  DEFINEPARS(rhos, vrot, v0, vesc, rs, r_sun, alpha)
  INTERPRET_AS_PARENT_FUNCTION(Halo_Einasto_rhos_to_Halo_Einasto)
#undef PARENT
#undef MODEL

#endif
```


-------------------------------

Updated on 2022-09-07 at 14:07:48 +0000
