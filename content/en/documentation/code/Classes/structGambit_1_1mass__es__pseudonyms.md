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
| | **[mass_es_pseudonyms](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#function-gambitmass-es-pseudonyms-mass-es-pseudonyms)**()<br>Constructor.  |
| void | **[fill](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#function-gambitmass-es-pseudonyms-fill)**(const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssm, double tol, bool pt_error, bool debug)<br>Fill strings and maps in struct.  |
| void | **[refill](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#function-gambitmass-es-pseudonyms-refill)**(const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssm, double tol, bool pt_error, bool debug)<br>Refill strings and maps in struct.  |
| void | **[debug_print](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#function-gambitmass-es-pseudonyms-debug-print)**(const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssm)<br>Debug printer for pseudonyms.  |
| void | **[debug_print_gauge](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#function-gambitmass-es-pseudonyms-debug-print-gauge)**(const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssm, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) & gauge_es, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) & mass_es, double & max_mix)<br>Gauge state debug printer for pseudonyms.  |
| void | **[debug_print_family](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#function-gambitmass-es-pseudonyms-debug-print-family)**(const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssm, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) & family_state, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) & mass_es, double & mix_mag_sq, double & tol)<br>Family state debug printer for pseudonyms.  |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[isdl](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-isdl)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[isul](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-isul)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[issl](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-issl)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[iscl](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-iscl)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[isb1](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-isb1)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[ist1](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-ist1)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[isell](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-isell)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[isnel](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-isnel)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[ismul](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-ismul)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[isnmul](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-isnmul)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[istau1](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-istau1)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[isntaul](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-isntaul)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[isdr](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-isdr)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[isur](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-isur)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[issr](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-issr)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[iscr](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-iscr)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[isb2](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-isb2)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[ist2](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-ist2)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[iselr](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-iselr)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[ismur](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-ismur)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[istau2](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-istau2)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[isdlbar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-isdlbar)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[isulbar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-isulbar)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[isslbar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-isslbar)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[isclbar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-isclbar)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[isb1bar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-isb1bar)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[ist1bar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-ist1bar)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[isellbar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-isellbar)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[isnelbar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-isnelbar)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[ismulbar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-ismulbar)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[isnmulbar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-isnmulbar)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[istau1bar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-istau1bar)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[isntaulbar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-isntaulbar)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[isdrbar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-isdrbar)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[isurbar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-isurbar)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[issrbar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-issrbar)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[iscrbar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-iscrbar)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[isb2bar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-isb2bar)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[ist2bar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-ist2bar)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[iselrbar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-iselrbar)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[ismurbar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-ismurbar)**  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[istau2bar](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-istau2bar)**  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str), [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) > | **[gauge_family_eigenstates](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-gauge-family-eigenstates)** <br>Maps relating the pseudonym strings in both directions.  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str), [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) > | **[mass_eigenstates](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-mass-eigenstates)**  |
| bool | **[filled](/documentation/code/classes/structgambit_1_1mass__es__pseudonyms/#variable-gambitmass-es-pseudonyms-filled)** <br>Struct has already been filled or not.  |

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

Updated on 2022-09-08 at 02:00:46 +0000