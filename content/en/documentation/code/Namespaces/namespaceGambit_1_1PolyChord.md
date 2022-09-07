---
title: 'namespace Gambit::PolyChord'

description: "[No description available]"

---

# Gambit::PolyChord

[No description available]

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Gambit::PolyChord::LogLikeWrapper](/documentation/code/classes/classgambit_1_1polychord_1_1loglikewrapper/)** <br>Class to connect PolyChord log-likelihood function and ScannerBit likelihood function.  |

## Types

|                | Name           |
| -------------- | -------------- |
| typedef [Gambit::Scanner::like_ptr](/documentation/code/classes/classgambit_1_1scanner_1_1like__ptr/) | **[scanPtr](/documentation/code/namespaces/namespacegambit_1_1polychord/#typedef-scanptr)** <br>Typedef for the ScannerBit pointer to the external loglikelihood function.  |

## Functions

|                | Name           |
| -------------- | -------------- |
| double | **[callback_loglike](/documentation/code/namespaces/namespacegambit_1_1polychord/#function-callback-loglike)**(double * Cube, int ndim, double * phi, int nderived)<br>C-functions to pass to PolyChord for the callbacks.  |
| void | **[callback_dumper](/documentation/code/namespaces/namespacegambit_1_1polychord/#function-callback-dumper)**(int ndead, int nlive, int npars, double * live, double * dead, double * logweights, double logZ, double logZerr) |

## Attributes

|                | Name           |
| -------------- | -------------- |
| [LogLikeWrapper](/documentation/code/classes/classgambit_1_1polychord_1_1loglikewrapper/) * | **[global_loglike_object](/documentation/code/namespaces/namespacegambit_1_1polychord/#variable-global-loglike-object)** <br>Global pointer to loglikelihood wrapper object, for use in the PolyChord callback functions.  |

## Types Documentation

### typedef scanPtr

```
typedef Gambit::Scanner::like_ptr Gambit::PolyChord::scanPtr;
```

Typedef for the ScannerBit pointer to the external loglikelihood function. 


## Functions Documentation

### function callback_loglike

```
double callback_loglike(
    double * Cube,
    int ndim,
    double * phi,
    int nderived
)
```

C-functions to pass to PolyChord for the callbacks. 

Plain-vanilla functions to pass to PolyChord for the callback. 


### function callback_dumper

```
void callback_dumper(
    int ndead,
    int nlive,
    int npars,
    double * live,
    double * dead,
    double * logweights,
    double logZ,
    double logZerr
)
```



## Attributes Documentation

### variable global_loglike_object

```
LogLikeWrapper * global_loglike_object;
```

Global pointer to loglikelihood wrapper object, for use in the PolyChord callback functions. 




-------------------------------

Updated on 2022-09-07 at 14:07:46 +0000