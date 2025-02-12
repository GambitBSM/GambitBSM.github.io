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
| | **[interp1d_collection](/documentation/code/classes/classgambit_1_1utils_1_1interp1d__collection/#function-interp1d-collection)**(const std::string collection_name_in, const std::string file_name_in, const std::vector< std::string > colnames_in) |
| | **[~interp1d_collection](/documentation/code/classes/classgambit_1_1utils_1_1interp1d__collection/#function-interp1d-collection)**() |
| double | **[eval](/documentation/code/classes/classgambit_1_1utils_1_1interp1d__collection/#function-eval)**(double x1, size_t interp_index) |
| bool | **[is_inside_range](/documentation/code/classes/classgambit_1_1utils_1_1interp1d__collection/#function-is-inside-range)**(double x1) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| std::string | **[collection_name](/documentation/code/classes/classgambit_1_1utils_1_1interp1d__collection/#variable-collection-name)**  |
| std::string | **[file_name](/documentation/code/classes/classgambit_1_1utils_1_1interp1d__collection/#variable-file-name)**  |
| std::string | **[x1_name](/documentation/code/classes/classgambit_1_1utils_1_1interp1d__collection/#variable-x1-name)**  |
| std::vector< std::string > | **[interpolator_names](/documentation/code/classes/classgambit_1_1utils_1_1interp1d__collection/#variable-interpolator-names)**  |
| std::vector< double > | **[x1_vec](/documentation/code/classes/classgambit_1_1utils_1_1interp1d__collection/#variable-x1-vec)**  |
| std::vector< double > | **[x1_vec_unsorted](/documentation/code/classes/classgambit_1_1utils_1_1interp1d__collection/#variable-x1-vec-unsorted)**  |
| std::vector< std::vector< double > > | **[interp_data](/documentation/code/classes/classgambit_1_1utils_1_1interp1d__collection/#variable-interp-data)**  |
| double | **[x1_min](/documentation/code/classes/classgambit_1_1utils_1_1interp1d__collection/#variable-x1-min)**  |
| double | **[x1_max](/documentation/code/classes/classgambit_1_1utils_1_1interp1d__collection/#variable-x1-max)**  |
| size_t | **[n_interpolators](/documentation/code/classes/classgambit_1_1utils_1_1interp1d__collection/#variable-n-interpolators)**  |

## Detailed Description

```
class Gambit::Utils::interp1d_collection;
```


A class for holding a collection of 1D interpolators, created from reading a tabulated ascii file.

* The first column is taken as the x value.
* For each remaining column a 1D interpolation function f(x) is created
* This is a simple linear interpolator that does not use GSL 

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
    double x1,
    size_t interp_index
)
```


### function is_inside_range

```
bool is_inside_range(
    double x1
)
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


### variable x1_name

```
std::string x1_name;
```


### variable interpolator_names

```
std::vector< std::string > interpolator_names;
```


### variable x1_vec

```
std::vector< double > x1_vec;
```


### variable x1_vec_unsorted

```
std::vector< double > x1_vec_unsorted;
```


### variable interp_data

```
std::vector< std::vector< double > > interp_data;
```


### variable x1_min

```
double x1_min;
```


### variable x1_max

```
double x1_max;
```


### variable n_interpolators

```
size_t n_interpolators;
```


-------------------------------

Updated on 2025-02-12 at 15:36:40 +0000