---
title: "struct Gambit::is_vector"

description: "[No description available]"

---

# struct Gambit::is_vector



[No description available] [More...](#detailed-description)

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef [__is_vector__](/documentation/code/classes/structgambit_1_1____is__vector____/)< typenameremove_all< T >::type >::type | **[type](/documentation/code/classes/structgambit_1_1is__vector/#typedef-type)**  |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| const bool | **[value](/documentation/code/classes/structgambit_1_1is__vector/#variable-value)**  |

## Detailed Description

```
template <typename T >
struct Gambit::is_vector;
```

## Public Types Documentation

### typedef type

```
typedef __is_vector__<typenameremove_all<T>::type>::type Gambit::is_vector< T >::type;
```


## Public Attributes Documentation

### variable value

```
static const bool value = __is_vector__<typename remove_all<T>::type>::value;
```


-------------------------------

Updated on 2022-09-08 at 00:43:00 +0000