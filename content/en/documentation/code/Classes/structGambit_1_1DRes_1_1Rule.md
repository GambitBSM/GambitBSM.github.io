---
title: "struct Gambit::DRes::Rule"

description: "[No description available]"

---

# struct Gambit::DRes::Rule



[No description available] [More...](#detailed-description)


`#include <depresolver.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Rule](/documentation/code/classes/structgambit_1_1dres_1_1rule/#function-rule)**(std::string function, std::string module) |
| | **[Rule](/documentation/code/classes/structgambit_1_1dres_1_1rule/#function-rule)**([IniParser::ObservableType](/documentation/code/classes/structgambit_1_1iniparser_1_1types_1_1observable/) t) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| std::string | **[capability](/documentation/code/classes/structgambit_1_1dres_1_1rule/#variable-capability)**  |
| std::string | **[type](/documentation/code/classes/structgambit_1_1dres_1_1rule/#variable-type)**  |
| std::string | **[function](/documentation/code/classes/structgambit_1_1dres_1_1rule/#variable-function)**  |
| std::string | **[module](/documentation/code/classes/structgambit_1_1dres_1_1rule/#variable-module)**  |
| std::string | **[backend](/documentation/code/classes/structgambit_1_1dres_1_1rule/#variable-backend)**  |
| std::string | **[version](/documentation/code/classes/structgambit_1_1dres_1_1rule/#variable-version)**  |
| [Options](/documentation/code/classes/classgambit_1_1options/) | **[options](/documentation/code/classes/structgambit_1_1dres_1_1rule/#variable-options)**  |

## Detailed Description

```
struct Gambit::DRes::Rule;
```


A simple rule for dependency resolution (aka constraints on module and function name). 

## Public Functions Documentation

### function Rule

```
inline Rule(
    std::string function,
    std::string module
)
```


### function Rule

```
inline Rule(
    IniParser::ObservableType t
)
```


## Public Attributes Documentation

### variable capability

```
std::string capability;
```


### variable type

```
std::string type;
```


### variable function

```
std::string function;
```


### variable module

```
std::string module;
```


### variable backend

```
std::string backend;
```


### variable version

```
std::string version;
```


### variable options

```
Options options;
```


-------------------------------

Updated on 2023-06-26 at 21:36:52 +0000