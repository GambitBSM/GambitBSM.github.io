---
title: 'struct Gambit::enable_if_one_member_vector'

description: "[No description available]"

---

# Gambit::enable_if_one_member_vector



[No description available] [More...](#detailed-description)

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef std::enable_if< [is_one_member_vector](/documentation/code/classes/structgambit_1_1is__one__member__vector/)< args... >::value, ret > | **[type](/documentation/code/classes/structgambit_1_1enable__if__one__member__vector/#typedef-type)**  |

## Detailed Description

```
template <typename ret ,
typename... args>
struct Gambit::enable_if_one_member_vector;
```

## Public Types Documentation

### typedef type

```
typedef std::enable_if<is_one_member_vector<args...>::value, ret> Gambit::enable_if_one_member_vector< ret, args >::type;
```


-------------------------------

Updated on 2022-09-07 at 14:07:44 +0000