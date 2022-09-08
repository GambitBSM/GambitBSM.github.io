---
title: "struct Gambit::is_pair"

description: "[No description available]"

---

# struct Gambit::is_pair



[No description available] [More...](#detailed-description)

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef [__is_pair__](/documentation/code/classes/structgambit_1_1____is__pair____/)< typenameremove_all< T >::type >::first_type | **[first_type](/documentation/code/classes/structgambit_1_1is__pair/#typedef-first-type)**  |
| typedef [__is_pair__](/documentation/code/classes/structgambit_1_1____is__pair____/)< typenameremove_all< T >::type >::second_type | **[second_type](/documentation/code/classes/structgambit_1_1is__pair/#typedef-second-type)**  |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| const bool | **[value](/documentation/code/classes/structgambit_1_1is__pair/#variable-value)**  |

## Detailed Description

```
template <typename T >
struct Gambit::is_pair;
```

## Public Types Documentation

### typedef first_type

```
typedef __is_pair__<typenameremove_all<T>::type>::first_type Gambit::is_pair< T >::first_type;
```


### typedef second_type

```
typedef __is_pair__<typenameremove_all<T>::type>::second_type Gambit::is_pair< T >::second_type;
```


## Public Attributes Documentation

### variable value

```
static const bool value = __is_pair__<typename remove_all<T>::type>::value;
```


-------------------------------

Updated on 2022-09-08 at 03:41:57 +0000