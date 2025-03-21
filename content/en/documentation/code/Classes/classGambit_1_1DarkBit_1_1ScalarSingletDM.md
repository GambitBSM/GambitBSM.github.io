---
title: "class Gambit::DarkBit::ScalarSingletDM"

description: "[No description available]"

---

# class Gambit::DarkBit::ScalarSingletDM



[No description available]

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[ScalarSingletDM](/documentation/code/classes/classgambit_1_1darkbit_1_1scalarsingletdm/#function-scalarsingletdm)**([TH_ProcessCatalog](/documentation/code/classes/structgambit_1_1darkbit_1_1th__processcatalog/) *const catalog, double gammaH, double vev, double alpha_strong, double vSigma_s)<br>Initialize SingletDM object (branching ratios etc)  |
| | **[~ScalarSingletDM](/documentation/code/classes/classgambit_1_1darkbit_1_1scalarsingletdm/#function-scalarsingletdm)**() |
| double | **[Dh2](/documentation/code/classes/classgambit_1_1darkbit_1_1scalarsingletdm/#function-dh2)**(double s)<br>Helper function (Breit-Wigner)  |
| double | **[sv](/documentation/code/classes/classgambit_1_1darkbit_1_1scalarsingletdm/#function-sv)**(std::string channel, double lambda, double mass, double v)<br>Returns <sigma v> in cm3/s for given channel, velocity and model parameters.  |
| double | **[sv_WW](/documentation/code/classes/classgambit_1_1darkbit_1_1scalarsingletdm/#function-sv-ww)**(double lambda, double mass, double v) |
| double | **[sv_ZZ](/documentation/code/classes/classgambit_1_1darkbit_1_1scalarsingletdm/#function-sv-zz)**(double lambda, double mass, double v) |
| double | **[sv_ff](/documentation/code/classes/classgambit_1_1darkbit_1_1scalarsingletdm/#function-sv-ff)**(double lambda, double mass, double v, double mf, bool is_quark) |
| double | **[sv_hh](/documentation/code/classes/classgambit_1_1darkbit_1_1scalarsingletdm/#function-sv-hh)**(double lambda, double mass, double v)<br>Annihilation into hh.  |

## Public Functions Documentation

### function ScalarSingletDM

```
inline ScalarSingletDM(
    TH_ProcessCatalog *const catalog,
    double gammaH,
    double vev,
    double alpha_strong,
    double vSigma_s
)
```

Initialize SingletDM object (branching ratios etc) 

### function ~ScalarSingletDM

```
inline ~ScalarSingletDM()
```


### function Dh2

```
inline double Dh2(
    double s
)
```

Helper function (Breit-Wigner) 

### function sv

```
inline double sv(
    std::string channel,
    double lambda,
    double mass,
    double v
)
```

Returns <sigma v> in cm3/s for given channel, velocity and model parameters. 

channel: bb, tautau, mumu, ss, cc, tt, gg, gammagamma, Zgamma, WW, ZZ, hh 


### function sv_WW

```
inline double sv_WW(
    double lambda,
    double mass,
    double v
)
```


### function sv_ZZ

```
inline double sv_ZZ(
    double lambda,
    double mass,
    double v
)
```


### function sv_ff

```
inline double sv_ff(
    double lambda,
    double mass,
    double v,
    double mf,
    bool is_quark
)
```


### function sv_hh

```
inline double sv_hh(
    double lambda,
    double mass,
    double v
)
```

Annihilation into hh. 

-------------------------------

Updated on 2025-02-12 at 16:10:32 +0000