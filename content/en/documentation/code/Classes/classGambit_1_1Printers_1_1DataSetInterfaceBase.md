---
title: "class Gambit::Printers::DataSetInterfaceBase"
description: "Wrapper object to manage a single dataset. "

---

# class Gambit::Printers::DataSetInterfaceBase



Wrapper object to manage a single dataset.  [More...](#detailed-description)


`#include <DataSetInterfaceBase.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[DataSetInterfaceBase](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/)**()<br>Constructors.  |
| | **[DataSetInterfaceBase](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/)**(hid_t location_id, const std::string & name, const std::size_t rdims[DSETRANK], const bool resume, const char access) |
| virtual | **[~DataSetInterfaceBase](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/)**()<br>Do cleanup (close dataset)  |
| hid_t | **[createDataSet](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/)**(hid_t location_id, const std::string & name, const std::size_t rdims[DSETRANK])<br>Create a (chunked) dataset.  |
| hid_t | **[openDataSet](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/)**(hid_t location_id, const std::string & name, const std::size_t rdims[DSETRANK])<br>Open an existing dataset.  |
| void | **[closeDataSet](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/)**()<br>Close an open dataset.  |
| void | **[extend_dset](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/)**(const unsigned long i)<br>Extend dataset to nearest multiple of CHUNKLENGTH above supplied length.  |
| std::string | **[get_myname](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/)**() const |
| std::size_t | **[get_dsetrank](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/)**() const |
| std::size_t | **[get_chunklength](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/)**() const |
| const hsize_t * | **[get_maxdsetdims](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/)**() const |
| const hsize_t * | **[get_chunkdims](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/)**() const |
| const hsize_t * | **[get_slicedims](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/)**() const |
| unsigned long | **[get_nextemptyslab](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/)**() const |
| unsigned long | **[dset_length](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/)**() const |
| char | **[access_mode](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/)**() const |
| void | **[reset_nextemptyslab](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/)**() |
| hsize_t * | **[dsetdims](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/)**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| hid_t | **[get_dset_id](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/)**() const |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| const hid_t | **[hdftype_id](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/)** <br>[DataSetInterfaceBase](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/) class member definitions.  |
| hid_t | **[dset_id](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/)**  |
| unsigned long | **[dsetnextemptyslab](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/)**  |
| unsigned long | **[virtualwriteposition](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/)**  |

## Detailed Description

```
template <class T ,
std::size_t RECORDRANK,
std::size_t CHUNKLENGTH>
class Gambit::Printers::DataSetInterfaceBase;
```

Wrapper object to manage a single dataset. 
## Public Functions Documentation

### function DataSetInterfaceBase

```
DataSetInterfaceBase()
```

Constructors. 

### function DataSetInterfaceBase

```
DataSetInterfaceBase(
    hid_t location_id,
    const std::string & name,
    const std::size_t rdims[DSETRANK],
    const bool resume,
    const char access
)
```


### function ~DataSetInterfaceBase

```
virtual ~DataSetInterfaceBase()
```

Do cleanup (close dataset) 

### function createDataSet

```
hid_t createDataSet(
    hid_t location_id,
    const std::string & name,
    const std::size_t rdims[DSETRANK]
)
```

Create a (chunked) dataset. 

### function openDataSet

```
hid_t openDataSet(
    hid_t location_id,
    const std::string & name,
    const std::size_t rdims[DSETRANK]
)
```

Open an existing dataset. 

Open an existing dataset It is assumed that we are resuming a run and therefore know what format this dataset should have 


### function closeDataSet

```
void closeDataSet()
```

Close an open dataset. 

Release resources associated with the underlying dataset. 


### function extend_dset

```
void extend_dset(
    const unsigned long i
)
```

Extend dataset to nearest multiple of CHUNKLENGTH above supplied length. 

### function get_myname

```
inline std::string get_myname() const
```


### function get_dsetrank

```
inline std::size_t get_dsetrank() const
```


### function get_chunklength

```
inline std::size_t get_chunklength() const
```


### function get_maxdsetdims

```
inline const hsize_t * get_maxdsetdims() const
```


### function get_chunkdims

```
inline const hsize_t * get_chunkdims() const
```


### function get_slicedims

```
inline const hsize_t * get_slicedims() const
```


### function get_nextemptyslab

```
inline unsigned long get_nextemptyslab() const
```


### function dset_length

```
inline unsigned long dset_length() const
```


### function access_mode

```
inline char access_mode() const
```


### function reset_nextemptyslab

```
inline void reset_nextemptyslab()
```


### function dsetdims

```
inline hsize_t * dsetdims()
```


## Protected Functions Documentation

### function get_dset_id

```
inline hid_t get_dset_id() const
```


## Protected Attributes Documentation

### variable hdftype_id

```
static const hid_t hdftype_id = get_hdf5_data_type<T>::type();
```

[DataSetInterfaceBase](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/) class member definitions. 

### variable dset_id

```
hid_t dset_id;
```


### variable dsetnextemptyslab

```
unsigned long dsetnextemptyslab;
```


### variable virtualwriteposition

```
unsigned long virtualwriteposition;
```


-------------------------------

Updated on 2022-09-08 at 01:05:18 +0000