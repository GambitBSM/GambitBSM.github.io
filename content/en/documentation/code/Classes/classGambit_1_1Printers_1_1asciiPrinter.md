---
title: "class Gambit::Printers::asciiPrinter"

description: "[No description available]"

---

# class Gambit::Printers::asciiPrinter



[No description available]

Inherits from [Gambit::Printers::BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/), [Gambit::Printers::BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual void | **[initialise](/documentation/code/classes/classgambit_1_1printers_1_1asciiprinter/#function-initialise)**(const std::vector< int > & )<br>Initialisation function.  |
| virtual void | **[reset](/documentation/code/classes/classgambit_1_1printers_1_1asciiprinter/#function-reset)**(bool force =false)<br>Delete contents of output file (to be replaced/updated) and erase everything in the buffer.  |
| virtual void | **[finalise](/documentation/code/classes/classgambit_1_1printers_1_1asciiprinter/#function-finalise)**(bool abnormal =false)<br>Do final buffer dumps.  |
| virtual void | **[flush](/documentation/code/classes/classgambit_1_1printers_1_1asciiprinter/#function-flush)**() |
| virtual [Options](/documentation/code/classes/classgambit_1_1options/) | **[resume_reader_options](/documentation/code/classes/classgambit_1_1printers_1_1asciiprinter/#function-resume-reader-options)**() |
| virtual void | **[_print_metadata](/documentation/code/classes/classgambit_1_1printers_1_1asciiprinter/#function-print-metadata)**([map_str_str](/documentation/code/namespaces/namespacegambit/#typedef-map-str-str) metadata) |
| template <typename T \> <br>void | **[_print](/documentation/code/classes/classgambit_1_1printers_1_1asciiprinter/#function-print)**(T const & , const std::string & label, const int vertexID, const uint, const ulong)<br>Print functions.  |
| template <typename T \> <br>void | **[_print](/documentation/code/classes/classgambit_1_1printers_1_1asciiprinter/#function-print)**(T const & in, const std::string & label, const uint rank, const ulong pointID)<br>Print functions.  |
| template <class T \> <br>void | **[template_print](/documentation/code/classes/classgambit_1_1printers_1_1asciiprinter/#function-template-print)**(T const & value, const std::string & label, const int IDcode, const uint, const ulong)<br>Helper print functions.  |
| template <class T \> <br>void | **[template_print_vec](/documentation/code/classes/classgambit_1_1printers_1_1asciiprinter/#function-template-print-vec)**(std::vector< T > const & value, const std::string & label, const int IDcode, const uint, const ulong)<br>Template for print functions of vectors of "simple" types.  |
| | **[asciiPrinter](/documentation/code/classes/classgambit_1_1printers_1_1asciiprinter/#function-asciiprinter)**(const [Options](/documentation/code/classes/classgambit_1_1options/) & options, [BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/) *const primary =NULL)<br>TODO: proper gambit error.  |
| void | **[common_constructor](/documentation/code/classes/classgambit_1_1printers_1_1asciiprinter/#function-common-constructor)**(const [Options](/documentation/code/classes/classgambit_1_1options/) & options)<br>Tasks common to the various constructors.  |
| | **[~asciiPrinter](/documentation/code/classes/classgambit_1_1printers_1_1asciiprinter/#function-asciiprinter)**()<br>Destructor.  |
| void | **[erase_buffer](/documentation/code/classes/classgambit_1_1printers_1_1asciiprinter/#function-erase-buffer)**()<br>Asciiprinter-specific functions.  |
| void | **[endline](/documentation/code/classes/classgambit_1_1printers_1_1asciiprinter/#function-endline)**() |
| void | **[addtobuffer](/documentation/code/classes/classgambit_1_1printers_1_1asciiprinter/#function-addtobuffer)**(const std::vector< double > & functor_data, const std::vector< std::string > & functor_labels, const int vID, const int rank, const int pointID) |
| void | **[dump_buffer](/documentation/code/classes/classgambit_1_1printers_1_1asciiprinter/#function-dump-buffer)**(bool force =false) |
| std::string | **[get_output_filename](/documentation/code/classes/classgambit_1_1printers_1_1asciiprinter/#function-get-output-filename)**() |
| int | **[get_bufferlength](/documentation/code/classes/classgambit_1_1printers_1_1asciiprinter/#function-get-bufferlength)**() |

## Additional inherited members

**Public Functions inherited from [Gambit::Printers::BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/)**

|                | Name           |
| -------------- | -------------- |
| | **[BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/#function-baseprinter)**() |
| | **[BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/#function-baseprinter)**([BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/) *const primary, bool is_aux_IN) |
| virtual | **[~BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/#function-baseprinter)**()<br>Destructor.  |
| void | **[set_as_aux](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/#function-set-as-aux)**()<br>Set this as an auxilliary printer.  |
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

Delete contents of output file (to be replaced/updated) and erase everything in the buffer. 

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
virtual void flush()
```


**Reimplements**: [Gambit::Printers::BasePrinter::flush](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/#function-flush)


Signal printer to flush data in buffers to disk [Printers](/documentation/code/namespaces/namespacegambit_1_1printers/) should do this automatically as needed, but this is useful if a scanner is printing a bunch of data as a batch, to make sure it is all on disk after the batch is done. 


### function resume_reader_options

```
virtual Options resume_reader_options()
```


**Reimplements**: [Gambit::Printers::BasePrinter::resume_reader_options](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/#function-resume-reader-options)


### function _print_metadata

```
virtual void _print_metadata(
    map_str_str metadata
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

### function template_print

```
template <class T >
void template_print(
    T const & value,
    const std::string & label,
    const int IDcode,
    const uint,
    const ulong
)
```

Helper print functions. 

Template for print functions of "simple" types.

PRINT FUNCTIONS Need to define one of these for every type we want to print! Could use macros again to generate identical print functions for all types that have a << operator already defined. 


### function template_print_vec

```
template <class T >
void template_print_vec(
    std::vector< T > const & value,
    const std::string & label,
    const int IDcode,
    const uint,
    const ulong
)
```

Template for print functions of vectors of "simple" types. 

### function asciiPrinter

```
asciiPrinter(
    const Options & options,
    BasePrinter *const primary =NULL
)
```

TODO: proper gambit error. 

Constructor (for construction via inifile options) 


### function common_constructor

```
void common_constructor(
    const Options & options
)
```

Tasks common to the various constructors. 

### function ~asciiPrinter

```
~asciiPrinter()
```

Destructor. 

### function erase_buffer

```
void erase_buffer()
```

Asciiprinter-specific functions. 

Clear buffer.

Ask the printer for the highest ID number known for a given rank process (needed for resuming, so the scanner can resume assigning point ID from this value. TODO: This does not work yet! Needed for resuming, which is not yet implemented in the asciiprinter DEPRECATED! 


### function endline

```
void endline()
```


### function addtobuffer

```
void addtobuffer(
    const std::vector< double > & functor_data,
    const std::vector< std::string > & functor_labels,
    const int vID,
    const int rank,
    const int pointID
)
```


### function dump_buffer

```
void dump_buffer(
    bool force =false
)
```


### function get_output_filename

```
std::string get_output_filename()
```


### function get_bufferlength

```
int get_bufferlength()
```


-------------------------------

Updated on 2024-05-31 at 15:12:04 +0000