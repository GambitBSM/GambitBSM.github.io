---
title: 'struct Gambit::variadic_ptr'
description: 'Type redefinition to get around icc compiler bugs. '

---

# Gambit::variadic_ptr



Type redefinition to get around icc compiler bugs.  [More...](#detailed-description)


`#include <functors.hpp>`

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef TYPE(*)(ARGS...,...) | **[type](/documentation/code/classes/structgambit_1_1variadic__ptr/#typedef-type)**  |

## Detailed Description

```
template <typename TYPE ,
typename... ARGS>
struct Gambit::variadic_ptr;
```

Type redefinition to get around icc compiler bugs. 
## Public Types Documentation

### typedef type

```
typedef TYPE(* Gambit::variadic_ptr< TYPE, ARGS >::type) (ARGS...,...);
```


-------------------------------

Updated on 2022-09-07 at 14:07:44 +0000