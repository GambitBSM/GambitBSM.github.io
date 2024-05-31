---
title: "class Gambit::Logging::BaseLogger"
description: "Logger virtual base class. "

---

# class Gambit::Logging::BaseLogger



Logger virtual base class. 


`#include <logging.hpp>`

Inherited by [Gambit::Logging::StdLogger](/documentation/code/classes/classgambit_1_1logging_1_1stdlogger/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual | **[~BaseLogger](/documentation/code/classes/classgambit_1_1logging_1_1baselogger/#function-baselogger)**()<br>Virtual destructor so we can delete the loggers by pointer to base.  |
| virtual void | **[write](/documentation/code/classes/classgambit_1_1logging_1_1baselogger/#function-write)**(const [SortedMessage](/documentation/code/classes/structgambit_1_1logging_1_1sortedmessage/) & ) =0<br>Write message.  |
| virtual void | **[flush](/documentation/code/classes/classgambit_1_1logging_1_1baselogger/#function-flush)**() =0<br>Flush stream buffer;.  |

## Public Functions Documentation

### function ~BaseLogger

```
virtual ~BaseLogger()
```

Virtual destructor so we can delete the loggers by pointer to base. 

%%%% Logger classes %%% 


### function write

```
virtual void write(
    const SortedMessage & 
) =0
```

Write message. 

**Reimplemented by**: [Gambit::Logging::StdLogger::write](/documentation/code/classes/classgambit_1_1logging_1_1stdlogger/#function-write)


### function flush

```
virtual void flush() =0
```

Flush stream buffer;. 

**Reimplemented by**: [Gambit::Logging::StdLogger::flush](/documentation/code/classes/classgambit_1_1logging_1_1stdlogger/#function-flush)


-------------------------------

Updated on 2024-05-31 at 15:12:04 +0000