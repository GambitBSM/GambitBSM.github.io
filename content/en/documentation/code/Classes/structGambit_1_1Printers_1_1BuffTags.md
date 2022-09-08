---
title: "struct Gambit::Printers::BuffTags"
description: "Struct for a collection of MPI tags belonging to a single buffer. "

---

# struct Gambit::Printers::BuffTags



Struct for a collection of MPI tags belonging to a single buffer. 


`#include <VertexBufferNumeric1D.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BuffTags](/documentation/code/classes/structgambit_1_1printers_1_1bufftags/#function-bufftags)**() |
| | **[BuffTags](/documentation/code/classes/structgambit_1_1printers_1_1bufftags/#function-bufftags)**(const int first_tag) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| int | **[SYNC_data](/documentation/code/classes/structgambit_1_1printers_1_1bufftags/#variable-sync-data)**  |
| int | **[SYNC_valid](/documentation/code/classes/structgambit_1_1printers_1_1bufftags/#variable-sync-valid)**  |
| int | **[RA_queue](/documentation/code/classes/structgambit_1_1printers_1_1bufftags/#variable-ra-queue)**  |
| int | **[RA_loc](/documentation/code/classes/structgambit_1_1printers_1_1bufftags/#variable-ra-loc)**  |
| int | **[RA_length](/documentation/code/classes/structgambit_1_1printers_1_1bufftags/#variable-ra-length)**  |
| bool | **[valid](/documentation/code/classes/structgambit_1_1printers_1_1bufftags/#variable-valid)**  |
| const std::size_t | **[NTAGS](/documentation/code/classes/structgambit_1_1printers_1_1bufftags/#variable-ntags)**  |

## Public Functions Documentation

### function BuffTags

```
inline BuffTags()
```


### function BuffTags

```
inline BuffTags(
    const int first_tag
)
```


## Public Attributes Documentation

### variable SYNC_data

```
int SYNC_data;
```


### variable SYNC_valid

```
int SYNC_valid;
```


### variable RA_queue

```
int RA_queue;
```


### variable RA_loc

```
int RA_loc;
```


### variable RA_length

```
int RA_length;
```


### variable valid

```
bool valid;
```


### variable NTAGS

```
static const std::size_t NTAGS =5;
```


-------------------------------

Updated on 2022-09-08 at 03:17:34 +0000