---
title: "struct Gambit::Scanner::Plugins::Plugin_Details"
description: "container info for a specific plugin "

---

# struct Gambit::Scanner::Plugins::Plugin_Details



container info for a specific plugin 


`#include <plugin_details.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Plugin_Details](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugin__details/)**() |
| std::multimap< std::string, std::string > | **[linked_libraries](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugin__details/)**() const |
| | **[Plugin_Details](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugin__details/)**(const std::string & str) |
| void | **[get_status](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugin__details/)**(const YAML::Node & libNode, const YAML::Node & plugNode, const YAML::Node & flagNode) |
| std::string | **[printMin](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugin__details/)**() const |
| std::string | **[print](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugin__details/)**() const |
| std::string | **[printFull](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugin__details/)**() const |
| std::string | **[get_description](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugin__details/)**(const std::vector< const [Plugin_Details](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugin__details/) * > & plugins) |
| std::string | **[printMultiPlugins](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugin__details/)**(const std::vector< const [Plugin_Details](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugin__details/) * > & plugins) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| std::string | **[version](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugin__details/)** <br>version string: maj.min.patch-release  |
| int | **[major_version](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugin__details/)** <br>major version number  |
| int | **[minor_version](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugin__details/)** <br>minor version number  |
| int | **[patch_version](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugin__details/)** <br>patch version number  |
| std::string | **[status](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugin__details/)** <br>status, not set right now  |
| std::vector< std::string > | **[reason](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugin__details/)** <br>reason is excluded  |
| std::string | **[release_version](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugin__details/)** <br>release version  |
| std::string | **[path](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugin__details/)** <br>full path to library containing plugin  |
| std::string | **[plugin](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugin__details/)** <br>plugin name  |
| std::string | **[type](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugin__details/)** <br>plugin type  |
| std::string | **[full_string](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugin__details/)** <br>full string that ScannerBit sees  |
| std::vector< std::string > | **[reqd_inifile_entries](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugin__details/)** <br>inifile entries requested my plugin in the "reqd_inifile_entries(...)" function  |
| std::vector< std::string > | **[reqd_not_linked_libs](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugin__details/)** <br>libraries that were not linked but requested by the "reqd_libraries(...)" function  |
| std::vector< std::string > | **[ini_libs_not_found](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugin__details/)** <br>libraries specified in the "locations.yaml" file but not found  |
| std::multimap< std::string, std::string > | **[linked_libs](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugin__details/)** <br>list of all libraries that are linked: {lib_name: path_to_lib}  |
| std::vector< std::string > | **[reqd_incs_not_found](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugin__details/)** <br>requested include files that were not found  |
| std::vector< std::string > | **[ini_incs_not_found](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugin__details/)** <br>paths specified in the "locations.yaml" file but where not found  |
| std::multimap< std::string, std::string > | **[found_incs](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugin__details/)** <br>list of all files that were found: {file_name: include_path_to_file}  |
| YAML::Node | **[flags](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugin__details/)** <br>flag list  |

## Public Functions Documentation

### function Plugin_Details

```
inline Plugin_Details()
```


### function linked_libraries

```
inline std::multimap< std::string, std::string > linked_libraries() const
```


### function Plugin_Details

```
Plugin_Details(
    const std::string & str
)
```


### function get_status

```
void get_status(
    const YAML::Node & libNode,
    const YAML::Node & plugNode,
    const YAML::Node & flagNode
)
```


### function printMin

```
std::string printMin() const
```


### function print

```
std::string print() const
```


### function printFull

```
std::string printFull() const
```


### function get_description

```
static std::string get_description(
    const std::vector< const Plugin_Details * > & plugins
)
```


### function printMultiPlugins

```
static std::string printMultiPlugins(
    const std::vector< const Plugin_Details * > & plugins
)
```


## Public Attributes Documentation

### variable version

```
std::string version;
```

version string: maj.min.patch-release 

### variable major_version

```
int major_version;
```

major version number 

### variable minor_version

```
int minor_version;
```

minor version number 

### variable patch_version

```
int patch_version;
```

patch version number 

### variable status

```
std::string status;
```

status, not set right now 

### variable reason

```
std::vector< std::string > reason;
```

reason is excluded 

### variable release_version

```
std::string release_version;
```

release version 

### variable path

```
std::string path;
```

full path to library containing plugin 

### variable plugin

```
std::string plugin;
```

plugin name 

### variable type

```
std::string type;
```

plugin type 

### variable full_string

```
std::string full_string;
```

full string that ScannerBit sees 

### variable reqd_inifile_entries

```
std::vector< std::string > reqd_inifile_entries;
```

inifile entries requested my plugin in the "reqd_inifile_entries(...)" function 

### variable reqd_not_linked_libs

```
std::vector< std::string > reqd_not_linked_libs;
```

libraries that were not linked but requested by the "reqd_libraries(...)" function 

### variable ini_libs_not_found

```
std::vector< std::string > ini_libs_not_found;
```

libraries specified in the "locations.yaml" file but not found 

### variable linked_libs

```
std::multimap< std::string, std::string > linked_libs;
```

list of all libraries that are linked: {lib_name: path_to_lib} 

### variable reqd_incs_not_found

```
std::vector< std::string > reqd_incs_not_found;
```

requested include files that were not found 

### variable ini_incs_not_found

```
std::vector< std::string > ini_incs_not_found;
```

paths specified in the "locations.yaml" file but where not found 

### variable found_incs

```
std::multimap< std::string, std::string > found_incs;
```

list of all files that were found: {file_name: include_path_to_file} 

### variable flags

```
YAML::Node flags;
```

flag list 

-------------------------------

Updated on 2022-09-08 at 01:05:18 +0000