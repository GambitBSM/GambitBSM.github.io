---
title: "class Gambit::FcomplexT"

description: "[No description available]"

---

# class Gambit::FcomplexT



[No description available] [More...](#detailed-description)


`#include <util_types.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[FcomplexT](/documentation/code/classes/classgambit_1_1fcomplext/#function-gambitfcomplext-fcomplext)**()<br>Default constructor.  |
| | **[~FcomplexT](/documentation/code/classes/classgambit_1_1fcomplext/#function-gambitfcomplext-fcomplext)**()<br>Default destructor.  |
| template <typename T2 \> <br>| **[FcomplexT](/documentation/code/classes/classgambit_1_1fcomplext/#function-gambitfcomplext-fcomplext)**(const [FcomplexT](/documentation/code/classes/classgambit_1_1fcomplext/)< T2 > & in)<br>Default copy constructor.  |
| | **[FcomplexT](/documentation/code/classes/classgambit_1_1fcomplext/#function-gambitfcomplext-fcomplext)**(const std::complex< T > & in)<br>Constructor from a C++ complex type.  |
| | **[FcomplexT](/documentation/code/classes/classgambit_1_1fcomplext/#function-gambitfcomplext-fcomplext)**(const T & in)<br>Constructor from a single instance of some type.  |
| template <typename T2 \> <br>[FcomplexT](/documentation/code/classes/classgambit_1_1fcomplext/) & | **[operator=](/documentation/code/classes/classgambit_1_1fcomplext/#function-gambitfcomplext-operator)**(const [FcomplexT](/documentation/code/classes/classgambit_1_1fcomplext/)< T2 > & in)<br>Assignment from another Fortran complex type.  |
| [FcomplexT](/documentation/code/classes/classgambit_1_1fcomplext/) & | **[operator=](/documentation/code/classes/classgambit_1_1fcomplext/#function-gambitfcomplext-operator)**(const std::complex< T > & in)<br>Assignment from a C++ complex type.  |
| [FcomplexT](/documentation/code/classes/classgambit_1_1fcomplext/) & | **[operator=](/documentation/code/classes/classgambit_1_1fcomplext/#function-gambitfcomplext-operator)**(const T & in)<br>Assignment from a single instance of some type.  |
| template <typename T2 \> <br>| **[operator FcomplexT< T2 >](/documentation/code/classes/classgambit_1_1fcomplext/#function-gambitfcomplext-operator-fcomplext-t2)**()<br>Type casting to another Fortran complex type.  |
| | **[operator std::complex< T >](/documentation/code/classes/classgambit_1_1fcomplext/#function-gambitfcomplext-operator-stdcomplex-t)**()<br>Type casting to a C++ complex type.  |
| T | **[abs](/documentation/code/classes/classgambit_1_1fcomplext/#function-gambitfcomplext-abs)**() const |
| template <typename T2 \> <br>[FcomplexT](/documentation/code/classes/classgambit_1_1fcomplext/) | **[operator*](/documentation/code/classes/classgambit_1_1fcomplext/#function-gambitfcomplext-operator)**(const [FcomplexT](/documentation/code/classes/classgambit_1_1fcomplext/)< T2 > & in) |
| template <typename T2 \> <br>[FcomplexT](/documentation/code/classes/classgambit_1_1fcomplext/) | **[operator/](/documentation/code/classes/classgambit_1_1fcomplext/#function-gambitfcomplext-operator)**(const [FcomplexT](/documentation/code/classes/classgambit_1_1fcomplext/)< T2 > & in) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| T | **[re](/documentation/code/classes/classgambit_1_1fcomplext/#variable-gambitfcomplext-re)**  |
| T | **[im](/documentation/code/classes/classgambit_1_1fcomplext/#variable-gambitfcomplext-im)**  |

## Detailed Description

```
template <typename T >
class Gambit::FcomplexT;
```


Fortran complex type. Use typdef versions instead of the DO NOT UNDER ANY CIRCUMSTANCE add new member variables to this class! 

## Public Functions Documentation

### function FcomplexT

```
inline FcomplexT()
```

Default constructor. 

### function ~FcomplexT

```
inline ~FcomplexT()
```

Default destructor. 

### function FcomplexT

```
template <typename T2 >
inline FcomplexT(
    const FcomplexT< T2 > & in
)
```

Default copy constructor. 

### function FcomplexT

```
inline FcomplexT(
    const std::complex< T > & in
)
```

Constructor from a C++ complex type. 

### function FcomplexT

```
inline FcomplexT(
    const T & in
)
```

Constructor from a single instance of some type. 

### function operator=

```
template <typename T2 >
inline FcomplexT & operator=(
    const FcomplexT< T2 > & in
)
```

Assignment from another Fortran complex type. 

### function operator=

```
inline FcomplexT & operator=(
    const std::complex< T > & in
)
```

Assignment from a C++ complex type. 

### function operator=

```
inline FcomplexT & operator=(
    const T & in
)
```

Assignment from a single instance of some type. 

### function operator FcomplexT< T2 >

```
template <typename T2 >
inline operator FcomplexT< T2 >()
```

Type casting to another Fortran complex type. 

### function operator std::complex< T >

```
inline operator std::complex< T >()
```

Type casting to a C++ complex type. 

### function abs

```
inline T abs() const
```


### function operator*

```
template <typename T2 >
inline FcomplexT operator*(
    const FcomplexT< T2 > & in
)
```


### function operator/

```
template <typename T2 >
inline FcomplexT operator/(
    const FcomplexT< T2 > & in
)
```


## Public Attributes Documentation

### variable re

```
T re;
```


### variable im

```
T im;
```


-------------------------------

Updated on 2022-09-08 at 01:48:53 +0000