---
title: "file models/MajoranaSingletDM_Z2.hpp"

description: "[No description available]"

---

# file models/MajoranaSingletDM_Z2.hpp

[No description available]

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/majoranasingletdm__z2_8hpp/#define-majoranasingletdm-z2-hpp-model)**  |
|  | **[MODEL](/documentation/code/files/majoranasingletdm__z2_8hpp/#define-majoranasingletdm-z2-hpp-model)**  |
|  | **[PARENT](/documentation/code/files/majoranasingletdm__z2_8hpp/#define-majoranasingletdm-z2-hpp-parent)**  |




## Macros Documentation

### define MODEL

```
#define MODEL MajoranaSingletDM_Z2
```


Majorana fermion singlet DM



------------------


# Authors

(add name and date if you modify)

Ankit Beniwal 

2016 August, 2017 June

Sebastian Wild 

2018 January

Sanjay Bloor 

2018 August 2020 May



------------------


### define MODEL

```
#define MODEL MajoranaSingletDM_Z2
```


Majorana fermion singlet DM



------------------


# Authors

(add name and date if you modify)

Ankit Beniwal 

2016 August, 2017 June

Sebastian Wild 

2018 January

Sanjay Bloor 

2018 August 2020 May



------------------


### define PARENT

```
#define PARENT MajoranaSingletDM_Z2
```


## Source code

```
//  GAMBIT: Global and Modular BSM Inference Tool
//  *********************************************
///
///  Majorana fermion singlet DM
///
///  *********************************************
///
///  Authors
///  =======
///
///  (add name and date if you modify)
///
///  \author Ankit Beniwal
///  \date 2016 August, 2017 June
///
///  \author Sebastian Wild
///  \date 2018 January
///
///  \author Sanjay Bloor
///  \date 2018 August
///        2020 May
///
///  *********************************************

#ifndef __MajoranaSingletDM_Z2_hpp__
#define __MajoranaSingletDM_Z2_hpp__

#define MODEL MajoranaSingletDM_Z2
  START_MODEL
  DEFINEPARS(mX, lX, xi)
#undef MODEL

#define MODEL MajoranaSingletDM_Z2_sps
#define PARENT MajoranaSingletDM_Z2
  START_MODEL
  DEFINEPARS(mX, lX_s, lX_ps)
  INTERPRET_AS_PARENT_FUNCTION(MajoranaSingletDM_Z2_sps_to_MajoranaSingletDM_Z2)
#undef PARENT
#undef MODEL

#endif
```


-------------------------------

Updated on 2022-09-08 at 02:00:51 +0000
