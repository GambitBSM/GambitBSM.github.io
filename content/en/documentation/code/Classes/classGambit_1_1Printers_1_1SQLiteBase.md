---
title: "class Gambit::Printers::SQLiteBase"
description: "SQLite base class for both reader and writer. "

---

# class Gambit::Printers::SQLiteBase



SQLite base class for both reader and writer. 


`#include <sqlitebase.hpp>`

Inherited by [Gambit::Printers::SQLitePrinter](/documentation/code/classes/classgambit_1_1printers_1_1sqliteprinter/), [Gambit::Printers::SQLiteReader](/documentation/code/classes/classgambit_1_1printers_1_1sqlitereader/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[SQLiteBase](/documentation/code/classes/classgambit_1_1printers_1_1sqlitebase/#function-sqlitebase)**() |
| | **[~SQLiteBase](/documentation/code/classes/classgambit_1_1printers_1_1sqlitebase/#function-sqlitebase)**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| std::string | **[get_database_file](/documentation/code/classes/classgambit_1_1printers_1_1sqlitebase/#function-get-database-file)**() |
| std::string | **[get_table_name](/documentation/code/classes/classgambit_1_1printers_1_1sqlitebase/#function-get-table-name)**() |
| std::string | **[get_metadata_table_name](/documentation/code/classes/classgambit_1_1printers_1_1sqlitebase/#function-get-metadata-table-name)**() |
| void | **[set_table_name](/documentation/code/classes/classgambit_1_1printers_1_1sqlitebase/#function-set-table-name)**(const std::string & table_name) |
| void | **[set_metadata_table_name](/documentation/code/classes/classgambit_1_1printers_1_1sqlitebase/#function-set-metadata-table-name)**(const std::string & metadata_table_name) |
| void | **[require_output_ready](/documentation/code/classes/classgambit_1_1printers_1_1sqlitebase/#function-require-output-ready)**() |
| void | **[open_db](/documentation/code/classes/classgambit_1_1printers_1_1sqlitebase/#function-open-db)**(const std::string & path, char access ='r') |
| void | **[close_db](/documentation/code/classes/classgambit_1_1printers_1_1sqlitebase/#function-close-db)**() |
| sqlite3 * | **[get_db](/documentation/code/classes/classgambit_1_1printers_1_1sqlitebase/#function-get-db)**() |
| void | **[cout_row](/documentation/code/classes/classgambit_1_1printers_1_1sqlitebase/#function-cout-row)**(sqlite3_stmt * tmp_stmt) |
| void | **[check_table_exists](/documentation/code/classes/classgambit_1_1printers_1_1sqlitebase/#function-check-table-exists)**() |
| void | **[set_table_exists](/documentation/code/classes/classgambit_1_1printers_1_1sqlitebase/#function-set-table-exists)**() |
| std::map< std::string, std::string, [Utils::ci_less](/documentation/code/classes/structgambit_1_1utils_1_1ci__less/) > | **[get_column_info](/documentation/code/classes/classgambit_1_1printers_1_1sqlitebase/#function-get-column-info)**() |
| int | **[submit_sql](/documentation/code/classes/classgambit_1_1printers_1_1sqlitebase/#function-submit-sql)**(const std::string & local_info, const std::string & sqlstr, bool allow_fail =false, sql_callback_fptr callback =NULL, void * data =NULL, char ** zErrMsg =NULL) |

## Public Functions Documentation

### function SQLiteBase

```
SQLiteBase()
```


### function ~SQLiteBase

```
~SQLiteBase()
```


## Protected Functions Documentation

### function get_database_file

```
std::string get_database_file()
```


### function get_table_name

```
std::string get_table_name()
```


### function get_metadata_table_name

```
std::string get_metadata_table_name()
```


### function set_table_name

```
void set_table_name(
    const std::string & table_name
)
```


### function set_metadata_table_name

```
void set_metadata_table_name(
    const std::string & metadata_table_name
)
```


### function require_output_ready

```
void require_output_ready()
```


### function open_db

```
void open_db(
    const std::string & path,
    char access ='r'
)
```


### function close_db

```
void close_db()
```


### function get_db

```
sqlite3 * get_db()
```


### function cout_row

```
void cout_row(
    sqlite3_stmt * tmp_stmt
)
```


### function check_table_exists

```
void check_table_exists()
```


### function set_table_exists

```
void set_table_exists()
```


### function get_column_info

```
std::map< std::string, std::string, Utils::ci_less > get_column_info()
```


### function submit_sql

```
int submit_sql(
    const std::string & local_info,
    const std::string & sqlstr,
    bool allow_fail =false,
    sql_callback_fptr callback =NULL,
    void * data =NULL,
    char ** zErrMsg =NULL
)
```


-------------------------------

Updated on 2024-05-31 at 15:12:04 +0000