---
title: "class Gambit::Printers::HDF5MasterBufferT"
description: "Class to manage a set of buffers for a single output type. "

---

# class Gambit::Printers::HDF5MasterBufferT



Class to manage a set of buffers for a single output type.  [More...](#detailed-description)


`#include <hdf5printer_v2.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[HDF5MasterBufferT](/documentation/code/classes/classgambit_1_1printers_1_1hdf5masterbuffert/#function-hdf5masterbuffert)**(bool sync)<br>Constructor.  |
| [HDF5Buffer](/documentation/code/classes/classgambit_1_1printers_1_1hdf5buffer/)< T > & | **[get_buffer](/documentation/code/classes/classgambit_1_1printers_1_1hdf5masterbuffert/#function-get-buffer)**(const std::string & label, const std::vector< [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/) > & buffered_points)<br>Retrieve buffer of our type for a given label.  |

## Detailed Description

```
template <class T >
class Gambit::Printers::HDF5MasterBufferT;
```

Class to manage a set of buffers for a single output type. 
## Public Functions Documentation

### function HDF5MasterBufferT

```
inline HDF5MasterBufferT(
    bool sync
)
```

Constructor. 

### function get_buffer

```
inline HDF5Buffer< T > & get_buffer(
    const std::string & label,
    const std::vector< PPIDpair > & buffered_points
)
```

Retrieve buffer of our type for a given label. 

-------------------------------

Updated on 2022-09-08 at 03:41:59 +0000