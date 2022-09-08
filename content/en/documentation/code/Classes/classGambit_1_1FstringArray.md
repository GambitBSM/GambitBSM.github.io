---
title: "class Gambit::FstringArray"

description: "[No description available]"

---

# class Gambit::FstringArray



[No description available] [More...](#detailed-description)


`#include <util_types.hpp>`

Inherits from [Gambit::Farray< char, 1, len, lims... >](/documentation/code/classes/classgambit_1_1farray/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| template <typename ... Args\> <br>[enable_if_all_member](/documentation/code/classes/structgambit_1_1enable__if__all__member/)< typenameFarray< char, 1, len, lims... >::allowed_types, [Fstring](/documentation/code/classes/classgambit_1_1fstring/)< len > *, Args... >::type::type | **[operator()](/documentation/code/classes/classgambit_1_1fstringarray/#function-operator)**(Args ... a) |

## Additional inherited members

**Protected Classes inherited from [Gambit::Farray< char, 1, len, lims... >](/documentation/code/classes/classgambit_1_1farray/)**

|                | Name           |
| -------------- | -------------- |
| struct | **[calc_nElem](/documentation/code/classes/structgambit_1_1farray_1_1calc__nelem/)**  |
| struct | **[calc_nElem< limL, limU >](/documentation/code/classes/structgambit_1_1farray_1_1calc__nelem_3_01liml_00_01limu_01_4/)**  |
| struct | **[calc_nElem< limL, limU, _lims... >](/documentation/code/classes/structgambit_1_1farray_1_1calc__nelem_3_01liml_00_01limu_00_01__lims_8_8_8_01_4/)**  |

**Public Types inherited from [Gambit::Farray< char, 1, len, lims... >](/documentation/code/classes/classgambit_1_1farray/)**

|                | Name           |
| -------------- | -------------- |
| typedef [calc_nElem](/documentation/code/classes/structgambit_1_1farray_1_1calc__nelem/)< lims... > | **[nElem](/documentation/code/classes/classgambit_1_1farray/#typedef-nelem)**  |

**Protected Types inherited from [Gambit::Farray< char, 1, len, lims... >](/documentation/code/classes/classgambit_1_1farray/)**

|                | Name           |
| -------------- | -------------- |
| typedef [mult_types](/documentation/code/classes/structgambit_1_1mult__types/)< short, const short, short &, const short &, unsigned short, const unsigned short, unsigned short &, const unsigned short &, int, const int, int &, const int &, unsigned, const unsigned, unsigned &, const unsigned &, long, const long, long &, const long &, unsigned long, const unsigned long, unsigned long &, const unsigned long &, long long, const long long, long long &, const long long &, unsigned long long, const unsigned long long, unsigned long long &, const unsigned long long & > | **[allowed_types](/documentation/code/classes/classgambit_1_1farray/#typedef-allowed-types)**  |

**Public Functions inherited from [Gambit::Farray< char, 1, len, lims... >](/documentation/code/classes/classgambit_1_1farray/)**

|                | Name           |
| -------------- | -------------- |
| | **[Farray](/documentation/code/classes/classgambit_1_1farray/#function-farray)**() |
| | **[Farray](/documentation/code/classes/classgambit_1_1farray/#function-farray)**([Farray](/documentation/code/classes/classgambit_1_1farray/)< T, lims... > & in) |
| [Farray](/documentation/code/classes/classgambit_1_1farray/)< T, lims... > & | **[operator=](/documentation/code/classes/classgambit_1_1farray/#function-operator)**(const [Farray](/documentation/code/classes/classgambit_1_1farray/)< T, lims... > & orig) |
| | **[Farray](/documentation/code/classes/classgambit_1_1farray/#function-farray)**(const T val) |
| [Farray](/documentation/code/classes/classgambit_1_1farray/)< T, lims... > & | **[operator=](/documentation/code/classes/classgambit_1_1farray/#function-operator)**(const T val) |

**Public Attributes inherited from [Gambit::Farray< char, 1, len, lims... >](/documentation/code/classes/classgambit_1_1farray/)**

|                | Name           |
| -------------- | -------------- |
| T[nElem::val] | **[array](/documentation/code/classes/classgambit_1_1farray/#variable-array)**  |


## Detailed Description

```
template <int len,
int... lims>
class Gambit::FstringArray;
```


[Farray](/documentation/code/classes/classgambit_1_1farray/) specialization for Fortran arrays of strings. This is an N+1-dimensional char array, where N is the number of dimensions specified by the user (1/2 * the number of array index limits). The special () operator is intended to be used instead of the operators of the [Farray](/documentation/code/classes/classgambit_1_1farray/) base class, and takes 1 argument less than the [Farray](/documentation/code/classes/classgambit_1_1farray/) class operators (the array index for the letters in the strings should not be passed). This operator returns pointers to [Fstring](/documentation/code/classes/classgambit_1_1fstring/) objects that can be assigned to and read from. Syntax: [FstringArray](/documentation/code/classes/classgambit_1_1fstringarray/)<[string length], [lower index, dim 1], [upper index, dim 1], [alternating lower/upper indices for subsequent dimensions]> DO NOT UNDER ANY CIRCUMSTANCE add new member variables to this class! 

## Public Functions Documentation

### function operator()

```
template <typename ... Args>
inline enable_if_all_member< typenameFarray< char, 1, len, lims... >::allowed_types, Fstring< len > *, Args... >::type::type operator()(
    Args ... a
)
```


-------------------------------

Updated on 2022-09-08 at 03:08:02 +0000