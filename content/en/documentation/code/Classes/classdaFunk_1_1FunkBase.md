---
title: "class daFunk::FunkBase"

description: "[No description available]"

---

# class daFunk::FunkBase



[No description available]

Inherits from boost::enable_shared_from_this< FunkBase >

Inherited by [daFunk::Bottle](/documentation/code/classes/classdafunk_1_1bottle/), [daFunk::FunkConst](/documentation/code/classes/classdafunk_1_1funkconst/), [daFunk::FunkDelta](/documentation/code/classes/classdafunk_1_1funkdelta/), [daFunk::FunkDerived](/documentation/code/classes/classdafunk_1_1funkderived/), [daFunk::FunkFunc< threadsafe, funcargs >](/documentation/code/classes/classdafunk_1_1funkfunc/), [daFunk::FunkFuncM< threadsafe, O, funcargs >](/documentation/code/classes/classdafunk_1_1funkfuncm/), [daFunk::FunkIfElse](/documentation/code/classes/classdafunk_1_1funkifelse/), [daFunk::FunkIntegrate_gsl1d](/documentation/code/classes/classdafunk_1_1funkintegrate__gsl1d/), [daFunk::FunkInterp](/documentation/code/classes/classdafunk_1_1funkinterp/), [daFunk::FunkMath_umin](/documentation/code/classes/classdafunk_1_1funkmath__umin/), [daFunk::FunkPlain](/documentation/code/classes/classdafunk_1_1funkplain/), [daFunk::FunkVar](/documentation/code/classes/classdafunk_1_1funkvar/), [daFunk::ThrowError](/documentation/code/classes/classdafunk_1_1throwerror/)

## Public Functions

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
| virtual double | **[value](/documentation/code/classes/classdafunk_1_1funkbase/#function-value)**(const std::vector< double > & , size_t bindID) =0 |
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

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| std::vector< Funk > | **[functions](/documentation/code/classes/classdafunk_1_1funkbase/#variable-functions)**  |
| ArgsType | **[arguments](/documentation/code/classes/classdafunk_1_1funkbase/#variable-arguments)**  |
| std::vector< std::vector< size_t > > | **[indices](/documentation/code/classes/classdafunk_1_1funkbase/#variable-indices)**  |
| size_t | **[datalen](/documentation/code/classes/classdafunk_1_1funkbase/#variable-datalen)**  |
| Singularities | **[singularities](/documentation/code/classes/classdafunk_1_1funkbase/#variable-singularities)**  |

## Public Functions Documentation

### function FunkBase

```
inline FunkBase()
```


### function ~FunkBase

```
inline virtual ~FunkBase()
```


### function set

```
template <typename... Args>
inline Funk set(
    std::string arg,
    Funk g,
    Args... args
)
```


### function set

```
template <typename... Args>
inline Funk set(
    std::string arg,
    double x,
    Args... args
)
```


### function set

```
template <typename... Args>
inline Funk set(
    std::string arg,
    std::string arg1,
    Args... args
)
```


### function set

```
template <typename... Args>
Funk set()
```


### function bind

```
template <typename... Args>
inline shared_ptr< FunkBound > bind(
    Args... args
)
```


### function getArgs

```
inline const std::vector< std::string > & getArgs()
```


### function getNArgs

```
inline std::size_t getNArgs()
```


### function hasArg

```
inline bool hasArg(
    std::string arg
)
```


### function hasArgs

```
inline bool hasArgs()
```


### function help

```
inline Funk help()
```


### function assert_args

```
template <typename... Args>
inline bool assert_args(
    Args... args
)
```


### function value

```
virtual double value(
    const std::vector< double > & ,
    size_t bindID
) =0
```


**Reimplemented by**: [daFunk::FunkPlain::value](/documentation/code/classes/classdafunk_1_1funkplain/#function-value), [daFunk::FunkConst::value](/documentation/code/classes/classdafunk_1_1funkconst/#function-value), [daFunk::FunkDerived::value](/documentation/code/classes/classdafunk_1_1funkderived/#function-value), [daFunk::FunkFunc::value](/documentation/code/classes/classdafunk_1_1funkfunc/#function-value), [daFunk::FunkFuncM::value](/documentation/code/classes/classdafunk_1_1funkfuncm/#function-value), [daFunk::FunkDelta::value](/documentation/code/classes/classdafunk_1_1funkdelta/#function-value), [daFunk::FunkVar::value](/documentation/code/classes/classdafunk_1_1funkvar/#function-value), [daFunk::FunkMath_umin::value](/documentation/code/classes/classdafunk_1_1funkmath__umin/#function-value), [daFunk::FunkInterp::value](/documentation/code/classes/classdafunk_1_1funkinterp/#function-value), [daFunk::FunkIfElse::value](/documentation/code/classes/classdafunk_1_1funkifelse/#function-value), [daFunk::ThrowError::value](/documentation/code/classes/classdafunk_1_1throwerror/#function-value), [daFunk::Bottle::value](/documentation/code/classes/classdafunk_1_1bottle/#function-value), [daFunk::FunkIntegrate_gsl1d::value](/documentation/code/classes/classdafunk_1_1funkintegrate__gsl1d/#function-value)


### function resolve

```
inline virtual void resolve(
    std::map< std::string, size_t > datamap,
    size_t & datalen,
    size_t bindID,
    std::map< std::string, size_t > & argmap
)
```


**Reimplemented by**: [daFunk::FunkDerived::resolve](/documentation/code/classes/classdafunk_1_1funkderived/#function-resolve), [daFunk::FunkIntegrate_gsl1d::resolve](/documentation/code/classes/classdafunk_1_1funkintegrate__gsl1d/#function-resolve)


### function getSingl

```
inline Singularities getSingl()
```


### function set_singularity

```
inline Funk set_singularity(
    std::string arg,
    double pos,
    double width
)
```


### function print

```
inline Funk print(
    std::string arg
)
```


### function gsl_integration

```
template <typename... Args>
inline shared_ptr< FunkIntegrate_gsl1d > gsl_integration(
    Args... args
)
```


### function plain

```
inline PlainPtrs1 plain(
    std::string arg1
)
```


### function plain

```
inline PlainPtrs2 plain(
    std::string arg1,
    std::string arg2
)
```


### function plain

```
inline PlainPtrs3 plain(
    std::string arg1,
    std::string arg2,
    std::string arg3
)
```


### function plain

```
inline PlainPtrs4 plain(
    std::string arg1,
    std::string arg2,
    std::string arg3,
    std::string arg4
)
```


### function plain

```
template <typename T >
inline PlainPtr1 plain(
    std::string arg1
)
```


### function plain

```
template <typename T >
inline PlainPtr2 plain(
    std::string arg1,
    std::string arg2
)
```


### function plain

```
template <typename T >
inline PlainPtr3 plain(
    std::string arg1,
    std::string arg2,
    std::string arg3
)
```


### function plain

```
template <typename T >
inline PlainPtr4 plain(
    std::string arg1,
    std::string arg2,
    std::string arg3,
    std::string arg4
)
```


### function set

```
inline Funk set()
```


## Protected Attributes Documentation

### variable functions

```
std::vector< Funk > functions;
```


### variable arguments

```
ArgsType arguments;
```


### variable indices

```
std::vector< std::vector< size_t > > indices;
```


### variable datalen

```
size_t datalen;
```


### variable singularities

```
Singularities singularities;
```


-------------------------------

Updated on 2022-09-08 at 03:08:04 +0000