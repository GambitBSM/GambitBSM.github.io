---
title: "class Gambit::IniParser::IniFile"
description: "Main inifile class. "

---

# class Gambit::IniParser::IniFile



Main inifile class. 


`#include <yaml_parser.hpp>`

Inherits from [Gambit::IniParser::Parser](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| const ObservablesType & | **[getObservables](/documentation/code/classes/classgambit_1_1iniparser_1_1inifile/)**() const |
| const ObservablesType & | **[getRules](/documentation/code/classes/classgambit_1_1iniparser_1_1inifile/)**() const |
| const [str](/documentation/code/namespaces/namespacegambit/) | **[filename](/documentation/code/classes/classgambit_1_1iniparser_1_1inifile/)**() const |
| virtual void | **[readFile](/documentation/code/classes/classgambit_1_1iniparser_1_1inifile/)**([str](/documentation/code/namespaces/namespacegambit/) name)<br>Read in the [YAML](/documentation/code/namespaces/namespaceyaml/) file.  |

## Additional inherited members

**Public Functions inherited from [Gambit::IniParser::Parser](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/)**

|                | Name           |
| -------------- | -------------- |
| YAML::Node | **[getParametersNode](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/)**() const |
| YAML::Node | **[getPriorsNode](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/)**() const |
| YAML::Node | **[getPrinterNode](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/)**() const |
| YAML::Node | **[getScannerNode](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/)**() const |
| YAML::Node | **[getLoggerNode](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/)**() const |
| YAML::Node | **[getKeyValuePairNode](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/)**() const |
| template <typename... args\> <br>bool | **[hasKey](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/)**(args... keys) const |
| template <typename TYPE ,typename... args\> <br>TYPE | **[getValue](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/)**(args... keys) const |
| template <typename TYPE ,typename... args\> <br>TYPE | **[getValueOrDef](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/)**(TYPE def, const args &... keys) const |
| template <typename TYPE \> <br>TYPE | **[getModelParameterEntry](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/)**([str](/documentation/code/namespaces/namespacegambit/) model, [str](/documentation/code/namespaces/namespacegambit/) param, [str](/documentation/code/namespaces/namespacegambit/) key) const |
| bool | **[hasModelParameterEntry](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/)**([str](/documentation/code/namespaces/namespacegambit/) model, [str](/documentation/code/namespaces/namespacegambit/) param, [str](/documentation/code/namespaces/namespacegambit/) key) const |
| const std::set< [str](/documentation/code/namespaces/namespacegambit/) > | **[getModelNames](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/)**() const<br>Return list of model names (without "adhoc" model!)  |
| const std::vector< [str](/documentation/code/namespaces/namespacegambit/) > | **[getModelParameters](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/)**([str](/documentation/code/namespaces/namespacegambit/) model) const |
| const [Options](/documentation/code/classes/classgambit_1_1options/) | **[getOptions](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/)**([str](/documentation/code/namespaces/namespacegambit/) key) const<br>Getter for options.  |

**Protected Functions inherited from [Gambit::IniParser::Parser](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/)**

|                | Name           |
| -------------- | -------------- |
| YAML::Node | **[filename_to_node](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/)**([str](/documentation/code/namespaces/namespacegambit/) filename)<br>Read in the actual [YAML](/documentation/code/namespaces/namespaceyaml/) file.  |
| void | **[basicParse](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/)**(YAML::Node root, [str](/documentation/code/namespaces/namespacegambit/) filename)<br>Do the basic parsing of the [YAML](/documentation/code/namespaces/namespaceyaml/) file.  |


## Public Functions Documentation

### function getObservables

```
const ObservablesType & getObservables() const
```


Getters for private observable and rules entries 


### function getRules

```
const ObservablesType & getRules() const
```


### function filename

```
const str filename() const
```


### function readFile

```
virtual void readFile(
    str name
)
```

Read in the [YAML](/documentation/code/namespaces/namespaceyaml/) file. 

**Reimplements**: [Gambit::IniParser::Parser::readFile](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/)


-------------------------------

Updated on 2022-09-08 at 01:05:17 +0000