---
title: "struct Gambit::DarkBit::RD_spectrum_type"

description: "[No description available]"

---

# struct Gambit::DarkBit::RD_spectrum_type



[No description available]

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[RD_spectrum_type](/documentation/code/classes/structgambit_1_1darkbit_1_1rd__spectrum__type/#function-rd-spectrum-type)**() |
| | **[RD_spectrum_type](/documentation/code/classes/structgambit_1_1darkbit_1_1rd__spectrum__type/#function-rd-spectrum-type)**(const std::vector< [RD_coannihilating_particle](/documentation/code/classes/structgambit_1_1darkbit_1_1rd__coannihilating__particle/) > & coannPart, const std::vector< [TH_Resonance](/documentation/code/classes/structgambit_1_1darkbit_1_1th__resonance/) > & resonances, const std::vector< double > & thresholds) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| std::vector< [RD_coannihilating_particle](/documentation/code/classes/structgambit_1_1darkbit_1_1rd__coannihilating__particle/) > | **[coannihilatingParticles](/documentation/code/classes/structgambit_1_1darkbit_1_1rd__spectrum__type/#variable-coannihilatingparticles)**  |
| std::vector< [TH_Resonance](/documentation/code/classes/structgambit_1_1darkbit_1_1th__resonance/) > | **[resonances](/documentation/code/classes/structgambit_1_1darkbit_1_1rd__spectrum__type/#variable-resonances)**  |
| std::vector< double > | **[threshold_energy](/documentation/code/classes/structgambit_1_1darkbit_1_1rd__spectrum__type/#variable-threshold-energy)**  |
| std::string | **[particle_index_type](/documentation/code/classes/structgambit_1_1darkbit_1_1rd__spectrum__type/#variable-particle-index-type)**  |
| double | **[etaDM](/documentation/code/classes/structgambit_1_1darkbit_1_1rd__spectrum__type/#variable-etadm)**  |
| bool | **[isSelfConj](/documentation/code/classes/structgambit_1_1darkbit_1_1rd__spectrum__type/#variable-isselfconj)**  |

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


### variable etaDM

```
double etaDM;
```


### variable isSelfConj

```
bool isSelfConj;
```


-------------------------------

Updated on 2025-02-12 at 16:10:32 +0000