---
title: "class Gambit::Backends::mathematica_function"
description: "Holds the info about a Mathematica backend function, and defines conversion functions. "

---

# class Gambit::Backends::mathematica_function



Holds the info about a Mathematica backend function, and defines conversion functions.  [More...](#detailed-description)


`#include <mathematica_function.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[mathematica_function](/documentation/code/classes/classgambit_1_1backends_1_1mathematica__function/#function-mathematica-function)**(const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & be, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & ver, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & symbol)<br>Constructor.  |
| TYPE | **[operator()](/documentation/code/classes/classgambit_1_1backends_1_1mathematica__function/#function-operator)**(ARGS &&... args)<br>Operation (execute function and return value)  |

## Detailed Description

```
template <typename TYPE ,
typename... ARGS>
class Gambit::Backends::mathematica_function;
```

Holds the info about a Mathematica backend function, and defines conversion functions. 
## Public Functions Documentation

### function mathematica_function

```
inline mathematica_function(
    const str & be,
    const str & ver,
    const str & symbol
)
```

Constructor. 

### function operator()

```
inline TYPE operator()(
    ARGS &&... args
)
```

Operation (execute function and return value) 

-------------------------------

Updated on 2025-02-12 at 15:36:38 +0000