---
title: "class Gambit::omp_safe_ptr"

description: "[No description available]"

---

# class Gambit::omp_safe_ptr



[No description available] [More...](#detailed-description)


`#include <util_types.hpp>`

Inherits from [Gambit::safe_ptr< TYPE >](/documentation/code/classes/classgambit_1_1safe__ptr/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[omp_safe_ptr](/documentation/code/classes/classgambit_1_1omp__safe__ptr/#function-omp-safe-ptr)**(TYPE * in_ptr =NULL)<br>Constructor.  |
| virtual const TYPE & | **[operator*](/documentation/code/classes/classgambit_1_1omp__safe__ptr/#function-operator)**() const<br>Dereference pointer.  |

## Additional inherited members

**Public Functions inherited from [Gambit::safe_ptr< TYPE >](/documentation/code/classes/classgambit_1_1safe__ptr/)**

|                | Name           |
| -------------- | -------------- |
| | **[safe_ptr](/documentation/code/classes/classgambit_1_1safe__ptr/#function-safe-ptr)**(TYPE * in_ptr =NULL)<br>Construct-o-safe_ptr.  |
| virtual void | **[set](/documentation/code/classes/classgambit_1_1safe__ptr/#function-set)**(TYPE * in_ptr)<br>Set pointer.  |
| virtual const TYPE & | **[operator[]](/documentation/code/classes/classgambit_1_1safe__ptr/#function-operator)**(int index) const<br>Dereference pointer as if it is an array.  |
| virtual const TYPE * | **[operator->](/documentation/code/classes/classgambit_1_1safe__ptr/#function-operator)**() const<br>Access is allowed to const member functions only.  |
| virtual bool | **[isNull](/documentation/code/classes/classgambit_1_1safe__ptr/#function-isnull)**() const |

**Protected Functions inherited from [Gambit::safe_ptr< TYPE >](/documentation/code/classes/classgambit_1_1safe__ptr/)**

|                | Name           |
| -------------- | -------------- |
| void | **[dieGracefully](/documentation/code/classes/classgambit_1_1safe__ptr/#function-diegracefully)**()<br>Failure message invoked when the user tries to dereference a null [safe_ptr](/documentation/code/classes/classgambit_1_1safe__ptr/).  |

**Protected Attributes inherited from [Gambit::safe_ptr< TYPE >](/documentation/code/classes/classgambit_1_1safe__ptr/)**

|                | Name           |
| -------------- | -------------- |
| const TYPE * | **[ptr](/documentation/code/classes/classgambit_1_1safe__ptr/#variable-ptr)** <br>The actual underlying pointer, interpreted as a pointer to constant value.  |


## Detailed Description

```
template <typename TYPE >
class Gambit::omp_safe_ptr;
```


A safe pointer designed to point at an array, and return the entry in that array corresponding to the current OpenMP thread. 

## Public Functions Documentation

### function omp_safe_ptr

```
inline omp_safe_ptr(
    TYPE * in_ptr =NULL
)
```

Constructor. 

### function operator*

```
inline virtual const TYPE & operator*() const
```

Dereference pointer. 

**Reimplements**: [Gambit::safe_ptr::operator*](/documentation/code/classes/classgambit_1_1safe__ptr/#function-operator)


-------------------------------

Updated on 2022-09-07 at 23:22:05 +0000