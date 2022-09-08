---
title: "class MontePythonLike::Likelihood_sd"

description: "[No description available]"

---

# class MontePythonLike::Likelihood_sd



[No description available]

Inherits from [MontePythonLike.Likelihood](/documentation/code/classes/classmontepythonlike_1_1likelihood/), object

## Public Functions

|                | Name           |
| -------------- | -------------- |
| def | **[__init__](/documentation/code/classes/classmontepythonlike_1_1likelihood__sd/)**(self self, path path, data data, command_line command_line) |
| def | **[eval_spinning_dust](/documentation/code/classes/classmontepythonlike_1_1likelihood__sd/)**(self self, lognu lognu, lognu_p lognu_p) |
| def | **[eval_co_integrated](/documentation/code/classes/classmontepythonlike_1_1likelihood__sd/)**(self self, lognu lognu) |
| def | **[loglkl](/documentation/code/classes/classmontepythonlike_1_1likelihood__sd/)**(self self, cosmo cosmo, data data) |
| def | **[compute_lkl](/documentation/code/classes/classmontepythonlike_1_1likelihood__sd/)**(self self, sd sd, cosmo cosmo, data data) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| | **[noise_from_file](/documentation/code/classes/classmontepythonlike_1_1likelihood__sd/)** <br>Noise spectrum.  |
| | **[noise_file](/documentation/code/classes/classmontepythonlike_1_1likelihood__sd/)**  |
| | **[detector_bin_number](/documentation/code/classes/classmontepythonlike_1_1likelihood__sd/)**  |
| | **[detector_nu_min](/documentation/code/classes/classmontepythonlike_1_1likelihood__sd/)**  |
| | **[detector_nu_max](/documentation/code/classes/classmontepythonlike_1_1likelihood__sd/)**  |
| | **[nu_range](/documentation/code/classes/classmontepythonlike_1_1likelihood__sd/)**  |
| | **[noise_Ic](/documentation/code/classes/classmontepythonlike_1_1likelihood__sd/)**  |
| | **[Ic_fid](/documentation/code/classes/classmontepythonlike_1_1likelihood__sd/)**  |
| | **[fid_values_exist](/documentation/code/classes/classmontepythonlike_1_1likelihood__sd/)**  |
| | **[spinning_dust_file](/documentation/code/classes/classmontepythonlike_1_1likelihood__sd/)**  |
| | **[spinning_dust_lognup_data](/documentation/code/classes/classmontepythonlike_1_1likelihood__sd/)**  |
| | **[spinning_dust_lognup_0](/documentation/code/classes/classmontepythonlike_1_1likelihood__sd/)**  |
| | **[spinning_dust_lognu_0](/documentation/code/classes/classmontepythonlike_1_1likelihood__sd/)**  |
| | **[spinning_dust_lognumin](/documentation/code/classes/classmontepythonlike_1_1likelihood__sd/)**  |
| | **[spinning_dust_lognumax](/documentation/code/classes/classmontepythonlike_1_1likelihood__sd/)**  |
| | **[spinning_dust_logT_brightness](/documentation/code/classes/classmontepythonlike_1_1likelihood__sd/)**  |
| | **[co_integrated_file](/documentation/code/classes/classmontepythonlike_1_1likelihood__sd/)**  |
| | **[co_integrated_lognu_min](/documentation/code/classes/classmontepythonlike_1_1likelihood__sd/)**  |
| | **[co_integrated_lognu_max](/documentation/code/classes/classmontepythonlike_1_1likelihood__sd/)**  |
| | **[co_integrated_logInu](/documentation/code/classes/classmontepythonlike_1_1likelihood__sd/)**  |

## Additional inherited members

**Public Functions inherited from [MontePythonLike.Likelihood](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**

|                | Name           |
| -------------- | -------------- |
| def | **[raise_fiducial_model_err](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self) |
| def | **[read_from_file](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, path path, data data, command_line command_line) |
| def | **[get_cl](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, cosmo cosmo, l_max l_max =-1) |
| def | **[get_unlensed_cl](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, cosmo cosmo, l_max l_max =-1) |
| def | **[need_cosmo_arguments](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, data data, dictionary dictionary) |
| def | **[read_contamination_spectra](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, data data) |
| def | **[add_contamination_spectra](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, cl cl, data data) |
| def | **[add_nuisance_prior](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, lkl lkl, data data) |
| def | **[computeLikelihood](/documentation/code/classes/classmontepythonlike_1_1likelihood/)**(self self, ctx ctx) |
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


### function eval_spinning_dust

```
def eval_spinning_dust(
    self self,
    lognu lognu,
    lognu_p lognu_p
)
```


### function eval_co_integrated

```
def eval_co_integrated(
    self self,
    lognu lognu
)
```


### function loglkl

```
def loglkl(
    self self,
    cosmo cosmo,
    data data
)
```


**Reimplements**: [MontePythonLike::Likelihood::loglkl](/documentation/code/classes/classmontepythonlike_1_1likelihood/)




```
Placeholder to remind that this function needs to be defined for a
new likelihood.

Raises
------
NotImplementedError```


### function compute_lkl

```
def compute_lkl(
    self self,
    sd sd,
    cosmo cosmo,
    data data
)
```


## Public Attributes Documentation

### variable noise_from_file

```
noise_from_file;
```

Noise spectrum. 

### variable noise_file

```
noise_file;
```


### variable detector_bin_number

```
detector_bin_number;
```


### variable detector_nu_min

```
detector_nu_min;
```


### variable detector_nu_max

```
detector_nu_max;
```


### variable nu_range

```
nu_range;
```


### variable noise_Ic

```
noise_Ic;
```


### variable Ic_fid

```
Ic_fid;
```


### variable fid_values_exist

```
fid_values_exist;
```


### variable spinning_dust_file

```
spinning_dust_file;
```


### variable spinning_dust_lognup_data

```
spinning_dust_lognup_data;
```


### variable spinning_dust_lognup_0

```
spinning_dust_lognup_0;
```


### variable spinning_dust_lognu_0

```
spinning_dust_lognu_0;
```


### variable spinning_dust_lognumin

```
spinning_dust_lognumin;
```


### variable spinning_dust_lognumax

```
spinning_dust_lognumax;
```


### variable spinning_dust_logT_brightness

```
spinning_dust_logT_brightness;
```


### variable co_integrated_file

```
co_integrated_file;
```


### variable co_integrated_lognu_min

```
co_integrated_lognu_min;
```


### variable co_integrated_lognu_max

```
co_integrated_lognu_max;
```


### variable co_integrated_logInu

```
co_integrated_logInu;
```


-------------------------------

Updated on 2022-09-08 at 01:05:15 +0000