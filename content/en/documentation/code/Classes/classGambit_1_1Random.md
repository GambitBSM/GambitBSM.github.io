---
title: "class Gambit::Random"

description: "[No description available]"

---

# class Gambit::Random



[No description available]

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[create_rng_engine](/documentation/code/classes/classgambit_1_1random/#function-create-rng-engine)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) engine, int seed =-1)<br>Choose the engine to use for random number generation, based on the contents of the ini file.  |
| double | **[draw](/documentation/code/classes/classgambit_1_1random/#function-draw)**()<br>Draw a single uniform random deviate from the interval (0,1) using the chosen RNG engine.  |
| [Utils::threadsafe_rng](/documentation/code/classes/classgambit_1_1utils_1_1threadsafe__rng/) & | **[rng](/documentation/code/classes/classgambit_1_1random/#function-rng)**() |

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

Updated on 2025-02-12 at 16:10:31 +0000