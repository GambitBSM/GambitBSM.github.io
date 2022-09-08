---
title: "class Gambit::safe_variable_ptr"

description: "[No description available]"

---

# class Gambit::safe_variable_ptr



[No description available] [More...](#detailed-description)


`#include <util_types.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| [safe_variable_ptr](/documentation/code/classes/classgambit_1_1safe__variable__ptr/) & | **[operator=](/documentation/code/classes/classgambit_1_1safe__variable__ptr/#function-operator)**(const [safe_variable_ptr](/documentation/code/classes/classgambit_1_1safe__variable__ptr/) & ) =delete<br>Remove the default copy constructor and assignment operator.  |
| | **[safe_variable_ptr](/documentation/code/classes/classgambit_1_1safe__variable__ptr/#function-safe-variable-ptr)**(const [safe_variable_ptr](/documentation/code/classes/classgambit_1_1safe__variable__ptr/) & ) =delete |
| | **[safe_variable_ptr](/documentation/code/classes/classgambit_1_1safe__variable__ptr/#function-safe-variable-ptr)**(TYPE * in_ptr =NULL)<br>Constructor.  |
| void | **[set](/documentation/code/classes/classgambit_1_1safe__variable__ptr/#function-set)**(TYPE * in_ptr)<br>Set pointer.  |
| TYPE * | **[get](/documentation/code/classes/classgambit_1_1safe__variable__ptr/#function-get)**()<br>Get pointer.  |
| TYPE & | **[operator*](/documentation/code/classes/classgambit_1_1safe__variable__ptr/#function-operator)**()<br>Dereference pointer.  |
| TYPE & | **[operator[]](/documentation/code/classes/classgambit_1_1safe__variable__ptr/#function-operator)**(int index)<br>Dereference pointer as if it is an array.  |
| TYPE * | **[operator->](/documentation/code/classes/classgambit_1_1safe__variable__ptr/#function-operator)**()<br>Access member functions.  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[dieGracefully](/documentation/code/classes/classgambit_1_1safe__variable__ptr/#function-diegracefully)**()<br>Failure message invoked when the user tries to dereference a null [safe_variable_ptr](/documentation/code/classes/classgambit_1_1safe__variable__ptr/).  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| TYPE * | **[ptr](/documentation/code/classes/classgambit_1_1safe__variable__ptr/#variable-ptr)** <br>The actual underlying pointer.  |

## Detailed Description

```
template <typename TYPE >
class Gambit::safe_variable_ptr;
```


A safe variable pointer that throws an informative error if you try to dereference it when nullified, but unlike [safe_ptr](/documentation/code/classes/classgambit_1_1safe__ptr/) it can be used to overwrite the thing it points to. However, it is not possible to change the address of this pointer without using the 'set' function (in which case you presumably know what you're doing). 

## Public Functions Documentation

### function operator=

```
safe_variable_ptr & operator=(
    const safe_variable_ptr & 
) =delete
```

Remove the default copy constructor and assignment operator. 

### function safe_variable_ptr

```
safe_variable_ptr(
    const safe_variable_ptr & 
) =delete
```


### function safe_variable_ptr

```
inline safe_variable_ptr(
    TYPE * in_ptr =NULL
)
```

Constructor. 

### function set

```
inline void set(
    TYPE * in_ptr
)
```

Set pointer. 

### function get

```
inline TYPE * get()
```

Get pointer. 

### function operator*

```
inline TYPE & operator*()
```

Dereference pointer. 

### function operator[]

```
inline TYPE & operator[](
    int index
)
```

Dereference pointer as if it is an array. 

### function operator->

```
inline TYPE * operator->()
```

Access member functions. 

## Protected Functions Documentation

### function dieGracefully

```
static inline void dieGracefully()
```

Failure message invoked when the user tries to dereference a null [safe_variable_ptr](/documentation/code/classes/classgambit_1_1safe__variable__ptr/). 

## Protected Attributes Documentation

### variable ptr

```
TYPE * ptr;
```

The actual underlying pointer. 

-------------------------------

Updated on 2022-09-08 at 03:17:32 +0000