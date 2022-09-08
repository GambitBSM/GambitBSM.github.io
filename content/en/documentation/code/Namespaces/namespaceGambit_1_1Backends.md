---
title: "namespace Gambit::Backends"

description: "[No description available]"

---

# namespace Gambit::Backends

[No description available]

## Namespaces

| Name           |
| -------------- |
| **[Gambit::Backends::AlterBBN_2_2](/documentation/code/namespaces/namespacegambit_1_1backends_1_1alterbbn__2__2/)**  |
| **[Gambit::Backends::gm2calc_1_2_0](/documentation/code/namespaces/namespacegambit_1_1backends_1_1gm2calc__1__2__0/)**  |
| **[Gambit::Backends::gm2calc_1_3_0](/documentation/code/namespaces/namespacegambit_1_1backends_1_1gm2calc__1__3__0/)**  |
| **[Gambit::Backends::HepLike_1_2](/documentation/code/namespaces/namespacegambit_1_1backends_1_1heplike__1__2/)**  |
| **[Gambit::Backends::Pythia_8_212](/documentation/code/namespaces/namespacegambit_1_1backends_1_1pythia__8__212/)**  |
| **[Gambit::Backends::vevacious_1_0](/documentation/code/namespaces/namespacegambit_1_1backends_1_1vevacious__1__0/)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| struct | **[Gambit::Backends::backend_info](/documentation/code/classes/structgambit_1_1backends_1_1backend__info/)** <br>Structure providing some basic info on backend libraries.  |
| class | **[Gambit::Backends::instance_helper](/documentation/code/classes/classgambit_1_1backends_1_1instance__helper/)**  |
| class | **[Gambit::Backends::instance_helper< void >](/documentation/code/classes/classgambit_1_1backends_1_1instance__helper_3_01void_01_4/)**  |
| class | **[Gambit::Backends::mathematica_function](/documentation/code/classes/classgambit_1_1backends_1_1mathematica__function/)** <br>Holds the info about a Mathematica backend function, and defines conversion functions.  |
| class | **[Gambit::Backends::python_function](/documentation/code/classes/classgambit_1_1backends_1_1python__function/)** <br>Holds the info about a python backend function, and defines conversion functions.  |
| union | **[Gambit::Backends::void_voidFptr](/documentation/code/classes/uniongambit_1_1backends_1_1void__voidfptr/)**  |

## Types

|                | Name           |
| -------------- | -------------- |
| typedef void(*)() | **[voidFptr](/documentation/code/namespaces/namespacegambit_1_1backends/)** <br>Simplify pointers to void functions.  |

## Functions

|                | Name           |
| -------------- | -------------- |
| int | **[WSGetVariable](/documentation/code/namespaces/namespacegambit_1_1backends/)**(WSLINK WSlink, int * val) |
| int | **[WSGetVariable](/documentation/code/namespaces/namespacegambit_1_1backends/)**(WSLINK WSlink, float * val) |
| int | **[WSGetVariable](/documentation/code/namespaces/namespacegambit_1_1backends/)**(WSLINK WSlink, double * val) |
| int | **[WSGetVariable](/documentation/code/namespaces/namespacegambit_1_1backends/)**(WSLINK WSlink, bool * val) |
| int | **[WSGetVariable](/documentation/code/namespaces/namespacegambit_1_1backends/)**(WSLINK WSlink, char * val) |
| int | **[WSGetVariable](/documentation/code/namespaces/namespacegambit_1_1backends/)**(WSLINK WSlink, [str](/documentation/code/namespaces/namespacegambit/) * val) |
| template <typename T \> <br>int | **[WSGetVariable](/documentation/code/namespaces/namespacegambit_1_1backends/)**(WSLINK WSlink, std::vector< T > * val) |
| int | **[WSPutVariable](/documentation/code/namespaces/namespacegambit_1_1backends/)**(WSLINK WSlink, int val) |
| int | **[WSPutVariable](/documentation/code/namespaces/namespacegambit_1_1backends/)**(WSLINK WSlink, float val) |
| int | **[WSPutVariable](/documentation/code/namespaces/namespacegambit_1_1backends/)**(WSLINK WSlink, double val) |
| int | **[WSPutVariable](/documentation/code/namespaces/namespacegambit_1_1backends/)**(WSLINK WSlink, bool val) |
| int | **[WSPutVariable](/documentation/code/namespaces/namespacegambit_1_1backends/)**(WSLINK WSlink, char val) |
| int | **[WSPutVariable](/documentation/code/namespaces/namespacegambit_1_1backends/)**(WSLINK WSlink, [str](/documentation/code/namespaces/namespacegambit/) val) |
| template <typename T \> <br>int | **[WSPutVariable](/documentation/code/namespaces/namespacegambit_1_1backends/)**(WSLINK WSlink, std::vector< T > val) |
| int | **[WSPutVariables](/documentation/code/namespaces/namespacegambit_1_1backends/)**(WSLINK ) |
| template <typename T \> <br>int | **[WSPutVariables](/documentation/code/namespaces/namespacegambit_1_1backends/)**(WSLINK WSlink, T last) |
| template <typename T1 ,typename T2 ,typename... Others\> <br>int | **[WSPutVariables](/documentation/code/namespaces/namespacegambit_1_1backends/)**(WSLINK WSlink, T1 first, T2 second, Others... args) |
| [backend_info](/documentation/code/classes/structgambit_1_1backends_1_1backend__info/) & | **[backendInfo](/documentation/code/namespaces/namespacegambit_1_1backends/)**()<br>Backend info accessor function.  |
| namespace | **[CAT_3](/documentation/code/namespaces/namespacegambit_1_1backends/)**(BACKENDNAME , _ , SAFE_VERSION ) |
| template <typename T \> <br>T | **[load_backend_symbol](/documentation/code/namespaces/namespacegambit_1_1backends/)**(const std::vector< [str](/documentation/code/namespaces/namespacegambit/) > & symbol_names, [str](/documentation/code/namespaces/namespacegambit/) be, [str](/documentation/code/namespaces/namespacegambit/) ver)<br>Get the pointer to the backend function.  |
| template <typename T \> <br>T | **[handover_factory_pointer](/documentation/code/namespaces/namespacegambit_1_1backends/)**([str](/documentation/code/namespaces/namespacegambit/) be, [str](/documentation/code/namespaces/namespacegambit/) ver, [str](/documentation/code/namespaces/namespacegambit/) name, [str](/documentation/code/namespaces/namespacegambit/) barename, [str](/documentation/code/namespaces/namespacegambit/) args, const std::vector< [str](/documentation/code/namespaces/namespacegambit/) > & symbol_names, T factory, T missing_backend, T missing_factory)<br>Provide the factory pointer to a BOSSed type's wrapper constructor.  |
| void | **[math_error](/documentation/code/namespaces/namespacegambit_1_1backends/)**(WSLINK , const [str](/documentation/code/namespaces/namespacegambit/) & , const [str](/documentation/code/namespaces/namespacegambit/) & )<br>Helper function to raise an appropriate warning or error in case of problems.  |
| template <typename T \> <br>bool | **[is_numeric](/documentation/code/namespaces/namespacegambit_1_1backends/)**()<br>Helper function that indicates if a type is numerical or not.  |

## Types Documentation

### typedef voidFptr

```
typedef void(* Gambit::Backends::voidFptr) ();
```

Simplify pointers to void functions. 


## Functions Documentation

### function WSGetVariable

```
int WSGetVariable(
    WSLINK WSlink,
    int * val
)
```


Overloaded functions to get data through WSTP 


### function WSGetVariable

```
int WSGetVariable(
    WSLINK WSlink,
    float * val
)
```


### function WSGetVariable

```
int WSGetVariable(
    WSLINK WSlink,
    double * val
)
```


### function WSGetVariable

```
int WSGetVariable(
    WSLINK WSlink,
    bool * val
)
```


### function WSGetVariable

```
int WSGetVariable(
    WSLINK WSlink,
    char * val
)
```


### function WSGetVariable

```
int WSGetVariable(
    WSLINK WSlink,
    str * val
)
```


### function WSGetVariable

```
template <typename T >
int WSGetVariable(
    WSLINK WSlink,
    std::vector< T > * val
)
```


### function WSPutVariable

```
int WSPutVariable(
    WSLINK WSlink,
    int val
)
```


Overloaded functions to put data through WSTP 


### function WSPutVariable

```
int WSPutVariable(
    WSLINK WSlink,
    float val
)
```


### function WSPutVariable

```
int WSPutVariable(
    WSLINK WSlink,
    double val
)
```


### function WSPutVariable

```
int WSPutVariable(
    WSLINK WSlink,
    bool val
)
```


### function WSPutVariable

```
int WSPutVariable(
    WSLINK WSlink,
    char val
)
```


### function WSPutVariable

```
int WSPutVariable(
    WSLINK WSlink,
    str val
)
```


### function WSPutVariable

```
template <typename T >
int WSPutVariable(
    WSLINK WSlink,
    std::vector< T > val
)
```


### function WSPutVariables

```
int WSPutVariables(
    WSLINK 
)
```


### function WSPutVariables

```
template <typename T >
int WSPutVariables(
    WSLINK WSlink,
    T last
)
```


### function WSPutVariables

```
template <typename T1 ,
typename T2 ,
typename... Others>
int WSPutVariables(
    WSLINK WSlink,
    T1 first,
    T2 second,
    Others... args
)
```


### function backendInfo

```
backend_info & backendInfo()
```

Backend info accessor function. 

### function CAT_3

```
namespace CAT_3(
    BACKENDNAME ,
    _ ,
    SAFE_VERSION 
)
```


### function load_backend_symbol

```
template <typename T >
T load_backend_symbol(
    const std::vector< str > & symbol_names,
    str be,
    str ver
)
```

Get the pointer to the backend function. 

### function handover_factory_pointer

```
template <typename T >
T handover_factory_pointer(
    str be,
    str ver,
    str name,
    str barename,
    str args,
    const std::vector< str > & symbol_names,
    T factory,
    T missing_backend,
    T missing_factory
)
```

Provide the factory pointer to a BOSSed type's wrapper constructor. 

### function math_error

```
void math_error(
    WSLINK ,
    const str & ,
    const str & 
)
```

Helper function to raise an appropriate warning or error in case of problems. 

### function is_numeric

```
template <typename T >
bool is_numeric()
```

Helper function that indicates if a type is numerical or not. 





-------------------------------

Updated on 2022-09-08 at 01:05:16 +0000