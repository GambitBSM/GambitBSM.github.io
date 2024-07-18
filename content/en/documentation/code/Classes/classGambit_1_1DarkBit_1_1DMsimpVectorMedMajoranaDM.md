---
title: "class Gambit::DarkBit::DMsimpVectorMedMajoranaDM"

description: "[No description available]"

---

# class Gambit::DarkBit::DMsimpVectorMedMajoranaDM



[No description available]

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[DMsimpVectorMedMajoranaDM](/documentation/code/classes/classgambit_1_1darkbit_1_1dmsimpvectormedmajoranadm/#function-dmsimpvectormedmajoranadm)**()<br>Initialize [DMsimpVectorMedMajoranaDM](/documentation/code/classes/classgambit_1_1darkbit_1_1dmsimpvectormedmajoranadm/) object (branching ratios etc)  |
| | **[~DMsimpVectorMedMajoranaDM](/documentation/code/classes/classgambit_1_1darkbit_1_1dmsimpvectormedmajoranadm/#function-dmsimpvectormedmajoranadm)**() |
| double | **[sv](/documentation/code/classes/classgambit_1_1darkbit_1_1dmsimpvectormedmajoranadm/#function-sv)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) channel, [DecayTable](/documentation/code/classes/classgambit_1_1decaytable/) & tbl, double(*)([str](/documentation/code/namespaces/namespacegambit/#typedef-str) &, std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > &, std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > &, double &, const [DecayTable](/documentation/code/classes/classgambit_1_1decaytable/) &) sigmav, double v_rel) |

## Public Functions Documentation

### function DMsimpVectorMedMajoranaDM

```
inline DMsimpVectorMedMajoranaDM()
```

Initialize [DMsimpVectorMedMajoranaDM](/documentation/code/classes/classgambit_1_1darkbit_1_1dmsimpvectormedmajoranadm/) object (branching ratios etc) 

### function ~DMsimpVectorMedMajoranaDM

```
inline ~DMsimpVectorMedMajoranaDM()
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

Updated on 2024-07-18 at 13:53:31 +0000