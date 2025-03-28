---
title: "struct Gambit::Scanner::Plugins::ScannerPyPlugin::like_physical"
description: "A derived class of [like_ptr_base]() for managing [Function_Base](/documentation/code/classes/classgambit_1_1scanner_1_1function__base/) objects related to physical properties. "

---

# struct Gambit::Scanner::Plugins::ScannerPyPlugin::like_physical



A derived class of [like_ptr_base]() for managing [Function_Base](/documentation/code/classes/classgambit_1_1scanner_1_1function__base/) objects related to physical properties.  [More...](#detailed-description)


`#include <py_module_scan.hpp>`

Inherits from [Gambit::Scanner::Plugins::ScannerPyPlugin::like_ptr_base< like_physical >](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1like__ptr__base/), std::enable_shared_from_this< T >

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[like_physical](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1like__physical/#function-like-physical)**([s_func](/documentation/code/classes/classgambit_1_1scanner_1_1function__base/) & s)<br>Constructs a [like_physical](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1like__physical/) object.  |

## Additional inherited members

**Protected Types inherited from [Gambit::Scanner::Plugins::ScannerPyPlugin::like_ptr_base< like_physical >](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1like__ptr__base/)**

|                | Name           |
| -------------- | -------------- |
| typedef std::shared_ptr< [Gambit::Scanner::Function_Base](/documentation/code/classes/classgambit_1_1scanner_1_1function__base/)< double(std::unordered_map< std::string, double > &)> > | **[s_ptr](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1like__ptr__base/#typedef-s-ptr)**  |
| typedef [Gambit::Scanner::Function_Base](/documentation/code/classes/classgambit_1_1scanner_1_1function__base/)< double(std::unordered_map< std::string, double > &)> | **[s_func](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1like__ptr__base/#typedef-s-func)**  |

**Public Functions inherited from [Gambit::Scanner::Plugins::ScannerPyPlugin::like_ptr_base< like_physical >](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1like__ptr__base/)**

|                | Name           |
| -------------- | -------------- |
| | **[like_ptr_base](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1like__ptr__base/#function-like-ptr-base)**([s_func](/documentation/code/classes/classgambit_1_1scanner_1_1function__base/) & s)<br>Constructs a [like_ptr_base](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1like__ptr__base/) object.  |
| [Gambit::Scanner::like_ptr](/documentation/code/classes/classgambit_1_1scanner_1_1like__ptr/) & | **[get](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1like__ptr__base/#function-get)**()<br>Retrieves the underlying shared pointer.  |

**Protected Attributes inherited from [Gambit::Scanner::Plugins::ScannerPyPlugin::like_ptr_base< like_physical >](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1like__ptr__base/)**

|                | Name           |
| -------------- | -------------- |
| s_ptr | **[ptr](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1like__ptr__base/#variable-ptr)**  |


## Detailed Description

```
struct Gambit::Scanner::Plugins::ScannerPyPlugin::like_physical;
```

A derived class of [like_ptr_base]() for managing [Function_Base](/documentation/code/classes/classgambit_1_1scanner_1_1function__base/) objects related to physical properties. 

This class is specifically designed to manage [Function_Base](/documentation/code/classes/classgambit_1_1scanner_1_1function__base/) objects that represent physical properties in a system. 

## Public Functions Documentation

### function like_physical

```
inline like_physical(
    s_func & s
)
```

Constructs a [like_physical](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1like__physical/) object. 

**Parameters**: 

  * **s** A reference to the [Function_Base](/documentation/code/classes/classgambit_1_1scanner_1_1function__base/) object to be managed. 


-------------------------------

Updated on 2025-02-12 at 16:10:33 +0000