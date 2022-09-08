---
title: "struct Gambit::enable_if_one_member"

description: "[No description available]"

---

# struct Gambit::enable_if_one_member



[No description available] [More...](#detailed-description)

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef std::enable_if< [is_one_member](/documentation/code/classes/structgambit_1_1is__one__member/)< T, args... >::value, ret > | **[type](/documentation/code/classes/structgambit_1_1enable__if__one__member/#typedef-type)**  |

## Detailed Description

```
template <typename T ,
typename ret ,
typename... args>
struct Gambit::enable_if_one_member;
```

## Public Types Documentation

### typedef type

```
typedef std::enable_if<is_one_member<T, args...>::value, ret> Gambit::enable_if_one_member< T, ret, args >::type;
```


-------------------------------

Updated on 2022-09-08 at 03:08:02 +0000