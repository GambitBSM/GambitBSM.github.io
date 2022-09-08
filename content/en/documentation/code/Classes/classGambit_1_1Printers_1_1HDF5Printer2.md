---
title: "class Gambit::Printers::HDF5Printer2"
description: "The main printer class for output to HDF5 format. "

---

# class Gambit::Printers::HDF5Printer2



The main printer class for output to HDF5 format. 


`#include <hdf5printer_v2.hpp>`

Inherits from [Gambit::Printers::BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/), [Gambit::Printers::BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[HDF5Printer2](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer2/#function-gambitprintershdf5printer2-hdf5printer2)**(const [Options](/documentation/code/classes/classgambit_1_1options/) & options, [BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/) *const primary =NULL)<br>Constructor (for construction via inifile options)  |
| | **[~HDF5Printer2](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer2/#function-gambitprintershdf5printer2-hdf5printer2)**()<br>Destructor.  |
| std::string | **[get_filename](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer2/#function-gambitprintershdf5printer2-get-filename)**()<br>Report name (inc. path) of output file.  |
| std::string | **[get_groupname](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer2/#function-gambitprintershdf5printer2-get-groupname)**()<br>Report group in output HDF5 file of output datasets.  |
| std::size_t | **[get_buffer_length](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer2/#function-gambitprintershdf5printer2-get-buffer-length)**()<br>Report length of buffer for HDF5 output.  |
| void | **[add_aux_buffer](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer2/#function-gambitprintershdf5printer2-add-aux-buffer)**([HDF5MasterBuffer](/documentation/code/classes/classgambit_1_1printers_1_1hdf5masterbuffer/) & aux_buffermaster)<br>Add buffer to the primary printers records.  |
| [HDF5Printer2](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer2/) * | **[get_HDF5_primary_printer](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer2/#function-gambitprintershdf5printer2-get-hdf5-primary-printer)**() |
| virtual void | **[initialise](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer2/#function-gambitprintershdf5printer2-initialise)**(const std::vector< int > & ) |
| virtual void | **[flush](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer2/#function-gambitprintershdf5printer2-flush)**() |
| virtual void | **[reset](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer2/#function-gambitprintershdf5printer2-reset)**(bool force =false)<br>Function to signal to the printer to write buffer contents to disk.  |
| virtual void | **[finalise](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer2/#function-gambitprintershdf5printer2-finalise)**(bool abnormal =false)<br>Signal printer that scan is finished, and final output needs to be performed.  |
| virtual [Options](/documentation/code/classes/classgambit_1_1options/) | **[resume_reader_options](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer2/#function-gambitprintershdf5printer2-resume-reader-options)**() |
| template <typename T \> <br>void | **[_print](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer2/#function-gambitprintershdf5printer2-print)**(T const & , const std::string & label, const int vertexID, const uint, const ulong)<br>Print functions.  |

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

### function HDF5Printer2

```
HDF5Printer2(
    const Options & options,
    BasePrinter *const primary =NULL
)
```

Constructor (for construction via inifile options) 

Constructor. 


Check if combined output file exists


### function ~HDF5Printer2

```
~HDF5Printer2()
```

Destructor. 

### function get_filename

```
std::string get_filename()
```

Report name (inc. path) of output file. 

### function get_groupname

```
std::string get_groupname()
```

Report group in output HDF5 file of output datasets. 

### function get_buffer_length

```
std::size_t get_buffer_length()
```

Report length of buffer for HDF5 output. 

### function add_aux_buffer

```
void add_aux_buffer(
    HDF5MasterBuffer & aux_buffermaster
)
```

Add buffer to the primary printers records. 

### function get_HDF5_primary_printer

```
HDF5Printer2 * get_HDF5_primary_printer()
```


Get pointer to primary printer of this class type (get_primary_printer returns a pointer-to-base) 


### function initialise

```
virtual void initialise(
    const std::vector< int > & 
)
```


**Reimplements**: [Gambit::Printers::BasePrinter::initialise](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/#function-gambitprintersbaseprinter-initialise)


Base class virtual function overloads (the public virtual interface) 


### function flush

```
virtual void flush()
```


**Reimplements**: [Gambit::Printers::BasePrinter::flush](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/#function-gambitprintersbaseprinter-flush)


Signal printer to flush data in buffers to disk [Printers](/documentation/code/namespaces/namespacegambit_1_1printers/) should do this automatically as needed, but this is useful if a scanner is printing a bunch of data as a batch, to make sure it is all on disk after the batch is done. 


### function reset

```
virtual void reset(
    bool force =false
)
```

Function to signal to the printer to write buffer contents to disk. 

**Reimplements**: [Gambit::Printers::BaseBasePrinter::reset](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-gambitprintersbasebaseprinter-reset)


Signal printer to reset contents, i.e. delete old data in preperation for replacement 


### function finalise

```
virtual void finalise(
    bool abnormal =false
)
```

Signal printer that scan is finished, and final output needs to be performed. 

**Reimplements**: [Gambit::Printers::BaseBasePrinter::finalise](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-gambitprintersbasebaseprinter-finalise)


Need to finalise output of the sync buffers for all printers before we do the RA buffers.

Need to know final nominal dataset size to ensure unsynchronised datasets match synchronised ones.


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

-------------------------------

Updated on 2022-09-08 at 01:48:56 +0000