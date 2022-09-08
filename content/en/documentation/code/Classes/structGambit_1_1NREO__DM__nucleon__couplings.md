---
title: "struct Gambit::NREO_DM_nucleon_couplings"
description: "Container for effective non-relativistic DM-nucleon Wilson coefficients. "

---

# struct Gambit::NREO_DM_nucleon_couplings



Container for effective non-relativistic DM-nucleon Wilson coefficients. 


`#include <DDCalc.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[NREO_DM_nucleon_couplings](/documentation/code/classes/structgambit_1_1nreo__dm__nucleon__couplings/)**()<br>Default [NREO_DM_nucleon_couplings](/documentation/code/classes/structgambit_1_1nreo__dm__nucleon__couplings/) constructor.  |
| | **[NREO_DM_nucleon_couplings](/documentation/code/classes/structgambit_1_1nreo__dm__nucleon__couplings/)**(int CPT)<br>Default [NREO_DM_nucleon_couplings](/documentation/code/classes/structgambit_1_1nreo__dm__nucleon__couplings/) constructor.  |
| | **[NREO_DM_nucleon_couplings](/documentation/code/classes/structgambit_1_1nreo__dm__nucleon__couplings/)**(const [ModelParameters](/documentation/code/classes/classgambit_1_1modelparameters/) & pars)<br>[NREO_DM_nucleon_couplings](/documentation/code/classes/structgambit_1_1nreo__dm__nucleon__couplings/) constuctor from [ModelParameters](/documentation/code/classes/classgambit_1_1modelparameters/) object.  |
| | **[NREO_DM_nucleon_couplings](/documentation/code/classes/structgambit_1_1nreo__dm__nucleon__couplings/)**(const [Models::safe_param_map](/documentation/code/classes/classgambit_1_1models_1_1safe__param__map/)< [safe_ptr](/documentation/code/classes/classgambit_1_1safe__ptr/)< const double > > & pars)<br>[NREO_DM_nucleon_couplings](/documentation/code/classes/structgambit_1_1nreo__dm__nucleon__couplings/) constuctor from functor 'Params', i.e. 'safe_param_map' used to hold collected model parameters.  |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| int | **[CPTbasis](/documentation/code/classes/structgambit_1_1nreo__dm__nucleon__couplings/)**  |
| std::map< int, double > | **[c0](/documentation/code/classes/structgambit_1_1nreo__dm__nucleon__couplings/)** <br>Store couplings in map for easier iteration.  |
| std::map< int, double > | **[c1](/documentation/code/classes/structgambit_1_1nreo__dm__nucleon__couplings/)**  |

## Public Functions Documentation

### function NREO_DM_nucleon_couplings

```
NREO_DM_nucleon_couplings()
```

Default [NREO_DM_nucleon_couplings](/documentation/code/classes/structgambit_1_1nreo__dm__nucleon__couplings/) constructor. 

### function NREO_DM_nucleon_couplings

```
NREO_DM_nucleon_couplings(
    int CPT
)
```

Default [NREO_DM_nucleon_couplings](/documentation/code/classes/structgambit_1_1nreo__dm__nucleon__couplings/) constructor. 

### function NREO_DM_nucleon_couplings

```
NREO_DM_nucleon_couplings(
    const ModelParameters & pars
)
```

[NREO_DM_nucleon_couplings](/documentation/code/classes/structgambit_1_1nreo__dm__nucleon__couplings/) constuctor from [ModelParameters](/documentation/code/classes/classgambit_1_1modelparameters/) object. 

### function NREO_DM_nucleon_couplings

```
NREO_DM_nucleon_couplings(
    const Models::safe_param_map< safe_ptr< const double > > & pars
)
```

[NREO_DM_nucleon_couplings](/documentation/code/classes/structgambit_1_1nreo__dm__nucleon__couplings/) constuctor from functor 'Params', i.e. 'safe_param_map' used to hold collected model parameters. 

## Public Attributes Documentation

### variable CPTbasis

```
int CPTbasis;
```


### variable c0

```
std::map< int, double > c0;
```

Store couplings in map for easier iteration. 

### variable c1

```
std::map< int, double > c1;
```


-------------------------------

Updated on 2022-09-08 at 01:05:16 +0000