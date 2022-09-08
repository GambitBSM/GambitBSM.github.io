---
title: "class daFunk::FunkVar"

description: "[No description available]"

---

# class daFunk::FunkVar



[No description available]

Inherits from [daFunk::FunkBase](/documentation/code/classes/classdafunk_1_1funkbase/), boost::enable_shared_from_this< FunkBase >

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[FunkVar](/documentation/code/classes/classdafunk_1_1funkvar/)**(std::string arg) |
| virtual double | **[value](/documentation/code/classes/classdafunk_1_1funkvar/)**(const std::vector< double > & data, size_t bindID) |

## Additional inherited members

**Public Functions inherited from [daFunk::FunkBase](/documentation/code/classes/classdafunk_1_1funkbase/)**

|                | Name           |
| -------------- | -------------- |
| | **[FunkBase](/documentation/code/classes/classdafunk_1_1funkbase/)**() |
| virtual | **[~FunkBase](/documentation/code/classes/classdafunk_1_1funkbase/)**() |
| template <typename... Args\> <br>Funk | **[set](/documentation/code/classes/classdafunk_1_1funkbase/)**(std::string arg, Funk g, Args... args) |
| template <typename... Args\> <br>Funk | **[set](/documentation/code/classes/classdafunk_1_1funkbase/)**(std::string arg, double x, Args... args) |
| template <typename... Args\> <br>Funk | **[set](/documentation/code/classes/classdafunk_1_1funkbase/)**(std::string arg, std::string arg1, Args... args) |
| template <typename... Args\> <br>Funk | **[set](/documentation/code/classes/classdafunk_1_1funkbase/)**() |
| template <typename... Args\> <br>shared_ptr< [FunkBound](/documentation/code/classes/classdafunk_1_1funkbound/) > | **[bind](/documentation/code/classes/classdafunk_1_1funkbase/)**(Args... args) |
| const std::vector< std::string > & | **[getArgs](/documentation/code/classes/classdafunk_1_1funkbase/)**() |
| std::size_t | **[getNArgs](/documentation/code/classes/classdafunk_1_1funkbase/)**() |
| bool | **[hasArg](/documentation/code/classes/classdafunk_1_1funkbase/)**(std::string arg) |
| bool | **[hasArgs](/documentation/code/classes/classdafunk_1_1funkbase/)**() |
| Funk | **[help](/documentation/code/classes/classdafunk_1_1funkbase/)**() |
| template <typename... Args\> <br>bool | **[assert_args](/documentation/code/classes/classdafunk_1_1funkbase/)**(Args... args) |
| virtual void | **[resolve](/documentation/code/classes/classdafunk_1_1funkbase/)**(std::map< std::string, size_t > datamap, size_t & datalen, size_t bindID, std::map< std::string, size_t > & argmap) |
| Singularities | **[getSingl](/documentation/code/classes/classdafunk_1_1funkbase/)**() |
| Funk | **[set_singularity](/documentation/code/classes/classdafunk_1_1funkbase/)**(std::string arg, double pos, double width) |
| Funk | **[print](/documentation/code/classes/classdafunk_1_1funkbase/)**(std::string arg) |
| template <typename... Args\> <br>shared_ptr< [FunkIntegrate_gsl1d](/documentation/code/classes/classdafunk_1_1funkintegrate__gsl1d/) > | **[gsl_integration](/documentation/code/classes/classdafunk_1_1funkbase/)**(Args... args) |
| PlainPtrs1 | **[plain](/documentation/code/classes/classdafunk_1_1funkbase/)**(std::string arg1) |
| PlainPtrs2 | **[plain](/documentation/code/classes/classdafunk_1_1funkbase/)**(std::string arg1, std::string arg2) |
| PlainPtrs3 | **[plain](/documentation/code/classes/classdafunk_1_1funkbase/)**(std::string arg1, std::string arg2, std::string arg3) |
| PlainPtrs4 | **[plain](/documentation/code/classes/classdafunk_1_1funkbase/)**(std::string arg1, std::string arg2, std::string arg3, std::string arg4) |
| template <typename T \> <br>PlainPtr1 | **[plain](/documentation/code/classes/classdafunk_1_1funkbase/)**(std::string arg1) |
| template <typename T \> <br>PlainPtr2 | **[plain](/documentation/code/classes/classdafunk_1_1funkbase/)**(std::string arg1, std::string arg2) |
| template <typename T \> <br>PlainPtr3 | **[plain](/documentation/code/classes/classdafunk_1_1funkbase/)**(std::string arg1, std::string arg2, std::string arg3) |
| template <typename T \> <br>PlainPtr4 | **[plain](/documentation/code/classes/classdafunk_1_1funkbase/)**(std::string arg1, std::string arg2, std::string arg3, std::string arg4) |
| Funk | **[set](/documentation/code/classes/classdafunk_1_1funkbase/)**() |

**Protected Attributes inherited from [daFunk::FunkBase](/documentation/code/classes/classdafunk_1_1funkbase/)**

|                | Name           |
| -------------- | -------------- |
| std::vector< Funk > | **[functions](/documentation/code/classes/classdafunk_1_1funkbase/)**  |
| ArgsType | **[arguments](/documentation/code/classes/classdafunk_1_1funkbase/)**  |
| std::vector< std::vector< size_t > > | **[indices](/documentation/code/classes/classdafunk_1_1funkbase/)**  |
| size_t | **[datalen](/documentation/code/classes/classdafunk_1_1funkbase/)**  |
| Singularities | **[singularities](/documentation/code/classes/classdafunk_1_1funkbase/)**  |


## Public Functions Documentation

### function FunkVar

```
inline FunkVar(
    std::string arg
)
```


### function value

```
inline virtual double value(
    const std::vector< double > & data,
    size_t bindID
)
```


**Reimplements**: [daFunk::FunkBase::value](/documentation/code/classes/classdafunk_1_1funkbase/)


-------------------------------

Updated on 2022-09-08 at 01:05:18 +0000