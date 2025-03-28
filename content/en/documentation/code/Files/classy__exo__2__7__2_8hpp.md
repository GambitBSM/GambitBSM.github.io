---
title: "file frontends/classy_exo_2_7_2.hpp"

description: "[No description available]"

---

# file frontends/classy_exo_2_7_2.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[BACKENDNAME](/documentation/code/files/classy__exo__2__7__2_8hpp/#define-backendname)**  |
|  | **[BACKENDLANG](/documentation/code/files/classy__exo__2__7__2_8hpp/#define-backendlang)**  |
|  | **[VERSION](/documentation/code/files/classy__exo__2__7__2_8hpp/#define-version)**  |
|  | **[SAFE_VERSION](/documentation/code/files/classy__exo__2__7__2_8hpp/#define-safe-version)**  |
|  | **[REFERENCE](/documentation/code/files/classy__exo__2__7__2_8hpp/#define-reference)**  |

## Detailed Description


**Author**: 

  * Janina Renk ([janina.renk@fysik.su.se](mailto:janina.renk@fysik.su.se)) 
  * Sanjay Bloor ([sanjay.bloor12@imperial.ac.uk](mailto:sanjay.bloor12@imperial.ac.uk)) 
  * Patrick Stoecker ([stoecker@physik.rwth-aachen.de](mailto:stoecker@physik.rwth-aachen.de)) 


**Date**: 

  * 2019 June 
  * 2020 July
  * 2019 June
  * 2019 July 
  * 2020 January 
  * 2021 January


Frontend header for the classy_exo backend.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define BACKENDNAME

```
#define BACKENDNAME classy_exo
```


### define BACKENDLANG

```
#define BACKENDLANG Python
```


### define VERSION

```
#define VERSION 2.7.2
```


### define SAFE_VERSION

```
#define SAFE_VERSION 2_7_2
```


### define REFERENCE

```
#define REFERENCE Blas:2011rf,Stocker:2018avm
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Frontend header for the classy_exo backend.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Janina Renk
///          (janina.renk@fysik.su.se)
///  \date 2019 June
///  \date 2020 July
///
///  \author Sanjay Bloor
///          (sanjay.bloor12@imperial.ac.uk)
///  \date 2019 June
///
///  \author Patrick Stoecker
///          (stoecker@physik.rwth-aachen.de)
///  \date 2019 July
///  \date 2020 January
///  \date 2021 January
///
///  *********************************************

#define BACKENDNAME classy_exo
#define BACKENDLANG Python
#define VERSION 2.7.2
#define SAFE_VERSION 2_7_2
#define REFERENCE Blas:2011rf,Stocker:2018avm

LOAD_LIBRARY

#ifdef HAVE_PYBIND11

  BE_CONV_FUNCTION(get_classy_cosmo_object, pybind11::object, (), "get_classy_cosmo_object")
  BE_CONV_FUNCTION(get_classy_backendDir, std::string, (), "get_classy_backendDir")

  BE_CONV_FUNCTION(class_get_rs,        double, (), "class_get_rs")
  BE_CONV_FUNCTION(class_get_tau_reio,  double, (), "class_get_tau_reio")
  BE_CONV_FUNCTION(class_get_z_reio,    double, (), "class_get_z_reio")
  BE_CONV_FUNCTION(class_get_Neff,      double, (), "class_get_Neff")
  BE_CONV_FUNCTION(class_get_sigma8,      double, (), "class_get_sigma8")
  BE_CONV_FUNCTION(class_get_Omega0_r,    double, (), "class_get_Omega0_r")
  BE_CONV_FUNCTION(class_get_Omega0_ur,     double, (), "class_get_Omega0_ur")
  BE_CONV_FUNCTION(class_get_Omega0_m,    double, (), "class_get_Omega0_m")
  BE_CONV_FUNCTION(class_get_Omega0_ncdm_tot, double, (), "class_get_Omega0_ncdm_tot")
  BE_CONV_FUNCTION(class_get_Omega0_Lambda,   double, (), "class_get_Omega0_Lambda")
  BE_CONV_FUNCTION(class_get_H0,              double, (), "class_get_H0")
  BE_CONV_FUNCTION(class_get_Da, double, (double), "class_get_Da")
  BE_CONV_FUNCTION(class_get_Dl, double, (double), "class_get_Dl")
  BE_CONV_FUNCTION(class_get_Hz, double, (double), "class_get_Hz")

  BE_CONV_FUNCTION(class_get_lensed_cl, std::vector<double>, (str), "class_get_lensed_cl")
  BE_CONV_FUNCTION(class_get_unlensed_cl, std::vector<double>, (str), "class_get_unlensed_cl")
  BE_CONV_FUNCTION(class_get_scale_independent_growth_factor,   double, (double), "class_get_scale_independent_growth_factor")
  BE_CONV_FUNCTION(class_get_scale_independent_growth_factor_f,   double, (double), "class_get_scale_independent_growth_factor_f")

  BE_INI_DEPENDENCY(classy_input_params, Classy_input)

#endif

// Undefine macros to avoid conflict with other backends
#include "gambit/Backends/backend_undefs.hpp"
```


-------------------------------

Updated on 2025-02-12 at 16:10:36 +0000
