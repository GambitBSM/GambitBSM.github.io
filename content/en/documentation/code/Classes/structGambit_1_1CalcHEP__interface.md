---
title: "struct Gambit::CalcHEP_interface"

description: "[No description available]"

---

# struct Gambit::CalcHEP_interface



[No description available]

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| int | **[forceUG](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-forceug)**  |
| char * | **[CALCHEP](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-calchep)**  |
| int | **[nvar](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-nvar)**  |
| int | **[nfunc](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-nfunc)**  |
| char ** | **[varName](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-varname)**  |
| REAL * | **[va](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-va)**  |
| int | **[nin](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-nin)**  |
| int | **[nout](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-nout)**  |
| int | **[nprc](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-nprc)**  |
| char *(*)(int, int, REAL *, int *) | **[pinf](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-pinf)**  |
| int(*)(int, int, int *, int *, int *) | **[pinfAux](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-pinfaux)**  |
| char ** | **[polarized](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-polarized)**  |
| int(*)(void) | **[calcFunc](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-calcfunc)**  |
| double * | **[BWrange](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-bwrange)**  |
| int * | **[twidth](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-twidth)**  |
| int * | **[gtwidth](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-gtwidth)**  |
| int * | **[gswidth](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-gswidth)**  |
| double(**)(char *) | **[aWidth](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-awidth)**  |
| double(*)(int, double, REAL *, REAL *, int *) | **[sqme](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-sqme)**  |
| char *(*)(int, int, int *, int *) | **[den_info](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-den-info)**  |
| [colorBasis](/documentation/code/classes/structgambit_1_1colorbasis/) * | **[cb](/documentation/code/classes/structgambit_1_1calchep__interface/#variable-cb)**  |

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

Updated on 2025-02-12 at 16:10:30 +0000