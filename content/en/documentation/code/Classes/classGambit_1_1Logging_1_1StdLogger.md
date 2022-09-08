---
title: "class Gambit::Logging::StdLogger"
description: "Logger for 'standard' messages. "

---

# class Gambit::Logging::StdLogger



Logger for 'standard' messages. 


`#include <logging.hpp>`

Inherits from [Gambit::Logging::BaseLogger](/documentation/code/classes/classgambit_1_1logging_1_1baselogger/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[StdLogger](/documentation/code/classes/classgambit_1_1logging_1_1stdlogger/#function-gambitloggingstdlogger-stdlogger)**(std::ostream & logstream)<br>Constructor.  |
| | **[StdLogger](/documentation/code/classes/classgambit_1_1logging_1_1stdlogger/#function-gambitloggingstdlogger-stdlogger)**(const std::string & filename)<br>Alternate constructor.  |
| virtual | **[~StdLogger](/documentation/code/classes/classgambit_1_1logging_1_1stdlogger/#function-gambitloggingstdlogger-stdlogger)**()<br>Destructor.  |
| virtual void | **[write](/documentation/code/classes/classgambit_1_1logging_1_1stdlogger/#function-gambitloggingstdlogger-write)**(const [SortedMessage](/documentation/code/classes/structgambit_1_1logging_1_1sortedmessage/) & mail)<br>Write message.  |
| virtual void | **[flush](/documentation/code/classes/classgambit_1_1logging_1_1stdlogger/#function-gambitloggingstdlogger-flush)**()<br>Flush stream buffer.  |
| void | **[writetags](/documentation/code/classes/classgambit_1_1logging_1_1stdlogger/#function-gambitloggingstdlogger-writetags)**(const std::set< LogTag > & tags)<br>Look up names corresponding to tags and write them out to the stream.  |
| void | **[writetags](/documentation/code/classes/classgambit_1_1logging_1_1stdlogger/#function-gambitloggingstdlogger-writetags)**(const std::set< int > & tags) |

## Additional inherited members

**Public Functions inherited from [Gambit::Logging::BaseLogger](/documentation/code/classes/classgambit_1_1logging_1_1baselogger/)**

|                | Name           |
| -------------- | -------------- |
| virtual | **[~BaseLogger](/documentation/code/classes/classgambit_1_1logging_1_1baselogger/#function-gambitloggingbaselogger-baselogger)**()<br>Virtual destructor so we can delete the loggers by pointer to base.  |


## Public Functions Documentation

### function StdLogger

```
StdLogger(
    std::ostream & logstream
)
```

Constructor. 

"Standard" logger class

Constructor Attach logger object to an existing stream 


### function StdLogger

```
StdLogger(
    const std::string & filename
)
```

Alternate constructor. 

Open new file stream and manage it internally. 


### function ~StdLogger

```
virtual ~StdLogger()
```

Destructor. 

### function write

```
virtual void write(
    const SortedMessage & mail
)
```

Write message. 

**Reimplements**: [Gambit::Logging::BaseLogger::write](/documentation/code/classes/classgambit_1_1logging_1_1baselogger/#function-gambitloggingbaselogger-write)


Write message to log file. 


### function flush

```
virtual void flush()
```

Flush stream buffer. 

**Reimplements**: [Gambit::Logging::BaseLogger::flush](/documentation/code/classes/classgambit_1_1logging_1_1baselogger/#function-gambitloggingbaselogger-flush)


### function writetags

```
void writetags(
    const std::set< LogTag > & tags
)
```

Look up names corresponding to tags and write them out to the stream. 

### function writetags

```
void writetags(
    const std::set< int > & tags
)
```


-------------------------------

Updated on 2022-09-08 at 01:48:55 +0000