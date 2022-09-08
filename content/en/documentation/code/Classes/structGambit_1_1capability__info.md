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
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[name](/documentation/code/classes/structgambit_1_1capability__info/#variable-gambitcapability-info-name)** <br>Capability name.  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str), std::set< std::pair< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str), [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) > > > | **[modset](/documentation/code/classes/structgambit_1_1capability__info/#variable-gambitcapability-info-modset)** <br>Set of modules and module functions in which capability is used, along with corresponding result types.  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str), std::set< std::pair< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str), [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) > > > | **[beset](/documentation/code/classes/structgambit_1_1capability__info/#variable-gambitcapability-info-beset)** <br>Set of backends and backend functions in which capability is used, along with corresponding type signatures.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[description](/documentation/code/classes/structgambit_1_1capability__info/#variable-gambitcapability-info-description)** <br>Full description of capability.  |
| bool | **[has_description](/documentation/code/classes/structgambit_1_1capability__info/#variable-gambitcapability-info-has-description)** <br>Flag to check if description is missing.  |

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

Updated on 2022-09-08 at 01:48:53 +0000