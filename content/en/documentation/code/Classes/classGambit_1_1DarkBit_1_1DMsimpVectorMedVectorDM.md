---
title: "class Gambit::DarkBit::DMsimpVectorMedVectorDM"

description: "[No description available]"

---

# class Gambit::DarkBit::DMsimpVectorMedVectorDM



[No description available]

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[DMsimpVectorMedVectorDM](/documentation/code/classes/classgambit_1_1darkbit_1_1dmsimpvectormedvectordm/#function-dmsimpvectormedvectordm)**()<br>Initialize [DMsimpVectorMedVectorDM](/documentation/code/classes/classgambit_1_1darkbit_1_1dmsimpvectormedvectordm/) object (branching ratios etc)  |
| | **[~DMsimpVectorMedVectorDM](/documentation/code/classes/classgambit_1_1darkbit_1_1dmsimpvectormedvectordm/#function-dmsimpvectormedvectordm)**() |
| double | **[sv](/documentation/code/classes/classgambit_1_1darkbit_1_1dmsimpvectormedvectordm/#function-sv)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) channel, [DecayTable](/documentation/code/classes/classgambit_1_1decaytable/) & tbl, double(*)([str](/documentation/code/namespaces/namespacegambit/#typedef-str) &, std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > &, std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > &, double &, const [DecayTable](/documentation/code/classes/classgambit_1_1decaytable/) &) sigmav, double v_rel) |

## Public Functions Documentation

### function DMsimpVectorMedVectorDM

```
inline DMsimpVectorMedVectorDM()
```

Initialize [DMsimpVectorMedVectorDM](/documentation/code/classes/classgambit_1_1darkbit_1_1dmsimpvectormedvectordm/) object (branching ratios etc) 

### function ~DMsimpVectorMedVectorDM

```
inline ~DMsimpVectorMedVectorDM()
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

Updated on 2025-02-12 at 16:10:32 +0000