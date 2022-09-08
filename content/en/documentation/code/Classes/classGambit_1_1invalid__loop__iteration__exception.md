---
title: "class Gambit::invalid_loop_iteration_exception"
description: "[Gambit](/documentation/code/namespaces/namespacegambit/) invalid loop iteration exception class. "

---

# class Gambit::invalid_loop_iteration_exception



[Gambit](/documentation/code/namespaces/namespacegambit/) invalid loop iteration exception class. 


`#include <exceptions.hpp>`

Inherits from [Gambit::special_exception](/documentation/code/classes/classgambit_1_1special__exception/), std::exception

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[invalid_loop_iteration_exception](/documentation/code/classes/classgambit_1_1invalid__loop__iteration__exception/#function-invalid-loop-iteration-exception)**()<br>Constructor.  |

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

### function invalid_loop_iteration_exception

```
invalid_loop_iteration_exception()
```

Constructor. 

[Gambit](/documentation/code/namespaces/namespacegambit/) invalid loop iteration exception class methods.

Constructor 


-------------------------------

Updated on 2022-09-08 at 03:17:31 +0000