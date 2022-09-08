---
title: "file models/ScalarSingletDM_Z3_running.hpp"

description: "[No description available]"

---

# file models/ScalarSingletDM_Z3_running.hpp

[No description available]

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/scalarsingletdm__z3__running_8hpp/#define-model)**  |




## Macros Documentation

### define MODEL

```
#define MODEL ScalarSingletDM_Z3_running
```


Z3 scalar singlet dark matter with running mass and quartic coupling



------------------


# Authors

James McKay 

2015 September

Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 

2018 Sep



------------------


## Source code

```
//  GAMBIT: Global and Modular BSM Inference Tool
//  *********************************************
///
///  Z3 scalar singlet dark matter with running mass
///  and quartic coupling
///
///  *********************************************
///
///  Authors
///  =======
///
///  \author James McKay
///  \date 2015 September
///
///  \author Pat Scott
///          (p.scott@imperial.ac.uk)
///  \date 2018 Sep
///
///  *********************************************

#ifndef __ScalarSingletDM_Z3_running_hpp__
#define __ScalarSingletDM_Z3_running_hpp__

#define MODEL ScalarSingletDM_Z3_running
  START_MODEL
  DEFINEPARS(mS, lambda_hS, lambda_S, mu3)
#undef MODEL

#endif
```


-------------------------------

Updated on 2022-09-08 at 02:23:03 +0000
