---
title: "class Gambit::Printers::HDF5BufferBase"
description: "Base class for buffers. "

---

# class Gambit::Printers::HDF5BufferBase



Base class for buffers. 


`#include <hdf5printer_v2.hpp>`

Inherited by [Gambit::Printers::HDF5Buffer< T >](/documentation/code/classes/classgambit_1_1printers_1_1hdf5buffer/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[HDF5BufferBase](/documentation/code/classes/classgambit_1_1printers_1_1hdf5bufferbase/#function-gambitprintershdf5bufferbase-hdf5bufferbase)**(const std::string & name, const bool sync)<br>Constructor.  |
| std::string | **[dset_name](/documentation/code/classes/classgambit_1_1printers_1_1hdf5bufferbase/#function-gambitprintershdf5bufferbase-dset-name)**() const<br>Report name of dataset for which we are the buffer.  |
| bool | **[is_synchronised](/documentation/code/classes/classgambit_1_1printers_1_1hdf5bufferbase/#function-gambitprintershdf5bufferbase-is-synchronised)**() const<br>Report whether this buffer is synchronised.  |
| std::set< [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/) > | **[get_points_set](/documentation/code/classes/classgambit_1_1printers_1_1hdf5bufferbase/#function-gambitprintershdf5bufferbase-get-points-set)**() const<br>Report all the points in this buffer.  |
| virtual | **[~HDF5BufferBase](/documentation/code/classes/classgambit_1_1printers_1_1hdf5bufferbase/#function-gambitprintershdf5bufferbase-hdf5bufferbase)**()<br>Destructor.  |
| virtual bool | **[exists_on_disk](/documentation/code/classes/classgambit_1_1printers_1_1hdf5bufferbase/#function-gambitprintershdf5bufferbase-exists-on-disk)**() const =0<br>Report whether the dataset for which we are the buffer is known to exist on disk yet.  |
| virtual void | **[update](/documentation/code/classes/classgambit_1_1printers_1_1hdf5bufferbase/#function-gambitprintershdf5bufferbase-update)**(const [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/) & ppid) =0<br>Make sure buffer includes the input point (data will be set as 'invalid' unless given elsewhere)  |
| virtual void | **[block_flush](/documentation/code/classes/classgambit_1_1printers_1_1hdf5bufferbase/#function-gambitprintershdf5bufferbase-block-flush)**(const hid_t loc_id, const std::vector< [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/) > & order, const std::size_t target_pos) =0<br>Empty buffer to disk as a block.  |
| virtual void | **[random_flush](/documentation/code/classes/classgambit_1_1printers_1_1hdf5bufferbase/#function-gambitprintershdf5bufferbase-random-flush)**(const hid_t loc_id, const std::map< [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/), std::size_t > & position_map) =0<br>Empty buffer to disk as arbitrarily positioned data.  |
| virtual std::pair< std::vector< double >, std::vector< int > > | **[flush_to_vector_dbl](/documentation/code/classes/classgambit_1_1printers_1_1hdf5bufferbase/#function-gambitprintershdf5bufferbase-flush-to-vector-dbl)**(const std::vector< [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/) > & order) =0 |
| virtual std::pair< std::vector< long >, std::vector< int > > | **[flush_to_vector_int](/documentation/code/classes/classgambit_1_1printers_1_1hdf5bufferbase/#function-gambitprintershdf5bufferbase-flush-to-vector-int)**(const std::vector< [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/) > & order) =0 |
| virtual void | **[ensure_dataset_exists](/documentation/code/classes/classgambit_1_1printers_1_1hdf5bufferbase/#function-gambitprintershdf5bufferbase-ensure-dataset-exists)**(const hid_t loc_id, const std::size_t length) =0<br>Make sure datasets exist on disk with the correct name and size.  |
| virtual void | **[reset](/documentation/code/classes/classgambit_1_1printers_1_1hdf5bufferbase/#function-gambitprintershdf5bufferbase-reset)**(hid_t loc_id) =0<br>Clear all data in memory _**and on disk**_ for this buffer.  |
| virtual std::size_t | **[N_items_in_buffer](/documentation/code/classes/classgambit_1_1printers_1_1hdf5bufferbase/#function-gambitprintershdf5bufferbase-n-items-in-buffer)**() =0 |
| virtual int | **[get_type_id](/documentation/code/classes/classgambit_1_1printers_1_1hdf5bufferbase/#function-gambitprintershdf5bufferbase-get-type-id)**() const =0<br>Retrieve the integer type ID for this dataset.  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| std::set< [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/) > | **[buffer_set](/documentation/code/classes/classgambit_1_1printers_1_1hdf5bufferbase/#variable-gambitprintershdf5bufferbase-buffer-set)** <br>Set detailing what points are in the buffer.  |
| std::map< [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/), int > | **[buffer_valid](/documentation/code/classes/classgambit_1_1printers_1_1hdf5bufferbase/#variable-gambitprintershdf5bufferbase-buffer-valid)** <br>Buffer specifying whether the data in the primary buffer is "valid".  |

## Public Functions Documentation

### function HDF5BufferBase

```
HDF5BufferBase(
    const std::string & name,
    const bool sync
)
```

Constructor. 

[HDF5BufferBase](/documentation/code/classes/classgambit_1_1printers_1_1hdf5bufferbase/) member functions.

Constructor 


### function dset_name

```
std::string dset_name() const
```

Report name of dataset for which we are the buffer. 

### function is_synchronised

```
bool is_synchronised() const
```

Report whether this buffer is synchronised. 

### function get_points_set

```
std::set< PPIDpair > get_points_set() const
```

Report all the points in this buffer. 

### function ~HDF5BufferBase

```
inline virtual ~HDF5BufferBase()
```

Destructor. 

### function exists_on_disk

```
virtual bool exists_on_disk() const =0
```

Report whether the dataset for which we are the buffer is known to exist on disk yet. 

**Reimplemented by**: [Gambit::Printers::HDF5Buffer::exists_on_disk](/documentation/code/classes/classgambit_1_1printers_1_1hdf5buffer/#function-gambitprintershdf5buffer-exists-on-disk)


### function update

```
virtual void update(
    const PPIDpair & ppid
) =0
```

Make sure buffer includes the input point (data will be set as 'invalid' unless given elsewhere) 

**Reimplemented by**: [Gambit::Printers::HDF5Buffer::update](/documentation/code/classes/classgambit_1_1printers_1_1hdf5buffer/#function-gambitprintershdf5buffer-update)


### function block_flush

```
virtual void block_flush(
    const hid_t loc_id,
    const std::vector< PPIDpair > & order,
    const std::size_t target_pos
) =0
```

Empty buffer to disk as a block. 

**Reimplemented by**: [Gambit::Printers::HDF5Buffer::block_flush](/documentation/code/classes/classgambit_1_1printers_1_1hdf5buffer/#function-gambitprintershdf5buffer-block-flush)


### function random_flush

```
virtual void random_flush(
    const hid_t loc_id,
    const std::map< PPIDpair, std::size_t > & position_map
) =0
```

Empty buffer to disk as arbitrarily positioned data. 

**Reimplemented by**: [Gambit::Printers::HDF5Buffer::random_flush](/documentation/code/classes/classgambit_1_1printers_1_1hdf5buffer/#function-gambitprintershdf5buffer-random-flush)


### function flush_to_vector_dbl

```
virtual std::pair< std::vector< double >, std::vector< int > > flush_to_vector_dbl(
    const std::vector< PPIDpair > & order
) =0
```


**Reimplemented by**: [Gambit::Printers::HDF5Buffer::flush_to_vector_dbl](/documentation/code/classes/classgambit_1_1printers_1_1hdf5buffer/#function-gambitprintershdf5buffer-flush-to-vector-dbl)


### function flush_to_vector_int

```
virtual std::pair< std::vector< long >, std::vector< int > > flush_to_vector_int(
    const std::vector< PPIDpair > & order
) =0
```


**Reimplemented by**: [Gambit::Printers::HDF5Buffer::flush_to_vector_int](/documentation/code/classes/classgambit_1_1printers_1_1hdf5buffer/#function-gambitprintershdf5buffer-flush-to-vector-int)


### function ensure_dataset_exists

```
virtual void ensure_dataset_exists(
    const hid_t loc_id,
    const std::size_t length
) =0
```

Make sure datasets exist on disk with the correct name and size. 

**Reimplemented by**: [Gambit::Printers::HDF5Buffer::ensure_dataset_exists](/documentation/code/classes/classgambit_1_1printers_1_1hdf5buffer/#function-gambitprintershdf5buffer-ensure-dataset-exists)


### function reset

```
virtual void reset(
    hid_t loc_id
) =0
```

Clear all data in memory _**and on disk**_ for this buffer. 

**Reimplemented by**: [Gambit::Printers::HDF5Buffer::reset](/documentation/code/classes/classgambit_1_1printers_1_1hdf5buffer/#function-gambitprintershdf5buffer-reset)


### function N_items_in_buffer

```
virtual std::size_t N_items_in_buffer() =0
```


**Reimplemented by**: [Gambit::Printers::HDF5Buffer::N_items_in_buffer](/documentation/code/classes/classgambit_1_1printers_1_1hdf5buffer/#function-gambitprintershdf5buffer-n-items-in-buffer)


### function get_type_id

```
virtual int get_type_id() const =0
```

Retrieve the integer type ID for this dataset. 

**Reimplemented by**: [Gambit::Printers::HDF5Buffer::get_type_id](/documentation/code/classes/classgambit_1_1printers_1_1hdf5buffer/#function-gambitprintershdf5buffer-get-type-id)


## Protected Attributes Documentation

### variable buffer_set

```
std::set< PPIDpair > buffer_set;
```

Set detailing what points are in the buffer. 

### variable buffer_valid

```
std::map< PPIDpair, int > buffer_valid;
```

Buffer specifying whether the data in the primary buffer is "valid". 

-------------------------------

Updated on 2022-09-08 at 01:48:56 +0000