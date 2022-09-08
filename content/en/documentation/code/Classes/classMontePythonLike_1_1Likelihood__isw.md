---
title: "class MontePythonLike::Likelihood_isw"

description: "[No description available]"

---

# class MontePythonLike::Likelihood_isw



[No description available]

Inherits from [MontePythonLike.Likelihood](/documentation/code/classes/classmontepythonlike_1_1likelihood/), [MontePythonLike.Likelihood](/documentation/code/classes/classmontepythonlike_1_1likelihood/), object

## Public Functions

|                | Name           |
| -------------- | -------------- |
| def | **[__init__](/documentation/code/classes/classmontepythonlike_1_1likelihood__isw/)**(self self, path path, data data, command_line command_line) |
| def | **[bin_cl](/documentation/code/classes/classmontepythonlike_1_1likelihood__isw/)**(self self, l l, cl cl, bins bins, cov cov =None) |
| def | **[integrand_cross](/documentation/code/classes/classmontepythonlike_1_1likelihood__isw/)**(self self, z z, cosmo cosmo, l l) |
| def | **[integrand_auto](/documentation/code/classes/classmontepythonlike_1_1likelihood__isw/)**(self self, z z, cosmo cosmo, l l) |
| def | **[compute_loglkl](/documentation/code/classes/classmontepythonlike_1_1likelihood__isw/)**(self self, cosmo cosmo, data data, b b) |
| def | **[__init__](/documentation/code/classes/classmontepythonlike_1_1likelihood__isw/)**(self self, path path, data data, command_line command_line) |
| def | **[bin_cl](/documentation/code/classes/classmontepythonlike_1_1likelihood__isw/)**(self self, l l, cl cl, bins bins, cov cov =None) |
| def | **[integrand_cross](/documentation/code/classes/classmontepythonlike_1_1likelihood__isw/)**(self self, z z, cosmo cosmo, l l) |
| def | **[integrand_auto](/documentation/code/classes/classmontepythonlike_1_1likelihood__isw/)**(self self, z z, cosmo cosmo, l l) |
| def | **[compute_loglkl](/documentation/code/classes/classmontepythonlike_1_1likelihood__isw/)**(self self, cosmo cosmo, data data, b b) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| | **[l_cross](/documentation/code/classes/classmontepythonlike_1_1likelihood__isw/)**  |
| | **[l_auto](/documentation/code/classes/classmontepythonlike_1_1likelihood__isw/)**  |
| | **[bins_cross](/documentation/code/classes/classmontepythonlike_1_1likelihood__isw/)**  |
| | **[bins_auto](/documentation/code/classes/classmontepythonlike_1_1likelihood__isw/)**  |
| | **[cov_binned_cross](/documentation/code/classes/classmontepythonlike_1_1likelihood__isw/)**  |
| | **[cov_binned_auto](/documentation/code/classes/classmontepythonlike_1_1likelihood__isw/)**  |
| | **[dndz](/documentation/code/classes/classmontepythonlike_1_1likelihood__isw/)**  |
| | **[norm](/documentation/code/classes/classmontepythonlike_1_1likelihood__isw/)**  |

## Additional inherited members

**Public Functions inherited from [MontePythonLike.Likelihood](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**

|                | Name           |
| -------------- | -------------- |
| def | **[loglkl](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, cosmo cosmo, data data) |
| def | **[raise_fiducial_model_err](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self) |
| def | **[read_from_file](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, path path, data data, command_line command_line) |
| def | **[get_cl](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, cosmo cosmo, l_max l_max =-1) |
| def | **[get_unlensed_cl](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, cosmo cosmo, l_max l_max =-1) |
| def | **[need_cosmo_arguments](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, data data, dictionary dictionary) |
| def | **[read_contamination_spectra](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, data data) |
| def | **[add_contamination_spectra](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, cl cl, data data) |
| def | **[add_nuisance_prior](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, lkl lkl, data data) |
| def | **[computeLikelihood](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, ctx ctx) |
| def | **[loglkl](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, cosmo cosmo, data data) |
| def | **[raise_fiducial_model_err](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self) |
| def | **[read_from_file](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, path path, data data, command_line command_line) |
| def | **[get_cl](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, cosmo cosmo, l_max l_max =-1) |
| def | **[get_unlensed_cl](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, cosmo cosmo, l_max l_max =-1) |
| def | **[need_cosmo_arguments](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, data data, dictionary dictionary) |
| def | **[read_contamination_spectra](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, data data) |
| def | **[add_contamination_spectra](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, cl cl, data data) |
| def | **[add_nuisance_prior](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, lkl lkl, data data) |
| def | **[computeLikelihood](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, ctx ctx) |

**Public Attributes inherited from [MontePythonLike.Likelihood](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**

|                | Name           |
| -------------- | -------------- |
| | **[name](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**  |
| | **[folder](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**  |
| | **[data_directory](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**  |
| | **[default_values](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**  |
| | **[need_update](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**  |
| | **[use_nuisance](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**  |
| | **[nuisance](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**  |
| | **[path](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**  |
| | **[dictionary](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**  |

**Public Functions inherited from [MontePythonLike.Likelihood](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**

|                | Name           |
| -------------- | -------------- |
| def | **[loglkl](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, cosmo cosmo, data data) |
| def | **[raise_fiducial_model_err](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self) |
| def | **[read_from_file](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, path path, data data, command_line command_line) |
| def | **[get_cl](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, cosmo cosmo, l_max l_max =-1) |
| def | **[get_unlensed_cl](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, cosmo cosmo, l_max l_max =-1) |
| def | **[need_cosmo_arguments](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, data data, dictionary dictionary) |
| def | **[read_contamination_spectra](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, data data) |
| def | **[add_contamination_spectra](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, cl cl, data data) |
| def | **[add_nuisance_prior](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, lkl lkl, data data) |
| def | **[computeLikelihood](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, ctx ctx) |
| def | **[loglkl](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, cosmo cosmo, data data) |
| def | **[raise_fiducial_model_err](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self) |
| def | **[read_from_file](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, path path, data data, command_line command_line) |
| def | **[get_cl](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, cosmo cosmo, l_max l_max =-1) |
| def | **[get_unlensed_cl](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, cosmo cosmo, l_max l_max =-1) |
| def | **[need_cosmo_arguments](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, data data, dictionary dictionary) |
| def | **[read_contamination_spectra](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, data data) |
| def | **[add_contamination_spectra](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, cl cl, data data) |
| def | **[add_nuisance_prior](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, lkl lkl, data data) |
| def | **[computeLikelihood](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, ctx ctx) |

**Public Attributes inherited from [MontePythonLike.Likelihood](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**

|                | Name           |
| -------------- | -------------- |
| | **[name](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**  |
| | **[folder](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**  |
| | **[data_directory](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**  |
| | **[default_values](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**  |
| | **[need_update](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**  |
| | **[use_nuisance](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**  |
| | **[nuisance](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**  |
| | **[path](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**  |
| | **[dictionary](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**  |


## Public Functions Documentation

### function __init__

```
def __init__(
    self self,
    path path,
    data data,
    command_line command_line
)
```


**Reimplements**: [MontePythonLike::Likelihood::__init__](/documentation/code/classes/classmontepythonlike_1_1likelihood/)




```
It copies the content of self.path from the initialization routine of
the :class:`Data <data.Data>` class, and defines a handful of useful
methods, that every likelihood might need.

If the nuisance parameters required to compute this likelihood are not
defined (either fixed or varying), the code will stop.

Parameters
----------
data : class
    Initialized instance of :class:`Data <data.Data>`
command_line : NameSpace
    NameSpace containing the command line arguments```


### function bin_cl

```
def bin_cl(
    self self,
    l l,
    cl cl,
    bins bins,
    cov cov =None
)
```


### function integrand_cross

```
def integrand_cross(
    self self,
    z z,
    cosmo cosmo,
    l l
)
```


### function integrand_auto

```
def integrand_auto(
    self self,
    z z,
    cosmo cosmo,
    l l
)
```


### function compute_loglkl

```
def compute_loglkl(
    self self,
    cosmo cosmo,
    data data,
    b b
)
```


### function __init__

```
def __init__(
    self self,
    path path,
    data data,
    command_line command_line
)
```


**Reimplements**: [MontePythonLike::Likelihood::__init__](/documentation/code/classes/classmontepythonlike_1_1likelihood/)




```
It copies the content of self.path from the initialization routine of
the :class:`Data <data.Data>` class, and defines a handful of useful
methods, that every likelihood might need.

If the nuisance parameters required to compute this likelihood are not
defined (either fixed or varying), the code will stop.

Parameters
----------
data : class
    Initialized instance of :class:`Data <data.Data>`
command_line : NameSpace
    NameSpace containing the command line arguments```


### function bin_cl

```
def bin_cl(
    self self,
    l l,
    cl cl,
    bins bins,
    cov cov =None
)
```


### function integrand_cross

```
def integrand_cross(
    self self,
    z z,
    cosmo cosmo,
    l l
)
```


### function integrand_auto

```
def integrand_auto(
    self self,
    z z,
    cosmo cosmo,
    l l
)
```


### function compute_loglkl

```
def compute_loglkl(
    self self,
    cosmo cosmo,
    data data,
    b b
)
```


## Public Attributes Documentation

### variable l_cross

```
l_cross;
```


### variable l_auto

```
l_auto;
```


### variable bins_cross

```
bins_cross;
```


### variable bins_auto

```
bins_auto;
```


### variable cov_binned_cross

```
cov_binned_cross;
```


### variable cov_binned_auto

```
cov_binned_auto;
```


### variable dndz

```
dndz;
```


### variable norm

```
norm;
```


-------------------------------

Updated on 2022-09-08 at 01:05:15 +0000