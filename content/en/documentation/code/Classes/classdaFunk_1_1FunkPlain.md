---
title: "class daFunk::FunkPlain"

description: "[No description available]"

---

# class daFunk::FunkPlain



[No description available]

Inherits from [daFunk::FunkBase](/documentation/code/classes/classdafunk_1_1funkbase/), boost::enable_shared_from_this< FunkBase >

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[FunkPlain](/documentation/code/classes/classdafunk_1_1funkplain/#function-funkplain)**(Funk fin, std::string arg1) |
| | **[FunkPlain](/documentation/code/classes/classdafunk_1_1funkplain/#function-funkplain)**(Funk fin, std::string arg1, std::string arg2) |
| | **[FunkPlain](/documentation/code/classes/classdafunk_1_1funkplain/#function-funkplain)**(Funk fin, std::string arg1, std::string arg2, std::string arg3) |
| | **[FunkPlain](/documentation/code/classes/classdafunk_1_1funkplain/#function-funkplain)**(Funk fin, std::string arg1, std::string arg2, std::string arg3, std::string arg4) |
| virtual double | **[value](/documentation/code/classes/classdafunk_1_1funkplain/#function-value)**(const std::vector< double > & args, size_t bindID) |
| double | **[plain1p](/documentation/code/classes/classdafunk_1_1funkplain/#function-plain1p)**(double x1, void * ptr) |
| double | **[plain2p](/documentation/code/classes/classdafunk_1_1funkplain/#function-plain2p)**(double x1, double x2, void * ptr) |
| double | **[plain3p](/documentation/code/classes/classdafunk_1_1funkplain/#function-plain3p)**(double x1, double x2, double x3, void * ptr) |
| double | **[plain4p](/documentation/code/classes/classdafunk_1_1funkplain/#function-plain4p)**(double x1, double x2, double x3, double x4, void * ptr) |
| template <typename T \> <br>double | **[plain1](/documentation/code/classes/classdafunk_1_1funkplain/#function-plain1)**(double & x1) |
| template <typename T \> <br>double | **[plain2](/documentation/code/classes/classdafunk_1_1funkplain/#function-plain2)**(double & x1, double & x2) |
| template <typename T \> <br>double | **[plain3](/documentation/code/classes/classdafunk_1_1funkplain/#function-plain3)**(double & x1, double & x2, double & x3) |
| template <typename T \> <br>double | **[plain4](/documentation/code/classes/classdafunk_1_1funkplain/#function-plain4)**(double & x1, double & x2, double & x3, double & x4) |

## Additional inherited members

**Public Functions inherited from [daFunk::FunkBase](/documentation/code/classes/classdafunk_1_1funkbase/)**

|                | Name           |
| -------------- | -------------- |
| | **[FunkBase](/documentation/code/classes/classdafunk_1_1funkbase/#function-funkbase)**() |
| virtual | **[~FunkBase](/documentation/code/classes/classdafunk_1_1funkbase/#function-funkbase)**() |
| template <typename... Args\> <br>Funk | **[set](/documentation/code/classes/classdafunk_1_1funkbase/#function-set)**(std::string arg, Funk g, Args... args) |
| template <typename... Args\> <br>Funk | **[set](/documentation/code/classes/classdafunk_1_1funkbase/#function-set)**(std::string arg, double x, Args... args) |
| template <typename... Args\> <br>Funk | **[set](/documentation/code/classes/classdafunk_1_1funkbase/#function-set)**(std::string arg, std::string arg1, Args... args) |
| template <typename... Args\> <br>Funk | **[set](/documentation/code/classes/classdafunk_1_1funkbase/#function-set)**() |
| template <typename... Args\> <br>shared_ptr< [FunkBound](/documentation/code/classes/classdafunk_1_1funkbound/) > | **[bind](/documentation/code/classes/classdafunk_1_1funkbase/#function-bind)**(Args... args) |
| const std::vector< std::string > & | **[getArgs](/documentation/code/classes/classdafunk_1_1funkbase/#function-getargs)**() |
| std::size_t | **[getNArgs](/documentation/code/classes/classdafunk_1_1funkbase/#function-getnargs)**() |
| bool | **[hasArg](/documentation/code/classes/classdafunk_1_1funkbase/#function-hasarg)**(std::string arg) |
| bool | **[hasArgs](/documentation/code/classes/classdafunk_1_1funkbase/#function-hasargs)**() |
| Funk | **[help](/documentation/code/classes/classdafunk_1_1funkbase/#function-help)**() |
| template <typename... Args\> <br>bool | **[assert_args](/documentation/code/classes/classdafunk_1_1funkbase/#function-assert-args)**(Args... args) |
| virtual void | **[resolve](/documentation/code/classes/classdafunk_1_1funkbase/#function-resolve)**(std::map< std::string, size_t > datamap, size_t & datalen, size_t bindID, std::map< std::string, size_t > & argmap) |
| Singularities | **[getSingl](/documentation/code/classes/classdafunk_1_1funkbase/#function-getsingl)**() |
| Funk | **[set_singularity](/documentation/code/classes/classdafunk_1_1funkbase/#function-set-singularity)**(std::string arg, double pos, double width) |
| Funk | **[print](/documentation/code/classes/classdafunk_1_1funkbase/#function-print)**(std::string arg) |
| template <typename... Args\> <br>shared_ptr< [FunkIntegrate_gsl1d](/documentation/code/classes/classdafunk_1_1funkintegrate__gsl1d/) > | **[gsl_integration](/documentation/code/classes/classdafunk_1_1funkbase/#function-gsl-integration)**(Args... args) |
| PlainPtrs1 | **[plain](/documentation/code/classes/classdafunk_1_1funkbase/#function-plain)**(std::string arg1) |
| PlainPtrs2 | **[plain](/documentation/code/classes/classdafunk_1_1funkbase/#function-plain)**(std::string arg1, std::string arg2) |
| PlainPtrs3 | **[plain](/documentation/code/classes/classdafunk_1_1funkbase/#function-plain)**(std::string arg1, std::string arg2, std::string arg3) |
| PlainPtrs4 | **[plain](/documentation/code/classes/classdafunk_1_1funkbase/#function-plain)**(std::string arg1, std::string arg2, std::string arg3, std::string arg4) |
| template <typename T \> <br>PlainPtr1 | **[plain](/documentation/code/classes/classdafunk_1_1funkbase/#function-plain)**(std::string arg1) |
| template <typename T \> <br>PlainPtr2 | **[plain](/documentation/code/classes/classdafunk_1_1funkbase/#function-plain)**(std::string arg1, std::string arg2) |
| template <typename T \> <br>PlainPtr3 | **[plain](/documentation/code/classes/classdafunk_1_1funkbase/#function-plain)**(std::string arg1, std::string arg2, std::string arg3) |
| template <typename T \> <br>PlainPtr4 | **[plain](/documentation/code/classes/classdafunk_1_1funkbase/#function-plain)**(std::string arg1, std::string arg2, std::string arg3, std::string arg4) |
| Funk | **[set](/documentation/code/classes/classdafunk_1_1funkbase/#function-set)**() |

**Protected Attributes inherited from [daFunk::FunkBase](/documentation/code/classes/classdafunk_1_1funkbase/)**

|                | Name           |
| -------------- | -------------- |
| std::vector< Funk > | **[functions](/documentation/code/classes/classdafunk_1_1funkbase/#variable-functions)**  |
| ArgsType | **[arguments](/documentation/code/classes/classdafunk_1_1funkbase/#variable-arguments)**  |
| std::vector< std::vector< size_t > > | **[indices](/documentation/code/classes/classdafunk_1_1funkbase/#variable-indices)**  |
| size_t | **[datalen](/documentation/code/classes/classdafunk_1_1funkbase/#variable-datalen)**  |
| Singularities | **[singularities](/documentation/code/classes/classdafunk_1_1funkbase/#variable-singularities)**  |


## Public Functions Documentation

### function FunkPlain

```
inline FunkPlain(
    Funk fin,
    std::string arg1
)
```


### function FunkPlain

```
inline FunkPlain(
    Funk fin,
    std::string arg1,
    std::string arg2
)
```


### function FunkPlain

```
inline FunkPlain(
    Funk fin,
    std::string arg1,
    std::string arg2,
    std::string arg3
)
```


### function FunkPlain

```
inline FunkPlain(
    Funk fin,
    std::string arg1,
    std::string arg2,
    std::string arg3,
    std::string arg4
)
```


### function value

```
inline virtual double value(
    const std::vector< double > & args,
    size_t bindID
)
```


**Reimplements**: [daFunk::FunkBase::value](/documentation/code/classes/classdafunk_1_1funkbase/#function-value)


### function plain1p

```
static inline double plain1p(
    double x1,
    void * ptr
)
```


### function plain2p

```
static inline double plain2p(
    double x1,
    double x2,
    void * ptr
)
```


### function plain3p

```
static inline double plain3p(
    double x1,
    double x2,
    double x3,
    void * ptr
)
```


### function plain4p

```
static inline double plain4p(
    double x1,
    double x2,
    double x3,
    double x4,
    void * ptr
)
```


### function plain1

```
template <typename T >
static inline double plain1(
    double & x1
)
```


### function plain2

```
template <typename T >
static inline double plain2(
    double & x1,
    double & x2
)
```


### function plain3

```
template <typename T >
static inline double plain3(
    double & x1,
    double & x2,
    double & x3
)
```


### function plain4

```
template <typename T >
static inline double plain4(
    double & x1,
    double & x2,
    double & x3,
    double & x4
)
```


-------------------------------

Updated on 2022-09-08 at 02:27:28 +0000