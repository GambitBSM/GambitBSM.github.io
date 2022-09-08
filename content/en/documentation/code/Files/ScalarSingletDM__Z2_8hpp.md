---
title: "file models/ScalarSingletDM_Z2.hpp"

description: "[No description available]"

---

# file models/ScalarSingletDM_Z2.hpp

[No description available]

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/scalarsingletdm__z2_8hpp/)**  |
|  | **[PARENT](/documentation/code/files/scalarsingletdm__z2_8hpp/)**  |




## Macros Documentation

### define MODEL

```
#define MODEL ScalarSingletDM_Z2
```


Singlet DM



------------------


# Authors

(add name and date if you modify)

Christoph Weniger 

2014 January

James McKay 

2015 September

Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 

2018 Sep



------------------


### define PARENT

```
#define PARENT ScalarSingletDM_Z2_running
```


## Source code

```
//  GAMBIT: Global and Modular BSM Inference Tool
//  *********************************************
///
///  Singlet DM
///
///  *********************************************
///
///  Authors
///  =======
///
///  (add name and date if you modify)
///
///  \author Christoph Weniger
///  \date 2014 January
///
///  \author James McKay
///  \date 2015 September
///
///  \author Pat Scott
///          (p.scott@imperial.ac.uk)
///  \date 2018 Sep
///
///  *********************************************

#ifndef __ScalarSingletDM_Z2_hpp__
#define __ScalarSingletDM_Z2_hpp__

// Must include models that are targets of translation functions
#include "gambit/Models/models/ScalarSingletDM_Z2_running.hpp"

#define MODEL ScalarSingletDM_Z2
#define PARENT ScalarSingletDM_Z2_running
  START_MODEL
  DEFINEPARS(mS, lambda_hS)
  // Translate this model into ScalarSingletDM_Z2_running
  INTERPRET_AS_PARENT_FUNCTION(ScalarSingletDM_Z2_to_ScalarSingletDM_Z2_running)
#undef PARENT
#undef MODEL

#endif
```


-------------------------------

Updated on 2022-09-08 at 01:05:20 +0000
