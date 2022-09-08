---
title: "class daFunk::FunkFunc"

description: "[No description available]"

---

# class daFunk::FunkFunc



[No description available] [More...](#detailed-description)

Inherits from [daFunk::FunkBase](/documentation/code/classes/classdafunk_1_1funkbase/), boost::enable_shared_from_this< FunkBase >

## Public Functions

|                | Name           |
| -------------- | -------------- |
| template <typename... Args\> <br>| **[FunkFunc](/documentation/code/classes/classdafunk_1_1funkfunc/#function-funkfunc)**(double(*)(funcargs...) f, Args... argss) |
| virtual double | **[value](/documentation/code/classes/classdafunk_1_1funkfunc/#function-value)**(const std::vector< double > & data, size_t bindID) |
| template <size_t... Args\> <br>double | **[ppp](/documentation/code/classes/classdafunk_1_1funkfunc/#function-ppp)**([index_list](/documentation/code/classes/structdafunk_1_1index__list/)< Args... > , std::tuple< typename std::remove_reference< funcargs >::type... > & my_input) |

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


## Detailed Description

```
template <bool threadsafe,
typename... funcargs>
class daFunk::FunkFunc;
```

## Public Functions Documentation

### function FunkFunc

```
template <typename... Args>
inline FunkFunc(
    double(*)(funcargs...) f,
    Args... argss
)
```


### function value

```
inline virtual double value(
    const std::vector< double > & data,
    size_t bindID
)
```


**Reimplements**: [daFunk::FunkBase::value](/documentation/code/classes/classdafunk_1_1funkbase/#function-value)


### function ppp

```
template <size_t... Args>
inline double ppp(
    index_list< Args... > ,
    std::tuple< typename std::remove_reference< funcargs >::type... > & my_input
)
```


-------------------------------

Updated on 2022-09-08 at 00:43:02 +0000