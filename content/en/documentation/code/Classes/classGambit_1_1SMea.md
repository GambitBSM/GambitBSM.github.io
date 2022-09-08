---
title: "class Gambit::SMea"

description: "[No description available]"

---

# class Gambit::SMea



[No description available] [More...](#detailed-description)


`#include <SMSimpleSpec.hpp>`

Inherits from [Gambit::SLHAeaModel](/documentation/code/classes/classgambit_1_1slhaeamodel/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[SMea](/documentation/code/classes/classgambit_1_1smea/#function-smea)**()<br>Constructors.  |
| | **[SMea](/documentation/code/classes/classgambit_1_1smea/#function-smea)**(const SLHAea::Coll & input)<br>Constructor via SLHAea object.  |
| double | **[get_MZ_pole](/documentation/code/classes/classgambit_1_1smea/#function-get-mz-pole)**() const<br>Getters for SM information.  |
| double | **[get_Mtop_pole](/documentation/code/classes/classgambit_1_1smea/#function-get-mtop-pole)**() const |
| double | **[get_MbMb](/documentation/code/classes/classgambit_1_1smea/#function-get-mbmb)**() const |
| double | **[get_McMc](/documentation/code/classes/classgambit_1_1smea/#function-get-mcmc)**() const |
| double | **[get_Mtau_pole](/documentation/code/classes/classgambit_1_1smea/#function-get-mtau-pole)**() const |
| double | **[get_Mmuon_pole](/documentation/code/classes/classgambit_1_1smea/#function-get-mmuon-pole)**() const |
| double | **[get_Melectron_pole](/documentation/code/classes/classgambit_1_1smea/#function-get-melectron-pole)**() const |
| double | **[get_Mnu1_pole](/documentation/code/classes/classgambit_1_1smea/#function-get-mnu1-pole)**() const |
| double | **[get_Mnu2_pole](/documentation/code/classes/classgambit_1_1smea/#function-get-mnu2-pole)**() const |
| double | **[get_Mnu3_pole](/documentation/code/classes/classgambit_1_1smea/#function-get-mnu3-pole)**() const |
| double | **[get_MPhoton_pole](/documentation/code/classes/classgambit_1_1smea/#function-get-mphoton-pole)**() const |
| double | **[get_MGluon_pole](/documentation/code/classes/classgambit_1_1smea/#function-get-mgluon-pole)**() const |
| double | **[get_MPhoton](/documentation/code/classes/classgambit_1_1smea/#function-get-mphoton)**() const |
| double | **[get_MGluon](/documentation/code/classes/classgambit_1_1smea/#function-get-mgluon)**() const |
| double | **[get_MW_pole](/documentation/code/classes/classgambit_1_1smea/#function-get-mw-pole)**() const |
| double | **[get_sinthW2_pole](/documentation/code/classes/classgambit_1_1smea/#function-get-sinthw2-pole)**() const |
| double | **[get_MW_unc](/documentation/code/classes/classgambit_1_1smea/#function-get-mw-unc)**() const |
| double | **[get_md](/documentation/code/classes/classgambit_1_1smea/#function-get-md)**() const<br>Running masses.  |
| double | **[get_mu](/documentation/code/classes/classgambit_1_1smea/#function-get-mu)**() const |
| double | **[get_ms](/documentation/code/classes/classgambit_1_1smea/#function-get-ms)**() const |
| double | **[get_mD](/documentation/code/classes/classgambit_1_1smea/#function-get-md)**(int i) const |
| double | **[get_mU](/documentation/code/classes/classgambit_1_1smea/#function-get-mu)**(int i) const |
| double | **[get_alpha](/documentation/code/classes/classgambit_1_1smea/#function-get-alpha)**() const |
| double | **[get_alphaS](/documentation/code/classes/classgambit_1_1smea/#function-get-alphas)**() const |

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


## Detailed Description

```
class Gambit::SMea;
```


Skeleton "model" class which interacts with an SLHAea object Some common functions defined in base class 

## Public Functions Documentation

### function SMea

```
SMea()
```

Constructors. 

Member functions for [SLHAeaModel](/documentation/code/classes/classgambit_1_1slhaeamodel/) class.

Default Constructor 


### function SMea

```
SMea(
    const SLHAea::Coll & input
)
```

Constructor via SLHAea object. 

### function get_MZ_pole

```
double get_MZ_pole() const
```

Getters for SM information. 

Pole masses 


### function get_Mtop_pole

```
double get_Mtop_pole() const
```


### function get_MbMb

```
double get_MbMb() const
```


### function get_McMc

```
double get_McMc() const
```


### function get_Mtau_pole

```
double get_Mtau_pole() const
```


### function get_Mmuon_pole

```
double get_Mmuon_pole() const
```


### function get_Melectron_pole

```
double get_Melectron_pole() const
```


### function get_Mnu1_pole

```
double get_Mnu1_pole() const
```


### function get_Mnu2_pole

```
double get_Mnu2_pole() const
```


### function get_Mnu3_pole

```
double get_Mnu3_pole() const
```


### function get_MPhoton_pole

```
double get_MPhoton_pole() const
```


### function get_MGluon_pole

```
double get_MGluon_pole() const
```


### function get_MPhoton

```
double get_MPhoton() const
```


### function get_MGluon

```
double get_MGluon() const
```


### function get_MW_pole

```
double get_MW_pole() const
```


### function get_sinthW2_pole

```
double get_sinthW2_pole() const
```


### function get_MW_unc

```
double get_MW_unc() const
```


### function get_md

```
double get_md() const
```

Running masses. 

### function get_mu

```
double get_mu() const
```


### function get_ms

```
double get_ms() const
```


### function get_mD

```
double get_mD(
    int i
) const
```


### function get_mU

```
double get_mU(
    int i
) const
```


### function get_alpha

```
double get_alpha() const
```


### function get_alphaS

```
double get_alphaS() const
```


-------------------------------

Updated on 2022-09-08 at 00:43:00 +0000