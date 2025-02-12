---
title: "class Gambit::DarkBit::SubGeVDM_fermion"
description: "Helper function (width rescaled for RD calculations) "

---

# class Gambit::DarkBit::SubGeVDM_fermion



Helper function (width rescaled for RD calculations) 

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[SubGeVDM_fermion](/documentation/code/classes/classgambit_1_1darkbit_1_1subgevdm__fermion/#function-subgevdm-fermion)**([TH_ProcessCatalog](/documentation/code/classes/structgambit_1_1darkbit_1_1th__processcatalog/) *const catalog, double gammaAp)<br>Initialize [SubGeVDM_fermion](/documentation/code/classes/classgambit_1_1darkbit_1_1subgevdm__fermion/) object (branching ratios etc)  |
| | **[~SubGeVDM_fermion](/documentation/code/classes/classgambit_1_1darkbit_1_1subgevdm__fermion/#function-subgevdm-fermion)**() |
| double | **[DAp2](/documentation/code/classes/classgambit_1_1darkbit_1_1subgevdm__fermion/#function-dap2)**(double s)<br>Helper function (Breit-Wigner, rescaled close to resonance)  |
| double | **[sv](/documentation/code/classes/classgambit_1_1darkbit_1_1subgevdm__fermion/#function-sv)**(std::string channel, double gDM, double gSM, double mass, double v, bool smooth) |
| double | **[sv_ff](/documentation/code/classes/classgambit_1_1darkbit_1_1subgevdm__fermion/#function-sv-ff)**(double gDM, double gSM, double mass, double v, double mf, double charge, int colour) |
| double | **[sv_ApAp](/documentation/code/classes/classgambit_1_1darkbit_1_1subgevdm__fermion/#function-sv-apap)**(double gDM, double mass, double v)<br>Annihilation into ApAp.  |

## Public Functions Documentation

### function SubGeVDM_fermion

```
inline SubGeVDM_fermion(
    TH_ProcessCatalog *const catalog,
    double gammaAp
)
```

Initialize [SubGeVDM_fermion](/documentation/code/classes/classgambit_1_1darkbit_1_1subgevdm__fermion/) object (branching ratios etc) 

### function ~SubGeVDM_fermion

```
inline ~SubGeVDM_fermion()
```


### function DAp2

```
inline double DAp2(
    double s
)
```

Helper function (Breit-Wigner, rescaled close to resonance) 

### function sv

```
inline double sv(
    std::string channel,
    double gDM,
    double gSM,
    double mass,
    double v,
    bool smooth
)
```


### function sv_ff

```
inline double sv_ff(
    double gDM,
    double gSM,
    double mass,
    double v,
    double mf,
    double charge,
    int colour
)
```


### function sv_ApAp

```
inline double sv_ApAp(
    double gDM,
    double mass,
    double v
)
```

Annihilation into ApAp. 

-------------------------------

Updated on 2025-02-12 at 16:10:32 +0000