---
title: "class Gambit::Models::DMsimpVectorMedMajoranaDMModel"
description: "Simple DMsimpVectorMedMajoranaDM model object. "

---

# class Gambit::Models::DMsimpVectorMedMajoranaDMModel



Simple DMsimpVectorMedMajoranaDM model object. 


`#include <DMsimpVectorMedMajoranaDMSimpleSpec.hpp>`

Inherits from [Gambit::SLHAeaModel](/documentation/code/classes/classgambit_1_1slhaeamodel/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[DMsimpVectorMedMajoranaDMModel](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormedmajoranadmmodel/#function-dmsimpvectormedmajoranadmmodel)**(const [SLHAstruct](/documentation/code/namespaces/namespacegambit/#typedef-slhastruct) & input)<br>Constructors.  |
| double | **[get_gAXm](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormedmajoranadmmodel/#function-get-gaxm)**() const<br>Getters for DMsimpVectorMedMajoranaDM information.  |
| double | **[get_gVq](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormedmajoranadmmodel/#function-get-gvq)**() const |
| double | **[get_vev](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormedmajoranadmmodel/#function-get-vev)**() const |
| double | **[get_g1](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormedmajoranadmmodel/#function-get-g1)**() const |
| double | **[get_g2](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormedmajoranadmmodel/#function-get-g2)**() const |
| double | **[get_g3](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormedmajoranadmmodel/#function-get-g3)**() const |
| double | **[get_sinW2](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormedmajoranadmmodel/#function-get-sinw2)**() const |
| double | **[get_Yd](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormedmajoranadmmodel/#function-get-yd)**(int i, int j) const |
| double | **[get_Yu](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormedmajoranadmmodel/#function-get-yu)**(int i, int j) const |
| double | **[get_Ye](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormedmajoranadmmodel/#function-get-ye)**(int i, int j) const |
| double | **[get_h0_1PoleMass](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormedmajoranadmmodel/#function-get-h0-1polemass)**() const |
| double | **[get_h0_1PoleMass_1srd_low](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormedmajoranadmmodel/#function-get-h0-1polemass-1srd-low)**() const |
| double | **[get_h0_1PoleMass_1srd_high](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormedmajoranadmmodel/#function-get-h0-1polemass-1srd-high)**() const |
| double | **[get_XmPoleMass](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormedmajoranadmmodel/#function-get-xmpolemass)**() const |
| double | **[get_XmPoleMass_1srd_low](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormedmajoranadmmodel/#function-get-xmpolemass-1srd-low)**() const |
| double | **[get_XmPoleMass_1srd_high](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormedmajoranadmmodel/#function-get-xmpolemass-1srd-high)**() const |
| double | **[get_Y1PoleMass](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormedmajoranadmmodel/#function-get-y1polemass)**() const |
| double | **[get_Y1PoleMass_1srd_low](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormedmajoranadmmodel/#function-get-y1polemass-1srd-low)**() const |
| double | **[get_Y1PoleMass_1srd_high](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormedmajoranadmmodel/#function-get-y1polemass-1srd-high)**() const |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| double | **[default_uncert](/documentation/code/classes/classgambit_1_1models_1_1dmsimpvectormedmajoranadmmodel/#variable-default-uncert)** <br>Default uncertainty.  |

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

### function DMsimpVectorMedMajoranaDMModel

```
inline DMsimpVectorMedMajoranaDMModel(
    const SLHAstruct & input
)
```

Constructors. 

### function get_gAXm

```
inline double get_gAXm() const
```

Getters for DMsimpVectorMedMajoranaDM information. 

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


### function get_XmPoleMass

```
inline double get_XmPoleMass() const
```


### function get_XmPoleMass_1srd_low

```
inline double get_XmPoleMass_1srd_low() const
```


### function get_XmPoleMass_1srd_high

```
inline double get_XmPoleMass_1srd_high() const
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

Updated on 2025-02-12 at 16:10:32 +0000