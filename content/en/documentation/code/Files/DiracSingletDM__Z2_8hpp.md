---
title: 'file models/DiracSingletDM_Z2.hpp'

description: "[No description available]"

---

# models/DiracSingletDM_Z2.hpp



[No description available]

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/diracsingletdm__z2_8hpp/#define-model)**  |
|  | **[MODEL](/documentation/code/files/diracsingletdm__z2_8hpp/#define-model)**  |
|  | **[PARENT](/documentation/code/files/diracsingletdm__z2_8hpp/#define-parent)**  |




## Macros Documentation

### define MODEL

```
#define MODEL DiracSingletDM_Z2
```


Dirac fermion singlet DM



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
#define MODEL DiracSingletDM_Z2
```


Dirac fermion singlet DM



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
#define PARENT DiracSingletDM_Z2
```


## Source code

```
//  GAMBIT: Global and Modular BSM Inference Tool
//  *********************************************
///
///  Dirac fermion singlet DM
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

#ifndef __DiracSingletDM_Z2_hpp__
#define __DiracSingletDM_Z2_hpp__

#define MODEL DiracSingletDM_Z2
  START_MODEL
  DEFINEPARS(mF, lF, xi)
#undef MODEL

#define MODEL DiracSingletDM_Z2_sps
#define PARENT DiracSingletDM_Z2
  START_MODEL
  DEFINEPARS(mF, lF_s, lF_ps)
  INTERPRET_AS_PARENT_FUNCTION(DiracSingletDM_Z2_sps_to_DiracSingletDM_Z2)
#undef PARENT
#undef MODEL

#endif
```


-------------------------------

Updated on 2022-09-07 at 13:49:53 +0000
