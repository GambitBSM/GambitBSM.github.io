---
title: "struct Gambit::CalcHEP_interface"

description: "[No description available]"

---

# struct Gambit::CalcHEP_interface



[No description available]

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| int | **[forceUG](/documentation/code/classes/structgambit_1_1calchep__interface/)**  |
| char * | **[CALCHEP](/documentation/code/classes/structgambit_1_1calchep__interface/)**  |
| int | **[nvar](/documentation/code/classes/structgambit_1_1calchep__interface/)**  |
| int | **[nfunc](/documentation/code/classes/structgambit_1_1calchep__interface/)**  |
| char ** | **[varName](/documentation/code/classes/structgambit_1_1calchep__interface/)**  |
| REAL * | **[va](/documentation/code/classes/structgambit_1_1calchep__interface/)**  |
| int | **[nin](/documentation/code/classes/structgambit_1_1calchep__interface/)**  |
| int | **[nout](/documentation/code/classes/structgambit_1_1calchep__interface/)**  |
| int | **[nprc](/documentation/code/classes/structgambit_1_1calchep__interface/)**  |
| char *(*)(int, int, REAL *, int *) | **[pinf](/documentation/code/classes/structgambit_1_1calchep__interface/)**  |
| int(*)(int, int, int *, int *, int *) | **[pinfAux](/documentation/code/classes/structgambit_1_1calchep__interface/)**  |
| char ** | **[polarized](/documentation/code/classes/structgambit_1_1calchep__interface/)**  |
| int(*)(void) | **[calcFunc](/documentation/code/classes/structgambit_1_1calchep__interface/)**  |
| double * | **[BWrange](/documentation/code/classes/structgambit_1_1calchep__interface/)**  |
| int * | **[twidth](/documentation/code/classes/structgambit_1_1calchep__interface/)**  |
| int * | **[gtwidth](/documentation/code/classes/structgambit_1_1calchep__interface/)**  |
| int * | **[gswidth](/documentation/code/classes/structgambit_1_1calchep__interface/)**  |
| double(**)(char *) | **[aWidth](/documentation/code/classes/structgambit_1_1calchep__interface/)**  |
| double(*)(int, double, REAL *, REAL *, int *) | **[sqme](/documentation/code/classes/structgambit_1_1calchep__interface/)**  |
| char *(*)(int, int, int *, int *) | **[den_info](/documentation/code/classes/structgambit_1_1calchep__interface/)**  |
| [colorBasis](/documentation/code/classes/structgambit_1_1colorbasis/) * | **[cb](/documentation/code/classes/structgambit_1_1calchep__interface/)**  |

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

Updated on 2022-09-08 at 01:05:15 +0000