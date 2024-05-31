---
title: "class Gambit::Printers::HDF5DataSet"
description: "Class for interfacing to a HDF5 dataset of fixed type. "

---

# class Gambit::Printers::HDF5DataSet



Class for interfacing to a HDF5 dataset of fixed type.  [More...](#detailed-description)


`#include <hdf5printer_v2.hpp>`

Inherits from [Gambit::Printers::HDF5DataSetBase](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[HDF5DataSet](/documentation/code/classes/classgambit_1_1printers_1_1hdf5dataset/#function-hdf5dataset)**(const std::string & name)<br>Constructor.  |
| std::size_t | **[write_single](/documentation/code/classes/classgambit_1_1printers_1_1hdf5dataset/#function-write-single)**(const hid_t loc_id, const T & data, const std::size_t target_pos, const bool force =false)<br>Write a single piece of data to disk at the target position.  |
| std::size_t | **[write_vector](/documentation/code/classes/classgambit_1_1printers_1_1hdf5dataset/#function-write-vector)**(const hid_t loc_id, const std::vector< T > & data, const std::size_t target_pos, const bool force =false)<br>Write a vector of data to disk at the target position.  |
| void | **[write_buffer](/documentation/code/classes/classgambit_1_1printers_1_1hdf5dataset/#function-write-buffer)**(const T(&) buffer[MAX_BUFFER_SIZE], const std::size_t length, const std::size_t target_pos, const bool force =false) |
| void | **[write_random](/documentation/code/classes/classgambit_1_1printers_1_1hdf5dataset/#function-write-random)**(const hid_t loc_id, const std::map< std::size_t, T > & data)<br>Write data to disk at specified positions.  |
| void | **[write_RA_buffer](/documentation/code/classes/classgambit_1_1printers_1_1hdf5dataset/#function-write-ra-buffer)**(const T(&) buffer[MAX_BUFFER_SIZE], const hsize_t(&) coords[MAX_BUFFER_SIZE], std::size_t npoints)<br>Write a buffer of data to disk at the specified positions (must be within current dataset extents)  |
| std::vector< T > | **[get_chunk](/documentation/code/classes/classgambit_1_1printers_1_1hdf5dataset/#function-get-chunk)**(std::size_t offset, std::size_t length) const<br>Extract a data slice from the linked dataset.  |
| void | **[reset](/documentation/code/classes/classgambit_1_1printers_1_1hdf5dataset/#function-reset)**(hid_t loc_id) |
| virtual void | **[create_dataset](/documentation/code/classes/classgambit_1_1printers_1_1hdf5dataset/#function-create-dataset)**(hid_t location_id)<br>Create a new dataset at the specified location.  |

## Additional inherited members

**Public Functions inherited from [Gambit::Printers::HDF5DataSetBase](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/)**

|                | Name           |
| -------------- | -------------- |
| | **[HDF5DataSetBase](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#function-hdf5datasetbase)**(const std::string & name, const hid_t hdftype_id)<br>[HDF5DataSetBase](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/) member functions.  |
| | **[HDF5DataSetBase](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#function-hdf5datasetbase)**(const std::string & name)<br>Version where type is not provided; set to default of -1.  |
| virtual | **[~HDF5DataSetBase](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#function-hdf5datasetbase)**()<br>Destructor.  |
| void | **[open_dataset](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#function-open-dataset)**(hid_t location_id)<br>Open dataset on disk and obtain HDF5 handles.  |
| void | **[close_dataset](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#function-close-dataset)**()<br>Close dataset on disk and release handles.  |
| std::size_t | **[get_dset_length](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#function-get-dset-length)**() const<br>Retrieve the current size of the dataset on disk.  |
| bool | **[dataset_exists](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#function-dataset-exists)**(const hid_t loc_id)<br>Check if our dataset exists on disk with the required name at the given location.  |
| void | **[ensure_dataset_exists](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#function-ensure-dataset-exists)**(const hid_t loc_id, const std::size_t length)<br>Ensure that a correctly named dataset exists at the target location with the specified length.  |
| void | **[extend_dset_to](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#function-extend-dset-to)**(const std::size_t new_size)<br>Extend dataset to the specified size, filling it with default values.  |
| std::string | **[myname](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#function-myname)**() const<br>Retrieve name of the dataset we are supposed to access.  |
| int | **[get_type_id](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#function-get-type-id)**() const<br>Retrieve the integer type ID for this dataset.  |
| hid_t | **[get_hdftype_id](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#function-get-hdftype-id)**() const<br>Retrieve the HDF5 type ID for this dataset.  |
| bool | **[get_exists_on_disk](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#function-get-exists-on-disk)**() const<br>Variable tracking whether the dataset is known to exist in the output file yet.  |
| void | **[set_exists_on_disk](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#function-set-exists-on-disk)**() |

**Protected Functions inherited from [Gambit::Printers::HDF5DataSetBase](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/)**

|                | Name           |
| -------------- | -------------- |
| void | **[ensure_dataset_is_open](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#function-ensure-dataset-is-open)**() const<br>Enforce that the dataset must be open for whatever follows (or else an error is thrown)  |
| hid_t | **[get_dset_id](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#function-get-dset-id)**() const<br>Retrieve the dataset ID for the currently open dataset.  |
| void | **[extend_dset_by](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#function-extend-dset-by)**(const std::size_t extend_by)<br>Set the variable that tracks the (virtual) dataset size on disk.  |
| std::pair< hid_t, hid_t > | **[select_hyperslab](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#function-select-hyperslab)**(std::size_t offset, std::size_t length) const<br>Obtain memory and dataspace identifiers for writing to a hyperslab in the dataset.  |

**Protected Attributes inherited from [Gambit::Printers::HDF5DataSetBase](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/)**

|                | Name           |
| -------------- | -------------- |
| hid_t | **[dset_id](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#variable-dset-id)** <br>HDF5 dataset identifer.  |
| hid_t | **[hdftype_id](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#variable-hdftype-id)** <br>HDF5 type ID for this dataset.  |
| int | **[type_id](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#variable-type-id)** <br>Integer identifier for the template type of this dataset (determined by derived type)  |


## Detailed Description

```
template <class T >
class Gambit::Printers::HDF5DataSet;
```

Class for interfacing to a HDF5 dataset of fixed type. 
## Public Functions Documentation

### function HDF5DataSet

```
inline HDF5DataSet(
    const std::string & name
)
```

Constructor. 

### function write_single

```
inline std::size_t write_single(
    const hid_t loc_id,
    const T & data,
    const std::size_t target_pos,
    const bool force =false
)
```

Write a single piece of data to disk at the target position. 

### function write_vector

```
inline std::size_t write_vector(
    const hid_t loc_id,
    const std::vector< T > & data,
    const std::size_t target_pos,
    const bool force =false
)
```

Write a vector of data to disk at the target position. 

### function write_buffer

```
inline void write_buffer(
    const T(&) buffer[MAX_BUFFER_SIZE],
    const std::size_t length,
    const std::size_t target_pos,
    const bool force =false
)
```


Write a block of data to disk at the end of the dataset This is the lower-level function. There is a fixed-size buffer that cannot be exceeded. If more data than MAX_BUFFER_SIZE is to be written then the 'write_vector' function will split it up and write it in pieces. If force=true then target_pos can be used to overwrite data 


### function write_random

```
inline void write_random(
    const hid_t loc_id,
    const std::map< std::size_t, T > & data
)
```

Write data to disk at specified positions. 

### function write_RA_buffer

```
inline void write_RA_buffer(
    const T(&) buffer[MAX_BUFFER_SIZE],
    const hsize_t(&) coords[MAX_BUFFER_SIZE],
    std::size_t npoints
)
```

Write a buffer of data to disk at the specified positions (must be within current dataset extents) 

### function get_chunk

```
inline std::vector< T > get_chunk(
    std::size_t offset,
    std::size_t length
) const
```

Extract a data slice from the linked dataset. 

### function reset

```
inline void reset(
    hid_t loc_id
)
```


Clear all data on disk for this dataset Note; this just sets all values to defaults, it doesn't delete or resize the dataset 


### function create_dataset

```
virtual void create_dataset(
    hid_t location_id
)
```

Create a new dataset at the specified location. 

**Reimplements**: [Gambit::Printers::HDF5DataSetBase::create_dataset](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#function-create-dataset)


Create a (chunked) dataset. 


-------------------------------

Updated on 2024-05-31 at 15:12:04 +0000