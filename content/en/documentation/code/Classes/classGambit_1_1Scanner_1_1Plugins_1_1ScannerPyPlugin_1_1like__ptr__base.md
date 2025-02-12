---
title: "class Gambit::Scanner::Plugins::ScannerPyPlugin::like_ptr_base"
description: "A class that wraps a shared pointer to a [Function_Base](/documentation/code/classes/classgambit_1_1scanner_1_1function__base/) object. "

---

# class Gambit::Scanner::Plugins::ScannerPyPlugin::like_ptr_base



A class that wraps a shared pointer to a [Function_Base](/documentation/code/classes/classgambit_1_1scanner_1_1function__base/) object.  [More...](#detailed-description)


`#include <py_module_scan.hpp>`

Inherits from std::enable_shared_from_this< T >

## Protected Types

|                | Name           |
| -------------- | -------------- |
| typedef std::shared_ptr< [Gambit::Scanner::Function_Base](/documentation/code/classes/classgambit_1_1scanner_1_1function__base/)< double(std::unordered_map< std::string, double > &)> > | **[s_ptr](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1like__ptr__base/#typedef-s-ptr)**  |
| typedef [Gambit::Scanner::Function_Base](/documentation/code/classes/classgambit_1_1scanner_1_1function__base/)< double(std::unordered_map< std::string, double > &)> | **[s_func](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1like__ptr__base/#typedef-s-func)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[like_ptr_base](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1like__ptr__base/#function-like-ptr-base)**([s_func](/documentation/code/classes/classgambit_1_1scanner_1_1function__base/) & s)<br>Constructs a [like_ptr_base](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1like__ptr__base/) object.  |
| [Gambit::Scanner::like_ptr](/documentation/code/classes/classgambit_1_1scanner_1_1like__ptr/) & | **[get](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1like__ptr__base/#function-get)**()<br>Retrieves the underlying shared pointer.  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| s_ptr | **[ptr](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1like__ptr__base/#variable-ptr)**  |

## Detailed Description

```
template <typename T >
class Gambit::Scanner::Plugins::ScannerPyPlugin::like_ptr_base;
```

A class that wraps a shared pointer to a [Function_Base](/documentation/code/classes/classgambit_1_1scanner_1_1function__base/) object. 

**Template Parameters**: 

  * **T** The specific type of the [Function_Base](/documentation/code/classes/classgambit_1_1scanner_1_1function__base/) object. 


This class is used to manage the lifetime of [Function_Base](/documentation/code/classes/classgambit_1_1scanner_1_1function__base/) objects and to provide a uniform interface for using them.

## Protected Types Documentation

### typedef s_ptr

```
typedef std::shared_ptr<Gambit::Scanner::Function_Base<double (std::unordered_map<std::string, double> &)> > Gambit::Scanner::Plugins::ScannerPyPlugin::like_ptr_base< T >::s_ptr;
```


### typedef s_func

```
typedef Gambit::Scanner::Function_Base<double (std::unordered_map<std::string, double> &)> Gambit::Scanner::Plugins::ScannerPyPlugin::like_ptr_base< T >::s_func;
```


## Public Functions Documentation

### function like_ptr_base

```
inline like_ptr_base(
    s_func & s
)
```

Constructs a [like_ptr_base](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1like__ptr__base/) object. 

**Parameters**: 

  * **s** A reference to the [Function_Base](/documentation/code/classes/classgambit_1_1scanner_1_1function__base/) object to be managed. 


### function get

```
inline Gambit::Scanner::like_ptr & get()
```

Retrieves the underlying shared pointer. 

**Return**: A reference to the underlying shared pointer. 

## Protected Attributes Documentation

### variable ptr

```
s_ptr ptr;
```


-------------------------------

Updated on 2025-02-12 at 15:36:39 +0000