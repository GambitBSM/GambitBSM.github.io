---
title: "class Gambit::Printers::coutPrinter"

description: "[No description available]"

---

# class Gambit::Printers::coutPrinter



[No description available]

Inherits from [Gambit::Printers::BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/), [Gambit::Printers::BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual void | **[initialise](/documentation/code/classes/classgambit_1_1printers_1_1coutprinter/#function-initialise)**(const std::vector< int > & )<br>Initialisation function.  |
| virtual void | **[reset](/documentation/code/classes/classgambit_1_1printers_1_1coutprinter/#function-reset)**(bool force =false)<br>Reset printer and output to clean state.  |
| virtual void | **[finalise](/documentation/code/classes/classgambit_1_1printers_1_1coutprinter/#function-finalise)**(bool abnormal =false)<br>Do final buffer dumps.  |
| virtual void | **[flush](/documentation/code/classes/classgambit_1_1printers_1_1coutprinter/#function-flush)**() |
| virtual [Options](/documentation/code/classes/classgambit_1_1options/) | **[resume_reader_options](/documentation/code/classes/classgambit_1_1printers_1_1coutprinter/#function-resume-reader-options)**()<br>Permanently unavailable for this printer.  |
| void | **[check_point](/documentation/code/classes/classgambit_1_1printers_1_1coutprinter/#function-check-point)**(unsigned int mpirank, unsigned long pointID)<br>[coutPrinter](/documentation/code/classes/classgambit_1_1printers_1_1coutprinter/) specific functions  |
| virtual void | **[_print_metadata](/documentation/code/classes/classgambit_1_1printers_1_1coutprinter/#function-print-metadata)**([map_str_str](/documentation/code/namespaces/namespacegambit/#typedef-map-str-str) ) |
| template <typename T \> <br>void | **[_print](/documentation/code/classes/classgambit_1_1printers_1_1coutprinter/#function-print)**(T const & , const std::string & label, const int vertexID, const uint, const ulong)<br>Print functions.  |
| template <typename T \> <br>void | **[_print](/documentation/code/classes/classgambit_1_1printers_1_1coutprinter/#function-print)**(T const & in, const std::string & label, const uint rank, const ulong pointID)<br>Print functions.  |
| | **[coutPrinter](/documentation/code/classes/classgambit_1_1printers_1_1coutprinter/#function-coutprinter)**(const [Options](/documentation/code/classes/classgambit_1_1options/) & options, [BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/) *const primary =NULL)<br>Constructor (for construction via inifile options)  |
| void | **[common_constructor](/documentation/code/classes/classgambit_1_1printers_1_1coutprinter/#function-common-constructor)**(const [Options](/documentation/code/classes/classgambit_1_1options/) & )<br>Tasks common to the various constructors.  |
| template <class T \> <br>void | **[template_print](/documentation/code/classes/classgambit_1_1printers_1_1coutprinter/#function-template-print)**(T const & value, const std::string & label, const int , const unsigned int mpirank, const unsigned long pointID)<br>Helper print functions.  |

## Additional inherited members

**Public Functions inherited from [Gambit::Printers::BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/)**

|                | Name           |
| -------------- | -------------- |
| | **[BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/#function-baseprinter)**() |
| | **[BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/#function-baseprinter)**([BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/) *const primary, bool is_aux_IN) |
| virtual | **[~BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/#function-baseprinter)**()<br>Destructor.  |
| void | **[set_as_aux](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/#function-set-as-aux)**()<br>Set this as an auxilliary printer.  |
| void | **[set_output_metadata](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/#function-set-output-metadata)**(bool use_metadata)<br>Set/Get whether to print the metadata.  |
| bool | **[get_output_metadata](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/#function-get-output-metadata)**() |
| virtual void | **[auxilliary_init](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/#function-auxilliary-init)**() |
| [BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/) * | **[get_primary_printer](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/#function-get-primary-printer)**() |
| bool | **[is_auxilliary_printer](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/#function-is-auxilliary-printer)**() |
| template <typename T \> <br>void | **[print](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/#function-print)**(T const & in, const std::string & label, const int vertexID, const uint rank, const ulong pointID) |
| template <typename T \> <br>void | **[print](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/#function-print)**(T const & in, const std::string & label, const uint rank, const ulong pointID) |

**Public Functions inherited from [Gambit::Printers::BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**

|                | Name           |
| -------------- | -------------- |
| | **[BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-basebaseprinter)**() |
| virtual | **[~BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-basebaseprinter)**() |
| int | **[getRank](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-getrank)**()<br>Retrieve/Set MPI rank (setting is useful for e.g. the postprocessor to re-print points from other ranks)  |
| void | **[setRank](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-setrank)**(int r) |
| bool & | **[get_printUnitcube](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-get-printunitcube)**() |
| void | **[set_printUnitcube](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-set-printunitcube)**(const bool & rflag) |
| std::set< std::string > | **[getPrintList](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-getprintlist)**() |
| void | **[setPrintList](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-setprintlist)**(const std::set< std::string > & in) |
| void | **[addToPrintList](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-addtoprintlist)**(const std::string & in) |
| bool | **[get_resume](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-get-resume)**() |
| void | **[set_resume](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-set-resume)**(bool rflag) |
| void | **[disable](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-disable)**(int n =-1) |
| void | **[enable](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-enable)**() |
| template <typename T \> <br>void | **[print](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-print)**(T const & in, const std::string & label, const int vertexID, const uint rank, const ulong pointID) |
| template <typename T \> <br>void | **[print](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-print)**(T const & in, const std::string & label, const uint rank, const ulong pointID) |
| void | **[print_metadata](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-print-metadata)**([map_str_str](/documentation/code/namespaces/namespacegambit/#typedef-map-str-str) datasets) |

**Protected Attributes inherited from [Gambit::Printers::BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)**

|                | Name           |
| -------------- | -------------- |
| bool | **[printer_enabled](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#variable-printer-enabled)** <br>Flag to check if print functions are enabled or disabled.  |
| int | **[printer_cooldown](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#variable-printer-cooldown)** <br>Counter for printer cooldown. If non-zero printer can be disabled for a fixed number of print calls.  |


## Public Functions Documentation

### function initialise

```
virtual void initialise(
    const std::vector< int > & 
)
```

Initialisation function. 

**Reimplements**: [Gambit::Printers::BasePrinter::initialise](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/#function-initialise)


Virtual function overloads: 


### function reset

```
virtual void reset(
    bool force =false
)
```

Reset printer and output to clean state. 

**Reimplements**: [Gambit::Printers::BaseBasePrinter::reset](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-reset)


### function finalise

```
virtual void finalise(
    bool abnormal =false
)
```

Do final buffer dumps. 

**Reimplements**: [Gambit::Printers::BaseBasePrinter::finalise](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-finalise)


### function flush

```
inline virtual void flush()
```


**Reimplements**: [Gambit::Printers::BasePrinter::flush](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/#function-flush)


Signal printer to flush data in buffers to disk [Printers](/documentation/code/namespaces/namespacegambit_1_1printers/) should do this automatically as needed, but this is useful if a scanner is printing a bunch of data as a batch, to make sure it is all on disk after the batch is done. 


### function resume_reader_options

```
virtual Options resume_reader_options()
```

Permanently unavailable for this printer. 

**Reimplements**: [Gambit::Printers::BasePrinter::resume_reader_options](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/#function-resume-reader-options)


### function check_point

```
void check_point(
    unsigned int mpirank,
    unsigned long pointID
)
```

[coutPrinter](/documentation/code/classes/classgambit_1_1printers_1_1coutprinter/) specific functions 

Perform any point-specific logic.

Perform any point-specific logic 


### function _print_metadata

```
inline virtual void _print_metadata(
    map_str_str 
)
```


**Reimplements**: [Gambit::Printers::BaseBasePrinter::_print_metadata](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-print-metadata)


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

Print functions. 

### function coutPrinter

```
coutPrinter(
    const Options & options,
    BasePrinter *const primary =NULL
)
```

Constructor (for construction via inifile options) 

### function common_constructor

```
void common_constructor(
    const Options & 
)
```

Tasks common to the various constructors. 

### function template_print

```
template <class T >
inline void template_print(
    T const & value,
    const std::string & label,
    const int ,
    const unsigned int mpirank,
    const unsigned long pointID
)
```

Helper print functions. 

-------------------------------

Updated on 2024-07-18 at 13:53:32 +0000