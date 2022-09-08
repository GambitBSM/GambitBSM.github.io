---
title: "class AdvanceDevs"

description: "[No description available]"

---

# class AdvanceDevs



[No description available]

Inherits from [BasicDevs](/documentation/code/classes/classbasicdevs/), [Cholesky](/documentation/code/classes/classcholesky/), [BasicDevs](/documentation/code/classes/classbasicdevs/), [Cholesky](/documentation/code/classes/classcholesky/), [Ran](/documentation/code/classes/classran/)

Inherited by [RandomPlane](/documentation/code/classes/classrandomplane/), [RandomPlane](/documentation/code/classes/classrandomplane/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[AdvanceDevs](/documentation/code/classes/classadvancedevs/)**(int nin, double din, unsigned long long iin) |
| | **[AdvanceDevs](/documentation/code/classes/classadvancedevs/)**(double ** vvar, const int nin, double din, unsigned long long iin) |
| void | **[MultiDev](/documentation/code/classes/classadvancedevs/)**(double * pin, double * p0) |
| void | **[MultiDev](/documentation/code/classes/classadvancedevs/)**(double ** cvar, double * pin, double * p0) |
| void | **[EllipseDev](/documentation/code/classes/classadvancedevs/)**(double * pin, double * p0, double fin) |
| void | **[EllipseDev](/documentation/code/classes/classadvancedevs/)**(double ** cvar, double * pin, double * p0, double fin) |
| | **[AdvanceDevs](/documentation/code/classes/classadvancedevs/)**(int nin, double din, unsigned long long iin) |
| | **[AdvanceDevs](/documentation/code/classes/classadvancedevs/)**(double ** vvar, const int nin, double din, unsigned long long iin) |
| double | **[MultiDevDist](/documentation/code/classes/classadvancedevs/)**() |
| double | **[MultiDevPDF](/documentation/code/classes/classadvancedevs/)**(double r, int dim) |
| void | **[MultiDev](/documentation/code/classes/classadvancedevs/)**(double * pin, double * p0) |
| void | **[MultiDev](/documentation/code/classes/classadvancedevs/)**(double ** cvar, double * pin, double * p0) |
| void | **[EllipseDev](/documentation/code/classes/classadvancedevs/)**(double * pin, double * p0, double fin) |
| void | **[EllipseDev](/documentation/code/classes/classadvancedevs/)**(double ** cvar, double * pin, double * p0, double fin) |

## Additional inherited members

**Public Functions inherited from [BasicDevs](/documentation/code/classes/classbasicdevs/)**

|                | Name           |
| -------------- | -------------- |
| | **[BasicDevs](/documentation/code/classes/classbasicdevs/)**(unsigned long long i) |
| double | **[Dev](/documentation/code/classes/classbasicdevs/)**() |
| double | **[ExpDev](/documentation/code/classes/classbasicdevs/)**() |
| | **[BasicDevs](/documentation/code/classes/classbasicdevs/)**(unsigned long long i) |
| double | **[Dev](/documentation/code/classes/classbasicdevs/)**() |
| double | **[ExpDev](/documentation/code/classes/classbasicdevs/)**() |

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

**Protected Attributes inherited from [Cholesky](/documentation/code/classes/classcholesky/)**

|                | Name           |
| -------------- | -------------- |
| int | **[num](/documentation/code/classes/classcholesky/)**  |

**Public Functions inherited from [BasicDevs](/documentation/code/classes/classbasicdevs/)**

|                | Name           |
| -------------- | -------------- |
| | **[BasicDevs](/documentation/code/classes/classbasicdevs/)**(unsigned long long i) |
| double | **[Dev](/documentation/code/classes/classbasicdevs/)**() |
| double | **[ExpDev](/documentation/code/classes/classbasicdevs/)**() |
| | **[BasicDevs](/documentation/code/classes/classbasicdevs/)**(unsigned long long i) |
| double | **[Dev](/documentation/code/classes/classbasicdevs/)**() |
| double | **[ExpDev](/documentation/code/classes/classbasicdevs/)**() |

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

**Protected Attributes inherited from [Cholesky](/documentation/code/classes/classcholesky/)**

|                | Name           |
| -------------- | -------------- |
| int | **[num](/documentation/code/classes/classcholesky/)**  |

**Public Functions inherited from [Ran](/documentation/code/classes/classran/)**

|                | Name           |
| -------------- | -------------- |
| | **[Ran](/documentation/code/classes/classran/)**(unsigned long long int ) |
| double | **[Doub](/documentation/code/classes/classran/)**() |
| | **[Ran](/documentation/code/classes/classran/)**(unsigned long long int ) |
| double | **[Doub](/documentation/code/classes/classran/)**() |


## Public Functions Documentation

### function AdvanceDevs

```
inline AdvanceDevs(
    int nin,
    double din,
    unsigned long long iin
)
```


### function AdvanceDevs

```
inline AdvanceDevs(
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


### function AdvanceDevs

```
inline AdvanceDevs(
    int nin,
    double din,
    unsigned long long iin
)
```


### function AdvanceDevs

```
inline AdvanceDevs(
    double ** vvar,
    const int nin,
    double din,
    unsigned long long iin
)
```


### function MultiDevDist

```
inline double MultiDevDist()
```


### function MultiDevPDF

```
inline double MultiDevPDF(
    double r,
    int dim
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