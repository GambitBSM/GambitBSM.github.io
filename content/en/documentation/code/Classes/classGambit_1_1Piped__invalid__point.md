---
title: "class Gambit::Piped_invalid_point"
description: "[Gambit](/documentation/code/namespaces/namespacegambit/) piped invalid point exception class. "

---

# class Gambit::Piped_invalid_point



[Gambit](/documentation/code/namespaces/namespacegambit/) piped invalid point exception class. 


`#include <exceptions.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Piped_invalid_point](/documentation/code/classes/classgambit_1_1piped__invalid__point/#function-piped-invalid-point)**()<br>Constructor.  |
| void | **[request](/documentation/code/classes/classgambit_1_1piped__invalid__point/#function-request)**(std::string message)<br>Request an exception.  |
| void | **[check](/documentation/code/classes/classgambit_1_1piped__invalid__point/#function-check)**()<br>Check whether an exception was requested, and throw it if necessary.  |

## Public Functions Documentation

### function Piped_invalid_point

```
inline Piped_invalid_point()
```

Constructor. 

### function request

```
void request(
    std::string message
)
```

Request an exception. 

Request a piped invalid point exception. 


### function check

```
void check()
```

Check whether an exception was requested, and throw it if necessary. 

Check whether a piped invalid point exception was requested, and throw if necessary. 


-------------------------------

Updated on 2023-06-26 at 21:36:51 +0000