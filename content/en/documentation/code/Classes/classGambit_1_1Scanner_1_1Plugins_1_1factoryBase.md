---
title: "class Gambit::Scanner::Plugins::factoryBase"

description: "[No description available]"

---

# class Gambit::Scanner::Plugins::factoryBase



[No description available] [More...](#detailed-description)


`#include <plugin_defs.hpp>`

Inherited by [Gambit::Scanner::Plugins::classFactory< T >](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1classfactory/), [Gambit::Scanner::Plugins::funcFactory< T >](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1funcfactory/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual void * | **[operator()](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1factorybase/#function-gambitscannerpluginsfactorybase-operator)**() =0 |
| virtual | **[~factoryBase](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1factorybase/#function-gambitscannerpluginsfactorybase-factorybase)**() |

## Detailed Description

```
class Gambit::Scanner::Plugins::factoryBase;
```


These classes are used by the plugins to load and save data 

## Public Functions Documentation

### function operator()

```
virtual void * operator()() =0
```


**Reimplemented by**: [Gambit::Scanner::Plugins::funcFactory::operator()](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1funcfactory/#function-gambitscannerpluginsfuncfactory-operator), [Gambit::Scanner::Plugins::classFactory::operator()](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1classfactory/#function-gambitscannerpluginsclassfactory-operator)


### function ~factoryBase

```
inline virtual ~factoryBase()
```


-------------------------------

Updated on 2022-09-08 at 02:00:49 +0000