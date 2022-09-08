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
| const ObservablesType & | **[getObservables](/documentation/code/classes/classgambit_1_1iniparser_1_1inifile/#function-gambitiniparserinifile-getobservables)**() const |
| const ObservablesType & | **[getRules](/documentation/code/classes/classgambit_1_1iniparser_1_1inifile/#function-gambitiniparserinifile-getrules)**() const |
| const [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[filename](/documentation/code/classes/classgambit_1_1iniparser_1_1inifile/#function-gambitiniparserinifile-filename)**() const |
| virtual void | **[readFile](/documentation/code/classes/classgambit_1_1iniparser_1_1inifile/#function-gambitiniparserinifile-readfile)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) name)<br>Read in the [YAML](/documentation/code/namespaces/namespaceyaml/) file.  |

## Additional inherited members

**Public Functions inherited from [Gambit::IniParser::Parser](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/)**

|                | Name           |
| -------------- | -------------- |
| YAML::Node | **[getParametersNode](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/#function-gambitiniparserparser-getparametersnode)**() const |
| YAML::Node | **[getPriorsNode](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/#function-gambitiniparserparser-getpriorsnode)**() const |
| YAML::Node | **[getPrinterNode](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/#function-gambitiniparserparser-getprinternode)**() const |
| YAML::Node | **[getScannerNode](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/#function-gambitiniparserparser-getscannernode)**() const |
| YAML::Node | **[getLoggerNode](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/#function-gambitiniparserparser-getloggernode)**() const |
| YAML::Node | **[getKeyValuePairNode](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/#function-gambitiniparserparser-getkeyvaluepairnode)**() const |
| template <typename... args\> <br>bool | **[hasKey](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/#function-gambitiniparserparser-haskey)**(args... keys) const |
| template <typename TYPE ,typename... args\> <br>TYPE | **[getValue](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/#function-gambitiniparserparser-getvalue)**(args... keys) const |
| template <typename TYPE ,typename... args\> <br>TYPE | **[getValueOrDef](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/#function-gambitiniparserparser-getvalueordef)**(TYPE def, const args &... keys) const |
| template <typename TYPE \> <br>TYPE | **[getModelParameterEntry](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/#function-gambitiniparserparser-getmodelparameterentry)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) model, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) param, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) key) const |
| bool | **[hasModelParameterEntry](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/#function-gambitiniparserparser-hasmodelparameterentry)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) model, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) param, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) key) const |
| const std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) > | **[getModelNames](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/#function-gambitiniparserparser-getmodelnames)**() const<br>Return list of model names (without "adhoc" model!)  |
| const std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) > | **[getModelParameters](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/#function-gambitiniparserparser-getmodelparameters)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) model) const |
| const [Options](/documentation/code/classes/classgambit_1_1options/) | **[getOptions](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/#function-gambitiniparserparser-getoptions)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) key) const<br>Getter for options.  |

**Protected Functions inherited from [Gambit::IniParser::Parser](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/)**

|                | Name           |
| -------------- | -------------- |
| YAML::Node | **[filename_to_node](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/#function-gambitiniparserparser-filename-to-node)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) filename)<br>Read in the actual [YAML](/documentation/code/namespaces/namespaceyaml/) file.  |
| void | **[basicParse](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/#function-gambitiniparserparser-basicparse)**(YAML::Node root, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) filename)<br>Do the basic parsing of the [YAML](/documentation/code/namespaces/namespaceyaml/) file.  |


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

**Reimplements**: [Gambit::IniParser::Parser::readFile](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/#function-gambitiniparserparser-readfile)


-------------------------------

Updated on 2022-09-08 at 02:00:48 +0000