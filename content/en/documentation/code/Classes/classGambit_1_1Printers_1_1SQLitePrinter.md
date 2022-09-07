---
title: 'class Gambit::Printers::SQLitePrinter'
description: 'The main printer class for output to SQLite database. '

---

# Gambit::Printers::SQLitePrinter



The main printer class for output to SQLite database. 


`#include <sqliteprinter.hpp>`

Inherits from [Gambit::Printers::BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/), [Gambit::Printers::SQLiteBase](/documentation/code/classes/classgambit_1_1printers_1_1sqlitebase/), [Gambit::Printers::BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual void | **[initialise](/documentation/code/classes/classgambit_1_1printers_1_1sqliteprinter/#function-initialise)**(const std::vector< int > & ) |
| virtual void | **[flush](/documentation/code/classes/classgambit_1_1printers_1_1sqliteprinter/#function-flush)**() |
| virtual void | **[reset](/documentation/code/classes/classgambit_1_1printers_1_1sqliteprinter/#function-reset)**(bool force =false)<br>Function to signal to the printer to write buffer contents to disk.  |
| virtual void | **[finalise](/documentation/code/classes/classgambit_1_1printers_1_1sqliteprinter/#function-finalise)**(bool abnormal =false)<br>Signal printer that scan is finished, and final output needs to be performed.  |
| virtual [Options](/documentation/code/classes/classgambit_1_1options/) | **[resume_reader_options](/documentation/code/classes/classgambit_1_1printers_1_1sqliteprinter/#function-resume-reader-options)**() |
| template <typename T \> <br>void | **[_print](/documentation/code/classes/classgambit_1_1printers_1_1sqliteprinter/#function-print)**(T const & , const std::string & label, const int vertexID, const uint, const ulong)<br>Print functions.  |
| | **[SQLitePrinter](/documentation/code/classes/classgambit_1_1printers_1_1sqliteprinter/#function-sqliteprinter)**(const [Options](/documentation/code/classes/classgambit_1_1options/) & options, [BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/) *const primary =NULL)<br>Constructor (for construction via inifile options)  |
| | **[~SQLitePrinter](/documentation/code/classes/classgambit_1_1printers_1_1sqliteprinter/#function-sqliteprinter)**()<br>Destructor.  |
| std::size_t | **[get_max_buffer_length](/documentation/code/classes/classgambit_1_1printers_1_1sqliteprinter/#function-get-max-buffer-length)**() |
| template <class T \> <br>void | **[template_print](/documentation/code/classes/classgambit_1_1printers_1_1sqliteprinter/#function-template-print)**(T const & value, const std::string & label, const int , const unsigned int mpirank, const unsigned long pointID, const std::string & col_type)<br>Helper print functions.  |

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

**Public Functions inherited from [Gambit::Printers::SQLiteBase](/documentation/code/classes/classgambit_1_1printers_1_1sqlitebase/)**

|                | Name           |
| -------------- | -------------- |
| | **[SQLiteBase](/documentation/code/classes/classgambit_1_1printers_1_1sqlitebase/#function-sqlitebase)**() |
| | **[~SQLiteBase](/documentation/code/classes/classgambit_1_1printers_1_1sqlitebase/#function-sqlitebase)**() |

**Protected Functions inherited from [Gambit::Printers::SQLiteBase](/documentation/code/classes/classgambit_1_1printers_1_1sqlitebase/)**

|                | Name           |
| -------------- | -------------- |
| std::string | **[get_database_file](/documentation/code/classes/classgambit_1_1printers_1_1sqlitebase/#function-get-database-file)**() |
| std::string | **[get_table_name](/documentation/code/classes/classgambit_1_1printers_1_1sqlitebase/#function-get-table-name)**() |
| void | **[set_table_name](/documentation/code/classes/classgambit_1_1printers_1_1sqlitebase/#function-set-table-name)**(const std::string & table_name) |
| void | **[require_output_ready](/documentation/code/classes/classgambit_1_1printers_1_1sqlitebase/#function-require-output-ready)**() |
| void | **[open_db](/documentation/code/classes/classgambit_1_1printers_1_1sqlitebase/#function-open-db)**(const std::string & path, char access ='r') |
| void | **[close_db](/documentation/code/classes/classgambit_1_1printers_1_1sqlitebase/#function-close-db)**() |
| sqlite3 * | **[get_db](/documentation/code/classes/classgambit_1_1printers_1_1sqlitebase/#function-get-db)**() |
| void | **[cout_row](/documentation/code/classes/classgambit_1_1printers_1_1sqlitebase/#function-cout-row)**(sqlite3_stmt * tmp_stmt) |
| void | **[check_table_exists](/documentation/code/classes/classgambit_1_1printers_1_1sqlitebase/#function-check-table-exists)**() |
| void | **[set_table_exists](/documentation/code/classes/classgambit_1_1printers_1_1sqlitebase/#function-set-table-exists)**() |
| std::map< std::string, std::string, [Utils::ci_less](/documentation/code/classes/structgambit_1_1utils_1_1ci__less/) > | **[get_column_info](/documentation/code/classes/classgambit_1_1printers_1_1sqlitebase/#function-get-column-info)**() |
| int | **[submit_sql](/documentation/code/classes/classgambit_1_1printers_1_1sqlitebase/#function-submit-sql)**(const std::string & local_info, const std::string & sqlstr, bool allow_fail =false, sql_callback_fptr callback =NULL, void * data =NULL, char ** zErrMsg =NULL) |

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


**Reimplements**: [Gambit::Printers::BasePrinter::initialise](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/#function-initialise)


Virtual function overloads: 


### function flush

```
virtual void flush()
```


**Reimplements**: [Gambit::Printers::BasePrinter::flush](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/#function-flush)


Signal printer to flush data in buffers to disk [Printers](/documentation/code/namespaces/namespacegambit_1_1printers/) should do this automatically as needed, but this is useful if a scanner is printing a bunch of data as a batch, to make sure it is all on disk after the batch is done. 


### function reset

```
virtual void reset(
    bool force =false
)
```

Function to signal to the printer to write buffer contents to disk. 

**Reimplements**: [Gambit::Printers::BaseBasePrinter::reset](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-reset)


Signal printer to reset contents, i.e. delete old data in preperation for replacement 


### function finalise

```
virtual void finalise(
    bool abnormal =false
)
```

Signal printer that scan is finished, and final output needs to be performed. 

**Reimplements**: [Gambit::Printers::BaseBasePrinter::finalise](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/#function-finalise)


### function resume_reader_options

```
virtual Options resume_reader_options()
```


**Reimplements**: [Gambit::Printers::BasePrinter::resume_reader_options](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/#function-resume-reader-options)


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

### function SQLitePrinter

```
SQLitePrinter(
    const Options & options,
    BasePrinter *const primary =NULL
)
```

Constructor (for construction via inifile options) 

### function ~SQLitePrinter

```
inline ~SQLitePrinter()
```

Destructor. 

### function get_max_buffer_length

```
std::size_t get_max_buffer_length()
```


### function template_print

```
template <class T >
inline void template_print(
    T const & value,
    const std::string & label,
    const int ,
    const unsigned int mpirank,
    const unsigned long pointID,
    const std::string & col_type
)
```

Helper print functions. 

-------------------------------

Updated on 2022-09-07 at 14:07:46 +0000