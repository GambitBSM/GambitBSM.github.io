---
title: "file coutprinter/coutprinter.cpp"

description: "[No description available]"

---

# file coutprinter/coutprinter.cpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::Printers](/documentation/code/namespaces/namespacegambit_1_1printers/)** <br>Forward declaration.  |

## Detailed Description


**Author**: Ben Farmer ([b.farmer@imperial.ac.uk](mailto:b.farmer@imperial.ac.uk)) 

**Date**: 2018 Apr

"cout" printer class member function definitions



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  "cout" printer class member function definitions
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Ben Farmer
///          (b.farmer@imperial.ac.uk)
///  \date 2018 Apr
///
///  *********************************************


// Standard libraries
#include <map>
#include <vector>
#include <algorithm>
#include <ios>
#include <sstream>
#include <fstream>
#include <iomanip>

// Gambit
#include "gambit/Printers/printers/coutprinter.hpp"
#include "gambit/Utils/standalone_error_handlers.hpp"
#include "gambit/Utils/stream_overloads.hpp"
#include "gambit/Utils/util_functions.hpp"

// Code!
namespace Gambit
{

  namespace Printers
  {

    // Constructor
    coutPrinter::coutPrinter(const Options& options, BasePrinter* const primary)
      : BasePrinter(primary,options.getValueOrDef<bool>(false,"auxilliary"))
    {
      set_resume(false);
      // No other setup required for this printer.
    }

    /// Initialisation function
    // Run by dependency resolver, which supplies the functors with a vector of VertexIDs whose requiresPrinting flags are set to true.
    void coutPrinter::initialise(const std::vector<int>& /*printmevec*/)
    {
    }

    /// Do final buffer dumps
    void coutPrinter::finalise(bool /*abnormal*/)
    {
    }

    /// Reset printer and output to clean state
    void coutPrinter::reset(bool)
    {
        // Nothing actually stored by this printer so no need for this to do anything
    }

    /// Perform any point-specific logic 
    void coutPrinter::check_point(unsigned int mpirank, unsigned long pointID)
    {
        // Actually I think it is just good enough to pre-pend the 
        // line with the point information
        std::cout << mpirank << ", " << pointID << ": "; // No endline
    }

    /// Permanently unavailable for this printer
    Options coutPrinter::resume_reader_options()
    {
        std::ostringstream err;
        err << "The cout printer is intrinsically incapable of reading from previous output, since the previous output just goes to cout. So you cannot use the 'resume_reader_options' function with this printer. This means that the coutPrinter cannot be used with e.g. the postprocessor v2 whilst also resuming. Sorry! (Note, postprocessor v1 should be able to resume with the coutPrinter)" << std::endl; 
        printer_error().raise(LOCAL_INFO, err.str());
        return Options();
    }
 
  } // end namespace printers
} // end namespace Gambit
```


-------------------------------

Updated on 2025-02-12 at 16:10:34 +0000
