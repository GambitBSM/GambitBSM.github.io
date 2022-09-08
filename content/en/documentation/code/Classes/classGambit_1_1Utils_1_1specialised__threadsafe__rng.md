---
title: "class Gambit::Utils::specialised_threadsafe_rng"
description: "Derived thread-safe random number generator class, templated on the RNG engine type. "

---

# class Gambit::Utils::specialised_threadsafe_rng



Derived thread-safe random number generator class, templated on the RNG engine type.  [More...](#detailed-description)


`#include <threadsafe_rng.hpp>`

Inherits from [Gambit::Utils::threadsafe_rng](/documentation/code/classes/classgambit_1_1utils_1_1threadsafe__rng/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[specialised_threadsafe_rng](/documentation/code/classes/classgambit_1_1utils_1_1specialised__threadsafe__rng/)**(int & seed)<br>Create RNG engines, one for each thread.  |
| virtual | **[~specialised_threadsafe_rng](/documentation/code/classes/classgambit_1_1utils_1_1specialised__threadsafe__rng/)**()<br>Destroy RNG engines.  |
| virtual [result_type](/documentation/code/classes/classgambit_1_1utils_1_1threadsafe__rng/) | **[operator()](/documentation/code/classes/classgambit_1_1utils_1_1specialised__threadsafe__rng/)**() |

## Additional inherited members

**Public Types inherited from [Gambit::Utils::threadsafe_rng](/documentation/code/classes/classgambit_1_1utils_1_1threadsafe__rng/)**

|                | Name           |
| -------------- | -------------- |
| typedef std::uint64_t | **[result_type](/documentation/code/classes/classgambit_1_1utils_1_1threadsafe__rng/)** <br>Return type (will convert underlying RNG type to this)  |

**Public Functions inherited from [Gambit::Utils::threadsafe_rng](/documentation/code/classes/classgambit_1_1utils_1_1threadsafe__rng/)**

|                | Name           |
| -------------- | -------------- |
| virtual | **[~threadsafe_rng](/documentation/code/classes/classgambit_1_1utils_1_1threadsafe__rng/)**() =0<br>Pure virtual destructor to force overriding in derived class.  |
| constexpr [result_type](/documentation/code/classes/classgambit_1_1utils_1_1threadsafe__rng/) | **[min](/documentation/code/classes/classgambit_1_1utils_1_1threadsafe__rng/)**()<br>Operators for compliance with RandomNumberEngine interface -> random distribution sampling.  |
| constexpr [result_type](/documentation/code/classes/classgambit_1_1utils_1_1threadsafe__rng/) | **[max](/documentation/code/classes/classgambit_1_1utils_1_1threadsafe__rng/)**() |


## Detailed Description

```
template <typename Engine >
class Gambit::Utils::specialised_threadsafe_rng;
```

Derived thread-safe random number generator class, templated on the RNG engine type. 
## Public Functions Documentation

### function specialised_threadsafe_rng

```
inline specialised_threadsafe_rng(
    int & seed
)
```

Create RNG engines, one for each thread. 

### function ~specialised_threadsafe_rng

```
inline virtual ~specialised_threadsafe_rng()
```

Destroy RNG engines. 

### function operator()

```
inline virtual result_type operator()()
```


**Reimplements**: [Gambit::Utils::threadsafe_rng::operator()](/documentation/code/classes/classgambit_1_1utils_1_1threadsafe__rng/)


Generate a random integer using the chosen engine Selected uniformly from range (min,max). To be used as an entropy source for stdlib distributions. If you want (0,1) random doubles then please use [Random::draw()](/documentation/code/classes/classgambit_1_1random/), NOT this function! 


-------------------------------

Updated on 2022-09-08 at 01:05:18 +0000