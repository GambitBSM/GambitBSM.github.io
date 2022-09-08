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
| | **[DependencyResolver](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#function-gambitdresdependencyresolver-dependencyresolver)**(const [gambit_core](/documentation/code/classes/classgambit_1_1gambit__core/) & core, const [Models::ModelFunctorClaw](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/) & claw, const [IniParser::IniFile](/documentation/code/classes/classgambit_1_1iniparser_1_1inifile/) & iniFile, const [Utils::type_equivalency](/documentation/code/classes/structgambit_1_1utils_1_1type__equivalency/) & equiv_classes, [Printers::BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/) & printer)<br>Constructor, provide module and backend functor lists.  |
| void | **[doResolution](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#function-gambitdresdependencyresolver-doresolution)**()<br>The dependency resolution.  |
| void | **[printFunctorList](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#function-gambitdresdependencyresolver-printfunctorlist)**()<br>Pretty print module functor information.  |
| void | **[printFunctorEvalOrder](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#function-gambitdresdependencyresolver-printfunctorevalorder)**(bool toterminal =false)<br>Pretty print function evaluation order.  |
| void | **[printRequiredBackends](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#function-gambitdresdependencyresolver-printrequiredbackends)**()<br>Print the list of required backends.  |
| void | **[getCitationKeys](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#function-gambitdresdependencyresolver-getcitationkeys)**()<br>Collect the citation keys for backends, modules, etc.  |
| void | **[printCitationKeys](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#function-gambitdresdependencyresolver-printcitationkeys)**() |
| std::vector< VertexID > | **[getObsLikeOrder](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#function-gambitdresdependencyresolver-getobslikeorder)**()<br>Retrieve the order in which target vertices are to be evaluated.  |
| void | **[calcObsLike](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#function-gambitdresdependencyresolver-calcobslike)**(VertexID vertex)<br>Calculate a single target vertex.  |
| void | **[printObsLike](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#function-gambitdresdependencyresolver-printobslike)**(VertexID vertex, const int pointID)<br>Print a single target vertex.  |
| bool | **[printTiming](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#function-gambitdresdependencyresolver-printtiming)**()<br>Getter for print_timing flag (used by LikelihoodContainer)  |
| [functor](/documentation/code/classes/classgambit_1_1functor/) * | **[get_functor](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#function-gambitdresdependencyresolver-get-functor)**(VertexID id)<br>Get the functor corresponding to a single VertexID.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[checkTypeMatch](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#function-gambitdresdependencyresolver-checktypematch)**(VertexID vertex, const [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) & purpose, const std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) > & types)<br>Ensure that the type of a given vertex is equivalent to at least one of a provided list, and return the matching list entry.  |
| template <typename TYPE \> <br>TYPE | **[getObsLike](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#function-gambitdresdependencyresolver-getobslike)**(VertexID vertex)<br>Return the result of a functor.  |
| const [IniParser::ObservableType](/documentation/code/classes/structgambit_1_1iniparser_1_1types_1_1observable/) * | **[getIniEntry](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#function-gambitdresdependencyresolver-getinientry)**(VertexID v) |
| void | **[invalidatePointAt](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#function-gambitdresdependencyresolver-invalidatepointat)**(VertexID vertex, bool isnan) |
| void | **[resetAll](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#function-gambitdresdependencyresolver-resetall)**() |
| [MasterGraphType](/documentation/code/namespaces/namespacegambit_1_1dres/#typedef-gambitdres-mastergraphtype) | **[cullInactiveFunctors](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/#function-gambitdresdependencyresolver-cullinactivefunctors)**([MasterGraphType](/documentation/code/namespaces/namespacegambit_1_1dres/#typedef-gambitdres-mastergraphtype) & )<br>Helper function that returns a new graph with all inactive vertices removed.  |

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


### function cullInactiveFunctors

```
static MasterGraphType cullInactiveFunctors(
    MasterGraphType & 
)
```

Helper function that returns a new graph with all inactive vertices removed. 

-------------------------------

Updated on 2022-09-08 at 02:00:48 +0000