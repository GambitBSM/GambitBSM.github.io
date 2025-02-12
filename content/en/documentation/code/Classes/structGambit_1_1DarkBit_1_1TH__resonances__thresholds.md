---
title: "struct Gambit::DarkBit::TH_resonances_thresholds"
description: "Location of resonances and thresholds in energy (GeV) "

---

# struct Gambit::DarkBit::TH_resonances_thresholds



Location of resonances and thresholds in energy (GeV) 


`#include <ProcessCatalog.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[TH_resonances_thresholds](/documentation/code/classes/structgambit_1_1darkbit_1_1th__resonances__thresholds/#function-th-resonances-thresholds)**() |
| | **[TH_resonances_thresholds](/documentation/code/classes/structgambit_1_1darkbit_1_1th__resonances__thresholds/#function-th-resonances-thresholds)**(const [TH_resonances_thresholds](/documentation/code/classes/structgambit_1_1darkbit_1_1th__resonances__thresholds/) & copy) |
| [TH_resonances_thresholds](/documentation/code/classes/structgambit_1_1darkbit_1_1th__resonances__thresholds/) & | **[operator=](/documentation/code/classes/structgambit_1_1darkbit_1_1th__resonances__thresholds/#function-operator)**(const [TH_resonances_thresholds](/documentation/code/classes/structgambit_1_1darkbit_1_1th__resonances__thresholds/) & ) =default |
| | **[TH_resonances_thresholds](/documentation/code/classes/structgambit_1_1darkbit_1_1th__resonances__thresholds/#function-th-resonances-thresholds)**(const std::vector< [TH_Resonance](/documentation/code/classes/structgambit_1_1darkbit_1_1th__resonance/) > & resonances, const std::vector< double > & thresholds) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| std::vector< [TH_Resonance](/documentation/code/classes/structgambit_1_1darkbit_1_1th__resonance/) > | **[resonances](/documentation/code/classes/structgambit_1_1darkbit_1_1th__resonances__thresholds/#variable-resonances)**  |
| std::vector< double > | **[threshold_energy](/documentation/code/classes/structgambit_1_1darkbit_1_1th__resonances__thresholds/#variable-threshold-energy)**  |

## Public Functions Documentation

### function TH_resonances_thresholds

```
inline TH_resonances_thresholds()
```


### function TH_resonances_thresholds

```
inline TH_resonances_thresholds(
    const TH_resonances_thresholds & copy
)
```


### function operator=

```
TH_resonances_thresholds & operator=(
    const TH_resonances_thresholds & 
) =default
```


### function TH_resonances_thresholds

```
inline TH_resonances_thresholds(
    const std::vector< TH_Resonance > & resonances,
    const std::vector< double > & thresholds
)
```


## Public Attributes Documentation

### variable resonances

```
std::vector< TH_Resonance > resonances;
```


### variable threshold_energy

```
std::vector< double > threshold_energy;
```


-------------------------------

Updated on 2025-02-12 at 16:10:32 +0000