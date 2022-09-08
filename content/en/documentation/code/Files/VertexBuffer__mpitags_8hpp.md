---
title: "file Printers/VertexBuffer_mpitags.hpp"

description: "[No description available]"

---

# file Printers/VertexBuffer_mpitags.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::Printers](/documentation/code/namespaces/namespacegambit_1_1printers/)** <br>Forward declaration.  |

## Detailed Description


**Author**: Ben Farmer ([benjamin.farmer@fysik.su.se](mailto:benjamin.farmer@fysik.su.se)) 

**Date**: 2015 May

MPI tag definitions for the VertexBuffer classes.



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  MPI tag definitions for the VertexBuffer classes.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///   
///  \author Ben Farmer
///          (benjamin.farmer@fysik.su.se)
///  \date 2015 May
///
///  *********************************************


#ifndef __vertexbuffer_mpitags_hpp__
#define __vertexbuffer_mpitags_hpp__

namespace Gambit
{
  namespace Printers 
  {

    /// Reserved tags for MPI messages
    /// TAG_REQ   - for messages registering/requesting a new tags
    /// INIT_PASS - for messages registering completion of initialisation
    /// PPFILES_PASS - for messages registering completion of preprocessing of existing files (combination/deletion)
    /// FINAL_PASS - for messages registering passing of checkpoint during finalise
    /// PPID_SEND - for messages transferring point ID information
    /// N_BUFFERS_SENT - for messages counting the number of buffer transfer messages being sent in one 'package' 
    /// RA_BUFFERS_SENT - Contains no data, just indicates that RA buffer messages from some process are waiting to send.
    /// FINAL_SYNC - Contains no data, used to trigger final buffer sends and receives.
    enum Tags { TAG_REQ=0, INIT_PASS, PPFILES_PASS, FINAL_PASS, PPID_SEND, N_BUFFERS_SENT, RA_BUFFERS_SENT, FINAL_SYNC };
    const int FIRST_EMPTY_TAG = FINAL_SYNC+1;

  }
}
#endif
```


-------------------------------

Updated on 2022-09-08 at 03:42:01 +0000
