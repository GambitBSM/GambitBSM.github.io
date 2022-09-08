---
title: "struct Gambit::is_one_member"

description: "[No description available]"

---

# struct Gambit::is_one_member



[No description available] [More...](#detailed-description)

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| const bool | **[value](/documentation/code/classes/structgambit_1_1is__one__member/#variable-gambitis-one-member-value)**  |

## Detailed Description

```
template <typename type ,
typename... args>
struct Gambit::is_one_member;
```

## Public Attributes Documentation

### variable value

```
static const bool value = is_one_member_internal<type, void (args...)>::value;
```


-------------------------------

Updated on 2022-09-08 at 02:00:46 +0000