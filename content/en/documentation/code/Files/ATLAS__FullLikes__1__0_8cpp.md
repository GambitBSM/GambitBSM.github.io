---
title: "file frontends/ATLAS_FullLikes_1_0.cpp"

description: "[No description available]"

---

# file frontends/ATLAS_FullLikes_1_0.cpp

[No description available] [More...](#detailed-description)

## Detailed Description


**Author**: Chris Chang ([christopher.chang@uqconnect.edu.au](mailto:christopher.chang@uqconnect.edu.au)) 

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
///          (christopher.chang@uqconnect.edu.au)
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
    double dll = FullLikes_Evaluate_pydict(n_sig_scaled,ana_name);
    
    return dll;
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

Updated on 2023-06-26 at 21:36:57 +0000
