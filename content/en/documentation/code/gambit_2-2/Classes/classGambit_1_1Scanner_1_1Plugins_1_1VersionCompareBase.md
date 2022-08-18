---
title: 'class Gambit::Scanner::Plugins::VersionCompareBase'
description: 'Base class for comparing scanner plugins. '

---








Base class for comparing scanner plugins. 


`#include <plugin_comparators.hpp>`

Inherited by [Gambit::Scanner::Plugins::VersionCompare](/documentation/code/gambit_2-2/classes/classgambit_1_1scanner_1_1plugins_1_1versioncompare/), [Gambit::Scanner::Plugins::VersionCompareBottom](/documentation/code/gambit_2-2/classes/classgambit_1_1scanner_1_1plugins_1_1versioncomparebottom/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[VersionCompareBase](/documentation/code/gambit_2-2/classes/classgambit_1_1scanner_1_1plugins_1_1versioncomparebase/#function-versioncomparebase)**() |
| virtual bool | **[operator()](/documentation/code/gambit_2-2/classes/classgambit_1_1scanner_1_1plugins_1_1versioncomparebase/#function-operator())**(const [Plugin_Details](/documentation/code/gambit_2-2/classes/structgambit_1_1scanner_1_1plugins_1_1plugin__details/) & ) =0 |
| bool | **[isEmpty](/documentation/code/gambit_2-2/classes/classgambit_1_1scanner_1_1plugins_1_1versioncomparebase/#function-isempty)**() const |
| void | **[setEmpty](/documentation/code/gambit_2-2/classes/classgambit_1_1scanner_1_1plugins_1_1versioncomparebase/#function-setempty)**(bool in) |
| virtual | **[~VersionCompareBase](/documentation/code/gambit_2-2/classes/classgambit_1_1scanner_1_1plugins_1_1versioncomparebase/#function-~versioncomparebase)**() |

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


**Reimplemented by**: [Gambit::Scanner::Plugins::VersionCompareBottom::operator()](/documentation/code/gambit_2-2/classes/classgambit_1_1scanner_1_1plugins_1_1versioncomparebottom/#function-operator()), [Gambit::Scanner::Plugins::VersionCompare::operator()](/documentation/code/gambit_2-2/classes/classgambit_1_1scanner_1_1plugins_1_1versioncompare/#function-operator())


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

Updated on 2022-08-10 at 17:51:35 +0000