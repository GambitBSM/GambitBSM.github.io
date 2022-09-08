---
title: "struct Gambit::DarkBit::RD_spectrum_type"

description: "[No description available]"

---

# struct Gambit::DarkBit::RD_spectrum_type



[No description available]

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[RD_spectrum_type](/documentation/code/classes/structgambit_1_1darkbit_1_1rd__spectrum__type/)**() |
| | **[RD_spectrum_type](/documentation/code/classes/structgambit_1_1darkbit_1_1rd__spectrum__type/)**(const std::vector< [RD_coannihilating_particle](/documentation/code/classes/structgambit_1_1darkbit_1_1rd__coannihilating__particle/) > & coannPart, const std::vector< [TH_Resonance](/documentation/code/classes/structgambit_1_1darkbit_1_1th__resonance/) > & resonances, const std::vector< double > & thresholds) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| std::vector< [RD_coannihilating_particle](/documentation/code/classes/structgambit_1_1darkbit_1_1rd__coannihilating__particle/) > | **[coannihilatingParticles](/documentation/code/classes/structgambit_1_1darkbit_1_1rd__spectrum__type/)**  |
| std::vector< [TH_Resonance](/documentation/code/classes/structgambit_1_1darkbit_1_1th__resonance/) > | **[resonances](/documentation/code/classes/structgambit_1_1darkbit_1_1rd__spectrum__type/)**  |
| std::vector< double > | **[threshold_energy](/documentation/code/classes/structgambit_1_1darkbit_1_1rd__spectrum__type/)**  |
| std::string | **[particle_index_type](/documentation/code/classes/structgambit_1_1darkbit_1_1rd__spectrum__type/)**  |
| bool | **[isSelfConj](/documentation/code/classes/structgambit_1_1darkbit_1_1rd__spectrum__type/)**  |

## Public Functions Documentation

### function RD_spectrum_type

```
inline RD_spectrum_type()
```


### function RD_spectrum_type

```
inline RD_spectrum_type(
    const std::vector< RD_coannihilating_particle > & coannPart,
    const std::vector< TH_Resonance > & resonances,
    const std::vector< double > & thresholds
)
```


## Public Attributes Documentation

### variable coannihilatingParticles

```
std::vector< RD_coannihilating_particle > coannihilatingParticles;
```


### variable resonances

```
std::vector< TH_Resonance > resonances;
```


### variable threshold_energy

```
std::vector< double > threshold_energy;
```


### variable particle_index_type

```
std::string particle_index_type;
```


### variable isSelfConj

```
bool isSelfConj;
```


-------------------------------

Updated on 2022-09-08 at 01:05:17 +0000