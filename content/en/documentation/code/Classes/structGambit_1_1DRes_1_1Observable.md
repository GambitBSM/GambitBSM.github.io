---
title: "struct Gambit::DRes::Observable"

description: "[No description available]"

---

# struct Gambit::DRes::Observable



[No description available]

## Public Functions

|                | Name           |
| -------------- | -------------- |
| bool | **[matches](/documentation/code/classes/structgambit_1_1dres_1_1observable/#function-matches)**([functor](/documentation/code/classes/classgambit_1_1functor/) * f, const [Utils::type_equivalency](/documentation/code/classes/structgambit_1_1utils_1_1type__equivalency/) & te) const<br>True if and only if the passed functor matches all matchable non-empty fields of the observable (i.e. everything except purpose, dependencies, backend_reqs, functionChain and subcaps).  |
| bool | **[dependencies_allow](/documentation/code/classes/structgambit_1_1dres_1_1observable/#function-dependencies-allow)**([functor](/documentation/code/classes/classgambit_1_1functor/) * f, const [Utils::type_equivalency](/documentation/code/classes/structgambit_1_1utils_1_1type__equivalency/) & te, bool ignore_if_weak =true) const<br>Whether the set of dependency rules subjugate to this observable allow a given module functor or not.  |
| bool | **[function_chain_allows](/documentation/code/classes/structgambit_1_1dres_1_1observable/#function-function-chain-allows)**([functor](/documentation/code/classes/classgambit_1_1functor/) * candidate, [functor](/documentation/code/classes/classgambit_1_1functor/) * dependee, const [Utils::type_equivalency](/documentation/code/classes/structgambit_1_1utils_1_1type__equivalency/) & te) const<br>Whether the functionChain of this observable allows a given module functor to be used to resolve the dependency of another.  |
| bool | **[backend_reqs_allow](/documentation/code/classes/structgambit_1_1dres_1_1observable/#function-backend-reqs-allow)**([functor](/documentation/code/classes/classgambit_1_1functor/) * f, const [Utils::type_equivalency](/documentation/code/classes/structgambit_1_1utils_1_1type__equivalency/) & te, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & group_being_resolved, bool ignore_if_weak =true) const<br>Whether the set of backend rules subjugate to this observable allow a given backend functor or not.  |
| | **[Observable](/documentation/code/classes/structgambit_1_1dres_1_1observable/#function-observable)**()<br>Default constructor. Sets all fields empty.  |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| YAML::Node | **[yaml](/documentation/code/classes/structgambit_1_1dres_1_1observable/#variable-yaml)** <br>The original [YAML](/documentation/code/namespaces/namespaceyaml/) (if any) from which this observable was derived.  |
| std::string | **[purpose](/documentation/code/classes/structgambit_1_1dres_1_1observable/#variable-purpose)** <br>Designated purpose of the observable (LogLike, etc).  |
| std::string | **[capability](/documentation/code/classes/structgambit_1_1dres_1_1observable/#variable-capability)** <br>Capability field targeted by the ObsLike entry.  |
| std::string | **[type](/documentation/code/classes/structgambit_1_1dres_1_1observable/#variable-type)** <br>Type field targeted by the ObsLike entry.  |
| std::string | **[function](/documentation/code/classes/structgambit_1_1dres_1_1observable/#variable-function)** <br>Function field targeted by the ObsLike entry.  |
| std::string | **[module](/documentation/code/classes/structgambit_1_1dres_1_1observable/#variable-module)** <br>Module targeted by the ObsLike entry.  |
| std::vector< [ModuleRule](/documentation/code/classes/structgambit_1_1dres_1_1modulerule/) > | **[dependencies](/documentation/code/classes/structgambit_1_1dres_1_1observable/#variable-dependencies)** <br>Subjugate dependency rules to be assigned to the observable.  |
| std::vector< [BackendRule](/documentation/code/classes/structgambit_1_1dres_1_1backendrule/) > | **[backends](/documentation/code/classes/structgambit_1_1dres_1_1observable/#variable-backends)** <br>Subjugate backend rules to be assigned to the observable.  |
| std::vector< std::string > | **[functionChain](/documentation/code/classes/structgambit_1_1dres_1_1observable/#variable-functionchain)** <br>Function chain to be assigned to the observable.  |
| YAML::Node | **[subcaps](/documentation/code/classes/structgambit_1_1dres_1_1observable/#variable-subcaps)** <br>Sub-capabilities to be assigned to the observable.  |
| bool | **[printme](/documentation/code/classes/structgambit_1_1dres_1_1observable/#variable-printme)** <br>Instruction to printer as to whether to write result to disk.  |
| bool | **[log_matches](/documentation/code/classes/structgambit_1_1dres_1_1observable/#variable-log-matches)** <br>Whether or not to log matches to the observable with functors.  |
| bool | **[include_all](/documentation/code/classes/structgambit_1_1dres_1_1observable/#variable-include-all)** <br>Whether to return multiple functor matches.  |

## Public Functions Documentation

### function matches

```
bool matches(
    functor * f,
    const Utils::type_equivalency & te
) const
```

True if and only if the passed functor matches all matchable non-empty fields of the observable (i.e. everything except purpose, dependencies, backend_reqs, functionChain and subcaps). 

### function dependencies_allow

```
bool dependencies_allow(
    functor * f,
    const Utils::type_equivalency & te,
    bool ignore_if_weak =true
) const
```

Whether the set of dependency rules subjugate to this observable allow a given module functor or not. 

Whether the set of dependency rules subjugate to this observable allow a given module functor or not. Must be true for the passed module functor to be used to resolve a dependency of the module functor that provides this observable (the dependee). Does not test if the dependee actually matches the observable, so should typically only be used after confirming this first. 


### function function_chain_allows

```
bool function_chain_allows(
    functor * candidate,
    functor * dependee,
    const Utils::type_equivalency & te
) const
```

Whether the functionChain of this observable allows a given module functor to be used to resolve the dependency of another. 

Whether the functionChain of this observable allows a given module functor to be used to resolve the dependency of another. Does not test if the dependent functor actually matches the observable, so should typically only be used after confirming this first. 


### function backend_reqs_allow

```
bool backend_reqs_allow(
    functor * f,
    const Utils::type_equivalency & te,
    const str & group_being_resolved,
    bool ignore_if_weak =true
) const
```

Whether the set of backend rules subjugate to this observable allow a given backend functor or not. 

Whether the set of backend rules subjugate to this observable allow a given backend functor or not. Must be true for the passed backend functor to be used to resolve a backend requirement of the module functor that matches this observable (the requiree). Does not test if the requiree actually matches the observable, so should typically only be used after confirming this first. 


### function Observable

```
inline Observable()
```

Default constructor. Sets all fields empty. 

## Public Attributes Documentation

### variable yaml

```
YAML::Node yaml;
```

The original [YAML](/documentation/code/namespaces/namespaceyaml/) (if any) from which this observable was derived. 

### variable purpose

```
std::string purpose;
```

Designated purpose of the observable (LogLike, etc). 

### variable capability

```
std::string capability;
```

Capability field targeted by the ObsLike entry. 

### variable type

```
std::string type;
```

Type field targeted by the ObsLike entry. 

### variable function

```
std::string function;
```

Function field targeted by the ObsLike entry. 

### variable module

```
std::string module;
```

Module targeted by the ObsLike entry. 

### variable dependencies

```
std::vector< ModuleRule > dependencies;
```

Subjugate dependency rules to be assigned to the observable. 

### variable backends

```
std::vector< BackendRule > backends;
```

Subjugate backend rules to be assigned to the observable. 

### variable functionChain

```
std::vector< std::string > functionChain;
```

Function chain to be assigned to the observable. 

### variable subcaps

```
YAML::Node subcaps;
```

Sub-capabilities to be assigned to the observable. 

### variable printme

```
bool printme;
```

Instruction to printer as to whether to write result to disk. 

### variable log_matches

```
bool log_matches;
```

Whether or not to log matches to the observable with functors. 

### variable include_all

```
bool include_all;
```

Whether to return multiple functor matches. 

-------------------------------

Updated on 2025-02-12 at 16:10:32 +0000