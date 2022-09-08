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
| | **[BEvariable_bucket](/documentation/code/classes/classgambit_1_1bevariable__bucket/#function-gambitbevariable-bucket-bevariable-bucket)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) mym, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) myf, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) me, [backend_functor](/documentation/code/classes/classgambit_1_1backend__functor/)< TYPE *(*)(), TYPE * > * functor_ptr_in =NULL)<br>Constructor for [BEvariable_bucket](/documentation/code/classes/classgambit_1_1bevariable__bucket/).  |
| void | **[initialize](/documentation/code/classes/classgambit_1_1bevariable__bucket/#function-gambitbevariable-bucket-initialize)**([backend_functor](/documentation/code/classes/classgambit_1_1backend__functor/)< TYPE *(*)(), TYPE * > * functor_ptr_in)<br>Initialize this bucket with a functor pointer.  |
| TYPE & | **[operator*](/documentation/code/classes/classgambit_1_1bevariable__bucket/#function-gambitbevariable-bucket-operator)**()<br>Dereference the variable pointer stored as a [safe_variable_ptr]().  |
| TYPE * | **[operator->](/documentation/code/classes/classgambit_1_1bevariable__bucket/#function-gambitbevariable-bucket-operator)**()<br>Access member functions.  |
| TYPE * | **[pointer](/documentation/code/classes/classgambit_1_1bevariable__bucket/#function-gambitbevariable-bucket-pointer)**()<br>Get the underlying variable pointer.  |
| [safe_variable_ptr](/documentation/code/classes/classgambit_1_1safe__variable__ptr/)< TYPE > & | **[safe_pointer](/documentation/code/classes/classgambit_1_1bevariable__bucket/#function-gambitbevariable-bucket-safe-pointer)**()<br>Get the [safe_variable_ptr]().  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| [backend_functor](/documentation/code/classes/classgambit_1_1backend__functor/)< TYPE *(*)(), TYPE * > * | **[_functor_ptr](/documentation/code/classes/classgambit_1_1bevariable__bucket/#variable-gambitbevariable-bucket-functor-ptr)**  |
| [safe_variable_ptr](/documentation/code/classes/classgambit_1_1safe__variable__ptr/)< TYPE > | **[_svptr](/documentation/code/classes/classgambit_1_1bevariable__bucket/#variable-gambitbevariable-bucket-svptr)**  |

## Additional inherited members

**Public Functions inherited from [Gambit::BE_bucket_base](/documentation/code/classes/classgambit_1_1be__bucket__base/)**

|                | Name           |
| -------------- | -------------- |
| | **[BE_bucket_base](/documentation/code/classes/classgambit_1_1be__bucket__base/#function-gambitbe-bucket-base-be-bucket-base)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) mym, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) myf, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) me)<br>Constructor for [BE_bucket_base](/documentation/code/classes/classgambit_1_1be__bucket__base/).  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[backend](/documentation/code/classes/classgambit_1_1be__bucket__base/#function-gambitbe-bucket-base-backend)**()<br>Get backend name.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[version](/documentation/code/classes/classgambit_1_1be__bucket__base/#function-gambitbe-bucket-base-version)**()<br>Get version information.  |

**Public Functions inherited from [Gambit::safety_bucket_base](/documentation/code/classes/classgambit_1_1safety__bucket__base/)**

|                | Name           |
| -------------- | -------------- |
| | **[safety_bucket_base](/documentation/code/classes/classgambit_1_1safety__bucket__base/#function-gambitsafety-bucket-base-safety-bucket-base)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) myinfo)<br>Master constructor.  |
| bool | **[active](/documentation/code/classes/classgambit_1_1safety__bucket__base/#function-gambitsafety-bucket-base-active)**() |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[name](/documentation/code/classes/classgambit_1_1safety__bucket__base/#function-gambitsafety-bucket-base-name)**()<br>Get capability name.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[origin](/documentation/code/classes/classgambit_1_1safety__bucket__base/#function-gambitsafety-bucket-base-origin)**()<br>Get name of origin (module/backend).  |

**Protected Functions inherited from [Gambit::safety_bucket_base](/documentation/code/classes/classgambit_1_1safety__bucket__base/)**

|                | Name           |
| -------------- | -------------- |
| void | **[dieGracefully](/documentation/code/classes/classgambit_1_1safety__bucket__base/#function-gambitsafety-bucket-base-diegracefully)**() const<br>Failure message invoked when the user tries to access the object before it is initialized.  |

**Protected Attributes inherited from [Gambit::safety_bucket_base](/documentation/code/classes/classgambit_1_1safety__bucket__base/)**

|                | Name           |
| -------------- | -------------- |
| [functor](/documentation/code/classes/classgambit_1_1functor/) * | **[_functor_base_ptr](/documentation/code/classes/classgambit_1_1safety__bucket__base/#variable-gambitsafety-bucket-base-functor-base-ptr)**  |
| bool | **[_initialized](/documentation/code/classes/classgambit_1_1safety__bucket__base/#variable-gambitsafety-bucket-base-initialized)**  |
| const [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[whoami](/documentation/code/classes/classgambit_1_1safety__bucket__base/#variable-gambitsafety-bucket-base-whoami)**  |


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

Updated on 2022-09-08 at 02:00:46 +0000