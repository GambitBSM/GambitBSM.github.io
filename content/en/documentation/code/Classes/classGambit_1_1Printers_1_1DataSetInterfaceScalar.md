---
title: "class Gambit::Printers::DataSetInterfaceScalar"

description: "[No description available]"

---

# class Gambit::Printers::DataSetInterfaceScalar



[No description available] [More...](#detailed-description)


`#include <DataSetInterfaceScalar.hpp>`

Inherits from [Gambit::Printers::DataSetInterfaceBase< T, 0, CHUNKLENGTH >](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[DataSetInterfaceScalar](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacescalar/#function-datasetinterfacescalar)**()<br>Constructors.  |
| | **[DataSetInterfaceScalar](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacescalar/#function-datasetinterfacescalar)**(hid_t location_id, const std::string & name, const bool resume, const char access) |
| std::pair< hid_t, hid_t > | **[select_chunk](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacescalar/#function-select-chunk)**(std::size_t offset, std::size_t length) const<br>Select a hyperslab chunk in the hosted dataset.  |
| void | **[writenewchunk](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacescalar/#function-writenewchunk)**(const T(&) chunkdata[CHUNKLENGTH])<br>Write data to a new chunk in the hosted dataset.  |
| void | **[RA_write](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacescalar/#function-ra-write)**(const T(&) values[CHUNKLENGTH], const hsize_t(&) coords[CHUNKLENGTH], std::size_t npoints) |
| void | **[zero](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacescalar/#function-zero)**()<br>Set all elements of the dataset to zero.  |
| std::vector< T > | **[get_chunk](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacescalar/#function-get-chunk)**(std::size_t i, std::size_t length) const<br>READ methods (perhaps can generalise to non-scalar case, but this doesn't exist yet for writing anyway so not bothering yet)  |
| T | **[get_entry](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacescalar/#function-get-entry)**(std::size_t index)<br>Extract a single entry from a linked dataset.  |

## Additional inherited members

**Public Functions inherited from [Gambit::Printers::DataSetInterfaceBase< T, 0, CHUNKLENGTH >](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/)**

|                | Name           |
| -------------- | -------------- |
| | **[DataSetInterfaceBase](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/#function-datasetinterfacebase)**()<br>Constructors.  |
| | **[DataSetInterfaceBase](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/#function-datasetinterfacebase)**(hid_t location_id, const std::string & name, const std::size_t rdims[DSETRANK], const bool resume, const char access) |
| virtual | **[~DataSetInterfaceBase](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/#function-datasetinterfacebase)**()<br>Do cleanup (close dataset)  |
| hid_t | **[createDataSet](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/#function-createdataset)**(hid_t location_id, const std::string & name, const std::size_t rdims[DSETRANK])<br>Create a (chunked) dataset.  |
| hid_t | **[openDataSet](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/#function-opendataset)**(hid_t location_id, const std::string & name, const std::size_t rdims[DSETRANK])<br>Open an existing dataset.  |
| void | **[closeDataSet](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/#function-closedataset)**()<br>Close an open dataset.  |
| void | **[extend_dset](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/#function-extend-dset)**(const unsigned long i)<br>Extend dataset to nearest multiple of CHUNKLENGTH above supplied length.  |
| std::string | **[get_myname](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/#function-get-myname)**() const |
| std::size_t | **[get_dsetrank](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/#function-get-dsetrank)**() const |
| std::size_t | **[get_chunklength](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/#function-get-chunklength)**() const |
| const hsize_t * | **[get_maxdsetdims](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/#function-get-maxdsetdims)**() const |
| const hsize_t * | **[get_chunkdims](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/#function-get-chunkdims)**() const |
| const hsize_t * | **[get_slicedims](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/#function-get-slicedims)**() const |
| unsigned long | **[get_nextemptyslab](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/#function-get-nextemptyslab)**() const |
| unsigned long | **[dset_length](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/#function-dset-length)**() const |
| char | **[access_mode](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/#function-access-mode)**() const |
| void | **[reset_nextemptyslab](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/#function-reset-nextemptyslab)**() |
| hsize_t * | **[dsetdims](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/#function-dsetdims)**() |

**Protected Functions inherited from [Gambit::Printers::DataSetInterfaceBase< T, 0, CHUNKLENGTH >](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/)**

|                | Name           |
| -------------- | -------------- |
| hid_t | **[get_dset_id](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/#function-get-dset-id)**() const |

**Protected Attributes inherited from [Gambit::Printers::DataSetInterfaceBase< T, 0, CHUNKLENGTH >](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/)**

|                | Name           |
| -------------- | -------------- |
| const hid_t | **[hdftype_id](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/#variable-hdftype-id)** <br>[DataSetInterfaceBase](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/) class member definitions.  |
| hid_t | **[dset_id](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/#variable-dset-id)**  |
| unsigned long | **[dsetnextemptyslab](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/#variable-dsetnextemptyslab)**  |
| unsigned long | **[virtualwriteposition](/documentation/code/classes/classgambit_1_1printers_1_1datasetinterfacebase/#variable-virtualwriteposition)**  |


## Detailed Description

```
template <class T ,
std::size_t CHUNKLENGTH>
class Gambit::Printers::DataSetInterfaceScalar;
```


Derived dataset interface, with methods for writing scalar records (i.e. single ints, doubles, etc.) i.e. RANK=0 case 

## Public Functions Documentation

### function DataSetInterfaceScalar

```
DataSetInterfaceScalar()
```

Constructors. 

### function DataSetInterfaceScalar

```
DataSetInterfaceScalar(
    hid_t location_id,
    const std::string & name,
    const bool resume,
    const char access
)
```


### function select_chunk

```
std::pair< hid_t, hid_t > select_chunk(
    std::size_t offset,
    std::size_t length
) const
```

Select a hyperslab chunk in the hosted dataset. 

To facilitate code factorisation, the hyperslab selection is now contained here Only selects whole chunks at the moment. 


### function writenewchunk

```
void writenewchunk(
    const T(&) chunkdata[CHUNKLENGTH]
)
```

Write data to a new chunk in the hosted dataset. 

### function RA_write

```
void RA_write(
    const T(&) values[CHUNKLENGTH],
    const hsize_t(&) coords[CHUNKLENGTH],
    std::size_t npoints
)
```


Perform desynchronised ("random access") dataset writes to previous scan iterations from a queue. 


### function zero

```
void zero()
```

Set all elements of the dataset to zero. 

Easiest way to do this is to simply point the "nextemptyslab" index back to the beginning of the dataset, and then rewrite all the chunks with zero values.

Figure out how many chunks to overwrite

Point hyperslab selector back to beginning of dataset (might already point there if this is a random-access dataset, which actually it should be since we shouldn't be resetting the sync datasets. Well anyway it should be ok, just means we cannot use it to compute how many chunks there are)


### function get_chunk

```
std::vector< T > get_chunk(
    std::size_t i,
    std::size_t length
) const
```

READ methods (perhaps can generalise to non-scalar case, but this doesn't exist yet for writing anyway so not bothering yet) 

{@ READ methods

Extract a data slice from the linked dataset 


### function get_entry

```
T get_entry(
    std::size_t index
)
```

Extract a single entry from a linked dataset. 

-------------------------------

Updated on 2024-07-18 at 13:53:32 +0000