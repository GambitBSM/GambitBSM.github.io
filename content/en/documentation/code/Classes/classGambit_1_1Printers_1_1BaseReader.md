---
title: "class Gambit::Printers::BaseReader"
description: "BASE READER CLASS. "

---

# class Gambit::Printers::BaseReader



BASE READER CLASS. 


`#include <baseprinter.hpp>`

Inherits from [Gambit::Printers::BaseBaseReader](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/)

Inherited by [Gambit::Printers::HDF5Reader](/documentation/code/classes/classgambit_1_1printers_1_1hdf5reader/), [Gambit::Printers::SQLiteReader](/documentation/code/classes/classgambit_1_1printers_1_1sqlitereader/), [Gambit::Printers::asciiReader](/documentation/code/classes/classgambit_1_1printers_1_1asciireader/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BaseReader](/documentation/code/classes/classgambit_1_1printers_1_1basereader/)**() |
| virtual | **[~BaseReader](/documentation/code/classes/classgambit_1_1printers_1_1basereader/)**()<br>Destructor.  |
| template <typename T \> <br>bool | **[retrieve](/documentation/code/classes/classgambit_1_1printers_1_1basereader/)**(T & out, const std::string & label)<br>Reimplement overload for 'retrieve' that uses the current point as the input for rank/pointID.  |
| template <typename T \> <br>bool | **[retrieve](/documentation/code/classes/classgambit_1_1printers_1_1basereader/)**(T & out, const std::string & label, const uint rank, const ulong pointID) |
| virtual bool | **[retrieve_and_print](/documentation/code/classes/classgambit_1_1printers_1_1basereader/)**(const std::string & in_label, const std::string & out_label, [BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/) & printer, const uint rank, const ulong pointID)<br>Retrieve and directly print data to new output.  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| template <typename T \> <br>bool | **[_retrieve](/documentation/code/classes/classgambit_1_1printers_1_1basereader/)**(T & , const std::string & label, const uint, const ulong) |

## Additional inherited members

**Public Functions inherited from [Gambit::Printers::BaseBaseReader](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/)**

|                | Name           |
| -------------- | -------------- |
| virtual | **[~BaseBaseReader](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/)**() |
| virtual void | **[reset](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/)**() =0 |
| virtual ulong | **[get_dataset_length](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/)**() =0 |
| virtual [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/) | **[get_current_point](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/)**() =0 |
| virtual ulong | **[get_current_index](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/)**() =0 |
| virtual [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/) | **[get_next_point](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/)**() =0 |
| virtual bool | **[eoi](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/)**() =0 |
| virtual std::size_t | **[get_type](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/)**(const std::string & label) =0 |
| virtual std::set< std::string > | **[get_all_labels](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/)**() =0 |


## Public Functions Documentation

### function BaseReader

```
inline BaseReader()
```


### function ~BaseReader

```
inline virtual ~BaseReader()
```

Destructor. 

### function retrieve

```
template <typename T >
inline bool retrieve(
    T & out,
    const std::string & label
)
```

Reimplement overload for 'retrieve' that uses the current point as the input for rank/pointID. 

### function retrieve

```
template <typename T >
inline bool retrieve(
    T & out,
    const std::string & label,
    const uint rank,
    const ulong pointID
)
```


### function retrieve_and_print

```
virtual bool retrieve_and_print(
    const std::string & in_label,
    const std::string & out_label,
    BaseBasePrinter & printer,
    const uint rank,
    const ulong pointID
)
```

Retrieve and directly print data to new output. 

**Reimplements**: [Gambit::Printers::BaseBaseReader::retrieve_and_print](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/)


First need to get the type data for 'in_label', then call appropriate retrieve and print functions. I think there is no choice but to do this with a big switch. Also need to check if the type matches what the printer expects, and decide what to do in case of mismatch.


## Protected Functions Documentation

### function _retrieve

```
template <typename T >
inline bool _retrieve(
    T & ,
    const std::string & label,
    const uint,
    const ulong
)
```


Default _retrieve function. Throws an error if no virtual function matching the type of the attempted retrieval is found. 


-------------------------------

Updated on 2022-09-08 at 01:05:18 +0000