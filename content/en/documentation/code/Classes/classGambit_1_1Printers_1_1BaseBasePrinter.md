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
| | **[BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-basebaseprinter)**() |
| virtual | **[~BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-basebaseprinter)**() |
| virtual void | **[reset](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-reset)**(bool force =false) =0<br>Function to signal to the printer to write buffer contents to disk.  |
| virtual void | **[flush](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-flush)**() =0 |
| int | **[getRank](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-getrank)**()<br>Retrieve/Set MPI rank (setting is useful for e.g. the postprocessor to re-print points from other ranks)  |
| void | **[setRank](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-setrank)**(int r) |
| bool & | **[get_printUnitcube](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-get-printunitcube)**() |
| void | **[set_printUnitcube](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-set-printunitcube)**(const bool & rflag) |
| std::set< std::string > | **[getPrintList](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-getprintlist)**() |
| void | **[setPrintList](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-setprintlist)**(const std::set< std::string > & in) |
| void | **[addToPrintList](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-addtoprintlist)**(const std::string & in) |
| virtual [Options](/documentation/code/classes/classgambit_1_1options/) | **[resume_reader_options](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-resume-reader-options)**() =0 |
| bool | **[get_resume](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-get-resume)**() |
| void | **[set_resume](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-set-resume)**(bool rflag) |
| virtual void | **[finalise](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-finalise)**(bool abnormal =false) =0<br>Signal printer that scan is finished, and final output needs to be performed.  |
| void | **[disable](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-disable)**(int n =-1) |
| void | **[enable](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-enable)**() |
| template <typename T \> <br>void | **[print](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-print)**(T const & in, const std::string & label, const int vertexID, const uint rank, const ulong pointID) |
| template <typename T \> <br>void | **[print](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-print)**(T const & in, const std::string & label, const uint rank, const ulong pointID) |
| void | **[print_metadata](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-print-metadata)**([map_str_str](/documentation/code/namespaces/namespacegambit/#typedef-map-str-str) datasets) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| template <typename T \> <br>void | **[_print](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-print)**(T const & , const std::string & label, const int vertexID, const uint, const ulong) |
| template <typename T \> <br>void | **[_print](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-print)**(T const & in, const std::string & label, const uint rank, const ulong pointID)<br>Same for overloaded function.  |
| virtual void | **[_print_metadata](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-print-metadata)**([map_str_str](/documentation/code/namespaces/namespacegambit/#typedef-map-str-str) ) |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| bool | **[printer_enabled](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#variable-printer-enabled)** <br>Flag to check if print functions are enabled or disabled.  |
| int | **[printer_cooldown](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#variable-printer-cooldown)** <br>Counter for printer cooldown. If non-zero printer can be disabled for a fixed number of print calls.  |

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

**Reimplemented by**: [Gambit::Printers::asciiPrinter::reset](/documentation/code/classes/classgambit_1_1printers_1_1asciiprinter/#function-reset), [Gambit::Printers::coutPrinter::reset](/documentation/code/classes/classgambit_1_1printers_1_1coutprinter/#function-reset), [Gambit::Printers::HDF5Printer::reset](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer/#function-reset), [Gambit::Printers::HDF5Printer2::reset](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer2/#function-reset), [Gambit::Printers::SQLitePrinter::reset](/documentation/code/classes/classgambit_1_1printers_1_1sqliteprinter/#function-reset), [Gambit::Printers::nonePrinter::reset](/documentation/code/classes/classgambit_1_1printers_1_1noneprinter/#function-reset)


Signal printer to reset contents, i.e. delete old data in preperation for replacement 


### function flush

```
virtual void flush() =0
```


**Reimplemented by**: [Gambit::Printers::asciiPrinter::flush](/documentation/code/classes/classgambit_1_1printers_1_1asciiprinter/#function-flush), [Gambit::Printers::coutPrinter::flush](/documentation/code/classes/classgambit_1_1printers_1_1coutprinter/#function-flush), [Gambit::Printers::HDF5Printer::flush](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer/#function-flush), [Gambit::Printers::HDF5Printer2::flush](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer2/#function-flush), [Gambit::Printers::nonePrinter::flush](/documentation/code/classes/classgambit_1_1printers_1_1noneprinter/#function-flush), [Gambit::Printers::SQLitePrinter::flush](/documentation/code/classes/classgambit_1_1printers_1_1sqliteprinter/#function-flush), [Gambit::Printers::BasePrinter::flush](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/#function-flush)


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


**Reimplemented by**: [Gambit::Printers::asciiPrinter::resume_reader_options](/documentation/code/classes/classgambit_1_1printers_1_1asciiprinter/#function-resume-reader-options), [Gambit::Printers::coutPrinter::resume_reader_options](/documentation/code/classes/classgambit_1_1printers_1_1coutprinter/#function-resume-reader-options), [Gambit::Printers::HDF5Printer::resume_reader_options](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer/#function-resume-reader-options), [Gambit::Printers::HDF5Printer2::resume_reader_options](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer2/#function-resume-reader-options), [Gambit::Printers::nonePrinter::resume_reader_options](/documentation/code/classes/classgambit_1_1printers_1_1noneprinter/#function-resume-reader-options), [Gambit::Printers::SQLitePrinter::resume_reader_options](/documentation/code/classes/classgambit_1_1printers_1_1sqliteprinter/#function-resume-reader-options), [Gambit::Printers::BasePrinter::resume_reader_options](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/#function-resume-reader-options)


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

**Reimplemented by**: [Gambit::Printers::asciiPrinter::finalise](/documentation/code/classes/classgambit_1_1printers_1_1asciiprinter/#function-finalise), [Gambit::Printers::coutPrinter::finalise](/documentation/code/classes/classgambit_1_1printers_1_1coutprinter/#function-finalise), [Gambit::Printers::HDF5Printer::finalise](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer/#function-finalise), [Gambit::Printers::HDF5Printer2::finalise](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer2/#function-finalise), [Gambit::Printers::SQLitePrinter::finalise](/documentation/code/classes/classgambit_1_1printers_1_1sqliteprinter/#function-finalise), [Gambit::Printers::nonePrinter::finalise](/documentation/code/classes/classgambit_1_1printers_1_1noneprinter/#function-finalise)


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


### function print_metadata

```
inline void print_metadata(
    map_str_str datasets
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


### function _print

```
template <typename T >
inline void _print(
    T const & in,
    const std::string & label,
    const uint rank,
    const ulong pointID
)
```

Same for overloaded function. 

### function _print_metadata

```
inline virtual void _print_metadata(
    map_str_str 
)
```


**Reimplemented by**: [Gambit::Printers::asciiPrinter::_print_metadata](/documentation/code/classes/classgambit_1_1printers_1_1asciiprinter/#function-print-metadata), [Gambit::Printers::coutPrinter::_print_metadata](/documentation/code/classes/classgambit_1_1printers_1_1coutprinter/#function-print-metadata), [Gambit::Printers::HDF5Printer::_print_metadata](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer/#function-print-metadata), [Gambit::Printers::HDF5Printer2::_print_metadata](/documentation/code/classes/classgambit_1_1printers_1_1hdf5printer2/#function-print-metadata), [Gambit::Printers::nonePrinter::_print_metadata](/documentation/code/classes/classgambit_1_1printers_1_1noneprinter/#function-print-metadata), [Gambit::Printers::SQLitePrinter::_print_metadata](/documentation/code/classes/classgambit_1_1printers_1_1sqliteprinter/#function-print-metadata)


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

Updated on 2023-06-26 at 21:36:52 +0000