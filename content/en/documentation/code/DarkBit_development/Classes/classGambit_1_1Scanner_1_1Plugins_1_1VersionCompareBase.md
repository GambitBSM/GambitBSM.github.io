---
title: 'class Gambit::Scanner::Plugins::VersionCompareBase'
description: 'Base class for comparing scanner plugins. '

---








Base class for comparing scanner plugins. 


`#include <plugin_comparators.hpp>`

Inherited by [Gambit::Scanner::Plugins::VersionCompare](/documentation/code/darkbit_development/classes/classgambit_1_1scanner_1_1plugins_1_1versioncompare/), [Gambit::Scanner::Plugins::VersionCompareBottom](/documentation/code/darkbit_development/classes/classgambit_1_1scanner_1_1plugins_1_1versioncomparebottom/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[VersionCompareBase](/documentation/code/darkbit_development/classes/classgambit_1_1scanner_1_1plugins_1_1versioncomparebase/#function-versioncomparebase)**() |
| virtual bool | **[operator()](/documentation/code/darkbit_development/classes/classgambit_1_1scanner_1_1plugins_1_1versioncomparebase/#function-operator())**(const [Plugin_Details](/documentation/code/darkbit_development/classes/structgambit_1_1scanner_1_1plugins_1_1plugin__details/) & ) =0 |
| bool | **[isEmpty](/documentation/code/darkbit_development/classes/classgambit_1_1scanner_1_1plugins_1_1versioncomparebase/#function-isempty)**() const |
| void | **[setEmpty](/documentation/code/darkbit_development/classes/classgambit_1_1scanner_1_1plugins_1_1versioncomparebase/#function-setempty)**(bool in) |
| virtual | **[~VersionCompareBase](/documentation/code/darkbit_development/classes/classgambit_1_1scanner_1_1plugins_1_1versioncomparebase/#function-~versioncomparebase)**() |

## Public Functions Documentation

### function VersionCompareBase

```
inline VersionCompareBase()
```


### function operator()

```
virtual bool operator()(
    const Plugin_Details & 
) =0
```


**Reimplemented by**: [Gambit::Scanner::Plugins::VersionCompareBottom::operator()](/documentation/code/darkbit_development/classes/classgambit_1_1scanner_1_1plugins_1_1versioncomparebottom/#function-operator()), [Gambit::Scanner::Plugins::VersionCompare::operator()](/documentation/code/darkbit_development/classes/classgambit_1_1scanner_1_1plugins_1_1versioncompare/#function-operator())


### function isEmpty

```
inline bool isEmpty() const
```


### function setEmpty

```
inline void setEmpty(
    bool in
)
```


### function ~VersionCompareBase

```
inline virtual ~VersionCompareBase()
```


-------------------------------

Updated on 2022-08-03 at 03:16:52 +0000