---
title: "class Gambit::Utils::threadsafe_rng"

description: "[No description available]"

---

# class Gambit::Utils::threadsafe_rng



[No description available] [More...](#detailed-description)


`#include <threadsafe_rng.hpp>`

Inherited by [Gambit::Utils::specialised_threadsafe_rng< Engine >](/documentation/code/classes/classgambit_1_1utils_1_1specialised__threadsafe__rng/)

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef std::uint64_t | **[result_type](/documentation/code/classes/classgambit_1_1utils_1_1threadsafe__rng/)** <br>Return type (will convert underlying RNG type to this)  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual | **[~threadsafe_rng](/documentation/code/classes/classgambit_1_1utils_1_1threadsafe__rng/)**() =0<br>Pure virtual destructor to force overriding in derived class.  |
| virtual [result_type](/documentation/code/classes/classgambit_1_1utils_1_1threadsafe__rng/) | **[operator()](/documentation/code/classes/classgambit_1_1utils_1_1threadsafe__rng/)**() =0<br>Operator used for getting random deviates.  |
| constexpr [result_type](/documentation/code/classes/classgambit_1_1utils_1_1threadsafe__rng/) | **[min](/documentation/code/classes/classgambit_1_1utils_1_1threadsafe__rng/)**()<br>Operators for compliance with RandomNumberEngine interface -> random distribution sampling.  |
| constexpr [result_type](/documentation/code/classes/classgambit_1_1utils_1_1threadsafe__rng/) | **[max](/documentation/code/classes/classgambit_1_1utils_1_1threadsafe__rng/)**() |

## Detailed Description

```
class Gambit::Utils::threadsafe_rng;
```


Base class for thread-safe random number generators. Must conform to the requirements of UniformRandomBitGenerator, see e.g. [https://en.cppreference.com/w/cpp/named_req/UniformRandomBitGenerator](https://en.cppreference.com/w/cpp/named_req/UniformRandomBitGenerator) Importantly, operator() must return UNSIGNED INTEGERS! 

## Public Types Documentation

### typedef result_type

```
typedef std::uint64_t Gambit::Utils::threadsafe_rng::result_type;
```

Return type (will convert underlying RNG type to this) 

## Public Functions Documentation

### function ~threadsafe_rng

```
inline virtual ~threadsafe_rng() =0
```

Pure virtual destructor to force overriding in derived class. 

Give an inline implementation of the destructor, to prevent link errors but keep base class pure virtual. 


### function operator()

```
virtual result_type operator()() =0
```

Operator used for getting random deviates. 

**Reimplemented by**: [Gambit::Utils::specialised_threadsafe_rng::operator()](/documentation/code/classes/classgambit_1_1utils_1_1specialised__threadsafe__rng/)


### function min

```
static inline constexpr result_type min()
```

Operators for compliance with RandomNumberEngine interface -> random distribution sampling. 

### function max

```
static inline constexpr result_type max()
```


-------------------------------

Updated on 2022-09-08 at 01:05:18 +0000