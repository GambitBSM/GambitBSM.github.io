---
title: "struct Gambit::ColliderBit::Analysis_ATLAS_13TeV_1LEPStop_36invfb::ClusteringHistory"

description: "[No description available]"

---

# struct Gambit::ColliderBit::Analysis_ATLAS_13TeV_1LEPStop_36invfb::ClusteringHistory



[No description available]

Inherits from FJNS::PseudoJet::UserInfoBase

## Public Classes

|                | Name           |
| -------------- | -------------- |
| struct | **[Step](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysis__atlas__13tev__1lepstop__36invfb_1_1clusteringhistory_1_1step/)**  |

## Public Types

|                | Name           |
| -------------- | -------------- |
| enum| **[Status](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysis__atlas__13tev__1lepstop__36invfb_1_1clusteringhistory/#enum-gambitcolliderbitanalysis-atlas-13tev-1lepstop-36invfbclusteringhistory-status)** { GOOD, JET_TOO_SMALL, JET_TOO_LARGE, TOO_MANY_ITERATIONS, NONE} |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| [ClusteringHistory](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysis__atlas__13tev__1lepstop__36invfb_1_1clusteringhistory/) * | **[AddStep](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysis__atlas__13tev__1lepstop__36invfb_1_1clusteringhistory/#function-gambitcolliderbitanalysis-atlas-13tev-1lepstop-36invfbclusteringhistory-addstep)**([ClusteringHistory](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysis__atlas__13tev__1lepstop__36invfb_1_1clusteringhistory/) & history, const [Step](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysis__atlas__13tev__1lepstop__36invfb_1_1clusteringhistory_1_1step/) & step) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| size_t | **[id](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysis__atlas__13tev__1lepstop__36invfb_1_1clusteringhistory/#variable-gambitcolliderbitanalysis-atlas-13tev-1lepstop-36invfbclusteringhistory-id)**  |
| std::vector< [Step](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysis__atlas__13tev__1lepstop__36invfb_1_1clusteringhistory_1_1step/) > | **[steps](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysis__atlas__13tev__1lepstop__36invfb_1_1clusteringhistory/#variable-gambitcolliderbitanalysis-atlas-13tev-1lepstop-36invfbclusteringhistory-steps)**  |

## Public Types Documentation

### enum Status

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| GOOD | |   |
| JET_TOO_SMALL | |   |
| JET_TOO_LARGE | |   |
| TOO_MANY_ITERATIONS | |   |
| NONE | |   |




## Public Functions Documentation

### function AddStep

```
static inline ClusteringHistory * AddStep(
    ClusteringHistory & history,
    const Step & step
)
```


## Public Attributes Documentation

### variable id

```
size_t id;
```


### variable steps

```
std::vector< Step > steps;
```


-------------------------------

Updated on 2022-09-08 at 02:00:47 +0000