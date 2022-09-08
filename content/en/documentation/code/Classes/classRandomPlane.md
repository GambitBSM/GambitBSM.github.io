---
title: "class RandomPlane"

description: "[No description available]"

---

# class RandomPlane



[No description available]

Inherits from [AdvanceDevs](/documentation/code/classes/classadvancedevs/), [AdvanceDevs](/documentation/code/classes/classadvancedevs/), [BasicDevs](/documentation/code/classes/classbasicdevs/), [Cholesky](/documentation/code/classes/classcholesky/), [Ran](/documentation/code/classes/classran/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[RandomPlane](/documentation/code/classes/classrandomplane/#function-randomplane-randomplane)**(const int projin, const int nin, const double din, const double alim, const double alimt, unsigned long long iin) |
| double | **[WalkDev](/documentation/code/classes/classrandomplane/#function-randomplane-walkdev)**() |
| double | **[TransDev](/documentation/code/classes/classrandomplane/#function-randomplane-transdev)**() |
| double | **[KWalkDev](/documentation/code/classes/classrandomplane/#function-randomplane-kwalkdev)**() |
| bool | **[KWalkDev](/documentation/code/classes/classrandomplane/#function-randomplane-kwalkdev)**(double & Z) |
| double | **[WalkDev](/documentation/code/classes/classrandomplane/#function-randomplane-walkdev)**(double * ptrOut, double * ptr, double * ptr0) |
| double | **[TransDev](/documentation/code/classes/classrandomplane/#function-randomplane-transdev)**(double * ptrOut, double * ptr, double * ptr0) |
| void | **[Mult](/documentation/code/classes/classrandomplane/#function-randomplane-mult)**(double * ptrOut, double * ptr, double * ptr0, const double Z) |
| void | **[Mult2](/documentation/code/classes/classrandomplane/#function-randomplane-mult2)**(double * ptrOut, double * ptr, double * ptr0, const double Z) |
| void | **[RandRot](/documentation/code/classes/classrandomplane/#function-randomplane-randrot)**(const int start =0) |
| void | **[RandRot](/documentation/code/classes/classrandomplane/#function-randomplane-randrot)**(const int start, const int end) |
| int | **[Dim](/documentation/code/classes/classrandomplane/#function-randomplane-dim)**() const |
| | **[~RandomPlane](/documentation/code/classes/classrandomplane/#function-randomplane-randomplane)**() |
| | **[RandomPlane](/documentation/code/classes/classrandomplane/#function-randomplane-randomplane)**(const int projin, const int nin, const double din, const double alim, const double alimt, unsigned long long iin) |
| double | **[WalkDev](/documentation/code/classes/classrandomplane/#function-randomplane-walkdev)**() |
| double | **[TransDev](/documentation/code/classes/classrandomplane/#function-randomplane-transdev)**() |
| double | **[KWalkDev](/documentation/code/classes/classrandomplane/#function-randomplane-kwalkdev)**() |
| bool | **[KWalkDev](/documentation/code/classes/classrandomplane/#function-randomplane-kwalkdev)**(double & Z) |
| double | **[WalkDev](/documentation/code/classes/classrandomplane/#function-randomplane-walkdev)**(double * ptrOut, double * ptr, double * ptr0) |
| double | **[TransDev](/documentation/code/classes/classrandomplane/#function-randomplane-transdev)**(double * ptrOut, double * ptr, double * ptr0) |
| void | **[Mult2](/documentation/code/classes/classrandomplane/#function-randomplane-mult2)**(double * ptrOut, double * ptr, double * ptr0, const double Z) |
| void | **[Mult](/documentation/code/classes/classrandomplane/#function-randomplane-mult)**(double * ptrOut, double * ptr, double * ptr0, const double Z) |
| void | **[HopBlow](/documentation/code/classes/classrandomplane/#function-randomplane-hopblow)**(double * ptrOut, double * ptrIn, double * ptr, double * ptr0) |
| void | **[RandRot](/documentation/code/classes/classrandomplane/#function-randomplane-randrot)**(const int start =0) |
| void | **[RandRot](/documentation/code/classes/classrandomplane/#function-randomplane-randrot)**(const int start, const int end) |
| int | **[Dim](/documentation/code/classes/classrandomplane/#function-randomplane-dim)**() const |
| | **[~RandomPlane](/documentation/code/classes/classrandomplane/#function-randomplane-randomplane)**() |

## Additional inherited members

**Public Functions inherited from [AdvanceDevs](/documentation/code/classes/classadvancedevs/)**

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

**Public Functions inherited from [AdvanceDevs](/documentation/code/classes/classadvancedevs/)**

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

### function RandomPlane

```
inline RandomPlane(
    const int projin,
    const int nin,
    const double din,
    const double alim,
    const double alimt,
    unsigned long long iin
)
```


### function WalkDev

```
inline double WalkDev()
```


### function TransDev

```
inline double TransDev()
```


### function KWalkDev

```
inline double KWalkDev()
```


### function KWalkDev

```
inline bool KWalkDev(
    double & Z
)
```


### function WalkDev

```
inline double WalkDev(
    double * ptrOut,
    double * ptr,
    double * ptr0
)
```


### function TransDev

```
inline double TransDev(
    double * ptrOut,
    double * ptr,
    double * ptr0
)
```


### function Mult

```
inline void Mult(
    double * ptrOut,
    double * ptr,
    double * ptr0,
    const double Z
)
```


### function Mult2

```
inline void Mult2(
    double * ptrOut,
    double * ptr,
    double * ptr0,
    const double Z
)
```


### function RandRot

```
inline void RandRot(
    const int start =0
)
```


### function RandRot

```
inline void RandRot(
    const int start,
    const int end
)
```


### function Dim

```
inline int Dim() const
```


### function ~RandomPlane

```
inline ~RandomPlane()
```


### function RandomPlane

```
inline RandomPlane(
    const int projin,
    const int nin,
    const double din,
    const double alim,
    const double alimt,
    unsigned long long iin
)
```


### function WalkDev

```
inline double WalkDev()
```


### function TransDev

```
inline double TransDev()
```


### function KWalkDev

```
inline double KWalkDev()
```


### function KWalkDev

```
inline bool KWalkDev(
    double & Z
)
```


### function WalkDev

```
inline double WalkDev(
    double * ptrOut,
    double * ptr,
    double * ptr0
)
```


### function TransDev

```
inline double TransDev(
    double * ptrOut,
    double * ptr,
    double * ptr0
)
```


### function Mult2

```
inline void Mult2(
    double * ptrOut,
    double * ptr,
    double * ptr0,
    const double Z
)
```


### function Mult

```
inline void Mult(
    double * ptrOut,
    double * ptr,
    double * ptr0,
    const double Z
)
```


### function HopBlow

```
inline void HopBlow(
    double * ptrOut,
    double * ptrIn,
    double * ptr,
    double * ptr0
)
```


### function RandRot

```
inline void RandRot(
    const int start =0
)
```


### function RandRot

```
inline void RandRot(
    const int start,
    const int end
)
```


### function Dim

```
inline int Dim() const
```


### function ~RandomPlane

```
inline ~RandomPlane()
```


-------------------------------

Updated on 2022-09-08 at 02:00:46 +0000