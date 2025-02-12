---
title: "file frontends/ATLAS_FullLikes_1_0.cpp"

description: "[No description available]"

---

# file frontends/ATLAS_FullLikes_1_0.cpp

[No description available] [More...](#detailed-description)

## Detailed Description


**Author**: Chris Chang ([c.j.chang@fys.uio.no](mailto:c.j.chang@fys.uio.no)) 

**Date**: 2021

Frontend source for the ATLAS_FullLikes 1.0 backend.



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Frontend source for the ATLAS_FullLikes 1.0 
///  backend.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Chris Chang
///          (c.j.chang@fys.uio.no)
///  \date 2021
///
///  *********************************************

#include "gambit/Backends/frontend_macros.hpp"
#include "gambit/Backends/frontends/ATLAS_FullLikes_1_0.hpp"

BE_INI_FUNCTION {}
END_BE_INI_FUNCTION

BE_NAMESPACE
{

#ifdef HAVE_PYBIND11
  // Wrapper for the FullLikes_Evaluate function
  double FullLikes_Evaluate(std::map<str,double>& SRsignal, const str& ana_name)
  {
    // Convert the std::map to a PyDict
    pybind11::dict n_sig_scaled;

    for (auto mydict : SRsignal)
    {
      pybind11::str SRName = mydict.first;
      n_sig_scaled[SRName] = mydict.second;
    }

    // Pull the delta LogLike from the backend
    try
    {
      return FullLikes_Evaluate_pydict(n_sig_scaled,ana_name);
    }
    catch (const std::exception& e)
    {
        invalid_point().raise(e.what());
    }
    catch (...)
    {
      invalid_point().raise("ATLAS FullLikes has failed on this point (perhaps in the scipy optimise).");
    }

    // Squash a warning about no return
    return 0.0;
  }
#else
  double FullLikes_Evaluate(std::map<str,double>& SRsignal, const str& ana_name)
  {
    backend_error().raise(LOCAL_INFO, "pybind11 has been excluded, but is required for the ATLAS_FullLikes backend.\n");
    return 0.0; // Just returning a number to be consistent with types
  }
#endif

}
END_BE_NAMESPACE
```


-------------------------------

Updated on 2025-02-12 at 15:36:43 +0000
