---
title: "class Gambit::Random"

description: "[No description available]"

---

# class Gambit::Random



[No description available]

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[create_rng_engine](/documentation/code/classes/classgambit_1_1random/)**([str](/documentation/code/namespaces/namespacegambit/) engine, int seed =-1)<br>Choose the engine to use for random number generation, based on the contents of the ini file.  |
| double | **[draw](/documentation/code/classes/classgambit_1_1random/)**()<br>Draw a single uniform random deviate from the interval (0,1) using the chosen RNG engine.  |
| [Utils::threadsafe_rng](/documentation/code/classes/classgambit_1_1utils_1_1threadsafe__rng/) & | **[rng](/documentation/code/classes/classgambit_1_1random/)**() |

## Public Functions Documentation

### function create_rng_engine

```
static void create_rng_engine(
    str engine,
    int seed =-1
)
```

Choose the engine to use for random number generation, based on the contents of the ini file. 

### function draw

```
static double draw()
```

Draw a single uniform random deviate from the interval (0,1) using the chosen RNG engine. 

Draw a single uniform random deviate in the range (0,1) using the chosen RNG engine. 


### function rng

```
static inline Utils::threadsafe_rng & rng()
```


Return a threadsafe wrapper for the chosen RNG engine (to be passed to e.g. std library distribution function objects) 


-------------------------------

Updated on 2022-09-08 at 01:05:16 +0000