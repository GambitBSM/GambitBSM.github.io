---
title: "namespace Gambit::Logging"
description: "Forward declare minimial logging components needed to use logger. "

---

# namespace Gambit::Logging

Forward declare minimial logging components needed to use logger. 

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Gambit::Logging::BaseLogger](/documentation/code/classes/classgambit_1_1logging_1_1baselogger/)** <br>Logger virtual base class.  |
| struct | **[Gambit::Logging::endofmessage](/documentation/code/classes/structgambit_1_1logging_1_1endofmessage/)** <br>Special (empty) struct for signalling end of message to [LogMaster]() stream.  |
| struct | **[Gambit::Logging::ensure_construction_order](/documentation/code/classes/structgambit_1_1logging_1_1ensure__construction__order/)**  |
| class | **[Gambit::Logging::LogMaster](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/)**  |
| struct | **[Gambit::Logging::Message](/documentation/code/classes/structgambit_1_1logging_1_1message/)** <br>structure for storing log messages and metadata  |
| struct | **[Gambit::Logging::SortedMessage](/documentation/code/classes/structgambit_1_1logging_1_1sortedmessage/)** <br>structure for storing log messages and metadata after tags are sorted  |
| class | **[Gambit::Logging::StdLogger](/documentation/code/classes/classgambit_1_1logging_1_1stdlogger/)** <br>Logger for 'standard' messages.  |

## Types

|                | Name           |
| -------------- | -------------- |
| typedef std::ostream &(*)(std::ostream &) | **[manip1](/documentation/code/namespaces/namespacegambit_1_1logging/#typedef-gambitlogging-manip1)**  |
| typedef std::basic_ios< std::ostream::char_type, std::ostream::traits_type > | **[ios_type](/documentation/code/namespaces/namespacegambit_1_1logging/#typedef-gambitlogging-ios-type)**  |
| typedef ios_type &(*)(ios_type &) | **[manip2](/documentation/code/namespaces/namespacegambit_1_1logging/#typedef-gambitlogging-manip2)**  |
| typedef std::ios_base &(*)(std::ios_base &) | **[manip3](/documentation/code/namespaces/namespacegambit_1_1logging/#typedef-gambitlogging-manip3)**  |

## Functions

|                | Name           |
| -------------- | -------------- |
| EXPORT_SYMBOLS [LogMaster](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/) & | **[operator<<](/documentation/code/namespaces/namespacegambit_1_1logging/#function-gambitlogging-operator)**([LogMaster](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/) & logobj, const std::string & in)<br>Stream functions for use with [LogMaster]().  |
| EXPORT_SYMBOLS [LogMaster](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/) & | **[operator<<](/documentation/code/namespaces/namespacegambit_1_1logging/#function-gambitlogging-operator)**([LogMaster](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/) & logobj, const LogTag & tag)<br>Handle LogTag input.  |
| EXPORT_SYMBOLS [LogMaster](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/) & | **[operator<<](/documentation/code/namespaces/namespacegambit_1_1logging/#function-gambitlogging-operator)**([LogMaster](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/) & logobj, const [endofmessage](/documentation/code/classes/structgambit_1_1logging_1_1endofmessage/) & eom)<br>Handle end of message character.  |
| EXPORT_SYMBOLS [LogMaster](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/) & | **[operator<<](/documentation/code/namespaces/namespacegambit_1_1logging/#function-gambitlogging-operator)**([LogMaster](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/) & logobj, const manip1)<br>Handle various stream manipulators.  |
| EXPORT_SYMBOLS [LogMaster](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/) & | **[operator<<](/documentation/code/namespaces/namespacegambit_1_1logging/#function-gambitlogging-operator)**([LogMaster](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/) & logobj, const manip2) |
| EXPORT_SYMBOLS [LogMaster](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/) & | **[operator<<](/documentation/code/namespaces/namespacegambit_1_1logging/#function-gambitlogging-operator)**([LogMaster](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/) & logobj, const manip3) |
| template <typename TYPE \> <br>[LogMaster](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/) & | **[operator<<](/documentation/code/namespaces/namespacegambit_1_1logging/#function-gambitlogging-operator)**([LogMaster](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/) & logobj, const TYPE & input) |
| template <typename TYPE \> <br>[LogMaster](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/) & | **[operator<<](/documentation/code/namespaces/namespacegambit_1_1logging/#function-gambitlogging-operator)**([LogMaster](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/) & logobj, TYPE & input) |
| int | **[str2tag](/documentation/code/namespaces/namespacegambit_1_1logging/#function-gambitlogging-str2tag)**(const std::string & tagname) |
| std::map< int, std::string > & | **[tag2str](/documentation/code/namespaces/namespacegambit_1_1logging/#function-gambitlogging-tag2str)**() |
| std::set< int > & | **[components](/documentation/code/namespaces/namespacegambit_1_1logging/#function-gambitlogging-components)**() |
| const Utils::time_point | **[start_time](/documentation/code/namespaces/namespacegambit_1_1logging/#function-gambitlogging-start-time)**(Utils::get_clock_now() ) |
| const std::set< LogTag > & | **[msgtypes](/documentation/code/namespaces/namespacegambit_1_1logging/#function-gambitlogging-msgtypes)**() |
| const std::set< LogTag > & | **[flags](/documentation/code/namespaces/namespacegambit_1_1logging/#function-gambitlogging-flags)**() |
| const std::set< LogTag > & | **[echoes](/documentation/code/namespaces/namespacegambit_1_1logging/#function-gambitlogging-echoes)**() |
| int | **[getfreetag](/documentation/code/namespaces/namespacegambit_1_1logging/#function-gambitlogging-getfreetag)**() |
| void | **[checktags](/documentation/code/namespaces/namespacegambit_1_1logging/#function-gambitlogging-checktags)**()<br>Function to inspect tags and their associated strings. For testing purposes only.  |
| std::map< int, std::string > | **[create_tag_names](/documentation/code/namespaces/namespacegambit_1_1logging/#function-gambitlogging-create-tag-names)**() |

## Attributes

|                | Name           |
| -------------- | -------------- |
| const bool | **[verbose](/documentation/code/namespaces/namespacegambit_1_1logging/#variable-gambitlogging-verbose)**  |

## Types Documentation

### typedef manip1

```
typedef std::ostream &(* Gambit::Logging::manip1) (std::ostream &);
```


### typedef ios_type

```
typedef std::basic_ios< std::ostream::char_type, std::ostream::traits_type > Gambit::Logging::ios_type;
```


### typedef manip2

```
typedef ios_type &(* Gambit::Logging::manip2) (ios_type &);
```


### typedef manip3

```
typedef std::ios_base &(* Gambit::Logging::manip3) (std::ios_base &);
```



## Functions Documentation

### function operator<<

```
EXPORT_SYMBOLS LogMaster & operator<<(
    LogMaster & logobj,
    const std::string & in
)
```

Stream functions for use with [LogMaster](). 

{@ Stream functions overloads for working with the logger

Stream functions for use with [LogMaster](/documentation/code/classes/classgambit_1_1logging_1_1logmaster/)


### function operator<<

```
EXPORT_SYMBOLS LogMaster & operator<<(
    LogMaster & logobj,
    const LogTag & tag
)
```

Handle LogTag input. 

### function operator<<

```
EXPORT_SYMBOLS LogMaster & operator<<(
    LogMaster & logobj,
    const endofmessage & eom
)
```

Handle end of message character. 

### function operator<<

```
EXPORT_SYMBOLS LogMaster & operator<<(
    LogMaster & logobj,
    const manip1
)
```

Handle various stream manipulators. 

### function operator<<

```
EXPORT_SYMBOLS LogMaster & operator<<(
    LogMaster & logobj,
    const manip2
)
```


### function operator<<

```
EXPORT_SYMBOLS LogMaster & operator<<(
    LogMaster & logobj,
    const manip3
)
```


### function operator<<

```
template <typename TYPE >
LogMaster & operator<<(
    LogMaster & logobj,
    const TYPE & input
)
```


### function operator<<

```
template <typename TYPE >
LogMaster & operator<<(
    LogMaster & logobj,
    TYPE & input
)
```


### function str2tag

```
int str2tag(
    const std::string & tagname
)
```


### function tag2str

```
std::map< int, std::string > & tag2str()
```


### function components

```
std::set< int > & components()
```


### function start_time

```
static const Utils::time_point start_time(
    Utils::get_clock_now() 
)
```


### function msgtypes

```
const std::set< LogTag > & msgtypes()
```


### function flags

```
const std::set< LogTag > & flags()
```


### function echoes

```
const std::set< LogTag > & echoes()
```


### function getfreetag

```
int getfreetag()
```


### function checktags

```
void checktags()
```

Function to inspect tags and their associated strings. For testing purposes only. 

### function create_tag_names

```
static std::map< int, std::string > create_tag_names()
```



## Attributes Documentation

### variable verbose

```
const bool verbose = false;
```





-------------------------------

Updated on 2022-09-08 at 01:48:55 +0000