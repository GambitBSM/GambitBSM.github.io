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
| const ObservablesType & | **[getObservables](/documentation/code/classes/classgambit_1_1iniparser_1_1inifile/#function-getobservables)**() const |
| const ObservablesType & | **[getRules](/documentation/code/classes/classgambit_1_1iniparser_1_1inifile/#function-getrules)**() const |
| const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[filename](/documentation/code/classes/classgambit_1_1iniparser_1_1inifile/#function-filename)**() const |
| virtual void | **[readFile](/documentation/code/classes/classgambit_1_1iniparser_1_1inifile/#function-readfile)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) name)<br>Read in the [YAML](/documentation/code/namespaces/namespaceyaml/) file.  |

## Additional inherited members

**Public Functions inherited from [Gambit::IniParser::Parser](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/)**

|                | Name           |
| -------------- | -------------- |
| YAML::Node | **[getParametersNode](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/#function-getparametersnode)**() const |
| YAML::Node | **[getPriorsNode](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/#function-getpriorsnode)**() const |
| YAML::Node | **[getPrinterNode](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/#function-getprinternode)**() const |
| YAML::Node | **[getScannerNode](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/#function-getscannernode)**() const |
| YAML::Node | **[getLoggerNode](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/#function-getloggernode)**() const |
| YAML::Node | **[getKeyValuePairNode](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/#function-getkeyvaluepairnode)**() const |
| template <typename... args\> <br>bool | **[hasKey](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/#function-haskey)**(args... keys) const |
| template <typename TYPE ,typename... args\> <br>TYPE | **[getValue](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/#function-getvalue)**(args... keys) const |
| template <typename TYPE ,typename... args\> <br>TYPE | **[getValueOrDef](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/#function-getvalueordef)**(TYPE def, const args &... keys) const |
| template <typename TYPE \> <br>TYPE | **[getModelParameterEntry](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/#function-getmodelparameterentry)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) model, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) param, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) key) const |
| bool | **[hasModelParameterEntry](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/#function-hasmodelparameterentry)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) model, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) param, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) key) const |
| const std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > | **[getModelNames](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/#function-getmodelnames)**() const<br>Return list of model names (without "adhoc" model!)  |
| const std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > | **[getModelParameters](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/#function-getmodelparameters)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) model) const |
| const [Options](/documentation/code/classes/classgambit_1_1options/) | **[getOptions](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/#function-getoptions)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) key) const<br>Getter for options.  |

**Protected Functions inherited from [Gambit::IniParser::Parser](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/)**

|                | Name           |
| -------------- | -------------- |
| YAML::Node | **[filename_to_node](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/#function-filename-to-node)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) filename)<br>Read in the actual [YAML](/documentation/code/namespaces/namespaceyaml/) file.  |
| void | **[basicParse](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/#function-basicparse)**(YAML::Node root, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) filename)<br>Do the basic parsing of the [YAML](/documentation/code/namespaces/namespaceyaml/) file.  |


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

**Reimplements**: [Gambit::IniParser::Parser::readFile](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/#function-readfile)


-------------------------------

Updated on 2022-09-08 at 02:23:01 +0000