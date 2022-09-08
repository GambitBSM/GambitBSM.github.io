---
title: "class Cholesky"

description: "[No description available]"

---

# class Cholesky



[No description available]

Inherited by [AdvanceDevs](/documentation/code/classes/classadvancedevs/), [AdvanceDevs](/documentation/code/classes/classadvancedevs/), [MultiNormDev](/documentation/code/classes/classmultinormdev/), [MultiNormDev](/documentation/code/classes/classmultinormdev/), [MultiNormalDev](/documentation/code/classes/classmultinormaldev/), [MultiNormalDev](/documentation/code/classes/classmultinormaldev/), [TransformRandomBasis](/documentation/code/classes/classtransformrandombasis/), [TransformRandomBasis](/documentation/code/classes/classtransformrandombasis/)

## Public Functions

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

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| int | **[num](/documentation/code/classes/classcholesky/#variable-cholesky-num)**  |

## Public Functions Documentation

### function Cholesky

```
inline Cholesky(
    const int nin
)
```


### function Cholesky

```
inline Cholesky(
    double ** a,
    const int nin
)
```


### function EnterMatM

```
inline bool EnterMatM(
    double ** a,
    const int min
)
```


### function EnterMat

```
inline bool EnterMat(
    double ** a
)
```


### function EnterMat

```
inline void EnterMat(
    double ** a,
    int nin
)
```


### function ElMult

```
inline void ElMult(
    double * y,
    double * b
)
```


### function ElMult

```
inline void ElMult(
    double * y
)
```


### function Solve

```
inline void Solve(
    double * b,
    double * x
)
```


### function Square

```
inline double Square(
    double * y,
    double * y0
)
```


### function Square

```
inline double Square(
    double * y,
    double * y0,
    int * map
)
```


### function Inverse

```
inline void Inverse(
    double ** ainv
)
```


### function DetSqrt

```
inline double DetSqrt()
```


### function ~Cholesky

```
inline ~Cholesky()
```


### function Cholesky

```
inline Cholesky(
    const int nin
)
```


### function Cholesky

```
inline Cholesky(
    double ** a,
    const int nin
)
```


### function EnterMatM

```
inline bool EnterMatM(
    double ** a,
    const int min
)
```


### function EnterMat

```
inline bool EnterMat(
    double ** a
)
```


### function EnterMat

```
inline bool EnterMat(
    const std::vector< std::vector< double > > & a
)
```


### function EnterMat

```
inline void EnterMat(
    double ** a,
    int nin
)
```


### function ElMult

```
inline void ElMult(
    double * y,
    double * b
)
```


### function ElMult

```
inline void ElMult(
    double * y
)
```


### function Solve

```
inline void Solve(
    double * b,
    double * x
)
```


### function Square

```
inline double Square(
    double * y,
    double * y0
)
```


### function Square

```
inline double Square(
    double * y,
    double * y0,
    int * map
)
```


### function Inverse

```
inline void Inverse(
    double ** ainv
)
```


### function DetSqrt

```
inline double DetSqrt()
```


### function ~Cholesky

```
inline ~Cholesky()
```


## Protected Attributes Documentation

### variable num

```
int num;
```


-------------------------------

Updated on 2022-09-08 at 01:48:53 +0000