---
title: "class Gambit::DarkBit::DMsimpVectorMedDiracDM"

description: "[No description available]"

---

# class Gambit::DarkBit::DMsimpVectorMedDiracDM



[No description available]

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[DMsimpVectorMedDiracDM](/documentation/code/classes/classgambit_1_1darkbit_1_1dmsimpvectormeddiracdm/#function-dmsimpvectormeddiracdm)**()<br>Initialize [DMsimpVectorMedDiracDM](/documentation/code/classes/classgambit_1_1darkbit_1_1dmsimpvectormeddiracdm/) object (branching ratios etc)  |
| | **[~DMsimpVectorMedDiracDM](/documentation/code/classes/classgambit_1_1darkbit_1_1dmsimpvectormeddiracdm/#function-dmsimpvectormeddiracdm)**() |
| double | **[sv](/documentation/code/classes/classgambit_1_1darkbit_1_1dmsimpvectormeddiracdm/#function-sv)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) channel, [DecayTable](/documentation/code/classes/classgambit_1_1decaytable/) & tbl, double(*)([str](/documentation/code/namespaces/namespacegambit/#typedef-str) &, std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > &, std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > &, double &, const [DecayTable](/documentation/code/classes/classgambit_1_1decaytable/) &) sigmav, double v_rel) |

## Public Functions Documentation

### function DMsimpVectorMedDiracDM

```
inline DMsimpVectorMedDiracDM()
```

Initialize [DMsimpVectorMedDiracDM](/documentation/code/classes/classgambit_1_1darkbit_1_1dmsimpvectormeddiracdm/) object (branching ratios etc) 

### function ~DMsimpVectorMedDiracDM

```
inline ~DMsimpVectorMedDiracDM()
```


### function sv

```
inline double sv(
    str channel,
    DecayTable & tbl,
    double(*)(str &, std::vector< str > &, std::vector< str > &, double &, const DecayTable &) sigmav,
    double v_rel
)
```


Returns sigma*v for a given channel.


-------------------------------

Updated on 2025-02-12 at 15:36:39 +0000