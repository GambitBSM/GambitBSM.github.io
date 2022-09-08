---
title: "file models/StandardModel_Higgs_running.hpp"

description: "[No description available]"

---

# file models/StandardModel_Higgs_running.hpp

[No description available]

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/standardmodel__higgs__running_8hpp/)**  |




## Macros Documentation

### define MODEL

```
#define MODEL StandardModel_Higgs_running
```


Standard Model Higgs sector parameters with running Lagrangian Higgs mass parameter



------------------

Authors (add name and date if you modify):

Ben Farmer ([benjamin.farmer@fysik.su.se](mailto:benjamin.farmer@fysik.su.se)) 2015 May

James McKay 2015 September 

------------------


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///
///
///  Standard Model Higgs sector parameters
///  with running Lagrangian Higgs mass parameter
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///    Ben Farmer
///          (benjamin.farmer@fysik.su.se)
///    2015 May
///
///    James McKay
///    2015 September
///  *********************************************


#ifndef __StandardModel_Higgs_running_hpp__
#define __StandardModel_Higgs_running_hpp__

#define MODEL StandardModel_Higgs_running
  START_MODEL

  DEFINEPARS(mH,Qin,QEWSB)

 #undef MODEL
#endif
```


-------------------------------

Updated on 2022-09-08 at 01:05:20 +0000
