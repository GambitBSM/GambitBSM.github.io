---
title: "struct Gambit::Logging::SortedMessage"
description: "structure for storing log messages and metadata after tags are sorted "

---

# struct Gambit::Logging::SortedMessage



structure for storing log messages and metadata after tags are sorted 


`#include <logging.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[SortedMessage](/documentation/code/classes/structgambit_1_1logging_1_1sortedmessage/)**(const [Message](/documentation/code/classes/structgambit_1_1logging_1_1message/) & mail)<br>Constructor for [SortedMessage](/documentation/code/classes/structgambit_1_1logging_1_1sortedmessage/) struct.  |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| const std::string & | **[message](/documentation/code/classes/structgambit_1_1logging_1_1sortedmessage/)**  |
| const Utils::time_point & | **[received_at](/documentation/code/classes/structgambit_1_1logging_1_1sortedmessage/)**  |
| std::set< LogTag > | **[type_tags](/documentation/code/classes/structgambit_1_1logging_1_1sortedmessage/)**  |
| std::set< int > | **[component_tags](/documentation/code/classes/structgambit_1_1logging_1_1sortedmessage/)**  |
| std::set< LogTag > | **[flag_tags](/documentation/code/classes/structgambit_1_1logging_1_1sortedmessage/)**  |
| std::set< LogTag > | **[echo_tags](/documentation/code/classes/structgambit_1_1logging_1_1sortedmessage/)**  |

## Public Functions Documentation

### function SortedMessage

```
SortedMessage(
    const Message & mail
)
```

Constructor for [SortedMessage](/documentation/code/classes/structgambit_1_1logging_1_1sortedmessage/) struct. 

## Public Attributes Documentation

### variable message

```
const std::string & message;
```


### variable received_at

```
const Utils::time_point & received_at;
```


### variable type_tags

```
std::set< LogTag > type_tags;
```


### variable component_tags

```
std::set< int > component_tags;
```


### variable flag_tags

```
std::set< LogTag > flag_tags;
```


### variable echo_tags

```
std::set< LogTag > echo_tags;
```


-------------------------------

Updated on 2022-09-08 at 01:05:17 +0000