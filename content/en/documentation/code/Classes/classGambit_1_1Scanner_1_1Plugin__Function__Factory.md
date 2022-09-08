---
title: "class Gambit::Scanner::Plugin_Function_Factory"
description: "Factory class to make objectives using objective plugins. "

---

# class Gambit::Scanner::Plugin_Function_Factory



Factory class to make objectives using objective plugins. 


`#include <plugin_factory.hpp>`

Inherits from [Gambit::Scanner::Factory_Base](/documentation/code/classes/classgambit_1_1scanner_1_1factory__base/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Plugin_Function_Factory](/documentation/code/classes/classgambit_1_1scanner_1_1plugin__function__factory/)**(const std::vector< std::string > & keys, std::map< std::string, std::vector< std::pair< std::string, std::string > > > & names) |
| virtual void * | **[operator()](/documentation/code/classes/classgambit_1_1scanner_1_1plugin__function__factory/)**(const std::string & purpose) const |
| | **[~Plugin_Function_Factory](/documentation/code/classes/classgambit_1_1scanner_1_1plugin__function__factory/)**() |

## Additional inherited members

**Public Functions inherited from [Gambit::Scanner::Factory_Base](/documentation/code/classes/classgambit_1_1scanner_1_1factory__base/)**

|                | Name           |
| -------------- | -------------- |
| virtual | **[~Factory_Base](/documentation/code/classes/classgambit_1_1scanner_1_1factory__base/)**() |


## Public Functions Documentation

### function Plugin_Function_Factory

```
inline Plugin_Function_Factory(
    const std::vector< std::string > & keys,
    std::map< std::string, std::vector< std::pair< std::string, std::string > > > & names
)
```


### function operator()

```
inline virtual void * operator()(
    const std::string & purpose
) const
```


**Reimplements**: [Gambit::Scanner::Factory_Base::operator()](/documentation/code/classes/classgambit_1_1scanner_1_1factory__base/)


### function ~Plugin_Function_Factory

```
inline ~Plugin_Function_Factory()
```


-------------------------------

Updated on 2022-09-08 at 01:05:18 +0000