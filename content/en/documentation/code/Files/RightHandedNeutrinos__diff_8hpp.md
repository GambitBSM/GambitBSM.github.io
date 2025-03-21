---
title: "file models/RightHandedNeutrinos_diff.hpp"

description: "[No description available]"

---

# file models/RightHandedNeutrinos_diff.hpp

[No description available]

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/righthandedneutrinos__diff_8hpp/#define-model)**  |
|  | **[PARENT](/documentation/code/files/righthandedneutrinos__diff_8hpp/#define-parent)**  |




## Macros Documentation

### define MODEL

```
#define MODEL RightHandedNeutrinos_diff
```


### define PARENT

```
#define PARENT RightHandedNeutrinos
```


## Source code

```
// GAMBIT: Global and Modular BSM Inference Tool
//
// *********************************************
//
// RH Neutrino Model with differential masses
//
// *********************************************
//
// Authors
// =======
//
// (add name and date if you modify)
//
// \author Tomas Gonzalo
//         (t.e.gonzalo@fys.uio.no)
// \date 2017 December
//
// *********************************************

#ifndef __RightHandedNeutrinos_diff_hpp__
#define __RightHandedNeutrinos_diff_hpp__

#include "gambit/Models/models/RightHandedNeutrinos.hpp"

#define MODEL RightHandedNeutrinos_diff
#define PARENT RightHandedNeutrinos
  START_MODEL
  DEFINEPARS(M_1, delta_M21, M_3, ReOm23, ImOm23, ReOm13, ImOm13, ReOm12, ImOm12, Rorder)
  INTERPRET_AS_PARENT_FUNCTION(RightHandedNeutrinos_diff_to_RightHandedNeutrinos)
#undef PARENT
#undef MODEL

#endif
```


-------------------------------

Updated on 2025-02-12 at 16:10:34 +0000
