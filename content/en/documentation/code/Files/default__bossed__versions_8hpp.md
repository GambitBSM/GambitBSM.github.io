---
title: "file Backends/default_bossed_versions.hpp"

description: "[No description available]"

---

# file Backends/default_bossed_versions.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[Default_gm2calc](/documentation/code/files/default__bossed__versions_8hpp/#define-default-gm2calc)**  |
|  | **[Default_Pythia](/documentation/code/files/default__bossed__versions_8hpp/#define-default-pythia)**  |
|  | **[Default_HepLike](/documentation/code/files/default__bossed__versions_8hpp/#define-default-heplike)**  |
|  | **[Default_vevacious](/documentation/code/files/default__bossed__versions_8hpp/#define-default-vevacious)**  |
|  | **[Default_Rivet](/documentation/code/files/default__bossed__versions_8hpp/#define-default-rivet)**  |
|  | **[Default_obscura](/documentation/code/files/default__bossed__versions_8hpp/#define-default-obscura)**  |

## Detailed Description


**Author**: 

  * Pat Scott ([patscott@physics.mcgill.ca](mailto:patscott@physics.mcgill.ca)) 
  * Tomas Gonzalo ([tomas.gonzalo@kit.edu](mailto:tomas.gonzalo@kit.edu)) 


**Date**: 

  * 2014 Nov
  * 2019 Sep, 2024 Apr


Choices about the default versions of backends to use for loading types (specific versions of types can always be used by employing the qualified type BACKENDNAME_SAFEVERSION::TYPE)



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define Default_gm2calc

```
#define Default_gm2calc 1_3_0
```


### define Default_Pythia

```
#define Default_Pythia 8_212
```


### define Default_HepLike

```
#define Default_HepLike 2_0
```


### define Default_vevacious

```
#define Default_vevacious 1_0
```


### define Default_Rivet

```
#define Default_Rivet 3_1_5
```


### define Default_obscura

```
#define Default_obscura 1_1_0
```


## Source code

```
//  *********************************************
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Choices about the default versions of backends
///  to use for loading types (specific versions
///  of types can always be used by employing the
///  qualified type BACKENDNAME_SAFEVERSION::TYPE)
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Pat Scott
///          (patscott@physics.mcgill.ca)
///  \date 2014 Nov
///
///  \author Tomas Gonzalo
///          (tomas.gonzalo@kit.edu)
///  \date 2019 Sep, 2024 Apr
///
///  *********************************************

#pragma once

// Choose default versions here, using underscores instead of periods

#define  Default_gm2calc 1_3_0
#define  Default_Pythia 8_212
#define  Default_HepLike 2_0
#define  Default_vevacious 1_0
#define  Default_Rivet 3_1_5
#define  Default_obscura 1_1_0

// Defaults added by GUM (do not remove this comment).
```


-------------------------------

Updated on 2024-07-18 at 13:53:35 +0000
