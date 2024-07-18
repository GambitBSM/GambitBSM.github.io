---
title: "struct Gambit::DRes::Rule"
description: "Base rule for resolution of dependencies and backend requirements. "

---

# struct Gambit::DRes::Rule



Base rule for resolution of dependencies and backend requirements. 


`#include <rule.hpp>`

Inherited by [Gambit::DRes::BackendRule](/documentation/code/classes/structgambit_1_1dres_1_1backendrule/), [Gambit::DRes::ModuleRule](/documentation/code/classes/structgambit_1_1dres_1_1modulerule/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| bool | **[base_antecedent_matches](/documentation/code/classes/structgambit_1_1dres_1_1rule/#function-base-antecedent-matches)**([functor](/documentation/code/classes/classgambit_1_1functor/) * f, const [Utils::type_equivalency](/documentation/code/classes/structgambit_1_1utils_1_1type__equivalency/) & te) const<br>True if and only if the passed functor matches the 'if' part of a rule.  |
| bool | **[base_consequent_matches](/documentation/code/classes/structgambit_1_1dres_1_1rule/#function-base-consequent-matches)**([functor](/documentation/code/classes/classgambit_1_1functor/) * f, const [Utils::type_equivalency](/documentation/code/classes/structgambit_1_1utils_1_1type__equivalency/) & te) const<br>True if and only if the passed functor matches the 'then' part of a rule.  |
| | **[Rule](/documentation/code/classes/structgambit_1_1dres_1_1rule/#function-rule)**()<br>Default constructor. Sets all fields empty.  |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| bool | **[has_if](/documentation/code/classes/structgambit_1_1dres_1_1rule/#variable-has-if)** <br>[Rule](/documentation/code/classes/structgambit_1_1dres_1_1rule/) has an antecedent ('if' clause)  |
| bool | **[has_then](/documentation/code/classes/structgambit_1_1dres_1_1rule/#variable-has-then)** <br>[Rule](/documentation/code/classes/structgambit_1_1dres_1_1rule/) has a consequent ('then' clause)  |
| YAML::Node | **[yaml](/documentation/code/classes/structgambit_1_1dres_1_1rule/#variable-yaml)** <br>The original [YAML](/documentation/code/namespaces/namespaceyaml/) (if any) from which this rule was derived.  |
| std::string | **[capability](/documentation/code/classes/structgambit_1_1dres_1_1rule/#variable-capability)** <br>Capability field targeted by the rule.  |
| bool | **[if_capability](/documentation/code/classes/structgambit_1_1dres_1_1rule/#variable-if-capability)** <br>Capability field appears in 'if' clause.  |
| bool | **[then_capability](/documentation/code/classes/structgambit_1_1dres_1_1rule/#variable-then-capability)** <br>Capability field appears in 'then' clause.  |
| std::string | **[type](/documentation/code/classes/structgambit_1_1dres_1_1rule/#variable-type)** <br>Type field targeted by the rule.  |
| bool | **[if_type](/documentation/code/classes/structgambit_1_1dres_1_1rule/#variable-if-type)** <br>Type field appears in 'if' clause.  |
| bool | **[then_type](/documentation/code/classes/structgambit_1_1dres_1_1rule/#variable-then-type)** <br>Type field appears in 'then' clause.  |
| std::string | **[function](/documentation/code/classes/structgambit_1_1dres_1_1rule/#variable-function)** <br>Function field targeted by the rule.  |
| bool | **[if_function](/documentation/code/classes/structgambit_1_1dres_1_1rule/#variable-if-function)** <br>Function field appears in 'if' clause.  |
| bool | **[then_function](/documentation/code/classes/structgambit_1_1dres_1_1rule/#variable-then-function)** <br>Function field appears in 'then' clause.  |
| bool | **[weakrule](/documentation/code/classes/structgambit_1_1dres_1_1rule/#variable-weakrule)** <br>Indicates that rule can be broken.  |
| bool | **[log_matches](/documentation/code/classes/structgambit_1_1dres_1_1rule/#variable-log-matches)** <br>Whether or not to log matches to the rule with functors.  |

## Public Functions Documentation

### function base_antecedent_matches

```
bool base_antecedent_matches(
    functor * f,
    const Utils::type_equivalency & te
) const
```

True if and only if the passed functor matches the 'if' part of a rule. 

True if and only if the passed functor matches the base part of an 'if' part of a rule. 


### function base_consequent_matches

```
bool base_consequent_matches(
    functor * f,
    const Utils::type_equivalency & te
) const
```

True if and only if the passed functor matches the 'then' part of a rule. 

True if and only if the passed functor matches the base part of a 'then' part of a rule. 


### function Rule

```
inline Rule()
```

Default constructor. Sets all fields empty. 

## Public Attributes Documentation

### variable has_if

```
bool has_if;
```

[Rule](/documentation/code/classes/structgambit_1_1dres_1_1rule/) has an antecedent ('if' clause) 

### variable has_then

```
bool has_then;
```

[Rule](/documentation/code/classes/structgambit_1_1dres_1_1rule/) has a consequent ('then' clause) 

### variable yaml

```
YAML::Node yaml;
```

The original [YAML](/documentation/code/namespaces/namespaceyaml/) (if any) from which this rule was derived. 

### variable capability

```
std::string capability;
```

Capability field targeted by the rule. 

### variable if_capability

```
bool if_capability;
```

Capability field appears in 'if' clause. 

### variable then_capability

```
bool then_capability;
```

Capability field appears in 'then' clause. 

### variable type

```
std::string type;
```

Type field targeted by the rule. 

### variable if_type

```
bool if_type;
```

Type field appears in 'if' clause. 

### variable then_type

```
bool then_type;
```

Type field appears in 'then' clause. 

### variable function

```
std::string function;
```

Function field targeted by the rule. 

### variable if_function

```
bool if_function;
```

Function field appears in 'if' clause. 

### variable then_function

```
bool then_function;
```

Function field appears in 'then' clause. 

### variable weakrule

```
bool weakrule;
```

Indicates that rule can be broken. 

### variable log_matches

```
bool log_matches;
```

Whether or not to log matches to the rule with functors. 

-------------------------------

Updated on 2024-07-18 at 13:53:31 +0000