---
title: "class Gambit::Piped_exceptions"
description: "[Gambit](/documentation/code/namespaces/namespacegambit/) piped error class. "

---

# class Gambit::Piped_exceptions



[Gambit](/documentation/code/namespaces/namespacegambit/) piped error class. 


`#include <exceptions.hpp>`

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef std::pair< std::string, std::string > | **[description](/documentation/code/classes/classgambit_1_1piped__exceptions/#typedef-description)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Piped_exceptions](/documentation/code/classes/classgambit_1_1piped__exceptions/#function-piped-exceptions)**(size_t maxExceptions)<br>Constructor.  |
| void | **[request](/documentation/code/classes/classgambit_1_1piped__exceptions/#function-request)**(std::string origin, std::string message)<br>Request an exception.  |
| void | **[request](/documentation/code/classes/classgambit_1_1piped__exceptions/#function-request)**(description desc)<br>Request a piped exception.  |
| void | **[check](/documentation/code/classes/classgambit_1_1piped__exceptions/#function-check)**([exception](/documentation/code/classes/classgambit_1_1exception/) & excep)<br>Check whether any exceptions were requested, and raise them.  |
| bool | **[inquire](/documentation/code/classes/classgambit_1_1piped__exceptions/#function-inquire)**()<br>Check whether any exceptions were requested without handling them.  |
| bool | **[inquire](/documentation/code/classes/classgambit_1_1piped__exceptions/#function-inquire)**(std::string message)<br>Check whether any exceptions with a specific message were requested, without handling them.  |

## Public Types Documentation

### typedef description

```
typedef std::pair<std::string,std::string> Gambit::Piped_exceptions::description;
```


## Public Functions Documentation

### function Piped_exceptions

```
inline Piped_exceptions(
    size_t maxExceptions
)
```

Constructor. 

### function request

```
void request(
    std::string origin,
    std::string message
)
```

Request an exception. 

Request a piped exception. 


### function request

```
void request(
    description desc
)
```

Request a piped exception. 

### function check

```
void check(
    exception & excep
)
```

Check whether any exceptions were requested, and raise them. 

### function inquire

```
bool inquire()
```

Check whether any exceptions were requested without handling them. 

### function inquire

```
bool inquire(
    std::string message
)
```

Check whether any exceptions with a specific message were requested, without handling them. 

-------------------------------

Updated on 2025-02-12 at 15:36:38 +0000