---
title: "class Gambit::Printers::HDF5Buffer"
description: "Class to manage buffer for a single output label. "

---

# class Gambit::Printers::HDF5Buffer



Class to manage buffer for a single output label.  [More...](#detailed-description)


`#include <hdf5printer_v2.hpp>`

Inherits from [Gambit::Printers::HDF5BufferBase](/documentation/code/classes/classgambit_1_1printers_1_1hdf5bufferbase/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[HDF5Buffer](/documentation/code/classes/classgambit_1_1printers_1_1hdf5buffer/#function-hdf5buffer)**(const std::string & name, const bool sync, const std::vector< [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/) > & buffered_points)<br>Constructor.  |
| virtual void | **[update](/documentation/code/classes/classgambit_1_1printers_1_1hdf5buffer/#function-update)**(const [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/) & ppid)<br>Make sure buffer includes the specified point (data will be set as 'invalid' unless given elsewhere)  |
| void | **[append](/documentation/code/classes/classgambit_1_1printers_1_1hdf5buffer/#function-append)**(T const & value, const [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/) & ppid)<br>Insert data to print buffer at the specified point (overwrite if it already exists in the buffer)  |
| virtual void | **[block_flush](/documentation/code/classes/classgambit_1_1printers_1_1hdf5buffer/#function-block-flush)**(const hid_t loc_id, const std::vector< [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/) > & order, const std::size_t target_pos) |
| virtual void | **[random_flush](/documentation/code/classes/classgambit_1_1printers_1_1hdf5buffer/#function-random-flush)**(const hid_t loc_id, const std::map< [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/), std::size_t > & position_map) |
| virtual void | **[reset](/documentation/code/classes/classgambit_1_1printers_1_1hdf5buffer/#function-reset)**(hid_t loc_id) |
| virtual void | **[ensure_dataset_exists](/documentation/code/classes/classgambit_1_1printers_1_1hdf5buffer/#function-ensure-dataset-exists)**(const hid_t loc_id, const std::size_t length)<br>Make sure datasets exist on disk with the correct name and size.  |
| virtual bool | **[exists_on_disk](/documentation/code/classes/classgambit_1_1printers_1_1hdf5buffer/#function-exists-on-disk)**() const<br>Report whether the dataset for which we are the buffer exists on disk yet.  |
| virtual std::size_t | **[N_items_in_buffer](/documentation/code/classes/classgambit_1_1printers_1_1hdf5buffer/#function-n-items-in-buffer)**() |
| void | **[add_float_block](/documentation/code/classes/classgambit_1_1printers_1_1hdf5buffer/#function-add-float-block)**(const [HDF5bufferchunk](/documentation/code/classes/structgambit_1_1printers_1_1hdf5bufferchunk/) & chunk, const std::size_t buf) |
| void | **[add_int_block](/documentation/code/classes/classgambit_1_1printers_1_1hdf5buffer/#function-add-int-block)**(const [HDF5bufferchunk](/documentation/code/classes/structgambit_1_1printers_1_1hdf5bufferchunk/) & chunk, const std::size_t buf) |
| virtual std::pair< std::vector< double >, std::vector< int > > | **[flush_to_vector_dbl](/documentation/code/classes/classgambit_1_1printers_1_1hdf5buffer/#function-flush-to-vector-dbl)**(const std::vector< [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/) > & order) |
| virtual std::pair< std::vector< long >, std::vector< int > > | **[flush_to_vector_int](/documentation/code/classes/classgambit_1_1printers_1_1hdf5buffer/#function-flush-to-vector-int)**(const std::vector< [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/) > & order) |
| virtual int | **[get_type_id](/documentation/code/classes/classgambit_1_1printers_1_1hdf5buffer/#function-get-type-id)**() const<br>Retrieve the integer type ID for the buffered dataset.  |

## Additional inherited members

**Public Functions inherited from [Gambit::Printers::HDF5BufferBase](/documentation/code/classes/classgambit_1_1printers_1_1hdf5bufferbase/)**

|                | Name           |
| -------------- | -------------- |
| | **[HDF5BufferBase](/documentation/code/classes/classgambit_1_1printers_1_1hdf5bufferbase/#function-hdf5bufferbase)**(const std::string & name, const bool sync)<br>Constructor.  |
| std::string | **[dset_name](/documentation/code/classes/classgambit_1_1printers_1_1hdf5bufferbase/#function-dset-name)**() const<br>Report name of dataset for which we are the buffer.  |
| bool | **[is_synchronised](/documentation/code/classes/classgambit_1_1printers_1_1hdf5bufferbase/#function-is-synchronised)**() const<br>Report whether this buffer is synchronised.  |
| std::set< [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/) > | **[get_points_set](/documentation/code/classes/classgambit_1_1printers_1_1hdf5bufferbase/#function-get-points-set)**() const<br>Report all the points in this buffer.  |
| virtual | **[~HDF5BufferBase](/documentation/code/classes/classgambit_1_1printers_1_1hdf5bufferbase/#function-hdf5bufferbase)**()<br>Destructor.  |

**Protected Attributes inherited from [Gambit::Printers::HDF5BufferBase](/documentation/code/classes/classgambit_1_1printers_1_1hdf5bufferbase/)**

|                | Name           |
| -------------- | -------------- |
| std::set< [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/) > | **[buffer_set](/documentation/code/classes/classgambit_1_1printers_1_1hdf5bufferbase/#variable-buffer-set)** <br>Set detailing what points are in the buffer.  |
| std::map< [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/), int > | **[buffer_valid](/documentation/code/classes/classgambit_1_1printers_1_1hdf5bufferbase/#variable-buffer-valid)** <br>Buffer specifying whether the data in the primary buffer is "valid".  |


## Detailed Description

```
template <class T >
class Gambit::Printers::HDF5Buffer;
```

Class to manage buffer for a single output label. 
## Public Functions Documentation

### function HDF5Buffer

```
inline HDF5Buffer(
    const std::string & name,
    const bool sync,
    const std::vector< PPIDpair > & buffered_points
)
```

Constructor. 

### function update

```
inline virtual void update(
    const PPIDpair & ppid
)
```

Make sure buffer includes the specified point (data will be set as 'invalid' unless given elsewhere) 

**Reimplements**: [Gambit::Printers::HDF5BufferBase::update](/documentation/code/classes/classgambit_1_1printers_1_1hdf5bufferbase/#function-update)


### function append

```
inline void append(
    T const & value,
    const PPIDpair & ppid
)
```

Insert data to print buffer at the specified point (overwrite if it already exists in the buffer) 

### function block_flush

```
inline virtual void block_flush(
    const hid_t loc_id,
    const std::vector< PPIDpair > & order,
    const std::size_t target_pos
)
```


**Reimplements**: [Gambit::Printers::HDF5BufferBase::block_flush](/documentation/code/classes/classgambit_1_1printers_1_1hdf5bufferbase/#function-block-flush)


Empty the buffer to disk as block with the specified order into the target position (only allowed if target_pos is beyond the current end of the dataset!) 


### function random_flush

```
inline virtual void random_flush(
    const hid_t loc_id,
    const std::map< PPIDpair, std::size_t > & position_map
)
```


**Reimplements**: [Gambit::Printers::HDF5BufferBase::random_flush](/documentation/code/classes/classgambit_1_1printers_1_1hdf5bufferbase/#function-random-flush)


Empty the buffer to disk as "random access" data at pre-existing positions matching the point IDs May not completely empty the buffer; points will be removed from the buffer if they are included in the supplied position map. 


### function reset

```
inline virtual void reset(
    hid_t loc_id
)
```


**Reimplements**: [Gambit::Printers::HDF5BufferBase::reset](/documentation/code/classes/classgambit_1_1printers_1_1hdf5bufferbase/#function-reset)


Clear all data in the buffer _**and on disk**_ Only allowed for "random access" buffers 


### function ensure_dataset_exists

```
inline virtual void ensure_dataset_exists(
    const hid_t loc_id,
    const std::size_t length
)
```

Make sure datasets exist on disk with the correct name and size. 

**Reimplements**: [Gambit::Printers::HDF5BufferBase::ensure_dataset_exists](/documentation/code/classes/classgambit_1_1printers_1_1hdf5bufferbase/#function-ensure-dataset-exists)


### function exists_on_disk

```
inline virtual bool exists_on_disk() const
```

Report whether the dataset for which we are the buffer exists on disk yet. 

**Reimplements**: [Gambit::Printers::HDF5BufferBase::exists_on_disk](/documentation/code/classes/classgambit_1_1printers_1_1hdf5bufferbase/#function-exists-on-disk)


### function N_items_in_buffer

```
inline virtual std::size_t N_items_in_buffer()
```


**Reimplements**: [Gambit::Printers::HDF5BufferBase::N_items_in_buffer](/documentation/code/classes/classgambit_1_1printers_1_1hdf5bufferbase/#function-n-items-in-buffer)


Might as well check the internal consistency of this buffer while we are at it


### function add_float_block

```
inline void add_float_block(
    const HDF5bufferchunk & chunk,
    const std::size_t buf
)
```


### function add_int_block

```
inline void add_int_block(
    const HDF5bufferchunk & chunk,
    const std::size_t buf
)
```


### function flush_to_vector_dbl

```
inline virtual std::pair< std::vector< double >, std::vector< int > > flush_to_vector_dbl(
    const std::vector< PPIDpair > & order
)
```


**Reimplements**: [Gambit::Printers::HDF5BufferBase::flush_to_vector_dbl](/documentation/code/classes/classgambit_1_1printers_1_1hdf5bufferbase/#function-flush-to-vector-dbl)


### function flush_to_vector_int

```
inline virtual std::pair< std::vector< long >, std::vector< int > > flush_to_vector_int(
    const std::vector< PPIDpair > & order
)
```


**Reimplements**: [Gambit::Printers::HDF5BufferBase::flush_to_vector_int](/documentation/code/classes/classgambit_1_1printers_1_1hdf5bufferbase/#function-flush-to-vector-int)


### function get_type_id

```
inline virtual int get_type_id() const
```

Retrieve the integer type ID for the buffered dataset. 

**Reimplements**: [Gambit::Printers::HDF5BufferBase::get_type_id](/documentation/code/classes/classgambit_1_1printers_1_1hdf5bufferbase/#function-get-type-id)


-------------------------------

Updated on 2022-09-08 at 02:27:27 +0000