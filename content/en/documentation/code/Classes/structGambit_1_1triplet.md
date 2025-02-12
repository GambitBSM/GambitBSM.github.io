---
title: "struct Gambit::triplet"

description: "[No description available]"

---

# struct Gambit::triplet



[No description available] [More...](#detailed-description)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[triplet](/documentation/code/classes/structgambit_1_1triplet/#function-triplet)**()<br>Default constructor.  |
| | **[triplet](/documentation/code/classes/structgambit_1_1triplet/#function-triplet)**(TYPE centralval)<br>One-value constructor.  |
| | **[triplet](/documentation/code/classes/structgambit_1_1triplet/#function-triplet)**(TYPE centralval, TYPE upperval, TYPE lowerval)<br>Three-value constructor.  |
| | **[triplet](/documentation/code/classes/structgambit_1_1triplet/#function-triplet)**(const [triplet](/documentation/code/classes/structgambit_1_1triplet/)< TYPE > & in)<br>Copy constructor.  |
| [triplet](/documentation/code/classes/structgambit_1_1triplet/)< TYPE > & | **[operator=](/documentation/code/classes/structgambit_1_1triplet/#function-operator)**(const [triplet](/documentation/code/classes/structgambit_1_1triplet/)< TYPE > & in)<br>Copy assignment operator.  |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TYPE | **[central](/documentation/code/classes/structgambit_1_1triplet/#variable-central)**  |
| TYPE | **[upper](/documentation/code/classes/structgambit_1_1triplet/#variable-upper)**  |
| TYPE | **[lower](/documentation/code/classes/structgambit_1_1triplet/#variable-lower)**  |

## Detailed Description

```
template <typename TYPE >
struct Gambit::triplet;
```

## Public Functions Documentation

### function triplet

```
inline triplet()
```

Default constructor. 

### function triplet

```
inline triplet(
    TYPE centralval
)
```

One-value constructor. 

### function triplet

```
inline triplet(
    TYPE centralval,
    TYPE upperval,
    TYPE lowerval
)
```

Three-value constructor. 

### function triplet

```
inline triplet(
    const triplet< TYPE > & in
)
```

Copy constructor. 

### function operator=

```
inline triplet< TYPE > & operator=(
    const triplet< TYPE > & in
)
```

Copy assignment operator. 

## Public Attributes Documentation

### variable central

```
TYPE central;
```


### variable upper

```
TYPE upper;
```


### variable lower

```
TYPE lower;
```


-------------------------------

Updated on 2025-02-12 at 16:10:31 +0000