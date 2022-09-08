---
title: "struct Gambit::Printers::BuffPair"

description: "[No description available]"

---

# struct Gambit::Printers::BuffPair



[No description available] [More...](#detailed-description)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BuffPair](/documentation/code/classes/structgambit_1_1printers_1_1buffpair/#function-gambitprintersbuffpair-buffpair)**([DataSetInterfaceScalar](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacescalar/)< T, CHUNKLENGTH > & d, [DataSetInterfaceScalar](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacescalar/)< int, CHUNKLENGTH > & v) |
| | **[BuffPair](/documentation/code/classes/structgambit_1_1printers_1_1buffpair/#function-gambitprintersbuffpair-buffpair)**(hid_t location_id, const std::string & name) |
| | **[BuffPair](/documentation/code/classes/structgambit_1_1printers_1_1buffpair/#function-gambitprintersbuffpair-buffpair)**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [DataSetInterfaceScalar](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacescalar/)< T, CHUNKLENGTH > | **[data](/documentation/code/classes/structgambit_1_1printers_1_1buffpair/#variable-gambitprintersbuffpair-data)**  |
| [DataSetInterfaceScalar](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacescalar/)< int, CHUNKLENGTH > | **[isvalid](/documentation/code/classes/structgambit_1_1printers_1_1buffpair/#variable-gambitprintersbuffpair-isvalid)**  |

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

Updated on 2022-09-08 at 02:00:49 +0000