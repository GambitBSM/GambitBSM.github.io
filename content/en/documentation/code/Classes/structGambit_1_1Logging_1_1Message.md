---
title: "struct Gambit::Logging::Message"
description: "structure for storing log messages and metadata "

---

# struct Gambit::Logging::Message



structure for storing log messages and metadata 


`#include <logging.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Message](/documentation/code/classes/structgambit_1_1logging_1_1message/#function-message)**(const std::string & msgIN, const std::set< int > & tagsIN)<br>Constructor.  |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| std::string | **[message](/documentation/code/classes/structgambit_1_1logging_1_1message/#variable-message)**  |
| std::set< int > | **[tags](/documentation/code/classes/structgambit_1_1logging_1_1message/#variable-tags)**  |
| Utils::time_point | **[received_at](/documentation/code/classes/structgambit_1_1logging_1_1message/#variable-received-at)**  |

## Public Functions Documentation

### function Message

```
inline Message(
    const std::string & msgIN,
    const std::set< int > & tagsIN
)
```

Constructor. 

## Public Attributes Documentation

### variable message

```
std::string message;
```


### variable tags

```
std::set< int > tags;
```


### variable received_at

```
Utils::time_point received_at;
```


-------------------------------

Updated on 2022-09-08 at 02:27:27 +0000