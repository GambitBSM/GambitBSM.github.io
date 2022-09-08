---
title: "struct Gambit::Printers::Record"
description: "Structure to hold data for a single model point. "

---

# struct Gambit::Printers::Record



Structure to hold data for a single model point. 


`#include <asciiprinter.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Record](/documentation/code/classes/structgambit_1_1printers_1_1record/#function-gambitprintersrecord-record)**() |
| void | **[reset](/documentation/code/classes/structgambit_1_1printers_1_1record/#function-gambitprintersrecord-reset)**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| LineBuf | **[data](/documentation/code/classes/structgambit_1_1printers_1_1record/#variable-gambitprintersrecord-data)** <br>The data; each functor outputs a vector of doubles. We index these by vertexID.  |
| bool | **[readyToPrint](/documentation/code/classes/structgambit_1_1printers_1_1record/#variable-gambitprintersrecord-readytoprint)** <br>Flag to indicate if record is available to send for output.  |

## Public Functions Documentation

### function Record

```
Record()
```


### function reset

```
void reset()
```


## Public Attributes Documentation

### variable data

```
LineBuf data;
```

The data; each functor outputs a vector of doubles. We index these by vertexID. 

### variable readyToPrint

```
bool readyToPrint;
```

Flag to indicate if record is available to send for output. 

-------------------------------

Updated on 2022-09-08 at 01:48:56 +0000