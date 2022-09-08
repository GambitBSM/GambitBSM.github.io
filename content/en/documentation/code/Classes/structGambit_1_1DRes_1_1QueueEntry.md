---
title: "struct Gambit::DRes::QueueEntry"
description: "Information in parameter queue. "

---

# struct Gambit::DRes::QueueEntry



Information in parameter queue. 


`#include <depresolver.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[QueueEntry](/documentation/code/classes/structgambit_1_1dres_1_1queueentry/)**() |
| | **[QueueEntry](/documentation/code/classes/structgambit_1_1dres_1_1queueentry/)**([sspair](/documentation/code/namespaces/namespacegambit/) a, DRes::VertexID b, int c, bool d) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [sspair](/documentation/code/namespaces/namespacegambit/) | **[first](/documentation/code/classes/structgambit_1_1dres_1_1queueentry/)**  |
| DRes::VertexID | **[second](/documentation/code/classes/structgambit_1_1dres_1_1queueentry/)**  |
| int | **[third](/documentation/code/classes/structgambit_1_1dres_1_1queueentry/)**  |
| bool | **[printme](/documentation/code/classes/structgambit_1_1dres_1_1queueentry/)**  |

## Public Functions Documentation

### function QueueEntry

```
inline QueueEntry()
```


### function QueueEntry

```
inline QueueEntry(
    sspair a,
    DRes::VertexID b,
    int c,
    bool d
)
```


## Public Attributes Documentation

### variable first

```
sspair first;
```


### variable second

```
DRes::VertexID second;
```


### variable third

```
int third;
```


### variable printme

```
bool printme;
```


-------------------------------

Updated on 2022-09-08 at 01:05:17 +0000