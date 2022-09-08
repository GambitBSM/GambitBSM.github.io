---
title: "class Gambit::DecayTable::Entry"
description: "[DecayTable](/documentation/code/classes/classgambit_1_1decaytable/) entry class. Holds the info on all decays of a given particle. "

---

# class Gambit::DecayTable::Entry



[DecayTable](/documentation/code/classes/classgambit_1_1decaytable/) entry class. Holds the info on all decays of a given particle. 


`#include <decay_table.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[set_BF](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/#function-set-bf)**(double BF, double error, const std::vector< std::pair< int, int > > & daughters)<br>Set branching fraction for decay to a given final state. 1. PDG-context integer pairs (vector)  |
| void | **[set_BF](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/#function-set-bf)**(double BF, double error, const std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > & daughters)<br>Set branching fraction for decay to a given final state. 2. full particle names (vector)  |
| template <typename... Args\> <br>void | **[set_BF](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/#function-set-bf)**(double BF, double error, std::pair< int, int > p1, Args... args) |
| template <typename... Args\> <br>void | **[set_BF](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/#function-set-bf)**(double BF, double error, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) p1, Args... args) |
| bool | **[has_channel](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/#function-has-channel)**(const std::vector< std::pair< int, int > > & daughters) const<br>Check if a given final state exists in this [DecayTable::Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/). 1. PDG-context integer pairs (vector)  |
| bool | **[has_channel](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/#function-has-channel)**(const std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > & daughters) const<br>Check if a given final state exists in this [DecayTable::Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/). 2. full particle names (vector)  |
| template <typename... Args\> <br>bool | **[has_channel](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/#function-has-channel)**(std::pair< int, int > p1, Args... args) const |
| template <typename... Args\> <br>bool | **[has_channel](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/#function-has-channel)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) p1, Args... args) const |
| double | **[BF](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/#function-bf)**(const std::vector< std::pair< int, int > > & daughters) const<br>Retrieve branching fraction for decay to a given final state. 1. PDG-context integer pairs (vector)  |
| double | **[BF](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/#function-bf)**(const std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > & daughters) const<br>Retrieve branching fraction for decay to a given final state. 2. full particle names (vector)  |
| template <typename... Args\> <br>double | **[BF](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/#function-bf)**(std::pair< int, int > p1, Args... args) const |
| template <typename... Args\> <br>double | **[BF](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/#function-bf)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) p1, Args... args) const |
| template <typename... Args\> <br>double | **[BF_error](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/#function-bf-error)**(std::pair< int, int > p1, Args... args) const |
| template <typename... Args\> <br>double | **[BF_error](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/#function-bf-error)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) p1, Args... args) const |
| template <typename... Args\> <br>std::pair< double, double > | **[BF_with_error](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/#function-bf-with-error)**(std::pair< int, int > p1, Args... args) const |
| template <typename... Args\> <br>std::pair< double, double > | **[BF_with_error](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/#function-bf-with-error)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) p1, Args... args) const |
| SLHAea::Block | **[getSLHAea_block](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/#function-getslhaea-block)**(int v, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) p, bool include_zero_bfs =false, const [mass_es_pseudonyms](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/) & psn =[mass_es_pseudonyms](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)()) const |
| SLHAea::Block | **[getSLHAea_block](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/#function-getslhaea-block)**(int v, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) p, int i, bool include_zero_bfs =false, const [mass_es_pseudonyms](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/) & psn =[mass_es_pseudonyms](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)()) const |
| SLHAea::Block | **[getSLHAea_block](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/#function-getslhaea-block)**(int v, std::pair< int, int > p, bool include_zero_bfs =false, const [mass_es_pseudonyms](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/) & psn =[mass_es_pseudonyms](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)()) const |
| | **[Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/#function-entry)**()<br>Default constructor.  |
| | **[Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/#function-entry)**(double width)<br>Constructor taking total width.  |
| | **[Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/#function-entry)**(const SLHAea::Block & block, int context =0, bool force_SM_fermion_gauge_eigenstates =false, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) calculator ="", [str](/documentation/code/namespaces/namespacegambit/#typedef-str) calculator_version ="")<br>Constructor creating a [DecayTable](/documentation/code/classes/classgambit_1_1decaytable/)[Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/) from an SLHAea DECAY block; full version.  |
| | **[Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/#function-entry)**(const SLHAea::Block & block, SLHAea::Block::const_iterator block_def, int context =0, bool force_SM_fermion_gauge_eigenstates =false, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) calculator ="", [str](/documentation/code/namespaces/namespacegambit/#typedef-str) calculator_version ="")<br>Constructor creating a [DecayTable](/documentation/code/classes/classgambit_1_1decaytable/)[Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/) from an SLHAea DECAY block; full version; version assuming block def is already known.  |
| double | **[sum_BF](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/#function-sum-bf)**() const<br>Sum up the partial widths and return the result.  |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| double | **[width_in_GeV](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/#variable-width-in-gev)** <br>Total particle width (in GeV)  |
| double | **[positive_error](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/#variable-positive-error)** <br>Positive error on width.  |
| double | **[negative_error](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/#variable-negative-error)** <br>Negative error on width.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[calculator](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/#variable-calculator)** <br>Name of the code (backend or otherwise) used for calculating this entry.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[calculator_version](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/#variable-calculator-version)** <br>Version of the code used for calculating this entry.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[warnings](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/#variable-warnings)** <br>Warnings from the calculator.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[errors](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/#variable-errors)** <br>Errors from the calculator.  |
| std::map< std::multiset< std::pair< int, int > >, std::pair< double, double > > | **[channels](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/#variable-channels)**  |

## Public Functions Documentation

### function set_BF

```
void set_BF(
    double BF,
    double error,
    const std::vector< std::pair< int, int > > & daughters
)
```

Set branching fraction for decay to a given final state. 1. PDG-context integer pairs (vector) 

Set branching fraction for decay to a given final state. Supports arbitrarily many final state particles. Five ways to specify final states:

1. PDG-context integer pairs (vector)
2. full particle names (vector)
3. PDG-context integer pairs (arguments)
4. full particle names (arguments)
5. short particle names + index integers (arguments) 


### function set_BF

```
void set_BF(
    double BF,
    double error,
    const std::vector< str > & daughters
)
```

Set branching fraction for decay to a given final state. 2. full particle names (vector) 

### function set_BF

```
template <typename... Args>
inline void set_BF(
    double BF,
    double error,
    std::pair< int, int > p1,
    Args... args
)
```


### function set_BF

```
template <typename... Args>
inline void set_BF(
    double BF,
    double error,
    str p1,
    Args... args
)
```


### function has_channel

```
bool has_channel(
    const std::vector< std::pair< int, int > > & daughters
) const
```

Check if a given final state exists in this [DecayTable::Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/). 1. PDG-context integer pairs (vector) 

Check if a given final state exists in this [DecayTable::Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/). Supports arbitrarily many final state particles. Five ways to specify final states:

1. PDG-context integer pairs (vector)
2. full particle names (vector)
3. PDG-context integer pairs (arguments)
4. full particle names (arguments)
5. short particle names + index integers (arguments) 


### function has_channel

```
bool has_channel(
    const std::vector< str > & daughters
) const
```

Check if a given final state exists in this [DecayTable::Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/). 2. full particle names (vector) 

### function has_channel

```
template <typename... Args>
inline bool has_channel(
    std::pair< int, int > p1,
    Args... args
) const
```


### function has_channel

```
template <typename... Args>
inline bool has_channel(
    str p1,
    Args... args
) const
```


### function BF

```
double BF(
    const std::vector< std::pair< int, int > > & daughters
) const
```

Retrieve branching fraction for decay to a given final state. 1. PDG-context integer pairs (vector) 

Retrieve branching fraction for decay to a given final state. Five ways to specify final states:

1. PDG-context integer pairs (vector)
2. full particle names (vector)
3. PDG-context integer pairs (arguments)
4. full particle names (arguments)
5. short particle names + index integers (arguments) Supports arbitrarily many final state particles. 


### function BF

```
double BF(
    const std::vector< str > & daughters
) const
```

Retrieve branching fraction for decay to a given final state. 2. full particle names (vector) 

### function BF

```
template <typename... Args>
inline double BF(
    std::pair< int, int > p1,
    Args... args
) const
```


### function BF

```
template <typename... Args>
inline double BF(
    str p1,
    Args... args
) const
```


### function BF_error

```
template <typename... Args>
inline double BF_error(
    std::pair< int, int > p1,
    Args... args
) const
```


Retrieve branching fraction error for decay to a given final state. Three ways to specify final states: PDG-context integer pairs, full particle names, short particle names + index integers. Supports arbitrarily many final state particles. 


### function BF_error

```
template <typename... Args>
inline double BF_error(
    str p1,
    Args... args
) const
```


### function BF_with_error

```
template <typename... Args>
inline std::pair< double, double > BF_with_error(
    std::pair< int, int > p1,
    Args... args
) const
```


Retrieve branching fraction and error for decay to a given final state. Three ways to specify final states: PDG-context integer pairs, full particle names, short particle names + index integers. Supports arbitrarily many final state particles. 


### function BF_with_error

```
template <typename... Args>
inline std::pair< double, double > BF_with_error(
    str p1,
    Args... args
) const
```


### function getSLHAea_block

```
SLHAea::Block getSLHAea_block(
    int v,
    str p,
    bool include_zero_bfs =false,
    const mass_es_pseudonyms & psn =mass_es_pseudonyms()
) const
```


Output this entry as an SLHAea DECAY block, using input parameter to identify the mother particle.

Output a decay table entry as an SLHAea DECAY block 


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


### function getSLHAea_block

```
SLHAea::Block getSLHAea_block(
    int v,
    std::pair< int, int > p,
    bool include_zero_bfs =false,
    const mass_es_pseudonyms & psn =mass_es_pseudonyms()
) const
```


### function Entry

```
inline Entry()
```

Default constructor. 

### function Entry

```
inline Entry(
    double width
)
```

Constructor taking total width. 

### function Entry

```
Entry(
    const SLHAea::Block & block,
    int context =0,
    bool force_SM_fermion_gauge_eigenstates =false,
    str calculator ="",
    str calculator_version =""
)
```

Constructor creating a [DecayTable](/documentation/code/classes/classgambit_1_1decaytable/)[Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/) from an SLHAea DECAY block; full version. 

### function Entry

```
Entry(
    const SLHAea::Block & block,
    SLHAea::Block::const_iterator block_def,
    int context =0,
    bool force_SM_fermion_gauge_eigenstates =false,
    str calculator ="",
    str calculator_version =""
)
```

Constructor creating a [DecayTable](/documentation/code/classes/classgambit_1_1decaytable/)[Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/) from an SLHAea DECAY block; full version; version assuming block def is already known. 

Constructor creating a [DecayTable](/documentation/code/classes/classgambit_1_1decaytable/)[Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/) from an SLHAea DECAY block; full version; version assuming block def is already known 


### function sum_BF

```
double sum_BF() const
```

Sum up the partial widths and return the result. 

Sum up the branching fractions for a single particle's entry and return the result. 


## Public Attributes Documentation

### variable width_in_GeV

```
double width_in_GeV;
```

Total particle width (in GeV) 

### variable positive_error

```
double positive_error;
```

Positive error on width. 

### variable negative_error

```
double negative_error;
```

Negative error on width. 

### variable calculator

```
str calculator;
```

Name of the code (backend or otherwise) used for calculating this entry. 

### variable calculator_version

```
str calculator_version;
```

Version of the code used for calculating this entry. 

### variable warnings

```
str warnings;
```

Warnings from the calculator. 

### variable errors

```
str errors;
```

Errors from the calculator. 

### variable channels

```
std::map< std::multiset< std::pair< int, int > >, std::pair< double, double > > channels;
```


The actual underlying map of channels to their BFs. Just iterate over this directly if you need to iterate over all decays of this particle. 


-------------------------------

Updated on 2022-09-08 at 03:17:31 +0000