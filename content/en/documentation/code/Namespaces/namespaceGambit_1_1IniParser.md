---
title: "namespace Gambit::IniParser"

description: "[No description available]"

---

# namespace Gambit::IniParser

[No description available]

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Gambit::IniParser::IniFile](/documentation/code/classes/classgambit_1_1iniparser_1_1inifile/)** <br>Main inifile class.  |
| class | **[Gambit::IniParser::Parser](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/)** <br>Inifile parser base class.  |

## Functions

|                | Name           |
| -------------- | -------------- |
| [error](/documentation/code/classes/classgambit_1_1error/) & | **[inifile_error](/documentation/code/namespaces/namespacegambit_1_1iniparser/#function-inifile-error)**()<br>[IniFile]() errors.  |
| [warning](/documentation/code/classes/classgambit_1_1warning/) & | **[inifile_warning](/documentation/code/namespaces/namespacegambit_1_1iniparser/#function-inifile-warning)**()<br>[IniFile]() warnings.  |
| int | **[importRound](/documentation/code/namespaces/namespacegambit_1_1iniparser/#function-importround)**(YAML::Node node, const std::string & filename)<br>Recursive import.  |
| void | **[recursiveImport](/documentation/code/namespaces/namespacegambit_1_1iniparser/#function-recursiveimport)**(const YAML::Node & node, const std::string & filename) |


## Functions Documentation

### function inifile_error

```
error & inifile_error()
```

[IniFile]() errors. 

### function inifile_warning

```
warning & inifile_warning()
```

[IniFile]() warnings. 

### function importRound

```
int importRound(
    YAML::Node node,
    const std::string & filename
)
```

Recursive import. 

### function recursiveImport

```
void recursiveImport(
    const YAML::Node & node,
    const std::string & filename
)
```






-------------------------------

Updated on 2025-02-12 at 16:10:32 +0000