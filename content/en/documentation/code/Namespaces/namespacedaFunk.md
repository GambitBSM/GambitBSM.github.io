---
title: "namespace daFunk"

description: "[No description available]"

---

# namespace daFunk

[No description available]

## Namespaces

| Name           |
| -------------- |
| **[daFunk::detail](/documentation/code/namespaces/namespacedafunk_1_1detail/)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[daFunk::Bottle](/documentation/code/classes/classdafunk_1_1bottle/)**  |
| class | **[daFunk::FunkBase](/documentation/code/classes/classdafunk_1_1funkbase/)**  |
| class | **[daFunk::FunkBound](/documentation/code/classes/classdafunk_1_1funkbound/)**  |
| class | **[daFunk::FunkConst](/documentation/code/classes/classdafunk_1_1funkconst/)**  |
| class | **[daFunk::FunkDelta](/documentation/code/classes/classdafunk_1_1funkdelta/)**  |
| class | **[daFunk::FunkDerived](/documentation/code/classes/classdafunk_1_1funkderived/)**  |
| class | **[daFunk::FunkFunc](/documentation/code/classes/classdafunk_1_1funkfunc/)**  |
| class | **[daFunk::FunkFuncM](/documentation/code/classes/classdafunk_1_1funkfuncm/)**  |
| class | **[daFunk::FunkIfElse](/documentation/code/classes/classdafunk_1_1funkifelse/)**  |
| class | **[daFunk::FunkIntegrate_gsl1d](/documentation/code/classes/classdafunk_1_1funkintegrate__gsl1d/)**  |
| class | **[daFunk::FunkInterp](/documentation/code/classes/classdafunk_1_1funkinterp/)**  |
| class | **[daFunk::FunkMath_umin](/documentation/code/classes/classdafunk_1_1funkmath__umin/)**  |
| class | **[daFunk::FunkPlain](/documentation/code/classes/classdafunk_1_1funkplain/)**  |
| class | **[daFunk::FunkVar](/documentation/code/classes/classdafunk_1_1funkvar/)**  |
| struct | **[daFunk::index_list](/documentation/code/classes/structdafunk_1_1index__list/)**  |
| class | **[daFunk::livingVector](/documentation/code/classes/classdafunk_1_1livingvector/)**  |
| class | **[daFunk::ThrowError](/documentation/code/classes/classdafunk_1_1throwerror/)**  |

## Types

|                | Name           |
| -------------- | -------------- |
| typedef shared_ptr< [FunkBase](/documentation/code/classes/classdafunk_1_1funkbase/) > | **[Funk](/documentation/code/namespaces/namespacedafunk/#typedef-funk)**  |
| typedef shared_ptr< [FunkBound](/documentation/code/classes/classdafunk_1_1funkbound/) > | **[BoundFunk](/documentation/code/namespaces/namespacedafunk/#typedef-boundfunk)**  |
| typedef std::vector< std::string > | **[ArgsType](/documentation/code/namespaces/namespacedafunk/#typedef-argstype)**  |
| typedef std::map< std::string, std::vector< std::pair< Funk, Funk > > > | **[Singularities](/documentation/code/namespaces/namespacedafunk/#typedef-singularities)**  |
| typedef double(*)(double &) | **[PlainPtr1](/documentation/code/namespaces/namespacedafunk/#typedef-plainptr1)**  |
| typedef double(*)(double &, double &) | **[PlainPtr2](/documentation/code/namespaces/namespacedafunk/#typedef-plainptr2)**  |
| typedef double(*)(double &, double &, double &) | **[PlainPtr3](/documentation/code/namespaces/namespacedafunk/#typedef-plainptr3)**  |
| typedef double(*)(double &, double &, double &, double &) | **[PlainPtr4](/documentation/code/namespaces/namespacedafunk/#typedef-plainptr4)**  |
| typedef std::pair< double(*)(double, void *), void * > | **[PlainPtrs1](/documentation/code/namespaces/namespacedafunk/#typedef-plainptrs1)**  |
| typedef std::pair< double(*)(double, double, void *), void * > | **[PlainPtrs2](/documentation/code/namespaces/namespacedafunk/#typedef-plainptrs2)**  |
| typedef std::pair< double(*)(double, double, double, void *), void * > | **[PlainPtrs3](/documentation/code/namespaces/namespacedafunk/#typedef-plainptrs3)**  |
| typedef std::pair< double(*)(double, double, double, double, void *), void * > | **[PlainPtrs4](/documentation/code/namespaces/namespacedafunk/#typedef-plainptrs4)**  |

## Functions

|                | Name           |
| -------------- | -------------- |
| template <typename T \> <br>std::vector< T > | **[vec](/documentation/code/namespaces/namespacedafunk/#function-vec)**(std::vector< T > vector) |
| template <typename T ,typename... Args\> <br>std::vector< T > | **[vec](/documentation/code/namespaces/namespacedafunk/#function-vec)**(std::vector< T > vector, T value, Args... args) |
| template <typename T ,typename... Args\> <br>std::vector< T > | **[vec](/documentation/code/namespaces/namespacedafunk/#function-vec)**(T value, Args... args) |
| template <typename T \> <br>std::vector< T > | **[vec](/documentation/code/namespaces/namespacedafunk/#function-vec)**() |
| std::vector< double > | **[linspace](/documentation/code/namespaces/namespacedafunk/#function-linspace)**(double x0, double x1, unsigned int n) |
| std::vector< double > | **[logspace](/documentation/code/namespaces/namespacedafunk/#function-logspace)**(double x0, double x1, unsigned int n) |
| bool | **[args_match](/documentation/code/namespaces/namespacedafunk/#function-args-match)**(ArgsType args1, ArgsType args2) |
| std::string | **[args_string](/documentation/code/namespaces/namespacedafunk/#function-args-string)**(ArgsType args) |
| ArgsType | **[joinArgs](/documentation/code/namespaces/namespacedafunk/#function-joinargs)**(ArgsType args1, ArgsType args2) |
| ArgsType | **[eraseArg](/documentation/code/namespaces/namespacedafunk/#function-erasearg)**(ArgsType args, std::string arg) |
| Singularities | **[joinSingl](/documentation/code/namespaces/namespacedafunk/#function-joinsingl)**(Singularities s1, Singularities s2) |
| template <typename... Args\> <br>Funk | **[one](/documentation/code/namespaces/namespacedafunk/#function-one)**(Args... argss) |
| template <typename... Args\> <br>Funk | **[zero](/documentation/code/namespaces/namespacedafunk/#function-zero)**(Args... argss) |
| template <typename... Args\> <br>Funk | **[cnst](/documentation/code/namespaces/namespacedafunk/#function-cnst)**(double x, Args... argss) |
| template <typename... funcargs,typename... Args\> <br>Funk | **[func](/documentation/code/namespaces/namespacedafunk/#function-func)**(double(*)(funcargs...) f, Args... args) |
| template <typename... funcargs,typename... Args\> <br>Funk | **[func_fromThreadsafe](/documentation/code/namespaces/namespacedafunk/#function-func-fromthreadsafe)**(double(*)(funcargs...) f, Args... args) |
| template <typename O ,typename... funcargs,typename... Args\> <br>Funk | **[funcM](/documentation/code/namespaces/namespacedafunk/#function-funcm)**(O * obj, double(O::*)(funcargs...) f, Args... args) |
| template <typename O ,typename... funcargs,typename... Args\> <br>Funk | **[funcM](/documentation/code/namespaces/namespacedafunk/#function-funcm)**(shared_ptr< O > obj, double(O::*)(funcargs...) f, Args... args) |
| template <typename O ,typename... funcargs,typename... Args\> <br>Funk | **[funcM_fromThreadsafe](/documentation/code/namespaces/namespacedafunk/#function-funcm-fromthreadsafe)**(O * obj, double(O::*)(funcargs...) f, Args... args) |
| template <typename O ,typename... funcargs,typename... Args\> <br>Funk | **[funcM_fromThreadsafe](/documentation/code/namespaces/namespacedafunk/#function-funcm-fromthreadsafe)**(shared_ptr< O > obj, double(O::*)(funcargs...) f, Args... args) |
| Funk | **[delta](/documentation/code/namespaces/namespacedafunk/#function-delta)**(std::string arg, double pos, double width) |
| Funk | **[var](/documentation/code/namespaces/namespacedafunk/#function-var)**(std::string arg) |
| Funk | **[operator-](/documentation/code/namespaces/namespacedafunk/#function-operator)**(Funk f) |
| template <typename T \> <br>shared_ptr< [FunkInterp](/documentation/code/classes/classdafunk_1_1funkinterp/) > | **[interp](/documentation/code/namespaces/namespacedafunk/#function-interp)**(T f, std::vector< double > x, std::vector< double > y) |
| Funk | **[ifelse](/documentation/code/namespaces/namespacedafunk/#function-ifelse)**(Funk f, Funk g, Funk h) |
| Funk | **[ifelse](/documentation/code/namespaces/namespacedafunk/#function-ifelse)**(Funk f, double g, Funk h) |
| Funk | **[ifelse](/documentation/code/namespaces/namespacedafunk/#function-ifelse)**(Funk f, double g, double h) |
| Funk | **[ifelse](/documentation/code/namespaces/namespacedafunk/#function-ifelse)**(Funk f, Funk g, double h) |
| Funk | **[throwError](/documentation/code/namespaces/namespacedafunk/#function-throwerror)**(std::string msg) |
| template <typename T1 ,typename T2 \> <br>shared_ptr< [FunkIntegrate_gsl1d](/documentation/code/classes/classdafunk_1_1funkintegrate__gsl1d/) > | **[getIntegrate_gsl1d](/documentation/code/namespaces/namespacedafunk/#function-getintegrate-gsl1d)**(Funk fptr, std::string arg, T1 x1, T2 x2) |
| std::vector< double > | **[augmentSingl](/documentation/code/namespaces/namespacedafunk/#function-augmentsingl)**(const std::vector< double > & xgrid, Funk f, int N =100, double sigma =3) |

## Types Documentation

### typedef Funk

```
typedef shared_ptr<FunkBase> daFunk::Funk;
```


### typedef BoundFunk

```
typedef shared_ptr<FunkBound> daFunk::BoundFunk;
```


### typedef ArgsType

```
typedef std::vector<std::string> daFunk::ArgsType;
```


### typedef Singularities

```
typedef std::map<std::string, std::vector<std::pair<Funk, Funk> > > daFunk::Singularities;
```


### typedef PlainPtr1

```
typedef double(* daFunk::PlainPtr1) (double &);
```


### typedef PlainPtr2

```
typedef double(* daFunk::PlainPtr2) (double &, double &);
```


### typedef PlainPtr3

```
typedef double(* daFunk::PlainPtr3) (double &, double &, double &);
```


### typedef PlainPtr4

```
typedef double(* daFunk::PlainPtr4) (double &, double &, double &, double &);
```


### typedef PlainPtrs1

```
typedef std::pair<double(*)(double,void*), void*> daFunk::PlainPtrs1;
```


### typedef PlainPtrs2

```
typedef std::pair<double(*)(double,double,void*), void*> daFunk::PlainPtrs2;
```


### typedef PlainPtrs3

```
typedef std::pair<double(*)(double,double,double,void*), void*> daFunk::PlainPtrs3;
```


### typedef PlainPtrs4

```
typedef std::pair<double(*)(double,double,double,double,void*), void*> daFunk::PlainPtrs4;
```



## Functions Documentation

### function vec

```
template <typename T >
inline std::vector< T > vec(
    std::vector< T > vector
)
```


### function vec

```
template <typename T ,
typename... Args>
inline std::vector< T > vec(
    std::vector< T > vector,
    T value,
    Args... args
)
```


### function vec

```
template <typename T ,
typename... Args>
inline std::vector< T > vec(
    T value,
    Args... args
)
```


### function vec

```
template <typename T >
inline std::vector< T > vec()
```


### function linspace

```
inline std::vector< double > linspace(
    double x0,
    double x1,
    unsigned int n
)
```


### function logspace

```
inline std::vector< double > logspace(
    double x0,
    double x1,
    unsigned int n
)
```


### function args_match

```
inline bool args_match(
    ArgsType args1,
    ArgsType args2
)
```


### function args_string

```
inline std::string args_string(
    ArgsType args
)
```


### function joinArgs

```
inline ArgsType joinArgs(
    ArgsType args1,
    ArgsType args2
)
```


### function eraseArg

```
inline ArgsType eraseArg(
    ArgsType args,
    std::string arg
)
```


### function joinSingl

```
inline Singularities joinSingl(
    Singularities s1,
    Singularities s2
)
```


### function one

```
template <typename... Args>
inline Funk one(
    Args... argss
)
```


### function zero

```
template <typename... Args>
inline Funk zero(
    Args... argss
)
```


### function cnst

```
template <typename... Args>
inline Funk cnst(
    double x,
    Args... argss
)
```


### function func

```
template <typename... funcargs,
typename... Args>
Funk func(
    double(*)(funcargs...) f,
    Args... args
)
```


### function func_fromThreadsafe

```
template <typename... funcargs,
typename... Args>
Funk func_fromThreadsafe(
    double(*)(funcargs...) f,
    Args... args
)
```


### function funcM

```
template <typename O ,
typename... funcargs,
typename... Args>
Funk funcM(
    O * obj,
    double(O::*)(funcargs...) f,
    Args... args
)
```


### function funcM

```
template <typename O ,
typename... funcargs,
typename... Args>
Funk funcM(
    shared_ptr< O > obj,
    double(O::*)(funcargs...) f,
    Args... args
)
```


### function funcM_fromThreadsafe

```
template <typename O ,
typename... funcargs,
typename... Args>
Funk funcM_fromThreadsafe(
    O * obj,
    double(O::*)(funcargs...) f,
    Args... args
)
```


### function funcM_fromThreadsafe

```
template <typename O ,
typename... funcargs,
typename... Args>
Funk funcM_fromThreadsafe(
    shared_ptr< O > obj,
    double(O::*)(funcargs...) f,
    Args... args
)
```


### function delta

```
inline Funk delta(
    std::string arg,
    double pos,
    double width
)
```


### function var

```
inline Funk var(
    std::string arg
)
```


### function operator-

```
inline Funk operator-(
    Funk f
)
```


### function interp

```
template <typename T >
inline shared_ptr< FunkInterp > interp(
    T f,
    std::vector< double > x,
    std::vector< double > y
)
```


### function ifelse

```
inline Funk ifelse(
    Funk f,
    Funk g,
    Funk h
)
```


### function ifelse

```
inline Funk ifelse(
    Funk f,
    double g,
    Funk h
)
```


### function ifelse

```
inline Funk ifelse(
    Funk f,
    double g,
    double h
)
```


### function ifelse

```
inline Funk ifelse(
    Funk f,
    Funk g,
    double h
)
```


### function throwError

```
inline Funk throwError(
    std::string msg
)
```


### function getIntegrate_gsl1d

```
template <typename T1 ,
typename T2 >
inline shared_ptr< FunkIntegrate_gsl1d > getIntegrate_gsl1d(
    Funk fptr,
    std::string arg,
    T1 x1,
    T2 x2
)
```


### function augmentSingl

```
inline std::vector< double > augmentSingl(
    const std::vector< double > & xgrid,
    Funk f,
    int N =100,
    double sigma =3
)
```






-------------------------------

Updated on 2023-06-26 at 21:36:53 +0000