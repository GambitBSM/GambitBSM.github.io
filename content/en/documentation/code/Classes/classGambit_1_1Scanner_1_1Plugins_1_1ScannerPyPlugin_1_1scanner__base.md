---
title: "class Gambit::Scanner::Plugins::ScannerPyPlugin::scanner_base"
description: "A base class for scanner functionality. "

---

# class Gambit::Scanner::Plugins::ScannerPyPlugin::scanner_base



A base class for scanner functionality.  [More...](#detailed-description)


`#include <py_module_scan.hpp>`

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef std::shared_ptr< [Gambit::Scanner::Function_Base](/documentation/code/classes/classgambit_1_1scanner_1_1function__base/)< double(std::unordered_map< std::string, double > &)> > | **[s_ptr](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1scanner__base/#typedef-s-ptr)**  |
| typedef [Gambit::Scanner::Function_Base](/documentation/code/classes/classgambit_1_1scanner_1_1function__base/)< double(std::unordered_map< std::string, double > &)> | **[s_func](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1scanner__base/#typedef-s-func)**  |
| typedef [Gambit::Scanner::Plugins::ScannerPyPlugin::like_hypercube](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1like__hypercube/) | **[s_hyper_func](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1scanner__base/#typedef-s-hyper-func)**  |
| typedef [Gambit::Scanner::Plugins::ScannerPyPlugin::like_physical](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1like__physical/) | **[s_phys_func](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1scanner__base/#typedef-s-phys-func)**  |
| typedef [Gambit::Scanner::Plugins::ScannerPyPlugin::like_prior_physical](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1like__prior__physical/) | **[s_phys_pr_func](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1scanner__base/#typedef-s-phys-pr-func)**  |
| typedef [Gambit::Scanner::Plugins::ScannerPyPlugin::prior_physical](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1prior__physical/) | **[s_pr_func](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1scanner__base/#typedef-s-pr-func)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| int | **[run](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1scanner__base/#function-run)**()<br>A method to run the scanner.  |
| template <typename T \> <br>py::list | **[to_list](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1scanner__base/#function-to-list)**(const std::vector< T > & vec)<br>Converts a vector to a Python list.  |
| YAML::Node & | **[getNode](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1scanner__base/#function-getnode)**()<br>Retrieves the [YAML](/documentation/code/namespaces/namespaceyaml/) node.  |
| std::shared_ptr< [s_func](/documentation/code/classes/classgambit_1_1scanner_1_1function__base/) > | **[getLike](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1scanner__base/#function-getlike)**()<br>Retrieves the likelihood function.  |
| bool | **[with_mpi](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1scanner__base/#function-with-mpi)**()<br>Checks if MPI is enabled.  |
| int | **[rank](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1scanner__base/#function-rank)**()<br>Retrieves the rank of the MPI process.  |
| int | **[numtasks](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1scanner__base/#function-numtasks)**()<br>Retrieves the number of MPI processes.  |

## Detailed Description

```
class Gambit::Scanner::Plugins::ScannerPyPlugin::scanner_base;
```

A base class for scanner functionality. 

This class provides a base for scanner functionality. It defines several types related to the Gambit::Scanner namespace and can be extended by other classes to provide more specific functionality. 

## Public Types Documentation

### typedef s_ptr

```
typedef std::shared_ptr<Gambit::Scanner::Function_Base<double (std::unordered_map<std::string, double> &)> > Gambit::Scanner::Plugins::ScannerPyPlugin::scanner_base::s_ptr;
```


### typedef s_func

```
typedef Gambit::Scanner::Function_Base<double (std::unordered_map<std::string, double> &)> Gambit::Scanner::Plugins::ScannerPyPlugin::scanner_base::s_func;
```


### typedef s_hyper_func

```
typedef Gambit::Scanner::Plugins::ScannerPyPlugin::like_hypercube Gambit::Scanner::Plugins::ScannerPyPlugin::scanner_base::s_hyper_func;
```


### typedef s_phys_func

```
typedef Gambit::Scanner::Plugins::ScannerPyPlugin::like_physical Gambit::Scanner::Plugins::ScannerPyPlugin::scanner_base::s_phys_func;
```


### typedef s_phys_pr_func

```
typedef Gambit::Scanner::Plugins::ScannerPyPlugin::like_prior_physical Gambit::Scanner::Plugins::ScannerPyPlugin::scanner_base::s_phys_pr_func;
```


### typedef s_pr_func

```
typedef Gambit::Scanner::Plugins::ScannerPyPlugin::prior_physical Gambit::Scanner::Plugins::ScannerPyPlugin::scanner_base::s_pr_func;
```


## Public Functions Documentation

### function run

```
inline int run()
```

A method to run the scanner. 

**Return**: Returns 1 if the method is not overridden in a derived class. 

This method is intended to be overridden by derived classes. If not overridden, it will print an error message and return 1.


### function to_list

```
template <typename T >
static inline py::list to_list(
    const std::vector< T > & vec
)
```

Converts a vector to a Python list. 

**Parameters**: 

  * **vec** The vector to be converted. 


**Template Parameters**: 

  * **T** The type of the elements in the vector. 


**Return**: Returns a Python list containing the elements of the input vector. 

This static method is used to convert a standard C++ vector into a Python list. Each element of the vector is appended to the Python list.


### function getNode

```
static inline YAML::Node & getNode()
```

Retrieves the [YAML](/documentation/code/namespaces/namespaceyaml/) node. 

**Return**: Returns a reference to the [YAML](/documentation/code/namespaces/namespaceyaml/) node. 

This static method is used to retrieve the [YAML](/documentation/code/namespaces/namespaceyaml/) node. If the node has not been initialized, it is set to the result of the `get_inifile_node` function.


### function getLike

```
static inline std::shared_ptr< s_func > getLike()
```

Retrieves the likelihood function. 

**Return**: Returns a shared pointer to the likelihood function. 

This static method is used to retrieve the likelihood function. If the function has not been initialized, it is set to the result of the `get_purpose` function with the "like" node from the [YAML](/documentation/code/namespaces/namespaceyaml/) node as the argument.


### function with_mpi

```
static inline bool with_mpi()
```

Checks if MPI is enabled. 

**Return**: Returns false if MPI is not enabled. 

This static method is used to check if MPI is enabled.


### function rank

```
static inline int rank()
```

Retrieves the rank of the MPI process. 

**Return**: Returns 0 if MPI is not enabled. 

This static method is used to retrieve the rank of the MPI process.


### function numtasks

```
static inline int numtasks()
```

Retrieves the number of MPI processes. 

**Return**: Returns 1 if MPI is not enabled. 

This static method is used to retrieve the number of MPI processes.


-------------------------------

Updated on 2024-07-18 at 13:53:32 +0000