---
title: "class Gambit::dep_bucket"
description: "An interface class for module dependencies. "

---

# class Gambit::dep_bucket



An interface class for module dependencies.  [More...](#detailed-description)


`#include <safety_bucket.hpp>`

Inherits from [Gambit::safety_bucket_base](/documentation/code/classes/classgambit_1_1safety__bucket__base/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[dep_bucket](/documentation/code/classes/classgambit_1_1dep__bucket/)**([str](/documentation/code/namespaces/namespacegambit/) mym, [str](/documentation/code/namespaces/namespacegambit/) myf, [str](/documentation/code/namespaces/namespacegambit/) me, [module_functor](/documentation/code/classes/classgambit_1_1module__functor/)< TYPE > * functor_ptr_in =NULL, [module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/) * dependent_functor_ptr_in =NULL)<br>Constructor for [dep_bucket](/documentation/code/classes/classgambit_1_1dep__bucket/).  |
| void | **[initialize](/documentation/code/classes/classgambit_1_1dep__bucket/)**([module_functor](/documentation/code/classes/classgambit_1_1module__functor/)< TYPE > * functor_ptr_in, [module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/) * dependent_functor_ptr_in)<br>Initialize this bucket with a depedency functor pointer.  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[module](/documentation/code/classes/classgambit_1_1dep__bucket/)**()<br>Get module name.  |
| const TYPE & | **[operator*](/documentation/code/classes/classgambit_1_1dep__bucket/)**() const<br>Dereference the dependency pointer stored as a [safe_ptr]().  |
| const TYPE * | **[operator->](/documentation/code/classes/classgambit_1_1dep__bucket/)**() const<br>Access is allowed to const member functions only.  |
| [safe_ptr](/documentation/code/classes/classgambit_1_1safe__ptr/)< TYPE > & | **[safe_pointer](/documentation/code/classes/classgambit_1_1dep__bucket/)**()<br>Get the [safe_ptr]().  |
| bool | **[use_thread_index](/documentation/code/classes/classgambit_1_1dep__bucket/)**([module_functor](/documentation/code/classes/classgambit_1_1module__functor/)< TYPE > * f1, [module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/) * f2)<br>Check if the thread index needs to be used to access the functor's result.  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| [module_functor](/documentation/code/classes/classgambit_1_1module__functor/)< TYPE > * | **[_functor_ptr](/documentation/code/classes/classgambit_1_1dep__bucket/)**  |
| [safe_ptr](/documentation/code/classes/classgambit_1_1safe__ptr/)< TYPE > | **[_sptr](/documentation/code/classes/classgambit_1_1dep__bucket/)**  |
| [module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/) * | **[_dependent_functor_ptr](/documentation/code/classes/classgambit_1_1dep__bucket/)**  |

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


## Detailed Description

```
template <typename TYPE >
class Gambit::dep_bucket;
```

An interface class for module dependencies. 
## Public Functions Documentation

### function dep_bucket

```
inline dep_bucket(
    str mym,
    str myf,
    str me,
    module_functor< TYPE > * functor_ptr_in =NULL,
    module_functor_common * dependent_functor_ptr_in =NULL
)
```

Constructor for [dep_bucket](/documentation/code/classes/classgambit_1_1dep__bucket/). 

### function initialize

```
inline void initialize(
    module_functor< TYPE > * functor_ptr_in,
    module_functor_common * dependent_functor_ptr_in
)
```

Initialize this bucket with a depedency functor pointer. 

### function module

```
inline str module()
```

Get module name. 

### function operator*

```
inline const TYPE & operator*() const
```

Dereference the dependency pointer stored as a [safe_ptr](). 

### function operator->

```
inline const TYPE * operator->() const
```

Access is allowed to const member functions only. 

### function safe_pointer

```
inline safe_ptr< TYPE > & safe_pointer()
```

Get the [safe_ptr](). 

### function use_thread_index

```
static inline bool use_thread_index(
    module_functor< TYPE > * f1,
    module_functor_common * f2
)
```

Check if the thread index needs to be used to access the functor's result. 

## Protected Attributes Documentation

### variable _functor_ptr

```
module_functor< TYPE > * _functor_ptr;
```


### variable _sptr

```
safe_ptr< TYPE > _sptr;
```


### variable _dependent_functor_ptr

```
module_functor_common * _dependent_functor_ptr;
```


-------------------------------

Updated on 2022-09-08 at 01:05:15 +0000