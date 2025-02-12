---
title: "struct Gambit::variadic_ptr"
description: "Type redefinition to get around icc compiler bugs. "

---

# struct Gambit::variadic_ptr



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

Updated on 2025-02-12 at 16:10:31 +0000