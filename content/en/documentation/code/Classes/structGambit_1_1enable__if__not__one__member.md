---
title: 'struct Gambit::enable_if_not_one_member'

description: "[No description available]"

---

# Gambit::enable_if_not_one_member



[No description available] [More...](#detailed-description)

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef std::enable_if<![is_one_member](/documentation/code/classes/structgambit_1_1is__one__member/)< T, args... >::value, ret > | **[type](/documentation/code/classes/structgambit_1_1enable__if__not__one__member/#typedef-type)**  |

## Detailed Description

```
template <typename T ,
typename ret ,
typename... args>
struct Gambit::enable_if_not_one_member;
```

## Public Types Documentation

### typedef type

```
typedef std::enable_if<!is_one_member<T, args...>::value, ret> Gambit::enable_if_not_one_member< T, ret, args >::type;
```


-------------------------------

Updated on 2022-09-07 at 14:07:44 +0000