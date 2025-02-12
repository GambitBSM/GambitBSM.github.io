---
title: "class Gambit::Scanner::Python::scan"

description: "[No description available]"

---

# class Gambit::Scanner::Python::scan



[No description available]

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[scan](/documentation/code/classes/classgambit_1_1scanner_1_1python_1_1scan/#function-scan)**(bool init_mpi) |
| std::shared_ptr< [printer_wrapper](/documentation/code/classes/classgambit_1_1scanner_1_1python_1_1printer__wrapper/) > | **[get_printer](/documentation/code/classes/classgambit_1_1scanner_1_1python_1_1scan/#function-get-printer)**() |
| void | **[dianostic](/documentation/code/classes/classgambit_1_1scanner_1_1python_1_1scan/#function-dianostic)**(py::args args, py::kwargs ) |
| int | **[run](/documentation/code/classes/classgambit_1_1scanner_1_1python_1_1scan/#function-run)**(py::object file_obj, py::object func_obj, py::object prior_obj, bool restart) |
| | **[~scan](/documentation/code/classes/classgambit_1_1scanner_1_1python_1_1scan/#function-scan)**() |
| void | **[print](/documentation/code/classes/classgambit_1_1scanner_1_1python_1_1scan/#function-print)**(const std::string & key, const double & value) |

## Public Functions Documentation

### function scan

```
inline scan(
    bool init_mpi
)
```


### function get_printer

```
inline std::shared_ptr< printer_wrapper > get_printer()
```


### function dianostic

```
inline void dianostic(
    py::args args,
    py::kwargs 
)
```


### function run

```
inline int run(
    py::object file_obj,
    py::object func_obj,
    py::object prior_obj,
    bool restart
)
```


### function ~scan

```
inline ~scan()
```


### function print

```
static inline void print(
    const std::string & key,
    const double & value
)
```


-------------------------------

Updated on 2025-02-12 at 15:36:40 +0000