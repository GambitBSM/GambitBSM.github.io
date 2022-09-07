---
title: 'class Gambit::safety_bucket_base'
description: 'Base class for the interface classes '[dep_bucket](/documentation/code/classes/classgambit_1_1dep__bucket/)', '[BEvariable_bucket](/documentation/code/classes/classgambit_1_1bevariable__bucket/)' and '[BEfunction_bucket](/documentation/code/classes/classgambit_1_1befunction__bucket/)'. '

---

# Gambit::safety_bucket_base



Base class for the interface classes '[dep_bucket](/documentation/code/classes/classgambit_1_1dep__bucket/)', '[BEvariable_bucket](/documentation/code/classes/classgambit_1_1bevariable__bucket/)' and '[BEfunction_bucket](/documentation/code/classes/classgambit_1_1befunction__bucket/)'. 


`#include <safety_bucket.hpp>`

Inherited by [Gambit::BE_bucket_base](/documentation/code/classes/classgambit_1_1be__bucket__base/), [Gambit::dep_bucket< TYPE >](/documentation/code/classes/classgambit_1_1dep__bucket/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[safety_bucket_base](/documentation/code/classes/classgambit_1_1safety__bucket__base/#function-safety-bucket-base)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) myinfo)<br>Master constructor.  |
| bool | **[active](/documentation/code/classes/classgambit_1_1safety__bucket__base/#function-active)**() |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[name](/documentation/code/classes/classgambit_1_1safety__bucket__base/#function-name)**()<br>Get capability name.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[origin](/documentation/code/classes/classgambit_1_1safety__bucket__base/#function-origin)**()<br>Get name of origin (module/backend).  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[dieGracefully](/documentation/code/classes/classgambit_1_1safety__bucket__base/#function-diegracefully)**() const<br>Failure message invoked when the user tries to access the object before it is initialized.  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| [functor](/documentation/code/classes/classgambit_1_1functor/) * | **[_functor_base_ptr](/documentation/code/classes/classgambit_1_1safety__bucket__base/#variable-functor-base-ptr)**  |
| bool | **[_initialized](/documentation/code/classes/classgambit_1_1safety__bucket__base/#variable-initialized)**  |
| const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[whoami](/documentation/code/classes/classgambit_1_1safety__bucket__base/#variable-whoami)**  |

## Public Functions Documentation

### function safety_bucket_base

```
inline safety_bucket_base(
    str myinfo
)
```

Master constructor. 

### function active

```
inline bool active()
```


Ask whether the bucket has been initialised with a valid pointer or not, i.e. has the dependency resolver activated this dependency / backend req? 


### function name

```
inline str name()
```

Get capability name. 

### function origin

```
inline str origin()
```

Get name of origin (module/backend). 

## Protected Functions Documentation

### function dieGracefully

```
inline void dieGracefully() const
```

Failure message invoked when the user tries to access the object before it is initialized. 

## Protected Attributes Documentation

### variable _functor_base_ptr

```
functor * _functor_base_ptr;
```


### variable _initialized

```
bool _initialized;
```


### variable whoami

```
const str whoami;
```


-------------------------------

Updated on 2022-09-07 at 14:07:44 +0000