---
title: "class Gambit::Farray"

description: "[No description available]"

---

# class Gambit::Farray



[No description available] [More...](#detailed-description)


`#include <util_types.hpp>`

## Protected Classes

|                | Name           |
| -------------- | -------------- |
| struct | **[calc_nElem](/documentation/code/classes/structgambit_1_1farray_1_1calc__nelem/)**  |
| struct | **[calc_nElem< limL, limU >](/documentation/code/classes/structgambit_1_1farray_1_1calc__nelem_3_01liml_00_01limu_01_4/)**  |
| struct | **[calc_nElem< limL, limU, _lims... >](/documentation/code/classes/structgambit_1_1farray_1_1calc__nelem_3_01liml_00_01limu_00_01__lims_8_8_8_01_4/)**  |

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef [calc_nElem](/documentation/code/classes/structgambit_1_1farray_1_1calc__nelem/)< lims... > | **[nElem](/documentation/code/classes/classgambit_1_1farray/#typedef-nelem)**  |

## Protected Types

|                | Name           |
| -------------- | -------------- |
| typedef [mult_types](/documentation/code/classes/structgambit_1_1mult__types/)< short, const short, short &, const short &, unsigned short, const unsigned short, unsigned short &, const unsigned short &, int, const int, int &, const int &, unsigned, const unsigned, unsigned &, const unsigned &, long, const long, long &, const long &, unsigned long, const unsigned long, unsigned long &, const unsigned long &, long long, const long long, long long &, const long long &, unsigned long long, const unsigned long long, unsigned long long &, const unsigned long long & > | **[allowed_types](/documentation/code/classes/classgambit_1_1farray/#typedef-allowed-types)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Farray](/documentation/code/classes/classgambit_1_1farray/#function-farray)**() |
| | **[Farray](/documentation/code/classes/classgambit_1_1farray/#function-farray)**([Farray](/documentation/code/classes/classgambit_1_1farray/)< T, lims... > & in) |
| template <typename ... Args\> <br>[enable_if_all_member](/documentation/code/classes/structgambit_1_1enable__if__all__member/)< [allowed_types](/documentation/code/classes/structgambit_1_1mult__types/), T &, Args... >::type::type | **[operator()](/documentation/code/classes/classgambit_1_1farray/#function-operator)**(Args ... a) |
| template <typename ... Args\> <br>[enable_if_all_member](/documentation/code/classes/structgambit_1_1enable__if__all__member/)< [allowed_types](/documentation/code/classes/structgambit_1_1mult__types/), constT &, Args... >::type::type | **[operator()](/documentation/code/classes/classgambit_1_1farray/#function-operator)**(Args ... a) const |
| [Farray](/documentation/code/classes/classgambit_1_1farray/)< T, lims... > & | **[operator=](/documentation/code/classes/classgambit_1_1farray/#function-operator)**(const [Farray](/documentation/code/classes/classgambit_1_1farray/)< T, lims... > & orig) |
| | **[Farray](/documentation/code/classes/classgambit_1_1farray/#function-farray)**(const T val) |
| [Farray](/documentation/code/classes/classgambit_1_1farray/)< T, lims... > & | **[operator=](/documentation/code/classes/classgambit_1_1farray/#function-operator)**(const T val) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| T[nElem::val] | **[array](/documentation/code/classes/classgambit_1_1farray/#variable-array)**  |

## Detailed Description

```
template <typename T ,
int... lims>
class Gambit::Farray;
```


Array class that matches the memory structure and functionality of arrays in Fortran codes Syntax: [Farray](/documentation/code/classes/classgambit_1_1farray/)<[type], [lower index, dim 1], [upper index, dim 1], [alternating lower/upper indices for subsequent dimensions]> DO NOT UNDER ANY CIRCUMSTANCE add new member variables to this class! This would break the crucial memory structure. 

## Public Types Documentation

### typedef nElem

```
typedef calc_nElem<lims... > Gambit::Farray< T, lims >::nElem;
```


## Protected Types Documentation

### typedef allowed_types

```
typedef mult_types< short, const short, short&, const short&, unsigned short, const unsigned short, unsigned short&, const unsigned short&, int, const int, int&, const int&, unsigned, const unsigned, unsigned&, const unsigned&, long, const long, long&, const long&, unsigned long, const unsigned long, unsigned long&, const unsigned long&, long long , const long long, long long&, const long long&, unsigned long long, const unsigned long long, unsigned long long&, const unsigned long long&> Gambit::Farray< T, lims >::allowed_types;
```


## Public Functions Documentation

### function Farray

```
inline Farray()
```


### function Farray

```
inline Farray(
    Farray< T, lims... > & in
)
```


### function operator()

```
template <typename ... Args>
inline enable_if_all_member< allowed_types, T &, Args... >::type::type operator()(
    Args ... a
)
```


### function operator()

```
template <typename ... Args>
inline enable_if_all_member< allowed_types, constT &, Args... >::type::type operator()(
    Args ... a
) const
```


### function operator=

```
inline Farray< T, lims... > & operator=(
    const Farray< T, lims... > & orig
)
```


### function Farray

```
inline Farray(
    const T val
)
```


### function operator=

```
inline Farray< T, lims... > & operator=(
    const T val
)
```


## Public Attributes Documentation

### variable array

```
T[nElem::val] array;
```


-------------------------------

Updated on 2022-09-08 at 03:17:31 +0000