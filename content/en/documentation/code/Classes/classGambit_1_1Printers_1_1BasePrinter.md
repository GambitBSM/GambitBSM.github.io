---
title: "class Gambit::Printers::BasePrinter"
description: "BASE PRINTER CLASS. "

---

# class Gambit::Printers::BasePrinter



BASE PRINTER CLASS. 


`#include <baseprinter.hpp>`

Inherits from [Gambit::Printers::BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)

Inherited by [Gambit::Printers::HDF5Printer](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer/), [Gambit::Printers::HDF5Printer2](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer2/), [Gambit::Printers::SQLitePrinter](/documentation/code/classes/classgambit_1_1printers_1_1sqliteprinter/), [Gambit::Printers::asciiPrinter](/documentation/code/classes/classgambit_1_1printers_1_1asciiprinter/), [Gambit::Printers::coutPrinter](/documentation/code/classes/classgambit_1_1printers_1_1coutprinter/), [Gambit::Printers::nonePrinter](/documentation/code/classes/classgambit_1_1printers_1_1noneprinter/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/)**() |
| | **[BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/)**([BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/) *const primary, bool is_aux_IN) |
| virtual | **[~BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/)**()<br>Destructor.  |
| virtual void | **[initialise](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/)**(const std::vector< int > & ) =0<br>Initialisation function.  |
| virtual void | **[flush](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/)**() =0 |
| virtual [Options](/documentation/code/classes/classgambit_1_1options/) | **[resume_reader_options](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/)**() =0 |
| void | **[set_as_aux](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/)**()<br>Set this as an auxilliary printer.  |
| virtual void | **[auxilliary_init](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/)**() |
| [BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/) * | **[get_primary_printer](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/)**() |
| bool | **[is_auxilliary_printer](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/)**() |
| template <typename T \> <br>void | **[print](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/)**(T const & in, const std::string & label, const int vertexID, const uint rank, const ulong pointID) |
| template <typename T \> <br>void | **[print](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/)**(T const & in, const std::string & label, const uint rank, const ulong pointID) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| template <typename T \> <br>void | **[_print](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/)**(T const & , const std::string & label, const int vertexID, const uint, const ulong) |

## Additional inherited members

**Public Functions inherited from [Gambit::Printers::BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**

|                | Name           |
| -------------- | -------------- |
| | **[BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**() |
| virtual | **[~BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**() |
| virtual void | **[reset](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**(bool force =false) =0<br>Function to signal to the printer to write buffer contents to disk.  |
| int | **[getRank](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**()<br>Retrieve/Set MPI rank (setting is useful for e.g. the postprocessor to re-print points from other ranks)  |
| void | **[setRank](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**(int r) |
| bool & | **[get_printUnitcube](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**() |
| void | **[set_printUnitcube](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**(const bool & rflag) |
| std::set< std::string > | **[getPrintList](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**() |
| void | **[setPrintList](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**(const std::set< std::string > & in) |
| void | **[addToPrintList](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**(const std::string & in) |
| bool | **[get_resume](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**() |
| void | **[set_resume](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**(bool rflag) |
| virtual void | **[finalise](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**(bool abnormal =false) =0<br>Signal printer that scan is finished, and final output needs to be performed.  |
| void | **[disable](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**(int n =-1) |
| void | **[enable](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**() |

**Protected Attributes inherited from [Gambit::Printers::BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**

|                | Name           |
| -------------- | -------------- |
| bool | **[printer_enabled](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)** <br>Flag to check if print functions are enabled or disabled.  |
| int | **[printer_cooldown](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)** <br>Counter for printer cooldown. If non-zero printer can be disabled for a fixed number of print calls.  |


## Public Functions Documentation

### function BasePrinter

```
inline BasePrinter()
```


### function BasePrinter

```
inline BasePrinter(
    BasePrinter *const primary,
    bool is_aux_IN
)
```


### function ~BasePrinter

```
inline virtual ~BasePrinter()
```

Destructor. 

### function initialise

```
virtual void initialise(
    const std::vector< int > & 
) =0
```

Initialisation function. 

**Reimplemented by**: [Gambit::Printers::asciiPrinter::initialise](/documentation/code/classes/classgambit_1_1printers_1_1asciiprinter/), [Gambit::Printers::coutPrinter::initialise](/documentation/code/classes/classgambit_1_1printers_1_1coutprinter/), [Gambit::Printers::HDF5Printer::initialise](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer/), [Gambit::Printers::HDF5Printer2::initialise](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer2/), [Gambit::Printers::nonePrinter::initialise](/documentation/code/classes/classgambit_1_1printers_1_1noneprinter/), [Gambit::Printers::SQLitePrinter::initialise](/documentation/code/classes/classgambit_1_1printers_1_1sqliteprinter/)


### function flush

```
virtual void flush() =0
```


**Reimplements**: [Gambit::Printers::BaseBasePrinter::flush](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)


**Reimplemented by**: [Gambit::Printers::asciiPrinter::flush](/documentation/code/classes/classgambit_1_1printers_1_1asciiprinter/), [Gambit::Printers::coutPrinter::flush](/documentation/code/classes/classgambit_1_1printers_1_1coutprinter/), [Gambit::Printers::HDF5Printer::flush](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer/), [Gambit::Printers::HDF5Printer2::flush](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer2/), [Gambit::Printers::nonePrinter::flush](/documentation/code/classes/classgambit_1_1printers_1_1noneprinter/), [Gambit::Printers::SQLitePrinter::flush](/documentation/code/classes/classgambit_1_1printers_1_1sqliteprinter/)


Signal printer to flush data in buffers to disk [Printers](/documentation/code/namespaces/namespacegambit_1_1printers/) should do this automatically as needed, but this is useful if a scanner is printing a bunch of data as a batch, to make sure it is all on disk after the batch is done. 


### function resume_reader_options

```
virtual Options resume_reader_options() =0
```


**Reimplements**: [Gambit::Printers::BaseBasePrinter::resume_reader_options](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)


**Reimplemented by**: [Gambit::Printers::asciiPrinter::resume_reader_options](/documentation/code/classes/classgambit_1_1printers_1_1asciiprinter/), [Gambit::Printers::coutPrinter::resume_reader_options](/documentation/code/classes/classgambit_1_1printers_1_1coutprinter/), [Gambit::Printers::HDF5Printer::resume_reader_options](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer/), [Gambit::Printers::HDF5Printer2::resume_reader_options](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer2/), [Gambit::Printers::nonePrinter::resume_reader_options](/documentation/code/classes/classgambit_1_1printers_1_1noneprinter/), [Gambit::Printers::SQLitePrinter::resume_reader_options](/documentation/code/classes/classgambit_1_1printers_1_1sqliteprinter/)


### function set_as_aux

```
inline void set_as_aux()
```

Set this as an auxilliary printer. 

### function auxilliary_init

```
inline virtual void auxilliary_init()
```


Helper initialisation for auxilliary printers Will be run when the auxilliary printer is created by a [PrinterManager](/documentation/code/classes/classgambit_1_1printers_1_1printermanager/). Define override of this if two-stage initialisation is needed 


### function get_primary_printer

```
inline BasePrinter * get_primary_printer()
```


### function is_auxilliary_printer

```
inline bool is_auxilliary_printer()
```


### function print

```
template <typename T >
inline void print(
    T const & in,
    const std::string & label,
    const int vertexID,
    const uint rank,
    const ulong pointID
)
```


### function print

```
template <typename T >
inline void print(
    T const & in,
    const std::string & label,
    const uint rank,
    const ulong pointID
)
```


## Protected Functions Documentation

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


Default _print function. Throws an error if no matching virtual function for the type of the attempted print is found. 


-------------------------------

Updated on 2022-09-08 at 01:05:18 +0000