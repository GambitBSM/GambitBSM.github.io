---
title: "class Gambit::Suspicious_point_exception"
description: "[Gambit](/documentation/code/namespaces/namespacegambit/) suspicious point exception class. "

---

# class Gambit::Suspicious_point_exception



[Gambit](/documentation/code/namespaces/namespacegambit/) suspicious point exception class. 


`#include <exceptions.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Suspicious_point_exception](/documentation/code/classes/classgambit_1_1suspicious__point__exception/#function-suspicious-point-exception)**()<br>Constructor.  |
| void | **[raise](/documentation/code/classes/classgambit_1_1suspicious__point__exception/#function-raise)**(const std::string & msg, int code, bool debug)<br>Raise the suspicious point exception. Print it with a message and a code. The default code is 1.  |

## Public Functions Documentation

### function Suspicious_point_exception

```
inline Suspicious_point_exception()
```

Constructor. 

### function raise

```
void raise(
    const std::string & msg,
    int code,
    bool debug
)
```

Raise the suspicious point exception. Print it with a message and a code. The default code is 1. 

-------------------------------

Updated on 2024-07-18 at 13:53:30 +0000