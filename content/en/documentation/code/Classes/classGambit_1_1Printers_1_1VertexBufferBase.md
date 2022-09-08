---
title: "class Gambit::Printers::VertexBufferBase"
description: "VertexBuffer abstract interface base class. "

---

# class Gambit::Printers::VertexBufferBase



VertexBuffer abstract interface base class. 


`#include <VertexBufferBase.hpp>`

Inherited by [Gambit::Printers::VertexBufferNumeric1D< T, CHUNKLENGTH >](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/), [Gambit::Printers::VertexBufferNumeric1D< T, LENGTH >](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/)

## Public Functions

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
| virtual unsigned long | **[dset_head_pos](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-dset-head-pos)**() =0 |
| virtual void | **[sync_report](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-sync-report)**() =0 |
| virtual void | **[flush](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-flush)**() =0 |
| virtual void | **[RA_flush](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-ra-flush)**(const std::map< [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/), ulong > & PPID_to_dsetindex) =0 |
| virtual void | **[finalise](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-finalise)**() =0 |
| virtual std::size_t | **[postponed_RA_queue_length](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-postponed-ra-queue-length)**() =0 |
| virtual uint | **[get_RA_queue_length](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-get-ra-queue-length)**() =0 |
| virtual void | **[reset](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-reset)**(bool force =false) =0 |
| virtual void | **[skip_append](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-skip-append)**() =0 |
| virtual void | **[N_skip_append](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-n-skip-append)**(ulong N) =0 |
| virtual ulong | **[get_dataset_length](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-get-dataset-length)**() =0 |
| bool | **[donepoint](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-donepoint)**() |
| void | **[set_donepoint](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-set-donepoint)**(bool flag) |
| void | **[move_head_to_next_slot](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-move-head-to-next-slot)**() |
| void | **[fast_forward](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-fast-forward)**(long target_pos) |
| void | **[reset_head](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-reset-head)**() |
| void | **[error_if_done](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-error-if-done)**() |
| virtual void | **[synchronise_output_to_position](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-gambitprintersvertexbufferbase-synchronise-output-to-position)**(const unsigned long i) =0 |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| bool | **[sync_buffer_full](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#variable-gambitprintersvertexbufferbase-sync-buffer-full)** <br>flag to indicate if the sync buffer is full (and ready for sending/dumping)  |
| bool | **[sync_buffer_empty](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#variable-gambitprintersvertexbufferbase-sync-buffer-empty)**  |

## Public Functions Documentation

### function access_mode

```
inline char access_mode() const
```

Buffer status getters. 

### function sync_buffer_is_full

```
inline bool sync_buffer_is_full() const
```


### function sync_buffer_is_empty

```
inline bool sync_buffer_is_empty() const
```


### function is_synchronised

```
inline bool is_synchronised() const
```


### function is_silenced

```
inline bool is_silenced() const
```


### function resume_mode

```
inline bool resume_mode() const
```


### function MPI_mode

```
inline bool MPI_mode() const
```


### function get_head_position

```
inline unsigned int get_head_position() const
```


### function VertexBufferBase

```
inline VertexBufferBase()
```


### function VertexBufferBase

```
inline VertexBufferBase(
    const std::string & l,
    const int vID,
    const uint i,
    const bool sync,
    const bool sil,
    const bool r,
    const bool mode,
    const char a
)
```


### function ~VertexBufferBase

```
inline virtual ~VertexBufferBase()
```


### function get_vertexID

```
inline int get_vertexID() const
```


### function get_index

```
inline uint get_index() const
```


### function get_label

```
inline std::string get_label() const
```


### function MPImode_only

```
inline void MPImode_only(
    std::string local_info
)
```


MPI mode error Put in functions which should not run if MPImode=false 


### function dset_head_pos

```
virtual unsigned long dset_head_pos() =0
```


**Reimplemented by**: [Gambit::Printers::VertexBufferNumeric1D_HDF5::dset_head_pos](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d__hdf5/#function-gambitprintersvertexbuffernumeric1d-hdf5-dset-head-pos), [Gambit::Printers::VertexBufferNumeric1D::dset_head_pos](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-gambitprintersvertexbuffernumeric1d-dset-head-pos), [Gambit::Printers::VertexBufferNumeric1D::dset_head_pos](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-gambitprintersvertexbuffernumeric1d-dset-head-pos)


### function sync_report

```
virtual void sync_report() =0
```


**Reimplemented by**: [Gambit::Printers::VertexBufferNumeric1D_HDF5::sync_report](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d__hdf5/#function-gambitprintersvertexbuffernumeric1d-hdf5-sync-report)


### function flush

```
virtual void flush() =0
```


**Reimplemented by**: [Gambit::Printers::VertexBufferNumeric1D::flush](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-gambitprintersvertexbuffernumeric1d-flush), [Gambit::Printers::VertexBufferNumeric1D::flush](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-gambitprintersvertexbuffernumeric1d-flush)


### function RA_flush

```
virtual void RA_flush(
    const std::map< PPIDpair, ulong > & PPID_to_dsetindex
) =0
```


**Reimplemented by**: [Gambit::Printers::VertexBufferNumeric1D::RA_flush](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-gambitprintersvertexbuffernumeric1d-ra-flush), [Gambit::Printers::VertexBufferNumeric1D::RA_flush](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-gambitprintersvertexbuffernumeric1d-ra-flush)


### function finalise

```
virtual void finalise() =0
```


**Reimplemented by**: [Gambit::Printers::VertexBufferNumeric1D_HDF5::finalise](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d__hdf5/#function-gambitprintersvertexbuffernumeric1d-hdf5-finalise)


### function postponed_RA_queue_length

```
virtual std::size_t postponed_RA_queue_length() =0
```


**Reimplemented by**: [Gambit::Printers::VertexBufferNumeric1D_HDF5::postponed_RA_queue_length](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d__hdf5/#function-gambitprintersvertexbuffernumeric1d-hdf5-postponed-ra-queue-length)


### function get_RA_queue_length

```
virtual uint get_RA_queue_length() =0
```


**Reimplemented by**: [Gambit::Printers::VertexBufferNumeric1D::get_RA_queue_length](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-gambitprintersvertexbuffernumeric1d-get-ra-queue-length), [Gambit::Printers::VertexBufferNumeric1D::get_RA_queue_length](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-gambitprintersvertexbuffernumeric1d-get-ra-queue-length)


### function reset

```
virtual void reset(
    bool force =false
) =0
```


**Reimplemented by**: [Gambit::Printers::VertexBufferNumeric1D_HDF5::reset](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d__hdf5/#function-gambitprintersvertexbuffernumeric1d-hdf5-reset)


### function skip_append

```
virtual void skip_append() =0
```


**Reimplemented by**: [Gambit::Printers::VertexBufferNumeric1D::skip_append](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-gambitprintersvertexbuffernumeric1d-skip-append), [Gambit::Printers::VertexBufferNumeric1D::skip_append](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-gambitprintersvertexbuffernumeric1d-skip-append)


### function N_skip_append

```
virtual void N_skip_append(
    ulong N
) =0
```


**Reimplemented by**: [Gambit::Printers::VertexBufferNumeric1D::N_skip_append](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-gambitprintersvertexbuffernumeric1d-n-skip-append), [Gambit::Printers::VertexBufferNumeric1D::N_skip_append](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-gambitprintersvertexbuffernumeric1d-n-skip-append)


Skip several/many positions NOTE! This is meant for initialising new buffers to the correct position. If buffer overflows it may get cleared without data being written, so don't use this in other contexts. 


### function get_dataset_length

```
virtual ulong get_dataset_length() =0
```


**Reimplemented by**: [Gambit::Printers::VertexBufferNumeric1D_HDF5::get_dataset_length](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d__hdf5/#function-gambitprintersvertexbuffernumeric1d-hdf5-get-dataset-length)


### function donepoint

```
inline bool donepoint()
```


### function set_donepoint

```
inline void set_donepoint(
    bool flag
)
```


### function move_head_to_next_slot

```
inline void move_head_to_next_slot()
```


### function fast_forward

```
inline void fast_forward(
    long target_pos
)
```


### function reset_head

```
inline void reset_head()
```


### function error_if_done

```
inline void error_if_done()
```


### function synchronise_output_to_position

```
virtual void synchronise_output_to_position(
    const unsigned long i
) =0
```


## Protected Attributes Documentation

### variable sync_buffer_full

```
bool sync_buffer_full = false;
```

flag to indicate if the sync buffer is full (and ready for sending/dumping) 

### variable sync_buffer_empty

```
bool sync_buffer_empty = true;
```


-------------------------------

Updated on 2022-09-08 at 01:48:56 +0000