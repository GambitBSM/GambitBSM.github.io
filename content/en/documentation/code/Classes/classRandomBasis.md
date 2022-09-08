---
title: "class RandomBasis"

description: "[No description available]"

---

# class RandomBasis



[No description available]

Inherits from [BasicDevs](/documentation/code/classes/classbasicdevs/), [BasicDevs](/documentation/code/classes/classbasicdevs/), [Ran](/documentation/code/classes/classran/)

Inherited by [MultiNormDev](/documentation/code/classes/classmultinormdev/), [MultiNormDev](/documentation/code/classes/classmultinormdev/), [TransformRandomBasis](/documentation/code/classes/classtransformrandombasis/), [TransformRandomBasis](/documentation/code/classes/classtransformrandombasis/)

## Public Functions

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

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| int | **[num](/documentation/code/classes/classrandombasis/)**  |
| double ** | **[currentVec](/documentation/code/classes/classrandombasis/)**  |
| double ** | **[endVec](/documentation/code/classes/classrandombasis/)**  |

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

### function RandomBasis

```
inline RandomBasis(
    int nin,
    unsigned long long iin
)
```


### function ChangeDim

```
inline void ChangeDim(
    const int nin
)
```


### function RandRot

```
inline void RandRot()
```


### function RanMult

```
inline double RanMult(
    double ** cin
)
```


### function RanMult

```
inline void RanMult(
    const double in,
    double * out
)
```


### function RanMult

```
inline void RanMult(
    double * in,
    const double w,
    double * out
)
```


### function Mag

```
inline double Mag(
    double * a,
    double * a0
)
```


### function Adjust

```
inline void Adjust(
    double * a,
    const double lim,
    const int iin
)
```


### function operator++

```
inline virtual void operator++(
    int 
)
```


**Reimplemented by**: [TransformRandomBasis::operator++](/documentation/code/classes/classtransformrandombasis/), [TransformRandomBasis::operator++](/documentation/code/classes/classtransformrandombasis/)


### function ~RandomBasis

```
inline virtual ~RandomBasis()
```


### function RandomBasis

```
inline RandomBasis(
    int nin,
    unsigned long long iin
)
```


### function ChangeDim

```
inline void ChangeDim(
    const int nin
)
```


### function RandRot

```
inline void RandRot()
```


### function RanMult

```
inline double RanMult(
    double ** cin
)
```


### function RanMult

```
inline void RanMult(
    const double in,
    double * out
)
```


### function RanMult

```
inline void RanMult(
    double * in,
    const double w,
    double * out
)
```


### function Mag

```
inline double Mag(
    double * a,
    double * a0
)
```


### function Adjust

```
inline void Adjust(
    double * a,
    const double lim,
    const int iin
)
```


### function operator++

```
inline virtual void operator++(
    int 
)
```


**Reimplemented by**: [TransformRandomBasis::operator++](/documentation/code/classes/classtransformrandombasis/), [TransformRandomBasis::operator++](/documentation/code/classes/classtransformrandombasis/)


### function ~RandomBasis

```
inline virtual ~RandomBasis()
```


## Protected Attributes Documentation

### variable num

```
int num;
```


### variable currentVec

```
double ** currentVec;
```


### variable endVec

```
double ** endVec;
```


-------------------------------

Updated on 2022-09-08 at 01:05:15 +0000