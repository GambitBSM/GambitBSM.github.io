---
title: "class Gambit::Models::DMsimpVectorMedDiracDMModel"
description: "Simple DMsimpVectorMedDiracDM model object. "

---

# class Gambit::Models::DMsimpVectorMedDiracDMModel



Simple DMsimpVectorMedDiracDM model object. 


`#include <DMsimpVectorMedDiracDMSimpleSpec.hpp>`

Inherits from [Gambit::SLHAeaModel](/documentation/code/classes/classgambit_1_1slhaeamodel/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[DMsimpVectorMedDiracDMModel](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormeddiracdmmodel/#function-dmsimpvectormeddiracdmmodel)**(const [SLHAstruct](/documentation/code/namespaces/namespacegambit/#typedef-slhastruct) & input)<br>Constructors.  |
| double | **[get_gVXd](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormeddiracdmmodel/#function-get-gvxd)**() const<br>Getters for DMsimpVectorMedDiracDM information.  |
| double | **[get_gAXd](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormeddiracdmmodel/#function-get-gaxd)**() const |
| double | **[get_gVq](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormeddiracdmmodel/#function-get-gvq)**() const |
| double | **[get_vev](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormeddiracdmmodel/#function-get-vev)**() const |
| double | **[get_g1](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormeddiracdmmodel/#function-get-g1)**() const |
| double | **[get_g2](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormeddiracdmmodel/#function-get-g2)**() const |
| double | **[get_g3](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormeddiracdmmodel/#function-get-g3)**() const |
| double | **[get_sinW2](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormeddiracdmmodel/#function-get-sinw2)**() const |
| double | **[get_Yd](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormeddiracdmmodel/#function-get-yd)**(int i, int j) const |
| double | **[get_Yu](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormeddiracdmmodel/#function-get-yu)**(int i, int j) const |
| double | **[get_Ye](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormeddiracdmmodel/#function-get-ye)**(int i, int j) const |
| double | **[get_h0_1PoleMass](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormeddiracdmmodel/#function-get-h0-1polemass)**() const |
| double | **[get_h0_1PoleMass_1srd_low](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormeddiracdmmodel/#function-get-h0-1polemass-1srd-low)**() const |
| double | **[get_h0_1PoleMass_1srd_high](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormeddiracdmmodel/#function-get-h0-1polemass-1srd-high)**() const |
| double | **[get_XdPoleMass](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormeddiracdmmodel/#function-get-xdpolemass)**() const |
| double | **[get_XdPoleMass_1srd_low](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormeddiracdmmodel/#function-get-xdpolemass-1srd-low)**() const |
| double | **[get_XdPoleMass_1srd_high](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormeddiracdmmodel/#function-get-xdpolemass-1srd-high)**() const |
| double | **[get_Y1PoleMass](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormeddiracdmmodel/#function-get-y1polemass)**() const |
| double | **[get_Y1PoleMass_1srd_low](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormeddiracdmmodel/#function-get-y1polemass-1srd-low)**() const |
| double | **[get_Y1PoleMass_1srd_high](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormeddiracdmmodel/#function-get-y1polemass-1srd-high)**() const |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| double | **[default_uncert](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormeddiracdmmodel/#variable-default-uncert)** <br>Default uncertainty.  |

## Additional inherited members

**Public Functions inherited from [Gambit::SLHAeaModel](/documentation/code/classes/classgambit_1_1slhaeamodel/)**

|                | Name           |
| -------------- | -------------- |
| | **[SLHAeaModel](/documentation/code/classes/classgambit_1_1slhaeamodel/#function-slhaeamodel)**()<br>Constructors.  |
| | **[SLHAeaModel](/documentation/code/classes/classgambit_1_1slhaeamodel/#function-slhaeamodel)**(const SLHAea::Coll & input)<br>Constructor via SLHAea object.  |
| int | **[slha_version](/documentation/code/classes/classgambit_1_1slhaeamodel/#function-slha-version)**() const<br>Get the SLHA version of the internal SLHAea object.  |
| const SLHAea::Coll & | **[get_slhaea](/documentation/code/classes/classgambit_1_1slhaeamodel/#function-get-slhaea)**() const<br>Get the internal SLHAea object.  |
| const std::map< int, int > & | **[PDG_translator](/documentation/code/classes/classgambit_1_1slhaeamodel/#function-pdg-translator)**() const<br>PDG code translation map, for special cases where an SLHA file has been read in and the PDG codes changed.  |
| double | **[getdata](/documentation/code/classes/classgambit_1_1slhaeamodel/#function-getdata)**(const std::string & block, int index) const<br>Helper functions to do error checking for SLHAea object contents.  |
| double | **[getdata](/documentation/code/classes/classgambit_1_1slhaeamodel/#function-getdata)**(const std::string & block, int i, int j) const<br>Two indices.  |
| bool | **[checkdata](/documentation/code/classes/classgambit_1_1slhaeamodel/#function-checkdata)**(const std::string & block, int index) const |

**Protected Attributes inherited from [Gambit::SLHAeaModel](/documentation/code/classes/classgambit_1_1slhaeamodel/)**

|                | Name           |
| -------------- | -------------- |
| SLHAea::Coll | **[data](/documentation/code/classes/classgambit_1_1slhaeamodel/#variable-data)** <br>SLHAea object.  |
| int | **[wrapped_slha_version](/documentation/code/classes/classgambit_1_1slhaeamodel/#variable-wrapped-slha-version)** <br>SLHA version of SLHAea object.  |
| std::map< int, int > | **[PDG_translation_map](/documentation/code/classes/classgambit_1_1slhaeamodel/#variable-pdg-translation-map)** <br>PDG translation map (e.g. from SLHA1 to SLHA2 for MSSMskeleton)  |


## Public Functions Documentation

### function DMsimpVectorMedDiracDMModel

```
inline DMsimpVectorMedDiracDMModel(
    const SLHAstruct & input
)
```

Constructors. 

### function get_gVXd

```
inline double get_gVXd() const
```

Getters for DMsimpVectorMedDiracDM information. 

### function get_gAXd

```
inline double get_gAXd() const
```


### function get_gVq

```
inline double get_gVq() const
```


### function get_vev

```
inline double get_vev() const
```


### function get_g1

```
inline double get_g1() const
```


### function get_g2

```
inline double get_g2() const
```


### function get_g3

```
inline double get_g3() const
```


### function get_sinW2

```
inline double get_sinW2() const
```


### function get_Yd

```
inline double get_Yd(
    int i,
    int j
) const
```


### function get_Yu

```
inline double get_Yu(
    int i,
    int j
) const
```


### function get_Ye

```
inline double get_Ye(
    int i,
    int j
) const
```


### function get_h0_1PoleMass

```
inline double get_h0_1PoleMass() const
```


### function get_h0_1PoleMass_1srd_low

```
inline double get_h0_1PoleMass_1srd_low() const
```


### function get_h0_1PoleMass_1srd_high

```
inline double get_h0_1PoleMass_1srd_high() const
```


### function get_XdPoleMass

```
inline double get_XdPoleMass() const
```


### function get_XdPoleMass_1srd_low

```
inline double get_XdPoleMass_1srd_low() const
```


### function get_XdPoleMass_1srd_high

```
inline double get_XdPoleMass_1srd_high() const
```


### function get_Y1PoleMass

```
inline double get_Y1PoleMass() const
```


### function get_Y1PoleMass_1srd_low

```
inline double get_Y1PoleMass_1srd_low() const
```


### function get_Y1PoleMass_1srd_high

```
inline double get_Y1PoleMass_1srd_high() const
```


## Public Attributes Documentation

### variable default_uncert

```
double default_uncert = 0.3;
```

Default uncertainty. 

-------------------------------

Updated on 2025-02-12 at 15:36:39 +0000