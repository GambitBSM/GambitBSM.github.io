---
title: "class Gambit::Fstring"

description: "[No description available]"

---

# class Gambit::Fstring



[No description available] [More...](#detailed-description)


`#include <util_types.hpp>`

Inherits from [Gambit::Farray< char, 1, len >](/documentation/code/classes/classgambit_1_1farray/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Fstring](/documentation/code/classes/classgambit_1_1fstring/#function-fstring)**() |
| | **[Fstring](/documentation/code/classes/classgambit_1_1fstring/#function-fstring)**(const std::string & in) |
| | **[Fstring](/documentation/code/classes/classgambit_1_1fstring/#function-fstring)**(const char * in) |
| | **[Fstring](/documentation/code/classes/classgambit_1_1fstring/#function-fstring)**(char in) |
| template <int ilen\> <br>| **[Fstring](/documentation/code/classes/classgambit_1_1fstring/#function-fstring)**(const [Fstring](/documentation/code/classes/classgambit_1_1fstring/)< ilen > & in) |
| [Fstring](/documentation/code/classes/classgambit_1_1fstring/) & | **[operator=](/documentation/code/classes/classgambit_1_1fstring/#function-operator)**(const std::string & in) |
| [Fstring](/documentation/code/classes/classgambit_1_1fstring/) & | **[operator=](/documentation/code/classes/classgambit_1_1fstring/#function-operator)**(const char * in) |
| [Fstring](/documentation/code/classes/classgambit_1_1fstring/) & | **[operator=](/documentation/code/classes/classgambit_1_1fstring/#function-operator)**(char in) |
| template <int ilen\> <br>[Fstring](/documentation/code/classes/classgambit_1_1fstring/) & | **[operator=](/documentation/code/classes/classgambit_1_1fstring/#function-operator)**(const [Fstring](/documentation/code/classes/classgambit_1_1fstring/)< ilen > & in) |
| std::string | **[str](/documentation/code/classes/classgambit_1_1fstring/#function-str)**() const<br>Get std::string copy of the [Fstring](/documentation/code/classes/classgambit_1_1fstring/), including all trailing spaces.  |
| std::string | **[trimmed_str](/documentation/code/classes/classgambit_1_1fstring/#function-trimmed-str)**() const<br>Get std::string copy of the [Fstring](/documentation/code/classes/classgambit_1_1fstring/) without trailing spaces.  |
| bool | **[operator==](/documentation/code/classes/classgambit_1_1fstring/#function-operator)**(std::string str) |

## Additional inherited members

**Protected Classes inherited from [Gambit::Farray< char, 1, len >](/documentation/code/classes/classgambit_1_1farray/)**

|                | Name           |
| -------------- | -------------- |
| struct | **[calc_nElem](/documentation/code/classes/structgambit_1_1farray_1_1calc__nelem/)**  |
| struct | **[calc_nElem< limL, limU >](/documentation/code/classes/structgambit_1_1farray_1_1calc__nelem_3_01liml_00_01limu_01_4/)**  |
| struct | **[calc_nElem< limL, limU, _lims... >](/documentation/code/classes/structgambit_1_1farray_1_1calc__nelem_3_01liml_00_01limu_00_01__lims_8_8_8_01_4/)**  |

**Public Types inherited from [Gambit::Farray< char, 1, len >](/documentation/code/classes/classgambit_1_1farray/)**

|                | Name           |
| -------------- | -------------- |
| typedef [calc_nElem](/documentation/code/classes/structgambit_1_1farray_1_1calc__nelem/)< lims... > | **[nElem](/documentation/code/classes/classgambit_1_1farray/#typedef-nelem)**  |

**Protected Types inherited from [Gambit::Farray< char, 1, len >](/documentation/code/classes/classgambit_1_1farray/)**

|                | Name           |
| -------------- | -------------- |
| typedef [mult_types](/documentation/code/classes/structgambit_1_1mult__types/)< short, const short, short &, const short &, unsigned short, const unsigned short, unsigned short &, const unsigned short &, int, const int, int &, const int &, unsigned, const unsigned, unsigned &, const unsigned &, long, const long, long &, const long &, unsigned long, const unsigned long, unsigned long &, const unsigned long &, long long, const long long, long long &, const long long &, unsigned long long, const unsigned long long, unsigned long long &, const unsigned long long & > | **[allowed_types](/documentation/code/classes/classgambit_1_1farray/#typedef-allowed-types)**  |

**Public Functions inherited from [Gambit::Farray< char, 1, len >](/documentation/code/classes/classgambit_1_1farray/)**

|                | Name           |
| -------------- | -------------- |
| | **[Farray](/documentation/code/classes/classgambit_1_1farray/#function-farray)**() |
| | **[Farray](/documentation/code/classes/classgambit_1_1farray/#function-farray)**([Farray](/documentation/code/classes/classgambit_1_1farray/)< T, lims... > & in) |
| template <typename ... Args\> <br>[enable_if_all_member](/documentation/code/classes/structgambit_1_1enable__if__all__member/)< [allowed_types](/documentation/code/classes/structgambit_1_1mult__types/), T &, Args... >::type::type | **[operator()](/documentation/code/classes/classgambit_1_1farray/#function-operator)**(Args ... a) |
| template <typename ... Args\> <br>[enable_if_all_member](/documentation/code/classes/structgambit_1_1enable__if__all__member/)< [allowed_types](/documentation/code/classes/structgambit_1_1mult__types/), constT &, Args... >::type::type | **[operator()](/documentation/code/classes/classgambit_1_1farray/#function-operator)**(Args ... a) const |
| | **[Farray](/documentation/code/classes/classgambit_1_1farray/#function-farray)**(const T val) |

**Public Attributes inherited from [Gambit::Farray< char, 1, len >](/documentation/code/classes/classgambit_1_1farray/)**

|                | Name           |
| -------------- | -------------- |
| T[nElem::val] | **[array](/documentation/code/classes/classgambit_1_1farray/#variable-array)**  |


## Detailed Description

```
template <int len>
class Gambit::Fstring;
```


[Farray](/documentation/code/classes/classgambit_1_1farray/) specialization for Fortran strings. This is a 1-dimensional char array with indices 1 to len. It has assignment operators for standard string types, and accessors that return std::string objects. Strings longer than len will be truncated by the assignment operators, and shorter strings will be given trailing spaces. Syntax: Fstring<[string length]> DO NOT UNDER ANY CIRCUMSTANCE add new member variables to this class! 

## Public Functions Documentation

### function Fstring

```
inline Fstring()
```


### function Fstring

```
inline Fstring(
    const std::string & in
)
```


### function Fstring

```
inline Fstring(
    const char * in
)
```


### function Fstring

```
inline Fstring(
    char in
)
```


### function Fstring

```
template <int ilen>
inline Fstring(
    const Fstring< ilen > & in
)
```


### function operator=

```
inline Fstring & operator=(
    const std::string & in
)
```


### function operator=

```
inline Fstring & operator=(
    const char * in
)
```


### function operator=

```
inline Fstring & operator=(
    char in
)
```


### function operator=

```
template <int ilen>
inline Fstring & operator=(
    const Fstring< ilen > & in
)
```


### function str

```
inline std::string str() const
```

Get std::string copy of the [Fstring](/documentation/code/classes/classgambit_1_1fstring/), including all trailing spaces. 

### function trimmed_str

```
inline std::string trimmed_str() const
```

Get std::string copy of the [Fstring](/documentation/code/classes/classgambit_1_1fstring/) without trailing spaces. 

### function operator==

```
inline bool operator==(
    std::string str
)
```


-------------------------------

Updated on 2022-09-08 at 02:27:26 +0000