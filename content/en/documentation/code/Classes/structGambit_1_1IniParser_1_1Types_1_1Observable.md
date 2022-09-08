---
title: "struct Gambit::IniParser::Types::Observable"

description: "[No description available]"

---

# struct Gambit::IniParser::Types::Observable



[No description available]

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Observable](/documentation/code/classes/structgambit_1_1iniparser_1_1types_1_1observable/#function-gambitiniparsertypesobservable-observable)**()<br>Default constructor, to ensure the default values are not gibberish.  |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| std::string | **[purpose](/documentation/code/classes/structgambit_1_1iniparser_1_1types_1_1observable/#variable-gambitiniparsertypesobservable-purpose)**  |
| std::string | **[capability](/documentation/code/classes/structgambit_1_1iniparser_1_1types_1_1observable/#variable-gambitiniparsertypesobservable-capability)**  |
| std::string | **[type](/documentation/code/classes/structgambit_1_1iniparser_1_1types_1_1observable/#variable-gambitiniparsertypesobservable-type)**  |
| std::string | **[function](/documentation/code/classes/structgambit_1_1iniparser_1_1types_1_1observable/#variable-gambitiniparsertypesobservable-function)**  |
| std::string | **[module](/documentation/code/classes/structgambit_1_1iniparser_1_1types_1_1observable/#variable-gambitiniparsertypesobservable-module)**  |
| std::string | **[backend](/documentation/code/classes/structgambit_1_1iniparser_1_1types_1_1observable/#variable-gambitiniparsertypesobservable-backend)**  |
| std::string | **[version](/documentation/code/classes/structgambit_1_1iniparser_1_1types_1_1observable/#variable-gambitiniparsertypesobservable-version)**  |
| bool | **[printme](/documentation/code/classes/structgambit_1_1iniparser_1_1types_1_1observable/#variable-gambitiniparsertypesobservable-printme)**  |
| bool | **[weakrule](/documentation/code/classes/structgambit_1_1iniparser_1_1types_1_1observable/#variable-gambitiniparsertypesobservable-weakrule)**  |
| [Options](/documentation/code/classes/classgambit_1_1options/) | **[options](/documentation/code/classes/structgambit_1_1iniparser_1_1types_1_1observable/#variable-gambitiniparsertypesobservable-options)**  |
| YAML::Node | **[subcaps](/documentation/code/classes/structgambit_1_1iniparser_1_1types_1_1observable/#variable-gambitiniparsertypesobservable-subcaps)**  |
| std::vector< [Observable](/documentation/code/classes/structgambit_1_1iniparser_1_1types_1_1observable/) > | **[dependencies](/documentation/code/classes/structgambit_1_1iniparser_1_1types_1_1observable/#variable-gambitiniparsertypesobservable-dependencies)**  |
| std::vector< [Observable](/documentation/code/classes/structgambit_1_1iniparser_1_1types_1_1observable/) > | **[backends](/documentation/code/classes/structgambit_1_1iniparser_1_1types_1_1observable/#variable-gambitiniparsertypesobservable-backends)**  |
| std::vector< std::string > | **[functionChain](/documentation/code/classes/structgambit_1_1iniparser_1_1types_1_1observable/#variable-gambitiniparsertypesobservable-functionchain)**  |

## Public Functions Documentation

### function Observable

```
inline Observable()
```

Default constructor, to ensure the default values are not gibberish. 

## Public Attributes Documentation

### variable purpose

```
std::string purpose;
```


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


### variable printme

```
bool printme;
```


### variable weakrule

```
bool weakrule;
```


### variable options

```
Options options;
```


### variable subcaps

```
YAML::Node subcaps;
```


### variable dependencies

```
std::vector< Observable > dependencies;
```


### variable backends

```
std::vector< Observable > backends;
```


### variable functionChain

```
std::vector< std::string > functionChain;
```


-------------------------------

Updated on 2022-09-08 at 01:48:55 +0000