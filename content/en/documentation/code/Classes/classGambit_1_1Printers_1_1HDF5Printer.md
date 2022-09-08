---
title: "class Gambit::Printers::HDF5Printer"
description: "The main printer class for output to HDF5 format. "

---

# class Gambit::Printers::HDF5Printer



The main printer class for output to HDF5 format. 


`#include <hdf5printer.hpp>`

Inherits from [Gambit::Printers::BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/), [Gambit::Printers::BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| bool | **[is_stream_managed](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer/#function-gambitprintershdf5printer-is-stream-managed)**([VBIDpair](/documentation/code/classes/structgambit_1_1printers_1_1vbidpair/) & key) const<br>HDF5Printer-specific functions.  |
| hid_t | **[get_location](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer/#function-gambitprintershdf5printer-get-location)**() const<br>Retrieve pointer to HDF5 location to which datasets are added.  |
| hid_t | **[get_RA_location](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer/#function-gambitprintershdf5printer-get-ra-location)**() const |
| void | **[insert_buffer](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer/#function-gambitprintershdf5printer-insert-buffer)**([VBIDpair](/documentation/code/classes/structgambit_1_1printers_1_1vbidpair/) & key, [VertexBufferBase](/documentation/code/classes/classgambit_1_1printers_1_1vertexbufferbase/) & newbuffer)<br>Add a pointer to a new buffer to the global list.  |
| unsigned long | **[get_sync_pos](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer/#function-gambitprintershdf5printer-get-sync-pos)**() const |
| | **[HDF5Printer](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer/#function-gambitprintershdf5printer-hdf5printer)**(const [Options](/documentation/code/classes/classgambit_1_1options/) & options, [BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/) *const primary =NULL)<br>Constructor (for construction via inifile options)  |
| void | **[common_constructor](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer/#function-gambitprintershdf5printer-common-constructor)**(const [Options](/documentation/code/classes/classgambit_1_1options/) & options)<br>Tasks common to the various constructors.  |
| | **[~HDF5Printer](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer/#function-gambitprintershdf5printer-hdf5printer)**()<br>Destructor.  |
| virtual void | **[initialise](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer/#function-gambitprintershdf5printer-initialise)**(const std::vector< int > & )<br>Initialisation function.  |
| virtual void | **[flush](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer/#function-gambitprintershdf5printer-flush)**() |
| virtual void | **[reset](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer/#function-gambitprintershdf5printer-reset)**(bool force =false) |
| virtual void | **[finalise](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer/#function-gambitprintershdf5printer-finalise)**(bool abnormal =false)<br>Perform final cleanup and write tasks.  |
| virtual [Options](/documentation/code/classes/classgambit_1_1options/) | **[resume_reader_options](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer/#function-gambitprintershdf5printer-resume-reader-options)**() |
| template <typename T \> <br>void | **[_print](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer/#function-gambitprintershdf5printer-print)**(T const & , const std::string & label, const int vertexID, const uint, const ulong)<br>Print functions.  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| [BaseBufferMap](/documentation/code/namespaces/namespacegambit_1_1printers/#typedef-gambitprinters-basebuffermap) | **[all_buffers](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer/#variable-gambitprintershdf5printer-all-buffers)** <br>Things which other printers need access to.  |

## Additional inherited members

**Public Functions inherited from [Gambit::Printers::BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/)**

|                | Name           |
| -------------- | -------------- |
| | **[BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/#function-gambitprintersbaseprinter-baseprinter)**() |
| | **[BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/#function-gambitprintersbaseprinter-baseprinter)**([BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/) *const primary, bool is_aux_IN) |
| virtual | **[~BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/#function-gambitprintersbaseprinter-baseprinter)**()<br>Destructor.  |
| void | **[set_as_aux](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/#function-gambitprintersbaseprinter-set-as-aux)**()<br>Set this as an auxilliary printer.  |
| virtual void | **[auxilliary_init](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/#function-gambitprintersbaseprinter-auxilliary-init)**() |
| [BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/) * | **[get_primary_printer](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/#function-gambitprintersbaseprinter-get-primary-printer)**() |
| bool | **[is_auxilliary_printer](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/#function-gambitprintersbaseprinter-is-auxilliary-printer)**() |
| template <typename T \> <br>void | **[print](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/#function-gambitprintersbaseprinter-print)**(T const & in, const std::string & label, const int vertexID, const uint rank, const ulong pointID) |
| template <typename T \> <br>void | **[print](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/#function-gambitprintersbaseprinter-print)**(T const & in, const std::string & label, const uint rank, const ulong pointID) |

**Public Functions inherited from [Gambit::Printers::BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**

|                | Name           |
| -------------- | -------------- |
| | **[BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-gambitprintersbasebaseprinter-basebaseprinter)**() |
| virtual | **[~BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-gambitprintersbasebaseprinter-basebaseprinter)**() |
| int | **[getRank](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-gambitprintersbasebaseprinter-getrank)**()<br>Retrieve/Set MPI rank (setting is useful for e.g. the postprocessor to re-print points from other ranks)  |
| void | **[setRank](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-gambitprintersbasebaseprinter-setrank)**(int r) |
| bool & | **[get_printUnitcube](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-gambitprintersbasebaseprinter-get-printunitcube)**() |
| void | **[set_printUnitcube](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-gambitprintersbasebaseprinter-set-printunitcube)**(const bool & rflag) |
| std::set< std::string > | **[getPrintList](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-gambitprintersbasebaseprinter-getprintlist)**() |
| void | **[setPrintList](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-gambitprintersbasebaseprinter-setprintlist)**(const std::set< std::string > & in) |
| void | **[addToPrintList](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-gambitprintersbasebaseprinter-addtoprintlist)**(const std::string & in) |
| bool | **[get_resume](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-gambitprintersbasebaseprinter-get-resume)**() |
| void | **[set_resume](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-gambitprintersbasebaseprinter-set-resume)**(bool rflag) |
| void | **[disable](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-gambitprintersbasebaseprinter-disable)**(int n =-1) |
| void | **[enable](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-gambitprintersbasebaseprinter-enable)**() |
| template <typename T \> <br>void | **[print](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-gambitprintersbasebaseprinter-print)**(T const & in, const std::string & label, const int vertexID, const uint rank, const ulong pointID) |
| template <typename T \> <br>void | **[print](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-gambitprintersbasebaseprinter-print)**(T const & in, const std::string & label, const uint rank, const ulong pointID) |

**Protected Attributes inherited from [Gambit::Printers::BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**

|                | Name           |
| -------------- | -------------- |
| bool | **[printer_enabled](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#variable-gambitprintersbasebaseprinter-printer-enabled)** <br>Flag to check if print functions are enabled or disabled.  |
| int | **[printer_cooldown](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#variable-gambitprintersbasebaseprinter-printer-cooldown)** <br>Counter for printer cooldown. If non-zero printer can be disabled for a fixed number of print calls.  |


## Public Functions Documentation

### function is_stream_managed

```
bool is_stream_managed(
    VBIDpair & key
) const
```

HDF5Printer-specific functions. 

Check if an output stream is already managed by some buffer in any printer.

Check if an output stream is already managed by some buffer in some printer 


### function get_location

```
hid_t get_location() const
```

Retrieve pointer to HDF5 location to which datasets are added. 

### function get_RA_location

```
hid_t get_RA_location() const
```


### function insert_buffer

```
void insert_buffer(
    VBIDpair & key,
    VertexBufferBase & newbuffer
)
```

Add a pointer to a new buffer to the global list. 

Add a pointer to a new buffer to the global list for this printer and also register it with the list global to all printers. 


### function get_sync_pos

```
inline unsigned long get_sync_pos() const
```


Get the number of pointIDs know to this printer (should correspond to the number of "appends" each active buffer has received) 


### function HDF5Printer

```
HDF5Printer(
    const Options & options,
    BasePrinter *const primary =NULL
)
```

Constructor (for construction via inifile options) 

[HDF5Printer](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer/) member functions. 


### function common_constructor

```
void common_constructor(
    const Options & options
)
```

Tasks common to the various constructors. 

Check if combined output file exists


### function ~HDF5Printer

```
~HDF5Printer()
```

Destructor. 

### function initialise

```
virtual void initialise(
    const std::vector< int > & 
)
```

Initialisation function. 

**Reimplements**: [Gambit::Printers::BasePrinter::initialise](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/#function-gambitprintersbaseprinter-initialise)


Virtual function overloads: 


### function flush

```
virtual void flush()
```


**Reimplements**: [Gambit::Printers::BasePrinter::flush](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/#function-gambitprintersbaseprinter-flush)


Empty all the buffers to disk Note: Empty sync buffers will not get flushed, to avoid writing extra buffer-lengths at the end of scan. 


### function reset

```
virtual void reset(
    bool force =false
)
```


**Reimplements**: [Gambit::Printers::BaseBasePrinter::reset](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-gambitprintersbasebaseprinter-reset)


Invalidate all data on disk which has been printed by this printer so far, and reset all the buffers to write back to the first data slots. This is only allowed if this is an auxilliary printer with global=true, or if "force=true" is specified. 


### function finalise

```
virtual void finalise(
    bool abnormal =false
)
```

Perform final cleanup and write tasks. 

**Reimplements**: [Gambit::Printers::BaseBasePrinter::finalise](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-gambitprintersbasebaseprinter-finalise)


Double-check that all the buffers are empty.

BEGIN DATA COMBINATION


### function resume_reader_options

```
virtual Options resume_reader_options()
```


**Reimplements**: [Gambit::Printers::BasePrinter::resume_reader_options](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/#function-gambitprintersbaseprinter-resume-reader-options)


### function _print

```
template <typename T >
inline void _print(
    T const & ,
    const std::string & label,
    const int vertexID,
    const uint,
    const ulong
)
```

Print functions. 

## Protected Attributes Documentation

### variable all_buffers

```
BaseBufferMap all_buffers;
```

Things which other printers need access to. 

Map containing pointers to all VertexBuffers, across all printers 


-------------------------------

Updated on 2022-09-08 at 02:00:49 +0000