---
title: "struct Gambit::is_same_type< mult_types< args... >, T >"

description: "[No description available]"

---

# struct Gambit::is_same_type< mult_types< args... >, T >



[No description available] [More...](#detailed-description)

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| const bool | **[value](/documentation/code/classes/structgambit_1_1is__same__type_3_01mult__types_3_01args_8_8_8_01_4_00_01t_01_4/#variable-value)**  |

## Detailed Description

```
template <typename T ,
typename... args>
struct Gambit::is_same_type< mult_types< args... >, T >;
```

## Public Attributes Documentation

### variable value

```
static const bool value = is_same_type_internal <typename mult_types<args...>::type, T>::value;
```


-------------------------------

Updated on 2022-09-07 at 23:22:05 +0000