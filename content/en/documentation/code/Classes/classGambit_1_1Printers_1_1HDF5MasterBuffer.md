---
title: "class Gambit::Printers::HDF5MasterBuffer"

description: "[No description available]"

---

# class Gambit::Printers::HDF5MasterBuffer



[No description available] [More...](#detailed-description)


`#include <hdf5printer_v2.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[HDF5MasterBuffer](/documentation/code/classes/classgambit_1_1printers_1_1hdf5masterbuffer/#function-hdf5masterbuffer)**(const std::string & filename, const std::string & groupname, const bool sync, const std::size_t buffer_length)<br>Constructor.  |
| | **[~HDF5MasterBuffer](/documentation/code/classes/classgambit_1_1printers_1_1hdf5masterbuffer/#function-hdf5masterbuffer)**()<br>Destructor.  |
| void | **[flush](/documentation/code/classes/classgambit_1_1printers_1_1hdf5masterbuffer/#function-flush)**()<br>Empty all buffers to disk.  |
| void | **[reset](/documentation/code/classes/classgambit_1_1printers_1_1hdf5masterbuffer/#function-reset)**()<br>Clear all data in buffers _**and on disk**_ for this printer.  |
| void | **[resynchronise](/documentation/code/classes/classgambit_1_1printers_1_1hdf5masterbuffer/#function-resynchronise)**()<br>Make sure all buffers know about all points in all buffers.  |
| bool | **[all_buffers_empty](/documentation/code/classes/classgambit_1_1printers_1_1hdf5masterbuffer/#function-all-buffers-empty)**()<br>Report whether all the buffers are empty.  |
| bool | **[is_synchronised](/documentation/code/classes/classgambit_1_1printers_1_1hdf5masterbuffer/#function-is-synchronised)**()<br>Report what sort of buffers we are managing.  |
| std::string | **[buffer_status](/documentation/code/classes/classgambit_1_1printers_1_1hdf5masterbuffer/#function-buffer-status)**()<br>Report status of non-empty buffers (as a string message)  |
| std::string | **[get_file](/documentation/code/classes/classgambit_1_1printers_1_1hdf5masterbuffer/#function-get-file)**()<br>Report what output file we are targeting.  |
| std::string | **[get_group](/documentation/code/classes/classgambit_1_1printers_1_1hdf5masterbuffer/#function-get-group)**()<br>Report which group in the output file we are targeting.  |
| std::size_t | **[get_buffer_length](/documentation/code/classes/classgambit_1_1printers_1_1hdf5masterbuffer/#function-get-buffer-length)**()<br>Report length of buffer for HDF5 output.  |
| std::size_t | **[get_Npoints](/documentation/code/classes/classgambit_1_1printers_1_1hdf5masterbuffer/#function-get-npoints)**()<br>Report number of points currently in the buffer.  |
| void | **[extend_all_datasets_to](/documentation/code/classes/classgambit_1_1printers_1_1hdf5masterbuffer/#function-extend-all-datasets-to)**(const std::size_t length)<br>Extend all datasets to the specified size;.  |
| std::map< ulong, ulong > | **[get_highest_PPIDs](/documentation/code/classes/classgambit_1_1printers_1_1hdf5masterbuffer/#function-get-highest-ppids)**(const int mpisize)<br>Search the existing output and find the highest used pointIDs for each rank.  |
| void | **[lock_and_open_file](/documentation/code/classes/classgambit_1_1printers_1_1hdf5masterbuffer/#function-lock-and-open-file)**(const char access_type ='w')<br>Open (and lock) output HDF5 file and obtain HDF5 handles.  |
| void | **[close_and_unlock_file](/documentation/code/classes/classgambit_1_1printers_1_1hdf5masterbuffer/#function-close-and-unlock-file)**()<br>Close (and unlock) output HDF5 file and release HDF5 handles.  |
| hid_t | **[get_location_id](/documentation/code/classes/classgambit_1_1printers_1_1hdf5masterbuffer/#function-get-location-id)**()<br>Retrieve the location_id specifying where output should be created in the HDF5 file.  |
| std::size_t | **[get_next_free_position](/documentation/code/classes/classgambit_1_1printers_1_1hdf5masterbuffer/#function-get-next-free-position)**()<br>Get next available position in the synchronised output datasets.  |
| std::size_t | **[get_Nbuffers](/documentation/code/classes/classgambit_1_1printers_1_1hdf5masterbuffer/#function-get-nbuffers)**()<br>Report number of buffers that we are managing.  |
| double | **[get_sizeMB](/documentation/code/classes/classgambit_1_1printers_1_1hdf5masterbuffer/#function-get-sizemb)**()<br>Report upper limit estimate of size of all buffer data in MB.  |
| std::vector< std::pair< std::string, int > > | **[get_all_dset_names_on_disk](/documentation/code/classes/classgambit_1_1printers_1_1hdf5masterbuffer/#function-get-all-dset-names-on-disk)**()<br>Get names and types of all datasets in the group that we are pointed at.  |
| const std::map< std::string, [HDF5BufferBase](/documentation/code/classes/classgambit_1_1printers_1_1hdf5bufferbase/) * > & | **[get_all_buffers](/documentation/code/classes/classgambit_1_1printers_1_1hdf5masterbuffer/#function-get-all-buffers)**()<br>Retrieve a map containing pointers to all buffers managed by this object.  |
| const std::set< [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/) > & | **[get_all_points](/documentation/code/classes/classgambit_1_1printers_1_1hdf5masterbuffer/#function-get-all-points)**()<br>Retrieve set containing all points currently known to be in these buffers.  |
| void | **[untrack_points](/documentation/code/classes/classgambit_1_1printers_1_1hdf5masterbuffer/#function-untrack-points)**(const std::set< [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/) > & removed_points)<br>Remove points from buffer tracking.  |
| template <class T \> <br>void | **[schedule_print](/documentation/code/classes/classgambit_1_1printers_1_1hdf5masterbuffer/#function-schedule-print)**(T const & value, const std::string & label, const unsigned int mpirank, const unsigned long pointID)<br>Queue up data to be written to disk when buffers are full.  |

## Detailed Description

```
class Gambit::Printers::HDF5MasterBuffer;
```


Class to manage all buffers for a given printer object Also handles the file locking/access to the output file 

## Public Functions Documentation

### function HDF5MasterBuffer

```
HDF5MasterBuffer(
    const std::string & filename,
    const std::string & groupname,
    const bool sync,
    const std::size_t buffer_length
)
```

Constructor. 

Member functions of [HDF5MasterBuffer](/documentation/code/classes/classgambit_1_1printers_1_1hdf5masterbuffer/). 


### function ~HDF5MasterBuffer

```
~HDF5MasterBuffer()
```

Destructor. 

### function flush

```
void flush()
```

Empty all buffers to disk. 

Empty all buffers to disk (or as much of them as is currently possible in RA case) 


While we are here, check that buffered_points and buffered_points_set are the same size


### function reset

```
void reset()
```

Clear all data in buffers _**and on disk**_ for this printer. 

### function resynchronise

```
void resynchronise()
```

Make sure all buffers know about all points in all buffers. 

Make sure all buffers know about all points in all buffers Should not generally be necessary if points are added in the "normal" way. Only needed in special circumstances (e.g. when receiving points from another process). 


### function all_buffers_empty

```
bool all_buffers_empty()
```

Report whether all the buffers are empty. 

### function is_synchronised

```
bool is_synchronised()
```

Report what sort of buffers we are managing. 

### function buffer_status

```
std::string buffer_status()
```

Report status of non-empty buffers (as a string message) 

Report status of non-empty buffers. 


### function get_file

```
std::string get_file()
```

Report what output file we are targeting. 

### function get_group

```
std::string get_group()
```

Report which group in the output file we are targeting. 

### function get_buffer_length

```
std::size_t get_buffer_length()
```

Report length of buffer for HDF5 output. 

### function get_Npoints

```
std::size_t get_Npoints()
```

Report number of points currently in the buffer. 

### function extend_all_datasets_to

```
void extend_all_datasets_to(
    const std::size_t length
)
```

Extend all datasets to the specified size;. 

### function get_highest_PPIDs

```
std::map< ulong, ulong > get_highest_PPIDs(
    const int mpisize
)
```

Search the existing output and find the highest used pointIDs for each rank. 

### function lock_and_open_file

```
void lock_and_open_file(
    const char access_type ='w'
)
```

Open (and lock) output HDF5 file and obtain HDF5 handles. 

### function close_and_unlock_file

```
void close_and_unlock_file()
```

Close (and unlock) output HDF5 file and release HDF5 handles. 

### function get_location_id

```
hid_t get_location_id()
```

Retrieve the location_id specifying where output should be created in the HDF5 file. 

### function get_next_free_position

```
std::size_t get_next_free_position()
```

Get next available position in the synchronised output datasets. 

Determine the next free index in the output datasets. 


### function get_Nbuffers

```
std::size_t get_Nbuffers()
```

Report number of buffers that we are managing. 

### function get_sizeMB

```
double get_sizeMB()
```

Report upper limit estimate of size of all buffer data in MB. 

### function get_all_dset_names_on_disk

```
std::vector< std::pair< std::string, int > > get_all_dset_names_on_disk()
```

Get names and types of all datasets in the group that we are pointed at. 

Get names of all datasets in the group that we are pointed at. 


### function get_all_buffers

```
const std::map< std::string, HDF5BufferBase * > & get_all_buffers()
```

Retrieve a map containing pointers to all buffers managed by this object. 

### function get_all_points

```
const std::set< PPIDpair > & get_all_points()
```

Retrieve set containing all points currently known to be in these buffers. 

### function untrack_points

```
void untrack_points(
    const std::set< PPIDpair > & removed_points
)
```

Remove points from buffer tracking. 

### function schedule_print

```
template <class T >
inline void schedule_print(
    T const & value,
    const std::string & label,
    const unsigned int mpirank,
    const unsigned long pointID
)
```

Queue up data to be written to disk when buffers are full. 

Check if the point is known to be in the buffers already

While we are here, check that buffered_points and buffered_points_set are the same size

This is a new point! See if buffers are full and need to be flushed

Sync buffers exceeded the allowed size somehow

RA buffers may not have been able to fully flush, so check their length and report if it is getting big.

Attempt to flush again every 1000 points beyond buffer limits


-------------------------------

Updated on 2022-09-08 at 03:41:59 +0000