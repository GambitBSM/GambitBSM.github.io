---
title: "class Gambit::WIMP_annihilation"

description: "[No description available]"

---

# class Gambit::WIMP_annihilation



[No description available] [More...](#detailed-description)


`#include <wimp_types.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[WIMP_annihilation](/documentation/code/classes/classgambit_1_1wimp__annihilation/#function-wimp-annihilation)**()<br>Set up generic parameterisation of WIMP self-annihilation cross-section (A + Bv^2)  |
| double | **[A](/documentation/code/classes/classgambit_1_1wimp__annihilation/#function-a)**(const std::string & channel) const |
| double | **[B](/documentation/code/classes/classgambit_1_1wimp__annihilation/#function-b)**(const std::string & channel) const |
| void | **[setA](/documentation/code/classes/classgambit_1_1wimp__annihilation/#function-seta)**(const std::string & channel, double val) |
| void | **[setB](/documentation/code/classes/classgambit_1_1wimp__annihilation/#function-setb)**(const std::string & channel, double val) |

## Detailed Description

```
class Gambit::WIMP_annihilation;
```


Contain for generic parameterisation of WIMP annihilation to various two-body final states, with <sigma v> expanded as a simple power series in v^2 

## Public Functions Documentation

### function WIMP_annihilation

```
WIMP_annihilation()
```

Set up generic parameterisation of WIMP self-annihilation cross-section (A + Bv^2) 

### function A

```
double A(
    const std::string & channel
) const
```


### function B

```
double B(
    const std::string & channel
) const
```


### function setA

```
void setA(
    const std::string & channel,
    double val
)
```


### function setB

```
void setB(
    const std::string & channel,
    double val
)
```


-------------------------------

Updated on 2022-09-08 at 02:27:26 +0000