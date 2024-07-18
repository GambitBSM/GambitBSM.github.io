---
title: "class Gambit::CallFcn< HostSpec, MapTag::Set >"
description: "Specialisation of [CallFcn](/documentation/code/classes/classgambit_1_1callfcn/) for calling 'setter' functions. "

---

# class Gambit::CallFcn< HostSpec, MapTag::Set >



Specialisation of [CallFcn](/documentation/code/classes/classgambit_1_1callfcn/) for calling 'setter' functions.  [More...](#detailed-description)


`#include <spec_fptrfinder.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[CallFcn](/documentation/code/classes/classgambit_1_1callfcn_3_01hostspec_00_01maptag_1_1set_01_4/#function-callfcn)**([FptrFinder](/documentation/code/classes/classgambit_1_1fptrfinder/)< HostSpec, [MapTag::Set](/documentation/code/classes/structgambit_1_1maptag_1_1set/) > * host) |
| void | **[operator()](/documentation/code/classes/classgambit_1_1callfcn_3_01hostspec_00_01maptag_1_1set_01_4/#function-operator)**(const double set_value) |

## Detailed Description

```
template <class HostSpec >
class Gambit::CallFcn< HostSpec, MapTag::Set >;
```

Specialisation of [CallFcn](/documentation/code/classes/classgambit_1_1callfcn/) for calling 'setter' functions. 
## Public Functions Documentation

### function CallFcn

```
inline CallFcn(
    FptrFinder< HostSpec, MapTag::Set > * host
)
```


### function operator()

```
inline void operator()(
    const double set_value
)
```


-------------------------------

Updated on 2024-07-18 at 13:53:30 +0000