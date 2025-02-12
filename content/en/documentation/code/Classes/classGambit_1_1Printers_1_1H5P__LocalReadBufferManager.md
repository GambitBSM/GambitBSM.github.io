---
title: "class Gambit::Printers::H5P_LocalReadBufferManager"

description: "[No description available]"

---

# class Gambit::Printers::H5P_LocalReadBufferManager



[No description available] [More...](#detailed-description)


`#include <hdf5reader.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[H5P_LocalReadBufferManager](/documentation/code/classes/classgambit_1_1printers_1_1h5p__localreadbuffermanager/#function-h5p-localreadbuffermanager)**()<br>Constructor.  |
| | **[~H5P_LocalReadBufferManager](/documentation/code/classes/classgambit_1_1printers_1_1h5p__localreadbuffermanager/#function-h5p-localreadbuffermanager)**()<br>Destructor. Close all datasets.  |
| [BuffPair](/documentation/code/classes/structgambit_1_1printers_1_1buffpair/)< T > & | **[get_buffer](/documentation/code/classes/classgambit_1_1printers_1_1h5p__localreadbuffermanager/#function-get-buffer)**(const int vID, const unsigned int i, const std::string & label, hid_t location_id)<br>Buffer retrieve function.  |

## Detailed Description

```
template <class T >
class Gambit::Printers::H5P_LocalReadBufferManager;
```


Keeps track of vertex buffers local to a retrieve function Similar to the buffer manager for [HDF5Printer](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer/). I considered trying to re-use that, but it is too integrated with the printer. 

## Public Functions Documentation

### function H5P_LocalReadBufferManager

```
inline H5P_LocalReadBufferManager()
```

Constructor. 

### function ~H5P_LocalReadBufferManager

```
inline ~H5P_LocalReadBufferManager()
```

Destructor. Close all datasets. 

### function get_buffer

```
BuffPair< T > & get_buffer(
    const int vID,
    const unsigned int i,
    const std::string & label,
    hid_t location_id
)
```

Buffer retrieve function. 

Retrieve a buffer for an IDcode/auxilliary-index pair location_id used to access dataset if it has not yet been opened. 


-------------------------------

Updated on 2025-02-12 at 16:10:32 +0000