---
title: "struct Gambit::ColliderBit::_gsl_target_func_params"
description: "A struct to contain parameters for the GSL optimiser target function. "

---

# struct Gambit::ColliderBit::_gsl_target_func_params



A struct to contain parameters for the GSL optimiser target function. 

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| double | **[lambda](/documentation/code/classes/structgambit_1_1colliderbit_1_1__gsl__target__func__params/#variable-lambda)**  |
| [AnalysisDataPointers](/documentation/code/namespaces/namespacegambit_1_1colliderbit/#typedef-analysisdatapointers) | **[adata_ptrs_original](/documentation/code/classes/structgambit_1_1colliderbit_1_1__gsl__target__func__params/#variable-adata-ptrs-original)**  |
| std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > | **[skip_analyses](/documentation/code/classes/structgambit_1_1colliderbit_1_1__gsl__target__func__params/#variable-skip-analyses)**  |
| bool | **[use_covar](/documentation/code/classes/structgambit_1_1colliderbit_1_1__gsl__target__func__params/#variable-use-covar)**  |
| bool | **[use_marg](/documentation/code/classes/structgambit_1_1colliderbit_1_1__gsl__target__func__params/#variable-use-marg)**  |
| bool | **[combine_nocovar_SRs](/documentation/code/classes/structgambit_1_1colliderbit_1_1__gsl__target__func__params/#variable-combine-nocovar-srs)**  |
| bool | **[use_fulllikes](/documentation/code/classes/structgambit_1_1colliderbit_1_1__gsl__target__func__params/#variable-use-fulllikes)**  |
| [Options](/documentation/code/classes/classgambit_1_1options/) | **[runOptions](/documentation/code/classes/structgambit_1_1colliderbit_1_1__gsl__target__func__params/#variable-runoptions)**  |
| bool(*)(const str &) | **[FullLikes_FileExists](/documentation/code/classes/structgambit_1_1colliderbit_1_1__gsl__target__func__params/#variable-fulllikes-fileexists)**  |
| int(*)(const str &, const str &) | **[FullLikes_ReadIn](/documentation/code/classes/structgambit_1_1colliderbit_1_1__gsl__target__func__params/#variable-fulllikes-readin)**  |
| double(*)(std::map< str, double > &, const str &) | **[FullLikes_Evaluate](/documentation/code/classes/structgambit_1_1colliderbit_1_1__gsl__target__func__params/#variable-fulllikes-evaluate)**  |
| double(*)(const int &, const double &, const double &, const double &) | **[marginaliser](/documentation/code/classes/structgambit_1_1colliderbit_1_1__gsl__target__func__params/#variable-marginaliser)**  |

## Public Attributes Documentation

### variable lambda

```
double lambda;
```


### variable adata_ptrs_original

```
AnalysisDataPointers adata_ptrs_original;
```


### variable skip_analyses

```
std::vector< str > skip_analyses;
```


### variable use_covar

```
bool use_covar;
```


### variable use_marg

```
bool use_marg;
```


### variable combine_nocovar_SRs

```
bool combine_nocovar_SRs;
```


### variable use_fulllikes

```
bool use_fulllikes;
```


### variable runOptions

```
Options runOptions;
```


### variable FullLikes_FileExists

```
bool(*)(const str &) FullLikes_FileExists;
```


### variable FullLikes_ReadIn

```
int(*)(const str &, const str &) FullLikes_ReadIn;
```


### variable FullLikes_Evaluate

```
double(*)(std::map< str, double > &, const str &) FullLikes_Evaluate;
```


### variable marginaliser

```
double(*)(const int &, const double &, const double &, const double &) marginaliser;
```


-------------------------------

Updated on 2025-02-12 at 15:36:38 +0000