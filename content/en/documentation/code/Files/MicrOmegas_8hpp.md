---
title: "file backend_types/MicrOmegas.hpp"

description: "[No description available]"

---

# file backend_types/MicrOmegas.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::MicrOmegas](/documentation/code/namespaces/namespacegambit_1_1micromegas/)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| struct | **[Gambit::MicrOmegas::MOcommonSTR](/documentation/code/classes/structgambit_1_1micromegas_1_1mocommonstr/)**  |
| struct | **[Gambit::MicrOmegas::aChannel](/documentation/code/classes/structgambit_1_1micromegas_1_1achannel/)**  |

## Detailed Description


**Author**: 

  * Jonathan Cornell ([jcornell@ucsc.edu](mailto:jcornell@ucsc.edu)) 
  * Ankit Beniwal ([ankit.beniwal@adelaide.edu.au](mailto:ankit.beniwal@adelaide.edu.au)) 


**Date**: 

  * 2014 Sep
  * 2016 Aug


Definitions of container classes for the micrOMEGAs backend.



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Definitions of container classes
///  for the micrOMEGAs backend.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Jonathan Cornell
///          (jcornell@ucsc.edu)
///  \date 2014 Sep
///
///  \author Ankit Beniwal
///          (ankit.beniwal@adelaide.edu.au)
///  \date 2016 Aug
///
///  *********************************************

#ifndef __MicrOmegas_types_hpp__
#define __MicrOmegas_types_hpp__

namespace Gambit
{
  namespace MicrOmegas
  {
    typedef struct { double par[36]; } MOcommonSTR;
    typedef struct { double weight; char*prtcl[5]; } aChannel;
  }
}

#endif // defined __MicrOmegas_types_hpp__
```


-------------------------------

Updated on 2025-02-12 at 16:10:36 +0000
