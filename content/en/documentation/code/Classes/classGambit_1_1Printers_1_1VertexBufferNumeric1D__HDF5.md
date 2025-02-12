---
title: "class Gambit::Printers::VertexBufferNumeric1D_HDF5"
description: "VertexBuffer for simple numerical types - derived version that handles output to hdf5. "

---

# class Gambit::Printers::VertexBufferNumeric1D_HDF5



VertexBuffer for simple numerical types - derived version that handles output to hdf5.  [More...](#detailed-description)


`#include <VertexBufferNumeric1D_HDF5.hpp>`

Inherits from [Gambit::Printers::VertexBufferNumeric1D< T, CHUNKLENGTH >](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/), [Gambit::Printers::VertexBufferBase](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[VertexBufferNumeric1D_HDF5](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d__hdf5/#function-vertexbuffernumeric1d-hdf5)**()<br>Constructors.  |
| | **[VertexBufferNumeric1D_HDF5](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d__hdf5/#function-vertexbuffernumeric1d-hdf5)**(hid_t location_id, const std::string & name, const int vID, const unsigned int i, const bool sync, const bool silence, const bool resume, const char access) |
| | **[~VertexBufferNumeric1D_HDF5](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d__hdf5/#function-vertexbuffernumeric1d-hdf5)**()<br>Destructor.  |
| virtual void | **[sync_report](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d__hdf5/#function-sync-report)**() |
| virtual unsigned long | **[dset_head_pos](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d__hdf5/#function-dset-head-pos)**() |
| virtual void | **[write_to_disk](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d__hdf5/#function-write-to-disk)**()<br>Write sync buffer to HDF5 dataset.  |
| virtual void | **[write_external_to_disk](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d__hdf5/#function-write-external-to-disk)**(const T(&) values[CHUNKLENGTH], const bool(&) isvalid[CHUNKLENGTH])<br>Write externally-supplied buffer to HDF5 dataset.  |
| virtual void | **[reset](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d__hdf5/#function-reset)**(bool force =false)<br>Reset the output (non-synchronised datasets only, unless force=true)  |
| virtual void | **[finalise](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d__hdf5/#function-finalise)**() |
| virtual void | **[RA_write_to_disk](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d__hdf5/#function-ra-write-to-disk)**(const std::map< [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/), ulong > & PPID_to_dsetindex)<br>Send random access write queue to dataset interfaces for writing.  |
| void | **[attempt_postponed_RA_write_to_disk](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d__hdf5/#function-attempt-postponed-ra-write-to-disk)**(const std::map< [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/), ulong > & PPID_to_dsetindex)<br>Attempt to write any postponed RA_write attempts to disk.  |
| virtual void | **[update_dset_head_pos](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d__hdf5/#function-update-dset-head-pos)**() |
| void | **[synchronise_output_to_position](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d__hdf5/#function-synchronise-output-to-position)**(const ulong i) |
| virtual std::size_t | **[postponed_RA_queue_length](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d__hdf5/#function-postponed-ra-queue-length)**() |
| virtual ulong | **[get_dataset_length](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d__hdf5/#function-get-dataset-length)**() |

## Additional inherited members

**Public Functions inherited from [Gambit::Printers::VertexBufferNumeric1D< T, CHUNKLENGTH >](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/)**

|                | Name           |
| -------------- | -------------- |
| | **[VertexBufferNumeric1D](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-vertexbuffernumeric1d)**()<br>Constructors.  |
| | **[VertexBufferNumeric1D](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-vertexbuffernumeric1d)**(const std::string & label, const int vID, const unsigned int i, const bool sync, const bool sil, const bool resume, const char access) |
| | **[~VertexBufferNumeric1D](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-vertexbuffernumeric1d)**()<br>Destructor.  |
| void | **[append](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-append)**(const T & value, const [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/) pID =null_PPID)<br>Append a record to the buffer.  |
| void | **[RA_write](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-ra-write)**(const T & value, const [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/) pID, const std::map< [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/), ulong > & PPID_to_dsetindex)<br>Queue up a desynchronised ("random access") dataset write to previous scan iteration.  |
| virtual void | **[skip_append](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-skip-append)**()<br>No data to append this iteration; skip this slot.  |
| virtual void | **[N_skip_append](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-n-skip-append)**(ulong N) |
| virtual void | **[flush](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-flush)**()<br>Either send sync buffer data to master node via MPI, or trigger the write to disk.  |
| virtual void | **[RA_flush](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-ra-flush)**(const std::map< [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/), ulong > & PPID_to_dsetindex)<br>Either send random-access buffer data to master node via MPI, or trigger the write to disk.  |
| virtual uint | **[get_RA_queue_length](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-get-ra-queue-length)**() |
| T | **[get_entry](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-get-entry)**(const std::size_t i) const<br>Extract (copy) a record.  |
| void | **[clear](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-clear)**()<br>Clear the buffer.  |

**Protected Attributes inherited from [Gambit::Printers::VertexBufferNumeric1D< T, CHUNKLENGTH >](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/)**

|                | Name           |
| -------------- | -------------- |
| bool[LENGTH] | **[buffer_valid](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#variable-buffer-valid)** <br>Buffer variables for sequential writing.  |
| T[LENGTH] | **[buffer_entries](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#variable-buffer-entries)**  |
| T[LENGTH] | **[RA_write_queue](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#variable-ra-write-queue)**  |
| [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/)[LENGTH] | **[RA_write_locations](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#variable-ra-write-locations)** <br>Target pointIDs for RA writes.  |
| uint | **[RA_queue_length](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#variable-ra-queue-length)** <br>Current length of the RA write queue.  |
| uint | **[myRank](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#variable-myrank)** <br>MPI rank for this process.  |

**Public Functions inherited from [Gambit::Printers::VertexBufferBase](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/)**

|                | Name           |
| -------------- | -------------- |
| char | **[access_mode](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-access-mode)**() const<br>Buffer status getters.  |
| bool | **[sync_buffer_is_full](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-sync-buffer-is-full)**() const |
| bool | **[sync_buffer_is_empty](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-sync-buffer-is-empty)**() const |
| bool | **[is_synchronised](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-is-synchronised)**() const |
| bool | **[is_silenced](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-is-silenced)**() const |
| bool | **[resume_mode](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-resume-mode)**() const |
| bool | **[MPI_mode](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-mpi-mode)**() const |
| unsigned int | **[get_head_position](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-get-head-position)**() const |
| | **[VertexBufferBase](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-vertexbufferbase)**() |
| | **[VertexBufferBase](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-vertexbufferbase)**(const std::string & l, const int vID, const uint i, const bool sync, const bool sil, const bool r, const bool mode, const char a) |
| virtual | **[~VertexBufferBase](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-vertexbufferbase)**() |
| int | **[get_vertexID](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-get-vertexid)**() const |
| uint | **[get_index](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-get-index)**() const |
| std::string | **[get_label](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-get-label)**() const |
| void | **[MPImode_only](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-mpimode-only)**(std::string local_info) |
| virtual void | **[flush](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-flush)**() =0 |
| virtual void | **[RA_flush](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-ra-flush)**(const std::map< [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/), ulong > & PPID_to_dsetindex) =0 |
| virtual uint | **[get_RA_queue_length](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-get-ra-queue-length)**() =0 |
| virtual void | **[skip_append](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-skip-append)**() =0 |
| virtual void | **[N_skip_append](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-n-skip-append)**(ulong N) =0 |
| bool | **[donepoint](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-donepoint)**() |
| void | **[set_donepoint](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-set-donepoint)**(bool flag) |
| void | **[move_head_to_next_slot](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-move-head-to-next-slot)**() |
| void | **[fast_forward](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-fast-forward)**(long target_pos) |
| void | **[reset_head](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-reset-head)**() |
| void | **[error_if_done](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-error-if-done)**() |

**Protected Attributes inherited from [Gambit::Printers::VertexBufferBase](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/)**

|                | Name           |
| -------------- | -------------- |
| bool | **[sync_buffer_full](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#variable-sync-buffer-full)** <br>flag to indicate if the sync buffer is full (and ready for sending/dumping)  |
| bool | **[sync_buffer_empty](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#variable-sync-buffer-empty)**  |


## Detailed Description

```
template <class T ,
std::size_t CHUNKLENGTH>
class Gambit::Printers::VertexBufferNumeric1D_HDF5;
```

VertexBuffer for simple numerical types - derived version that handles output to hdf5. 
## Public Functions Documentation

### function VertexBufferNumeric1D_HDF5

```
VertexBufferNumeric1D_HDF5()
```

Constructors. 

[VertexBufferNumeric1D_HDF5](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d__hdf5/) member function definitions.

Constructors 


### function VertexBufferNumeric1D_HDF5

```
VertexBufferNumeric1D_HDF5(
    hid_t location_id,
    const std::string & name,
    const int vID,
    const unsigned int i,
    const bool sync,
    const bool silence,
    const bool resume,
    const char access
)
```


### function ~VertexBufferNumeric1D_HDF5

```
~VertexBufferNumeric1D_HDF5()
```

Destructor. 

Destructor Make sure buffer contents are written to file when buffer object is destroyed 


### function sync_report

```
virtual void sync_report()
```


**Reimplements**: [Gambit::Printers::VertexBufferBase::sync_report](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-sync-report)


### function dset_head_pos

```
inline virtual unsigned long dset_head_pos()
```


**Reimplements**: [Gambit::Printers::VertexBufferNumeric1D::dset_head_pos](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-dset-head-pos)


(virtual for debugging purposes) Current absolute "write head" position for synchronised buffers 


### function write_to_disk

```
virtual void write_to_disk()
```

Write sync buffer to HDF5 dataset. 

**Reimplements**: [Gambit::Printers::VertexBufferNumeric1D::write_to_disk](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-write-to-disk)


Override of buffer dump function to handle HDF5 output. 


### function write_external_to_disk

```
virtual void write_external_to_disk(
    const T(&) values[CHUNKLENGTH],
    const bool(&) isvalid[CHUNKLENGTH]
)
```

Write externally-supplied buffer to HDF5 dataset. 

Manual command to send an arbitrary buffer to be written to disk. 


### function reset

```
virtual void reset(
    bool force =false
)
```

Reset the output (non-synchronised datasets only, unless force=true) 

**Reimplements**: [Gambit::Printers::VertexBufferBase::reset](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-reset)


Reset the output (non-synchronised datasets only) 


Empty the queue of postponed writes, because it would now be erased had we gotten around to writing it.

Invalidate the contents of the linked datasets This can be done by simply resetting the all validity bools to "false"


### function finalise

```
virtual void finalise()
```


**Reimplements**: [Gambit::Printers::VertexBufferBase::finalise](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-finalise)


### function RA_write_to_disk

```
virtual void RA_write_to_disk(
    const std::map< PPIDpair, ulong > & PPID_to_dsetindex
)
```

Send random access write queue to dataset interfaces for writing. 

**Reimplements**: [Gambit::Printers::VertexBufferNumeric1D::RA_write_to_disk](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-ra-write-to-disk)


Use the provided PPIDpair-->dset_location map to locate the target parameter points in the output dataset. (Temp RA buffers for immediate writes)


### function attempt_postponed_RA_write_to_disk

```
void attempt_postponed_RA_write_to_disk(
    const std::map< PPIDpair, ulong > & PPID_to_dsetindex
)
```

Attempt to write any postponed RA_write attempts to disk. 

Attempt to write postponed RA entries to disk. 


Use the provided PPIDpair-->dset_location map to locate the target parameter points in the output dataset. (Temp RA buffers for immediate writes)

Postponed entries which still cannot be written will be added here.

Need to go through the postponed entries one CHUNKLENGTH at a time


### function update_dset_head_pos

```
inline virtual void update_dset_head_pos()
```


**Reimplements**: [Gambit::Printers::VertexBufferNumeric1D::update_dset_head_pos](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-update-dset-head-pos)


Update the variables needed to tracks the currently target dset slot (really just updates the nextemptyslab variable) 


### function synchronise_output_to_position

```
void synchronise_output_to_position(
    const ulong i
)
```


Ensure dataset "write head" (i.e. next append) is prepared to write to the supplied absolute dataset index (e.g. by inserting blank entries if need)

Ensure dataset "write head" (i.e. next append) is prepared to write to the supplied absolute dataset index (e.g. by inserting blank entries if need)

NEW MEANING: Ensure that the supplied index has been written to, and that the next append will happen to the next index above it. 


### function postponed_RA_queue_length

```
inline virtual std::size_t postponed_RA_queue_length()
```


**Reimplements**: [Gambit::Printers::VertexBufferBase::postponed_RA_queue_length](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-postponed-ra-queue-length)


Check how many RA writes are waiting in the postpone queue (mostly for debugging purposes) 


### function get_dataset_length

```
virtual ulong get_dataset_length()
```


**Reimplements**: [Gambit::Printers::VertexBufferBase::get_dataset_length](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-get-dataset-length)


-------------------------------

Updated on 2025-02-12 at 15:36:39 +0000