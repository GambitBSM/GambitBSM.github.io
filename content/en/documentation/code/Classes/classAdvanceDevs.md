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
| | **[AdvanceDevs](/documentation/code/classes/classadvancedevs/#function-advancedevs-advancedevs)**(int nin, double din, unsigned long long iin) |
| | **[AdvanceDevs](/documentation/code/classes/classadvancedevs/#function-advancedevs-advancedevs)**(double ** vvar, const int nin, double din, unsigned long long iin) |
| void | **[MultiDev](/documentation/code/classes/classadvancedevs/#function-advancedevs-multidev)**(double * pin, double * p0) |
| void | **[MultiDev](/documentation/code/classes/classadvancedevs/#function-advancedevs-multidev)**(double ** cvar, double * pin, double * p0) |
| void | **[EllipseDev](/documentation/code/classes/classadvancedevs/#function-advancedevs-ellipsedev)**(double * pin, double * p0, double fin) |
| void | **[EllipseDev](/documentation/code/classes/classadvancedevs/#function-advancedevs-ellipsedev)**(double ** cvar, double * pin, double * p0, double fin) |
| | **[AdvanceDevs](/documentation/code/classes/classadvancedevs/#function-advancedevs-advancedevs)**(int nin, double din, unsigned long long iin) |
| | **[AdvanceDevs](/documentation/code/classes/classadvancedevs/#function-advancedevs-advancedevs)**(double ** vvar, const int nin, double din, unsigned long long iin) |
| double | **[MultiDevDist](/documentation/code/classes/classadvancedevs/#function-advancedevs-multidevdist)**() |
| double | **[MultiDevPDF](/documentation/code/classes/classadvancedevs/#function-advancedevs-multidevpdf)**(double r, int dim) |
| void | **[MultiDev](/documentation/code/classes/classadvancedevs/#function-advancedevs-multidev)**(double * pin, double * p0) |
| void | **[MultiDev](/documentation/code/classes/classadvancedevs/#function-advancedevs-multidev)**(double ** cvar, double * pin, double * p0) |
| void | **[EllipseDev](/documentation/code/classes/classadvancedevs/#function-advancedevs-ellipsedev)**(double * pin, double * p0, double fin) |
| void | **[EllipseDev](/documentation/code/classes/classadvancedevs/#function-advancedevs-ellipsedev)**(double ** cvar, double * pin, double * p0, double fin) |

## Additional inherited members

**Public Functions inherited from [BasicDevs](/documentation/code/classes/classbasicdevs/)**

|                | Name           |
| -------------- | -------------- |
| | **[BasicDevs](/documentation/code/classes/classbasicdevs/#function-basicdevs-basicdevs)**(unsigned long long i) |
| double | **[Dev](/documentation/code/classes/classbasicdevs/#function-basicdevs-dev)**() |
| double | **[ExpDev](/documentation/code/classes/classbasicdevs/#function-basicdevs-expdev)**() |
| | **[BasicDevs](/documentation/code/classes/classbasicdevs/#function-basicdevs-basicdevs)**(unsigned long long i) |
| double | **[Dev](/documentation/code/classes/classbasicdevs/#function-basicdevs-dev)**() |
| double | **[ExpDev](/documentation/code/classes/classbasicdevs/#function-basicdevs-expdev)**() |

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

**Public Functions inherited from [BasicDevs](/documentation/code/classes/classbasicdevs/)**

|                | Name           |
| -------------- | -------------- |
| | **[BasicDevs](/documentation/code/classes/classbasicdevs/#function-basicdevs-basicdevs)**(unsigned long long i) |
| double | **[Dev](/documentation/code/classes/classbasicdevs/#function-basicdevs-dev)**() |
| double | **[ExpDev](/documentation/code/classes/classbasicdevs/#function-basicdevs-expdev)**() |
| | **[BasicDevs](/documentation/code/classes/classbasicdevs/#function-basicdevs-basicdevs)**(unsigned long long i) |
| double | **[Dev](/documentation/code/classes/classbasicdevs/#function-basicdevs-dev)**() |
| double | **[ExpDev](/documentation/code/classes/classbasicdevs/#function-basicdevs-expdev)**() |

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

Updated on 2022-09-08 at 02:00:46 +0000