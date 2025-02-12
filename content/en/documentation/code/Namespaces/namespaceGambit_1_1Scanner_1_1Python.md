---
title: "namespace Gambit::Scanner::Python"

description: "[No description available]"

---

# namespace Gambit::Scanner::Python

[No description available]

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Gambit::Scanner::Python::diagnostics](/documentation/code/classes/classgambit_1_1scanner_1_1python_1_1diagnostics/)**  |
| class | **[Gambit::Scanner::Python::fake_vector](/documentation/code/classes/classgambit_1_1scanner_1_1python_1_1fake__vector/)**  |
| class | **[Gambit::Scanner::Python::IniFileParser](/documentation/code/classes/classgambit_1_1scanner_1_1python_1_1inifileparser/)**  |
| class | **[Gambit::Scanner::Python::printer_wrapper](/documentation/code/classes/classgambit_1_1scanner_1_1python_1_1printer__wrapper/)**  |
| class | **[Gambit::Scanner::Python::scan](/documentation/code/classes/classgambit_1_1scanner_1_1python_1_1scan/)**  |
| class | **[Gambit::Scanner::Python::scan_interface](/documentation/code/classes/classgambit_1_1scanner_1_1python_1_1scan__interface/)**  |

## Functions

|                | Name           |
| -------------- | -------------- |
| std::string | **[pytype](/documentation/code/namespaces/namespacegambit_1_1scanner_1_1python/#function-pytype)**(py::handle o) |
| template <typename T \> <br>T | **[pyconvert](/documentation/code/namespaces/namespacegambit_1_1scanner_1_1python/#function-pyconvert)**(py::handle o) |
| YAML::Node | **[pyyamlconvert](/documentation/code/namespaces/namespacegambit_1_1scanner_1_1python/#function-pyyamlconvert)**(py::handle o) |
| void | **[scanner_diagnostic](/documentation/code/namespaces/namespacegambit_1_1scanner_1_1python/#function-scanner-diagnostic)**() |
| void | **[test_function_diagnostic](/documentation/code/namespaces/namespacegambit_1_1scanner_1_1python/#function-test-function-diagnostic)**() |
| void | **[prior_diagnostic](/documentation/code/namespaces/namespacegambit_1_1scanner_1_1python/#function-prior-diagnostic)**() |
| void | **[ff_prior_diagnostic](/documentation/code/namespaces/namespacegambit_1_1scanner_1_1python/#function-ff-prior-diagnostic)**(const std::string & command) |
| void | **[ff_scanner_diagnostic](/documentation/code/namespaces/namespacegambit_1_1scanner_1_1python/#function-ff-scanner-diagnostic)**(const std::string & command) |
| void | **[ff_test_function_diagnostic](/documentation/code/namespaces/namespacegambit_1_1scanner_1_1python/#function-ff-test-function-diagnostic)**(const std::string & command) |
| void | **[do_cleanup](/documentation/code/namespaces/namespacegambit_1_1scanner_1_1python/#function-do-cleanup)**() |
| void | **[terminator](/documentation/code/namespaces/namespacegambit_1_1scanner_1_1python/#function-terminator)**() |
| void | **[ensure_size_fake](/documentation/code/namespaces/namespacegambit_1_1scanner_1_1python/#function-ensure-size-fake)**([scanpy::fake_vector](/documentation/code/classes/classgambit_1_1scanner_1_1python_1_1fake__vector/) & vec, size_t i) |
| void | **[ensure_size_vec](/documentation/code/namespaces/namespacegambit_1_1scanner_1_1python/#function-ensure-size-vec)**(std::vector< double > & , size_t ) |
| void | **[ensure_size_evec](/documentation/code/namespaces/namespacegambit_1_1scanner_1_1python/#function-ensure-size-evec)**([hyper_cube_ref](/documentation/code/namespaces/namespacegambit_1_1scanner/#using-hyper-cube-ref)< double > , size_t ) |

## Attributes

|                | Name           |
| -------------- | -------------- |
| std::shared_ptr< [printer_wrapper](/documentation/code/classes/classgambit_1_1scanner_1_1python_1_1printer__wrapper/) > | **[printer_manager](/documentation/code/namespaces/namespacegambit_1_1scanner_1_1python/#variable-printer-manager)**  |


## Functions Documentation

### function pytype

```
inline std::string pytype(
    py::handle o
)
```


### function pyconvert

```
template <typename T >
T pyconvert(
    py::handle o
)
```


### function pyyamlconvert

```
inline YAML::Node pyyamlconvert(
    py::handle o
)
```


### function scanner_diagnostic

```
inline void scanner_diagnostic()
```


### function test_function_diagnostic

```
inline void test_function_diagnostic()
```


### function prior_diagnostic

```
inline void prior_diagnostic()
```


### function ff_prior_diagnostic

```
inline void ff_prior_diagnostic(
    const std::string & command
)
```


### function ff_scanner_diagnostic

```
inline void ff_scanner_diagnostic(
    const std::string & command
)
```


### function ff_test_function_diagnostic

```
inline void ff_test_function_diagnostic(
    const std::string & command
)
```


### function do_cleanup

```
void do_cleanup()
```


### function terminator

```
static void terminator()
```


### function ensure_size_fake

```
void ensure_size_fake(
    scanpy::fake_vector & vec,
    size_t i
)
```


### function ensure_size_vec

```
void ensure_size_vec(
    std::vector< double > & ,
    size_t 
)
```


### function ensure_size_evec

```
void ensure_size_evec(
    hyper_cube_ref< double > ,
    size_t 
)
```



## Attributes Documentation

### variable printer_manager

```
std::shared_ptr< printer_wrapper > printer_manager;
```





-------------------------------

Updated on 2025-02-12 at 15:36:39 +0000