---
title: "file Rivet_4_1_0/Rivet_4_1_0/loaded_types.hpp"

description: "[No description available]"

---

# file Rivet_4_1_0/Rivet_4_1_0/loaded_types.hpp

[No description available]

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[Rivet_4_1_0_all_data](/documentation/code/files/rivet__4__1__0_2loaded__types_8hpp/#define-rivet-4-1-0-all-data)**  |




## Macros Documentation

### define Rivet_4_1_0_all_data

```
#define Rivet_4_1_0_all_data   (( /*class*/(Rivet)(AnalysisHandler),    /*constructors*/((("Factory_AnalysisHandler_0__BOSS_1","_Factory_AnalysisHandler_0__BOSS_1"),())) )) \
```


## Source code

```
#ifndef __loaded_types_Rivet_4_1_0_hpp__
#define __loaded_types_Rivet_4_1_0_hpp__ 1

#ifndef EXCLUDE_YODA
#ifndef EXCLUDE_HEPMC

#include "gambit/Utils/begin_ignore_warnings_rivet_backend.hpp"
#include "wrapper_AnalysisHandler.hh"
#include "identification.hpp"
#include "gambit/Utils/end_ignore_warnings.hpp"

// Indicate which types are provided by this backend, and what the symbols of their factories are.
#define Rivet_4_1_0_all_data \
  (( /*class*/(Rivet)(AnalysisHandler),    /*constructors*/((("Factory_AnalysisHandler_0__BOSS_1","_Factory_AnalysisHandler_0__BOSS_1"),())) )) \

// If the default version has been loaded, set it as default.
#if ALREADY_LOADED(CAT_3(BACKENDNAME,_,CAT(Default_,BACKENDNAME)))
  SET_DEFAULT_VERSION_FOR_LOADING_TYPES(BACKENDNAME,SAFE_VERSION,CAT(Default_,BACKENDNAME))
#endif

// Undefine macros to avoid conflict with other backends.
#include "gambit/Backends/backend_undefs.hpp"
 
#endif
#endif

#endif /* __loaded_types_Rivet_4_1_0_hpp__ */
```


-------------------------------

Updated on 2026-11-03 at 14:50:48 +0000
