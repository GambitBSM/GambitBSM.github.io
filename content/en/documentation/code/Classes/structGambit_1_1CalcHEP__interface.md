---
title: "struct Gambit::CalcHEP_interface"

description: "[No description available]"

---

# struct Gambit::CalcHEP_interface



[No description available]

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| int | **[forceUG](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-gambitcalchep-interface-forceug)**  |
| char * | **[CALCHEP](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-gambitcalchep-interface-calchep)**  |
| int | **[nvar](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-gambitcalchep-interface-nvar)**  |
| int | **[nfunc](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-gambitcalchep-interface-nfunc)**  |
| char ** | **[varName](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-gambitcalchep-interface-varname)**  |
| REAL * | **[va](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-gambitcalchep-interface-va)**  |
| int | **[nin](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-gambitcalchep-interface-nin)**  |
| int | **[nout](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-gambitcalchep-interface-nout)**  |
| int | **[nprc](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-gambitcalchep-interface-nprc)**  |
| char *(*)(int, int, REAL *, int *) | **[pinf](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-gambitcalchep-interface-pinf)**  |
| int(*)(int, int, int *, int *, int *) | **[pinfAux](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-gambitcalchep-interface-pinfaux)**  |
| char ** | **[polarized](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-gambitcalchep-interface-polarized)**  |
| int(*)(void) | **[calcFunc](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-gambitcalchep-interface-calcfunc)**  |
| double * | **[BWrange](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-gambitcalchep-interface-bwrange)**  |
| int * | **[twidth](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-gambitcalchep-interface-twidth)**  |
| int * | **[gtwidth](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-gambitcalchep-interface-gtwidth)**  |
| int * | **[gswidth](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-gambitcalchep-interface-gswidth)**  |
| double(**)(char *) | **[aWidth](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-gambitcalchep-interface-awidth)**  |
| double(*)(int, double, REAL *, REAL *, int *) | **[sqme](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-gambitcalchep-interface-sqme)**  |
| char *(*)(int, int, int *, int *) | **[den_info](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-gambitcalchep-interface-den-info)**  |
| [colorBasis](/documentation/code/classes/structgambit_1_1colorbasis/) * | **[cb](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-gambitcalchep-interface-cb)**  |

## Public Attributes Documentation

### variable forceUG

```
int forceUG;
```


### variable CALCHEP

```
char * CALCHEP;
```


### variable nvar

```
int nvar;
```


### variable nfunc

```
int nfunc;
```


### variable varName

```
char ** varName;
```


### variable va

```
REAL * va;
```


### variable nin

```
int nin;
```


### variable nout

```
int nout;
```


### variable nprc

```
int nprc;
```


### variable pinf

```
char *(*)(int, int, REAL *, int *) pinf;
```


### variable pinfAux

```
int(*)(int, int, int *, int *, int *) pinfAux;
```


### variable polarized

```
char ** polarized;
```


### variable calcFunc

```
int(*)(void) calcFunc;
```


### variable BWrange

```
double * BWrange;
```


### variable twidth

```
int * twidth;
```


### variable gtwidth

```
int * gtwidth;
```


### variable gswidth

```
int * gswidth;
```


### variable aWidth

```
double(**)(char *) aWidth;
```


### variable sqme

```
double(*)(int, double, REAL *, REAL *, int *) sqme;
```


### variable den_info

```
char *(*)(int, int, int *, int *) den_info;
```


### variable cb

```
colorBasis * cb;
```


-------------------------------

Updated on 2022-09-08 at 02:00:46 +0000