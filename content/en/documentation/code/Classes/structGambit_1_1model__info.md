---
title: "struct Gambit::model_info"
description: "Helper struct to carry around model information. "

---

# struct Gambit::model_info



Helper struct to carry around model information. 


`#include <yaml_description_database.hpp>`

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[name](/documentation/code/classes/structgambit_1_1model__info/#variable-gambitmodel-info-name)** <br>Model name.  |
| std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) > | **[parameters](/documentation/code/classes/structgambit_1_1model__info/#variable-gambitmodel-info-parameters)** <br>Parameter names.  |
| int | **[nparams](/documentation/code/classes/structgambit_1_1model__info/#variable-gambitmodel-info-nparams)** <br>Number of parameters ( parameters.size() )  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[parent](/documentation/code/classes/structgambit_1_1model__info/#variable-gambitmodel-info-parent)** <br>Parent model name.  |
| std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) > | **[lineage](/documentation/code/classes/structgambit_1_1model__info/#variable-gambitmodel-info-lineage)** <br>Parent and all ancestor models.  |
| std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) > | **[descendants](/documentation/code/classes/structgambit_1_1model__info/#variable-gambitmodel-info-descendants)** <br>All children and later descendants.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[description](/documentation/code/classes/structgambit_1_1model__info/#variable-gambitmodel-info-description)** <br>Full description of capability.  |
| bool | **[has_description](/documentation/code/classes/structgambit_1_1model__info/#variable-gambitmodel-info-has-description)** <br>Flag to check if description is missing.  |

## Public Attributes Documentation

### variable name

```
str name;
```

Model name. 

### variable parameters

```
std::vector< str > parameters;
```

Parameter names. 

### variable nparams

```
int nparams;
```

Number of parameters ( parameters.size() ) 

### variable parent

```
str parent;
```

Parent model name. 

### variable lineage

```
std::vector< str > lineage;
```

Parent and all ancestor models. 

### variable descendants

```
std::vector< str > descendants;
```

All children and later descendants. 

### variable description

```
str description;
```

Full description of capability. 

### variable has_description

```
bool has_description;
```

Flag to check if description is missing. 

-------------------------------

Updated on 2022-09-08 at 01:48:54 +0000