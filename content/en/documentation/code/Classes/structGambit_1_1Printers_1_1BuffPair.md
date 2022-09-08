---
title: "struct Gambit::Printers::BuffPair"

description: "[No description available]"

---

# struct Gambit::Printers::BuffPair



[No description available] [More...](#detailed-description)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BuffPair](/documentation/code/classes/structgambit_1_1printers_1_1buffpair/)**([DataSetInterfaceScalar](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacescalar/)< T, CHUNKLENGTH > & d, [DataSetInterfaceScalar](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacescalar/)< int, CHUNKLENGTH > & v) |
| | **[BuffPair](/documentation/code/classes/structgambit_1_1printers_1_1buffpair/)**(hid_t location_id, const std::string & name) |
| | **[BuffPair](/documentation/code/classes/structgambit_1_1printers_1_1buffpair/)**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [DataSetInterfaceScalar](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacescalar/)< T, CHUNKLENGTH > | **[data](/documentation/code/classes/structgambit_1_1printers_1_1buffpair/)**  |
| [DataSetInterfaceScalar](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacescalar/)< int, CHUNKLENGTH > | **[isvalid](/documentation/code/classes/structgambit_1_1printers_1_1buffpair/)**  |

## Detailed Description

```
template <class T >
struct Gambit::Printers::BuffPair;
```

## Public Functions Documentation

### function BuffPair

```
inline BuffPair(
    DataSetInterfaceScalar< T, CHUNKLENGTH > & d,
    DataSetInterfaceScalar< int, CHUNKLENGTH > & v
)
```


### function BuffPair

```
inline BuffPair(
    hid_t location_id,
    const std::string & name
)
```


### function BuffPair

```
inline BuffPair()
```


## Public Attributes Documentation

### variable data

```
DataSetInterfaceScalar< T, CHUNKLENGTH > data;
```


### variable isvalid

```
DataSetInterfaceScalar< int, CHUNKLENGTH > isvalid;
```


-------------------------------

Updated on 2022-09-08 at 01:05:18 +0000