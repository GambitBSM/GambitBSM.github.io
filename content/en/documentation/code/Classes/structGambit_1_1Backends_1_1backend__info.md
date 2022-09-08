---
title: "struct Gambit::Backends::backend_info"
description: "Structure providing some basic info on backend libraries. "

---

# struct Gambit::Backends::backend_info



Structure providing some basic info on backend libraries. 


`#include <backend_info.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[backend_info](/documentation/code/classes/structgambit_1_1backends_1_1backend__info/)**()<br>Constructor.  |
| | **[~backend_info](/documentation/code/classes/structgambit_1_1backends_1_1backend__info/)**()<br>Destructor.  |
| bool | **[custom_locations_exist](/documentation/code/classes/structgambit_1_1backends_1_1backend__info/)**() const<br>Indicate whether a custom backend locations file exists.  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[backend_locations](/documentation/code/classes/structgambit_1_1backends_1_1backend__info/)**() const<br>Return the path to any custom user backend locations file.  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[default_backend_locations](/documentation/code/classes/structgambit_1_1backends_1_1backend__info/)**() const<br>Return the path to the default backend locations file.  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[path](/documentation/code/classes/structgambit_1_1backends_1_1backend__info/)**([str](/documentation/code/namespaces/namespacegambit/) be, [str](/documentation/code/namespaces/namespacegambit/) ver) const<br>Return the path to a backend library.  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[corrected_path](/documentation/code/classes/structgambit_1_1backends_1_1backend__info/)**([str](/documentation/code/namespaces/namespacegambit/) be, [str](/documentation/code/namespaces/namespacegambit/) ver) const<br>Return the path to a backend library with GAMBIT_DIR expanded.  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[path_dir](/documentation/code/classes/structgambit_1_1backends_1_1backend__info/)**([str](/documentation/code/namespaces/namespacegambit/) be, [str](/documentation/code/namespaces/namespacegambit/) ver) const<br>Return the path to the folder in which a backend library resides.  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[lib_name](/documentation/code/classes/structgambit_1_1backends_1_1backend__info/)**([str](/documentation/code/namespaces/namespacegambit/) be, [str](/documentation/code/namespaces/namespacegambit/) ver) const<br>Return the bare name of the library of a backend library, with no path or extension.  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[version_from_safe_version](/documentation/code/classes/structgambit_1_1backends_1_1backend__info/)**([str](/documentation/code/namespaces/namespacegambit/) be, [str](/documentation/code/namespaces/namespacegambit/) sv) const<br>Given a backend and a safe version (with no periods), return the true version.  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[safe_version_from_version](/documentation/code/classes/structgambit_1_1backends_1_1backend__info/)**([str](/documentation/code/namespaces/namespacegambit/) be, [str](/documentation/code/namespaces/namespacegambit/) v) const<br>Given a backend and a true version (with periods), return the safe version.  |
| void | **[link_versions](/documentation/code/classes/structgambit_1_1backends_1_1backend__info/)**([str](/documentation/code/namespaces/namespacegambit/) be, [str](/documentation/code/namespaces/namespacegambit/) v, [str](/documentation/code/namespaces/namespacegambit/) sv)<br>Link a backend's version and safe version.  |
| void | **[override_path](/documentation/code/classes/structgambit_1_1backends_1_1backend__info/)**(const [str](/documentation/code/namespaces/namespacegambit/) & be, const [str](/documentation/code/namespaces/namespacegambit/) & ver, [str](/documentation/code/namespaces/namespacegambit/) path)<br>Override a backend's config file location.  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[default_version](/documentation/code/classes/structgambit_1_1backends_1_1backend__info/)**(const [str](/documentation/code/namespaces/namespacegambit/) & be) const<br>Get the default version of a BOSSed backend.  |
| std::vector< [str](/documentation/code/namespaces/namespacegambit/) > | **[working_versions](/documentation/code/classes/structgambit_1_1backends_1_1backend__info/)**(const [str](/documentation/code/namespaces/namespacegambit/) & be)<br>Get all versions of a given backend that are successfully loaded.  |
| std::vector< [str](/documentation/code/namespaces/namespacegambit/) > | **[working_safe_versions](/documentation/code/classes/structgambit_1_1backends_1_1backend__info/)**(const [str](/documentation/code/namespaces/namespacegambit/) & be)<br>Get all safe versions of a given backend that are successfully loaded.  |
| void | **[attempt_backend_path_override](/documentation/code/classes/structgambit_1_1backends_1_1backend__info/)**(const [str](/documentation/code/namespaces/namespacegambit/) & be, const [str](/documentation/code/namespaces/namespacegambit/) & ver, const char * name)<br>Try to resolve a pointer to a partial path to a shared library and use it to override the stored backend path.  |
| int | **[loadLibrary](/documentation/code/classes/structgambit_1_1backends_1_1backend__info/)**(const [str](/documentation/code/namespaces/namespacegambit/) & be, const [str](/documentation/code/namespaces/namespacegambit/) & ver, const [str](/documentation/code/namespaces/namespacegambit/) & sv, bool with_BOSS, const [str](/documentation/code/namespaces/namespacegambit/) & lang)<br>Attempt to load a backend library.  |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| std::map< [str](/documentation/code/namespaces/namespacegambit/), [str](/documentation/code/namespaces/namespacegambit/) > | **[dlerrors](/documentation/code/classes/structgambit_1_1backends_1_1backend__info/)** <br>Key: backend name + version.  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/), [str](/documentation/code/namespaces/namespacegambit/) > | **[default_safe_versions](/documentation/code/classes/structgambit_1_1backends_1_1backend__info/)** <br>Key: backend name (map from BOSSed backend names to their default safe versions)  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/), bool > | **[works](/documentation/code/classes/structgambit_1_1backends_1_1backend__info/)** <br>Key: backend name + version.  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/), bool > | **[needsMathematica](/documentation/code/classes/structgambit_1_1backends_1_1backend__info/)** <br>Key: backend name + version.  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/), bool > | **[needsPython](/documentation/code/classes/structgambit_1_1backends_1_1backend__info/)** <br>Key: backend name + version.  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/), int > | **[missingPythonVersion](/documentation/code/classes/structgambit_1_1backends_1_1backend__info/)** <br>Key: backend name + version.  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/), bool > | **[classloader](/documentation/code/classes/structgambit_1_1backends_1_1backend__info/)** <br>Key: backend name + version.  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/), bool > | **[classes_OK](/documentation/code/classes/structgambit_1_1backends_1_1backend__info/)** <br>Key: backend name + version.  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/), std::set< [str](/documentation/code/namespaces/namespacegambit/) > > | **[classes](/documentation/code/classes/structgambit_1_1backends_1_1backend__info/)** <br>Key: backend name + version.  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/), std::set< [str](/documentation/code/namespaces/namespacegambit/) > > | **[factory_args](/documentation/code/classes/structgambit_1_1backends_1_1backend__info/)** <br>Key: backend name + version + class name.  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/), [str](/documentation/code/namespaces/namespacegambit/) > | **[constructor_status](/documentation/code/classes/structgambit_1_1backends_1_1backend__info/)** <br>Key: backend name + version + class name + factory args.  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/), void * > | **[loaded_C_CXX_Fortran_backends](/documentation/code/classes/structgambit_1_1backends_1_1backend__info/)** <br>C/C++/Fortran backends that have been successfully loaded (Key: name+version)  |

## Public Functions Documentation

### function backend_info

```
backend_info()
```

Constructor. 

### function ~backend_info

```
~backend_info()
```

Destructor. 

### function custom_locations_exist

```
bool custom_locations_exist() const
```

Indicate whether a custom backend locations file exists. 

### function backend_locations

```
str backend_locations() const
```

Return the path to any custom user backend locations file. 

### function default_backend_locations

```
str default_backend_locations() const
```

Return the path to the default backend locations file. 

### function path

```
str path(
    str be,
    str ver
) const
```

Return the path to a backend library. 

Return the path to a backend library, given a backend name and version. 


### function corrected_path

```
str corrected_path(
    str be,
    str ver
) const
```

Return the path to a backend library with GAMBIT_DIR expanded. 

Return the complete path to a backend library, given a backend name and version. 


### function path_dir

```
str path_dir(
    str be,
    str ver
) const
```

Return the path to the folder in which a backend library resides. 

### function lib_name

```
str lib_name(
    str be,
    str ver
) const
```

Return the bare name of the library of a backend library, with no path or extension. 

### function version_from_safe_version

```
str version_from_safe_version(
    str be,
    str sv
) const
```

Given a backend and a safe version (with no periods), return the true version. 

### function safe_version_from_version

```
str safe_version_from_version(
    str be,
    str v
) const
```

Given a backend and a true version (with periods), return the safe version. 

### function link_versions

```
void link_versions(
    str be,
    str v,
    str sv
)
```

Link a backend's version and safe version. 

### function override_path

```
void override_path(
    const str & be,
    const str & ver,
    str path
)
```

Override a backend's config file location. 

### function default_version

```
str default_version(
    const str & be
) const
```

Get the default version of a BOSSed backend. 

### function working_versions

```
std::vector< str > working_versions(
    const str & be
)
```

Get all versions of a given backend that are successfully loaded. 

### function working_safe_versions

```
std::vector< str > working_safe_versions(
    const str & be
)
```

Get all safe versions of a given backend that are successfully loaded. 

### function attempt_backend_path_override

```
void attempt_backend_path_override(
    const str & be,
    const str & ver,
    const char * name
)
```

Try to resolve a pointer to a partial path to a shared library and use it to override the stored backend path. 

### function loadLibrary

```
int loadLibrary(
    const str & be,
    const str & ver,
    const str & sv,
    bool with_BOSS,
    const str & lang
)
```

Attempt to load a backend library. 

## Public Attributes Documentation

### variable dlerrors

```
std::map< str, str > dlerrors;
```

Key: backend name + version. 

### variable default_safe_versions

```
std::map< str, str > default_safe_versions;
```

Key: backend name (map from BOSSed backend names to their default safe versions) 

### variable works

```
std::map< str, bool > works;
```

Key: backend name + version. 

### variable needsMathematica

```
std::map< str, bool > needsMathematica;
```

Key: backend name + version. 

### variable needsPython

```
std::map< str, bool > needsPython;
```

Key: backend name + version. 

### variable missingPythonVersion

```
std::map< str, int > missingPythonVersion;
```

Key: backend name + version. 

### variable classloader

```
std::map< str, bool > classloader;
```

Key: backend name + version. 

### variable classes_OK

```
std::map< str, bool > classes_OK;
```

Key: backend name + version. 

### variable classes

```
std::map< str, std::set< str > > classes;
```

Key: backend name + version. 

### variable factory_args

```
std::map< str, std::set< str > > factory_args;
```

Key: backend name + version + class name. 

### variable constructor_status

```
std::map< str, str > constructor_status;
```

Key: backend name + version + class name + factory args. 

### variable loaded_C_CXX_Fortran_backends

```
std::map< str, void * > loaded_C_CXX_Fortran_backends;
```

C/C++/Fortran backends that have been successfully loaded (Key: name+version) 

-------------------------------

Updated on 2022-09-08 at 01:05:16 +0000