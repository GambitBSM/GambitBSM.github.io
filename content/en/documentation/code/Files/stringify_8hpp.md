---
title: "file Utils/stringify.hpp"

description: "[No description available]"

---

# file Utils/stringify.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[STRINGIFY](/documentation/code/files/stringify_8hpp/#define-stringify)**(X)  |
|  | **[STRINGIFY2](/documentation/code/files/stringify_8hpp/#define-stringify2)**(X)  |
|  | **[SAFE_STRINGIFY](/documentation/code/files/stringify_8hpp/#define-safe-stringify)**(...) <br>Stringification macros that can stringify arguments with commas.  |
|  | **[SAFE_STRINGIFY2](/documentation/code/files/stringify_8hpp/#define-safe-stringify2)**(...)  |

## Detailed Description


**Author**: 

  * Pat Scott ([patscott@physics.mcgill.ca](mailto:patscott@physics.mcgill.ca)) 
  * Ben Farmer ([benjamin.farmer@fysik.su.se](mailto:benjamin.farmer@fysik.su.se)) 


**Date**: 

  * 2013 Apr, Oct 
  * 2014 Mar
  * 2016 Jan


Stringification macro. Separated from other util_macros to facilicate code factorisation.



------------------

Authors:



------------------




## Macros Documentation

### define STRINGIFY

```
#define STRINGIFY(
    X
)
STRINGIFY2(X)
```


### define STRINGIFY2

```
#define STRINGIFY2(
    X
)
#X
```


### define SAFE_STRINGIFY

```
#define SAFE_STRINGIFY(
    ...
)
SAFE_STRINGIFY2(__VA_ARGS__)
```

Stringification macros that can stringify arguments with commas. 

### define SAFE_STRINGIFY2

```
#define SAFE_STRINGIFY2(
    ...
)
#__VA_ARGS__
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Stringification macro. Separated from other
///  util_macros to facilicate code factorisation.
///
///  *********************************************
///
///  Authors: 
///  <!-- add name and date if you modify -->
///   
///  \author Pat Scott
///          (patscott@physics.mcgill.ca)
///  \date 2013 Apr, Oct
///  \date 2014 Mar
///
///  \author Ben Farmer
///          (benjamin.farmer@fysik.su.se)
///  \date 2016 Jan
///
///  *********************************************

#ifndef __stringify_hpp__
#define __stringify_hpp__

/// \name Stringification macros
/// @{
#define STRINGIFY(X) STRINGIFY2(X)
#define STRINGIFY2(X) #X
/// Stringification macros that can stringify arguments with commas
#define SAFE_STRINGIFY(...) SAFE_STRINGIFY2(__VA_ARGS__)
#define SAFE_STRINGIFY2(...) #__VA_ARGS__
/// @}

#endif //defined __util_macros_hpp__
```


-------------------------------

Updated on 2022-09-08 at 03:42:00 +0000
