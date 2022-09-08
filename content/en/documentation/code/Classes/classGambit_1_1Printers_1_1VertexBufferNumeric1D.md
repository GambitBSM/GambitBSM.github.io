---
title: "class Gambit::Printers::VertexBufferNumeric1D"
description: "VertexBuffer for simple numerical types. "

---

# class Gambit::Printers::VertexBufferNumeric1D



VertexBuffer for simple numerical types.  [More...](#detailed-description)


`#include <VertexBufferNumeric1D.hpp>`

Inherits from [Gambit::Printers::VertexBufferBase](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[VertexBufferNumeric1D](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-gambitprintersvertexbuffernumeric1d-vertexbuffernumeric1d)**()<br>Constructors.  |
| | **[VertexBufferNumeric1D](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-gambitprintersvertexbuffernumeric1d-vertexbuffernumeric1d)**(const std::string & label, const int vID, const unsigned int i, const bool sync, const bool sil, const bool resume, const char access) |
| | **[~VertexBufferNumeric1D](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-gambitprintersvertexbuffernumeric1d-vertexbuffernumeric1d)**()<br>Destructor.  |
| void | **[append](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-gambitprintersvertexbuffernumeric1d-append)**(const T & value, const [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/) pID =null_PPID)<br>Append a record to the buffer.  |
| virtual unsigned long | **[dset_head_pos](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-gambitprintersvertexbuffernumeric1d-dset-head-pos)**() =0<br>Virtual for debugging; find out what the absolute sync position is from the derived class.  |
| virtual void | **[update_dset_head_pos](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-gambitprintersvertexbuffernumeric1d-update-dset-head-pos)**() =0<br>Virtual for debugging: Update the variables needed to track the currently target dset slot.  |
| void | **[RA_write](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-gambitprintersvertexbuffernumeric1d-ra-write)**(const T & value, const [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/) pID, const std::map< [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/), ulong > & PPID_to_dsetindex)<br>Queue up a desynchronised ("random access") dataset write to previous scan iteration.  |
| virtual void | **[skip_append](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-gambitprintersvertexbuffernumeric1d-skip-append)**()<br>No data to append this iteration; skip this slot.  |
| virtual void | **[N_skip_append](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-gambitprintersvertexbuffernumeric1d-n-skip-append)**(ulong N) |
| virtual void | **[flush](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-gambitprintersvertexbuffernumeric1d-flush)**()<br>Either send sync buffer data to master node via MPI, or trigger the write to disk.  |
| virtual void | **[RA_flush](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-gambitprintersvertexbuffernumeric1d-ra-flush)**(const std::map< [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/), ulong > & PPID_to_dsetindex)<br>Either send random-access buffer data to master node via MPI, or trigger the write to disk.  |
| virtual void | **[write_to_disk](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-gambitprintersvertexbuffernumeric1d-write-to-disk)**() =0 |
| virtual void | **[RA_write_to_disk](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-gambitprintersvertexbuffernumeric1d-ra-write-to-disk)**(const std::map< [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/), ulong > & PPID_to_dsetindex) =0 |
| virtual void | **[write_external_to_disk](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-gambitprintersvertexbuffernumeric1d-write-external-to-disk)**(const T(&) values[LENGTH], const bool(&) isvalid[LENGTH]) =0<br>Write externally-supplied buffer to HDF5 dataset.  |
| virtual uint | **[get_RA_queue_length](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-gambitprintersvertexbuffernumeric1d-get-ra-queue-length)**() |
| T | **[get_entry](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-gambitprintersvertexbuffernumeric1d-get-entry)**(const std::size_t i) const<br>Extract (copy) a record.  |
| void | **[clear](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-gambitprintersvertexbuffernumeric1d-clear)**()<br>Clear the buffer.  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| bool[LENGTH] | **[buffer_valid](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#variable-gambitprintersvertexbuffernumeric1d-buffer-valid)** <br>Buffer variables for sequential writing.  |
| T[LENGTH] | **[buffer_entries](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#variable-gambitprintersvertexbuffernumeric1d-buffer-entries)**  |
| T[LENGTH] | **[RA_write_queue](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#variable-gambitprintersvertexbuffernumeric1d-ra-write-queue)**  |
| [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/)[LENGTH] | **[RA_write_locations](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#variable-gambitprintersvertexbuffernumeric1d-ra-write-locations)** <br>Target pointIDs for RA writes.  |
| uint | **[RA_queue_length](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#variable-gambitprintersvertexbuffernumeric1d-ra-queue-length)** <br>Current length of the RA write queue.  |
| uint | **[myRank](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#variable-gambitprintersvertexbuffernumeric1d-myrank)** <br>MPI rank for this process.  |

## Additional inherited members

**Public Functions inherited from [Gambit::Printers::VertexBufferBase](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/)**

|                | Name           |
| -------------- | -------------- |
| char | **[access_mode](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-access-mode)**() const<br>Buffer status getters.  |
| bool | **[sync_buffer_is_full](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-sync-buffer-is-full)**() const |
| bool | **[sync_buffer_is_empty](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-sync-buffer-is-empty)**() const |
| bool | **[is_synchronised](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-is-synchronised)**() const |
| bool | **[is_silenced](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-is-silenced)**() const |
| bool | **[resume_mode](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-resume-mode)**() const |
| bool | **[MPI_mode](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-mpi-mode)**() const |
| unsigned int | **[get_head_position](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-get-head-position)**() const |
| | **[VertexBufferBase](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-vertexbufferbase)**() |
| | **[VertexBufferBase](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-vertexbufferbase)**(const std::string & l, const int vID, const uint i, const bool sync, const bool sil, const bool r, const bool mode, const char a) |
| virtual | **[~VertexBufferBase](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-vertexbufferbase)**() |
| int | **[get_vertexID](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-get-vertexid)**() const |
| uint | **[get_index](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-get-index)**() const |
| std::string | **[get_label](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-get-label)**() const |
| void | **[MPImode_only](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-mpimode-only)**(std::string local_info) |
| virtual void | **[sync_report](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-sync-report)**() =0 |
| virtual void | **[finalise](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-finalise)**() =0 |
| virtual std::size_t | **[postponed_RA_queue_length](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-postponed-ra-queue-length)**() =0 |
| virtual void | **[reset](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-reset)**(bool force =false) =0 |
| virtual ulong | **[get_dataset_length](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-get-dataset-length)**() =0 |
| bool | **[donepoint](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-donepoint)**() |
| void | **[set_donepoint](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-set-donepoint)**(bool flag) |
| void | **[move_head_to_next_slot](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-move-head-to-next-slot)**() |
| void | **[fast_forward](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-fast-forward)**(long target_pos) |
| void | **[reset_head](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-reset-head)**() |
| void | **[error_if_done](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-error-if-done)**() |
| virtual void | **[synchronise_output_to_position](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-synchronise-output-to-position)**(const unsigned long i) =0 |

**Protected Attributes inherited from [Gambit::Printers::VertexBufferBase](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/)**

|                | Name           |
| -------------- | -------------- |
| bool | **[sync_buffer_full](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#variable-gambitprintersvertexbufferbase-sync-buffer-full)** <br>flag to indicate if the sync buffer is full (and ready for sending/dumping)  |
| bool | **[sync_buffer_empty](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#variable-gambitprintersvertexbufferbase-sync-buffer-empty)**  |


## Detailed Description

```
template <class T ,
std::size_t LENGTH>
class Gambit::Printers::VertexBufferNumeric1D;
```

VertexBuffer for simple numerical types. 
## Public Functions Documentation

### function VertexBufferNumeric1D

```
inline VertexBufferNumeric1D()
```

Constructors. 

### function VertexBufferNumeric1D

```
inline VertexBufferNumeric1D(
    const std::string & label,
    const int vID,
    const unsigned int i,
    const bool sync,
    const bool sil,
    const bool resume,
    const char access
)
```


### function ~VertexBufferNumeric1D

```
inline ~VertexBufferNumeric1D()
```

Destructor. 

### function append

```
void append(
    const T & value,
    const PPIDpair pID =null_PPID
)
```

Append a record to the buffer. 

[VertexBufferNumeric1D](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/) function definitions.

Append a record to the buffer 


### function dset_head_pos

```
virtual unsigned long dset_head_pos() =0
```

Virtual for debugging; find out what the absolute sync position is from the derived class. 

**Reimplements**: [Gambit::Printers::VertexBufferBase::dset_head_pos](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-dset-head-pos)


**Reimplemented by**: [Gambit::Printers::VertexBufferNumeric1D_HDF5::dset_head_pos](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d__hdf5/#function-gambitprintersvertexbuffernumeric1d-hdf5-dset-head-pos)


### function update_dset_head_pos

```
virtual void update_dset_head_pos() =0
```

Virtual for debugging: Update the variables needed to track the currently target dset slot. 

**Reimplemented by**: [Gambit::Printers::VertexBufferNumeric1D_HDF5::update_dset_head_pos](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d__hdf5/#function-gambitprintersvertexbuffernumeric1d-hdf5-update-dset-head-pos)


### function RA_write

```
void RA_write(
    const T & value,
    const PPIDpair pID,
    const std::map< PPIDpair, ulong > & PPID_to_dsetindex
)
```

Queue up a desynchronised ("random access") dataset write to previous scan iteration. 

### function skip_append

```
virtual void skip_append()
```

No data to append this iteration; skip this slot. 

**Reimplements**: [Gambit::Printers::VertexBufferBase::skip_append](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-skip-append)


### function N_skip_append

```
virtual void N_skip_append(
    ulong N
)
```


**Reimplements**: [Gambit::Printers::VertexBufferBase::N_skip_append](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-n-skip-append)


Skip several/many positions NOTE! This is meant for initialising new buffers to the correct position. If buffer overflows it may get cleared without data being written, so don't use this in other contexts.

TODO: Deprecated. Skip several/many positions NOTE! This is meant for initialising new buffers to the correct position. If buffer overflows it will be cleared without data being written, so don't use this in other contexts. 


### function flush

```
virtual void flush()
```

Either send sync buffer data to master node via MPI, or trigger the write to disk. 

**Reimplements**: [Gambit::Printers::VertexBufferBase::flush](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-flush)


### function RA_flush

```
virtual void RA_flush(
    const std::map< PPIDpair, ulong > & PPID_to_dsetindex
)
```

Either send random-access buffer data to master node via MPI, or trigger the write to disk. 

**Reimplements**: [Gambit::Printers::VertexBufferBase::RA_flush](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-ra-flush)


### function write_to_disk

```
virtual void write_to_disk() =0
```


**Reimplemented by**: [Gambit::Printers::VertexBufferNumeric1D_HDF5::write_to_disk](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d__hdf5/#function-gambitprintersvertexbuffernumeric1d-hdf5-write-to-disk)


### function RA_write_to_disk

```
virtual void RA_write_to_disk(
    const std::map< PPIDpair, ulong > & PPID_to_dsetindex
) =0
```


**Reimplemented by**: [Gambit::Printers::VertexBufferNumeric1D_HDF5::RA_write_to_disk](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d__hdf5/#function-gambitprintersvertexbuffernumeric1d-hdf5-ra-write-to-disk)


### function write_external_to_disk

```
virtual void write_external_to_disk(
    const T(&) values[LENGTH],
    const bool(&) isvalid[LENGTH]
) =0
```

Write externally-supplied buffer to HDF5 dataset. 

### function get_RA_queue_length

```
inline virtual uint get_RA_queue_length()
```


**Reimplements**: [Gambit::Printers::VertexBufferBase::get_RA_queue_length](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-get-ra-queue-length)


### function get_entry

```
T get_entry(
    const std::size_t i
) const
```

Extract (copy) a record. 

### function clear

```
void clear()
```

Clear the buffer. 

## Protected Attributes Documentation

### variable buffer_valid

```
bool[LENGTH] buffer_valid;
```

Buffer variables for sequential writing. 

### variable buffer_entries

```
T[LENGTH] buffer_entries;
```


### variable RA_write_queue

```
T[LENGTH] RA_write_queue;
```


Buffer variables for random access writing Queue for random access writes to dataset (independent of main buffer) 


### variable RA_write_locations

```
PPIDpair[LENGTH] RA_write_locations;
```

Target pointIDs for RA writes. 

### variable RA_queue_length

```
uint RA_queue_length = 0;
```

Current length of the RA write queue. 

### variable myRank

```
uint myRank = 0;
```

MPI rank for this process. 

-------------------------------

Updated on 2022-09-08 at 01:48:56 +0000