---
title: "class Gambit::CallFcn< HostSpec, MapTag::Get >"
description: "Specialisation of [CallFcn](/documentation/code/classes/classgambit_1_1callfcn/) for calling 'getter' functions. "

---

# class Gambit::CallFcn< HostSpec, MapTag::Get >



Specialisation of [CallFcn](/documentation/code/classes/classgambit_1_1callfcn/) for calling 'getter' functions.  [More...](#detailed-description)


`#include <spec_fptrfinder.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[CallFcn](/documentation/code/classes/classgambit_1_1callfcn_3_01hostspec_00_01maptag_1_1get_01_4/#function-callfcn)**([FptrFinder](/documentation/code/classes/classgambit_1_1fptrfinder/)< HostSpec, [MapTag::Get](/documentation/code/classes/structgambit_1_1maptag_1_1get/) > * host) |
| double | **[operator()](/documentation/code/classes/classgambit_1_1callfcn_3_01hostspec_00_01maptag_1_1get_01_4/#function-operator)**() |

## Detailed Description

```
template <class HostSpec >
class Gambit::CallFcn< HostSpec, MapTag::Get >;
```

Specialisation of [CallFcn](/documentation/code/classes/classgambit_1_1callfcn/) for calling 'getter' functions. 
## Public Functions Documentation

### function CallFcn

```
inline CallFcn(
    FptrFinder< HostSpec, MapTag::Get > * host
)
```


### function operator()

```
inline double operator()()
```


-------------------------------

Updated on 2024-05-31 at 15:12:02 +0000