---
title: 'namespace Gambit::Diver_1_0_2'

description: "[No description available]"

---






[No description available]

## Classes

|                | Name           |
| -------------- | -------------- |
| struct | **[Gambit::Diver_1_0_2::diverScanData](/documentation/code/gambit_2-2/classes/structgambit_1_1diver__1__0__2_1_1diverscandata/)** <br>Structure for passing likelihood and printer data through Diver to the objective function.  |

## Functions

|                | Name           |
| -------------- | -------------- |
| double | **[objective](/documentation/code/gambit_2-2/namespaces/namespacegambit_1_1diver__1__0__2/#function-objective)**(double params[], const int param_dim, int & fcall, bool & quit, const bool validvector, void *& context)<br>Function to be minimised by Diver.  |


## Functions Documentation

### function objective

```
double objective(
    double params[],
    const int param_dim,
    int & fcall,
    bool & quit,
    const bool validvector,
    void *& context
)
```

Function to be minimised by Diver. 





-------------------------------

Updated on 2022-08-10 at 17:51:35 +0000