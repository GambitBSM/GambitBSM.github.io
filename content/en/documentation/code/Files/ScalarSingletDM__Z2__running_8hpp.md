---
title: 'file models/ScalarSingletDM_Z2_running.hpp'

description: "[No description available]"

---

# models/ScalarSingletDM_Z2_running.hpp



[No description available]

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/scalarsingletdm__z2__running_8hpp/#define-model)**  |




## Macros Documentation

### define MODEL

```
#define MODEL ScalarSingletDM_Z2_running
```


Scalar singlet dark matter with running mass and quartic coupling 

------------------


# Authors

(add name and date if you modify) Christoph Weniger 

2014 January

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
///  Scalar singlet dark matter with running mass
///  and quartic coupling
///  *********************************************
///
///  Authors
///  =======
///
///  (add name and date if you modify)
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

#ifndef __ScalarSingletDM_Z2_running_hpp__
#define __ScalarSingletDM_Z2_running_hpp__

#define MODEL ScalarSingletDM_Z2_running
  START_MODEL
  DEFINEPARS(mS, lambda_hS, lambda_S)
#undef MODEL

#endif
```


-------------------------------

Updated on 2022-09-07 at 13:49:53 +0000
