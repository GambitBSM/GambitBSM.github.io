---
title: "struct Gambit::Printers::DSetData"

description: "[No description available]"

---

# struct Gambit::Printers::DSetData



[No description available]

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[DSetData](/documentation/code/classes/structgambit_1_1printers_1_1dsetdata/#function-dsetdata)**(int r) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| int | **[rank](/documentation/code/classes/structgambit_1_1printers_1_1dsetdata/#variable-rank)**  |
| std::vector< std::string > | **[names](/documentation/code/classes/structgambit_1_1printers_1_1dsetdata/#variable-names)**  |
| std::vector< unsigned long > | **[lengths](/documentation/code/classes/structgambit_1_1printers_1_1dsetdata/#variable-lengths)**  |
| std::string | **[local_info](/documentation/code/classes/structgambit_1_1printers_1_1dsetdata/#variable-local-info)** <br>Need to analyse this in a more "streaming" way, otherwise too big and slow.  |
| std::string | **[errmsg](/documentation/code/classes/structgambit_1_1printers_1_1dsetdata/#variable-errmsg)**  |

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

Updated on 2024-07-18 at 13:53:32 +0000