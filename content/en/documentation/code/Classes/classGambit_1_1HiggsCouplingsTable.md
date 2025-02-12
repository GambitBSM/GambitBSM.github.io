---
title: "class Gambit::HiggsCouplingsTable"
description: "GAMBIT native higgs coupling table class. "

---

# class Gambit::HiggsCouplingsTable



GAMBIT native higgs coupling table class. 


`#include <higgs_couplings_table.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| template <typename T \> <br>double | **[compute_effective_coupling](/documentation/code/classes/classgambit_1_1higgscouplingstable/#function-compute-effective-coupling)**(int index, const T & p1, const T & p2) |
| template <typename T \> <br>double | **[compute_effective_coupling](/documentation/code/classes/classgambit_1_1higgscouplingstable/#function-compute-effective-coupling)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) name, const T & p1, const T & p2) |
| void | **[set_neutral_decays_SM](/documentation/code/classes/classgambit_1_1higgscouplingstable/#function-set-neutral-decays-sm)**(int index, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & name, const [DecayTable::Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/) & entry)<br>Assign SM decay entries to neutral higgses.  |
| void | **[set_neutral_decays](/documentation/code/classes/classgambit_1_1higgscouplingstable/#function-set-neutral-decays)**(int index, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & name, const [DecayTable::Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/) & entry)<br>Assign decay entries to neutral higgses.  |
| void | **[set_charged_decays](/documentation/code/classes/classgambit_1_1higgscouplingstable/#function-set-charged-decays)**(int index, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & name, const [DecayTable::Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/) & entry)<br>Assign decay entries to charged higgses.  |
| void | **[set_t_decays](/documentation/code/classes/classgambit_1_1higgscouplingstable/#function-set-t-decays)**(const [DecayTable::Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/) & entry)<br>Assign decay entries to top.  |
| const std::vector< const [DecayTable::Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/) * > & | **[get_neutral_decays_SM_array](/documentation/code/classes/classgambit_1_1higgscouplingstable/#function-get-neutral-decays-sm-array)**() const<br>Retrieve SM decays of all neutral higgses.  |
| const [DecayTable::Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/) & | **[get_neutral_decays_SM](/documentation/code/classes/classgambit_1_1higgscouplingstable/#function-get-neutral-decays-sm)**(int index) const<br>Retrieve SM decays of a specific neutral Higgs, by index.  |
| const [DecayTable::Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/) & | **[get_neutral_decays_SM](/documentation/code/classes/classgambit_1_1higgscouplingstable/#function-get-neutral-decays-sm)**(const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & name) const<br>Retrieve SM decays of a specific neutral Higgs, by name.  |
| const std::vector< const [DecayTable::Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/) * > & | **[get_neutral_decays_array](/documentation/code/classes/classgambit_1_1higgscouplingstable/#function-get-neutral-decays-array)**() const<br>Retrieve decays of all neutral higgses.  |
| const [DecayTable::Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/) & | **[get_neutral_decays](/documentation/code/classes/classgambit_1_1higgscouplingstable/#function-get-neutral-decays)**(int index) const<br>Retrieve decays of a specific neutral Higgs, by index.  |
| const [DecayTable::Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/) & | **[get_neutral_decays](/documentation/code/classes/classgambit_1_1higgscouplingstable/#function-get-neutral-decays)**(const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & name) const<br>Retrieve decays of a specific neutral Higgs, by name.  |
| const std::vector< const [DecayTable::Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/) * > & | **[get_charged_decays_array](/documentation/code/classes/classgambit_1_1higgscouplingstable/#function-get-charged-decays-array)**() const<br>Retrieve decays of all charged higgses.  |
| const [DecayTable::Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/) & | **[get_charged_decays](/documentation/code/classes/classgambit_1_1higgscouplingstable/#function-get-charged-decays)**(int index) const<br>Retrieve decays of a specific charged Higgs, by index.  |
| const [DecayTable::Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/) & | **[get_charged_decays](/documentation/code/classes/classgambit_1_1higgscouplingstable/#function-get-charged-decays)**(const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & name) const<br>Retrieve decays of a specific charged Higgs, by name.  |
| const [DecayTable::Entry](/documentation/code/classes/classgambit_1_1decaytable_1_1entry/) & | **[get_t_decays](/documentation/code/classes/classgambit_1_1higgscouplingstable/#function-get-t-decays)**() const<br>Retrieve decays of the top quark.  |
| | **[HiggsCouplingsTable](/documentation/code/classes/classgambit_1_1higgscouplingstable/#function-higgscouplingstable)**()<br>Constructor.  |
| void | **[set_n_neutral_higgs](/documentation/code/classes/classgambit_1_1higgscouplingstable/#function-set-n-neutral-higgs)**(int n)<br>Set the number of neutral Higgses.  |
| void | **[set_n_charged_higgs](/documentation/code/classes/classgambit_1_1higgscouplingstable/#function-set-n-charged-higgs)**(int n)<br>Set the number of charged Higgses.  |
| int | **[get_n_neutral_higgs](/documentation/code/classes/classgambit_1_1higgscouplingstable/#function-get-n-neutral-higgs)**() const<br>Retrieve number of neutral higgses.  |
| int | **[get_n_charged_higgs](/documentation/code/classes/classgambit_1_1higgscouplingstable/#function-get-n-charged-higgs)**() const<br>Retrieve number of charged higgses.  |
| void | **[set_effective_couplings_to_unity](/documentation/code/classes/classgambit_1_1higgscouplingstable/#function-set-effective-couplings-to-unity)**()<br>Set all effective couplings to 1.  |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| std::vector< double > | **[C_WW2](/documentation/code/classes/classgambit_1_1higgscouplingstable/#variable-c-ww2)**  |
| std::vector< double > | **[C_ZZ2](/documentation/code/classes/classgambit_1_1higgscouplingstable/#variable-c-zz2)**  |
| std::vector< double > | **[C_tt2](/documentation/code/classes/classgambit_1_1higgscouplingstable/#variable-c-tt2)**  |
| std::vector< double > | **[C_bb2](/documentation/code/classes/classgambit_1_1higgscouplingstable/#variable-c-bb2)**  |
| std::vector< double > | **[C_cc2](/documentation/code/classes/classgambit_1_1higgscouplingstable/#variable-c-cc2)**  |
| std::vector< double > | **[C_tautau2](/documentation/code/classes/classgambit_1_1higgscouplingstable/#variable-c-tautau2)**  |
| std::vector< double > | **[C_gaga2](/documentation/code/classes/classgambit_1_1higgscouplingstable/#variable-c-gaga2)**  |
| std::vector< double > | **[C_gg2](/documentation/code/classes/classgambit_1_1higgscouplingstable/#variable-c-gg2)**  |
| std::vector< double > | **[C_mumu2](/documentation/code/classes/classgambit_1_1higgscouplingstable/#variable-c-mumu2)**  |
| std::vector< double > | **[C_Zga2](/documentation/code/classes/classgambit_1_1higgscouplingstable/#variable-c-zga2)**  |
| std::vector< double > | **[C_ss2](/documentation/code/classes/classgambit_1_1higgscouplingstable/#variable-c-ss2)**  |
| std::vector< std::vector< double > > | **[C_hiZ2](/documentation/code/classes/classgambit_1_1higgscouplingstable/#variable-c-hiz2)**  |
| std::vector< double > | **[CP](/documentation/code/classes/classgambit_1_1higgscouplingstable/#variable-cp)** <br>CP of neutral higgses.  |
| std::vector< std::pair< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > > | **[invisibles](/documentation/code/classes/classgambit_1_1higgscouplingstable/#variable-invisibles)** <br>Particles that higgses can decay invisibly to.  |

## Public Functions Documentation

### function compute_effective_coupling

```
template <typename T >
inline double compute_effective_coupling(
    int index,
    const T & p1,
    const T & p2
)
```


Compute a neutral higgs effective coupling from the current two-body neutral higgs decays 


### function compute_effective_coupling

```
template <typename T >
inline double compute_effective_coupling(
    str name,
    const T & p1,
    const T & p2
)
```


### function set_neutral_decays_SM

```
void set_neutral_decays_SM(
    int index,
    const str & name,
    const DecayTable::Entry & entry
)
```

Assign SM decay entries to neutral higgses. 

Assign decay entries to the various table components 


### function set_neutral_decays

```
void set_neutral_decays(
    int index,
    const str & name,
    const DecayTable::Entry & entry
)
```

Assign decay entries to neutral higgses. 

### function set_charged_decays

```
void set_charged_decays(
    int index,
    const str & name,
    const DecayTable::Entry & entry
)
```

Assign decay entries to charged higgses. 

### function set_t_decays

```
void set_t_decays(
    const DecayTable::Entry & entry
)
```

Assign decay entries to top. 

### function get_neutral_decays_SM_array

```
const std::vector< const DecayTable::Entry * > & get_neutral_decays_SM_array() const
```

Retrieve SM decays of all neutral higgses. 

Retrieve decay sets 


### function get_neutral_decays_SM

```
const DecayTable::Entry & get_neutral_decays_SM(
    int index
) const
```

Retrieve SM decays of a specific neutral Higgs, by index. 

### function get_neutral_decays_SM

```
const DecayTable::Entry & get_neutral_decays_SM(
    const str & name
) const
```

Retrieve SM decays of a specific neutral Higgs, by name. 

### function get_neutral_decays_array

```
const std::vector< const DecayTable::Entry * > & get_neutral_decays_array() const
```

Retrieve decays of all neutral higgses. 

### function get_neutral_decays

```
const DecayTable::Entry & get_neutral_decays(
    int index
) const
```

Retrieve decays of a specific neutral Higgs, by index. 

### function get_neutral_decays

```
const DecayTable::Entry & get_neutral_decays(
    const str & name
) const
```

Retrieve decays of a specific neutral Higgs, by name. 

### function get_charged_decays_array

```
const std::vector< const DecayTable::Entry * > & get_charged_decays_array() const
```

Retrieve decays of all charged higgses. 

### function get_charged_decays

```
const DecayTable::Entry & get_charged_decays(
    int index
) const
```

Retrieve decays of a specific charged Higgs, by index. 

### function get_charged_decays

```
const DecayTable::Entry & get_charged_decays(
    const str & name
) const
```

Retrieve decays of a specific charged Higgs, by name. 

### function get_t_decays

```
const DecayTable::Entry & get_t_decays() const
```

Retrieve decays of the top quark. 

### function HiggsCouplingsTable

```
inline HiggsCouplingsTable()
```

Constructor. 

### function set_n_neutral_higgs

```
void set_n_neutral_higgs(
    int n
)
```

Set the number of neutral Higgses. 

### function set_n_charged_higgs

```
void set_n_charged_higgs(
    int n
)
```

Set the number of charged Higgses. 

### function get_n_neutral_higgs

```
int get_n_neutral_higgs() const
```

Retrieve number of neutral higgses. 

### function get_n_charged_higgs

```
int get_n_charged_higgs() const
```

Retrieve number of charged higgses. 

### function set_effective_couplings_to_unity

```
void set_effective_couplings_to_unity()
```

Set all effective couplings to 1. 

## Public Attributes Documentation

### variable C_WW2

```
std::vector< double > C_WW2;
```


Effective couplings for neutral higgses 


### variable C_ZZ2

```
std::vector< double > C_ZZ2;
```


### variable C_tt2

```
std::vector< double > C_tt2;
```


### variable C_bb2

```
std::vector< double > C_bb2;
```


### variable C_cc2

```
std::vector< double > C_cc2;
```


### variable C_tautau2

```
std::vector< double > C_tautau2;
```


### variable C_gaga2

```
std::vector< double > C_gaga2;
```


### variable C_gg2

```
std::vector< double > C_gg2;
```


### variable C_mumu2

```
std::vector< double > C_mumu2;
```


### variable C_Zga2

```
std::vector< double > C_Zga2;
```


### variable C_ss2

```
std::vector< double > C_ss2;
```


### variable C_hiZ2

```
std::vector< std::vector< double > > C_hiZ2;
```


### variable CP

```
std::vector< double > CP;
```

CP of neutral higgses. 

### variable invisibles

```
std::vector< std::pair< str, str > > invisibles;
```

Particles that higgses can decay invisibly to. 

-------------------------------

Updated on 2025-02-12 at 15:36:38 +0000