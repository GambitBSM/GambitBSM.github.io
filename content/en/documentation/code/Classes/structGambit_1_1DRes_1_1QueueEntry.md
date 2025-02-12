---
title: "struct Gambit::DRes::QueueEntry"
description: "Information in resolution queue. "

---

# struct Gambit::DRes::QueueEntry



Information in resolution queue. 


`#include <depresolver.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[QueueEntry](/documentation/code/classes/structgambit_1_1dres_1_1queueentry/#function-queueentry)**()<br>Default constructor for [QueueEntry](/documentation/code/classes/structgambit_1_1dres_1_1queueentry/).  |
| | **[QueueEntry](/documentation/code/classes/structgambit_1_1dres_1_1queueentry/#function-queueentry)**([sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) a, VertexID b, int c, bool d)<br>Alternative constructor for [QueueEntry](/documentation/code/classes/structgambit_1_1dres_1_1queueentry/).  |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) | **[quantity](/documentation/code/classes/structgambit_1_1dres_1_1queueentry/#variable-quantity)**  |
| VertexID | **[toVertex](/documentation/code/classes/structgambit_1_1dres_1_1queueentry/#variable-tovertex)**  |
| int | **[dependency_type](/documentation/code/classes/structgambit_1_1dres_1_1queueentry/#variable-dependency-type)**  |
| bool | **[printme](/documentation/code/classes/structgambit_1_1dres_1_1queueentry/#variable-printme)**  |
| const [Observable](/documentation/code/classes/structgambit_1_1dres_1_1observable/) * | **[obslike](/documentation/code/classes/structgambit_1_1dres_1_1queueentry/#variable-obslike)**  |

## Public Functions Documentation

### function QueueEntry

```
QueueEntry()
```

Default constructor for [QueueEntry](/documentation/code/classes/structgambit_1_1dres_1_1queueentry/). 

### function QueueEntry

```
QueueEntry(
    sspair a,
    VertexID b,
    int c,
    bool d
)
```

Alternative constructor for [QueueEntry](/documentation/code/classes/structgambit_1_1dres_1_1queueentry/). 

## Public Attributes Documentation

### variable quantity

```
sspair quantity;
```


### variable toVertex

```
VertexID toVertex;
```


### variable dependency_type

```
int dependency_type;
```


### variable printme

```
bool printme;
```


### variable obslike

```
const Observable * obslike;
```


-------------------------------

Updated on 2025-02-12 at 16:10:32 +0000