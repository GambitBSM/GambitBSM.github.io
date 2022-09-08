---
title: "class Gambit::Utils::interp1d_collection"

description: "[No description available]"

---

# class Gambit::Utils::interp1d_collection



[No description available] [More...](#detailed-description)


`#include <interp_collection.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[interp1d_collection](/documentation/code/classes/classgambit_1_1utils_1_1interp1d__collection/)**(const std::string collection_name_in, const std::string file_name_in, const std::vector< std::string > colnames_in) |
| | **[~interp1d_collection](/documentation/code/classes/classgambit_1_1utils_1_1interp1d__collection/)**() |
| double | **[eval](/documentation/code/classes/classgambit_1_1utils_1_1interp1d__collection/)**(double x, size_t interp_index) const |
| double | **[eval](/documentation/code/classes/classgambit_1_1utils_1_1interp1d__collection/)**(double x) const |
| bool | **[is_inside_range](/documentation/code/classes/classgambit_1_1utils_1_1interp1d__collection/)**(double x) const |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| std::string | **[collection_name](/documentation/code/classes/classgambit_1_1utils_1_1interp1d__collection/)**  |
| std::string | **[file_name](/documentation/code/classes/classgambit_1_1utils_1_1interp1d__collection/)**  |
| std::string | **[x_name](/documentation/code/classes/classgambit_1_1utils_1_1interp1d__collection/)**  |
| std::vector< std::string > | **[interpolator_names](/documentation/code/classes/classgambit_1_1utils_1_1interp1d__collection/)**  |
| std::vector< gsl_spline * > | **[splines](/documentation/code/classes/classgambit_1_1utils_1_1interp1d__collection/)**  |
| std::vector< gsl_interp_accel * > | **[x_accels](/documentation/code/classes/classgambit_1_1utils_1_1interp1d__collection/)**  |
| double | **[x_min](/documentation/code/classes/classgambit_1_1utils_1_1interp1d__collection/)**  |
| double | **[x_max](/documentation/code/classes/classgambit_1_1utils_1_1interp1d__collection/)**  |
| size_t | **[n_interpolators](/documentation/code/classes/classgambit_1_1utils_1_1interp1d__collection/)**  |

## Detailed Description

```
class Gambit::Utils::interp1d_collection;
```


A class for holding a collection of 1D interpolators, created from reading a tabulated ascii file.

* The first column is taken as the x value.
* For each remaining column a 1D interpolation function f(x) is created 

## Public Functions Documentation

### function interp1d_collection

```
interp1d_collection(
    const std::string collection_name_in,
    const std::string file_name_in,
    const std::vector< std::string > colnames_in
)
```


### function ~interp1d_collection

```
~interp1d_collection()
```


### function eval

```
double eval(
    double x,
    size_t interp_index
) const
```


### function eval

```
double eval(
    double x
) const
```


### function is_inside_range

```
bool is_inside_range(
    double x
) const
```


## Public Attributes Documentation

### variable collection_name

```
std::string collection_name;
```


### variable file_name

```
std::string file_name;
```


### variable x_name

```
std::string x_name;
```


### variable interpolator_names

```
std::vector< std::string > interpolator_names;
```


### variable splines

```
std::vector< gsl_spline * > splines;
```


### variable x_accels

```
std::vector< gsl_interp_accel * > x_accels;
```


### variable x_min

```
double x_min;
```


### variable x_max

```
double x_max;
```


### variable n_interpolators

```
size_t n_interpolators;
```


-------------------------------

Updated on 2022-09-08 at 01:05:18 +0000