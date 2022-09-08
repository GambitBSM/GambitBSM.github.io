---
title: "class Gambit::warning"
description: "GAMBIT warning class. "

---

# class Gambit::warning



GAMBIT warning class. 


`#include <exceptions.hpp>`

Inherits from [Gambit::exception](/documentation/code/classes/classgambit_1_1exception/), std::exception

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[warning](/documentation/code/classes/classgambit_1_1warning/)**(const char * message, const char * inikey)<br>GAMBIT warning class constructors.  |
| | **[warning](/documentation/code/classes/classgambit_1_1warning/)**(const char * message, const char * inikey, LogTag t1)<br>Constructor with 1 log tag.  |
| | **[warning](/documentation/code/classes/classgambit_1_1warning/)**(const char * message, const char * inikey, LogTag t1, LogTag t2)<br>Constructor with 2 log tags.  |
| | **[warning](/documentation/code/classes/classgambit_1_1warning/)**(const char * message, const char * inikey, LogTag t1, LogTag t2, LogTag t3)<br>Constructor with 3 log tags.  |
| | **[warning](/documentation/code/classes/classgambit_1_1warning/)**(const char * message, const char * inikey, LogTag t1, LogTag t2, LogTag t3, LogTag t4)<br>Constructor with 4 log tags.  |
| | **[warning](/documentation/code/classes/classgambit_1_1warning/)**(const char * message, const char * inikey, LogTag t1, LogTag t2, LogTag t3, LogTag t4, LogTag t5)<br>Constructor with 5 log tags.  |
| | **[warning](/documentation/code/classes/classgambit_1_1warning/)**(const char * message, const char * inikey, LogTag t1, LogTag t2, LogTag t3, LogTag t4, LogTag t5, LogTag t6)<br>Constructor with 6 log tags.  |
| | **[warning](/documentation/code/classes/classgambit_1_1warning/)**(const char * message, const char * inikey, std::set< LogTag > tags)<br>Constructor with log tags as a set.  |

## Additional inherited members

**Public Functions inherited from [Gambit::exception](/documentation/code/classes/classgambit_1_1exception/)**

|                | Name           |
| -------------- | -------------- |
| | **[exception](/documentation/code/classes/classgambit_1_1exception/)**(const char * kind, const char * what, const char * message, const char * inikey, bool fatal)<br>Constructor without log tags.  |
| | **[exception](/documentation/code/classes/classgambit_1_1exception/)**(const char * kind, const char * what, const char * message, const char * inikey, bool fatal, LogTag t1)<br>Constructor with 1 log tag.  |
| | **[exception](/documentation/code/classes/classgambit_1_1exception/)**(const char * kind, const char * what, const char * message, const char * inikey, bool fatal, LogTag t1, LogTag t2)<br>Constructor with 2 log tags.  |
| | **[exception](/documentation/code/classes/classgambit_1_1exception/)**(const char * kind, const char * what, const char * message, const char * inikey, bool fatal, LogTag t1, LogTag t2, LogTag t3)<br>Constructor with 3 log tags.  |
| | **[exception](/documentation/code/classes/classgambit_1_1exception/)**(const char * kind, const char * what, const char * message, const char * inikey, bool fatal, LogTag t1, LogTag t2, LogTag t3, LogTag t4)<br>Constructor with 4 log tags.  |
| | **[exception](/documentation/code/classes/classgambit_1_1exception/)**(const char * kind, const char * what, const char * message, const char * inikey, bool fatal, LogTag t1, LogTag t2, LogTag t3, LogTag t4, LogTag t5)<br>Constructor with 5 log tags.  |
| | **[exception](/documentation/code/classes/classgambit_1_1exception/)**(const char * kind, const char * what, const char * message, const char * inikey, bool fatal, LogTag t1, LogTag t2, LogTag t3, LogTag t4, LogTag t5, LogTag t6)<br>Constructor with 6 log tags.  |
| | **[exception](/documentation/code/classes/classgambit_1_1exception/)**(const char * kind, const char * what, const char * message, const char * inikey, bool fatal, LogTag t1, LogTag t2, LogTag t3, LogTag t4, LogTag t5, LogTag t6, LogTag t7)<br>Constructor with 7 log tags.  |
| | **[exception](/documentation/code/classes/classgambit_1_1exception/)**(const char * kind, const char * what, const char * message, const char * inikey, bool fatal, std::set< LogTag > tags)<br>Constructor with log tags as a set.  |
| void | **[forced_throw](/documentation/code/classes/classgambit_1_1exception/)**(const std::string & origin, const std::string & specific_message)<br>Log the exception and throw it regardless of whether is is fatal or not.  |
| void | **[silent_forced_throw](/documentation/code/classes/classgambit_1_1exception/)**()<br>As per forced_throw but without logging.  |
| virtual | **[~exception](/documentation/code/classes/classgambit_1_1exception/)**()<br>Destructor.  |
| void | **[set_fatal](/documentation/code/classes/classgambit_1_1exception/)**(bool fatal)<br>Setter for the fatal flag.  |
| virtual const char * | **[what](/documentation/code/classes/classgambit_1_1exception/)**() const<br>Retrieve the identity of the exception.  |
| void | **[raise](/documentation/code/classes/classgambit_1_1exception/)**(const std::string & origin, const std::string & specific_message) |
| const std::map< const char *, [exception](/documentation/code/classes/classgambit_1_1exception/) * > & | **[all_exceptions](/documentation/code/classes/classgambit_1_1exception/)**()<br>Get a read-only map of pointers to all instances of this class.  |
| void | **[set_parameters](/documentation/code/classes/classgambit_1_1exception/)**(std::string params)<br>Set the parameter point string to append if a fatal exception is thrown.  |

**Protected Attributes inherited from [Gambit::exception](/documentation/code/classes/classgambit_1_1exception/)**

|                | Name           |
| -------------- | -------------- |
| std::set< LogTag > | **[myLogTags](/documentation/code/classes/classgambit_1_1exception/)** <br>The set of tags to be passed to the logger.  |


## Public Functions Documentation

### function warning

```
warning(
    const char * message,
    const char * inikey
)
```

GAMBIT warning class constructors. 

Constructors

Constructor without log tags

Constructor without log tags 


### function warning

```
warning(
    const char * message,
    const char * inikey,
    LogTag t1
)
```

Constructor with 1 log tag. 

### function warning

```
warning(
    const char * message,
    const char * inikey,
    LogTag t1,
    LogTag t2
)
```

Constructor with 2 log tags. 

### function warning

```
warning(
    const char * message,
    const char * inikey,
    LogTag t1,
    LogTag t2,
    LogTag t3
)
```

Constructor with 3 log tags. 

### function warning

```
warning(
    const char * message,
    const char * inikey,
    LogTag t1,
    LogTag t2,
    LogTag t3,
    LogTag t4
)
```

Constructor with 4 log tags. 

### function warning

```
warning(
    const char * message,
    const char * inikey,
    LogTag t1,
    LogTag t2,
    LogTag t3,
    LogTag t4,
    LogTag t5
)
```

Constructor with 5 log tags. 

### function warning

```
warning(
    const char * message,
    const char * inikey,
    LogTag t1,
    LogTag t2,
    LogTag t3,
    LogTag t4,
    LogTag t5,
    LogTag t6
)
```

Constructor with 6 log tags. 

### function warning

```
warning(
    const char * message,
    const char * inikey,
    std::set< LogTag > tags
)
```

Constructor with log tags as a set. 

-------------------------------

Updated on 2022-09-08 at 01:05:16 +0000