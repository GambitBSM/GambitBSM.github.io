---
title: "struct Gambit::SpecTraits< MSSMSimpleSpec >"
description: "Specialisation of traits class needed to inform base spectrum class of the Model and Input types. "

---

# struct Gambit::SpecTraits< MSSMSimpleSpec >



Specialisation of traits class needed to inform base spectrum class of the Model and Input types. 


`#include <MSSMSimpleSpec.hpp>`

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef [SpectrumContents::MSSM](/documentation/code/classes/structgambit_1_1spectrumcontents_1_1mssm/) | **[Contents](/documentation/code/classes/structgambit_1_1spectraits_3_01mssmsimplespec_01_4/#typedef-contents)**  |
| typedef [MSSMea](/documentation/code/classes/classgambit_1_1mssmea/) | **[Model](/documentation/code/classes/structgambit_1_1spectraits_3_01mssmsimplespec_01_4/#typedef-model)**  |
| typedef [DummyInput](/documentation/code/classes/classgambit_1_1dummyinput/) | **[Input](/documentation/code/classes/structgambit_1_1spectraits_3_01mssmsimplespec_01_4/#typedef-input)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| std::string | **[name](/documentation/code/classes/structgambit_1_1spectraits_3_01mssmsimplespec_01_4/#function-name)**() |

## Public Types Documentation

### typedef Contents

```
typedef SpectrumContents::MSSM Gambit::SpecTraits< MSSMSimpleSpec >::Contents;
```


### typedef Model

```
typedef MSSMea Gambit::SpecTraits< MSSMSimpleSpec >::Model;
```


### typedef Input

```
typedef DummyInput Gambit::SpecTraits< MSSMSimpleSpec >::Input;
```


## Public Functions Documentation

### function name

```
static inline std::string name()
```


-------------------------------

Updated on 2025-02-12 at 16:10:31 +0000