---
title: "class Gambit::halt_loop_exception"
description: "[Gambit](/documentation/code/namespaces/namespacegambit/) halt loop exception class. "

---

# class Gambit::halt_loop_exception



[Gambit](/documentation/code/namespaces/namespacegambit/) halt loop exception class. 


`#include <exceptions.hpp>`

Inherits from [Gambit::special_exception](/documentation/code/classes/classgambit_1_1special__exception/), std::exception

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[halt_loop_exception](/documentation/code/classes/classgambit_1_1halt__loop__exception/#function-halt-loop-exception)**()<br>Constructor.  |

## Additional inherited members

**Public Functions inherited from [Gambit::special_exception](/documentation/code/classes/classgambit_1_1special__exception/)**

|                | Name           |
| -------------- | -------------- |
| | **[special_exception](/documentation/code/classes/classgambit_1_1special__exception/#function-special-exception)**(const char * what)<br>Constructor.  |
| virtual | **[~special_exception](/documentation/code/classes/classgambit_1_1special__exception/#function-special-exception)**()<br>Destructor.  |
| virtual const char * | **[what](/documentation/code/classes/classgambit_1_1special__exception/#function-what)**() const<br>Retrieve the identity of the exception.  |
| std::string | **[message](/documentation/code/classes/classgambit_1_1special__exception/#function-message)**()<br>Retrieve the message that this exception was raised with.  |
| virtual void | **[raise](/documentation/code/classes/classgambit_1_1special__exception/#function-raise)**(const std::string & msg)<br>Raise the exception, i.e. throw it.  |

**Public Attributes inherited from [Gambit::special_exception](/documentation/code/classes/classgambit_1_1special__exception/)**

|                | Name           |
| -------------- | -------------- |
| int | **[invalidcode](/documentation/code/classes/classgambit_1_1special__exception/#variable-invalidcode)** <br>Integer code used for exceptions.  |

**Protected Attributes inherited from [Gambit::special_exception](/documentation/code/classes/classgambit_1_1special__exception/)**

|                | Name           |
| -------------- | -------------- |
| std::string | **[myMessage](/documentation/code/classes/classgambit_1_1special__exception/#variable-mymessage)** <br>The message passed when this exception is raised.  |


## Public Functions Documentation

### function halt_loop_exception

```
halt_loop_exception()
```

Constructor. 

[Gambit](/documentation/code/namespaces/namespacegambit/) halt loop exception class methods.

Constructor 


-------------------------------

Updated on 2023-06-26 at 21:36:50 +0000