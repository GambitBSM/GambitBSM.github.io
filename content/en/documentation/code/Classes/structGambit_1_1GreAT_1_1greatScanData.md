---
title: "struct Gambit::GreAT::greatScanData"
description: "Structure for passing likelihood and printer data through GreAT to the objective function. "

---

# struct Gambit::GreAT::greatScanData



Structure for passing likelihood and printer data through GreAT to the objective function. 


`#include <great.hpp>`

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [Scanner::like_ptr](/documentation/code/classes/classgambit_1_1scanner_1_1like__ptr/) | **[likelihood_function](/documentation/code/classes/structgambit_1_1great_1_1greatscandata/)**  |
| [Scanner::printer_interface](/documentation/code/namespaces/namespacegambit_1_1scanner/) * | **[printer](/documentation/code/classes/structgambit_1_1great_1_1greatscandata/)**  |
| double | **[min_logLike](/documentation/code/classes/structgambit_1_1great_1_1greatscandata/)**  |

## Public Attributes Documentation

### variable likelihood_function

```
Scanner::like_ptr likelihood_function;
```


### variable printer

```
Scanner::printer_interface * printer;
```


### variable min_logLike

```
double min_logLike;
```


-------------------------------

Updated on 2022-09-08 at 01:05:17 +0000