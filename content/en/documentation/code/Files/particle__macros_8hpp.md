---
title: "file Models/particle_macros.hpp"

description: "[No description available]"

---

# file Models/particle_macros.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[add_particle](/documentation/code/files/particle__macros_8hpp/#define-add-particle)**(LONGNAME, INTPAIR, SPINX2, CHARGEX3, COLOR)  |
|  | **[add_SM_particle](/documentation/code/files/particle__macros_8hpp/#define-add-sm-particle)**(LONGNAME, INTPAIR, SPINX2, CHARGEX3, COLOR)  |
|  | **[add_generic_particle](/documentation/code/files/particle__macros_8hpp/#define-add-generic-particle)**(LONGNAME, INTPAIR, SPINX2, CHARGEX3, COLOR)  |
|  | **[ADD_PARTICLE_I](/documentation/code/files/particle__macros_8hpp/#define-add-particle-i)**(r, DATA, I, ELEM)  |
|  | **[ADD_SM_PARTICLE_I](/documentation/code/files/particle__macros_8hpp/#define-add-sm-particle-i)**(r, DATA, I, ELEM)  |
|  | **[add_particle_set](/documentation/code/files/particle__macros_8hpp/#define-add-particle-set)**(SHORTNAME, __TUP, SPINX2, CHARGEX3, COLOR)  |
|  | **[add_SM_particle_set](/documentation/code/files/particle__macros_8hpp/#define-add-sm-particle-set)**(SHORTNAME, __TUP, SPINX2, CHARGEX3, COLOR)  |

## Detailed Description


**Author**: Pat Scott 

 ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 

**Date**: 2015 Jan

Macros for defining new particles.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define add_particle

```
#define add_particle(
    LONGNAME,
    INTPAIR,
    SPINX2,
    CHARGEX3,
    COLOR
)
particles->add(LONGNAME, std::pair<int, int> INTPAIR, SPINX2, CHARGEX3, COLOR);
```


### define add_SM_particle

```
#define add_SM_particle(
    LONGNAME,
    INTPAIR,
    SPINX2,
    CHARGEX3,
    COLOR
)
particles->add_SM(LONGNAME, std::pair<int, int> INTPAIR, SPINX2, CHARGEX3, COLOR );
```


### define add_generic_particle

```
#define add_generic_particle(
    LONGNAME,
    INTPAIR,
    SPINX2,
    CHARGEX3,
    COLOR
)
particles->add_generic(LONGNAME, std::pair<int, int> INTPAIR, SPINX2, CHARGEX3, COLOR);
```


### define ADD_PARTICLE_I

```
#define ADD_PARTICLE_I(
    r,
    DATA,
    I,
    ELEM
)
particles->add_with_short_pair(BOOST_PP_TUPLE_ELEM(4, 0, DATA) "_" STRINGIFY(BOOST_PP_ADD(I,1)), std::pair<int, int> ELEM, std::pair<str, int> (BOOST_PP_TUPLE_ELEM(4, 0, DATA),BOOST_PP_ADD(I,1)), BOOST_PP_TUPLE_ELEM(4, 1, DATA), BOOST_PP_TUPLE_ELEM(4, 2, DATA), BOOST_PP_TUPLE_ELEM(4, 3, DATA));
```


### define ADD_SM_PARTICLE_I

```
#define ADD_SM_PARTICLE_I(
    r,
    DATA,
    I,
    ELEM
)
particles->add_SM_with_short_pair(BOOST_PP_TUPLE_ELEM(4, 0, DATA) "_" STRINGIFY(BOOST_PP_ADD(I,1)), std::pair<int, int> ELEM, std::pair<str, int> (BOOST_PP_TUPLE_ELEM(4, 0, DATA),BOOST_PP_ADD(I,1)), BOOST_PP_TUPLE_ELEM(4, 1, DATA), BOOST_PP_TUPLE_ELEM(4, 2, DATA), BOOST_PP_TUPLE_ELEM(4, 3, DATA));
```


### define add_particle_set

```
#define add_particle_set(
    SHORTNAME,
    __TUP,
    SPINX2,
    CHARGEX3,
    COLOR
)
BOOST_PP_SEQ_FOR_EACH_I(ADD_PARTICLE_I, (SHORTNAME, SPINX2, CHARGEX3, COLOR), BOOST_PP_TUPLE_TO_SEQ(__TUP))
```


### define add_SM_particle_set

```
#define add_SM_particle_set(
    SHORTNAME,
    __TUP,
    SPINX2,
    CHARGEX3,
    COLOR
)
BOOST_PP_SEQ_FOR_EACH_I(ADD_SM_PARTICLE_I, (SHORTNAME, SPINX2, CHARGEX3, COLOR), BOOST_PP_TUPLE_TO_SEQ(__TUP))
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Macros for defining new particles.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///   
///  \author Pat Scott  
///          (p.scott@imperial.ac.uk)
///  \date 2015 Jan
///
///  *********************************************

#ifndef __particle_macros_hpp__
#define __particle_macros_hpp__

#include "gambit/Utils/boost_fallbacks.hpp"

#include <boost/preprocessor/tuple/to_seq.hpp>
#include <boost/preprocessor/seq/for_each_i.hpp>
#include <boost/preprocessor/arithmetic/add.hpp>

#define add_particle(LONGNAME, INTPAIR, SPINX2, CHARGEX3, COLOR) particles->add(LONGNAME, std::pair<int, int> INTPAIR, SPINX2, CHARGEX3, COLOR);
#define add_SM_particle(LONGNAME, INTPAIR, SPINX2, CHARGEX3, COLOR) particles->add_SM(LONGNAME, std::pair<int, int> INTPAIR, SPINX2, CHARGEX3, COLOR );
#define add_generic_particle(LONGNAME, INTPAIR, SPINX2, CHARGEX3, COLOR) particles->add_generic(LONGNAME, std::pair<int, int> INTPAIR, SPINX2, CHARGEX3, COLOR);
#define ADD_PARTICLE_I(r, DATA, I, ELEM) particles->add_with_short_pair(BOOST_PP_TUPLE_ELEM(4, 0, DATA) "_" STRINGIFY(BOOST_PP_ADD(I,1)), std::pair<int, int> ELEM, std::pair<str, int> (BOOST_PP_TUPLE_ELEM(4, 0, DATA),BOOST_PP_ADD(I,1)), BOOST_PP_TUPLE_ELEM(4, 1, DATA), BOOST_PP_TUPLE_ELEM(4, 2, DATA), BOOST_PP_TUPLE_ELEM(4, 3, DATA));
#define ADD_SM_PARTICLE_I(r, DATA, I, ELEM) particles->add_SM_with_short_pair(BOOST_PP_TUPLE_ELEM(4, 0, DATA) "_" STRINGIFY(BOOST_PP_ADD(I,1)), std::pair<int, int> ELEM, std::pair<str, int> (BOOST_PP_TUPLE_ELEM(4, 0, DATA),BOOST_PP_ADD(I,1)), BOOST_PP_TUPLE_ELEM(4, 1, DATA), BOOST_PP_TUPLE_ELEM(4, 2, DATA), BOOST_PP_TUPLE_ELEM(4, 3, DATA));
#define add_particle_set(SHORTNAME, __TUP, SPINX2, CHARGEX3, COLOR) BOOST_PP_SEQ_FOR_EACH_I(ADD_PARTICLE_I, (SHORTNAME, SPINX2, CHARGEX3, COLOR), BOOST_PP_TUPLE_TO_SEQ(__TUP))
#define add_SM_particle_set(SHORTNAME, __TUP, SPINX2, CHARGEX3, COLOR) BOOST_PP_SEQ_FOR_EACH_I(ADD_SM_PARTICLE_I, (SHORTNAME, SPINX2, CHARGEX3, COLOR), BOOST_PP_TUPLE_TO_SEQ(__TUP))

#endif //__particle_macros_hpp__
```


-------------------------------

Updated on 2022-09-08 at 03:17:36 +0000
