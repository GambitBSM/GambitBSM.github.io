---
title: "class Gambit::Printers::HDF5DataSetBase"
description: "Base class for interfacing to a HDF5 dataset. "

---

# class Gambit::Printers::HDF5DataSetBase



Base class for interfacing to a HDF5 dataset. 


`#include <hdf5printer_v2.hpp>`

Inherited by [Gambit::Printers::HDF5DataSet< int >](/documentation/code/classes/classgambit_1_1printers_1_1hdf5dataset/), [Gambit::Printers::HDF5DataSet< T >](/documentation/code/classes/classgambit_1_1printers_1_1hdf5dataset/), [Gambit::Printers::HDF5DataSetBasic](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbasic/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[HDF5DataSetBase](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#function-gambitprintershdf5datasetbase-hdf5datasetbase)**(const std::string & name, const hid_t hdftype_id)<br>[HDF5DataSetBase](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/) member functions.  |
| | **[HDF5DataSetBase](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#function-gambitprintershdf5datasetbase-hdf5datasetbase)**(const std::string & name)<br>Version where type is not provided; set to default of -1.  |
| virtual | **[~HDF5DataSetBase](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#function-gambitprintershdf5datasetbase-hdf5datasetbase)**()<br>Destructor.  |
| void | **[open_dataset](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#function-gambitprintershdf5datasetbase-open-dataset)**(hid_t location_id)<br>Open dataset on disk and obtain HDF5 handles.  |
| void | **[close_dataset](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#function-gambitprintershdf5datasetbase-close-dataset)**()<br>Close dataset on disk and release handles.  |
| std::size_t | **[get_dset_length](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#function-gambitprintershdf5datasetbase-get-dset-length)**() const<br>Retrieve the current size of the dataset on disk.  |
| bool | **[dataset_exists](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#function-gambitprintershdf5datasetbase-dataset-exists)**(const hid_t loc_id)<br>Check if our dataset exists on disk with the required name at the given location.  |
| void | **[ensure_dataset_exists](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#function-gambitprintershdf5datasetbase-ensure-dataset-exists)**(const hid_t loc_id, const std::size_t length)<br>Ensure that a correctly named dataset exists at the target location with the specified length.  |
| void | **[extend_dset_to](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#function-gambitprintershdf5datasetbase-extend-dset-to)**(const std::size_t new_size)<br>Extend dataset to the specified size, filling it with default values.  |
| std::string | **[myname](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#function-gambitprintershdf5datasetbase-myname)**() const<br>Retrieve name of the dataset we are supposed to access.  |
| int | **[get_type_id](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#function-gambitprintershdf5datasetbase-get-type-id)**() const<br>Retrieve the integer type ID for this dataset.  |
| hid_t | **[get_hdftype_id](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#function-gambitprintershdf5datasetbase-get-hdftype-id)**() const<br>Retrieve the HDF5 type ID for this dataset.  |
| bool | **[get_exists_on_disk](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#function-gambitprintershdf5datasetbase-get-exists-on-disk)**() const<br>Variable tracking whether the dataset is known to exist in the output file yet.  |
| void | **[set_exists_on_disk](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#function-gambitprintershdf5datasetbase-set-exists-on-disk)**() |
| virtual void | **[create_dataset](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#function-gambitprintershdf5datasetbase-create-dataset)**(hid_t location_id) =0 |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[ensure_dataset_is_open](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#function-gambitprintershdf5datasetbase-ensure-dataset-is-open)**() const<br>Enforce that the dataset must be open for whatever follows (or else an error is thrown)  |
| hid_t | **[get_dset_id](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#function-gambitprintershdf5datasetbase-get-dset-id)**() const<br>Retrieve the dataset ID for the currently open dataset.  |
| void | **[extend_dset_by](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#function-gambitprintershdf5datasetbase-extend-dset-by)**(const std::size_t extend_by)<br>Set the variable that tracks the (virtual) dataset size on disk.  |
| std::pair< hid_t, hid_t > | **[select_hyperslab](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#function-gambitprintershdf5datasetbase-select-hyperslab)**(std::size_t offset, std::size_t length) const<br>Obtain memory and dataspace identifiers for writing to a hyperslab in the dataset.  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| hid_t | **[dset_id](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#variable-gambitprintershdf5datasetbase-dset-id)** <br>HDF5 dataset identifer.  |
| hid_t | **[hdftype_id](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#variable-gambitprintershdf5datasetbase-hdftype-id)** <br>HDF5 type ID for this dataset.  |
| int | **[type_id](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#variable-gambitprintershdf5datasetbase-type-id)** <br>Integer identifier for the template type of this dataset (determined by derived type)  |

## Public Functions Documentation

### function HDF5DataSetBase

```
HDF5DataSetBase(
    const std::string & name,
    const hid_t hdftype_id
)
```

[HDF5DataSetBase](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/) member functions. 

Constructor 


### function HDF5DataSetBase

```
HDF5DataSetBase(
    const std::string & name
)
```

Version where type is not provided; set to default of -1. 

### function ~HDF5DataSetBase

```
virtual ~HDF5DataSetBase()
```

Destructor. 

### function open_dataset

```
void open_dataset(
    hid_t location_id
)
```

Open dataset on disk and obtain HDF5 handles. 

Open an existing dataset. 


### function close_dataset

```
void close_dataset()
```

Close dataset on disk and release handles. 

Close a dataset. 


### function get_dset_length

```
std::size_t get_dset_length() const
```

Retrieve the current size of the dataset on disk. 

### function dataset_exists

```
bool dataset_exists(
    const hid_t loc_id
)
```

Check if our dataset exists on disk with the required name at the given location. 

### function ensure_dataset_exists

```
void ensure_dataset_exists(
    const hid_t loc_id,
    const std::size_t length
)
```

Ensure that a correctly named dataset exists at the target location with the specified length. 

Ensure that the dataset exists with the specified length. 


### function extend_dset_to

```
void extend_dset_to(
    const std::size_t new_size
)
```

Extend dataset to the specified size, filling it with default values. 

Set the variable that tracks the (used) dataset size on disk.

Extend dataset to the specified size 


### function myname

```
std::string myname() const
```

Retrieve name of the dataset we are supposed to access. 

### function get_type_id

```
int get_type_id() const
```

Retrieve the integer type ID for this dataset. 

### function get_hdftype_id

```
hid_t get_hdftype_id() const
```

Retrieve the HDF5 type ID for this dataset. 

### function get_exists_on_disk

```
bool get_exists_on_disk() const
```

Variable tracking whether the dataset is known to exist in the output file yet. 

Access variables that track whether the dataset exists on disk yet. 


### function set_exists_on_disk

```
void set_exists_on_disk()
```


### function create_dataset

```
virtual void create_dataset(
    hid_t location_id
) =0
```


**Reimplemented by**: [Gambit::Printers::HDF5DataSetBasic::create_dataset](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbasic/#function-gambitprintershdf5datasetbasic-create-dataset), [Gambit::Printers::HDF5DataSet::create_dataset](/documentation/code/classes/classgambit_1_1printers_1_1hdf5dataset/#function-gambitprintershdf5dataset-create-dataset), [Gambit::Printers::HDF5DataSet::create_dataset](/documentation/code/classes/classgambit_1_1printers_1_1hdf5dataset/#function-gambitprintershdf5dataset-create-dataset)


Create a new dataset at the specified location (implemented in derived class since need to know the type) 


## Protected Functions Documentation

### function ensure_dataset_is_open

```
void ensure_dataset_is_open() const
```

Enforce that the dataset must be open for whatever follows (or else an error is thrown) 

### function get_dset_id

```
hid_t get_dset_id() const
```

Retrieve the dataset ID for the currently open dataset. 

### function extend_dset_by

```
void extend_dset_by(
    const std::size_t extend_by
)
```

Set the variable that tracks the (virtual) dataset size on disk. 

Extend dataset by the specified amount.

Extend dataset by the specified amount 


### function select_hyperslab

```
std::pair< hid_t, hid_t > select_hyperslab(
    std::size_t offset,
    std::size_t length
) const
```

Obtain memory and dataspace identifiers for writing to a hyperslab in the dataset. 

## Protected Attributes Documentation

### variable dset_id

```
hid_t dset_id;
```

HDF5 dataset identifer. 

### variable hdftype_id

```
hid_t hdftype_id;
```

HDF5 type ID for this dataset. 

### variable type_id

```
int type_id;
```

Integer identifier for the template type of this dataset (determined by derived type) 

-------------------------------

Updated on 2022-09-08 at 02:00:49 +0000