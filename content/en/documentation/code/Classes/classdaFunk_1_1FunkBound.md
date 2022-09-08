---
title: "class daFunk::FunkBound"

description: "[No description available]"

---

# class daFunk::FunkBound



[No description available]

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[FunkBound](/documentation/code/classes/classdafunk_1_1funkbound/#function-funkbound)**(Funk f, size_t datalen, size_t bindID) |
| | **[~FunkBound](/documentation/code/classes/classdafunk_1_1funkbound/#function-funkbound)**() |
| double | **[value](/documentation/code/classes/classdafunk_1_1funkbound/#function-value)**(std::vector< double > & map, size_t bindID) |
| template <typename... Args\> <br>double | **[eval](/documentation/code/classes/classdafunk_1_1funkbound/#function-eval)**(Args... argss) |
| template <typename... Args\> <br>std::vector< double > | **[vect](/documentation/code/classes/classdafunk_1_1funkbound/#function-vect)**(Args... argss) |

## Friends

|                | Name           |
| -------------- | -------------- |
| shared_ptr< [FunkBound](/documentation/code/classes/classdafunk_1_1funkbound/) > | **[FunkBase::bind](/documentation/code/classes/classdafunk_1_1funkbound/#friend-funkbasebind)**(Args... argss)  |

## Public Functions Documentation

### function FunkBound

```
inline FunkBound(
    Funk f,
    size_t datalen,
    size_t bindID
)
```


### function ~FunkBound

```
inline ~FunkBound()
```


### function value

```
inline double value(
    std::vector< double > & map,
    size_t bindID
)
```


### function eval

```
template <typename... Args>
inline double eval(
    Args... argss
)
```


### function vect

```
template <typename... Args>
inline std::vector< double > vect(
    Args... argss
)
```


## Friends

### friend FunkBase::bind

```
friend shared_ptr< FunkBound > FunkBase::bind(
    Args... argss
);
```


-------------------------------

Updated on 2022-09-08 at 00:43:02 +0000