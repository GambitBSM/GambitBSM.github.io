---
title: "class Gambit::Utils::interp4d_collection"

description: "[No description available]"

---

# class Gambit::Utils::interp4d_collection



[No description available] [More...](#detailed-description)


`#include <interp_collection.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[interp4d_collection](/documentation/code/classes/classgambit_1_1utils_1_1interp4d__collection/#function-interp4d-collection)**(const std::string collection_name_in, const std::string file_name_in, const std::vector< std::string > colnames_in, bool allow_missing_points, double missing_pts_val) |
| | **[~interp4d_collection](/documentation/code/classes/classgambit_1_1utils_1_1interp4d__collection/#function-interp4d-collection)**() |
| double | **[linearinterp1D](/documentation/code/classes/classgambit_1_1utils_1_1interp4d__collection/#function-linearinterp1d)**(double x1, double x2, double y1, double y2, double xtest) |
| double | **[eval](/documentation/code/classes/classgambit_1_1utils_1_1interp4d__collection/#function-eval)**(double x1, double x2, double x3, double x4, size_t interp_index) |
| bool | **[is_inside_range](/documentation/code/classes/classgambit_1_1utils_1_1interp4d__collection/#function-is-inside-range)**(double x1, double x2, double x3, double x4) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| std::string | **[collection_name](/documentation/code/classes/classgambit_1_1utils_1_1interp4d__collection/#variable-collection-name)**  |
| std::string | **[file_name](/documentation/code/classes/classgambit_1_1utils_1_1interp4d__collection/#variable-file-name)**  |
| std::string | **[x1_name](/documentation/code/classes/classgambit_1_1utils_1_1interp4d__collection/#variable-x1-name)**  |
| std::string | **[x2_name](/documentation/code/classes/classgambit_1_1utils_1_1interp4d__collection/#variable-x2-name)**  |
| std::string | **[x3_name](/documentation/code/classes/classgambit_1_1utils_1_1interp4d__collection/#variable-x3-name)**  |
| std::string | **[x4_name](/documentation/code/classes/classgambit_1_1utils_1_1interp4d__collection/#variable-x4-name)**  |
| std::vector< std::string > | **[interpolator_names](/documentation/code/classes/classgambit_1_1utils_1_1interp4d__collection/#variable-interpolator-names)**  |
| std::vector< double > | **[x1_vec](/documentation/code/classes/classgambit_1_1utils_1_1interp4d__collection/#variable-x1-vec)**  |
| std::vector< double > | **[x2_vec](/documentation/code/classes/classgambit_1_1utils_1_1interp4d__collection/#variable-x2-vec)**  |
| std::vector< double > | **[x3_vec](/documentation/code/classes/classgambit_1_1utils_1_1interp4d__collection/#variable-x3-vec)**  |
| std::vector< double > | **[x4_vec](/documentation/code/classes/classgambit_1_1utils_1_1interp4d__collection/#variable-x4-vec)**  |
| std::vector< double > | **[x1_vec_unsorted](/documentation/code/classes/classgambit_1_1utils_1_1interp4d__collection/#variable-x1-vec-unsorted)**  |
| std::vector< double > | **[x2_vec_unsorted](/documentation/code/classes/classgambit_1_1utils_1_1interp4d__collection/#variable-x2-vec-unsorted)**  |
| std::vector< double > | **[x3_vec_unsorted](/documentation/code/classes/classgambit_1_1utils_1_1interp4d__collection/#variable-x3-vec-unsorted)**  |
| std::vector< double > | **[x4_vec_unsorted](/documentation/code/classes/classgambit_1_1utils_1_1interp4d__collection/#variable-x4-vec-unsorted)**  |
| std::vector< std::vector< double > > | **[interp_data](/documentation/code/classes/classgambit_1_1utils_1_1interp4d__collection/#variable-interp-data)**  |
| double | **[x1_min](/documentation/code/classes/classgambit_1_1utils_1_1interp4d__collection/#variable-x1-min)**  |
| double | **[x1_max](/documentation/code/classes/classgambit_1_1utils_1_1interp4d__collection/#variable-x1-max)**  |
| double | **[x2_min](/documentation/code/classes/classgambit_1_1utils_1_1interp4d__collection/#variable-x2-min)**  |
| double | **[x2_max](/documentation/code/classes/classgambit_1_1utils_1_1interp4d__collection/#variable-x2-max)**  |
| double | **[x3_min](/documentation/code/classes/classgambit_1_1utils_1_1interp4d__collection/#variable-x3-min)**  |
| double | **[x3_max](/documentation/code/classes/classgambit_1_1utils_1_1interp4d__collection/#variable-x3-max)**  |
| double | **[x4_min](/documentation/code/classes/classgambit_1_1utils_1_1interp4d__collection/#variable-x4-min)**  |
| double | **[x4_max](/documentation/code/classes/classgambit_1_1utils_1_1interp4d__collection/#variable-x4-max)**  |
| size_t | **[n_interpolators](/documentation/code/classes/classgambit_1_1utils_1_1interp4d__collection/#variable-n-interpolators)**  |
| bool | **[allow_missing_pts](/documentation/code/classes/classgambit_1_1utils_1_1interp4d__collection/#variable-allow-missing-pts)**  |
| double | **[missing_point_val](/documentation/code/classes/classgambit_1_1utils_1_1interp4d__collection/#variable-missing-point-val)**  |

## Detailed Description

```
class Gambit::Utils::interp4d_collection;
```


A class for holding a collection of 4D interpolators, created from reading a tabulated ascii file.

* The first 4 columns are taken to be the x1,x2,x3,x4 grid points.
* A series of 1D interpolations is performed repeatedly to form the result. 

## Public Functions Documentation

### function interp4d_collection

```
interp4d_collection(
    const std::string collection_name_in,
    const std::string file_name_in,
    const std::vector< std::string > colnames_in,
    bool allow_missing_points,
    double missing_pts_val
)
```


### function ~interp4d_collection

```
~interp4d_collection()
```


### function linearinterp1D

```
double linearinterp1D(
    double x1,
    double x2,
    double y1,
    double y2,
    double xtest
)
```


### function eval

```
double eval(
    double x1,
    double x2,
    double x3,
    double x4,
    size_t interp_index
)
```


### function is_inside_range

```
bool is_inside_range(
    double x1,
    double x2,
    double x3,
    double x4
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


### variable x2_name

```
std::string x2_name;
```


### variable x3_name

```
std::string x3_name;
```


### variable x4_name

```
std::string x4_name;
```


### variable interpolator_names

```
std::vector< std::string > interpolator_names;
```


### variable x1_vec

```
std::vector< double > x1_vec;
```


### variable x2_vec

```
std::vector< double > x2_vec;
```


### variable x3_vec

```
std::vector< double > x3_vec;
```


### variable x4_vec

```
std::vector< double > x4_vec;
```


### variable x1_vec_unsorted

```
std::vector< double > x1_vec_unsorted;
```


### variable x2_vec_unsorted

```
std::vector< double > x2_vec_unsorted;
```


### variable x3_vec_unsorted

```
std::vector< double > x3_vec_unsorted;
```


### variable x4_vec_unsorted

```
std::vector< double > x4_vec_unsorted;
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


### variable x2_min

```
double x2_min;
```


### variable x2_max

```
double x2_max;
```


### variable x3_min

```
double x3_min;
```


### variable x3_max

```
double x3_max;
```


### variable x4_min

```
double x4_min;
```


### variable x4_max

```
double x4_max;
```


### variable n_interpolators

```
size_t n_interpolators;
```


### variable allow_missing_pts

```
bool allow_missing_pts;
```


### variable missing_point_val

```
double missing_point_val;
```


-------------------------------

Updated on 2024-07-18 at 13:53:32 +0000