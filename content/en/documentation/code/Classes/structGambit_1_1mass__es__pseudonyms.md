---
title: "struct Gambit::mass_es_pseudonyms"
description: "Structure to hold mass eigenstate pseudonyms for gauge eigenstates. "

---

# struct Gambit::mass_es_pseudonyms



Structure to hold mass eigenstate pseudonyms for gauge eigenstates. 


`#include <mssm_slhahelp.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[mass_es_pseudonyms](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**()<br>Constructor.  |
| void | **[fill](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**(const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssm, double tol, bool pt_error, bool debug)<br>Fill strings and maps in struct.  |
| void | **[refill](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**(const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssm, double tol, bool pt_error, bool debug)<br>Refill strings and maps in struct.  |
| void | **[debug_print](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**(const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssm)<br>Debug printer for pseudonyms.  |
| void | **[debug_print_gauge](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**(const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssm, [str](/documentation/code/namespaces/namespacegambit/) & gauge_es, [str](/documentation/code/namespaces/namespacegambit/) & mass_es, double & max_mix)<br>Gauge state debug printer for pseudonyms.  |
| void | **[debug_print_family](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**(const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssm, [str](/documentation/code/namespaces/namespacegambit/) & family_state, [str](/documentation/code/namespaces/namespacegambit/) & mass_es, double & mix_mag_sq, double & tol)<br>Family state debug printer for pseudonyms.  |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [str](/documentation/code/namespaces/namespacegambit/) | **[isdl](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[isul](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[issl](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[iscl](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[isb1](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[ist1](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[isell](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[isnel](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[ismul](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[isnmul](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[istau1](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[isntaul](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[isdr](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[isur](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[issr](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[iscr](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[isb2](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[ist2](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[iselr](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[ismur](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[istau2](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[isdlbar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[isulbar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[isslbar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[isclbar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[isb1bar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[ist1bar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[isellbar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[isnelbar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[ismulbar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[isnmulbar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[istau1bar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[isntaulbar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[isdrbar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[isurbar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[issrbar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[iscrbar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[isb2bar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[ist2bar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[iselrbar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[ismurbar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[istau2bar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/), [str](/documentation/code/namespaces/namespacegambit/) > | **[gauge_family_eigenstates](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)** <br>Maps relating the pseudonym strings in both directions.  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/), [str](/documentation/code/namespaces/namespacegambit/) > | **[mass_eigenstates](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)**  |
| bool | **[filled](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/)** <br>Struct has already been filled or not.  |

## Public Functions Documentation

### function mass_es_pseudonyms

```
inline mass_es_pseudonyms()
```

Constructor. 

### function fill

```
void fill(
    const SubSpectrum & mssm,
    double tol,
    bool pt_error,
    bool debug
)
```

Fill strings and maps in struct. 

Fill strings in struct. 


### function refill

```
void refill(
    const SubSpectrum & mssm,
    double tol,
    bool pt_error,
    bool debug
)
```

Refill strings and maps in struct. 

Refill strings in struct. 


### function debug_print

```
void debug_print(
    const SubSpectrum & mssm
)
```

Debug printer for pseudonyms. 

General debug printer for pseudonyms. 


### function debug_print_gauge

```
void debug_print_gauge(
    const SubSpectrum & mssm,
    str & gauge_es,
    str & mass_es,
    double & max_mix
)
```

Gauge state debug printer for pseudonyms. 

### function debug_print_family

```
void debug_print_family(
    const SubSpectrum & mssm,
    str & family_state,
    str & mass_es,
    double & mix_mag_sq,
    double & tol
)
```

Family state debug printer for pseudonyms. 

## Public Attributes Documentation

### variable isdl

```
str isdl;
```


Known pseudonym strings

Particles 


### variable isul

```
str isul;
```


### variable issl

```
str issl;
```


### variable iscl

```
str iscl;
```


### variable isb1

```
str isb1;
```


### variable ist1

```
str ist1;
```


### variable isell

```
str isell;
```


### variable isnel

```
str isnel;
```


### variable ismul

```
str ismul;
```


### variable isnmul

```
str isnmul;
```


### variable istau1

```
str istau1;
```


### variable isntaul

```
str isntaul;
```


### variable isdr

```
str isdr;
```


### variable isur

```
str isur;
```


### variable issr

```
str issr;
```


### variable iscr

```
str iscr;
```


### variable isb2

```
str isb2;
```


### variable ist2

```
str ist2;
```


### variable iselr

```
str iselr;
```


### variable ismur

```
str ismur;
```


### variable istau2

```
str istau2;
```


### variable isdlbar

```
str isdlbar;
```


Anti-particles 


### variable isulbar

```
str isulbar;
```


### variable isslbar

```
str isslbar;
```


### variable isclbar

```
str isclbar;
```


### variable isb1bar

```
str isb1bar;
```


### variable ist1bar

```
str ist1bar;
```


### variable isellbar

```
str isellbar;
```


### variable isnelbar

```
str isnelbar;
```


### variable ismulbar

```
str ismulbar;
```


### variable isnmulbar

```
str isnmulbar;
```


### variable istau1bar

```
str istau1bar;
```


### variable isntaulbar

```
str isntaulbar;
```


### variable isdrbar

```
str isdrbar;
```


### variable isurbar

```
str isurbar;
```


### variable issrbar

```
str issrbar;
```


### variable iscrbar

```
str iscrbar;
```


### variable isb2bar

```
str isb2bar;
```


### variable ist2bar

```
str ist2bar;
```


### variable iselrbar

```
str iselrbar;
```


### variable ismurbar

```
str ismurbar;
```


### variable istau2bar

```
str istau2bar;
```


### variable gauge_family_eigenstates

```
std::map< str, str > gauge_family_eigenstates;
```

Maps relating the pseudonym strings in both directions. 

### variable mass_eigenstates

```
std::map< str, str > mass_eigenstates;
```


### variable filled

```
bool filled;
```

Struct has already been filled or not. 

-------------------------------

Updated on 2022-09-08 at 01:05:16 +0000