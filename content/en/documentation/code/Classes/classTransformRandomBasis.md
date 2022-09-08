---
title: "class TransformRandomBasis"

description: "[No description available]"

---

# class TransformRandomBasis



[No description available]

Inherits from [RandomBasis](/documentation/code/classes/classrandombasis/), [Cholesky](/documentation/code/classes/classcholesky/), [RandomBasis](/documentation/code/classes/classrandombasis/), [Cholesky](/documentation/code/classes/classcholesky/), [BasicDevs](/documentation/code/classes/classbasicdevs/), [Ran](/documentation/code/classes/classran/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[TransformRandomBasis](/documentation/code/classes/classtransformrandombasis/#function-transformrandombasis-transformrandombasis)**(double ** vvar, int nin, unsigned long long iin) |
| virtual void | **[operator++](/documentation/code/classes/classtransformrandombasis/#function-transformrandombasis-operator)**(int ) |
| | **[TransformRandomBasis](/documentation/code/classes/classtransformrandombasis/#function-transformrandombasis-transformrandombasis)**(double ** vvar, int nin, unsigned long long iin) |
| virtual void | **[operator++](/documentation/code/classes/classtransformrandombasis/#function-transformrandombasis-operator)**(int ) |

## Additional inherited members

**Public Functions inherited from [RandomBasis](/documentation/code/classes/classrandombasis/)**

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
| virtual | **[~RandomBasis](/documentation/code/classes/classrandombasis/#function-randombasis-randombasis)**() |
| | **[RandomBasis](/documentation/code/classes/classrandombasis/#function-randombasis-randombasis)**(int nin, unsigned long long iin) |
| void | **[ChangeDim](/documentation/code/classes/classrandombasis/#function-randombasis-changedim)**(const int nin) |
| void | **[RandRot](/documentation/code/classes/classrandombasis/#function-randombasis-randrot)**() |
| double | **[RanMult](/documentation/code/classes/classrandombasis/#function-randombasis-ranmult)**(double ** cin) |
| void | **[RanMult](/documentation/code/classes/classrandombasis/#function-randombasis-ranmult)**(const double in, double * out) |
| void | **[RanMult](/documentation/code/classes/classrandombasis/#function-randombasis-ranmult)**(double * in, const double w, double * out) |
| double | **[Mag](/documentation/code/classes/classrandombasis/#function-randombasis-mag)**(double * a, double * a0) |
| void | **[Adjust](/documentation/code/classes/classrandombasis/#function-randombasis-adjust)**(double * a, const double lim, const int iin) |
| virtual | **[~RandomBasis](/documentation/code/classes/classrandombasis/#function-randombasis-randombasis)**() |

**Protected Attributes inherited from [RandomBasis](/documentation/code/classes/classrandombasis/)**

|                | Name           |
| -------------- | -------------- |
| double ** | **[currentVec](/documentation/code/classes/classrandombasis/#variable-randombasis-currentvec)**  |
| double ** | **[endVec](/documentation/code/classes/classrandombasis/#variable-randombasis-endvec)**  |

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

**Public Functions inherited from [RandomBasis](/documentation/code/classes/classrandombasis/)**

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
| virtual | **[~RandomBasis](/documentation/code/classes/classrandombasis/#function-randombasis-randombasis)**() |
| | **[RandomBasis](/documentation/code/classes/classrandombasis/#function-randombasis-randombasis)**(int nin, unsigned long long iin) |
| void | **[ChangeDim](/documentation/code/classes/classrandombasis/#function-randombasis-changedim)**(const int nin) |
| void | **[RandRot](/documentation/code/classes/classrandombasis/#function-randombasis-randrot)**() |
| double | **[RanMult](/documentation/code/classes/classrandombasis/#function-randombasis-ranmult)**(double ** cin) |
| void | **[RanMult](/documentation/code/classes/classrandombasis/#function-randombasis-ranmult)**(const double in, double * out) |
| void | **[RanMult](/documentation/code/classes/classrandombasis/#function-randombasis-ranmult)**(double * in, const double w, double * out) |
| double | **[Mag](/documentation/code/classes/classrandombasis/#function-randombasis-mag)**(double * a, double * a0) |
| void | **[Adjust](/documentation/code/classes/classrandombasis/#function-randombasis-adjust)**(double * a, const double lim, const int iin) |
| virtual | **[~RandomBasis](/documentation/code/classes/classrandombasis/#function-randombasis-randombasis)**() |

**Protected Attributes inherited from [RandomBasis](/documentation/code/classes/classrandombasis/)**

|                | Name           |
| -------------- | -------------- |
| double ** | **[currentVec](/documentation/code/classes/classrandombasis/#variable-randombasis-currentvec)**  |
| double ** | **[endVec](/documentation/code/classes/classrandombasis/#variable-randombasis-endvec)**  |

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

### function TransformRandomBasis

```
inline TransformRandomBasis(
    double ** vvar,
    int nin,
    unsigned long long iin
)
```


### function operator++

```
inline virtual void operator++(
    int 
)
```


**Reimplements**: [RandomBasis::operator++](/documentation/code/classes/classrandombasis/#function-randombasis-operator)


### function TransformRandomBasis

```
inline TransformRandomBasis(
    double ** vvar,
    int nin,
    unsigned long long iin
)
```


### function operator++

```
inline virtual void operator++(
    int 
)
```


**Reimplements**: [RandomBasis::operator++](/documentation/code/classes/classrandombasis/#function-randombasis-operator)


-------------------------------

Updated on 2022-09-08 at 02:00:46 +0000