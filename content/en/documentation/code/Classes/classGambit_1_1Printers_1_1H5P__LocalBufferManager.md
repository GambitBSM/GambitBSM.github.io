---
title: "class Gambit::Printers::H5P_LocalBufferManager"
description: "Keeps track of vertex buffers local to a print function. "

---

# class Gambit::Printers::H5P_LocalBufferManager



Keeps track of vertex buffers local to a print function.  [More...](#detailed-description)


`#include <hdf5printer.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[init](/documentation/code/classes/classgambit_1_1printers_1_1h5p__localbuffermanager/#function-gambitprintersh5p-localbuffermanager-init)**([HDF5Printer](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer/) * p, bool synchronised)<br>Initialise the buffer (attach it to a printer and set its behaviour)  |
| BuffType & | **[get_buffer](/documentation/code/classes/classgambit_1_1printers_1_1h5p__localbuffermanager/#function-gambitprintersh5p-localbuffermanager-get-buffer)**(const int vID, const unsigned int i, const std::string & label)<br>Retrieve a buffer for an IDcode/auxilliary-index pair.  |
| | **[H5P_LocalBufferManager](/documentation/code/classes/classgambit_1_1printers_1_1h5p__localbuffermanager/#function-gambitprintersh5p-localbuffermanager-h5p-localbuffermanager)**()<br>Constructor.  |
| bool | **[ready](/documentation/code/classes/classgambit_1_1printers_1_1h5p__localbuffermanager/#function-gambitprintersh5p-localbuffermanager-ready)**()<br>Signal whether initialisation has occured.  |

## Detailed Description

```
template <class BuffType >
class Gambit::Printers::H5P_LocalBufferManager;
```

Keeps track of vertex buffers local to a print function. 
## Public Functions Documentation

### function init

```
void init(
    HDF5Printer * p,
    bool synchronised
)
```

Initialise the buffer (attach it to a printer and set its behaviour) 

Templated [H5P_LocalBufferManager](/documentation/code/classes/classgambit_1_1printers_1_1h5p__localbuffermanager/) member functions. 


### function get_buffer

```
BuffType & get_buffer(
    const int vID,
    const unsigned int i,
    const std::string & label
)
```

Retrieve a buffer for an IDcode/auxilliary-index pair. 

### function H5P_LocalBufferManager

```
inline H5P_LocalBufferManager()
```

Constructor. 

### function ready

```
inline bool ready()
```

Signal whether initialisation has occured. 

-------------------------------

Updated on 2022-09-08 at 02:00:49 +0000