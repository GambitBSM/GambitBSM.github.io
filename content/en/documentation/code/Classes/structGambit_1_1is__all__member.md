---
title: "struct Gambit::is_all_member"

description: "[No description available]"

---

# struct Gambit::is_all_member



[No description available] [More...](#detailed-description)

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| const bool | **[value](/documentation/code/classes/structgambit_1_1is__all__member/#variable-value)**  |

## Detailed Description

```
template <typename type ,
typename... args>
struct Gambit::is_all_member;
```

## Public Attributes Documentation

### variable value

```
static const bool value = is_all_member_internal<type, void (args...)>::value;
```


-------------------------------

Updated on 2022-09-08 at 03:08:02 +0000