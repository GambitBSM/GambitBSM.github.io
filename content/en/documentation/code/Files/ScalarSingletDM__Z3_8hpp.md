---
title: "file models/ScalarSingletDM_Z3.hpp"

description: "[No description available]"

---

# file models/ScalarSingletDM_Z3.hpp

[No description available]

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/scalarsingletdm__z3_8hpp/#define-model)**  |
|  | **[PARENT](/documentation/code/files/scalarsingletdm__z3_8hpp/#define-parent)**  |




## Macros Documentation

### define MODEL

```
#define MODEL ScalarSingletDM_Z3
```


Z3 scalar singlet dark matter without running parameters.



------------------


# Authors

James McKay 

2015 September

Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 

2018 Sep



------------------


### define PARENT

```
#define PARENT ScalarSingletDM_Z3_running
```


## Source code

```
//  GAMBIT: Global and Modular BSM Inference Tool
//  *********************************************
///
///  Z3 scalar singlet dark matter without running
///  parameters.
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

#ifndef __ScalarSingletDM_Z3_hpp__
#define __ScalarSingletDM_Z3_hpp__

// Must include models that are targets of translation functions
#include "gambit/Models/models/ScalarSingletDM_Z3_running.hpp"

#define MODEL ScalarSingletDM_Z3
#define PARENT ScalarSingletDM_Z3_running
  START_MODEL
  DEFINEPARS(mS, lambda_hS, mu3)
  // Translate this model into ScalarSingletDM_Z3_running
  INTERPRET_AS_PARENT_FUNCTION(ScalarSingletDM_Z3_to_ScalarSingletDM_Z3_running)
#undef PARENT
#undef MODEL

#endif
```


-------------------------------

Updated on 2022-09-07 at 23:22:09 +0000
