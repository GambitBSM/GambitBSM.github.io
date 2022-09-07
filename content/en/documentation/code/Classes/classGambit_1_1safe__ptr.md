---
title: 'class Gambit::safe_ptr'

description: "[No description available]"

---

# Gambit::safe_ptr



[No description available] [More...](#detailed-description)


`#include <util_types.hpp>`

Inherited by [Gambit::omp_safe_ptr< TYPE >](/documentation/code/classes/classgambit_1_1omp__safe__ptr/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[safe_ptr](/documentation/code/classes/classgambit_1_1safe__ptr/#function-safe-ptr)**(TYPE * in_ptr =NULL)<br>Construct-o-safe_ptr.  |
| virtual void | **[set](/documentation/code/classes/classgambit_1_1safe__ptr/#function-set)**(TYPE * in_ptr)<br>Set pointer.  |
| virtual const TYPE & | **[operator*](/documentation/code/classes/classgambit_1_1safe__ptr/#function-operator)**() const<br>Dereference pointer.  |
| virtual const TYPE & | **[operator[]](/documentation/code/classes/classgambit_1_1safe__ptr/#function-operator)**(int index) const<br>Dereference pointer as if it is an array.  |
| virtual const TYPE * | **[operator->](/documentation/code/classes/classgambit_1_1safe__ptr/#function-operator)**() const<br>Access is allowed to const member functions only.  |
| virtual bool | **[isNull](/documentation/code/classes/classgambit_1_1safe__ptr/#function-isnull)**() const |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[dieGracefully](/documentation/code/classes/classgambit_1_1safe__ptr/#function-diegracefully)**()<br>Failure message invoked when the user tries to dereference a null [safe_ptr](/documentation/code/classes/classgambit_1_1safe__ptr/).  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| const TYPE * | **[ptr](/documentation/code/classes/classgambit_1_1safe__ptr/#variable-ptr)** <br>The actual underlying pointer, interpreted as a pointer to constant value.  |

## Detailed Description

```
template <typename TYPE >
class Gambit::safe_ptr;
```


A safe pointer that throws an informative error if you try to dereference it when nullified, and cannot be used to overwrite the thing it points to. 

## Public Functions Documentation

### function safe_ptr

```
inline safe_ptr(
    TYPE * in_ptr =NULL
)
```

Construct-o-safe_ptr. 

### function set

```
inline virtual void set(
    TYPE * in_ptr
)
```

Set pointer. 

### function operator*

```
inline virtual const TYPE & operator*() const
```

Dereference pointer. 

**Reimplemented by**: [Gambit::omp_safe_ptr::operator*](/documentation/code/classes/classgambit_1_1omp__safe__ptr/#function-operator)


### function operator[]

```
inline virtual const TYPE & operator[](
    int index
) const
```

Dereference pointer as if it is an array. 

### function operator->

```
inline virtual const TYPE * operator->() const
```

Access is allowed to const member functions only. 

### function isNull

```
inline virtual bool isNull() const
```


## Protected Functions Documentation

### function dieGracefully

```
static inline void dieGracefully()
```

Failure message invoked when the user tries to dereference a null [safe_ptr](/documentation/code/classes/classgambit_1_1safe__ptr/). 

## Protected Attributes Documentation

### variable ptr

```
const TYPE * ptr;
```

The actual underlying pointer, interpreted as a pointer to constant value. 

-------------------------------

Updated on 2022-09-07 at 14:07:44 +0000