---
title: "struct Gambit::Printers::HDF5bufferchunk"

description: "[No description available]"

---

# struct Gambit::Printers::HDF5bufferchunk



[No description available]

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| const std::size_t | **[SIZE](/documentation/code/classes/structgambit_1_1printers_1_1hdf5bufferchunk/)**  |
| const std::size_t | **[NBUFFERS](/documentation/code/classes/structgambit_1_1printers_1_1hdf5bufferchunk/)**  |
| std::size_t | **[used_size](/documentation/code/classes/structgambit_1_1printers_1_1hdf5bufferchunk/)**  |
| std::size_t | **[used_nbuffers](/documentation/code/classes/structgambit_1_1printers_1_1hdf5bufferchunk/)**  |
| int[NBUFFERS] | **[name_id](/documentation/code/classes/structgambit_1_1printers_1_1hdf5bufferchunk/)**  |
| unsigned long long[SIZE] | **[pointIDs](/documentation/code/classes/structgambit_1_1printers_1_1hdf5bufferchunk/)**  |
| unsigned int[SIZE] | **[ranks](/documentation/code/classes/structgambit_1_1printers_1_1hdf5bufferchunk/)**  |
| double[NBUFFERS][SIZE] | **[values](/documentation/code/classes/structgambit_1_1printers_1_1hdf5bufferchunk/)**  |
| long long[NBUFFERS][SIZE] | **[values_int](/documentation/code/classes/structgambit_1_1printers_1_1hdf5bufferchunk/)**  |
| int[NBUFFERS][SIZE] | **[valid](/documentation/code/classes/structgambit_1_1printers_1_1hdf5bufferchunk/)**  |

## Public Attributes Documentation

### variable SIZE

```
static const std::size_t SIZE =10;
```


### variable NBUFFERS

```
static const std::size_t NBUFFERS =10;
```


### variable used_size

```
std::size_t used_size;
```


### variable used_nbuffers

```
std::size_t used_nbuffers;
```


### variable name_id

```
int[NBUFFERS] name_id;
```


### variable pointIDs

```
unsigned long long[SIZE] pointIDs;
```


### variable ranks

```
unsigned int[SIZE] ranks;
```


### variable values

```
double[NBUFFERS][SIZE] values;
```


### variable values_int

```
long long[NBUFFERS][SIZE] values_int;
```


### variable valid

```
int[NBUFFERS][SIZE] valid;
```


-------------------------------

Updated on 2022-09-08 at 01:05:18 +0000