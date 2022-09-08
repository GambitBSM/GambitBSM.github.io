---
title: "class Gambit::BEvariable_bucket"
description: "An interface class for backend variables. "

---

# class Gambit::BEvariable_bucket



An interface class for backend variables.  [More...](#detailed-description)


`#include <safety_bucket.hpp>`

Inherits from [Gambit::BE_bucket_base](/documentation/code/classes/classgambit_1_1be__bucket__base/), [Gambit::safety_bucket_base](/documentation/code/classes/classgambit_1_1safety__bucket__base/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BEvariable_bucket](/documentation/code/classes/classgambit_1_1bevariable__bucket/#function-bevariable-bucket)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) mym, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) myf, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) me, [backend_functor](/documentation/code/classes/classgambit_1_1backend__functor/)< TYPE *(*)(), TYPE * > * functor_ptr_in =NULL)<br>Constructor for [BEvariable_bucket](/documentation/code/classes/classgambit_1_1bevariable__bucket/).  |
| void | **[initialize](/documentation/code/classes/classgambit_1_1bevariable__bucket/#function-initialize)**([backend_functor](/documentation/code/classes/classgambit_1_1backend__functor/)< TYPE *(*)(), TYPE * > * functor_ptr_in)<br>Initialize this bucket with a functor pointer.  |
| TYPE & | **[operator*](/documentation/code/classes/classgambit_1_1bevariable__bucket/#function-operator)**()<br>Dereference the variable pointer stored as a [safe_variable_ptr]().  |
| TYPE * | **[operator->](/documentation/code/classes/classgambit_1_1bevariable__bucket/#function-operator)**()<br>Access member functions.  |
| TYPE * | **[pointer](/documentation/code/classes/classgambit_1_1bevariable__bucket/#function-pointer)**()<br>Get the underlying variable pointer.  |
| [safe_variable_ptr](/documentation/code/classes/classgambit_1_1safe__variable__ptr/)< TYPE > & | **[safe_pointer](/documentation/code/classes/classgambit_1_1bevariable__bucket/#function-safe-pointer)**()<br>Get the [safe_variable_ptr]().  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| [backend_functor](/documentation/code/classes/classgambit_1_1backend__functor/)< TYPE *(*)(), TYPE * > * | **[_functor_ptr](/documentation/code/classes/classgambit_1_1bevariable__bucket/#variable-functor-ptr)**  |
| [safe_variable_ptr](/documentation/code/classes/classgambit_1_1safe__variable__ptr/)< TYPE > | **[_svptr](/documentation/code/classes/classgambit_1_1bevariable__bucket/#variable-svptr)**  |

## Additional inherited members

**Public Functions inherited from [Gambit::BE_bucket_base](/documentation/code/classes/classgambit_1_1be__bucket__base/)**

|                | Name           |
| -------------- | -------------- |
| | **[BE_bucket_base](/documentation/code/classes/classgambit_1_1be__bucket__base/#function-be-bucket-base)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) mym, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) myf, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) me)<br>Constructor for [BE_bucket_base](/documentation/code/classes/classgambit_1_1be__bucket__base/).  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[backend](/documentation/code/classes/classgambit_1_1be__bucket__base/#function-backend)**()<br>Get backend name.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[version](/documentation/code/classes/classgambit_1_1be__bucket__base/#function-version)**()<br>Get version information.  |

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


## Detailed Description

```
template <typename TYPE >
class Gambit::BEvariable_bucket;
```

An interface class for backend variables. 
## Public Functions Documentation

### function BEvariable_bucket

```
inline BEvariable_bucket(
    str mym,
    str myf,
    str me,
    backend_functor< TYPE *(*)(), TYPE * > * functor_ptr_in =NULL
)
```

Constructor for [BEvariable_bucket](/documentation/code/classes/classgambit_1_1bevariable__bucket/). 

### function initialize

```
inline void initialize(
    backend_functor< TYPE *(*)(), TYPE * > * functor_ptr_in
)
```

Initialize this bucket with a functor pointer. 

### function operator*

```
inline TYPE & operator*()
```

Dereference the variable pointer stored as a [safe_variable_ptr](). 

### function operator->

```
inline TYPE * operator->()
```

Access member functions. 

### function pointer

```
inline TYPE * pointer()
```

Get the underlying variable pointer. 

### function safe_pointer

```
inline safe_variable_ptr< TYPE > & safe_pointer()
```

Get the [safe_variable_ptr](). 

## Protected Attributes Documentation

### variable _functor_ptr

```
backend_functor< TYPE *(*)(), TYPE * > * _functor_ptr;
```


### variable _svptr

```
safe_variable_ptr< TYPE > _svptr;
```


-------------------------------

Updated on 2022-09-08 at 03:08:02 +0000