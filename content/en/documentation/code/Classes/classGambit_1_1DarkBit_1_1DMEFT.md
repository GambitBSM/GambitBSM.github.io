---
title: "class Gambit::DarkBit::DMEFT"

description: "[No description available]"

---

# class Gambit::DarkBit::DMEFT



[No description available]

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[DMEFT](/documentation/code/classes/classgambit_1_1darkbit_1_1dmeft/#function-gambitdarkbitdmeft-dmeft)**()<br>Initialize [DMEFT](/documentation/code/classes/classgambit_1_1darkbit_1_1dmeft/) object (branching ratios etc)  |
| | **[~DMEFT](/documentation/code/classes/classgambit_1_1darkbit_1_1dmeft/#function-gambitdarkbitdmeft-dmeft)**() |
| double | **[sv](/documentation/code/classes/classgambit_1_1darkbit_1_1dmeft/#function-gambitdarkbitdmeft-sv)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) channel, [DecayTable](/documentation/code/classes/classgambit_1_1decaytable/) & tbl, double(*)([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) &, std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) > &, std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) > &, double &, const [DecayTable](/documentation/code/classes/classgambit_1_1decaytable/) &) sigmav, double v_rel) |

## Public Functions Documentation

### function DMEFT

```
inline DMEFT()
```

Initialize [DMEFT](/documentation/code/classes/classgambit_1_1darkbit_1_1dmeft/) object (branching ratios etc) 

### function ~DMEFT

```
inline ~DMEFT()
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

Updated on 2022-09-08 at 02:00:48 +0000