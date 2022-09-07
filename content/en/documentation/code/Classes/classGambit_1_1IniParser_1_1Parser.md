---
title: 'class Gambit::IniParser::Parser'
description: 'Inifile parser base class. '

---

# Gambit::IniParser::Parser





Inifile parser base class. 


`#include <yaml_parser_base.hpp>`

Inherited by [Gambit::IniParser::IniFile](/documentation/code/classes/classgambit_1_1iniparser_1_1inifile/)

## Public Functions

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
| virtual void | **[readFile](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/#function-readfile)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) filename)<br>Read in the [YAML](/documentation/code/namespaces/namespaceyaml/) file.  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| YAML::Node | **[filename_to_node](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/#function-filename-to-node)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) filename)<br>Read in the actual [YAML](/documentation/code/namespaces/namespaceyaml/) file.  |
| void | **[basicParse](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/#function-basicparse)**(YAML::Node root, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) filename)<br>Do the basic parsing of the [YAML](/documentation/code/namespaces/namespaceyaml/) file.  |

## Public Functions Documentation

### function getParametersNode

```
YAML::Node getParametersNode() const
```


Getters for key/value section 


### function getPriorsNode

```
YAML::Node getPriorsNode() const
```


### function getPrinterNode

```
YAML::Node getPrinterNode() const
```


### function getScannerNode

```
YAML::Node getScannerNode() const
```


### function getLoggerNode

```
YAML::Node getLoggerNode() const
```


### function getKeyValuePairNode

```
YAML::Node getKeyValuePairNode() const
```


### function hasKey

```
template <typename... args>
inline bool hasKey(
    args... keys
) const
```


### function getValue

```
template <typename TYPE ,
typename... args>
inline TYPE getValue(
    args... keys
) const
```


### function getValueOrDef

```
template <typename TYPE ,
typename... args>
inline TYPE getValueOrDef(
    TYPE def,
    const args &... keys
) const
```


### function getModelParameterEntry

```
template <typename TYPE >
inline TYPE getModelParameterEntry(
    str model,
    str param,
    str key
) const
```


Getters for model/parameter section 


### function hasModelParameterEntry

```
bool hasModelParameterEntry(
    str model,
    str param,
    str key
) const
```


Getters for model/parameter section 


### function getModelNames

```
const std::set< str > getModelNames() const
```

Return list of model names (without "adhoc" model!) 

### function getModelParameters

```
const std::vector< str > getModelParameters(
    str model
) const
```


### function getOptions

```
const Options getOptions(
    str key
) const
```

Getter for options. 

### function readFile

```
virtual void readFile(
    str filename
)
```

Read in the [YAML](/documentation/code/namespaces/namespaceyaml/) file. 

**Reimplemented by**: [Gambit::IniParser::IniFile::readFile](/documentation/code/classes/classgambit_1_1iniparser_1_1inifile/#function-readfile)


## Protected Functions Documentation

### function filename_to_node

```
YAML::Node filename_to_node(
    str filename
)
```

Read in the actual [YAML](/documentation/code/namespaces/namespaceyaml/) file. 

### function basicParse

```
void basicParse(
    YAML::Node root,
    str filename
)
```

Do the basic parsing of the [YAML](/documentation/code/namespaces/namespaceyaml/) file. 

-------------------------------

Updated on 2022-09-07 at 13:49:50 +0000