---
title: "class Gambit::Printers::nonePrinter"

description: "[No description available]"

---

# class Gambit::Printers::nonePrinter



[No description available]

Inherits from [Gambit::Printers::BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/), [Gambit::Printers::BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual void | **[initialise](/documentation/code/classes/classgambit_1_1printers_1_1noneprinter/)**(const std::vector< int > & ) |
| virtual void | **[reset](/documentation/code/classes/classgambit_1_1printers_1_1noneprinter/)**(bool force)<br>Function to signal to the printer to write buffer contents to disk.  |
| virtual void | **[finalise](/documentation/code/classes/classgambit_1_1printers_1_1noneprinter/)**(bool abnormal)<br>Signal printer that scan is finished, and final output needs to be performed.  |
| virtual void | **[flush](/documentation/code/classes/classgambit_1_1printers_1_1noneprinter/)**() |
| virtual [Options](/documentation/code/classes/classgambit_1_1options/) | **[resume_reader_options](/documentation/code/classes/classgambit_1_1printers_1_1noneprinter/)**() |
| template <typename T \> <br>void | **[_print](/documentation/code/classes/classgambit_1_1printers_1_1noneprinter/)**(T const & , const std::string & label, const int vertexID, const uint, const ulong)<br>Print functions.  |
| | **[nonePrinter](/documentation/code/classes/classgambit_1_1printers_1_1noneprinter/)**(const [Options](/documentation/code/classes/classgambit_1_1options/) & options, [BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/) *const primary) |

## Additional inherited members

**Public Functions inherited from [Gambit::Printers::BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/)**

|                | Name           |
| -------------- | -------------- |
| | **[BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/)**() |
| | **[BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/)**([BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/) *const primary, bool is_aux_IN) |
| virtual | **[~BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/)**()<br>Destructor.  |
| void | **[set_as_aux](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/)**()<br>Set this as an auxilliary printer.  |
| virtual void | **[auxilliary_init](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/)**() |
| [BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/) * | **[get_primary_printer](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/)**() |
| bool | **[is_auxilliary_printer](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/)**() |
| template <typename T \> <br>void | **[print](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/)**(T const & in, const std::string & label, const int vertexID, const uint rank, const ulong pointID) |
| template <typename T \> <br>void | **[print](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/)**(T const & in, const std::string & label, const uint rank, const ulong pointID) |

**Public Functions inherited from [Gambit::Printers::BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**

|                | Name           |
| -------------- | -------------- |
| | **[BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**() |
| virtual | **[~BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**() |
| int | **[getRank](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**()<br>Retrieve/Set MPI rank (setting is useful for e.g. the postprocessor to re-print points from other ranks)  |
| void | **[setRank](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**(int r) |
| bool & | **[get_printUnitcube](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**() |
| void | **[set_printUnitcube](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**(const bool & rflag) |
| std::set< std::string > | **[getPrintList](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**() |
| void | **[setPrintList](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**(const std::set< std::string > & in) |
| void | **[addToPrintList](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**(const std::string & in) |
| bool | **[get_resume](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**() |
| void | **[set_resume](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**(bool rflag) |
| void | **[disable](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**(int n =-1) |
| void | **[enable](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**() |
| template <typename T \> <br>void | **[print](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**(T const & in, const std::string & label, const int vertexID, const uint rank, const ulong pointID) |
| template <typename T \> <br>void | **[print](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**(T const & in, const std::string & label, const uint rank, const ulong pointID) |

**Protected Attributes inherited from [Gambit::Printers::BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**

|                | Name           |
| -------------- | -------------- |
| bool | **[printer_enabled](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)** <br>Flag to check if print functions are enabled or disabled.  |
| int | **[printer_cooldown](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)** <br>Counter for printer cooldown. If non-zero printer can be disabled for a fixed number of print calls.  |


## Public Functions Documentation

### function initialise

```
inline virtual void initialise(
    const std::vector< int > & 
)
```


**Reimplements**: [Gambit::Printers::BasePrinter::initialise](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/)


Virtual function overloads: 


### function reset

```
inline virtual void reset(
    bool force
)
```

Function to signal to the printer to write buffer contents to disk. 

**Reimplements**: [Gambit::Printers::BaseBasePrinter::reset](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)


Signal printer to reset contents, i.e. delete old data in preperation for replacement 


### function finalise

```
inline virtual void finalise(
    bool abnormal
)
```

Signal printer that scan is finished, and final output needs to be performed. 

**Reimplements**: [Gambit::Printers::BaseBasePrinter::finalise](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)


### function flush

```
inline virtual void flush()
```


**Reimplements**: [Gambit::Printers::BasePrinter::flush](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/)


Signal printer to flush data in buffers to disk [Printers](/documentation/code/namespaces/namespacegambit_1_1printers/) should do this automatically as needed, but this is useful if a scanner is printing a bunch of data as a batch, to make sure it is all on disk after the batch is done. 


### function resume_reader_options

```
inline virtual Options resume_reader_options()
```


**Reimplements**: [Gambit::Printers::BasePrinter::resume_reader_options](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/)


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

### function nonePrinter

```
inline nonePrinter(
    const Options & options,
    BasePrinter *const primary
)
```


-------------------------------

Updated on 2022-09-08 at 01:05:18 +0000