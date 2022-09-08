---
title: "file Utils/export_symbols.hpp"

description: "[No description available]"

---

# file Utils/export_symbols.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[EXPORT_SYMBOLS](/documentation/code/files/export__symbols_8hpp/#define-export-symbols)**  |

## Detailed Description


**Author**: 

  * Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 
  * Ben Farmer ([b.farmer@imperial.ac.uk](mailto:b.farmer@imperial.ac.uk)) 


**Date**: 

  * 2018 Oct
  * 2018 Oct


Helper macro for controlling symbol visibility in shared libraries



------------------

Authors:



------------------




## Macros Documentation

### define EXPORT_SYMBOLS

```
#define EXPORT_SYMBOLS __attribute__ ((visibility ("default")))
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Helper macro for controlling symbol visibility in shared libraries
///
///  *********************************************
///
///  Authors:
///  <!-- add name and date if you modify -->
///
///  \author Pat Scott
///          (p.scott@imperial.ac.uk)
///  \date 2018 Oct
///
///  \author Ben Farmer
///          (b.farmer@imperial.ac.uk)
///  \date 2018 Oct
///
///  *********************************************

#ifndef __export_symbols_hpp__
#define __export_symbols_hpp__

/// \name Symbol visibility macro
#define EXPORT_SYMBOLS __attribute__ ((visibility ("default")))

#endif
```


-------------------------------

Updated on 2022-09-08 at 03:08:04 +0000
