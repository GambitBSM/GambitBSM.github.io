---
title: "class Gambit::SLHAeaModel"
description: "Skeleton model class which interacts with an SLHAea object. "

---

# class Gambit::SLHAeaModel



Skeleton "model" class which interacts with an SLHAea object. 


`#include <SLHASimpleSpec.hpp>`

Inherited by [Gambit::MSSMea](/documentation/code/classes/classgambit_1_1mssmea/), [Gambit::SMea](/documentation/code/classes/classgambit_1_1smea/)

## Public Functions

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

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| SLHAea::Coll | **[data](/documentation/code/classes/classgambit_1_1slhaeamodel/#variable-data)** <br>SLHAea object.  |
| int | **[wrapped_slha_version](/documentation/code/classes/classgambit_1_1slhaeamodel/#variable-wrapped-slha-version)** <br>SLHA version of SLHAea object.  |
| std::map< int, int > | **[PDG_translation_map](/documentation/code/classes/classgambit_1_1slhaeamodel/#variable-pdg-translation-map)** <br>PDG translation map (e.g. from SLHA1 to SLHA2 for MSSMskeleton)  |

## Public Functions Documentation

### function SLHAeaModel

```
SLHAeaModel()
```

Constructors. 

Member functions for [SLHAeaModel](/documentation/code/classes/classgambit_1_1slhaeamodel/) class.

Default Constructor 


### function SLHAeaModel

```
SLHAeaModel(
    const SLHAea::Coll & input
)
```

Constructor via SLHAea object. 

### function slha_version

```
int slha_version() const
```

Get the SLHA version of the internal SLHAea object. 

### function get_slhaea

```
const SLHAea::Coll & get_slhaea() const
```

Get the internal SLHAea object. 

Get reference to internal SLHAea object. 


### function PDG_translator

```
const std::map< int, int > & PDG_translator() const
```

PDG code translation map, for special cases where an SLHA file has been read in and the PDG codes changed. 

### function getdata

```
double getdata(
    const std::string & block,
    int index
) const
```

Helper functions to do error checking for SLHAea object contents. 

One index 


### function getdata

```
double getdata(
    const std::string & block,
    int i,
    int j
) const
```

Two indices. 

### function checkdata

```
bool checkdata(
    const std::string & block,
    int index
) const
```


## Protected Attributes Documentation

### variable data

```
SLHAea::Coll data;
```

SLHAea object. 

### variable wrapped_slha_version

```
int wrapped_slha_version;
```

SLHA version of SLHAea object. 

### variable PDG_translation_map

```
std::map< int, int > PDG_translation_map;
```

PDG translation map (e.g. from SLHA1 to SLHA2 for MSSMskeleton) 

-------------------------------

Updated on 2022-09-08 at 03:41:57 +0000