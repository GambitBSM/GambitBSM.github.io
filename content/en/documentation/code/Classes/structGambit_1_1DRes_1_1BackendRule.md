---
title: "struct Gambit::DRes::BackendRule"
description: "Derived class rule for resolution of backend requirements. "

---

# struct Gambit::DRes::BackendRule



Derived class rule for resolution of backend requirements. 


`#include <rule.hpp>`

Inherits from [Gambit::DRes::Rule](/documentation/code/classes/structgambit_1_1dres_1_1rule/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| bool | **[antecedent_matches](/documentation/code/classes/structgambit_1_1dres_1_1backendrule/#function-antecedent-matches)**([functor](/documentation/code/classes/classgambit_1_1functor/) * f, const [Utils::type_equivalency](/documentation/code/classes/structgambit_1_1utils_1_1type__equivalency/) & te, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & group_being_resolved) const<br>True if and only if the passed backend functor matches the 'if' part of a rule.  |
| bool | **[consequent_matches](/documentation/code/classes/structgambit_1_1dres_1_1backendrule/#function-consequent-matches)**([functor](/documentation/code/classes/classgambit_1_1functor/) * f, const [Utils::type_equivalency](/documentation/code/classes/structgambit_1_1utils_1_1type__equivalency/) & te) const<br>True if and only if the passed backend functor matches the 'then' part of a rule.  |
| bool | **[allows](/documentation/code/classes/structgambit_1_1dres_1_1backendrule/#function-allows)**([functor](/documentation/code/classes/classgambit_1_1functor/) * f, const [Utils::type_equivalency](/documentation/code/classes/structgambit_1_1utils_1_1type__equivalency/) & te, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & group_being_resolved, bool ignore_if_weak =true) const |
| | **[BackendRule](/documentation/code/classes/structgambit_1_1dres_1_1backendrule/#function-backendrule)**()<br>Default constructor. Sets all fields empty.  |
| bool | **[permits_field](/documentation/code/classes/structgambit_1_1dres_1_1backendrule/#function-permits-field)**(const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & field)<br>Check if a given string is a permitted field of this class.  |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| std::string | **[version](/documentation/code/classes/structgambit_1_1dres_1_1backendrule/#variable-version)** <br>Version field targeted by the rule.  |
| bool | **[if_version](/documentation/code/classes/structgambit_1_1dres_1_1backendrule/#variable-if-version)** <br>Version field appears in 'if' clause.  |
| bool | **[then_version](/documentation/code/classes/structgambit_1_1dres_1_1backendrule/#variable-then-version)** <br>Version field appears in 'then' clause.  |
| std::string | **[backend](/documentation/code/classes/structgambit_1_1dres_1_1backendrule/#variable-backend)** <br>Backend field targeted by the rule.  |
| bool | **[if_backend](/documentation/code/classes/structgambit_1_1dres_1_1backendrule/#variable-if-backend)** <br>Backend field appears in 'if' clause.  |
| bool | **[then_backend](/documentation/code/classes/structgambit_1_1dres_1_1backendrule/#variable-then-backend)** <br>Backend field appears in 'then' clause.  |
| std::string | **[group](/documentation/code/classes/structgambit_1_1dres_1_1backendrule/#variable-group)** <br>Backend group referenced by the rule.  |
| bool | **[if_group](/documentation/code/classes/structgambit_1_1dres_1_1backendrule/#variable-if-group)** <br>Group field appears in 'if' clause.  |

## Additional inherited members

**Public Functions inherited from [Gambit::DRes::Rule](/documentation/code/classes/structgambit_1_1dres_1_1rule/)**

|                | Name           |
| -------------- | -------------- |
| bool | **[base_antecedent_matches](/documentation/code/classes/structgambit_1_1dres_1_1rule/#function-base-antecedent-matches)**([functor](/documentation/code/classes/classgambit_1_1functor/) * f, const [Utils::type_equivalency](/documentation/code/classes/structgambit_1_1utils_1_1type__equivalency/) & te) const<br>True if and only if the passed functor matches the 'if' part of a rule.  |
| bool | **[base_consequent_matches](/documentation/code/classes/structgambit_1_1dres_1_1rule/#function-base-consequent-matches)**([functor](/documentation/code/classes/classgambit_1_1functor/) * f, const [Utils::type_equivalency](/documentation/code/classes/structgambit_1_1utils_1_1type__equivalency/) & te) const<br>True if and only if the passed functor matches the 'then' part of a rule.  |
| | **[Rule](/documentation/code/classes/structgambit_1_1dres_1_1rule/#function-rule)**()<br>Default constructor. Sets all fields empty.  |

**Public Attributes inherited from [Gambit::DRes::Rule](/documentation/code/classes/structgambit_1_1dres_1_1rule/)**

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

### function antecedent_matches

```
bool antecedent_matches(
    functor * f,
    const Utils::type_equivalency & te,
    const str & group_being_resolved
) const
```

True if and only if the passed backend functor matches the 'if' part of a rule. 

### function consequent_matches

```
bool consequent_matches(
    functor * f,
    const Utils::type_equivalency & te
) const
```

True if and only if the passed backend functor matches the 'then' part of a rule. 

### function allows

```
bool allows(
    functor * f,
    const Utils::type_equivalency & te,
    const str & group_being_resolved,
    bool ignore_if_weak =true
) const
```


Whether a backend rule allows a given backend functor or not. 

 Must be true for a backend functor to be used to resolve a backend requirement. 

 True unless the functor passes the antecedent ('if' part of the rule) but fails the consequent ('then' part of the rule). 


### function BackendRule

```
inline BackendRule()
```

Default constructor. Sets all fields empty. 

### function permits_field

```
static bool permits_field(
    const str & field
)
```

Check if a given string is a permitted field of this class. 

Check if a given string is a permitted field of the [BackendRule](/documentation/code/classes/structgambit_1_1dres_1_1backendrule/) class. 


## Public Attributes Documentation

### variable version

```
std::string version;
```

Version field targeted by the rule. 

### variable if_version

```
bool if_version;
```

Version field appears in 'if' clause. 

### variable then_version

```
bool then_version;
```

Version field appears in 'then' clause. 

### variable backend

```
std::string backend;
```

Backend field targeted by the rule. 

### variable if_backend

```
bool if_backend;
```

Backend field appears in 'if' clause. 

### variable then_backend

```
bool then_backend;
```

Backend field appears in 'then' clause. 

### variable group

```
std::string group;
```

Backend group referenced by the rule. 

### variable if_group

```
bool if_group;
```

Group field appears in 'if' clause. 

-------------------------------

Updated on 2025-02-12 at 15:36:39 +0000