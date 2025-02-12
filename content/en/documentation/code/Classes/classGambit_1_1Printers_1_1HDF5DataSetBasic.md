---
title: "class Gambit::Printers::HDF5DataSetBasic"
description: "Constructable class for doing basic operations on a HDF5 dataset. "

---

# class Gambit::Printers::HDF5DataSetBasic



Constructable class for doing basic operations on a HDF5 dataset. 


`#include <hdf5printer_v2.hpp>`

Inherits from [Gambit::Printers::HDF5DataSetBase](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[HDF5DataSetBasic](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbasic/#function-hdf5datasetbasic)**(const std::string & name)<br>[HDF5DataSetBasic](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbasic/) member functions.  |
| virtual void | **[create_dataset](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbasic/#function-create-dataset)**(hid_t location_id) |

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


## Public Functions Documentation

### function HDF5DataSetBasic

```
HDF5DataSetBasic(
    const std::string & name
)
```

[HDF5DataSetBasic](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbasic/) member functions. 

### function create_dataset

```
virtual void create_dataset(
    hid_t location_id
)
```


**Reimplements**: [Gambit::Printers::HDF5DataSetBase::create_dataset](/documentation/code/classes/classgambit_1_1printers_1_1hdf5datasetbase/#function-create-dataset)


Create a new dataset at the specified location (implemented in derived class since need to know the type) 


-------------------------------

Updated on 2025-02-12 at 15:36:39 +0000