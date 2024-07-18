---
title: "struct Gambit::DRes::ModuleRule"
description: "Derived class rule for resolution of dependencies. "

---

# struct Gambit::DRes::ModuleRule



Derived class rule for resolution of dependencies. 


`#include <rule.hpp>`

Inherits from [Gambit::DRes::Rule](/documentation/code/classes/structgambit_1_1dres_1_1rule/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| bool | **[antecedent_matches](/documentation/code/classes/structgambit_1_1dres_1_1modulerule/#function-antecedent-matches)**([functor](/documentation/code/classes/classgambit_1_1functor/) * f, const [Utils::type_equivalency](/documentation/code/classes/structgambit_1_1utils_1_1type__equivalency/) & te) const<br>True if and only if the passed module functor matches the 'if' part of a rule.  |
| bool | **[consequent_matches](/documentation/code/classes/structgambit_1_1dres_1_1modulerule/#function-consequent-matches)**([functor](/documentation/code/classes/classgambit_1_1functor/) * f, const [Utils::type_equivalency](/documentation/code/classes/structgambit_1_1utils_1_1type__equivalency/) & te) const<br>True if and only if the passed module functor matches the 'then' part of a rule.  |
| bool | **[allows](/documentation/code/classes/structgambit_1_1dres_1_1modulerule/#function-allows)**([functor](/documentation/code/classes/classgambit_1_1functor/) * f, const [Utils::type_equivalency](/documentation/code/classes/structgambit_1_1utils_1_1type__equivalency/) & te, bool ignore_if_weak =true) const |
| bool | **[dependencies_allow](/documentation/code/classes/structgambit_1_1dres_1_1modulerule/#function-dependencies-allow)**([functor](/documentation/code/classes/classgambit_1_1functor/) * f, const [Utils::type_equivalency](/documentation/code/classes/structgambit_1_1utils_1_1type__equivalency/) & te, bool ignore_if_weak =true) const<br>Whether the set of dependency rules subjugate to this rule allow a given module functor or not.  |
| bool | **[function_chain_allows](/documentation/code/classes/structgambit_1_1dres_1_1modulerule/#function-function-chain-allows)**([functor](/documentation/code/classes/classgambit_1_1functor/) * candidate, [functor](/documentation/code/classes/classgambit_1_1functor/) * dependee, const [Utils::type_equivalency](/documentation/code/classes/structgambit_1_1utils_1_1type__equivalency/) & te, bool ignore_if_weak =true) const<br>Whether the functionChain of this rule allows a given module functor to be used to resolve the dependency of another.  |
| bool | **[backend_reqs_allow](/documentation/code/classes/structgambit_1_1dres_1_1modulerule/#function-backend-reqs-allow)**([functor](/documentation/code/classes/classgambit_1_1functor/) * f, const [Utils::type_equivalency](/documentation/code/classes/structgambit_1_1utils_1_1type__equivalency/) & te, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & group_being_resolved, bool ignore_if_weak =true) const<br>Whether the set of backend rules subjugate to this rule allow a given backend functor or not.  |
| | **[ModuleRule](/documentation/code/classes/structgambit_1_1dres_1_1modulerule/#function-modulerule)**()<br>Default constructor. Sets all fields empty.  |
| bool | **[permits_field](/documentation/code/classes/structgambit_1_1dres_1_1modulerule/#function-permits-field)**(const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & field)<br>Check if a given string is a permitted field of this class.  |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| std::string | **[module](/documentation/code/classes/structgambit_1_1dres_1_1modulerule/#variable-module)** <br>Module field targeted by the rule.  |
| bool | **[if_module](/documentation/code/classes/structgambit_1_1dres_1_1modulerule/#variable-if-module)** <br>Module field appears in 'if' clause.  |
| bool | **[then_module](/documentation/code/classes/structgambit_1_1dres_1_1modulerule/#variable-then-module)** <br>Module field appears in 'then' clause.  |
| [Options](/documentation/code/classes/classgambit_1_1options/) | **[options](/documentation/code/classes/structgambit_1_1dres_1_1modulerule/#variable-options)** <br>[Options](/documentation/code/classes/classgambit_1_1options/) provided by the rule.  |
| bool | **[then_options](/documentation/code/classes/structgambit_1_1dres_1_1modulerule/#variable-then-options)** <br>[Options](/documentation/code/classes/classgambit_1_1options/) appear in 'then' clause.  |
| std::vector< [ModuleRule](/documentation/code/classes/structgambit_1_1dres_1_1modulerule/) > | **[dependencies](/documentation/code/classes/structgambit_1_1dres_1_1modulerule/#variable-dependencies)** <br>Subjugate dependency rules provided by the rule.  |
| bool | **[then_dependencies](/documentation/code/classes/structgambit_1_1dres_1_1modulerule/#variable-then-dependencies)** <br>Subjugate dependency rules appear in 'then' clause.  |
| std::vector< [BackendRule](/documentation/code/classes/structgambit_1_1dres_1_1backendrule/) > | **[backends](/documentation/code/classes/structgambit_1_1dres_1_1modulerule/#variable-backends)** <br>Subjugate backend rules provided by the rule.  |
| bool | **[then_backends](/documentation/code/classes/structgambit_1_1dres_1_1modulerule/#variable-then-backends)** <br>Subjugate backend rules appear in 'then' clause.  |
| std::vector< std::string > | **[functionChain](/documentation/code/classes/structgambit_1_1dres_1_1modulerule/#variable-functionchain)** <br>Function chain provided by the rule.  |
| bool | **[then_functionChain](/documentation/code/classes/structgambit_1_1dres_1_1modulerule/#variable-then-functionchain)** <br>Function chain appears in the 'then' clause.  |

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
    const Utils::type_equivalency & te
) const
```

True if and only if the passed module functor matches the 'if' part of a rule. 

### function consequent_matches

```
bool consequent_matches(
    functor * f,
    const Utils::type_equivalency & te
) const
```

True if and only if the passed module functor matches the 'then' part of a rule. 

### function allows

```
bool allows(
    functor * f,
    const Utils::type_equivalency & te,
    bool ignore_if_weak =true
) const
```


Whether a module rule allows a given module functor or not. 

 Must be true for a module functor to be used to resolve a dependency. 

 True unless the functor passes the antecedent ('if' part of the rule) but fails the consequent ('then' part of the rule). 


### function dependencies_allow

```
bool dependencies_allow(
    functor * f,
    const Utils::type_equivalency & te,
    bool ignore_if_weak =true
) const
```

Whether the set of dependency rules subjugate to this rule allow a given module functor or not. 

Whether the set of dependency rules subjugate to this rule allow a given module functor or not. Must be true for the passed module functor to be used to resolve a dependency of another module functor that matches this rule (the dependee). Does not test if the dependee actually matches the rule, so should typically only be used after confirming this first. 


### function function_chain_allows

```
bool function_chain_allows(
    functor * candidate,
    functor * dependee,
    const Utils::type_equivalency & te,
    bool ignore_if_weak =true
) const
```

Whether the functionChain of this rule allows a given module functor to be used to resolve the dependency of another. 

Whether the functionChain of this rule allow a given module functor to be used to resolve the dependency of another. Does not test if the dependent functor actually matches the rule, so should typically only be used after confirming this first. 


### function backend_reqs_allow

```
bool backend_reqs_allow(
    functor * f,
    const Utils::type_equivalency & te,
    const str & group_being_resolved,
    bool ignore_if_weak =true
) const
```

Whether the set of backend rules subjugate to this rule allow a given backend functor or not. 

Whether the set of backend rules subjugate to this rule allow a given backend functor or not. Must be true for the passed backend functor to be used to resolve a backend requirement of another module functor that matches this rule (the requiree). Does not test if the requiree actually matches the rule, so should typically only be used after confirming this first. 


### function ModuleRule

```
inline ModuleRule()
```

Default constructor. Sets all fields empty. 

### function permits_field

```
static bool permits_field(
    const str & field
)
```

Check if a given string is a permitted field of this class. 

Check if a given string is a permitted field of the [ModuleRule](/documentation/code/classes/structgambit_1_1dres_1_1modulerule/) class. 


## Public Attributes Documentation

### variable module

```
std::string module;
```

Module field targeted by the rule. 

### variable if_module

```
bool if_module;
```

Module field appears in 'if' clause. 

### variable then_module

```
bool then_module;
```

Module field appears in 'then' clause. 

### variable options

```
Options options;
```

[Options](/documentation/code/classes/classgambit_1_1options/) provided by the rule. 

### variable then_options

```
bool then_options;
```

[Options](/documentation/code/classes/classgambit_1_1options/) appear in 'then' clause. 

### variable dependencies

```
std::vector< ModuleRule > dependencies;
```

Subjugate dependency rules provided by the rule. 

### variable then_dependencies

```
bool then_dependencies;
```

Subjugate dependency rules appear in 'then' clause. 

### variable backends

```
std::vector< BackendRule > backends;
```

Subjugate backend rules provided by the rule. 

### variable then_backends

```
bool then_backends;
```

Subjugate backend rules appear in 'then' clause. 

### variable functionChain

```
std::vector< std::string > functionChain;
```

Function chain provided by the rule. 

### variable then_functionChain

```
bool then_functionChain;
```

Function chain appears in the 'then' clause. 

-------------------------------

Updated on 2024-07-18 at 13:53:31 +0000