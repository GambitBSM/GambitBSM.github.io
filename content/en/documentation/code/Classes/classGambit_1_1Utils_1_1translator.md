---
title: "class Gambit::Utils::translator"

description: "[No description available]"

---

# class Gambit::Utils::translator



[No description available]

## Public Functions

|                | Name           |
| -------------- | -------------- |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[operator()](/documentation/code/classes/classgambit_1_1utils_1_1translator/#function-operator)**(const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & from, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & to, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & obs)<br>Translate terms from one language to another.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[operator()](/documentation/code/classes/classgambit_1_1utils_1_1translator/#function-operator)**(const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & from, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & to, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & obs, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & suffix)<br>Translate terms from one language to another and add a suffix.  |
| std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > | **[operator()](/documentation/code/classes/classgambit_1_1utils_1_1translator/#function-operator)**(const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & from, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & to, const std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > & obs)<br>Translate terms from one language to another.  |
| std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > | **[operator()](/documentation/code/classes/classgambit_1_1utils_1_1translator/#function-operator)**(const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & from, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & to, const std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > & obs, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & suffix)<br>Translate terms from one language to another and add a suffix.  |
| | **[translator](/documentation/code/classes/classgambit_1_1utils_1_1translator/#function-translator)**(const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & filename_)<br>Constructor for translator.  |

## Public Functions Documentation

### function operator()

```
str operator()(
    const str & from,
    const str & to,
    const str & obs
)
```

Translate terms from one language to another. 

Translate terms from one language to another. 


### function operator()

```
str operator()(
    const str & from,
    const str & to,
    const str & obs,
    const str & suffix
)
```

Translate terms from one language to another and add a suffix. 

### function operator()

```
std::vector< str > operator()(
    const str & from,
    const str & to,
    const std::vector< str > & obs
)
```

Translate terms from one language to another. 

### function operator()

```
std::vector< str > operator()(
    const str & from,
    const str & to,
    const std::vector< str > & obs,
    const str & suffix
)
```

Translate terms from one language to another and add a suffix. 

### function translator

```
translator(
    const str & filename_
)
```

Constructor for translator. 

-------------------------------

Updated on 2025-02-12 at 16:10:33 +0000