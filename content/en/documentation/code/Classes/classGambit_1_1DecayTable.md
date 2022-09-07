---
title: 'class Gambit::DecayTable'
description: 'GAMBIT native decay table class. '

---

# Gambit::DecayTable





GAMBIT native decay table class. 


`#include <decay_table.hpp>`

## Public Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/)** <br>[DecayTable](/documentation/code/classes/classgambit_1_1decaytable/) entry class. Holds the info on all decays of a given particle.  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[DecayTable](/documentation/code/classes/classgambit_1_1decaytable/#function-decaytable)**() |
| | **[DecayTable](/documentation/code/classes/classgambit_1_1decaytable/#function-decaytable)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) slha, int context =0, bool force_SM_fermion_gauge_eigenstates =false)<br>Create a [DecayTable](/documentation/code/classes/classgambit_1_1decaytable/) from an SLHA file.  |
| | **[DecayTable](/documentation/code/classes/classgambit_1_1decaytable/#function-decaytable)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) slha, const std::map< int, int > & PDG_map, int context =0, bool force_SM_fermion_gauge_eigenstates =false)<br>Create a [DecayTable](/documentation/code/classes/classgambit_1_1decaytable/) from an SLHA file, with PDG code remapping.  |
| | **[DecayTable](/documentation/code/classes/classgambit_1_1decaytable/#function-decaytable)**(const [SLHAstruct](/documentation/code/namespaces/namespacegambit/#typedef-slhastruct) & slha, int context =0, bool force_SM_fermion_gauge_eigenstates =false)<br>Create a [DecayTable](/documentation/code/classes/classgambit_1_1decaytable/) from an SLHAea object containing DECAY blocks.  |
| | **[DecayTable](/documentation/code/classes/classgambit_1_1decaytable/#function-decaytable)**(const [SLHAstruct](/documentation/code/namespaces/namespacegambit/#typedef-slhastruct) & slha_in, const std::map< int, int > & PDG_map, int context =0, bool force_SM_fermion_gauge_eigenstates =false)<br>Create a [DecayTable](/documentation/code/classes/classgambit_1_1decaytable/) from an SLHAea object containing DECAY blocks, and remap PDG codes according to provided map.  |
| SLHAea::Block | **[getSLHAea_block](/documentation/code/classes/classgambit_1_1decaytable/#function-getslhaea-block)**(int v, std::pair< int, int > p, bool include_zero_bfs =false, const [mass_es_pseudonyms](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/) & psn =[mass_es_pseudonyms](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)()) const |
| SLHAea::Block | **[getSLHAea_block](/documentation/code/classes/classgambit_1_1decaytable/#function-getslhaea-block)**(int v, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) p, bool include_zero_bfs =false, const [mass_es_pseudonyms](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/) & psn =[mass_es_pseudonyms](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)()) const |
| SLHAea::Block | **[getSLHAea_block](/documentation/code/classes/classgambit_1_1decaytable/#function-getslhaea-block)**(int v, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) p, int i, bool include_zero_bfs =false, const [mass_es_pseudonyms](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/) & psn =[mass_es_pseudonyms](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)()) const |
| [Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/) & | **[operator()](/documentation/code/classes/classgambit_1_1decaytable/#function-operator)**(std::pair< int, int > p) |
| [Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/) & | **[operator()](/documentation/code/classes/classgambit_1_1decaytable/#function-operator)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) p) |
| [Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/) & | **[operator()](/documentation/code/classes/classgambit_1_1decaytable/#function-operator)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) p, int i) |
| const [Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/) & | **[operator()](/documentation/code/classes/classgambit_1_1decaytable/#function-operator)**(std::pair< int, int > p) const |
| const [Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/) & | **[operator()](/documentation/code/classes/classgambit_1_1decaytable/#function-operator)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) p) const |
| const [Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/) & | **[operator()](/documentation/code/classes/classgambit_1_1decaytable/#function-operator)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) p, int i) const |
| [Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/) & | **[at](/documentation/code/classes/classgambit_1_1decaytable/#function-at)**(std::pair< int, int > p) |
| [Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/) & | **[at](/documentation/code/classes/classgambit_1_1decaytable/#function-at)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) p) |
| [Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/) & | **[at](/documentation/code/classes/classgambit_1_1decaytable/#function-at)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) p, int i) |
| const [Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/) & | **[at](/documentation/code/classes/classgambit_1_1decaytable/#function-at)**(std::pair< int, int > p) const |
| const [Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/) & | **[at](/documentation/code/classes/classgambit_1_1decaytable/#function-at)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) p) const |
| const [Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/) & | **[at](/documentation/code/classes/classgambit_1_1decaytable/#function-at)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) p, int i) const |
| [SLHAstruct](/documentation/code/namespaces/namespacegambit/#typedef-slhastruct) | **[getSLHAea](/documentation/code/classes/classgambit_1_1decaytable/#function-getslhaea)**(int SLHA_version, bool include_zero_bfs =false, const [mass_es_pseudonyms](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/) & psn =[mass_es_pseudonyms](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)()) const<br>Output entire decay table as an SLHAea file full of DECAY blocks.  |
| void | **[writeSLHAfile](/documentation/code/classes/classgambit_1_1decaytable/#function-writeslhafile)**(int SLHA_version, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & filename, bool include_zero_bfs =false, const [mass_es_pseudonyms](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/) & psn =[mass_es_pseudonyms](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)()) const<br>Output entire decay table as an SLHA file full of DECAY blocks.  |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| std::map< std::pair< int, int >, [Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/) > | **[particles](/documentation/code/classes/classgambit_1_1decaytable/#variable-particles)** <br>The actual underlying map. Just iterate over this directly if you need to iterate over all particles in the table.  |

## Public Functions Documentation

### function DecayTable

```
inline DecayTable()
```


Constructors

Default constructor 


### function DecayTable

```
DecayTable(
    str slha,
    int context =0,
    bool force_SM_fermion_gauge_eigenstates =false
)
```

Create a [DecayTable](/documentation/code/classes/classgambit_1_1decaytable/) from an SLHA file. 

### function DecayTable

```
DecayTable(
    str slha,
    const std::map< int, int > & PDG_map,
    int context =0,
    bool force_SM_fermion_gauge_eigenstates =false
)
```

Create a [DecayTable](/documentation/code/classes/classgambit_1_1decaytable/) from an SLHA file, with PDG code remapping. 

### function DecayTable

```
DecayTable(
    const SLHAstruct & slha,
    int context =0,
    bool force_SM_fermion_gauge_eigenstates =false
)
```

Create a [DecayTable](/documentation/code/classes/classgambit_1_1decaytable/) from an SLHAea object containing DECAY blocks. 

### function DecayTable

```
DecayTable(
    const SLHAstruct & slha_in,
    const std::map< int, int > & PDG_map,
    int context =0,
    bool force_SM_fermion_gauge_eigenstates =false
)
```

Create a [DecayTable](/documentation/code/classes/classgambit_1_1decaytable/) from an SLHAea object containing DECAY blocks, and remap PDG codes according to provided map. 

### function getSLHAea_block

```
SLHAea::Block getSLHAea_block(
    int v,
    std::pair< int, int > p,
    bool include_zero_bfs =false,
    const mass_es_pseudonyms & psn =mass_es_pseudonyms()
) const
```


Output a decay table entry as an SLHAea DECAY block, using input parameter to identify the entry.

Output a decay table entry as an SLHAea DECAY block 


### function getSLHAea_block

```
SLHAea::Block getSLHAea_block(
    int v,
    str p,
    bool include_zero_bfs =false,
    const mass_es_pseudonyms & psn =mass_es_pseudonyms()
) const
```


### function getSLHAea_block

```
SLHAea::Block getSLHAea_block(
    int v,
    str p,
    int i,
    bool include_zero_bfs =false,
    const mass_es_pseudonyms & psn =mass_es_pseudonyms()
) const
```


### function operator()

```
Entry & operator()(
    std::pair< int, int > p
)
```


Get entry in decay table for a given particle, adding the particle to the table if it is absent. Three access methods: PDG-context integer pair, full particle name, short particle name + index integer. 


### function operator()

```
Entry & operator()(
    str p
)
```


### function operator()

```
Entry & operator()(
    str p,
    int i
)
```


### function operator()

```
const Entry & operator()(
    std::pair< int, int > p
) const
```


### function operator()

```
const Entry & operator()(
    str p
) const
```


### function operator()

```
const Entry & operator()(
    str p,
    int i
) const
```


### function at

```
Entry & at(
    std::pair< int, int > p
)
```


Get entry in decay table for a give particle, throwing an error if particle is absent. Three access methods: PDG-context integer pair, full particle name, short particle name + index integer. 


### function at

```
Entry & at(
    str p
)
```


### function at

```
Entry & at(
    str p,
    int i
)
```


### function at

```
const Entry & at(
    std::pair< int, int > p
) const
```


### function at

```
const Entry & at(
    str p
) const
```


### function at

```
const Entry & at(
    str p,
    int i
) const
```


### function getSLHAea

```
SLHAstruct getSLHAea(
    int SLHA_version,
    bool include_zero_bfs =false,
    const mass_es_pseudonyms & psn =mass_es_pseudonyms()
) const
```

Output entire decay table as an SLHAea file full of DECAY blocks. 

### function writeSLHAfile

```
void writeSLHAfile(
    int SLHA_version,
    const str & filename,
    bool include_zero_bfs =false,
    const mass_es_pseudonyms & psn =mass_es_pseudonyms()
) const
```

Output entire decay table as an SLHA file full of DECAY blocks. 

## Public Attributes Documentation

### variable particles

```
std::map< std::pair< int, int >, Entry > particles;
```

The actual underlying map. Just iterate over this directly if you need to iterate over all particles in the table. 

-------------------------------

Updated on 2022-09-07 at 13:49:48 +0000