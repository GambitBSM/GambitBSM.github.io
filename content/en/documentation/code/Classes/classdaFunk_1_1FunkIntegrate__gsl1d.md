---
title: "class daFunk::FunkIntegrate_gsl1d"

description: "[No description available]"

---

# class daFunk::FunkIntegrate_gsl1d



[No description available]

Inherits from [daFunk::FunkBase](/documentation/code/classes/classdafunk_1_1funkbase/), gsl_function

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[FunkIntegrate_gsl1d](/documentation/code/classes/classdafunk_1_1funkintegrate__gsl1d/#function-funkintegrate-gsl1d)**(Funk f0, std::string arg, Funk f1, Funk f2) |
| | **[FunkIntegrate_gsl1d](/documentation/code/classes/classdafunk_1_1funkintegrate__gsl1d/#function-funkintegrate-gsl1d)**(Funk f0, std::string arg, double x, Funk f) |
| | **[FunkIntegrate_gsl1d](/documentation/code/classes/classdafunk_1_1funkintegrate__gsl1d/#function-funkintegrate-gsl1d)**(Funk f0, std::string arg, double x, double y) |
| | **[FunkIntegrate_gsl1d](/documentation/code/classes/classdafunk_1_1funkintegrate__gsl1d/#function-funkintegrate-gsl1d)**(Funk f0, std::string arg, Funk f, double x) |
| | **[FunkIntegrate_gsl1d](/documentation/code/classes/classdafunk_1_1funkintegrate__gsl1d/#function-funkintegrate-gsl1d)**(Funk f0, std::string arg, std::string x, Funk f) |
| | **[FunkIntegrate_gsl1d](/documentation/code/classes/classdafunk_1_1funkintegrate__gsl1d/#function-funkintegrate-gsl1d)**(Funk f0, std::string arg, std::string x, std::string y) |
| | **[FunkIntegrate_gsl1d](/documentation/code/classes/classdafunk_1_1funkintegrate__gsl1d/#function-funkintegrate-gsl1d)**(Funk f0, std::string arg, Funk f, std::string x) |
| | **[FunkIntegrate_gsl1d](/documentation/code/classes/classdafunk_1_1funkintegrate__gsl1d/#function-funkintegrate-gsl1d)**(Funk f0, std::string arg, std::string x, double y) |
| | **[FunkIntegrate_gsl1d](/documentation/code/classes/classdafunk_1_1funkintegrate__gsl1d/#function-funkintegrate-gsl1d)**(Funk f0, std::string arg, double y, std::string x) |
| virtual void | **[resolve](/documentation/code/classes/classdafunk_1_1funkintegrate__gsl1d/#function-resolve)**(std::map< std::string, size_t > datamap, size_t & datalen, size_t bindID, std::map< std::string, size_t > & argmap) |
| | **[~FunkIntegrate_gsl1d](/documentation/code/classes/classdafunk_1_1funkintegrate__gsl1d/#function-funkintegrate-gsl1d)**() |
| shared_ptr< [FunkIntegrate_gsl1d](/documentation/code/classes/classdafunk_1_1funkintegrate__gsl1d/) > | **[set_epsrel](/documentation/code/classes/classdafunk_1_1funkintegrate__gsl1d/#function-set-epsrel)**(double epsrel) |
| shared_ptr< [FunkIntegrate_gsl1d](/documentation/code/classes/classdafunk_1_1funkintegrate__gsl1d/) > | **[set_epsabs](/documentation/code/classes/classdafunk_1_1funkintegrate__gsl1d/#function-set-epsabs)**(double epsabs) |
| shared_ptr< [FunkIntegrate_gsl1d](/documentation/code/classes/classdafunk_1_1funkintegrate__gsl1d/) > | **[set_limit](/documentation/code/classes/classdafunk_1_1funkintegrate__gsl1d/#function-set-limit)**(size_t limit) |
| shared_ptr< [FunkIntegrate_gsl1d](/documentation/code/classes/classdafunk_1_1funkintegrate__gsl1d/) > | **[set_singularity_factor](/documentation/code/classes/classdafunk_1_1funkintegrate__gsl1d/#function-set-singularity-factor)**(double f) |
| shared_ptr< [FunkIntegrate_gsl1d](/documentation/code/classes/classdafunk_1_1funkintegrate__gsl1d/) > | **[set_use_log_fallback](/documentation/code/classes/classdafunk_1_1funkintegrate__gsl1d/#function-set-use-log-fallback)**(bool flag) |
| virtual double | **[value](/documentation/code/classes/classdafunk_1_1funkintegrate__gsl1d/#function-value)**(const std::vector< double > & data, size_t bindID) |

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

### function FunkIntegrate_gsl1d

```
inline FunkIntegrate_gsl1d(
    Funk f0,
    std::string arg,
    Funk f1,
    Funk f2
)
```


### function FunkIntegrate_gsl1d

```
inline FunkIntegrate_gsl1d(
    Funk f0,
    std::string arg,
    double x,
    Funk f
)
```


### function FunkIntegrate_gsl1d

```
inline FunkIntegrate_gsl1d(
    Funk f0,
    std::string arg,
    double x,
    double y
)
```


### function FunkIntegrate_gsl1d

```
inline FunkIntegrate_gsl1d(
    Funk f0,
    std::string arg,
    Funk f,
    double x
)
```


### function FunkIntegrate_gsl1d

```
inline FunkIntegrate_gsl1d(
    Funk f0,
    std::string arg,
    std::string x,
    Funk f
)
```


### function FunkIntegrate_gsl1d

```
inline FunkIntegrate_gsl1d(
    Funk f0,
    std::string arg,
    std::string x,
    std::string y
)
```


### function FunkIntegrate_gsl1d

```
inline FunkIntegrate_gsl1d(
    Funk f0,
    std::string arg,
    Funk f,
    std::string x
)
```


### function FunkIntegrate_gsl1d

```
inline FunkIntegrate_gsl1d(
    Funk f0,
    std::string arg,
    std::string x,
    double y
)
```


### function FunkIntegrate_gsl1d

```
inline FunkIntegrate_gsl1d(
    Funk f0,
    std::string arg,
    double y,
    std::string x
)
```


### function resolve

```
inline virtual void resolve(
    std::map< std::string, size_t > datamap,
    size_t & datalen,
    size_t bindID,
    std::map< std::string, size_t > & argmap
)
```


**Reimplements**: [daFunk::FunkBase::resolve](/documentation/code/classes/classdafunk_1_1funkbase/#function-resolve)


### function ~FunkIntegrate_gsl1d

```
inline ~FunkIntegrate_gsl1d()
```


### function set_epsrel

```
inline shared_ptr< FunkIntegrate_gsl1d > set_epsrel(
    double epsrel
)
```


### function set_epsabs

```
inline shared_ptr< FunkIntegrate_gsl1d > set_epsabs(
    double epsabs
)
```


### function set_limit

```
inline shared_ptr< FunkIntegrate_gsl1d > set_limit(
    size_t limit
)
```


### function set_singularity_factor

```
inline shared_ptr< FunkIntegrate_gsl1d > set_singularity_factor(
    double f
)
```


### function set_use_log_fallback

```
inline shared_ptr< FunkIntegrate_gsl1d > set_use_log_fallback(
    bool flag
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


-------------------------------

Updated on 2024-05-31 at 15:12:05 +0000