---
title: "struct Gambit::is_one_member_internal< type, void(T, args...)>"

description: "[No description available]"

---

# struct Gambit::is_one_member_internal< type, void(T, args...)>



[No description available] [More...](#detailed-description)

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| const bool | **[value](/documentation/code/classes/structgambit_1_1is__one__member__internal_3_01type_00_01void_07t_00_01args_8_8_8_08_4/#variable-gambitis-one-member-internal-type-voidt-args-value)**  |

## Detailed Description

```
template <typename type ,
typename T ,
typename... args>
struct Gambit::is_one_member_internal< type, void(T, args...)>;
```

## Public Attributes Documentation

### variable value

```
static const bool value = is_same_type<type, T>::value || is_one_member_internal<type, void (args...)>::value;
```


-------------------------------

Updated on 2022-09-08 at 01:48:54 +0000