---
title: "struct Gambit::SpecTraits< SpecBit::QedQcdWrapper >"
description: "Specialisation of traits class needed to inform base spectrum class of the Model and Input types. "

---

# struct Gambit::SpecTraits< SpecBit::QedQcdWrapper >



Specialisation of traits class needed to inform base spectrum class of the Model and Input types. 


`#include <QedQcdWrapper.hpp>`

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef [SpectrumContents::SM](/documentation/code/classes/structgambit_1_1spectrumcontents_1_1sm/) | **[Contents](/documentation/code/classes/structgambit_1_1spectraits_3_01specbit_1_1qedqcdwrapper_01_4/#typedef-gambitspectraits-specbitqedqcdwrapper-contents)**  |
| typedef softsusy::QedQcd | **[Model](/documentation/code/classes/structgambit_1_1spectraits_3_01specbit_1_1qedqcdwrapper_01_4/#typedef-gambitspectraits-specbitqedqcdwrapper-model)**  |
| typedef [SMInputs](/documentation/code/classes/structgambit_1_1sminputs/) | **[Input](/documentation/code/classes/structgambit_1_1spectraits_3_01specbit_1_1qedqcdwrapper_01_4/#typedef-gambitspectraits-specbitqedqcdwrapper-input)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| std::string | **[name](/documentation/code/classes/structgambit_1_1spectraits_3_01specbit_1_1qedqcdwrapper_01_4/#function-gambitspectraits-specbitqedqcdwrapper-name)**() |

## Public Types Documentation

### typedef Contents

```
typedef SpectrumContents::SM Gambit::SpecTraits< SpecBit::QedQcdWrapper >::Contents;
```


### typedef Model

```
typedef softsusy::QedQcd Gambit::SpecTraits< SpecBit::QedQcdWrapper >::Model;
```


### typedef Input

```
typedef SMInputs Gambit::SpecTraits< SpecBit::QedQcdWrapper >::Input;
```


## Public Functions Documentation

### function name

```
static inline std::string name()
```


-------------------------------

Updated on 2022-09-08 at 02:00:47 +0000