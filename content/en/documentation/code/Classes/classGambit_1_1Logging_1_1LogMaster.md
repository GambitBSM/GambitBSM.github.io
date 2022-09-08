---
title: "class Gambit::Logging::LogMaster"

description: "[No description available]"

---

# class Gambit::Logging::LogMaster



[No description available] [More...](#detailed-description)


`#include <logmaster.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[LogMaster](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/#function-logmaster)**()<br>Default constructor.  |
| | **[LogMaster](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/#function-logmaster)**(std::map< std::set< int >, [BaseLogger](/documentation/code/classes/classgambit_1_1logging_1_1baselogger/) * > & loggersIN)<br>Alternate constructor.  |
| | **[~LogMaster](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/#function-logmaster)**() |
| void | **[init_memory](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/#function-init-memory)**()<br>Initialise dynamic memory required for thread safety.  |
| void | **[initialise](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/#function-initialise)**(std::vector< std::pair< std::set< std::string >, std::string > > & loggerinfo)<br>Function to construct loggers according to blueprint.  |
| void | **[initialise](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/#function-initialise)**(std::map< std::set< std::string >, std::string > & loggerinfo) |
| void | **[initialise](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/#function-initialise)**(std::map< std::string, std::string > & loggerinfo) |
| void | **[disable](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/#function-disable)**() |
| bool | **[disabled](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/#function-disabled)**() |
| void | **[enable](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/#function-enable)**() |
| void | **[emit_backlog](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/#function-emit-backlog)**(bool verbose)<br>Print the backlogs to the default log file.  |
| void | **[input](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/#function-input)**(const std::string & in)<br>Functions for stream input (actual stream operators which use these are defined in [logger.cpp]())  |
| void | **[input](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/#function-input)**(const LogTag & tag)<br>Handle LogTag input.  |
| void | **[input](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/#function-input)**(const [endofmessage](/documentation/code/classes/structgambit_1_1logging_1_1endofmessage/) & )<br>Handle end of message character.  |
| void | **[input](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/#function-input)**(const manip1)<br>Handle various stream manipulators.  |
| void | **[input](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/#function-input)**(const manip2) |
| void | **[input](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/#function-input)**(const manip3) |
| void | **[send](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/#function-send)**(const std::string & message)<br>Main logging function (user-friendly overloaded version)  |
| void | **[send](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/#function-send)**(const std::string & message, LogTag tag1) |
| void | **[send](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/#function-send)**(const std::string & message, LogTag tag1, LogTag tag2) |
| void | **[send](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/#function-send)**(const std::string & message, LogTag tag1, LogTag tag2, LogTag tag3) |
| void | **[send](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/#function-send)**(const std::string & message, LogTag tag1, LogTag tag2, LogTag tag3, LogTag tag4) |
| void | **[send](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/#function-send)**(const std::string & message, LogTag tag1, LogTag tag2, LogTag tag3, LogTag tag4, LogTag tag5) |
| void | **[send](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/#function-send)**(const std::ostringstream & message)<br>stringstream versions....  |
| void | **[send](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/#function-send)**(const std::ostringstream & message, LogTag tag1) |
| void | **[send](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/#function-send)**(const std::ostringstream & message, LogTag tag1, LogTag tag2) |
| void | **[send](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/#function-send)**(const std::ostringstream & message, LogTag tag1, LogTag tag2, LogTag tag3) |
| void | **[send](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/#function-send)**(const std::ostringstream & message, LogTag tag1, LogTag tag2, LogTag tag3, LogTag tag4) |
| void | **[send](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/#function-send)**(const std::ostringstream & message, LogTag tag1, LogTag tag2, LogTag tag3, LogTag tag4, LogTag tag5) |
| void | **[send](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/#function-send)**(const std::string & message, std::set< LogTag > & tags)<br>Internal version of main logging function.  |
| void | **[send](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/#function-send)**(const std::string & message, std::set< int > & tags)<br>Serious version of main logging function.  |
| void | **[finalsend](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/#function-finalsend)**(const [Message](/documentation/code/classes/structgambit_1_1logging_1_1message/) & mail)<br>Version of send function used by buffer dump; skips all the tag modification stuff.  |
| void | **[send](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/#function-send)**(const std::ostringstream & message, std::set< LogTag > & tags)<br>stringstream overloads...  |
| void | **[send](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/#function-send)**(const std::ostringstream & message, std::set< int > & tags) |
| void | **[entering_module](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/#function-entering-module)**(int i)<br>Set the internal variables tracking which module and/or backend is currently running.  |
| void | **[leaving_module](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/#function-leaving-module)**() |
| void | **[entering_backend](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/#function-entering-backend)**(int i) |
| void | **[leaving_backend](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/#function-leaving-backend)**() |
| void | **[set_log_debug_messages](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/#function-set-log-debug-messages)**(bool flag)<br>Choose whether "Debug" tagged log messages will be ignored (i.e. not logged)  |

## Detailed Description

```
class Gambit::Logging::LogMaster;
```


[Logging](/documentation/code/namespaces/namespacegambit_1_1logging/) "controller" object Keeps track of the various "Logger" objects 

## Public Functions Documentation

### function LogMaster

```
LogMaster()
```

Default constructor. 

Logger class member function definitions.

[Logging](/documentation/code/namespaces/namespacegambit_1_1logging/) "controller" object Keeps track of the individual logging objects. 


### function LogMaster

```
LogMaster(
    std::map< std::set< int >, BaseLogger * > & loggersIN
)
```

Alternate constructor. 

Alternate constructor Mainly for testing; lets you pass in pre-built loggers and their tags 


### function ~LogMaster

```
~LogMaster()
```


Destructor If errors happen before the inifile is loaded, we need to dump the log messages (that have been buffered) into a default log file. These will be log messages coming from initialisation code and so on. 


### function init_memory

```
void init_memory()
```

Initialise dynamic memory required for thread safety. 

### function initialise

```
void initialise(
    std::vector< std::pair< std::set< std::string >, std::string > > & loggerinfo
)
```

Function to construct loggers according to blueprint. 

### function initialise

```
void initialise(
    std::map< std::set< std::string >, std::string > & loggerinfo
)
```


### function initialise

```
void initialise(
    std::map< std::string, std::string > & loggerinfo
)
```


### function disable

```
void disable()
```


### function disabled

```
bool disabled()
```


### function enable

```
void enable()
```


### function emit_backlog

```
void emit_backlog(
    bool verbose
)
```

Print the backlogs to the default log file. 

### function input

```
void input(
    const std::string & in
)
```

Functions for stream input (actual stream operators which use these are defined in [logger.cpp]()) 

Handle strings. 


### function input

```
void input(
    const LogTag & tag
)
```

Handle LogTag input. 

### function input

```
void input(
    const endofmessage & 
)
```

Handle end of message character. 

### function input

```
void input(
    const manip1
)
```

Handle various stream manipulators. 

### function input

```
void input(
    const manip2
)
```


### function input

```
void input(
    const manip3
)
```


### function send

```
void send(
    const std::string & message
)
```

Main logging function (user-friendly overloaded version) 

### function send

```
void send(
    const std::string & message,
    LogTag tag1
)
```


### function send

```
void send(
    const std::string & message,
    LogTag tag1,
    LogTag tag2
)
```


### function send

```
void send(
    const std::string & message,
    LogTag tag1,
    LogTag tag2,
    LogTag tag3
)
```


### function send

```
void send(
    const std::string & message,
    LogTag tag1,
    LogTag tag2,
    LogTag tag3,
    LogTag tag4
)
```


### function send

```
void send(
    const std::string & message,
    LogTag tag1,
    LogTag tag2,
    LogTag tag3,
    LogTag tag4,
    LogTag tag5
)
```


### function send

```
void send(
    const std::ostringstream & message
)
```

stringstream versions.... 

### function send

```
void send(
    const std::ostringstream & message,
    LogTag tag1
)
```


### function send

```
void send(
    const std::ostringstream & message,
    LogTag tag1,
    LogTag tag2
)
```


### function send

```
void send(
    const std::ostringstream & message,
    LogTag tag1,
    LogTag tag2,
    LogTag tag3
)
```


### function send

```
void send(
    const std::ostringstream & message,
    LogTag tag1,
    LogTag tag2,
    LogTag tag3,
    LogTag tag4
)
```


### function send

```
void send(
    const std::ostringstream & message,
    LogTag tag1,
    LogTag tag2,
    LogTag tag3,
    LogTag tag4,
    LogTag tag5
)
```


### function send

```
void send(
    const std::string & message,
    std::set< LogTag > & tags
)
```

Internal version of main logging function. 

### function send

```
void send(
    const std::string & message,
    std::set< int > & tags
)
```

Serious version of main logging function. 

### function finalsend

```
void finalsend(
    const Message & mail
)
```

Version of send function used by buffer dump; skips all the tag modification stuff. 

### function send

```
void send(
    const std::ostringstream & message,
    std::set< LogTag > & tags
)
```

stringstream overloads... 

### function send

```
void send(
    const std::ostringstream & message,
    std::set< int > & tags
)
```


### function entering_module

```
void entering_module(
    int i
)
```

Set the internal variables tracking which module and/or backend is currently running. 

### function leaving_module

```
void leaving_module()
```


### function entering_backend

```
void entering_backend(
    int i
)
```


### function leaving_backend

```
void leaving_backend()
```


### function set_log_debug_messages

```
inline void set_log_debug_messages(
    bool flag
)
```

Choose whether "Debug" tagged log messages will be ignored (i.e. not logged) 

Setters for behaviour options Must be used before "initialise" in order to have any effect Choose whether a separate log file for each MPI process is used NOW FORBIDDEN! Always must be true to avoid concurrent write access issues void set_separate_file_per_process(bool flag) {separate_file_per_process=flag;} 


-------------------------------

Updated on 2022-09-08 at 03:08:03 +0000