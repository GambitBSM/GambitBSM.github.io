---
title: "struct Gambit::Scanner::Plugins::pluginData"
description: "Structure that holds all the data provided by plugins about themselves. "

---

# struct Gambit::Scanner::Plugins::pluginData



Structure that holds all the data provided by plugins about themselves. 


`#include <plugin_defs.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[pluginData](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugindata/#function-gambitscannerpluginsplugindata-plugindata)**(const std::string & name, const std::string & type, const std::string & version_in) |
| std::string | **[print](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugindata/#function-gambitscannerpluginsplugindata-print)**() |
| | **[~pluginData](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugindata/#function-gambitscannerpluginsplugindata-plugindata)**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| std::string | **[name](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugindata/#variable-gambitscannerpluginsplugindata-name)**  |
| std::string | **[type](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugindata/#variable-gambitscannerpluginsplugindata-type)**  |
| std::string | **[version](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugindata/#variable-gambitscannerpluginsplugindata-version)**  |
| std::string | **[tag](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugindata/#variable-gambitscannerpluginsplugindata-tag)**  |
| YAML::Node | **[node](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugindata/#variable-gambitscannerpluginsplugindata-node)**  |
| [printer_interface](/documentation/code/namespaces/namespacegambit_1_1scanner/#typedef-gambitscanner-printer-interface) * | **[printer](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugindata/#variable-gambitscannerpluginsplugindata-printer)**  |
| [prior_interface](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/) * | **[prior](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugindata/#variable-gambitscannerpluginsplugindata-prior)**  |
| std::vector< void * > | **[inputData](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugindata/#variable-gambitscannerpluginsplugindata-inputdata)**  |
| std::vector< void(*)([pluginData](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugindata/) &)> | **[inits](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugindata/#variable-gambitscannerpluginsplugindata-inits)**  |
| std::map< std::string, [factoryBase](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1factorybase/) * > | **[outputFuncs](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugindata/#variable-gambitscannerpluginsplugindata-outputfuncs)**  |
| std::map< [type_index](/documentation/code/classes/structgambit_1_1type__index/), void * > | **[plugin_mains](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugindata/#variable-gambitscannerpluginsplugindata-plugin-mains)**  |
| void(*)() | **[deconstructor](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugindata/#variable-gambitscannerpluginsplugindata-deconstructor)**  |
| bool | **[loaded](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugindata/#variable-gambitscannerpluginsplugindata-loaded)**  |

## Public Functions Documentation

### function pluginData

```
inline pluginData(
    const std::string & name,
    const std::string & type,
    const std::string & version_in
)
```


### function print

```
inline std::string print()
```


### function ~pluginData

```
inline ~pluginData()
```


## Public Attributes Documentation

### variable name

```
std::string name;
```


### variable type

```
std::string type;
```


### variable version

```
std::string version;
```


### variable tag

```
std::string tag;
```


### variable node

```
YAML::Node node;
```


### variable printer

```
printer_interface * printer;
```


### variable prior

```
prior_interface * prior;
```


### variable inputData

```
std::vector< void * > inputData;
```


### variable inits

```
std::vector< void(*)(pluginData &)> inits;
```


### variable outputFuncs

```
std::map< std::string, factoryBase * > outputFuncs;
```


### variable plugin_mains

```
std::map< type_index, void * > plugin_mains;
```


### variable deconstructor

```
void(*)() deconstructor;
```


### variable loaded

```
bool loaded;
```


-------------------------------

Updated on 2022-09-08 at 01:48:56 +0000