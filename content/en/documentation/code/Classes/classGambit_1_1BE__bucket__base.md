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
| | **[BE_bucket_base](/documentation/code/classes/classgambit_1_1be__bucket__base/#function-be-bucket-base)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) mym, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) myf, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) me)<br>Constructor for [BE_bucket_base](/documentation/code/classes/classgambit_1_1be__bucket__base/).  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[backend](/documentation/code/classes/classgambit_1_1be__bucket__base/#function-backend)**()<br>Get backend name.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[version](/documentation/code/classes/classgambit_1_1be__bucket__base/#function-version)**()<br>Get version information.  |

## Additional inherited members

**Public Functions inherited from [Gambit::safety_bucket_base](/documentation/code/classes/classgambit_1_1safety__bucket__base/)**

|                | Name           |
| -------------- | -------------- |
| | **[safety_bucket_base](/documentation/code/classes/classgambit_1_1safety__bucket__base/#function-safety-bucket-base)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) myinfo)<br>Master constructor.  |
| bool | **[active](/documentation/code/classes/classgambit_1_1safety__bucket__base/#function-active)**() |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[name](/documentation/code/classes/classgambit_1_1safety__bucket__base/#function-name)**()<br>Get capability name.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[origin](/documentation/code/classes/classgambit_1_1safety__bucket__base/#function-origin)**()<br>Get name of origin (module/backend).  |

**Protected Functions inherited from [Gambit::safety_bucket_base](/documentation/code/classes/classgambit_1_1safety__bucket__base/)**

|                | Name           |
| -------------- | -------------- |
| void | **[dieGracefully](/documentation/code/classes/classgambit_1_1safety__bucket__base/#function-diegracefully)**() const<br>Failure message invoked when the user tries to access the object before it is initialized.  |

**Protected Attributes inherited from [Gambit::safety_bucket_base](/documentation/code/classes/classgambit_1_1safety__bucket__base/)**

|                | Name           |
| -------------- | -------------- |
| [functor](/documentation/code/classes/classgambit_1_1functor/) * | **[_functor_base_ptr](/documentation/code/classes/classgambit_1_1safety__bucket__base/#variable-functor-base-ptr)**  |
| bool | **[_initialized](/documentation/code/classes/classgambit_1_1safety__bucket__base/#variable-initialized)**  |
| const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[whoami](/documentation/code/classes/classgambit_1_1safety__bucket__base/#variable-whoami)**  |


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

Updated on 2022-09-08 at 03:41:57 +0000