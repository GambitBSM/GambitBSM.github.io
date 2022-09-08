---
title: "struct Gambit::Printers::PPIDpair"

description: "[No description available]"

---

# struct Gambit::Printers::PPIDpair



[No description available] [More...](#detailed-description)


`#include <new_mpi_datatypes.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/#function-ppidpair)**() |
| | **[PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/#function-ppidpair)**(const unsigned long long int p, const int r) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| unsigned long long int | **[pointID](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/#variable-pointid)**  |
| unsigned int | **[rank](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/#variable-rank)**  |
| unsigned int | **[valid](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/#variable-valid)**  |

## Friends

|                | Name           |
| -------------- | -------------- |
| std::ostream & | **[operator<<](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/#friend-operator)**(std::ostream & stream, const [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/) & ppid) <br>Stream operator overloads.  |

## Detailed Description

```
struct Gambit::Printers::PPIDpair;
```


pointID / process number pair Used to identify a single parameter space point 

## Public Functions Documentation

### function PPIDpair

```
inline PPIDpair()
```


### function PPIDpair

```
inline PPIDpair(
    const unsigned long long int p,
    const int r
)
```


## Public Attributes Documentation

### variable pointID

```
unsigned long long int pointID;
```


### variable rank

```
unsigned int rank;
```


### variable valid

```
unsigned int valid;
```


## Friends

### friend operator<<

```
friend std::ostream & operator<<(
    std::ostream & stream,

    const PPIDpair & ppid
);
```

Stream operator overloads. 

-------------------------------

Updated on 2022-09-08 at 02:27:27 +0000