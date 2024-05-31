---
title: "struct Gambit::is_container"

description: "[No description available]"

---

# struct Gambit::is_container



[No description available] [More...](#detailed-description)

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef [__is_container__](/documentation/code/classes/structgambit_1_1____is__container____/)< typenameremove_all< T >::type >::type | **[type](/documentation/code/classes/structgambit_1_1is__container/#typedef-type)**  |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| const bool | **[value](/documentation/code/classes/structgambit_1_1is__container/#variable-value)**  |

## Detailed Description

```
template <typename T >
struct Gambit::is_container;
```

## Public Types Documentation

### typedef type

```
typedef __is_container__<typenameremove_all<T>::type>::type Gambit::is_container< T >::type;
```


## Public Attributes Documentation

### variable value

```
static const bool value = __is_container__<typename remove_all<T>::type>::value;
```


-------------------------------

Updated on 2024-05-31 at 15:12:03 +0000