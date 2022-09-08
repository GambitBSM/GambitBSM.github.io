---
title: "class Gambit::invalid_point_exception"
description: "[Gambit](/documentation/code/namespaces/namespacegambit/) invalid point exception class. "

---

# class Gambit::invalid_point_exception



[Gambit](/documentation/code/namespaces/namespacegambit/) invalid point exception class. 


`#include <exceptions.hpp>`

Inherits from [Gambit::special_exception](/documentation/code/classes/classgambit_1_1special__exception/), std::exception

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[invalid_point_exception](/documentation/code/classes/classgambit_1_1invalid__point__exception/)**()<br>Constructor.  |
| void | **[set_thrower](/documentation/code/classes/classgambit_1_1invalid__point__exception/)**([functor](/documentation/code/classes/classgambit_1_1functor/) * thrown_from)<br>Set the pointer to the functor that threw the invalid point exception.  |
| [functor](/documentation/code/classes/classgambit_1_1functor/) * | **[thrower](/documentation/code/classes/classgambit_1_1invalid__point__exception/)**()<br>Retrieve pointer to the functor that threw the invalid point exception.  |
| virtual void | **[raise](/documentation/code/classes/classgambit_1_1invalid__point__exception/)**(const std::string & msg)<br>Raise the exception, i.e. throw it. Exact override of base method.  |
| virtual void | **[raise](/documentation/code/classes/classgambit_1_1invalid__point__exception/)**(const std::string & msg, int code)<br>Raise the exception, i.e. throw it with a message and code.  |

## Additional inherited members

**Public Functions inherited from [Gambit::special_exception](/documentation/code/classes/classgambit_1_1special__exception/)**

|                | Name           |
| -------------- | -------------- |
| | **[special_exception](/documentation/code/classes/classgambit_1_1special__exception/)**(const char * what)<br>Constructor.  |
| virtual | **[~special_exception](/documentation/code/classes/classgambit_1_1special__exception/)**()<br>Destructor.  |
| virtual const char * | **[what](/documentation/code/classes/classgambit_1_1special__exception/)**() const<br>Retrieve the identity of the exception.  |
| std::string | **[message](/documentation/code/classes/classgambit_1_1special__exception/)**()<br>Retrieve the message that this exception was raised with.  |

**Public Attributes inherited from [Gambit::special_exception](/documentation/code/classes/classgambit_1_1special__exception/)**

|                | Name           |
| -------------- | -------------- |
| int | **[invalidcode](/documentation/code/classes/classgambit_1_1special__exception/)** <br>Integer code used for exceptions.  |

**Protected Attributes inherited from [Gambit::special_exception](/documentation/code/classes/classgambit_1_1special__exception/)**

|                | Name           |
| -------------- | -------------- |
| std::string | **[myMessage](/documentation/code/classes/classgambit_1_1special__exception/)** <br>The message passed when this exception is raised.  |


## Public Functions Documentation

### function invalid_point_exception

```
invalid_point_exception()
```

Constructor. 

[Gambit](/documentation/code/namespaces/namespacegambit/) invalid point exception class methods.

Constructor 


### function set_thrower

```
void set_thrower(
    functor * thrown_from
)
```

Set the pointer to the functor that threw the invalid point exception. 

### function thrower

```
functor * thrower()
```

Retrieve pointer to the functor that threw the invalid point exception. 

### function raise

```
virtual void raise(
    const std::string & msg
)
```

Raise the exception, i.e. throw it. Exact override of base method. 

**Reimplements**: [Gambit::special_exception::raise](/documentation/code/classes/classgambit_1_1special__exception/)


Raise the invalid point exception, i.e throw it with a message and a default code. 


### function raise

```
virtual void raise(
    const std::string & msg,
    int code
)
```

Raise the exception, i.e. throw it with a message and code. 

Raise the invalid point exception, i.e. throw it with a message and a code. 


-------------------------------

Updated on 2022-09-08 at 01:05:16 +0000