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
| virtual unsigned long | **[dset_head_pos](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-dset-head-pos)**() =0 |
| virtual void | **[sync_report](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-sync-report)**() =0 |
| virtual void | **[flush](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-flush)**() =0 |
| virtual void | **[RA_flush](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-ra-flush)**(const std::map< [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/), ulong > & PPID_to_dsetindex) =0 |
| virtual void | **[finalise](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-finalise)**() =0 |
| virtual std::size_t | **[postponed_RA_queue_length](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-postponed-ra-queue-length)**() =0 |
| virtual uint | **[get_RA_queue_length](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-get-ra-queue-length)**() =0 |
| virtual void | **[reset](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-reset)**(bool force =false) =0 |
| virtual void | **[skip_append](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-skip-append)**() =0 |
| virtual void | **[N_skip_append](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-n-skip-append)**(ulong N) =0 |
| virtual ulong | **[get_dataset_length](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-get-dataset-length)**() =0 |
| bool | **[donepoint](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-donepoint)**() |
| void | **[set_donepoint](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-set-donepoint)**(bool flag) |
| void | **[move_head_to_next_slot](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-move-head-to-next-slot)**() |
| void | **[fast_forward](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-fast-forward)**(long target_pos) |
| void | **[reset_head](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-reset-head)**() |
| void | **[error_if_done](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-error-if-done)**() |
| virtual void | **[synchronise_output_to_position](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#function-synchronise-output-to-position)**(const unsigned long i) =0 |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| bool | **[sync_buffer_full](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#variable-sync-buffer-full)** <br>flag to indicate if the sync buffer is full (and ready for sending/dumping)  |
| bool | **[sync_buffer_empty](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/#variable-sync-buffer-empty)**  |

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


**Reimplemented by**: [Gambit::Printers::VertexBufferNumeric1D_HDF5::dset_head_pos](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d__hdf5/#function-dset-head-pos), [Gambit::Printers::VertexBufferNumeric1D::dset_head_pos](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-dset-head-pos), [Gambit::Printers::VertexBufferNumeric1D::dset_head_pos](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-dset-head-pos)


### function sync_report

```
virtual void sync_report() =0
```


**Reimplemented by**: [Gambit::Printers::VertexBufferNumeric1D_HDF5::sync_report](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d__hdf5/#function-sync-report)


### function flush

```
virtual void flush() =0
```


**Reimplemented by**: [Gambit::Printers::VertexBufferNumeric1D::flush](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-flush), [Gambit::Printers::VertexBufferNumeric1D::flush](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-flush)


### function RA_flush

```
virtual void RA_flush(
    const std::map< PPIDpair, ulong > & PPID_to_dsetindex
) =0
```


**Reimplemented by**: [Gambit::Printers::VertexBufferNumeric1D::RA_flush](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-ra-flush), [Gambit::Printers::VertexBufferNumeric1D::RA_flush](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-ra-flush)


### function finalise

```
virtual void finalise() =0
```


**Reimplemented by**: [Gambit::Printers::VertexBufferNumeric1D_HDF5::finalise](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d__hdf5/#function-finalise)


### function postponed_RA_queue_length

```
virtual std::size_t postponed_RA_queue_length() =0
```


**Reimplemented by**: [Gambit::Printers::VertexBufferNumeric1D_HDF5::postponed_RA_queue_length](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d__hdf5/#function-postponed-ra-queue-length)


### function get_RA_queue_length

```
virtual uint get_RA_queue_length() =0
```


**Reimplemented by**: [Gambit::Printers::VertexBufferNumeric1D::get_RA_queue_length](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-get-ra-queue-length), [Gambit::Printers::VertexBufferNumeric1D::get_RA_queue_length](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-get-ra-queue-length)


### function reset

```
virtual void reset(
    bool force =false
) =0
```


**Reimplemented by**: [Gambit::Printers::VertexBufferNumeric1D_HDF5::reset](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d__hdf5/#function-reset)


### function skip_append

```
virtual void skip_append() =0
```


**Reimplemented by**: [Gambit::Printers::VertexBufferNumeric1D::skip_append](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-skip-append), [Gambit::Printers::VertexBufferNumeric1D::skip_append](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-skip-append)


### function N_skip_append

```
virtual void N_skip_append(
    ulong N
) =0
```


**Reimplemented by**: [Gambit::Printers::VertexBufferNumeric1D::N_skip_append](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-n-skip-append), [Gambit::Printers::VertexBufferNumeric1D::N_skip_append](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d/#function-n-skip-append)


Skip several/many positions NOTE! This is meant for initialising new buffers to the correct position. If buffer overflows it may get cleared without data being written, so don't use this in other contexts. 


### function get_dataset_length

```
virtual ulong get_dataset_length() =0
```


**Reimplemented by**: [Gambit::Printers::VertexBufferNumeric1D_HDF5::get_dataset_length](/documentation/code/classes/classgambit_1_1printers_1_1vertexbuffernumeric1d__hdf5/#function-get-dataset-length)


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

Updated on 2022-09-08 at 02:27:27 +0000