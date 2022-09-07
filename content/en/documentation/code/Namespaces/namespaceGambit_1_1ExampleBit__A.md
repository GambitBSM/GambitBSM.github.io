---
title: 'namespace Gambit::ExampleBit_A'

description: "[No description available]"

---

# Gambit::ExampleBit_A



[No description available]

## Functions

|                | Name           |
| -------------- | -------------- |
| double | **[some_other_function](/documentation/code/namespaces/namespacegambit_1_1examplebit__a/#function-some-other-function)**(int & input)<br>Some other example function.  |
| double | **[logf](/documentation/code/namespaces/namespacegambit_1_1examplebit__a/#function-logf)**(double x, double mu, double sig)<br>Un-normalised gaussian log-likelihood.  |
| void | **[nevents_pred](/documentation/code/namespaces/namespacegambit_1_1examplebit__a/#function-nevents-pred)**(double & result) |
| void | **[nevents_like](/documentation/code/namespaces/namespacegambit_1_1examplebit__a/#function-nevents-like)**(double & result) |
| void | **[particle_identity](/documentation/code/namespaces/namespacegambit_1_1examplebit__a/#function-particle-identity)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) & result) |
| void | **[nevents_pred_rounded](/documentation/code/namespaces/namespacegambit_1_1examplebit__a/#function-nevents-pred-rounded)**(int & result) |
| void | **[test_sigma](/documentation/code/namespaces/namespacegambit_1_1examplebit__a/#function-test-sigma)**(double & result) |
| void | **[function_pointer_retriever](/documentation/code/namespaces/namespacegambit_1_1examplebit__a/#function-function-pointer-retriever)**(double(*&)(int &) result) |
| void | **[example_damu](/documentation/code/namespaces/namespacegambit_1_1examplebit__a/#function-example-damu)**(double & result)<br>Example of interacting with models.  |
| void | **[lnL_gaussian](/documentation/code/namespaces/namespacegambit_1_1examplebit__a/#function-lnl-gaussian)**(double & result) |
| void | **[eventLoopManager](/documentation/code/namespaces/namespacegambit_1_1examplebit__a/#function-eventloopmanager)**()<br>Run a fake 'event loop'.  |
| void | **[exampleEventGen](/documentation/code/namespaces/namespacegambit_1_1examplebit__a/#function-exampleeventgen)**(float & result)<br>Produces a random floating-point 'event count' between 0 and 5.  |
| void | **[exampleCut](/documentation/code/namespaces/namespacegambit_1_1examplebit__a/#function-examplecut)**(int & result)<br>Rounds an event count to the nearest integer.  |
| void | **[eventAccumulator](/documentation/code/namespaces/namespacegambit_1_1examplebit__a/#function-eventaccumulator)**(int & result)<br>Adds an integral event count to a total number of accumulated events.  |
| void | **[do_Farray_stuff](/documentation/code/namespaces/namespacegambit_1_1examplebit__a/#function-do-farray-stuff)**(double & result) |
| void | **[local_xsection](/documentation/code/namespaces/namespacegambit_1_1examplebit__a/#function-local-xsection)**(double & result) |
| void | **[large_print](/documentation/code/namespaces/namespacegambit_1_1examplebit__a/#function-large-print)**(std::map< std::string, double > & result) |
| void | **[marg_poisson_test](/documentation/code/namespaces/namespacegambit_1_1examplebit__a/#function-marg-poisson-test)**(double & result)<br>Test inline marginalisation of a Poisson likelihood over a log-normally or Gaussianly-distributed nuisance parameter.  |
| void | **[bossed_pythia_test_function](/documentation/code/namespaces/namespacegambit_1_1examplebit__a/#function-bossed-pythia-test-function)**(bool & result)<br>Example of using a BOSSed version of Pythia.  |
| void | **[Backend_array_test](/documentation/code/namespaces/namespacegambit_1_1examplebit__a/#function-backend-array-test)**(double & result)<br>Tester for C/C++ backend array interfaces.  |
| void | **[flat_likelihood](/documentation/code/namespaces/namespacegambit_1_1examplebit__a/#function-flat-likelihood)**(double & result)<br>Flat test likelihood for checking prior distributions.  |

## Attributes

|                | Name           |
| -------------- | -------------- |
| double(*)(int &, const double &) | **[callback_pointer](/documentation/code/namespaces/namespacegambit_1_1examplebit__a/#variable-callback-pointer)** <br>Pointer to some function.  |


## Functions Documentation

### function some_other_function

```
double some_other_function(
    int & input
)
```

Some other example function. 

### function logf

```
double logf(
    double x,
    double mu,
    double sig
)
```

Un-normalised gaussian log-likelihood. 

### function nevents_pred

```
void nevents_pred(
    double & result
)
```


### function nevents_like

```
void nevents_like(
    double & result
)
```


### function particle_identity

```
void particle_identity(
    str & result
)
```


### function nevents_pred_rounded

```
void nevents_pred_rounded(
    int & result
)
```


### function test_sigma

```
void test_sigma(
    double & result
)
```


### function function_pointer_retriever

```
void function_pointer_retriever(
    double(*&)(int &) result
)
```


### function example_damu

```
void example_damu(
    double & result
)
```

Example of interacting with models. 

### function lnL_gaussian

```
void lnL_gaussian(
    double & result
)
```


Likelihood function for fitting the population parameters of a normal distribution (with hard-coded "observations") Mainly used for testing scanning algorthims 


### function eventLoopManager

```
void eventLoopManager()
```

Run a fake 'event loop'. 

### function exampleEventGen

```
void exampleEventGen(
    float & result
)
```

Produces a random floating-point 'event count' between 0 and 5. 

### function exampleCut

```
void exampleCut(
    int & result
)
```

Rounds an event count to the nearest integer. 

### function eventAccumulator

```
void eventAccumulator(
    int & result
)
```

Adds an integral event count to a total number of accumulated events. 

### function do_Farray_stuff

```
void do_Farray_stuff(
    double & result
)
```


### function local_xsection

```
void local_xsection(
    double & result
)
```


### function large_print

```
void large_print(
    std::map< std::string, double > & result
)
```


Scale test for various aspects of the printer buffer system Creates 1000 items to be printed per point 


### function marg_poisson_test

```
void marg_poisson_test(
    double & result
)
```

Test inline marginalisation of a Poisson likelihood over a log-normally or Gaussianly-distributed nuisance parameter. 

### function bossed_pythia_test_function

```
void bossed_pythia_test_function(
    bool & result
)
```

Example of using a BOSSed version of Pythia. 

### function Backend_array_test

```
void Backend_array_test(
    double & result
)
```

Tester for C/C++ backend array interfaces. 

### function flat_likelihood

```
void flat_likelihood(
    double & result
)
```

Flat test likelihood for checking prior distributions. 


## Attributes Documentation

### variable callback_pointer

```
double(*)(int &, const double &) callback_pointer;
```

Pointer to some function. 




-------------------------------

Updated on 2022-09-07 at 13:49:50 +0000