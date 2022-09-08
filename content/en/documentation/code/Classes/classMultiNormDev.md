---
title: "class MultiNormDev"

description: "[No description available]"

---

# class MultiNormDev



[No description available]

Inherits from [RandomBasis](/documentation/code/classes/classrandombasis/), [Cholesky](/documentation/code/classes/classcholesky/), [RandomBasis](/documentation/code/classes/classrandombasis/), [Cholesky](/documentation/code/classes/classcholesky/), [BasicDevs](/documentation/code/classes/classbasicdevs/), [Ran](/documentation/code/classes/classran/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[MultiNormDev](/documentation/code/classes/classmultinormdev/)**(int nin, double din, unsigned long long iin) |
| | **[MultiNormDev](/documentation/code/classes/classmultinormdev/)**(double ** vvar, const int nin, double din, unsigned long long iin) |
| void | **[MultiDev](/documentation/code/classes/classmultinormdev/)**(double * pin, double * p0) |
| void | **[MultiDev](/documentation/code/classes/classmultinormdev/)**(double ** cvar, double * pin, double * p0) |
| void | **[MultiDevGauss](/documentation/code/classes/classmultinormdev/)**(double ** cvar, double * pin, double * p0) |
| void | **[EllipseDev](/documentation/code/classes/classmultinormdev/)**(double * pin, double * p0, double fin) |
| void | **[EllipseDev](/documentation/code/classes/classmultinormdev/)**(double ** cvar, double * pin, double * p0, double fin) |
| | **[MultiNormDev](/documentation/code/classes/classmultinormdev/)**(int nin, double din, unsigned long long iin) |
| | **[MultiNormDev](/documentation/code/classes/classmultinormdev/)**(double ** vvar, const int nin, double din, unsigned long long iin) |
| void | **[MultiDev](/documentation/code/classes/classmultinormdev/)**(double * pin, double * p0) |
| void | **[MultiDev](/documentation/code/classes/classmultinormdev/)**(double ** cvar, double * pin, double * p0) |
| void | **[MultiDevGauss](/documentation/code/classes/classmultinormdev/)**(double ** cvar, double * pin, double * p0) |
| void | **[EllipseDev](/documentation/code/classes/classmultinormdev/)**(double * pin, double * p0, double fin) |
| void | **[EllipseDev](/documentation/code/classes/classmultinormdev/)**(double ** cvar, double * pin, double * p0, double fin) |

## Additional inherited members

**Public Functions inherited from [RandomBasis](/documentation/code/classes/classrandombasis/)**

|                | Name           |
| -------------- | -------------- |
| | **[RandomBasis](/documentation/code/classes/classrandombasis/)**(int nin, unsigned long long iin) |
| void | **[ChangeDim](/documentation/code/classes/classrandombasis/)**(const int nin) |
| void | **[RandRot](/documentation/code/classes/classrandombasis/)**() |
| double | **[RanMult](/documentation/code/classes/classrandombasis/)**(double ** cin) |
| void | **[RanMult](/documentation/code/classes/classrandombasis/)**(const double in, double * out) |
| void | **[RanMult](/documentation/code/classes/classrandombasis/)**(double * in, const double w, double * out) |
| double | **[Mag](/documentation/code/classes/classrandombasis/)**(double * a, double * a0) |
| void | **[Adjust](/documentation/code/classes/classrandombasis/)**(double * a, const double lim, const int iin) |
| virtual void | **[operator++](/documentation/code/classes/classrandombasis/)**(int ) |
| virtual | **[~RandomBasis](/documentation/code/classes/classrandombasis/)**() |
| | **[RandomBasis](/documentation/code/classes/classrandombasis/)**(int nin, unsigned long long iin) |
| void | **[ChangeDim](/documentation/code/classes/classrandombasis/)**(const int nin) |
| void | **[RandRot](/documentation/code/classes/classrandombasis/)**() |
| double | **[RanMult](/documentation/code/classes/classrandombasis/)**(double ** cin) |
| void | **[RanMult](/documentation/code/classes/classrandombasis/)**(const double in, double * out) |
| void | **[RanMult](/documentation/code/classes/classrandombasis/)**(double * in, const double w, double * out) |
| double | **[Mag](/documentation/code/classes/classrandombasis/)**(double * a, double * a0) |
| void | **[Adjust](/documentation/code/classes/classrandombasis/)**(double * a, const double lim, const int iin) |
| virtual void | **[operator++](/documentation/code/classes/classrandombasis/)**(int ) |
| virtual | **[~RandomBasis](/documentation/code/classes/classrandombasis/)**() |

**Protected Attributes inherited from [RandomBasis](/documentation/code/classes/classrandombasis/)**

|                | Name           |
| -------------- | -------------- |
| double ** | **[currentVec](/documentation/code/classes/classrandombasis/)**  |
| double ** | **[endVec](/documentation/code/classes/classrandombasis/)**  |

**Public Functions inherited from [Cholesky](/documentation/code/classes/classcholesky/)**

|                | Name           |
| -------------- | -------------- |
| | **[Cholesky](/documentation/code/classes/classcholesky/)**(const int nin) |
| | **[Cholesky](/documentation/code/classes/classcholesky/)**(double ** a, const int nin) |
| bool | **[EnterMatM](/documentation/code/classes/classcholesky/)**(double ** a, const int min) |
| bool | **[EnterMat](/documentation/code/classes/classcholesky/)**(double ** a) |
| void | **[EnterMat](/documentation/code/classes/classcholesky/)**(double ** a, int nin) |
| void | **[ElMult](/documentation/code/classes/classcholesky/)**(double * y, double * b) |
| void | **[ElMult](/documentation/code/classes/classcholesky/)**(double * y) |
| void | **[Solve](/documentation/code/classes/classcholesky/)**(double * b, double * x) |
| double | **[Square](/documentation/code/classes/classcholesky/)**(double * y, double * y0) |
| double | **[Square](/documentation/code/classes/classcholesky/)**(double * y, double * y0, int * map) |
| void | **[Inverse](/documentation/code/classes/classcholesky/)**(double ** ainv) |
| double | **[DetSqrt](/documentation/code/classes/classcholesky/)**() |
| | **[~Cholesky](/documentation/code/classes/classcholesky/)**() |
| | **[Cholesky](/documentation/code/classes/classcholesky/)**(const int nin) |
| | **[Cholesky](/documentation/code/classes/classcholesky/)**(double ** a, const int nin) |
| bool | **[EnterMatM](/documentation/code/classes/classcholesky/)**(double ** a, const int min) |
| bool | **[EnterMat](/documentation/code/classes/classcholesky/)**(double ** a) |
| bool | **[EnterMat](/documentation/code/classes/classcholesky/)**(const std::vector< std::vector< double > > & a) |
| void | **[EnterMat](/documentation/code/classes/classcholesky/)**(double ** a, int nin) |
| void | **[ElMult](/documentation/code/classes/classcholesky/)**(double * y, double * b) |
| void | **[ElMult](/documentation/code/classes/classcholesky/)**(double * y) |
| void | **[Solve](/documentation/code/classes/classcholesky/)**(double * b, double * x) |
| double | **[Square](/documentation/code/classes/classcholesky/)**(double * y, double * y0) |
| double | **[Square](/documentation/code/classes/classcholesky/)**(double * y, double * y0, int * map) |
| void | **[Inverse](/documentation/code/classes/classcholesky/)**(double ** ainv) |
| double | **[DetSqrt](/documentation/code/classes/classcholesky/)**() |
| | **[~Cholesky](/documentation/code/classes/classcholesky/)**() |

**Public Functions inherited from [RandomBasis](/documentation/code/classes/classrandombasis/)**

|                | Name           |
| -------------- | -------------- |
| | **[RandomBasis](/documentation/code/classes/classrandombasis/)**(int nin, unsigned long long iin) |
| void | **[ChangeDim](/documentation/code/classes/classrandombasis/)**(const int nin) |
| void | **[RandRot](/documentation/code/classes/classrandombasis/)**() |
| double | **[RanMult](/documentation/code/classes/classrandombasis/)**(double ** cin) |
| void | **[RanMult](/documentation/code/classes/classrandombasis/)**(const double in, double * out) |
| void | **[RanMult](/documentation/code/classes/classrandombasis/)**(double * in, const double w, double * out) |
| double | **[Mag](/documentation/code/classes/classrandombasis/)**(double * a, double * a0) |
| void | **[Adjust](/documentation/code/classes/classrandombasis/)**(double * a, const double lim, const int iin) |
| virtual void | **[operator++](/documentation/code/classes/classrandombasis/)**(int ) |
| virtual | **[~RandomBasis](/documentation/code/classes/classrandombasis/)**() |
| | **[RandomBasis](/documentation/code/classes/classrandombasis/)**(int nin, unsigned long long iin) |
| void | **[ChangeDim](/documentation/code/classes/classrandombasis/)**(const int nin) |
| void | **[RandRot](/documentation/code/classes/classrandombasis/)**() |
| double | **[RanMult](/documentation/code/classes/classrandombasis/)**(double ** cin) |
| void | **[RanMult](/documentation/code/classes/classrandombasis/)**(const double in, double * out) |
| void | **[RanMult](/documentation/code/classes/classrandombasis/)**(double * in, const double w, double * out) |
| double | **[Mag](/documentation/code/classes/classrandombasis/)**(double * a, double * a0) |
| void | **[Adjust](/documentation/code/classes/classrandombasis/)**(double * a, const double lim, const int iin) |
| virtual void | **[operator++](/documentation/code/classes/classrandombasis/)**(int ) |
| virtual | **[~RandomBasis](/documentation/code/classes/classrandombasis/)**() |

**Protected Attributes inherited from [RandomBasis](/documentation/code/classes/classrandombasis/)**

|                | Name           |
| -------------- | -------------- |
| double ** | **[currentVec](/documentation/code/classes/classrandombasis/)**  |
| double ** | **[endVec](/documentation/code/classes/classrandombasis/)**  |

**Public Functions inherited from [Cholesky](/documentation/code/classes/classcholesky/)**

|                | Name           |
| -------------- | -------------- |
| | **[Cholesky](/documentation/code/classes/classcholesky/)**(const int nin) |
| | **[Cholesky](/documentation/code/classes/classcholesky/)**(double ** a, const int nin) |
| bool | **[EnterMatM](/documentation/code/classes/classcholesky/)**(double ** a, const int min) |
| bool | **[EnterMat](/documentation/code/classes/classcholesky/)**(double ** a) |
| void | **[EnterMat](/documentation/code/classes/classcholesky/)**(double ** a, int nin) |
| void | **[ElMult](/documentation/code/classes/classcholesky/)**(double * y, double * b) |
| void | **[ElMult](/documentation/code/classes/classcholesky/)**(double * y) |
| void | **[Solve](/documentation/code/classes/classcholesky/)**(double * b, double * x) |
| double | **[Square](/documentation/code/classes/classcholesky/)**(double * y, double * y0) |
| double | **[Square](/documentation/code/classes/classcholesky/)**(double * y, double * y0, int * map) |
| void | **[Inverse](/documentation/code/classes/classcholesky/)**(double ** ainv) |
| double | **[DetSqrt](/documentation/code/classes/classcholesky/)**() |
| | **[~Cholesky](/documentation/code/classes/classcholesky/)**() |
| | **[Cholesky](/documentation/code/classes/classcholesky/)**(const int nin) |
| | **[Cholesky](/documentation/code/classes/classcholesky/)**(double ** a, const int nin) |
| bool | **[EnterMatM](/documentation/code/classes/classcholesky/)**(double ** a, const int min) |
| bool | **[EnterMat](/documentation/code/classes/classcholesky/)**(double ** a) |
| bool | **[EnterMat](/documentation/code/classes/classcholesky/)**(const std::vector< std::vector< double > > & a) |
| void | **[EnterMat](/documentation/code/classes/classcholesky/)**(double ** a, int nin) |
| void | **[ElMult](/documentation/code/classes/classcholesky/)**(double * y, double * b) |
| void | **[ElMult](/documentation/code/classes/classcholesky/)**(double * y) |
| void | **[Solve](/documentation/code/classes/classcholesky/)**(double * b, double * x) |
| double | **[Square](/documentation/code/classes/classcholesky/)**(double * y, double * y0) |
| double | **[Square](/documentation/code/classes/classcholesky/)**(double * y, double * y0, int * map) |
| void | **[Inverse](/documentation/code/classes/classcholesky/)**(double ** ainv) |
| double | **[DetSqrt](/documentation/code/classes/classcholesky/)**() |
| | **[~Cholesky](/documentation/code/classes/classcholesky/)**() |

**Public Functions inherited from [BasicDevs](/documentation/code/classes/classbasicdevs/)**

|                | Name           |
| -------------- | -------------- |
| | **[BasicDevs](/documentation/code/classes/classbasicdevs/)**(unsigned long long i) |
| double | **[Dev](/documentation/code/classes/classbasicdevs/)**() |
| double | **[ExpDev](/documentation/code/classes/classbasicdevs/)**() |
| | **[BasicDevs](/documentation/code/classes/classbasicdevs/)**(unsigned long long i) |
| double | **[Dev](/documentation/code/classes/classbasicdevs/)**() |
| double | **[ExpDev](/documentation/code/classes/classbasicdevs/)**() |

**Public Functions inherited from [Ran](/documentation/code/classes/classran/)**

|                | Name           |
| -------------- | -------------- |
| | **[Ran](/documentation/code/classes/classran/)**(unsigned long long int ) |
| double | **[Doub](/documentation/code/classes/classran/)**() |
| | **[Ran](/documentation/code/classes/classran/)**(unsigned long long int ) |
| double | **[Doub](/documentation/code/classes/classran/)**() |


## Public Functions Documentation

### function MultiNormDev

```
inline MultiNormDev(
    int nin,
    double din,
    unsigned long long iin
)
```


### function MultiNormDev

```
inline MultiNormDev(
    double ** vvar,
    const int nin,
    double din,
    unsigned long long iin
)
```


### function MultiDev

```
inline void MultiDev(
    double * pin,
    double * p0
)
```


### function MultiDev

```
inline void MultiDev(
    double ** cvar,
    double * pin,
    double * p0
)
```


### function MultiDevGauss

```
inline void MultiDevGauss(
    double ** cvar,
    double * pin,
    double * p0
)
```


### function EllipseDev

```
inline void EllipseDev(
    double * pin,
    double * p0,
    double fin
)
```


### function EllipseDev

```
inline void EllipseDev(
    double ** cvar,
    double * pin,
    double * p0,
    double fin
)
```


### function MultiNormDev

```
inline MultiNormDev(
    int nin,
    double din,
    unsigned long long iin
)
```


### function MultiNormDev

```
inline MultiNormDev(
    double ** vvar,
    const int nin,
    double din,
    unsigned long long iin
)
```


### function MultiDev

```
inline void MultiDev(
    double * pin,
    double * p0
)
```


### function MultiDev

```
inline void MultiDev(
    double ** cvar,
    double * pin,
    double * p0
)
```


### function MultiDevGauss

```
inline void MultiDevGauss(
    double ** cvar,
    double * pin,
    double * p0
)
```


### function EllipseDev

```
inline void EllipseDev(
    double * pin,
    double * p0,
    double fin
)
```


### function EllipseDev

```
inline void EllipseDev(
    double ** cvar,
    double * pin,
    double * p0,
    double fin
)
```


-------------------------------

Updated on 2022-09-08 at 01:05:15 +0000