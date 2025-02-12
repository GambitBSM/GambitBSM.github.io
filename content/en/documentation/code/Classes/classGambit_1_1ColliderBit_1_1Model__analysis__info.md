---
title: "class Gambit::ColliderBit::Model_analysis_info"

description: "[No description available]"

---

# class Gambit::ColliderBit::Model_analysis_info



[No description available] [More...](#detailed-description)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[add_bkgcov](/documentation/code/classes/classgambit_1_1colliderbit_1_1model__analysis__info/#function-add-bkgcov)**(const std::vector< std::vector< double > > & bkgcov_in) |
| void | **[add_interp1d](/documentation/code/classes/classgambit_1_1colliderbit_1_1model__analysis__info/#function-add-interp1d)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) name, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) filename, std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > colnames) |
| void | **[add_interp2d](/documentation/code/classes/classgambit_1_1colliderbit_1_1model__analysis__info/#function-add-interp2d)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) name, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) filename, std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > colnames) |
| void | **[add_interp4d](/documentation/code/classes/classgambit_1_1colliderbit_1_1model__analysis__info/#function-add-interp4d)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) name, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) filename, std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > colnames, bool allow_missing_points) |
| void | **[add_interp5d](/documentation/code/classes/classgambit_1_1colliderbit_1_1model__analysis__info/#function-add-interp5d)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) name, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) filename, std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > colnames, bool allow_missing_points) |
| void | **[add_interpNd](/documentation/code/classes/classgambit_1_1colliderbit_1_1model__analysis__info/#function-add-interpnd)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) name, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) filename, std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > colnames, int N, bool allow_missing_points) |
| bool | **[has_interp1d](/documentation/code/classes/classgambit_1_1colliderbit_1_1model__analysis__info/#function-has-interp1d)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) name) const |
| const [Utils::interp1d_gsl_collection](/documentation/code/classes/classgambit_1_1utils_1_1interp1d__gsl__collection/) & | **[get_interp1d](/documentation/code/classes/classgambit_1_1colliderbit_1_1model__analysis__info/#function-get-interp1d)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) name) const |
| bool | **[has_interp2d](/documentation/code/classes/classgambit_1_1colliderbit_1_1model__analysis__info/#function-has-interp2d)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) name) const |
| const [Utils::interp2d_gsl_collection](/documentation/code/classes/classgambit_1_1utils_1_1interp2d__gsl__collection/) & | **[get_interp2d](/documentation/code/classes/classgambit_1_1colliderbit_1_1model__analysis__info/#function-get-interp2d)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) name) const |
| bool | **[has_interp4d](/documentation/code/classes/classgambit_1_1colliderbit_1_1model__analysis__info/#function-has-interp4d)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) name) const |
| [Utils::interp4d_collection](/documentation/code/classes/classgambit_1_1utils_1_1interp4d__collection/) & | **[get_interp4d](/documentation/code/classes/classgambit_1_1colliderbit_1_1model__analysis__info/#function-get-interp4d)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) name) const |
| bool | **[has_interp5d](/documentation/code/classes/classgambit_1_1colliderbit_1_1model__analysis__info/#function-has-interp5d)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) name) const |
| [Utils::interp5d_collection](/documentation/code/classes/classgambit_1_1utils_1_1interp5d__collection/) & | **[get_interp5d](/documentation/code/classes/classgambit_1_1colliderbit_1_1model__analysis__info/#function-get-interp5d)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) name) const |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[name](/documentation/code/classes/classgambit_1_1colliderbit_1_1model__analysis__info/#variable-name)**  |
| double | **[lumi_invfb](/documentation/code/classes/classgambit_1_1colliderbit_1_1model__analysis__info/#variable-lumi-invfb)**  |
| size_t | **[n_signal_regions](/documentation/code/classes/classgambit_1_1colliderbit_1_1model__analysis__info/#variable-n-signal-regions)**  |
| std::vector< int > | **[obsnum](/documentation/code/classes/classgambit_1_1colliderbit_1_1model__analysis__info/#variable-obsnum)**  |
| std::vector< double > | **[bkgnum](/documentation/code/classes/classgambit_1_1colliderbit_1_1model__analysis__info/#variable-bkgnum)**  |
| std::vector< double > | **[bkgerr](/documentation/code/classes/classgambit_1_1colliderbit_1_1model__analysis__info/#variable-bkgerr)**  |
| Eigen::MatrixXd | **[bkgcov](/documentation/code/classes/classgambit_1_1colliderbit_1_1model__analysis__info/#variable-bkgcov)**  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), std::vector< double > > | **[extra_info](/documentation/code/classes/classgambit_1_1colliderbit_1_1model__analysis__info/#variable-extra-info)**  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), std::unique_ptr< [Utils::interp1d_gsl_collection](/documentation/code/classes/classgambit_1_1utils_1_1interp1d__gsl__collection/) > > | **[interp1d](/documentation/code/classes/classgambit_1_1colliderbit_1_1model__analysis__info/#variable-interp1d)**  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), std::unique_ptr< [Utils::interp2d_gsl_collection](/documentation/code/classes/classgambit_1_1utils_1_1interp2d__gsl__collection/) > > | **[interp2d](/documentation/code/classes/classgambit_1_1colliderbit_1_1model__analysis__info/#variable-interp2d)**  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), std::unique_ptr< [Utils::interp4d_collection](/documentation/code/classes/classgambit_1_1utils_1_1interp4d__collection/) > > | **[interp4d](/documentation/code/classes/classgambit_1_1colliderbit_1_1model__analysis__info/#variable-interp4d)**  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), std::unique_ptr< [Utils::interp5d_collection](/documentation/code/classes/classgambit_1_1utils_1_1interp5d__collection/) > > | **[interp5d](/documentation/code/classes/classgambit_1_1colliderbit_1_1model__analysis__info/#variable-interp5d)**  |

## Detailed Description

```
class Gambit::ColliderBit::Model_analysis_info;
```


A minimal class with analysis info, maps for containing collections of 1D/2D/4D/5D interpolators and some helper functions for adding and accessing the interpolators, and for adding a background covariance matrix. Currently this class is tailored specifically for the DMEFT/DMsimp models &ndash; it will be generalized in the future. 

## Public Functions Documentation

### function add_bkgcov

```
inline void add_bkgcov(
    const std::vector< std::vector< double > > & bkgcov_in
)
```


### function add_interp1d

```
inline void add_interp1d(
    str name,
    str filename,
    std::vector< str > colnames
)
```


### function add_interp2d

```
inline void add_interp2d(
    str name,
    str filename,
    std::vector< str > colnames
)
```


### function add_interp4d

```
inline void add_interp4d(
    str name,
    str filename,
    std::vector< str > colnames,
    bool allow_missing_points
)
```


### function add_interp5d

```
inline void add_interp5d(
    str name,
    str filename,
    std::vector< str > colnames,
    bool allow_missing_points
)
```


### function add_interpNd

```
inline void add_interpNd(
    str name,
    str filename,
    std::vector< str > colnames,
    int N,
    bool allow_missing_points
)
```


### function has_interp1d

```
inline bool has_interp1d(
    str name
) const
```


### function get_interp1d

```
inline const Utils::interp1d_gsl_collection & get_interp1d(
    str name
) const
```


### function has_interp2d

```
inline bool has_interp2d(
    str name
) const
```


### function get_interp2d

```
inline const Utils::interp2d_gsl_collection & get_interp2d(
    str name
) const
```


### function has_interp4d

```
inline bool has_interp4d(
    str name
) const
```


### function get_interp4d

```
inline Utils::interp4d_collection & get_interp4d(
    str name
) const
```


### function has_interp5d

```
inline bool has_interp5d(
    str name
) const
```


### function get_interp5d

```
inline Utils::interp5d_collection & get_interp5d(
    str name
) const
```


## Public Attributes Documentation

### variable name

```
str name;
```


### variable lumi_invfb

```
double lumi_invfb;
```


### variable n_signal_regions

```
size_t n_signal_regions;
```


### variable obsnum

```
std::vector< int > obsnum;
```


### variable bkgnum

```
std::vector< double > bkgnum;
```


### variable bkgerr

```
std::vector< double > bkgerr;
```


### variable bkgcov

```
Eigen::MatrixXd bkgcov;
```


### variable extra_info

```
std::map< str, std::vector< double > > extra_info;
```


### variable interp1d

```
std::map< str, std::unique_ptr< Utils::interp1d_gsl_collection > > interp1d;
```


### variable interp2d

```
std::map< str, std::unique_ptr< Utils::interp2d_gsl_collection > > interp2d;
```


### variable interp4d

```
std::map< str, std::unique_ptr< Utils::interp4d_collection > > interp4d;
```


### variable interp5d

```
std::map< str, std::unique_ptr< Utils::interp5d_collection > > interp5d;
```


-------------------------------

Updated on 2025-02-12 at 15:36:39 +0000