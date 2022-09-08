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
| | **[RandomBasis](/documentation/code/classes/classrandombasis/#function-randombasis-randombasis)**(int nin, unsigned long long iin) |
| void | **[ChangeDim](/documentation/code/classes/classrandombasis/#function-randombasis-changedim)**(const int nin) |
| void | **[RandRot](/documentation/code/classes/classrandombasis/#function-randombasis-randrot)**() |
| double | **[RanMult](/documentation/code/classes/classrandombasis/#function-randombasis-ranmult)**(double ** cin) |
| void | **[RanMult](/documentation/code/classes/classrandombasis/#function-randombasis-ranmult)**(const double in, double * out) |
| void | **[RanMult](/documentation/code/classes/classrandombasis/#function-randombasis-ranmult)**(double * in, const double w, double * out) |
| double | **[Mag](/documentation/code/classes/classrandombasis/#function-randombasis-mag)**(double * a, double * a0) |
| void | **[Adjust](/documentation/code/classes/classrandombasis/#function-randombasis-adjust)**(double * a, const double lim, const int iin) |
| virtual void | **[operator++](/documentation/code/classes/classrandombasis/#function-randombasis-operator)**(int ) |
| virtual | **[~RandomBasis](/documentation/code/classes/classrandombasis/#function-randombasis-randombasis)**() |
| | **[RandomBasis](/documentation/code/classes/classrandombasis/#function-randombasis-randombasis)**(int nin, unsigned long long iin) |
| void | **[ChangeDim](/documentation/code/classes/classrandombasis/#function-randombasis-changedim)**(const int nin) |
| void | **[RandRot](/documentation/code/classes/classrandombasis/#function-randombasis-randrot)**() |
| double | **[RanMult](/documentation/code/classes/classrandombasis/#function-randombasis-ranmult)**(double ** cin) |
| void | **[RanMult](/documentation/code/classes/classrandombasis/#function-randombasis-ranmult)**(const double in, double * out) |
| void | **[RanMult](/documentation/code/classes/classrandombasis/#function-randombasis-ranmult)**(double * in, const double w, double * out) |
| double | **[Mag](/documentation/code/classes/classrandombasis/#function-randombasis-mag)**(double * a, double * a0) |
| void | **[Adjust](/documentation/code/classes/classrandombasis/#function-randombasis-adjust)**(double * a, const double lim, const int iin) |
| virtual void | **[operator++](/documentation/code/classes/classrandombasis/#function-randombasis-operator)**(int ) |
| virtual | **[~RandomBasis](/documentation/code/classes/classrandombasis/#function-randombasis-randombasis)**() |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| int | **[num](/documentation/code/classes/classrandombasis/#variable-randombasis-num)**  |
| double ** | **[currentVec](/documentation/code/classes/classrandombasis/#variable-randombasis-currentvec)**  |
| double ** | **[endVec](/documentation/code/classes/classrandombasis/#variable-randombasis-endvec)**  |

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

**Public Functions inherited from [BasicDevs](/documentation/code/classes/classbasicdevs/)**

|                | Name           |
| -------------- | -------------- |
| | **[BasicDevs](/documentation/code/classes/classbasicdevs/#function-basicdevs-basicdevs)**(unsigned long long i) |
| double | **[Dev](/documentation/code/classes/classbasicdevs/#function-basicdevs-dev)**() |
| double | **[ExpDev](/documentation/code/classes/classbasicdevs/#function-basicdevs-expdev)**() |
| | **[BasicDevs](/documentation/code/classes/classbasicdevs/#function-basicdevs-basicdevs)**(unsigned long long i) |
| double | **[Dev](/documentation/code/classes/classbasicdevs/#function-basicdevs-dev)**() |
| double | **[ExpDev](/documentation/code/classes/classbasicdevs/#function-basicdevs-expdev)**() |

**Public Functions inherited from [Ran](/documentation/code/classes/classran/)**

|                | Name           |
| -------------- | -------------- |
| | **[Ran](/documentation/code/classes/classran/#function-ran-ran)**(unsigned long long int ) |
| double | **[Doub](/documentation/code/classes/classran/#function-ran-doub)**() |
| | **[Ran](/documentation/code/classes/classran/#function-ran-ran)**(unsigned long long int ) |
| double | **[Doub](/documentation/code/classes/classran/#function-ran-doub)**() |


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


**Reimplemented by**: [TransformRandomBasis::operator++](/documentation/code/classes/classtransformrandombasis/#function-transformrandombasis-operator), [TransformRandomBasis::operator++](/documentation/code/classes/classtransformrandombasis/#function-transformrandombasis-operator)


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


**Reimplemented by**: [TransformRandomBasis::operator++](/documentation/code/classes/classtransformrandombasis/#function-transformrandombasis-operator), [TransformRandomBasis::operator++](/documentation/code/classes/classtransformrandombasis/#function-transformrandombasis-operator)


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

Updated on 2022-09-08 at 01:48:53 +0000