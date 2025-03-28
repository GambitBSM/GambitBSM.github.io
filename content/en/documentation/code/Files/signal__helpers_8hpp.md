---
title: "file Utils/signal_helpers.hpp"

description: "[No description available]"

---

# file Utils/signal_helpers.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |

## Detailed Description


**Author**: Ben Farmer ([benjamin.farmer@fysik.su.se](mailto:benjamin.farmer@fysik.su.se)) 

**Date**: 2015 Oct

Helper functions for dealing with POSIX signals.

It seems that odd things can happen if signals are caught inside some of our OpenMP blocks. To prevent this, the following functions can be used to prevent signals being acted upon until after they are unblocked.

See e.g. [http://www.gnu.org/software/libc/manual/html_node/Blocking-Signals.html](http://www.gnu.org/software/libc/manual/html_node/Blocking-Signals.html)

For optimum safety it would probably be best to add these around all OpenMP blocks, though I am not of the maximum time for which the signal block can be maintained.

The blocks act upon a globally defined set of signals, which can be manipulated using other function declared in this file.



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Helper functions for dealing with POSIX
///  signals.
///
///  It seems that odd things can happen if 
///  signals are caught inside some of our OpenMP 
///  blocks. To prevent this, the following 
///  functions can be used to prevent signals 
///  being acted upon until after they are 
///  unblocked. 
///
///  See e.g. http://www.gnu.org/software/libc/manual/html_node/Blocking-Signals.html
///
///  For optimum safety it would probably be best
///  to add these around all OpenMP blocks, though
///  I am not of the maximum time for which the 
///  signal block can be maintained.
///
///  The blocks act upon a globally defined set of 
///  signals, which can be manipulated using other
///  function declared in this file.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///   
///  \author Ben Farmer
///          (benjamin.farmer@fysik.su.se)
///  \date 2015 Oct
///
///  *********************************************

#ifndef __signal_helpers_hpp__
#define __signal_helpers_hpp__

#include <signal.h>

namespace Gambit
{

   /// @{ Signal blocking/unblocking
   void block_signals();    
   void unblock_signals();
   /// @}

   // Retrieve the global signal mask set
   sigset_t* signal_mask();
}

#endif
```


-------------------------------

Updated on 2025-02-12 at 16:10:33 +0000
