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
| | **[SortedMessage](/documentation/code/classes/structgambit_1_1logging_1_1sortedmessage/#function-sortedmessage)**(const [Message](/documentation/code/classes/structgambit_1_1logging_1_1message/) & mail)<br>Constructor for [SortedMessage](/documentation/code/classes/structgambit_1_1logging_1_1sortedmessage/) struct.  |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| const std::string & | **[message](/documentation/code/classes/structgambit_1_1logging_1_1sortedmessage/#variable-message)**  |
| const Utils::time_point & | **[received_at](/documentation/code/classes/structgambit_1_1logging_1_1sortedmessage/#variable-received-at)**  |
| std::set< LogTag > | **[type_tags](/documentation/code/classes/structgambit_1_1logging_1_1sortedmessage/#variable-type-tags)**  |
| std::set< int > | **[component_tags](/documentation/code/classes/structgambit_1_1logging_1_1sortedmessage/#variable-component-tags)**  |
| std::set< LogTag > | **[flag_tags](/documentation/code/classes/structgambit_1_1logging_1_1sortedmessage/#variable-flag-tags)**  |
| std::set< LogTag > | **[echo_tags](/documentation/code/classes/structgambit_1_1logging_1_1sortedmessage/#variable-echo-tags)**  |

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

Updated on 2024-05-31 at 15:12:04 +0000