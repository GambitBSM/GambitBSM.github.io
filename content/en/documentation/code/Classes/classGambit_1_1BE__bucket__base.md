---
title: "class Gambit::BE_bucket_base"
description: "A base class for [BEvariable_bucket]() and [BEfunction_bucket](). "

---

# class Gambit::BE_bucket_base



A base class for [BEvariable_bucket]() and [BEfunction_bucket](). 


`#include <safety_bucket.hpp>`

Inherits from [Gambit::safety_bucket_base](/documentation/code/classes/classgambit_1_1safety__bucket__base/)

Inherited by [Gambit::BEfunction_bucket_common< TYPE(*)(ARGS...), TYPE, ARGS... >](/documentation/code/classes/classgambit_1_1befunction__bucket__common/), [Gambit::BEfunction_bucket_common< variadic_ptr< TYPE, ARGS... >::type, TYPE, ARGS... >](/documentation/code/classes/classgambit_1_1befunction__bucket__common/), [Gambit::BEfunction_bucket_common< PTR_TYPE, TYPE, ARGS >](/documentation/code/classes/classgambit_1_1befunction__bucket__common/), [Gambit::BEvariable_bucket< TYPE >](/documentation/code/classes/classgambit_1_1bevariable__bucket/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BE_bucket_base](/documentation/code/classes/classgambit_1_1be__bucket__base/)**([str](/documentation/code/namespaces/namespacegambit/) mym, [str](/documentation/code/namespaces/namespacegambit/) myf, [str](/documentation/code/namespaces/namespacegambit/) me)<br>Constructor for [BE_bucket_base](/documentation/code/classes/classgambit_1_1be__bucket__base/).  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[backend](/documentation/code/classes/classgambit_1_1be__bucket__base/)**()<br>Get backend name.  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[version](/documentation/code/classes/classgambit_1_1be__bucket__base/)**()<br>Get version information.  |

## Additional inherited members

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


## Public Functions Documentation

### function BE_bucket_base

```
inline BE_bucket_base(
    str mym,
    str myf,
    str me
)
```

Constructor for [BE_bucket_base](/documentation/code/classes/classgambit_1_1be__bucket__base/). 

### function backend

```
inline str backend()
```

Get backend name. 

### function version

```
inline str version()
```

Get version information. 

-------------------------------

Updated on 2022-09-08 at 01:05:15 +0000