---
title: "class Gambit::BEfunction_bucket_common"
description: "An interface class for backend functions. "

---

# class Gambit::BEfunction_bucket_common



An interface class for backend functions.  [More...](#detailed-description)


`#include <safety_bucket.hpp>`

Inherits from [Gambit::BE_bucket_base](/documentation/code/classes/classgambit_1_1be__bucket__base/), [Gambit::safety_bucket_base](/documentation/code/classes/classgambit_1_1safety__bucket__base/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BEfunction_bucket_common](/documentation/code/classes/classgambit_1_1befunction__bucket__common/)**([str](/documentation/code/namespaces/namespacegambit/) mym, [str](/documentation/code/namespaces/namespacegambit/) myf, [str](/documentation/code/namespaces/namespacegambit/) me, [backend_functor](/documentation/code/classes/classgambit_1_1backend__functor/)< PTR_TYPE, TYPE, ARGS... > * functor_ptr_in =NULL)<br>Constructor for [BEfunction_bucket_common](/documentation/code/classes/classgambit_1_1befunction__bucket__common/).  |
| void | **[initialize](/documentation/code/classes/classgambit_1_1befunction__bucket__common/)**([backend_functor](/documentation/code/classes/classgambit_1_1backend__functor/)< PTR_TYPE, TYPE, ARGS... > * functor_ptr_in)<br>Initialize this bucket with a functor pointer.  |
| PTR_TYPE | **[pointer](/documentation/code/classes/classgambit_1_1befunction__bucket__common/)**()<br>Return the underlying function pointer.  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| [backend_functor](/documentation/code/classes/classgambit_1_1backend__functor/)< PTR_TYPE, TYPE, ARGS... > * | **[_functor_ptr](/documentation/code/classes/classgambit_1_1befunction__bucket__common/)**  |

## Additional inherited members

**Public Functions inherited from [Gambit::BE_bucket_base](/documentation/code/classes/classgambit_1_1be__bucket__base/)**

|                | Name           |
| -------------- | -------------- |
| | **[BE_bucket_base](/documentation/code/classes/classgambit_1_1be__bucket__base/)**([str](/documentation/code/namespaces/namespacegambit/) mym, [str](/documentation/code/namespaces/namespacegambit/) myf, [str](/documentation/code/namespaces/namespacegambit/) me)<br>Constructor for [BE_bucket_base](/documentation/code/classes/classgambit_1_1be__bucket__base/).  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[backend](/documentation/code/classes/classgambit_1_1be__bucket__base/)**()<br>Get backend name.  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[version](/documentation/code/classes/classgambit_1_1be__bucket__base/)**()<br>Get version information.  |

**Public Functions inherited from [Gambit::safety_bucket_base](/documentation/code/classes/classgambit_1_1safety__bucket__base/)**

|                | Name           |
| -------------- | -------------- |
| | **[safety_bucket_base](/documentation/code/classes/classgambit_1_1safety__bucket__base/)**([str](/documentation/code/namespaces/namespacegambit/) myinfo)<br>Master constructor.  |
| bool | **[active](/documentation/code/classes/classgambit_1_1safety__bucket__base/)**() |
| [str](/documentation/code/namespaces/namespacegambit/) | **[name](/documentation/code/classes/classgambit_1_1safety__bucket__base/)**()<br>Get capability name.  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[origin](/documentation/code/classes/classgambit_1_1safety__bucket__base/)**()<br>Get name of origin (module/backend).  |

**Protected Functions inherited from [Gambit::safety_bucket_base](/documentation/code/classes/classgambit_1_1safety__bucket__base/)**

|                | Name           |
| -------------- | -------------- |
| void | **[dieGracefully](/documentation/code/classes/classgambit_1_1safety__bucket__base/)**() const<br>Failure message invoked when the user tries to access the object before it is initialized.  |

**Protected Attributes inherited from [Gambit::safety_bucket_base](/documentation/code/classes/classgambit_1_1safety__bucket__base/)**

|                | Name           |
| -------------- | -------------- |
| [functor](/documentation/code/classes/classgambit_1_1functor/) * | **[_functor_base_ptr](/documentation/code/classes/classgambit_1_1safety__bucket__base/)**  |
| bool | **[_initialized](/documentation/code/classes/classgambit_1_1safety__bucket__base/)**  |
| const [str](/documentation/code/namespaces/namespacegambit/) | **[whoami](/documentation/code/classes/classgambit_1_1safety__bucket__base/)**  |


## Detailed Description

```
template <typename PTR_TYPE ,
typename TYPE ,
typename... ARGS>
class Gambit::BEfunction_bucket_common;
```

An interface class for backend functions. 
## Public Functions Documentation

### function BEfunction_bucket_common

```
inline BEfunction_bucket_common(
    str mym,
    str myf,
    str me,
    backend_functor< PTR_TYPE, TYPE, ARGS... > * functor_ptr_in =NULL
)
```

Constructor for [BEfunction_bucket_common](/documentation/code/classes/classgambit_1_1befunction__bucket__common/). 

### function initialize

```
inline void initialize(
    backend_functor< PTR_TYPE, TYPE, ARGS... > * functor_ptr_in
)
```

Initialize this bucket with a functor pointer. 

### function pointer

```
inline PTR_TYPE pointer()
```

Return the underlying function pointer. 

## Protected Attributes Documentation

### variable _functor_ptr

```
backend_functor< PTR_TYPE, TYPE, ARGS... > * _functor_ptr;
```


-------------------------------

Updated on 2022-09-08 at 01:05:15 +0000