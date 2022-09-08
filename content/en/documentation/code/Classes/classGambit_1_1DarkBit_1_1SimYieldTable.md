---
title: "class Gambit::DarkBit::SimYieldTable"
description: "Channel container Object containing tabularized yields for particle decay and two-body final states. "

---

# class Gambit::DarkBit::SimYieldTable



Channel container Object containing tabularized yields for particle decay and two-body final states. 


`#include <DarkBit_types.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[SimYieldTable](/documentation/code/classes/classgambit_1_1darkbit_1_1simyieldtable/#function-gambitdarkbitsimyieldtable-simyieldtable)**()<br>Sim yield table dummy constructor.  |
| void | **[addChannel](/documentation/code/classes/classgambit_1_1darkbit_1_1simyieldtable/#function-gambitdarkbitsimyieldtable-addchannel)**(daFunk::Funk dNdE, const std::string & p1, const std::string & p2, const std::string & finalState, double Ecm_min, double Ecm_max, [safe_ptr](/documentation/code/classes/classgambit_1_1safe__ptr/)< [Options](/documentation/code/classes/classgambit_1_1options/) > runOptions) |
| void | **[addChannel](/documentation/code/classes/classgambit_1_1darkbit_1_1simyieldtable/#function-gambitdarkbitsimyieldtable-addchannel)**(daFunk::Funk dNdE, const std::string & p1, const std::string & finalState, double Ecm_min, double Ecm_max, [safe_ptr](/documentation/code/classes/classgambit_1_1safe__ptr/)< [Options](/documentation/code/classes/classgambit_1_1options/) > runOptions) |
| void | **[addChannel](/documentation/code/classes/classgambit_1_1darkbit_1_1simyieldtable/#function-gambitdarkbitsimyieldtable-addchannel)**([SimYieldChannel](/documentation/code/classes/structgambit_1_1darkbit_1_1simyieldchannel/) channel) |
| void | **[replaceFinalState](/documentation/code/classes/classgambit_1_1darkbit_1_1simyieldtable/#function-gambitdarkbitsimyieldtable-replacefinalstate)**(const std::string & oldFinalState, const std::string & newFinalState) |
| void | **[donateChannels](/documentation/code/classes/classgambit_1_1darkbit_1_1simyieldtable/#function-gambitdarkbitsimyieldtable-donatechannels)**([SimYieldTable](/documentation/code/classes/classgambit_1_1darkbit_1_1simyieldtable/) & receiver) const |
| bool | **[hasChannel](/documentation/code/classes/classgambit_1_1darkbit_1_1simyieldtable/#function-gambitdarkbitsimyieldtable-haschannel)**(const std::string & p1, const std::string & p2, const std::string & finalState) const |
| bool | **[hasChannel](/documentation/code/classes/classgambit_1_1darkbit_1_1simyieldtable/#function-gambitdarkbitsimyieldtable-haschannel)**(const std::string & p1, const std::string & finalState) const |
| bool | **[hasAnyChannel](/documentation/code/classes/classgambit_1_1darkbit_1_1simyieldtable/#function-gambitdarkbitsimyieldtable-hasanychannel)**(const std::string & p1) const |
| bool | **[hasAnyChannel](/documentation/code/classes/classgambit_1_1darkbit_1_1simyieldtable/#function-gambitdarkbitsimyieldtable-hasanychannel)**(const std::string & p1, const std::string & p2) const |
| const [SimYieldChannel](/documentation/code/classes/structgambit_1_1darkbit_1_1simyieldchannel/) & | **[getChannel](/documentation/code/classes/classgambit_1_1darkbit_1_1simyieldtable/#function-gambitdarkbitsimyieldtable-getchannel)**(const std::string & p1, const std::string & p2, const std::string & finalState) const |
| daFunk::Funk | **[operator()](/documentation/code/classes/classgambit_1_1darkbit_1_1simyieldtable/#function-gambitdarkbitsimyieldtable-operator)**(const std::string & p1, const std::string & p2, const std::string & finalState, double Ecm) const<br>Retrieve simyield table entries at given center of mass energy (GeV)  |
| daFunk::Funk | **[operator()](/documentation/code/classes/classgambit_1_1darkbit_1_1simyieldtable/#function-gambitdarkbitsimyieldtable-operator)**(const std::string & p1, const std::string & finalState, double Ecm) const<br>Retrieve simyield table entries at given center of mass energy (GeV)  |
| daFunk::Funk | **[operator()](/documentation/code/classes/classgambit_1_1darkbit_1_1simyieldtable/#function-gambitdarkbitsimyieldtable-operator)**(const std::string & p1, const std::string & p2, const std::string & finalState) const<br>Retrieve simyield table entries at given center of mass energy (GeV)  |
| daFunk::Funk | **[operator()](/documentation/code/classes/classgambit_1_1darkbit_1_1simyieldtable/#function-gambitdarkbitsimyieldtable-operator)**(const std::string & p1, const std::string & finalState) const |

## Public Functions Documentation

### function SimYieldTable

```
SimYieldTable()
```

Sim yield table dummy constructor. 

### function addChannel

```
void addChannel(
    daFunk::Funk dNdE,
    const std::string & p1,
    const std::string & p2,
    const std::string & finalState,
    double Ecm_min,
    double Ecm_max,
    safe_ptr< Options > runOptions
)
```


### function addChannel

```
void addChannel(
    daFunk::Funk dNdE,
    const std::string & p1,
    const std::string & finalState,
    double Ecm_min,
    double Ecm_max,
    safe_ptr< Options > runOptions
)
```


### function addChannel

```
void addChannel(
    SimYieldChannel channel
)
```


### function replaceFinalState

```
void replaceFinalState(
    const std::string & oldFinalState,
    const std::string & newFinalState
)
```


### function donateChannels

```
void donateChannels(
    SimYieldTable & receiver
) const
```


### function hasChannel

```
bool hasChannel(
    const std::string & p1,
    const std::string & p2,
    const std::string & finalState
) const
```


### function hasChannel

```
bool hasChannel(
    const std::string & p1,
    const std::string & finalState
) const
```


### function hasAnyChannel

```
bool hasAnyChannel(
    const std::string & p1
) const
```


### function hasAnyChannel

```
bool hasAnyChannel(
    const std::string & p1,
    const std::string & p2
) const
```


### function getChannel

```
const SimYieldChannel & getChannel(
    const std::string & p1,
    const std::string & p2,
    const std::string & finalState
) const
```


### function operator()

```
daFunk::Funk operator()(
    const std::string & p1,
    const std::string & p2,
    const std::string & finalState,
    double Ecm
) const
```

Retrieve simyield table entries at given center of mass energy (GeV) 

### function operator()

```
daFunk::Funk operator()(
    const std::string & p1,
    const std::string & finalState,
    double Ecm
) const
```

Retrieve simyield table entries at given center of mass energy (GeV) 

### function operator()

```
daFunk::Funk operator()(
    const std::string & p1,
    const std::string & p2,
    const std::string & finalState
) const
```

Retrieve simyield table entries at given center of mass energy (GeV) 

### function operator()

```
daFunk::Funk operator()(
    const std::string & p1,
    const std::string & finalState
) const
```


-------------------------------

Updated on 2022-09-08 at 01:48:55 +0000