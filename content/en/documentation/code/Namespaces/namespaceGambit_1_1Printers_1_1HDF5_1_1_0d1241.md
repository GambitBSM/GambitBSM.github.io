---
title: "namespace Gambit::Printers::HDF5::@1241"
description: "Close hdf5 type ID. "

---

# namespace Gambit::Printers::HDF5::@1241

Close hdf5 type ID.  [More...](#detailed-description)

## Detailed Description

Close hdf5 type ID. 

Close hdf5 group State for [errorsOff()](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-errorsoff) / [errorsOn()](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-errorson). The bool guard errors_are_off ensures that a redundant [errorsOff()](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-errorsoff) called while errors are already off does NOT overwrite the saved handler with the NULL handler. 






-------------------------------

Updated on 2026-11-03 at 14:50:42 +0000