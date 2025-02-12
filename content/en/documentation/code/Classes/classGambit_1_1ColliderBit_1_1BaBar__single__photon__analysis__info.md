---
title: "class Gambit::ColliderBit::BaBar_single_photon_analysis_info"
description: "A class to hold analysis information for the BaBar single photon search (specific to dark photon models) "

---

# class Gambit::ColliderBit::BaBar_single_photon_analysis_info



A class to hold analysis information for the BaBar single photon search (specific to dark photon models) 

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[add_interp1d](/documentation/code/classes/classgambit_1_1colliderbit_1_1babar__single__photon__analysis__info/#function-add-interp1d)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) name, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) filename, std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > colnames) |
| const [Utils::interp1d_gsl_collection](/documentation/code/classes/classgambit_1_1utils_1_1interp1d__gsl__collection/) & | **[get_interp1d](/documentation/code/classes/classgambit_1_1colliderbit_1_1babar__single__photon__analysis__info/#function-get-interp1d)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) name) const |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[name](/documentation/code/classes/classgambit_1_1colliderbit_1_1babar__single__photon__analysis__info/#variable-name)**  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), std::unique_ptr< [Utils::interp1d_gsl_collection](/documentation/code/classes/classgambit_1_1utils_1_1interp1d__gsl__collection/) > > | **[interp1d](/documentation/code/classes/classgambit_1_1colliderbit_1_1babar__single__photon__analysis__info/#variable-interp1d)**  |

## Public Functions Documentation

### function add_interp1d

```
inline void add_interp1d(
    str name,
    str filename,
    std::vector< str > colnames
)
```


### function get_interp1d

```
inline const Utils::interp1d_gsl_collection & get_interp1d(
    str name
) const
```


## Public Attributes Documentation

### variable name

```
str name;
```


### variable interp1d

```
std::map< str, std::unique_ptr< Utils::interp1d_gsl_collection > > interp1d;
```


-------------------------------

Updated on 2025-02-12 at 16:10:32 +0000