---
title: "namespace configs::vevacious_1_0"

description: "[No description available]"

---

# namespace configs::vevacious_1_0

[No description available]

## Attributes

|                | Name           |
| -------------- | -------------- |
| string | **[castxml_cc_id](/documentation/code/namespaces/namespaceconfigs_1_1vevacious__1__0/)**  |
| string | **[castxml_cc](/documentation/code/namespaces/namespaceconfigs_1_1vevacious__1__0/)**  |
| string | **[castxml_cc_opt](/documentation/code/namespaces/namespaceconfigs_1_1vevacious__1__0/)**  |
| string | **[gambit_backend_name](/documentation/code/namespaces/namespaceconfigs_1_1vevacious__1__0/)**  |
| string | **[gambit_backend_version](/documentation/code/namespaces/namespaceconfigs_1_1vevacious__1__0/)**  |
| string | **[gambit_backend_reference](/documentation/code/namespaces/namespaceconfigs_1_1vevacious__1__0/)**  |
| string | **[gambit_base_namespace](/documentation/code/namespaces/namespaceconfigs_1_1vevacious__1__0/)**  |
| string | **[gambit_minuit_version](/documentation/code/namespaces/namespaceconfigs_1_1vevacious__1__0/)**  |
| list | **[input_files](/documentation/code/namespaces/namespaceconfigs_1_1vevacious__1__0/)**  |
| list | **[include_paths](/documentation/code/namespaces/namespaceconfigs_1_1vevacious__1__0/)**  |
| list | **[base_paths](/documentation/code/namespaces/namespaceconfigs_1_1vevacious__1__0/)**  |
| string | **[header_files_to](/documentation/code/namespaces/namespaceconfigs_1_1vevacious__1__0/)**  |
| string | **[src_files_to](/documentation/code/namespaces/namespaceconfigs_1_1vevacious__1__0/)**  |
| list | **[load_classes](/documentation/code/namespaces/namespaceconfigs_1_1vevacious__1__0/)**  |
| list | **[load_functions](/documentation/code/namespaces/namespaceconfigs_1_1vevacious__1__0/)**  |
| list | **[ditch](/documentation/code/namespaces/namespaceconfigs_1_1vevacious__1__0/)**  |
| bool | **[auto_detect_stdlib_paths](/documentation/code/namespaces/namespaceconfigs_1_1vevacious__1__0/)**  |
| bool | **[load_parent_classes](/documentation/code/namespaces/namespaceconfigs_1_1vevacious__1__0/)**  |
| bool | **[wrap_inherited_members](/documentation/code/namespaces/namespaceconfigs_1_1vevacious__1__0/)**  |
| string | **[header_extension](/documentation/code/namespaces/namespaceconfigs_1_1vevacious__1__0/)**  |
| string | **[source_extension](/documentation/code/namespaces/namespaceconfigs_1_1vevacious__1__0/)**  |
| int | **[indent](/documentation/code/namespaces/namespaceconfigs_1_1vevacious__1__0/)**  |
| dictionary | **[known_classes](/documentation/code/namespaces/namespaceconfigs_1_1vevacious__1__0/)**  |
| list | **[pragmas_begin](/documentation/code/namespaces/namespaceconfigs_1_1vevacious__1__0/)**  |
| list | **[pragmas_end](/documentation/code/namespaces/namespaceconfigs_1_1vevacious__1__0/)**  |



## Attributes Documentation

### variable castxml_cc_id

```
string castxml_cc_id =  'gnu';
```




```
                           #
```

 Configuration module for BOSS # # 


### variable castxml_cc

```
string castxml_cc =  'g++';
```


### variable castxml_cc_opt

```
string castxml_cc_opt =  '-std=c++11';
```


### variable gambit_backend_name

```
string gambit_backend_name =  'vevacious';
```


### variable gambit_backend_version

```
string gambit_backend_version =  '1.0';
```


### variable gambit_backend_reference

```
string gambit_backend_reference =  'Camargo-Molina:2013qva';
```


### variable gambit_base_namespace

```
string gambit_base_namespace =  '';
```


### variable gambit_minuit_version

```
string gambit_minuit_version =  '6.23.01';
```


### variable input_files

```
list input_files =  [
    '../../../Backends/installed/'+gambit_backend_name+'/'+gambit_backend_version+'/include/VevaciousPlusPlus.hpp',
];
```


### variable include_paths

```
list include_paths =  [
    '../../../Backends/installed/'+gambit_backend_name+'/'+gambit_backend_version+'/include',
    '../../../Backends/installed/'+gambit_backend_name+'/'+gambit_backend_version+'/include/LHPC',
    '../../../ScannerBit/installed/minuit2/'+gambit_minuit_version+'/inc',
#    '../../../contrib/eigen3.2.8' # This should be learned from GAMBIT somehow to future-protect against version changes (and if user uses own library!)
];
```


### variable base_paths

```
list base_paths =  ['../../../Backends/installed/'+gambit_backend_name+'/'+gambit_backend_version];
```


### variable header_files_to

```
string header_files_to =  '../../../Backends/installed/'+gambit_backend_name+'/'+gambit_backend_version+'/include';
```


### variable src_files_to

```
string src_files_to =  '../../../Backends/installed/'+gambit_backend_name+'/'+gambit_backend_version+'/source';
```


### variable load_classes

```
list load_classes =  [
  'VevaciousPlusPlus::VevaciousPlusPlus'
];
```


### variable load_functions

```
list load_functions =  [
];
```


### variable ditch

```
list ditch =  [];
```


### variable auto_detect_stdlib_paths

```
bool auto_detect_stdlib_paths =  False;
```


### variable load_parent_classes

```
bool load_parent_classes =  False;
```


### variable wrap_inherited_members

```
bool wrap_inherited_members =  False;
```


### variable header_extension

```
string header_extension =  '.hpp';
```


### variable source_extension

```
string source_extension =  '.cpp';
```


### variable indent

```
int indent =  4;
```


### variable known_classes

```
dictionary known_classes =  {
#    "Eigen::Matrix" : "<Eigen/Core>",
#    "Eigen::Array" : "<Eigen/Core>",
};
```


### variable pragmas_begin

```
list pragmas_begin =  [
];
```


### variable pragmas_end

```
list pragmas_end =  [
];
```





-------------------------------

Updated on 2022-09-08 at 01:05:18 +0000