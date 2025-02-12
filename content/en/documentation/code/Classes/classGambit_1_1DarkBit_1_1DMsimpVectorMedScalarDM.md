---
title: "class Gambit::DarkBit::DMsimpVectorMedScalarDM"

description: "[No description available]"

---

# class Gambit::DarkBit::DMsimpVectorMedScalarDM



[No description available]

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[DMsimpVectorMedScalarDM](/documentation/code/classes/classgambit_1_1darkbit_1_1dmsimpvectormedscalardm/#function-dmsimpvectormedscalardm)**()<br>Initialize [DMsimpVectorMedScalarDM](/documentation/code/classes/classgambit_1_1darkbit_1_1dmsimpvectormedscalardm/) object (branching ratios etc)  |
| | **[~DMsimpVectorMedScalarDM](/documentation/code/classes/classgambit_1_1darkbit_1_1dmsimpvectormedscalardm/#function-dmsimpvectormedscalardm)**() |
| double | **[sv](/documentation/code/classes/classgambit_1_1darkbit_1_1dmsimpvectormedscalardm/#function-sv)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) channel, [DecayTable](/documentation/code/classes/classgambit_1_1decaytable/) & tbl, double(*)([str](/documentation/code/namespaces/namespacegambit/#typedef-str) &, std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > &, std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > &, double &, const [DecayTable](/documentation/code/classes/classgambit_1_1decaytable/) &) sigmav, double v_rel) |

## Public Functions Documentation

### function DMsimpVectorMedScalarDM

```
inline DMsimpVectorMedScalarDM()
```

Initialize [DMsimpVectorMedScalarDM](/documentation/code/classes/classgambit_1_1darkbit_1_1dmsimpvectormedscalardm/) object (branching ratios etc) 

### function ~DMsimpVectorMedScalarDM

```
inline ~DMsimpVectorMedScalarDM()
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