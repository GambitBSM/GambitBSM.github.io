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
| | **[BuffTags](/documentation/code/classes/structgambit_1_1printers_1_1bufftags/#function-gambitprintersbufftags-bufftags)**() |
| | **[BuffTags](/documentation/code/classes/structgambit_1_1printers_1_1bufftags/#function-gambitprintersbufftags-bufftags)**(const int first_tag) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| int | **[SYNC_data](/documentation/code/classes/structgambit_1_1printers_1_1bufftags/#variable-gambitprintersbufftags-sync-data)**  |
| int | **[SYNC_valid](/documentation/code/classes/structgambit_1_1printers_1_1bufftags/#variable-gambitprintersbufftags-sync-valid)**  |
| int | **[RA_queue](/documentation/code/classes/structgambit_1_1printers_1_1bufftags/#variable-gambitprintersbufftags-ra-queue)**  |
| int | **[RA_loc](/documentation/code/classes/structgambit_1_1printers_1_1bufftags/#variable-gambitprintersbufftags-ra-loc)**  |
| int | **[RA_length](/documentation/code/classes/structgambit_1_1printers_1_1bufftags/#variable-gambitprintersbufftags-ra-length)**  |
| bool | **[valid](/documentation/code/classes/structgambit_1_1printers_1_1bufftags/#variable-gambitprintersbufftags-valid)**  |
| const std::size_t | **[NTAGS](/documentation/code/classes/structgambit_1_1printers_1_1bufftags/#variable-gambitprintersbufftags-ntags)**  |

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

Updated on 2022-09-08 at 01:48:56 +0000