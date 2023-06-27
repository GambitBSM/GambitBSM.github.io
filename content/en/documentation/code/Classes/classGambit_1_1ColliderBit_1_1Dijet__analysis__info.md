---
title: "class Gambit::ColliderBit::Dijet_analysis_info"
description: "A class to hold analysis information for DiJets (specific to DMsimp models) "

---

# class Gambit::ColliderBit::Dijet_analysis_info



A class to hold analysis information for DiJets (specific to DMsimp models) 

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[add_interp1d](/documentation/code/classes/classgambit_1_1colliderbit_1_1dijet__analysis__info/#function-add-interp1d)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) name, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) filename, std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > colnames) |
| void | **[add_interp2d_simple](/documentation/code/classes/classgambit_1_1colliderbit_1_1dijet__analysis__info/#function-add-interp2d-simple)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) name, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) filename, std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > colnames) |
| const [Utils::interp1d_gsl_collection](/documentation/code/classes/classgambit_1_1utils_1_1interp1d__gsl__collection/) & | **[get_interp1d](/documentation/code/classes/classgambit_1_1colliderbit_1_1dijet__analysis__info/#function-get-interp1d)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) name) const |
| [Utils::interp2d_collection](/documentation/code/classes/classgambit_1_1utils_1_1interp2d__collection/) & | **[get_interp2d_simple](/documentation/code/classes/classgambit_1_1colliderbit_1_1dijet__analysis__info/#function-get-interp2d-simple)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) name) const |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[name](/documentation/code/classes/classgambit_1_1colliderbit_1_1dijet__analysis__info/#variable-name)**  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), std::unique_ptr< [Utils::interp1d_gsl_collection](/documentation/code/classes/classgambit_1_1utils_1_1interp1d__gsl__collection/) > > | **[interp1d](/documentation/code/classes/classgambit_1_1colliderbit_1_1dijet__analysis__info/#variable-interp1d)**  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), std::unique_ptr< [Utils::interp2d_collection](/documentation/code/classes/classgambit_1_1utils_1_1interp2d__collection/) > > | **[interp2d_simple](/documentation/code/classes/classgambit_1_1colliderbit_1_1dijet__analysis__info/#variable-interp2d-simple)**  |

## Public Functions Documentation

### function add_interp1d

```
inline void add_interp1d(
    str name,
    str filename,
    std::vector< str > colnames
)
```


### function add_interp2d_simple

```
inline void add_interp2d_simple(
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


### function get_interp2d_simple

```
inline Utils::interp2d_collection & get_interp2d_simple(
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


### variable interp2d_simple

```
std::map< str, std::unique_ptr< Utils::interp2d_collection > > interp2d_simple;
```


-------------------------------

Updated on 2023-06-26 at 21:36:52 +0000