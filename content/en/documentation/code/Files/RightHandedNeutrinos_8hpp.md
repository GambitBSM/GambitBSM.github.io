---
title: "file models/RightHandedNeutrinos.hpp"

description: "[No description available]"

---

# file models/RightHandedNeutrinos.hpp

[No description available]

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/righthandedneutrinos_8hpp/#define-model)**  |




## Macros Documentation

### define MODEL

```
#define MODEL RightHandedNeutrinos
```


## Source code

```
// GAMBIT: Global and Modular BSM Inference Tool
//
// *********************************************
//
// RH Neutrino Model
//
// *********************************************
//
// Authors
// =======
//
// (add name and date if you modify)
//
// \author Suraj Krishnamurthy
// \date 2017 February
//
// \author Tomas Gonzalo
//         (t.e.gonzalo@fys.uio.no)
// \date 2018 Jan
//
// *********************************************

#ifndef __RightHandedNeutrinos_hpp__
#define __RightHandedNeutrinos_hpp__

#define MODEL RightHandedNeutrinos
  START_MODEL
  DEFINEPARS(M_1, M_2, M_3, ReOm23, ImOm23, ReOm13, ImOm13, ReOm12, ImOm12, Rorder)
#undef MODEL

#endif
```


-------------------------------

Updated on 2022-09-07 at 23:22:09 +0000
