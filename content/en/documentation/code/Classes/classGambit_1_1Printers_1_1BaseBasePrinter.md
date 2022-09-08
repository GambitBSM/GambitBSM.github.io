---
title: "class Gambit::Printers::BaseBasePrinter"

description: "[No description available]"

---

# class Gambit::Printers::BaseBasePrinter



[No description available]

Inherited by [Gambit::Printers::BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**() |
| virtual | **[~BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**() |
| virtual void | **[reset](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**(bool force =false) =0<br>Function to signal to the printer to write buffer contents to disk.  |
| virtual void | **[flush](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**() =0 |
| int | **[getRank](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**()<br>Retrieve/Set MPI rank (setting is useful for e.g. the postprocessor to re-print points from other ranks)  |
| void | **[setRank](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**(int r) |
| bool & | **[get_printUnitcube](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**() |
| void | **[set_printUnitcube](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**(const bool & rflag) |
| std::set< std::string > | **[getPrintList](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**() |
| void | **[setPrintList](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**(const std::set< std::string > & in) |
| void | **[addToPrintList](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**(const std::string & in) |
| virtual [Options](/documentation/code/classes/classgambit_1_1options/) | **[resume_reader_options](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**() =0 |
| bool | **[get_resume](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**() |
| void | **[set_resume](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**(bool rflag) |
| virtual void | **[finalise](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**(bool abnormal =false) =0<br>Signal printer that scan is finished, and final output needs to be performed.  |
| void | **[disable](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**(int n =-1) |
| void | **[enable](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**() |
| template <typename T \> <br>void | **[print](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**(T const & in, const std::string & label, const int vertexID, const uint rank, const ulong pointID) |
| template <typename T \> <br>void | **[print](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**(T const & in, const std::string & label, const uint rank, const ulong pointID) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| template <typename T \> <br>void | **[_print](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**(T const & , const std::string & label, const int vertexID, const uint, const ulong) |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| bool | **[printer_enabled](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)** <br>Flag to check if print functions are enabled or disabled.  |
| int | **[printer_cooldown](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)** <br>Counter for printer cooldown. If non-zero printer can be disabled for a fixed number of print calls.  |

## Public Functions Documentation

### function BaseBasePrinter

```
inline BaseBasePrinter()
```


### function ~BaseBasePrinter

```
inline virtual ~BaseBasePrinter()
```


### function reset

```
virtual void reset(
    bool force =false
) =0
```

Function to signal to the printer to write buffer contents to disk. 

**Reimplemented by**: [Gambit::Printers::asciiPrinter::reset](/documentation/code/classes/classgambit_1_1printers_1_1asciiprinter/), [Gambit::Printers::coutPrinter::reset](/documentation/code/classes/classgambit_1_1printers_1_1coutprinter/), [Gambit::Printers::HDF5Printer::reset](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer/), [Gambit::Printers::HDF5Printer2::reset](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer2/), [Gambit::Printers::SQLitePrinter::reset](/documentation/code/classes/classgambit_1_1printers_1_1sqliteprinter/), [Gambit::Printers::nonePrinter::reset](/documentation/code/classes/classgambit_1_1printers_1_1noneprinter/)


Signal printer to reset contents, i.e. delete old data in preperation for replacement 


### function flush

```
virtual void flush() =0
```


**Reimplemented by**: [Gambit::Printers::asciiPrinter::flush](/documentation/code/classes/classgambit_1_1printers_1_1asciiprinter/), [Gambit::Printers::coutPrinter::flush](/documentation/code/classes/classgambit_1_1printers_1_1coutprinter/), [Gambit::Printers::HDF5Printer::flush](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer/), [Gambit::Printers::HDF5Printer2::flush](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer2/), [Gambit::Printers::nonePrinter::flush](/documentation/code/classes/classgambit_1_1printers_1_1noneprinter/), [Gambit::Printers::SQLitePrinter::flush](/documentation/code/classes/classgambit_1_1printers_1_1sqliteprinter/), [Gambit::Printers::BasePrinter::flush](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/)


Signal printer to flush data in buffers to disk [Printers](/documentation/code/namespaces/namespacegambit_1_1printers/) should do this automatically as needed, but this is useful if a scanner is printing a bunch of data as a batch, to make sure it is all on disk after the batch is done. 


### function getRank

```
inline int getRank()
```

Retrieve/Set MPI rank (setting is useful for e.g. the postprocessor to re-print points from other ranks) 

### function setRank

```
inline void setRank(
    int r
)
```


### function get_printUnitcube

```
inline bool & get_printUnitcube()
```


### function set_printUnitcube

```
inline void set_printUnitcube(
    const bool & rflag
)
```


### function getPrintList

```
inline std::set< std::string > getPrintList()
```


Retrieve/Set print list for this printer Required by e.g. postprocessor. 


### function setPrintList

```
inline void setPrintList(
    const std::set< std::string > & in
)
```


### function addToPrintList

```
inline void addToPrintList(
    const std::string & in
)
```


### function resume_reader_options

```
virtual Options resume_reader_options() =0
```


**Reimplemented by**: [Gambit::Printers::asciiPrinter::resume_reader_options](/documentation/code/classes/classgambit_1_1printers_1_1asciiprinter/), [Gambit::Printers::coutPrinter::resume_reader_options](/documentation/code/classes/classgambit_1_1printers_1_1coutprinter/), [Gambit::Printers::HDF5Printer::resume_reader_options](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer/), [Gambit::Printers::HDF5Printer2::resume_reader_options](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer2/), [Gambit::Printers::nonePrinter::resume_reader_options](/documentation/code/classes/classgambit_1_1printers_1_1noneprinter/), [Gambit::Printers::SQLitePrinter::resume_reader_options](/documentation/code/classes/classgambit_1_1printers_1_1sqliteprinter/), [Gambit::Printers::BasePrinter::resume_reader_options](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/)


### function get_resume

```
inline bool get_resume()
```


### function set_resume

```
inline void set_resume(
    bool rflag
)
```


### function finalise

```
virtual void finalise(
    bool abnormal =false
) =0
```

Signal printer that scan is finished, and final output needs to be performed. 

**Reimplemented by**: [Gambit::Printers::asciiPrinter::finalise](/documentation/code/classes/classgambit_1_1printers_1_1asciiprinter/), [Gambit::Printers::coutPrinter::finalise](/documentation/code/classes/classgambit_1_1printers_1_1coutprinter/), [Gambit::Printers::HDF5Printer::finalise](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer/), [Gambit::Printers::HDF5Printer2::finalise](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer2/), [Gambit::Printers::SQLitePrinter::finalise](/documentation/code/classes/classgambit_1_1printers_1_1sqliteprinter/), [Gambit::Printers::nonePrinter::finalise](/documentation/code/classes/classgambit_1_1printers_1_1noneprinter/)


### function disable

```
inline void disable(
    int n =-1
)
```


"Turn off" printer; i.e. calls to print functions will do nothing while this is active Optionally, disable printer just for the next n print calls unless it was already disabled 


### function enable

```
inline void enable()
```


"Turn on" printer; print calls will work as normal. Reset cooldown 


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


## Protected Attributes Documentation

### variable printer_enabled

```
bool printer_enabled;
```

Flag to check if print functions are enabled or disabled. 

### variable printer_cooldown

```
int printer_cooldown;
```

Counter for printer cooldown. If non-zero printer can be disabled for a fixed number of print calls. 

-------------------------------

Updated on 2022-09-08 at 01:05:18 +0000