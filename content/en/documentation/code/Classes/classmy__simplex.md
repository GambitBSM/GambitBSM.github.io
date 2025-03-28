---
title: "class my_simplex"

description: "[No description available]"

---

# class my_simplex



[No description available]

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[my_simplex](/documentation/code/classes/classmy__simplex/#function-my-simplex)**(int dd, double aalpha, double bbeta, double ggamma, [my_func](/documentation/code/classes/structmy__func/) * ff) |
| void | **[find_min](/documentation/code/classes/classmy__simplex/#function-find-min)**() |
| void | **[find_max](/documentation/code/classes/classmy__simplex/#function-find-max)**() |
| void | **[my_SetUp](/documentation/code/classes/classmy__simplex/#function-my-setup)**(double xin[]) |
| void | **[set_y](/documentation/code/classes/classmy__simplex/#function-set-y)**() |
| void | **[my_Centroid](/documentation/code/classes/classmy__simplex/#function-my-centroid)**(int h) |
| void | **[my_Reflection](/documentation/code/classes/classmy__simplex/#function-my-reflection)**() |
| void | **[my_Expansion](/documentation/code/classes/classmy__simplex/#function-my-expansion)**() |
| void | **[my_Contraction](/documentation/code/classes/classmy__simplex/#function-my-contraction)**() |
| void | **[replace_all](/documentation/code/classes/classmy__simplex/#function-replace-all)**() |
| double | **[get_yavg](/documentation/code/classes/classmy__simplex/#function-get-yavg)**() |
| double | **[get_sigma](/documentation/code/classes/classmy__simplex/#function-get-sigma)**() |
| void | **[print_Centroid](/documentation/code/classes/classmy__simplex/#function-print-centroid)**() |
| void | **[print_Reflect](/documentation/code/classes/classmy__simplex/#function-print-reflect)**() |
| void | **[print_Expand](/documentation/code/classes/classmy__simplex/#function-print-expand)**() |
| void | **[print_Contract](/documentation/code/classes/classmy__simplex/#function-print-contract)**() |
| void | **[print_max](/documentation/code/classes/classmy__simplex/#function-print-max)**() |
| void | **[print_min](/documentation/code/classes/classmy__simplex/#function-print-min)**() |
| void | **[print_all](/documentation/code/classes/classmy__simplex/#function-print-all)**() |
| void | **[print_xy](/documentation/code/classes/classmy__simplex/#function-print-xy)**() |
| void | **[print_xyl](/documentation/code/classes/classmy__simplex/#function-print-xyl)**() |
| void | **[print_xyh](/documentation/code/classes/classmy__simplex/#function-print-xyh)**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [my_func](/documentation/code/classes/structmy__func/) * | **[f](/documentation/code/classes/classmy__simplex/#variable-f)**  |
| double[DMAX *(DMAX+1)] | **[xstart](/documentation/code/classes/classmy__simplex/#variable-xstart)**  |
| double[DMAX *(DMAX+1)] | **[x](/documentation/code/classes/classmy__simplex/#variable-x)**  |
| double[DMAX] | **[xh](/documentation/code/classes/classmy__simplex/#variable-xh)**  |
| double[DMAX] | **[xl](/documentation/code/classes/classmy__simplex/#variable-xl)**  |
| double[DMAX+1] | **[y](/documentation/code/classes/classmy__simplex/#variable-y)**  |
| double | **[yl](/documentation/code/classes/classmy__simplex/#variable-yl)**  |
| double | **[ynh](/documentation/code/classes/classmy__simplex/#variable-ynh)**  |
| double | **[yh](/documentation/code/classes/classmy__simplex/#variable-yh)**  |
| double[DMAX] | **[xCentroid](/documentation/code/classes/classmy__simplex/#variable-xcentroid)**  |
| double | **[yReflect](/documentation/code/classes/classmy__simplex/#variable-yreflect)**  |
| double | **[yExpand](/documentation/code/classes/classmy__simplex/#variable-yexpand)**  |
| double | **[yContract](/documentation/code/classes/classmy__simplex/#variable-ycontract)**  |
| double[DMAX] | **[xReflect](/documentation/code/classes/classmy__simplex/#variable-xreflect)**  |
| double[DMAX] | **[xExpand](/documentation/code/classes/classmy__simplex/#variable-xexpand)**  |
| double[DMAX] | **[xContract](/documentation/code/classes/classmy__simplex/#variable-xcontract)**  |
| int | **[imin](/documentation/code/classes/classmy__simplex/#variable-imin)**  |
| int | **[imax](/documentation/code/classes/classmy__simplex/#variable-imax)**  |
| int | **[inmax](/documentation/code/classes/classmy__simplex/#variable-inmax)**  |

## Public Functions Documentation

### function my_simplex

```
my_simplex(
    int dd,
    double aalpha,
    double bbeta,
    double ggamma,
    my_func * ff
)
```


### function find_min

```
void find_min()
```


### function find_max

```
void find_max()
```


### function my_SetUp

```
void my_SetUp(
    double xin[]
)
```


### function set_y

```
void set_y()
```


### function my_Centroid

```
void my_Centroid(
    int h
)
```


### function my_Reflection

```
void my_Reflection()
```


### function my_Expansion

```
void my_Expansion()
```


### function my_Contraction

```
void my_Contraction()
```


### function replace_all

```
void replace_all()
```


### function get_yavg

```
double get_yavg()
```


### function get_sigma

```
double get_sigma()
```


### function print_Centroid

```
void print_Centroid()
```


### function print_Reflect

```
void print_Reflect()
```


### function print_Expand

```
void print_Expand()
```


### function print_Contract

```
void print_Contract()
```


### function print_max

```
void print_max()
```


### function print_min

```
void print_min()
```


### function print_all

```
void print_all()
```


### function print_xy

```
void print_xy()
```


### function print_xyl

```
void print_xyl()
```


### function print_xyh

```
void print_xyh()
```


## Public Attributes Documentation

### variable f

```
my_func * f;
```


### variable xstart

```
double[DMAX *(DMAX+1)] xstart;
```


### variable x

```
double[DMAX *(DMAX+1)] x;
```


### variable xh

```
double[DMAX] xh;
```


### variable xl

```
double[DMAX] xl;
```


### variable y

```
double[DMAX+1] y;
```


### variable yl

```
double yl;
```


### variable ynh

```
double ynh;
```


### variable yh

```
double yh;
```


### variable xCentroid

```
double[DMAX] xCentroid;
```


### variable yReflect

```
double yReflect;
```


### variable yExpand

```
double yExpand;
```


### variable yContract

```
double yContract;
```


### variable xReflect

```
double[DMAX] xReflect;
```


### variable xExpand

```
double[DMAX] xExpand;
```


### variable xContract

```
double[DMAX] xContract;
```


### variable imin

```
int imin;
```


### variable imax

```
int imax;
```


### variable inmax

```
int inmax;
```


-------------------------------

Updated on 2025-02-12 at 16:10:30 +0000