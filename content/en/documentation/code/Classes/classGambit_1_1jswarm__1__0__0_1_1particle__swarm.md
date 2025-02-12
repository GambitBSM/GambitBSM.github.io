---
title: "class Gambit::jswarm_1_0_0::particle_swarm"
description: "A swarm of particles and methods to evolve them. "

---

# class Gambit::jswarm_1_0_0::particle_swarm



A swarm of particles and methods to evolve them. 


`#include <jswarm.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[particle_swarm](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle__swarm/#function-particle-swarm)**()<br>Constructor.  |
| void | **[init](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle__swarm/#function-init)**()<br>Initialise the swarm.  |
| void | **[run](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle__swarm/#function-run)**()<br>Release the swarm.  |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| std::vector< double > | **[upperbounds](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle__swarm/#variable-upperbounds)**  |
| std::vector< double > | **[lowerbounds](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle__swarm/#variable-lowerbounds)**  |
| [Scanner::like_ptr](/documentation/code/classes/classgambit_1_1scanner_1_1like__ptr/) | **[likelihood_function](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle__swarm/#variable-likelihood-function)** <br>Pointer to objective function.  |
| [Scanner::printer_interface](/documentation/code/namespaces/namespacegambit_1_1scanner/#typedef-printer-interface) * | **[printer](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle__swarm/#variable-printer)** <br>Pointer to GAMBIT printer.  |
| std::string | **[path](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle__swarm/#variable-path)** <br>Prefix for all j-Swarm save files.  |
| int | **[nPar](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle__swarm/#variable-npar)** <br>Dimensionality of the parameter space.  |
| int | **[nDerived](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle__swarm/#variable-nderived)** <br>Number of derived quantities to output (GAMBIT printers handle these).  |
| int | **[nDiscrete](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle__swarm/#variable-ndiscrete)** <br>Number of parameters that are to be treated as discrete.  |
| int | **[maxgen](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle__swarm/#variable-maxgen)** <br>Maximum number of generations.  |
| int | **[NP](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle__swarm/#variable-np)** <br>Population size (individuals per generation)  |
| int | **[bndry](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle__swarm/#variable-bndry)** <br>Boundary constraint: 1=brick wall, 2=random re-initialization, 3=reflection.  |
| int | **[convsteps](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle__swarm/#variable-convsteps)** <br>Number of steps to smooth over when checking convergence.  |
| int | **[savecount](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle__swarm/#variable-savecount)** <br>Save progress every savecount generations.  |
| int | **[init_pop_strategy](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle__swarm/#variable-init-pop-strategy)** <br>Initialisation strategy: 0=one shot, 1=n-shot, 2=n-shot with error if no valid vectors found.  |
| int | **[max_ini_attempts](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle__swarm/#variable-max-ini-attempts)** <br>Maximum number of times to try to find a valid vector for each slot in the initial population.  |
| int | **[verbose](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle__swarm/#variable-verbose)** <br>Output verbosity: 0=only error messages, 1=basic info, 2=civ-level info, 3+=population info.  |
| int | **[seed](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle__swarm/#variable-seed)** <br>Base seed for random number generation; non-positive means seed from the system clock.  |
| int | **[fcall](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle__swarm/#variable-fcall)** <br>Number of calls to the objective function so far.  |
| int | **[fcall_global](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle__swarm/#variable-fcall-global)** <br>Number of calls to the objective function so far across all processes.  |
| double | **[omega](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle__swarm/#variable-omega)** <br>Inertial weight.  |
| double | **[phi1](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle__swarm/#variable-phi1)** <br>Cognitive weight.  |
| double | **[phi2](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle__swarm/#variable-phi2)** <br>Social weight.  |
| double | **[convthresh](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle__swarm/#variable-convthresh)** <br>Threshold for gen-level convergence: smoothed fractional improvement in the mean personal best population value.  |
| double | **[min_acceptable_value](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle__swarm/#variable-min-acceptable-value)** <br>Minimum function value to accept for the initial generation if init_population_strategy > 0.  |
| bool | **[adapt_phi](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle__swarm/#variable-adapt-phi)** <br>Use self-optimising adaptive choices for phi1 and phi2.  |
| bool | **[adapt_omega](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle__swarm/#variable-adapt-omega)** <br>Use self-optimising adaptive choices for omega.  |
| bool | **[init_stationary](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle__swarm/#variable-init-stationary)** <br>Initialise particle velocities to zero.  |
| bool | **[resume](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle__swarm/#variable-resume)** <br>Resume from previous run.  |
| bool | **[allow_new_settings](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle__swarm/#variable-allow-new-settings)** <br>Allow settings to be overridden with new values when resuming.  |
| bool | **[save_particles_natively](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle__swarm/#variable-save-particles-natively)** <br>Save full particle data from every generation.  |
| std::vector< int > | **[discrete](/documentation/code/classes/classgambit_1_1jswarm__1__0__0_1_1particle__swarm/#variable-discrete)** <br>Indices of parameters to be treated as discrete.  |

## Public Functions Documentation

### function particle_swarm

```
particle_swarm()
```

Constructor. 

### function init

```
void init()
```

Initialise the swarm. 

### function run

```
void run()
```

Release the swarm. 

## Public Attributes Documentation

### variable upperbounds

```
std::vector< double > upperbounds;
```


Parameter space boundaries 


### variable lowerbounds

```
std::vector< double > lowerbounds;
```


### variable likelihood_function

```
Scanner::like_ptr likelihood_function;
```

Pointer to objective function. 

### variable printer

```
Scanner::printer_interface * printer;
```

Pointer to GAMBIT printer. 

### variable path

```
std::string path;
```

Prefix for all j-Swarm save files. 

### variable nPar

```
int nPar;
```

Dimensionality of the parameter space. 

### variable nDerived

```
int nDerived;
```

Number of derived quantities to output (GAMBIT printers handle these). 

### variable nDiscrete

```
int nDiscrete;
```

Number of parameters that are to be treated as discrete. 

### variable maxgen

```
int maxgen;
```

Maximum number of generations. 

### variable NP

```
int NP;
```

Population size (individuals per generation) 

### variable bndry

```
int bndry;
```

Boundary constraint: 1=brick wall, 2=random re-initialization, 3=reflection. 

### variable convsteps

```
int convsteps;
```

Number of steps to smooth over when checking convergence. 

### variable savecount

```
int savecount;
```

Save progress every savecount generations. 

### variable init_pop_strategy

```
int init_pop_strategy;
```

Initialisation strategy: 0=one shot, 1=n-shot, 2=n-shot with error if no valid vectors found. 

### variable max_ini_attempts

```
int max_ini_attempts;
```

Maximum number of times to try to find a valid vector for each slot in the initial population. 

### variable verbose

```
int verbose;
```

Output verbosity: 0=only error messages, 1=basic info, 2=civ-level info, 3+=population info. 

### variable seed

```
int seed;
```

Base seed for random number generation; non-positive means seed from the system clock. 

### variable fcall

```
int fcall;
```

Number of calls to the objective function so far. 

### variable fcall_global

```
int fcall_global;
```

Number of calls to the objective function so far across all processes. 

### variable omega

```
double omega;
```

Inertial weight. 

### variable phi1

```
double phi1;
```

Cognitive weight. 

### variable phi2

```
double phi2;
```

Social weight. 

### variable convthresh

```
double convthresh;
```

Threshold for gen-level convergence: smoothed fractional improvement in the mean personal best population value. 

### variable min_acceptable_value

```
double min_acceptable_value;
```

Minimum function value to accept for the initial generation if init_population_strategy > 0. 

### variable adapt_phi

```
bool adapt_phi;
```

Use self-optimising adaptive choices for phi1 and phi2. 

### variable adapt_omega

```
bool adapt_omega;
```

Use self-optimising adaptive choices for omega. 

### variable init_stationary

```
bool init_stationary;
```

Initialise particle velocities to zero. 

### variable resume

```
bool resume;
```

Resume from previous run. 

### variable allow_new_settings

```
bool allow_new_settings;
```

Allow settings to be overridden with new values when resuming. 

### variable save_particles_natively

```
bool save_particles_natively;
```

Save full particle data from every generation. 

### variable discrete

```
std::vector< int > discrete;
```

Indices of parameters to be treated as discrete. 

-------------------------------

Updated on 2025-02-12 at 15:36:39 +0000