---
title: "struct Gambit::capability_info"
description: "Helper struct to carry around capability information. "

---

# struct Gambit::capability_info



Helper struct to carry around capability information. 


`#include <yaml_description_database.hpp>`

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[name](/documentation/code/classes/structgambit_1_1capability__info/#variable-name)** <br>Capability name.  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), std::set< std::pair< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > > > | **[modset](/documentation/code/classes/structgambit_1_1capability__info/#variable-modset)** <br>Set of modules and module functions in which capability is used, along with corresponding result types.  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), std::set< std::pair< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > > > | **[beset](/documentation/code/classes/structgambit_1_1capability__info/#variable-beset)** <br>Set of backends and backend functions in which capability is used, along with corresponding type signatures.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[description](/documentation/code/classes/structgambit_1_1capability__info/#variable-description)** <br>Full description of capability.  |
| bool | **[has_description](/documentation/code/classes/structgambit_1_1capability__info/#variable-has-description)** <br>Flag to check if description is missing.  |

## Public Attributes Documentation

### variable name

```
str name;
```

Capability name. 

### variable modset

```
std::map< str, std::set< std::pair< str, str > > > modset;
```

Set of modules and module functions in which capability is used, along with corresponding result types. 

### variable beset

```
std::map< str, std::set< std::pair< str, str > > > beset;
```

Set of backends and backend functions in which capability is used, along with corresponding type signatures. 

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

Updated on 2025-02-12 at 16:10:30 +0000