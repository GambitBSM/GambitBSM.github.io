---
title: "file Rivet_3_1_5/Rivet_3_1_5/loaded_types.hpp"

description: "[No description available]"

---

# file Rivet_3_1_5/Rivet_3_1_5/loaded_types.hpp

[No description available]

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[Rivet_3_1_5_all_data](/documentation/code/files/rivet__3__1__5_2loaded__types_8hpp/#define-rivet-3-1-5-all-data)**  |




## Macros Documentation

### define Rivet_3_1_5_all_data

```
#define Rivet_3_1_5_all_data   (( /*class*/(Rivet)(AnalysisHandler),    /*constructors*/(("Factory_AnalysisHandler_0__BOSS_1",(const std::string&))) (("Factory_AnalysisHandler_1__BOSS_2",())) )) \
```


## Source code

```
#ifndef __loaded_types_Rivet_3_1_5_hpp__
#define __loaded_types_Rivet_3_1_5_hpp__ 1

#ifndef EXCLUDE_YODA
#ifndef EXCLUDE_HEPMC

#include "gambit/Utils/begin_ignore_warnings_rivet_backend.hpp"
#include "wrapper_AnalysisHandler.hh"
#include "identification.hpp"
#include "gambit/Utils/end_ignore_warnings.hpp"

// Indicate which types are provided by this backend, and what the symbols of their factories are.
#define Rivet_3_1_5_all_data \
  (( /*class*/(Rivet)(AnalysisHandler),    /*constructors*/(("Factory_AnalysisHandler_0__BOSS_1",(const std::string&))) (("Factory_AnalysisHandler_1__BOSS_2",())) )) \

// If the default version has been loaded, set it as default.
#if ALREADY_LOADED(CAT_3(BACKENDNAME,_,CAT(Default_,BACKENDNAME)))
  SET_DEFAULT_VERSION_FOR_LOADING_TYPES(BACKENDNAME,SAFE_VERSION,CAT(Default_,BACKENDNAME))
#endif

// Undefine macros to avoid conflict with other backends.
#include "gambit/Backends/backend_undefs.hpp"
 
#endif
#endif

#endif /* __loaded_types_Rivet_3_1_5_hpp__ */
```


-------------------------------

Updated on 2023-06-26 at 21:36:57 +0000
