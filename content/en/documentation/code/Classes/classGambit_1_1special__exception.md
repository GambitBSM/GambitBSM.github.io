---
title: "class Gambit::special_exception"
description: "GAMBIT special exception class. Not logged, meant for always catching. "

---

# class Gambit::special_exception



GAMBIT special exception class. Not logged, meant for always catching. 


`#include <exceptions.hpp>`

Inherits from std::exception

Inherited by [Gambit::halt_loop_exception](/documentation/code/classes/classgambit_1_1halt__loop__exception/), [Gambit::invalid_loop_iteration_exception](/documentation/code/classes/classgambit_1_1invalid__loop__iteration__exception/), [Gambit::invalid_point_exception](/documentation/code/classes/classgambit_1_1invalid__point__exception/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[special_exception](/documentation/code/classes/classgambit_1_1special__exception/#function-special-exception)**(const char * what)<br>Constructor.  |
| virtual | **[~special_exception](/documentation/code/classes/classgambit_1_1special__exception/#function-special-exception)**()<br>Destructor.  |
| virtual const char * | **[what](/documentation/code/classes/classgambit_1_1special__exception/#function-what)**() const<br>Retrieve the identity of the exception.  |
| std::string | **[message](/documentation/code/classes/classgambit_1_1special__exception/#function-message)**()<br>Retrieve the message that this exception was raised with.  |
| virtual void | **[raise](/documentation/code/classes/classgambit_1_1special__exception/#function-raise)**(const std::string & msg)<br>Raise the exception, i.e. throw it.  |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| int | **[invalidcode](/documentation/code/classes/classgambit_1_1special__exception/#variable-invalidcode)** <br>Integer code used for exceptions.  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| std::string | **[myMessage](/documentation/code/classes/classgambit_1_1special__exception/#variable-mymessage)** <br>The message passed when this exception is raised.  |

## Public Functions Documentation

### function special_exception

```
special_exception(
    const char * what
)
```

Constructor. 

GAMBIT special exception class methods.

Constructor 


### function ~special_exception

```
inline virtual ~special_exception()
```

Destructor. 

### function what

```
virtual const char * what() const
```

Retrieve the identity of the exception. 

### function message

```
std::string message()
```

Retrieve the message that this exception was raised with. 

### function raise

```
virtual void raise(
    const std::string & msg
)
```

Raise the exception, i.e. throw it. 

**Reimplemented by**: [Gambit::invalid_point_exception::raise](/documentation/code/classes/classgambit_1_1invalid__point__exception/#function-raise)


Raise the exception, i.e. throw it with a message. 


## Public Attributes Documentation

### variable invalidcode

```
int invalidcode;
```

Integer code used for exceptions. 

## Protected Attributes Documentation

### variable myMessage

```
std::string myMessage;
```

The message passed when this exception is raised. 

-------------------------------

Updated on 2024-05-31 at 15:12:03 +0000