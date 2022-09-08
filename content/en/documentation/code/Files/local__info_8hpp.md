---
title: "file Utils/local_info.hpp"

description: "[No description available]"

---

# file Utils/local_info.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[LOCAL_INFO](/documentation/code/files/local__info_8hpp/#define-local-info)**  |

## Detailed Description


**Author**: 

  * Pat Scott ([patscott@physics.mcgill.ca](mailto:patscott@physics.mcgill.ca)) 
  * Ben Farmer ([benjamin.farmer@fysik.su.se](mailto:benjamin.farmer@fysik.su.se)) 


**Date**: 

  * 2013 Apr, Oct 
  * 2014 Mar
  * 2016 Jan


LOCAL_INFO macro. Separated from other util_macros because it is used so commonly, and saves including loads of boost headers in unnecessary places.



------------------

Authors:



------------------




## Macros Documentation

### define LOCAL_INFO

```
#define LOCAL_INFO std::string("line ") + STRINGIFY(__LINE__) + " in function " + BOOST_CURRENT_FUNCTION + " of " + __FILE__
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  LOCAL_INFO macro. Separated from other
///  util_macros because it is used so commonly,
///  and saves including loads of boost headers
///  in unnecessary places.
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

#ifndef __local_info_hpp__
#define __local_info_hpp__

#include <string>
#include <boost/current_function.hpp> 
#include "gambit/Utils/stringify.hpp"

/// \name Local information macro.
#define LOCAL_INFO std::string("line ") + STRINGIFY(__LINE__) + " in function " + BOOST_CURRENT_FUNCTION + " of " + __FILE__

#endif //defined __util_macros_hpp__
```


-------------------------------

Updated on 2022-09-08 at 00:43:02 +0000
