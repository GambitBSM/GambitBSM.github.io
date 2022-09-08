---
title: "struct Gambit::SpecTraits< SMSimpleSpec >"
description: "Specialisation of traits class needed to inform base spectrum class of the Model and Input types. "

---

# struct Gambit::SpecTraits< SMSimpleSpec >



Specialisation of traits class needed to inform base spectrum class of the Model and Input types. 


`#include <SMSimpleSpec.hpp>`

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef [SpectrumContents::SM_slha](/documentation/code/classes/structgambit_1_1spectrumcontents_1_1sm__slha/) | **[Contents](/documentation/code/classes/structgambit_1_1spectraits_3_01smsimplespec_01_4/#typedef-contents)**  |
| typedef [SMea](/documentation/code/classes/classgambit_1_1smea/) | **[Model](/documentation/code/classes/structgambit_1_1spectraits_3_01smsimplespec_01_4/#typedef-model)**  |
| typedef [DummyInput](/documentation/code/classes/classgambit_1_1dummyinput/) | **[Input](/documentation/code/classes/structgambit_1_1spectraits_3_01smsimplespec_01_4/#typedef-input)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| std::string | **[name](/documentation/code/classes/structgambit_1_1spectraits_3_01smsimplespec_01_4/#function-name)**() |

## Public Types Documentation

### typedef Contents

```
typedef SpectrumContents::SM_slha Gambit::SpecTraits< SMSimpleSpec >::Contents;
```


### typedef Model

```
typedef SMea Gambit::SpecTraits< SMSimpleSpec >::Model;
```


### typedef Input

```
typedef DummyInput Gambit::SpecTraits< SMSimpleSpec >::Input;
```


## Public Functions Documentation

### function name

```
static inline std::string name()
```


-------------------------------

Updated on 2022-09-08 at 00:43:00 +0000