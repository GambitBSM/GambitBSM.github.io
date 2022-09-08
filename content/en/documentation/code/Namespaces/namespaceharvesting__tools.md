---
title: "namespace harvesting_tools"

description: "[No description available]"

---

# namespace harvesting_tools

[No description available]

## Functions

|                | Name           |
| -------------- | -------------- |
| def | **[get_default_boss_namespaces](/documentation/code/namespaces/namespaceharvesting__tools/)**() |
| def | **[get_type_equivalencies](/documentation/code/namespaces/namespaceharvesting__tools/)**(nses nses) |
| def | **[comment_remover](/documentation/code/namespaces/namespaceharvesting__tools/)**(text text) |
| def | **[readlines_nocomments](/documentation/code/namespaces/namespaceharvesting__tools/)**(f f) |
| def | **[neatsplit](/documentation/code/namespaces/namespaceharvesting__tools/)**(regex regex, string string) |
| def | **[excluded](/documentation/code/namespaces/namespaceharvesting__tools/)**(string string, st st) |
| def | **[sorted_nicely](/documentation/code/namespaces/namespaceharvesting__tools/)**(l l) |
| def | **[check_for_declaration](/documentation/code/namespaces/namespaceharvesting__tools/)**(input_snippet input_snippet, module module, all_modules all_modules, local_namespace local_namespace, candidate_type candidate_type) |
| def | **[check_for_namespace](/documentation/code/namespaces/namespaceharvesting__tools/)**(input_snippet input_snippet, local_namespace local_namespace) |
| def | **[addifheader](/documentation/code/namespaces/namespaceharvesting__tools/)**(line line, headerset headerset, exclude_set exclude_set, verbose verbose =False) |
| def | **[update_module](/documentation/code/namespaces/namespaceharvesting__tools/)**(line line, module module) |
| def | **[first_simple_type_equivalent](/documentation/code/namespaces/namespaceharvesting__tools/)**(candidate_in candidate_in, equivs equivs, nses nses, existing existing) |
| def | **[strip_ws](/documentation/code/namespaces/namespaceharvesting__tools/)**(s s, qualifiers qualifiers) |
| def | **[addiffunctormacro](/documentation/code/namespaces/namespaceharvesting__tools/)**(line line, module module, all_modules all_modules, typedict typedict, typeheaders typeheaders, intrinsic_types intrinsic_types, exclude_types exclude_types, equiv_classes equiv_classes, equiv_ns equiv_ns, verbose verbose =False) |
| def | **[addifbefunctormacro](/documentation/code/namespaces/namespaceharvesting__tools/)**(line line, be_typeset be_typeset, type_pack_set type_pack_set, equiv_classes equiv_classes, equiv_ns equiv_ns, verbose verbose =False) |
| def | **[get_headers](/documentation/code/namespaces/namespaceharvesting__tools/)**(path path, header_set header_set, exclude_set exclude_set, verbose verbose =False) |
| def | **[find_and_harvest_headers](/documentation/code/namespaces/namespaceharvesting__tools/)**(header_set header_set, fullheadlist fullheadlist, exclude_set exclude_set, dir_exclude_set dir_exclude_set, verbose verbose =False) |
| def | **[retrieve_rollcall_headers](/documentation/code/namespaces/namespaceharvesting__tools/)**(verbose verbose, install_dir install_dir, excludes excludes) |
| def | **[retrieve_module_type_headers](/documentation/code/namespaces/namespaceharvesting__tools/)**(verbose verbose, install_dir install_dir, excludes excludes) |
| def | **[get_all_files_with_ext](/documentation/code/namespaces/namespaceharvesting__tools/)**(verbose verbose, starting_dir starting_dir, ext_set ext_set, kind kind) |
| def | **[retrieve_generic_headers](/documentation/code/namespaces/namespaceharvesting__tools/)**(verbose verbose, starting_dir starting_dir, kind kind, excludes excludes, exclude_list exclude_list =[]) |
| def | **[same](/documentation/code/namespaces/namespaceharvesting__tools/)**(f1 f1, f2 f2) |
| def | **[update_only_if_different](/documentation/code/namespaces/namespaceharvesting__tools/)**(existing existing, candidate candidate, verbose verbose =True) |
| def | **[make_module_rollcall](/documentation/code/namespaces/namespaceharvesting__tools/)**(rollcall_headers rollcall_headers, verbose verbose) |

## Attributes

|                | Name           |
| -------------- | -------------- |
| string | **[default_bossed_versions](/documentation/code/namespaces/namespaceharvesting__tools/)**  |
| string | **[equiv_config](/documentation/code/namespaces/namespaceharvesting__tools/)**  |


## Functions Documentation

### function get_default_boss_namespaces

```
def get_default_boss_namespaces()
```


### function get_type_equivalencies

```
def get_type_equivalencies(
    nses nses
)
```


### function comment_remover

```
def comment_remover(
    text text
)
```


### function readlines_nocomments

```
def readlines_nocomments(
    f f
)
```


### function neatsplit

```
def neatsplit(
    regex regex,
    string string
)
```


### function excluded

```
def excluded(
    string string,
    st st
)
```


### function sorted_nicely

```
def sorted_nicely(
    l l
)
```




```
 Sort the given iterable in the way that humans expect.```


### function check_for_declaration

```
def check_for_declaration(
    input_snippet input_snippet,
    module module,
    all_modules all_modules,
    local_namespace local_namespace,
    candidate_type candidate_type
)
```


### function check_for_namespace

```
def check_for_namespace(
    input_snippet input_snippet,
    local_namespace local_namespace
)
```


### function addifheader

```
def addifheader(
    line line,
    headerset headerset,
    exclude_set exclude_set,
    verbose verbose =False
)
```


### function update_module

```
def update_module(
    line line,
    module module
)
```


### function first_simple_type_equivalent

```
def first_simple_type_equivalent(
    candidate_in candidate_in,
    equivs equivs,
    nses nses,
    existing existing
)
```


### function strip_ws

```
def strip_ws(
    s s,
    qualifiers qualifiers
)
```


### function addiffunctormacro

```
def addiffunctormacro(
    line line,
    module module,
    all_modules all_modules,
    typedict typedict,
    typeheaders typeheaders,
    intrinsic_types intrinsic_types,
    exclude_types exclude_types,
    equiv_classes equiv_classes,
    equiv_ns equiv_ns,
    verbose verbose =False
)
```


### function addifbefunctormacro

```
def addifbefunctormacro(
    line line,
    be_typeset be_typeset,
    type_pack_set type_pack_set,
    equiv_classes equiv_classes,
    equiv_ns equiv_ns,
    verbose verbose =False
)
```


### function get_headers

```
def get_headers(
    path path,
    header_set header_set,
    exclude_set exclude_set,
    verbose verbose =False
)
```




```
Parse the file at 'path' and add any headers that are "include"ed therin to the set 'header_set'```


### function find_and_harvest_headers

```
def find_and_harvest_headers(
    header_set header_set,
    fullheadlist fullheadlist,
    exclude_set exclude_set,
    dir_exclude_set dir_exclude_set,
    verbose verbose =False
)
```




```
Locate 'init_headers' in gambit source tree, then read through them and add any headers that are "include"ed in them to headlist
Args:
header_set - set of file names of headers to parse
fullheadlist - list to which full paths of both init_headers, and any subsequently found headers, should be added.
exclude_set - set of names of headers to ignore if we find them.
dir_exclude_set - set of directory names to skip over during the os.walk
```


### function retrieve_rollcall_headers

```
def retrieve_rollcall_headers(
    verbose verbose,
    install_dir install_dir,
    excludes excludes
)
```


### function retrieve_module_type_headers

```
def retrieve_module_type_headers(
    verbose verbose,
    install_dir install_dir,
    excludes excludes
)
```


### function get_all_files_with_ext

```
def get_all_files_with_ext(
    verbose verbose,
    starting_dir starting_dir,
    ext_set ext_set,
    kind kind
)
```


### function retrieve_generic_headers

```
def retrieve_generic_headers(
    verbose verbose,
    starting_dir starting_dir,
    kind kind,
    excludes excludes,
    exclude_list exclude_list =[]
)
```


### function same

```
def same(
    f1 f1,
    f2 f2
)
```


### function update_only_if_different

```
def update_only_if_different(
    existing existing,
    candidate candidate,
    verbose verbose =True
)
```


### function make_module_rollcall

```
def make_module_rollcall(
    rollcall_headers rollcall_headers,
    verbose verbose
)
```



## Attributes Documentation

### variable default_bossed_versions

```
string default_bossed_versions =  "./Backends/include/gambit/Backends/default_bossed_versions.hpp";
```


### variable equiv_config

```
string equiv_config =  "./config/resolution_type_equivalency_classes.yaml";
```





-------------------------------

Updated on 2022-09-08 at 01:05:15 +0000