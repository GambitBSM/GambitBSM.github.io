---
title: "class Gambit::jswarm_1_0_0::particle"
description: "An individual particle in a swarm. "

---

# class Gambit::jswarm_1_0_0::particle



An individual particle in a swarm. 


`#include <jswarm.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[particle](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle/#function-particle)**(int nPar, std::vector< double > & lb, std::vector< double > & ub, [rng_type](/documentation/code/namespaces/namespacegambit_1_1jswarm__1__0__0/#typedef-rng-type) & generator)<br>Constructor.  |
| void | **[init](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle/#function-init)**(bool zero_vel)<br>Initialise a particle with a random position and zero/random velocity.  |
| void | **[update_personal_best](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle/#function-update-personal-best)**()<br>Update the particle's personal best-seen fit so far.  |
| void | **[reflect](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle/#function-reflect)**()<br>Reflect a particle's position and velocity about the walls of the prior box.  |
| std::vector< double > | **[discretised_x](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle/#function-discretised-x)**(const std::vector< int > & indices)<br>Return a particle's position vector, discretised at some specified indices.  |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| std::vector< double > | **[x](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle/#variable-x)** <br>Particle position vector.  |
| std::vector< double > | **[v](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle/#variable-v)** <br>Particle velocity vector.  |
| double | **[lnlike](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle/#variable-lnlike)** <br>Current objective value.  |
| double | **[personal_best_value](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle/#variable-personal-best-value)** <br>Current personal best fit.  |
| std::vector< double > | **[personal_best_x](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle/#variable-personal-best-x)** <br>Current personal best-fit vector.  |

## Public Functions Documentation

### function particle

```
particle(
    int nPar,
    std::vector< double > & lb,
    std::vector< double > & ub,
    rng_type & generator
)
```

Constructor. 

### function init

```
void init(
    bool zero_vel
)
```

Initialise a particle with a random position and zero/random velocity. 

### function update_personal_best

```
void update_personal_best()
```

Update the particle's personal best-seen fit so far. 

Update the particle's personal best fit seen so far. 


### function reflect

```
void reflect()
```

Reflect a particle's position and velocity about the walls of the prior box. 

Reflect a particle's position and velocity off the walls of the prior box. 


### function discretised_x

```
std::vector< double > discretised_x(
    const std::vector< int > & indices
)
```

Return a particle's position vector, discretised at some specified indices. 

## Public Attributes Documentation

### variable x

```
std::vector< double > x;
```

Particle position vector. 

### variable v

```
std::vector< double > v;
```

Particle velocity vector. 

### variable lnlike

```
double lnlike;
```

Current objective value. 

### variable personal_best_value

```
double personal_best_value;
```

Current personal best fit. 

### variable personal_best_x

```
std::vector< double > personal_best_x;
```

Current personal best-fit vector. 

-------------------------------

Updated on 2025-02-12 at 15:36:39 +0000