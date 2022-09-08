---
title: "class Gambit::BEfunction_bucket< TYPE(*)(ARGS...), TYPE, ARGS... >"
description: "Partial specialisation for non-variadic backend functions. "

---

# class Gambit::BEfunction_bucket< TYPE(*)(ARGS...), TYPE, ARGS... >



Partial specialisation for non-variadic backend functions.  [More...](#detailed-description)


`#include <safety_bucket.hpp>`

Inherits from [Gambit::BEfunction_bucket_common< TYPE(*)(ARGS...), TYPE, ARGS... >](/documentation/code/classes/classgambit_1_1befunction__bucket__common/), [Gambit::BE_bucket_base](/documentation/code/classes/classgambit_1_1be__bucket__base/), [Gambit::safety_bucket_base](/documentation/code/classes/classgambit_1_1safety__bucket__base/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BEfunction_bucket](/documentation/code/classes/classgambit_1_1befunction__bucket_3_01type_07_5_08_07args_8_8_8_08_00_01type_00_01args_8_8_8_01_4/)**([str](/documentation/code/namespaces/namespacegambit/) mym, [str](/documentation/code/namespaces/namespacegambit/) myf, [str](/documentation/code/namespaces/namespacegambit/) me, [backend_functor](/documentation/code/classes/classgambit_1_1backend__functor/)< TYPE(*)(ARGS...), TYPE, ARGS... > * functor_ptr_in =NULL)<br>Constructor for non-variadic [BEfunction_bucket](/documentation/code/classes/classgambit_1_1befunction__bucket/).  |
| TYPE | **[operator()](/documentation/code/classes/classgambit_1_1befunction__bucket_3_01type_07_5_08_07args_8_8_8_08_00_01type_00_01args_8_8_8_01_4/)**(ARGS &&... args)<br>Call backend function.  |

## Additional inherited members

**Public Functions inherited from [Gambit::BEfunction_bucket_common< TYPE(*)(ARGS...), TYPE, ARGS... >](/documentation/code/classes/classgambit_1_1befunction__bucket__common/)**

|                | Name           |
| -------------- | -------------- |
| | **[BEfunction_bucket_common](/documentation/code/classes/classgambit_1_1befunction__bucket__common/)**([str](/documentation/code/namespaces/namespacegambit/) mym, [str](/documentation/code/namespaces/namespacegambit/) myf, [str](/documentation/code/namespaces/namespacegambit/) me, [backend_functor](/documentation/code/classes/classgambit_1_1backend__functor/)< PTR_TYPE, TYPE, ARGS... > * functor_ptr_in =NULL)<br>Constructor for [BEfunction_bucket_common](/documentation/code/classes/classgambit_1_1befunction__bucket__common/).  |
| void | **[initialize](/documentation/code/classes/classgambit_1_1befunction__bucket__common/)**([backend_functor](/documentation/code/classes/classgambit_1_1backend__functor/)< PTR_TYPE, TYPE, ARGS... > * functor_ptr_in)<br>Initialize this bucket with a functor pointer.  |
| PTR_TYPE | **[pointer](/documentation/code/classes/classgambit_1_1befunction__bucket__common/)**()<br>Return the underlying function pointer.  |

**Protected Attributes inherited from [Gambit::BEfunction_bucket_common< TYPE(*)(ARGS...), TYPE, ARGS... >](/documentation/code/classes/classgambit_1_1befunction__bucket__common/)**

|                | Name           |
| -------------- | -------------- |
| [backend_functor](/documentation/code/classes/classgambit_1_1backend__functor/)< PTR_TYPE, TYPE, ARGS... > * | **[_functor_ptr](/documentation/code/classes/classgambit_1_1befunction__bucket__common/)**  |

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
template <typename TYPE ,
typename... ARGS>
class Gambit::BEfunction_bucket< TYPE(*)(ARGS...), TYPE, ARGS... >;
```

Partial specialisation for non-variadic backend functions. 
## Public Functions Documentation

### function BEfunction_bucket

```
inline BEfunction_bucket(
    str mym,
    str myf,
    str me,
    backend_functor< TYPE(*)(ARGS...), TYPE, ARGS... > * functor_ptr_in =NULL
)
```

Constructor for non-variadic [BEfunction_bucket](/documentation/code/classes/classgambit_1_1befunction__bucket/). 

### function operator()

```
inline TYPE operator()(
    ARGS &&... args
)
```

Call backend function. 

-------------------------------

Updated on 2022-09-08 at 01:05:15 +0000