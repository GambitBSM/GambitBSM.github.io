---
title: "class Gambit::DRes::DependencyResolver"
description: "Main dependency resolver. "

---

# class Gambit::DRes::DependencyResolver



Main dependency resolver. 


`#include <depresolver.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[DependencyResolver](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#function-dependencyresolver)**(const [gambit_core](/documentation/code/classes/classgambit_1_1gambit__core/) & core, const [Models::ModelFunctorClaw](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/) & claw, const [IniParser::IniFile](/documentation/code/classes/classgambit_1_1iniparser_1_1inifile/) & iniFile, const [Utils::type_equivalency](/documentation/code/classes/structgambit_1_1utils_1_1type__equivalency/) & equiv_classes, [Printers::BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/) & printer)<br>Constructor, provide module and backend functor lists.  |
| void | **[doResolution](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#function-doresolution)**()<br>The dependency resolution.  |
| void | **[printFunctorList](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#function-printfunctorlist)**()<br>Pretty print module functor information.  |
| void | **[printFunctorEvalOrder](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#function-printfunctorevalorder)**(bool toterminal =false)<br>Pretty print function evaluation order.  |
| void | **[printRequiredBackends](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#function-printrequiredbackends)**()<br>Print the list of required backends.  |
| void | **[getCitationKeys](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#function-getcitationkeys)**()<br>Collect the citation keys for backends, modules, etc.  |
| void | **[printCitationKeys](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#function-printcitationkeys)**() |
| std::vector< VertexID > | **[getObsLikeOrder](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#function-getobslikeorder)**()<br>Retrieve the order in which target vertices are to be evaluated.  |
| void | **[calcObsLike](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#function-calcobslike)**(VertexID vertex)<br>Calculate a single target vertex.  |
| void | **[printObsLike](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#function-printobslike)**(VertexID vertex, const int pointID)<br>Print a single target vertex.  |
| bool | **[printTiming](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#function-printtiming)**()<br>Getter for print_timing flag (used by LikelihoodContainer)  |
| [functor](/documentation/code/classes/classgambit_1_1functor/) * | **[get_functor](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#function-get-functor)**(VertexID id)<br>Get the functor corresponding to a single VertexID.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[checkTypeMatch](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#function-checktypematch)**(VertexID vertex, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & purpose, const std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > & types)<br>Ensure that the type of a given vertex is equivalent to at least one of a provided list, and return the matching list entry.  |
| template <typename TYPE \> <br>TYPE | **[getObsLike](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#function-getobslike)**(VertexID vertex)<br>Return the result of a functor.  |
| const [IniParser::ObservableType](/documentation/code/classes/structgambit_1_1iniparser_1_1types_1_1observable/) * | **[getIniEntry](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#function-getinientry)**(VertexID v) |
| void | **[invalidatePointAt](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#function-invalidatepointat)**(VertexID vertex, bool isnan) |
| void | **[resetAll](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#function-resetall)**() |
| void | **[checkForUnusedRules](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#function-checkforunusedrules)**(int mpi_rank)<br>Check for unused rules and options.  |
| void | **[set_scanID](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#function-set-scanid)**()<br>Set the Scan ID.  |
| [map_str_str](/documentation/code/namespaces/namespacegambit/#typedef-map-str-str) | **[getMetadata](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#function-getmetadata)**()<br>Construct metadata information from used observables, rules and options.  |
| [MasterGraphType](/documentation/code/namespaces/namespacegambit_1_1dres/#typedef-mastergraphtype) | **[cullInactiveFunctors](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#function-cullinactivefunctors)**([MasterGraphType](/documentation/code/namespaces/namespacegambit_1_1dres/#typedef-mastergraphtype) & )<br>Helper function that returns a new graph with all inactive vertices removed.  |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| int | **[scanID](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#variable-scanid)**  |

## Public Functions Documentation

### function DependencyResolver

```
DependencyResolver(
    const gambit_core & core,
    const Models::ModelFunctorClaw & claw,
    const IniParser::IniFile & iniFile,
    const Utils::type_equivalency & equiv_classes,
    Printers::BasePrinter & printer
)
```

Constructor, provide module and backend functor lists. 

### function doResolution

```
void doResolution()
```

The dependency resolution. 

### function printFunctorList

```
void printFunctorList()
```

Pretty print module functor information. 

List of masterGraph content. 


### function printFunctorEvalOrder

```
void printFunctorEvalOrder(
    bool toterminal =false
)
```

Pretty print function evaluation order. 

### function printRequiredBackends

```
void printRequiredBackends()
```

Print the list of required backends. 

### function getCitationKeys

```
void getCitationKeys()
```

Collect the citation keys for backends, modules, etc. 

### function printCitationKeys

```
void printCitationKeys()
```


### function getObsLikeOrder

```
std::vector< VertexID > getObsLikeOrder()
```

Retrieve the order in which target vertices are to be evaluated. 

### function calcObsLike

```
void calcObsLike(
    VertexID vertex
)
```

Calculate a single target vertex. 

### function printObsLike

```
void printObsLike(
    VertexID vertex,
    const int pointID
)
```

Print a single target vertex. 

### function printTiming

```
bool printTiming()
```

Getter for print_timing flag (used by LikelihoodContainer) 

### function get_functor

```
functor * get_functor(
    VertexID id
)
```

Get the functor corresponding to a single VertexID. 

### function checkTypeMatch

```
str checkTypeMatch(
    VertexID vertex,
    const str & purpose,
    const std::vector< str > & types
)
```

Ensure that the type of a given vertex is equivalent to at least one of a provided list, and return the matching list entry. 

### function getObsLike

```
template <typename TYPE >
inline TYPE getObsLike(
    VertexID vertex
)
```

Return the result of a functor. 

### function getIniEntry

```
const IniParser::ObservableType * getIniEntry(
    VertexID v
)
```


### function invalidatePointAt

```
void invalidatePointAt(
    VertexID vertex,
    bool isnan
)
```


### function resetAll

```
void resetAll()
```


### function checkForUnusedRules

```
void checkForUnusedRules(
    int mpi_rank
)
```

Check for unused rules and options. 

### function set_scanID

```
void set_scanID()
```

Set the Scan ID. 

### function getMetadata

```
map_str_str getMetadata()
```

Construct metadata information from used observables, rules and options. 

Construct metadata information from used observables, rules and options Note: No keys can be identical (or differing only by capitalisation) to those printed in the main file, otherwise the sqlite printer fails 


### function cullInactiveFunctors

```
static MasterGraphType cullInactiveFunctors(
    MasterGraphType & 
)
```

Helper function that returns a new graph with all inactive vertices removed. 

## Public Attributes Documentation

### variable scanID

```
int scanID;
```


-------------------------------

Updated on 2024-05-31 at 15:12:04 +0000