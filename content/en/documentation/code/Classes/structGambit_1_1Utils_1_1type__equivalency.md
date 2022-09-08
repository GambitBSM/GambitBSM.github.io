---
title: "struct Gambit::Utils::type_equivalency"
description: "Structure providing type equivalency classes to the dep resolver. "

---

# struct Gambit::Utils::type_equivalency



Structure providing type equivalency classes to the dep resolver. 


`#include <type_equivalency.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[add](/documentation/code/classes/structgambit_1_1utils_1_1type__equivalency/#function-add)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) t1, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) t2) |
| void | **[add](/documentation/code/classes/structgambit_1_1utils_1_1type__equivalency/#function-add)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) t1, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) t2, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) t3) |
| void | **[add](/documentation/code/classes/structgambit_1_1utils_1_1type__equivalency/#function-add)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) t1, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) t2, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) t3, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) t4) |
| void | **[add](/documentation/code/classes/structgambit_1_1utils_1_1type__equivalency/#function-add)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) t1, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) t2, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) t3, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) t4, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) t5) |
| void | **[add](/documentation/code/classes/structgambit_1_1utils_1_1type__equivalency/#function-add)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) t1, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) t2, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) t3, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) t4, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) t5, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) t6) |
| void | **[add](/documentation/code/classes/structgambit_1_1utils_1_1type__equivalency/#function-add)**(std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > v) |
| | **[type_equivalency](/documentation/code/classes/structgambit_1_1utils_1_1type__equivalency/#function-type-equivalency)**()<br>Constructor.  |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| std::set< std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > > | **[equivalency_classes](/documentation/code/classes/structgambit_1_1utils_1_1type__equivalency/#variable-equivalency-classes)**  |

## Public Functions Documentation

### function add

```
void add(
    str t1,
    str t2
)
```


Define a new equivalency relation {@ 


### function add

```
void add(
    str t1,
    str t2,
    str t3
)
```


### function add

```
void add(
    str t1,
    str t2,
    str t3,
    str t4
)
```


### function add

```
void add(
    str t1,
    str t2,
    str t3,
    str t4,
    str t5
)
```


### function add

```
void add(
    str t1,
    str t2,
    str t3,
    str t4,
    str t5,
    str t6
)
```


### function add

```
void add(
    std::vector< str > v
)
```


### function type_equivalency

```
type_equivalency()
```

Constructor. 

Constructor for [type_equivalency](/documentation/code/classes/structgambit_1_1utils_1_1type__equivalency/). 


## Public Attributes Documentation

### variable equivalency_classes

```
std::set< std::set< str > > equivalency_classes;
```


}@ The total set of equivalency classes 


-------------------------------

Updated on 2022-09-08 at 00:43:02 +0000