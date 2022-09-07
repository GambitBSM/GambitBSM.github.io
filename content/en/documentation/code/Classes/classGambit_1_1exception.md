---
title: 'class Gambit::exception'
description: 'GAMBIT exception base class. '

---

# Gambit::exception



GAMBIT exception base class. 


`#include <exceptions.hpp>`

Inherits from std::exception

Inherited by [Gambit::error](/documentation/code/classes/classgambit_1_1error/), [Gambit::warning](/documentation/code/classes/classgambit_1_1warning/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[exception](/documentation/code/classes/classgambit_1_1exception/#function-exception)**(const char * kind, const char * what, const char * message, const char * inikey, bool fatal)<br>Constructor without log tags.  |
| | **[exception](/documentation/code/classes/classgambit_1_1exception/#function-exception)**(const char * kind, const char * what, const char * message, const char * inikey, bool fatal, LogTag t1)<br>Constructor with 1 log tag.  |
| | **[exception](/documentation/code/classes/classgambit_1_1exception/#function-exception)**(const char * kind, const char * what, const char * message, const char * inikey, bool fatal, LogTag t1, LogTag t2)<br>Constructor with 2 log tags.  |
| | **[exception](/documentation/code/classes/classgambit_1_1exception/#function-exception)**(const char * kind, const char * what, const char * message, const char * inikey, bool fatal, LogTag t1, LogTag t2, LogTag t3)<br>Constructor with 3 log tags.  |
| | **[exception](/documentation/code/classes/classgambit_1_1exception/#function-exception)**(const char * kind, const char * what, const char * message, const char * inikey, bool fatal, LogTag t1, LogTag t2, LogTag t3, LogTag t4)<br>Constructor with 4 log tags.  |
| | **[exception](/documentation/code/classes/classgambit_1_1exception/#function-exception)**(const char * kind, const char * what, const char * message, const char * inikey, bool fatal, LogTag t1, LogTag t2, LogTag t3, LogTag t4, LogTag t5)<br>Constructor with 5 log tags.  |
| | **[exception](/documentation/code/classes/classgambit_1_1exception/#function-exception)**(const char * kind, const char * what, const char * message, const char * inikey, bool fatal, LogTag t1, LogTag t2, LogTag t3, LogTag t4, LogTag t5, LogTag t6)<br>Constructor with 6 log tags.  |
| | **[exception](/documentation/code/classes/classgambit_1_1exception/#function-exception)**(const char * kind, const char * what, const char * message, const char * inikey, bool fatal, LogTag t1, LogTag t2, LogTag t3, LogTag t4, LogTag t5, LogTag t6, LogTag t7)<br>Constructor with 7 log tags.  |
| | **[exception](/documentation/code/classes/classgambit_1_1exception/#function-exception)**(const char * kind, const char * what, const char * message, const char * inikey, bool fatal, std::set< LogTag > tags)<br>Constructor with log tags as a set.  |
| void | **[forced_throw](/documentation/code/classes/classgambit_1_1exception/#function-forced-throw)**(const std::string & origin, const std::string & specific_message)<br>Log the exception and throw it regardless of whether is is fatal or not.  |
| void | **[silent_forced_throw](/documentation/code/classes/classgambit_1_1exception/#function-silent-forced-throw)**()<br>As per forced_throw but without logging.  |
| virtual | **[~exception](/documentation/code/classes/classgambit_1_1exception/#function-exception)**()<br>Destructor.  |
| void | **[set_fatal](/documentation/code/classes/classgambit_1_1exception/#function-set-fatal)**(bool fatal)<br>Setter for the fatal flag.  |
| virtual const char * | **[what](/documentation/code/classes/classgambit_1_1exception/#function-what)**() const<br>Retrieve the identity of the exception.  |
| void | **[raise](/documentation/code/classes/classgambit_1_1exception/#function-raise)**(const std::string & origin, const std::string & specific_message) |
| const std::map< const char *, [exception](/documentation/code/classes/classgambit_1_1exception/) * > & | **[all_exceptions](/documentation/code/classes/classgambit_1_1exception/#function-all-exceptions)**()<br>Get a read-only map of pointers to all instances of this class.  |
| void | **[set_parameters](/documentation/code/classes/classgambit_1_1exception/#function-set-parameters)**(std::string params)<br>Set the parameter point string to append if a fatal exception is thrown.  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| std::set< LogTag > | **[myLogTags](/documentation/code/classes/classgambit_1_1exception/#variable-mylogtags)** <br>The set of tags to be passed to the logger.  |

## Public Functions Documentation

### function exception

```
exception(
    const char * kind,
    const char * what,
    const char * message,
    const char * inikey,
    bool fatal
)
```

Constructor without log tags. 

Constructors

Constructor without log tags 


### function exception

```
exception(
    const char * kind,
    const char * what,
    const char * message,
    const char * inikey,
    bool fatal,
    LogTag t1
)
```

Constructor with 1 log tag. 

### function exception

```
exception(
    const char * kind,
    const char * what,
    const char * message,
    const char * inikey,
    bool fatal,
    LogTag t1,
    LogTag t2
)
```

Constructor with 2 log tags. 

### function exception

```
exception(
    const char * kind,
    const char * what,
    const char * message,
    const char * inikey,
    bool fatal,
    LogTag t1,
    LogTag t2,
    LogTag t3
)
```

Constructor with 3 log tags. 

### function exception

```
exception(
    const char * kind,
    const char * what,
    const char * message,
    const char * inikey,
    bool fatal,
    LogTag t1,
    LogTag t2,
    LogTag t3,
    LogTag t4
)
```

Constructor with 4 log tags. 

### function exception

```
exception(
    const char * kind,
    const char * what,
    const char * message,
    const char * inikey,
    bool fatal,
    LogTag t1,
    LogTag t2,
    LogTag t3,
    LogTag t4,
    LogTag t5
)
```

Constructor with 5 log tags. 

### function exception

```
exception(
    const char * kind,
    const char * what,
    const char * message,
    const char * inikey,
    bool fatal,
    LogTag t1,
    LogTag t2,
    LogTag t3,
    LogTag t4,
    LogTag t5,
    LogTag t6
)
```

Constructor with 6 log tags. 

### function exception

```
exception(
    const char * kind,
    const char * what,
    const char * message,
    const char * inikey,
    bool fatal,
    LogTag t1,
    LogTag t2,
    LogTag t3,
    LogTag t4,
    LogTag t5,
    LogTag t6,
    LogTag t7
)
```

Constructor with 7 log tags. 

### function exception

```
exception(
    const char * kind,
    const char * what,
    const char * message,
    const char * inikey,
    bool fatal,
    std::set< LogTag > tags
)
```

Constructor with log tags as a set. 

### function forced_throw

```
void forced_throw(
    const std::string & origin,
    const std::string & specific_message
)
```

Log the exception and throw it regardless of whether is is fatal or not. 

Force a throw of the exception. These should only be used inside a try block, i.e. if you plan to catch the exception.

Log the exception and throw it regardless of whether is is fatal or not. 


### function silent_forced_throw

```
void silent_forced_throw()
```

As per forced_throw but without logging. 

### function ~exception

```
inline virtual ~exception()
```

Destructor. 

### function set_fatal

```
void set_fatal(
    bool fatal
)
```

Setter for the fatal flag. 

### function what

```
virtual const char * what() const
```

Retrieve the identity of the exception. 

### function raise

```
void raise(
    const std::string & origin,
    const std::string & specific_message
)
```


Raise the exception. Log the exception and, if it is considered fatal, actually throw it. This is the canonical way to trigger a GAMBIT error or warning.

Raise the exception. Log the exception and, if it is considered fatal, actually throw it. This is the regular way to trigger a GAMBIT error or warning. 


### function all_exceptions

```
static const std::map< const char *, exception * > & all_exceptions()
```

Get a read-only map of pointers to all instances of this class. 

### function set_parameters

```
static void set_parameters(
    std::string params
)
```

Set the parameter point string to append if a fatal exception is thrown. 

## Protected Attributes Documentation

### variable myLogTags

```
std::set< LogTag > myLogTags;
```

The set of tags to be passed to the logger. 

-------------------------------

Updated on 2022-09-07 at 14:07:44 +0000