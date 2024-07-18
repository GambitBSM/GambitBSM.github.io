---
title: "namespace Gambit::DRes"
description: "Forward declaration of [Rule]() and Observables classes for saving pointers to ignored and matched examples. "

---

# namespace Gambit::DRes

Forward declaration of [Rule]() and Observables classes for saving pointers to ignored and matched examples. 

## Classes

|                | Name           |
| -------------- | -------------- |
| struct | **[Gambit::DRes::BackendRule](/documentation/code/classes/structgambit_1_1dres_1_1backendrule/)** <br>Derived class rule for resolution of backend requirements.  |
| class | **[Gambit::DRes::DependencyResolver](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/)** <br>Main dependency resolver.  |
| class | **[Gambit::DRes::edgeWriter](/documentation/code/classes/classgambit_1_1dres_1_1edgewriter/)** <br>Graphviz output for edges/dependencies.  |
| class | **[Gambit::DRes::labelWriter](/documentation/code/classes/classgambit_1_1dres_1_1labelwriter/)** <br>Graphviz output for individual vertices/nodes/module functions.  |
| struct | **[Gambit::DRes::ModuleRule](/documentation/code/classes/structgambit_1_1dres_1_1modulerule/)** <br>Derived class rule for resolution of dependencies.  |
| struct | **[Gambit::DRes::Observable](/documentation/code/classes/structgambit_1_1dres_1_1observable/)**  |
| struct | **[Gambit::DRes::OutputVertex](/documentation/code/classes/structgambit_1_1dres_1_1outputvertex/)** <br>Bind purpose to output vertex.  |
| struct | **[Gambit::DRes::QueueEntry](/documentation/code/classes/structgambit_1_1dres_1_1queueentry/)** <br>Information in resolution queue.  |
| struct | **[Gambit::DRes::Rule](/documentation/code/classes/structgambit_1_1dres_1_1rule/)** <br>Base rule for resolution of dependencies and backend requirements.  |

## Types

|                | Name           |
| -------------- | -------------- |
| typedef adjacency_list< vecS, vecS, bidirectionalS, [functor](/documentation/code/classes/classgambit_1_1functor/) *, vecS > | **[MasterGraphType](/documentation/code/namespaces/namespacegambit_1_1dres/#typedef-mastergraphtype)**  |
| typedef graph_traits< [MasterGraphType](/documentation/code/namespaces/namespacegambit_1_1dres/#typedef-mastergraphtype) >::vertex_descriptor | **[VertexID](/documentation/code/namespaces/namespacegambit_1_1dres/#typedef-vertexid)**  |
| typedef graph_traits< [MasterGraphType](/documentation/code/namespaces/namespacegambit_1_1dres/#typedef-mastergraphtype) >::edge_descriptor | **[EdgeID](/documentation/code/namespaces/namespacegambit_1_1dres/#typedef-edgeid)**  |
| typedef property_map< [MasterGraphType](/documentation/code/namespaces/namespacegambit_1_1dres/#typedef-mastergraphtype), vertex_index_t >::type | **[IndexMap](/documentation/code/namespaces/namespacegambit_1_1dres/#typedef-indexmap)**  |
| typedef std::map< std::string, double * > | **[inputMapType](/documentation/code/namespaces/namespacegambit_1_1dres/#typedef-inputmaptype)**  |
| typedef std::map< std::string, std::vector< [functor](/documentation/code/classes/classgambit_1_1functor/) * > > | **[outputMapType](/documentation/code/namespaces/namespacegambit_1_1dres/#typedef-outputmaptype)**  |

## Functions

|                | Name           |
| -------------- | -------------- |
| [error](/documentation/code/classes/classgambit_1_1error/) & | **[dependency_resolver_error](/documentation/code/namespaces/namespacegambit_1_1dres/#function-dependency-resolver-error)**()<br>Dependency resolver errors.  |
| [warning](/documentation/code/classes/classgambit_1_1warning/) & | **[dependency_resolver_warning](/documentation/code/namespaces/namespacegambit_1_1dres/#function-dependency-resolver-warning)**()<br>Dependency resolver warnings.  |
| bool | **[stringComp](/documentation/code/namespaces/namespacegambit_1_1dres/#function-stringcomp)**(const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & s1, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & s2)<br>Check whether s1 (wildcard + regex allowed) matches s2.  |
| bool | **[typeComp](/documentation/code/namespaces/namespacegambit_1_1dres/#function-typecomp)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) s1, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) s2, const [Utils::type_equivalency](/documentation/code/classes/structgambit_1_1utils_1_1type__equivalency/) & eq)<br>Check whether type 1 (wildcard + regex allowed) matches type 2, taking into account equivalence classes.  |
| void | **[getParentVertices](/documentation/code/namespaces/namespacegambit_1_1dres/#function-getparentvertices)**(const VertexID & vertex, const [MasterGraphType](/documentation/code/namespaces/namespacegambit_1_1dres/#typedef-mastergraphtype) & graph, std::set< VertexID > & myVertexList)<br>Collect parent vertices recursively (excluding root vertex)  |
| std::vector< VertexID > | **[sortVertices](/documentation/code/namespaces/namespacegambit_1_1dres/#function-sortvertices)**(const std::set< VertexID > & set, const std::list< VertexID > & topoOrder)<br>Sort given list of vertices (according to topological sort result)  |
| std::vector< VertexID > | **[getSortedParentVertices](/documentation/code/namespaces/namespacegambit_1_1dres/#function-getsortedparentvertices)**(const VertexID & vertex, const [MasterGraphType](/documentation/code/namespaces/namespacegambit_1_1dres/#typedef-mastergraphtype) & graph, const std::list< VertexID > & topoOrder)<br>Get sorted list of parent vertices.  |
| double | **[getTimeEstimate](/documentation/code/namespaces/namespacegambit_1_1dres/#function-gettimeestimate)**(const std::set< VertexID > & vertexList, const [MasterGraphType](/documentation/code/namespaces/namespacegambit_1_1dres/#typedef-mastergraphtype) & graph)<br>Return runtime estimate for a set of nodes.  |
| template <typename RuleT \> <br>std::set< const RuleT * > | **[getUsedOrUnusedRules](/documentation/code/namespaces/namespacegambit_1_1dres/#function-getusedorunusedrules)**(bool find_used, const std::vector< RuleT > & rules, const [MasterGraphType](/documentation/code/namespaces/namespacegambit_1_1dres/#typedef-mastergraphtype) & masterGraph)<br>Retrieve used or unused rules.  |
| template <typename RuleT \> <br>std::set< const RuleT * > | **[getUsedRules](/documentation/code/namespaces/namespacegambit_1_1dres/#function-getusedrules)**(const std::vector< RuleT > & rules, const [MasterGraphType](/documentation/code/namespaces/namespacegambit_1_1dres/#typedef-mastergraphtype) & masterGraph) |
| template <typename RuleT \> <br>std::set< const RuleT * > | **[getUnusedRules](/documentation/code/namespaces/namespacegambit_1_1dres/#function-getunusedrules)**(const std::vector< RuleT > & rules, const [MasterGraphType](/documentation/code/namespaces/namespacegambit_1_1dres/#typedef-mastergraphtype) & masterGraph) |

## Types Documentation

### typedef MasterGraphType

```
typedef adjacency_list<vecS, vecS, bidirectionalS, functor*, vecS> Gambit::DRes::MasterGraphType;
```


Typedefs for central boost graph 


### typedef VertexID

```
typedef graph_traits<MasterGraphType>::vertex_descriptor Gambit::DRes::VertexID;
```


### typedef EdgeID

```
typedef graph_traits<MasterGraphType>::edge_descriptor Gambit::DRes::EdgeID;
```


### typedef IndexMap

```
typedef property_map<MasterGraphType,vertex_index_t>::type Gambit::DRes::IndexMap;
```


### typedef inputMapType

```
typedef std::map<std::string, double *> Gambit::DRes::inputMapType;
```


Typedefs for communication channels with the master-likelihood 


### typedef outputMapType

```
typedef std::map<std::string, std::vector<functor*> > Gambit::DRes::outputMapType;
```



## Functions Documentation

### function dependency_resolver_error

```
error & dependency_resolver_error()
```

Dependency resolver errors. 

### function dependency_resolver_warning

```
warning & dependency_resolver_warning()
```

Dependency resolver warnings. 

### function stringComp

```
bool stringComp(
    const str & s1,
    const str & s2
)
```

Check whether s1 (wildcard + regex allowed) matches s2. 

### function typeComp

```
bool typeComp(
    str s1,
    str s2,
    const Utils::type_equivalency & eq
)
```

Check whether type 1 (wildcard + regex allowed) matches type 2, taking into account equivalence classes. 

### function getParentVertices

```
void getParentVertices(
    const VertexID & vertex,
    const MasterGraphType & graph,
    std::set< VertexID > & myVertexList
)
```

Collect parent vertices recursively (excluding root vertex) 

### function sortVertices

```
std::vector< VertexID > sortVertices(
    const std::set< VertexID > & set,
    const std::list< VertexID > & topoOrder
)
```

Sort given list of vertices (according to topological sort result) 

### function getSortedParentVertices

```
std::vector< VertexID > getSortedParentVertices(
    const VertexID & vertex,
    const MasterGraphType & graph,
    const std::list< VertexID > & topoOrder
)
```

Get sorted list of parent vertices. 

### function getTimeEstimate

```
double getTimeEstimate(
    const std::set< VertexID > & vertexList,
    const MasterGraphType & graph
)
```

Return runtime estimate for a set of nodes. 

### function getUsedOrUnusedRules

```
template <typename RuleT >
std::set< const RuleT * > getUsedOrUnusedRules(
    bool find_used,
    const std::vector< RuleT > & rules,
    const MasterGraphType & masterGraph
)
```

Retrieve used or unused rules. 

### function getUsedRules

```
template <typename RuleT >
std::set< const RuleT * > getUsedRules(
    const std::vector< RuleT > & rules,
    const MasterGraphType & masterGraph
)
```


### function getUnusedRules

```
template <typename RuleT >
std::set< const RuleT * > getUnusedRules(
    const std::vector< RuleT > & rules,
    const MasterGraphType & masterGraph
)
```






-------------------------------

Updated on 2024-07-18 at 13:53:31 +0000