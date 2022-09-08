---
title: "class Gambit::Scanner::Plugins::VersionCompare"

description: "[No description available]"

---

# class Gambit::Scanner::Plugins::VersionCompare



[No description available]

Inherits from [Gambit::Scanner::Plugins::VersionCompareBase](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1versioncomparebase/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[VersionCompare](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1versioncompare/#function-gambitscannerpluginsversioncompare-versioncompare)**(const std::string & version) |
| virtual bool | **[operator()](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1versioncompare/#function-gambitscannerpluginsversioncompare-operator)**(const [Plugin_Details](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugin__details/) & plugin) |
| | **[~VersionCompare](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1versioncompare/#function-gambitscannerpluginsversioncompare-versioncompare)**() |

## Additional inherited members

**Public Functions inherited from [Gambit::Scanner::Plugins::VersionCompareBase](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1versioncomparebase/)**

|                | Name           |
| -------------- | -------------- |
| | **[VersionCompareBase](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1versioncomparebase/#function-gambitscannerpluginsversioncomparebase-versioncomparebase)**() |
| bool | **[isEmpty](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1versioncomparebase/#function-gambitscannerpluginsversioncomparebase-isempty)**() const |
| void | **[setEmpty](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1versioncomparebase/#function-gambitscannerpluginsversioncomparebase-setempty)**(bool in) |
| virtual | **[~VersionCompareBase](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1versioncomparebase/#function-gambitscannerpluginsversioncomparebase-versioncomparebase)**() |


## Public Functions Documentation

### function VersionCompare

```
VersionCompare(
    const std::string & version
)
```


### function operator()

```
virtual bool operator()(
    const Plugin_Details & plugin
)
```


**Reimplements**: [Gambit::Scanner::Plugins::VersionCompareBase::operator()](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1versioncomparebase/#function-gambitscannerpluginsversioncomparebase-operator)


### function ~VersionCompare

```
~VersionCompare()
```


-------------------------------

Updated on 2022-09-08 at 02:00:49 +0000