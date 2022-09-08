---
title: "struct Gambit::Printers::DSetData"

description: "[No description available]"

---

# struct Gambit::Printers::DSetData



[No description available]

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[DSetData](/documentation/code/classes/structgambit_1_1printers_1_1dsetdata/)**(int r) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| int | **[rank](/documentation/code/classes/structgambit_1_1printers_1_1dsetdata/)**  |
| std::vector< std::string > | **[names](/documentation/code/classes/structgambit_1_1printers_1_1dsetdata/)**  |
| std::vector< unsigned long > | **[lengths](/documentation/code/classes/structgambit_1_1printers_1_1dsetdata/)**  |
| std::string | **[local_info](/documentation/code/classes/structgambit_1_1printers_1_1dsetdata/)** <br>Need to analyse this in a more "streaming" way, otherwise too big and slow.  |
| std::string | **[errmsg](/documentation/code/classes/structgambit_1_1printers_1_1dsetdata/)**  |

## Public Functions Documentation

### function DSetData

```
inline DSetData(
    int r
)
```


## Public Attributes Documentation

### variable rank

```
int rank;
```


### variable names

```
std::vector< std::string > names;
```


### variable lengths

```
std::vector< unsigned long > lengths;
```


### variable local_info

```
std::string local_info;
```

Need to analyse this in a more "streaming" way, otherwise too big and slow. 

### variable errmsg

```
std::string errmsg;
```


-------------------------------

Updated on 2022-09-08 at 01:05:18 +0000