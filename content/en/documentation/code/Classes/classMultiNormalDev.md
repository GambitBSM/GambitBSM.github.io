---
title: "class MultiNormalDev"

description: "[No description available]"

---

# class MultiNormalDev



[No description available]

Inherits from [Ran](/documentation/code/classes/classran/), [Cholesky](/documentation/code/classes/classcholesky/), [Ran](/documentation/code/classes/classran/), [Cholesky](/documentation/code/classes/classcholesky/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[MultiNormalDev](/documentation/code/classes/classmultinormaldev/#function-multinormaldev-multinormaldev)**(double ** vvar, double fin, unsigned long long int j, int nin) |
| void | **[Dev](/documentation/code/classes/classmultinormaldev/#function-multinormaldev-dev)**(double * pt, double * mean) |
| void | **[Dev](/documentation/code/classes/classmultinormaldev/#function-multinormaldev-dev)**(double ** cvar, double * pt, double * mean) |
| | **[~MultiNormalDev](/documentation/code/classes/classmultinormaldev/#function-multinormaldev-multinormaldev)**() |
| | **[MultiNormalDev](/documentation/code/classes/classmultinormaldev/#function-multinormaldev-multinormaldev)**(double ** vvar, double fin, unsigned long long int j, int nin) |
| void | **[Dev](/documentation/code/classes/classmultinormaldev/#function-multinormaldev-dev)**(double * pt, double * mean) |
| void | **[Dev](/documentation/code/classes/classmultinormaldev/#function-multinormaldev-dev)**(double ** cvar, double * pt, double * mean) |
| | **[~MultiNormalDev](/documentation/code/classes/classmultinormaldev/#function-multinormaldev-multinormaldev)**() |

## Additional inherited members

**Public Functions inherited from [Ran](/documentation/code/classes/classran/)**

|                | Name           |
| -------------- | -------------- |
| | **[Ran](/documentation/code/classes/classran/#function-ran-ran)**(unsigned long long int ) |
| double | **[Doub](/documentation/code/classes/classran/#function-ran-doub)**() |
| | **[Ran](/documentation/code/classes/classran/#function-ran-ran)**(unsigned long long int ) |
| double | **[Doub](/documentation/code/classes/classran/#function-ran-doub)**() |

**Public Functions inherited from [Cholesky](/documentation/code/classes/classcholesky/)**

|                | Name           |
| -------------- | -------------- |
| | **[Cholesky](/documentation/code/classes/classcholesky/#function-cholesky-cholesky)**(const int nin) |
| | **[Cholesky](/documentation/code/classes/classcholesky/#function-cholesky-cholesky)**(double ** a, const int nin) |
| bool | **[EnterMatM](/documentation/code/classes/classcholesky/#function-cholesky-entermatm)**(double ** a, const int min) |
| bool | **[EnterMat](/documentation/code/classes/classcholesky/#function-cholesky-entermat)**(double ** a) |
| void | **[EnterMat](/documentation/code/classes/classcholesky/#function-cholesky-entermat)**(double ** a, int nin) |
| void | **[ElMult](/documentation/code/classes/classcholesky/#function-cholesky-elmult)**(double * y, double * b) |
| void | **[ElMult](/documentation/code/classes/classcholesky/#function-cholesky-elmult)**(double * y) |
| void | **[Solve](/documentation/code/classes/classcholesky/#function-cholesky-solve)**(double * b, double * x) |
| double | **[Square](/documentation/code/classes/classcholesky/#function-cholesky-square)**(double * y, double * y0) |
| double | **[Square](/documentation/code/classes/classcholesky/#function-cholesky-square)**(double * y, double * y0, int * map) |
| void | **[Inverse](/documentation/code/classes/classcholesky/#function-cholesky-inverse)**(double ** ainv) |
| double | **[DetSqrt](/documentation/code/classes/classcholesky/#function-cholesky-detsqrt)**() |
| | **[~Cholesky](/documentation/code/classes/classcholesky/#function-cholesky-cholesky)**() |
| | **[Cholesky](/documentation/code/classes/classcholesky/#function-cholesky-cholesky)**(const int nin) |
| | **[Cholesky](/documentation/code/classes/classcholesky/#function-cholesky-cholesky)**(double ** a, const int nin) |
| bool | **[EnterMatM](/documentation/code/classes/classcholesky/#function-cholesky-entermatm)**(double ** a, const int min) |
| bool | **[EnterMat](/documentation/code/classes/classcholesky/#function-cholesky-entermat)**(double ** a) |
| bool | **[EnterMat](/documentation/code/classes/classcholesky/#function-cholesky-entermat)**(const std::vector< std::vector< double > > & a) |
| void | **[EnterMat](/documentation/code/classes/classcholesky/#function-cholesky-entermat)**(double ** a, int nin) |
| void | **[ElMult](/documentation/code/classes/classcholesky/#function-cholesky-elmult)**(double * y, double * b) |
| void | **[ElMult](/documentation/code/classes/classcholesky/#function-cholesky-elmult)**(double * y) |
| void | **[Solve](/documentation/code/classes/classcholesky/#function-cholesky-solve)**(double * b, double * x) |
| double | **[Square](/documentation/code/classes/classcholesky/#function-cholesky-square)**(double * y, double * y0) |
| double | **[Square](/documentation/code/classes/classcholesky/#function-cholesky-square)**(double * y, double * y0, int * map) |
| void | **[Inverse](/documentation/code/classes/classcholesky/#function-cholesky-inverse)**(double ** ainv) |
| double | **[DetSqrt](/documentation/code/classes/classcholesky/#function-cholesky-detsqrt)**() |
| | **[~Cholesky](/documentation/code/classes/classcholesky/#function-cholesky-cholesky)**() |

**Protected Attributes inherited from [Cholesky](/documentation/code/classes/classcholesky/)**

|                | Name           |
| -------------- | -------------- |
| int | **[num](/documentation/code/classes/classcholesky/#variable-cholesky-num)**  |

**Public Functions inherited from [Ran](/documentation/code/classes/classran/)**

|                | Name           |
| -------------- | -------------- |
| | **[Ran](/documentation/code/classes/classran/#function-ran-ran)**(unsigned long long int ) |
| double | **[Doub](/documentation/code/classes/classran/#function-ran-doub)**() |
| | **[Ran](/documentation/code/classes/classran/#function-ran-ran)**(unsigned long long int ) |
| double | **[Doub](/documentation/code/classes/classran/#function-ran-doub)**() |

**Public Functions inherited from [Cholesky](/documentation/code/classes/classcholesky/)**

|                | Name           |
| -------------- | -------------- |
| | **[Cholesky](/documentation/code/classes/classcholesky/#function-cholesky-cholesky)**(const int nin) |
| | **[Cholesky](/documentation/code/classes/classcholesky/#function-cholesky-cholesky)**(double ** a, const int nin) |
| bool | **[EnterMatM](/documentation/code/classes/classcholesky/#function-cholesky-entermatm)**(double ** a, const int min) |
| bool | **[EnterMat](/documentation/code/classes/classcholesky/#function-cholesky-entermat)**(double ** a) |
| void | **[EnterMat](/documentation/code/classes/classcholesky/#function-cholesky-entermat)**(double ** a, int nin) |
| void | **[ElMult](/documentation/code/classes/classcholesky/#function-cholesky-elmult)**(double * y, double * b) |
| void | **[ElMult](/documentation/code/classes/classcholesky/#function-cholesky-elmult)**(double * y) |
| void | **[Solve](/documentation/code/classes/classcholesky/#function-cholesky-solve)**(double * b, double * x) |
| double | **[Square](/documentation/code/classes/classcholesky/#function-cholesky-square)**(double * y, double * y0) |
| double | **[Square](/documentation/code/classes/classcholesky/#function-cholesky-square)**(double * y, double * y0, int * map) |
| void | **[Inverse](/documentation/code/classes/classcholesky/#function-cholesky-inverse)**(double ** ainv) |
| double | **[DetSqrt](/documentation/code/classes/classcholesky/#function-cholesky-detsqrt)**() |
| | **[~Cholesky](/documentation/code/classes/classcholesky/#function-cholesky-cholesky)**() |
| | **[Cholesky](/documentation/code/classes/classcholesky/#function-cholesky-cholesky)**(const int nin) |
| | **[Cholesky](/documentation/code/classes/classcholesky/#function-cholesky-cholesky)**(double ** a, const int nin) |
| bool | **[EnterMatM](/documentation/code/classes/classcholesky/#function-cholesky-entermatm)**(double ** a, const int min) |
| bool | **[EnterMat](/documentation/code/classes/classcholesky/#function-cholesky-entermat)**(double ** a) |
| bool | **[EnterMat](/documentation/code/classes/classcholesky/#function-cholesky-entermat)**(const std::vector< std::vector< double > > & a) |
| void | **[EnterMat](/documentation/code/classes/classcholesky/#function-cholesky-entermat)**(double ** a, int nin) |
| void | **[ElMult](/documentation/code/classes/classcholesky/#function-cholesky-elmult)**(double * y, double * b) |
| void | **[ElMult](/documentation/code/classes/classcholesky/#function-cholesky-elmult)**(double * y) |
| void | **[Solve](/documentation/code/classes/classcholesky/#function-cholesky-solve)**(double * b, double * x) |
| double | **[Square](/documentation/code/classes/classcholesky/#function-cholesky-square)**(double * y, double * y0) |
| double | **[Square](/documentation/code/classes/classcholesky/#function-cholesky-square)**(double * y, double * y0, int * map) |
| void | **[Inverse](/documentation/code/classes/classcholesky/#function-cholesky-inverse)**(double ** ainv) |
| double | **[DetSqrt](/documentation/code/classes/classcholesky/#function-cholesky-detsqrt)**() |
| | **[~Cholesky](/documentation/code/classes/classcholesky/#function-cholesky-cholesky)**() |

**Protected Attributes inherited from [Cholesky](/documentation/code/classes/classcholesky/)**

|                | Name           |
| -------------- | -------------- |
| int | **[num](/documentation/code/classes/classcholesky/#variable-cholesky-num)**  |


## Public Functions Documentation

### function MultiNormalDev

```
inline MultiNormalDev(
    double ** vvar,
    double fin,
    unsigned long long int j,
    int nin
)
```


### function Dev

```
inline void Dev(
    double * pt,
    double * mean
)
```


### function Dev

```
inline void Dev(
    double ** cvar,
    double * pt,
    double * mean
)
```


### function ~MultiNormalDev

```
inline ~MultiNormalDev()
```


### function MultiNormalDev

```
inline MultiNormalDev(
    double ** vvar,
    double fin,
    unsigned long long int j,
    int nin
)
```


### function Dev

```
inline void Dev(
    double * pt,
    double * mean
)
```


### function Dev

```
inline void Dev(
    double ** cvar,
    double * pt,
    double * mean
)
```


### function ~MultiNormalDev

```
inline ~MultiNormalDev()
```


-------------------------------

Updated on 2022-09-08 at 01:48:53 +0000