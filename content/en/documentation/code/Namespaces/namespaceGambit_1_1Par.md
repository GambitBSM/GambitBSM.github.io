---
title: "namespace Gambit::Par"
description: "List of parameter types used to classify spectrum contents. "

---

# namespace Gambit::Par

List of parameter types used to classify spectrum contents. 

## Types

|                | Name           |
| -------------- | -------------- |
| enum| **[Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags)** { Pole_Mass = 0, Pole_Mass_1srd_high, Pole_Mass_1srd_low, Pole_Mixing, mass4 = Pole_Mixing+1, mass3, mass2, mass1, dimensionless, mass_eigenstate} |

## Functions

|                | Name           |
| -------------- | -------------- |
| std::vector< [Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) > | **[get_all](/documentation/code/namespaces/namespacegambit_1_1par/#function-get-all)**() |
| std::map< [Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags), std::string > | **[fill_map](/documentation/code/namespaces/namespacegambit_1_1par/#function-fill-map)**()<br>Map from enum value to string, for error messages.  |

## Attributes

|                | Name           |
| -------------- | -------------- |
| const std::map< [Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags), std::string > | **[toString](/documentation/code/namespaces/namespacegambit_1_1par/#variable-tostring)**  |

## Types Documentation

### enum Tags

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Pole_Mass | 0| Ex-"Phys" tags.   |
| Pole_Mass_1srd_high | |   |
| Pole_Mass_1srd_low | |   |
| Pole_Mixing | |   |
| mass4 | Pole_Mixing+1| Ex-"Running" tags.   |
| mass3 | |   |
| mass2 | |   |
| mass1 | |   |
| dimensionless | |   |
| mass_eigenstate | |   |





## Functions Documentation

### function get_all

```
inline std::vector< Tags > get_all()
```


### function fill_map

```
static std::map< Tags, std::string > fill_map()
```

Map from enum value to string, for error messages. 


## Attributes Documentation

### variable toString

```
static const std::map< Tags, std::string > toString = fill_map();
```





-------------------------------

Updated on 2025-02-12 at 16:10:32 +0000