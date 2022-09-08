---
title: "class Gambit::DarkBit::SolarModel"

description: "[No description available]"

---

# class Gambit::DarkBit::SolarModel



[No description available]

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[SolarModel](/documentation/code/classes/classgambit_1_1darkbit_1_1solarmodel/)**() |
| | **[SolarModel](/documentation/code/classes/classgambit_1_1darkbit_1_1solarmodel/)**(std::string file) |
| | **[~SolarModel](/documentation/code/classes/classgambit_1_1darkbit_1_1solarmodel/)**() |
| [SolarModel](/documentation/code/classes/classgambit_1_1darkbit_1_1solarmodel/) & | **[operator=](/documentation/code/classes/classgambit_1_1darkbit_1_1solarmodel/)**([SolarModel](/documentation/code/classes/classgambit_1_1darkbit_1_1solarmodel/) && model) |
| | **[SolarModel](/documentation/code/classes/classgambit_1_1darkbit_1_1solarmodel/)**(const [SolarModel](/documentation/code/classes/classgambit_1_1darkbit_1_1solarmodel/) & ) =delete |
| [SolarModel](/documentation/code/classes/classgambit_1_1darkbit_1_1solarmodel/) | **[operator=](/documentation/code/classes/classgambit_1_1darkbit_1_1solarmodel/)**(const [SolarModel](/documentation/code/classes/classgambit_1_1darkbit_1_1solarmodel/) & ) =delete |
| double | **[kappa_squared](/documentation/code/classes/classgambit_1_1darkbit_1_1solarmodel/)**(double r) |
| double | **[temperature_in_keV](/documentation/code/classes/classgambit_1_1darkbit_1_1solarmodel/)**(double r) |
| double | **[omega_pl_squared](/documentation/code/classes/classgambit_1_1darkbit_1_1solarmodel/)**(double r) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| double | **[r_lo](/documentation/code/classes/classgambit_1_1darkbit_1_1solarmodel/)**  |
| double | **[r_hi](/documentation/code/classes/classgambit_1_1darkbit_1_1solarmodel/)**  |

## Public Functions Documentation

### function SolarModel

```
SolarModel()
```


### function SolarModel

```
SolarModel(
    std::string file
)
```


### function ~SolarModel

```
~SolarModel()
```


### function operator=

```
SolarModel & operator=(
    SolarModel && model
)
```


### function SolarModel

```
SolarModel(
    const SolarModel & 
) =delete
```


### function operator=

```
SolarModel operator=(
    const SolarModel & 
) =delete
```


### function kappa_squared

```
double kappa_squared(
    double r
)
```


### function temperature_in_keV

```
double temperature_in_keV(
    double r
)
```


### function omega_pl_squared

```
double omega_pl_squared(
    double r
)
```


## Public Attributes Documentation

### variable r_lo

```
double r_lo;
```


### variable r_hi

```
double r_hi;
```


-------------------------------

Updated on 2022-09-08 at 01:05:17 +0000