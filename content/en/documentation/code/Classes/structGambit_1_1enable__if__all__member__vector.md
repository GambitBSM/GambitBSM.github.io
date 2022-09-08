---
title: "struct Gambit::enable_if_all_member_vector"

description: "[No description available]"

---

# struct Gambit::enable_if_all_member_vector



[No description available] [More...](#detailed-description)

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef std::enable_if< [is_all_member_vector](/documentation/code/classes/structgambit_1_1is__all__member__vector/)< args... >::value, ret > | **[type](/documentation/code/classes/structgambit_1_1enable__if__all__member__vector/#typedef-gambitenable-if-all-member-vector-type)**  |

## Detailed Description

```
template <typename ret ,
typename... args>
struct Gambit::enable_if_all_member_vector;
```

## Public Types Documentation

### typedef type

```
typedef std::enable_if<is_all_member_vector<args...>::value, ret> Gambit::enable_if_all_member_vector< ret, args >::type;
```


-------------------------------

Updated on 2022-09-08 at 01:48:53 +0000