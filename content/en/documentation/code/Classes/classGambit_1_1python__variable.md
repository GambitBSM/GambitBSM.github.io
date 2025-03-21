---
title: "class Gambit::python_variable"
description: "Holds the info about a python backend variable, and defines conversion functions. "

---

# class Gambit::python_variable



Holds the info about a python backend variable, and defines conversion functions.  [More...](#detailed-description)


`#include <python_variable.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[python_variable](/documentation/code/classes/classgambit_1_1python__variable/#function-python-variable)**(const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & , const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & , const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & )<br>Constructor.  |
| [python_variable](/documentation/code/classes/classgambit_1_1python__variable/) & | **[operator=](/documentation/code/classes/classgambit_1_1python__variable/#function-operator)**(const TYPE & )<br>Assignment operator for [python_variable](/documentation/code/classes/classgambit_1_1python__variable/) from equivalent C++ type.  |
| | **[operator TYPE const](/documentation/code/classes/classgambit_1_1python__variable/#function-operator-type-const)**()<br>Cast operator from [python_variable](/documentation/code/classes/classgambit_1_1python__variable/) to equivalent C++ type.  |

## Detailed Description

```
template <typename TYPE >
class Gambit::python_variable;
```

Holds the info about a python backend variable, and defines conversion functions. 
## Public Functions Documentation

### function python_variable

```
inline python_variable(
    const str & ,
    const str & ,
    const str & 
)
```

Constructor. 

### function operator=

```
inline python_variable & operator=(
    const TYPE & 
)
```

Assignment operator for [python_variable](/documentation/code/classes/classgambit_1_1python__variable/) from equivalent C++ type. 

### function operator TYPE const

```
inline operator TYPE const()
```

Cast operator from [python_variable](/documentation/code/classes/classgambit_1_1python__variable/) to equivalent C++ type. 

-------------------------------

Updated on 2025-02-12 at 16:10:31 +0000