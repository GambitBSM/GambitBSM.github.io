---
title: "struct Gambit::SMInputs"
description: "Container class for Standard Model input information (defined as in SLHA2) "

---

# struct Gambit::SMInputs



Container class for Standard Model input information (defined as in SLHA2) 


`#include <sminputs.hpp>`

## Public Classes

|                | Name           |
| -------------- | -------------- |
| struct | **[CKMdef](/documentation/code/classes/structgambit_1_1sminputs_1_1ckmdef/)**  |
| struct | **[PMNSdef](/documentation/code/classes/structgambit_1_1sminputs_1_1pmnsdef/)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[SMInputs](/documentation/code/classes/structgambit_1_1sminputs/#function-gambitsminputs-sminputs)**() |
| | **[SMInputs](/documentation/code/classes/structgambit_1_1sminputs/#function-gambitsminputs-sminputs)**([SLHAstruct](/documentation/code/namespaces/namespacegambit/#typedef-gambit-slhastruct) & data) |
| [SLHAstruct](/documentation/code/namespaces/namespacegambit/#typedef-gambit-slhastruct) | **[getSLHAea](/documentation/code/classes/structgambit_1_1sminputs/#function-gambitsminputs-getslhaea)**() const |
| void | **[add_to_SLHAea](/documentation/code/classes/structgambit_1_1sminputs/#function-gambitsminputs-add-to-slhaea)**([SLHAstruct](/documentation/code/namespaces/namespacegambit/#typedef-gambit-slhastruct) & slha) const |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| double | **[alphainv](/documentation/code/classes/structgambit_1_1sminputs/#variable-gambitsminputs-alphainv)**  |
| double | **[GF](/documentation/code/classes/structgambit_1_1sminputs/#variable-gambitsminputs-gf)**  |
| double | **[alphaS](/documentation/code/classes/structgambit_1_1sminputs/#variable-gambitsminputs-alphas)**  |
| double | **[mZ](/documentation/code/classes/structgambit_1_1sminputs/#variable-gambitsminputs-mz)**  |
| double | **[mBmB](/documentation/code/classes/structgambit_1_1sminputs/#variable-gambitsminputs-mbmb)**  |
| double | **[mT](/documentation/code/classes/structgambit_1_1sminputs/#variable-gambitsminputs-mt)**  |
| double | **[mTau](/documentation/code/classes/structgambit_1_1sminputs/#variable-gambitsminputs-mtau)**  |
| double | **[mNu3](/documentation/code/classes/structgambit_1_1sminputs/#variable-gambitsminputs-mnu3)**  |
| double | **[mE](/documentation/code/classes/structgambit_1_1sminputs/#variable-gambitsminputs-me)**  |
| double | **[mNu1](/documentation/code/classes/structgambit_1_1sminputs/#variable-gambitsminputs-mnu1)**  |
| double | **[mMu](/documentation/code/classes/structgambit_1_1sminputs/#variable-gambitsminputs-mmu)**  |
| double | **[mNu2](/documentation/code/classes/structgambit_1_1sminputs/#variable-gambitsminputs-mnu2)**  |
| double | **[mD](/documentation/code/classes/structgambit_1_1sminputs/#variable-gambitsminputs-md)**  |
| double | **[mU](/documentation/code/classes/structgambit_1_1sminputs/#variable-gambitsminputs-mu)**  |
| double | **[mS](/documentation/code/classes/structgambit_1_1sminputs/#variable-gambitsminputs-ms)**  |
| double | **[mCmC](/documentation/code/classes/structgambit_1_1sminputs/#variable-gambitsminputs-mcmc)**  |
| [CKMdef](/documentation/code/classes/structgambit_1_1sminputs_1_1ckmdef/) | **[CKM](/documentation/code/classes/structgambit_1_1sminputs/#variable-gambitsminputs-ckm)**  |
| [PMNSdef](/documentation/code/classes/structgambit_1_1sminputs_1_1pmnsdef/) | **[PMNS](/documentation/code/classes/structgambit_1_1sminputs/#variable-gambitsminputs-pmns)**  |
| double | **[mW](/documentation/code/classes/structgambit_1_1sminputs/#variable-gambitsminputs-mw)**  |

## Public Functions Documentation

### function SMInputs

```
inline SMInputs()
```


### function SMInputs

```
SMInputs(
    SLHAstruct & data
)
```


### function getSLHAea

```
SLHAstruct getSLHAea() const
```


### function add_to_SLHAea

```
void add_to_SLHAea(
    SLHAstruct & slha
) const
```


## Public Attributes Documentation

### variable alphainv

```
double alphainv;
```


### variable GF

```
double GF;
```


### variable alphaS

```
double alphaS;
```


### variable mZ

```
double mZ;
```


### variable mBmB

```
double mBmB;
```


### variable mT

```
double mT;
```


### variable mTau

```
double mTau;
```


### variable mNu3

```
double mNu3;
```


### variable mE

```
double mE;
```


### variable mNu1

```
double mNu1;
```


### variable mMu

```
double mMu;
```


### variable mNu2

```
double mNu2;
```


### variable mD

```
double mD;
```


### variable mU

```
double mU;
```


### variable mS

```
double mS;
```


### variable mCmC

```
double mCmC;
```


### variable CKM

```
CKMdef CKM;
```


### variable PMNS

```
PMNSdef PMNS;
```


### variable mW

```
double mW = mw_central_observed;
```


-------------------------------

Updated on 2022-09-08 at 01:48:54 +0000