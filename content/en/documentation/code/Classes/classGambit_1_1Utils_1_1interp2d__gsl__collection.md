---
title: "class Gambit::Utils::interp2d_gsl_collection"

description: "[No description available]"

---

# class Gambit::Utils::interp2d_gsl_collection



[No description available] [More...](#detailed-description)


`#include <interp_collection.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[interp2d_gsl_collection](/documentation/code/classes/classgambit_1_1utils_1_1interp2d__gsl__collection/#function-interp2d-gsl-collection)**(const std::string collection_name_in, const std::string file_name_in, const std::vector< std::string > colnames_in) |
| | **[~interp2d_gsl_collection](/documentation/code/classes/classgambit_1_1utils_1_1interp2d__gsl__collection/#function-interp2d-gsl-collection)**() |
| double | **[eval](/documentation/code/classes/classgambit_1_1utils_1_1interp2d__gsl__collection/#function-eval)**(double x, double y, size_t interp_index) const |
| double | **[eval](/documentation/code/classes/classgambit_1_1utils_1_1interp2d__gsl__collection/#function-eval)**(double x, double y) const |
| bool | **[is_inside_range](/documentation/code/classes/classgambit_1_1utils_1_1interp2d__gsl__collection/#function-is-inside-range)**(double x, double y) const |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| std::string | **[collection_name](/documentation/code/classes/classgambit_1_1utils_1_1interp2d__gsl__collection/#variable-collection-name)**  |
| std::string | **[file_name](/documentation/code/classes/classgambit_1_1utils_1_1interp2d__gsl__collection/#variable-file-name)**  |
| std::string | **[x_name](/documentation/code/classes/classgambit_1_1utils_1_1interp2d__gsl__collection/#variable-x-name)**  |
| std::string | **[y_name](/documentation/code/classes/classgambit_1_1utils_1_1interp2d__gsl__collection/#variable-y-name)**  |
| std::vector< std::string > | **[interpolator_names](/documentation/code/classes/classgambit_1_1utils_1_1interp2d__gsl__collection/#variable-interpolator-names)**  |
| std::vector< gsl_spline2d * > | **[splines](/documentation/code/classes/classgambit_1_1utils_1_1interp2d__gsl__collection/#variable-splines)**  |
| std::vector< gsl_interp_accel * > | **[x_accels](/documentation/code/classes/classgambit_1_1utils_1_1interp2d__gsl__collection/#variable-x-accels)**  |
| std::vector< gsl_interp_accel * > | **[y_accels](/documentation/code/classes/classgambit_1_1utils_1_1interp2d__gsl__collection/#variable-y-accels)**  |
| double | **[x_min](/documentation/code/classes/classgambit_1_1utils_1_1interp2d__gsl__collection/#variable-x-min)**  |
| double | **[x_max](/documentation/code/classes/classgambit_1_1utils_1_1interp2d__gsl__collection/#variable-x-max)**  |
| double | **[y_min](/documentation/code/classes/classgambit_1_1utils_1_1interp2d__gsl__collection/#variable-y-min)**  |
| double | **[y_max](/documentation/code/classes/classgambit_1_1utils_1_1interp2d__gsl__collection/#variable-y-max)**  |
| size_t | **[n_interpolators](/documentation/code/classes/classgambit_1_1utils_1_1interp2d__gsl__collection/#variable-n-interpolators)**  |

## Detailed Description

```
class Gambit::Utils::interp2d_gsl_collection;
```


A class for holding a collection of 2D interpolators, created from reading a tabulated ascii file.

* The first two columns are taken to be the x and y grid points.
* For each remaining column a 2D interpolation function f(x,y) is created
* Note that GLS assumes the points are ordered according to increasing x (first) and y (second) values, i.e. an ordering like (x0,y0), (x1,y0), (x2,y0), ... (x0,y1), (x1,y1), (x2,y1), ... 

## Public Functions Documentation

### function interp2d_gsl_collection

```
interp2d_gsl_collection(
    const std::string collection_name_in,
    const std::string file_name_in,
    const std::vector< std::string > colnames_in
)
```


### function ~interp2d_gsl_collection

```
~interp2d_gsl_collection()
```


### function eval

```
double eval(
    double x,
    double y,
    size_t interp_index
) const
```


### function eval

```
double eval(
    double x,
    double y
) const
```


### function is_inside_range

```
bool is_inside_range(
    double x,
    double y
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


### variable y_name

```
std::string y_name;
```


### variable interpolator_names

```
std::vector< std::string > interpolator_names;
```


### variable splines

```
std::vector< gsl_spline2d * > splines;
```


### variable x_accels

```
std::vector< gsl_interp_accel * > x_accels;
```


### variable y_accels

```
std::vector< gsl_interp_accel * > y_accels;
```


### variable x_min

```
double x_min;
```


### variable x_max

```
double x_max;
```


### variable y_min

```
double y_min;
```


### variable y_max

```
double y_max;
```


### variable n_interpolators

```
size_t n_interpolators;
```


-------------------------------

Updated on 2025-02-12 at 15:36:40 +0000