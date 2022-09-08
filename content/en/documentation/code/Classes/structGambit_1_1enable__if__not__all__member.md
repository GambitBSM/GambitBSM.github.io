---
title: "struct Gambit::enable_if_not_all_member"

description: "[No description available]"

---

# struct Gambit::enable_if_not_all_member



[No description available] [More...](#detailed-description)

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef std::enable_if<![is_all_member](/documentation/code/classes/structgambit_1_1is__all__member/)< T, args... >::value, ret > | **[type](/documentation/code/classes/structgambit_1_1enable__if__not__all__member/#typedef-gambitenable-if-not-all-member-type)**  |

## Detailed Description

```
template <typename T ,
typename ret ,
typename... args>
struct Gambit::enable_if_not_all_member;
```

## Public Types Documentation

### typedef type

```
typedef std::enable_if<!is_all_member<T, args...>::value, ret> Gambit::enable_if_not_all_member< T, ret, args >::type;
```


-------------------------------

Updated on 2022-09-08 at 02:00:46 +0000