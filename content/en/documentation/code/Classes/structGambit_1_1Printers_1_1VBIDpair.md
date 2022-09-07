---
title: 'struct Gambit::Printers::VBIDpair'

description: "[No description available]"

---

# Gambit::Printers::VBIDpair





[No description available] [More...](#detailed-description)


`#include <new_mpi_datatypes.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[VBIDpair](/documentation/code/classes/structgambit_1_1printers_1_1vbidpair/#function-vbidpair)**() =default |
| | **[VBIDpair](/documentation/code/classes/structgambit_1_1printers_1_1vbidpair/#function-vbidpair)**(const int v, const int i) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| int | **[vertexID](/documentation/code/classes/structgambit_1_1printers_1_1vbidpair/#variable-vertexid)**  |
| int | **[index](/documentation/code/classes/structgambit_1_1printers_1_1vbidpair/#variable-index)**  |

## Detailed Description

```
struct Gambit::Printers::VBIDpair;
```


vertexID / sub-print index pair Identifies individual buffers (I call them VertexBuffer, but actually there can be more than one per vertex) 

## Public Functions Documentation

### function VBIDpair

```
VBIDpair() =default
```


### function VBIDpair

```
inline VBIDpair(
    const int v,
    const int i
)
```


## Public Attributes Documentation

### variable vertexID

```
int vertexID;
```


### variable index

```
int index;
```


-------------------------------

Updated on 2022-09-07 at 13:49:51 +0000