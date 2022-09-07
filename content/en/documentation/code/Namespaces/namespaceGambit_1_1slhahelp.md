---
title: "namespace Gambit::slhahelp"

description: "[No description available]"

---

# namespace Gambit::slhahelp

[No description available]

## Types

|                | Name           |
| -------------- | -------------- |
| typedef std::pair< int, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > | **[p_int_string](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#typedef-p-int-string)** <br>Typedefs for pairs that we will use in maps.  |
| typedef std::pair< int, int > | **[pair_ints](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#typedef-pair-ints)**  |
| typedef std::pair< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), pair_ints > | **[pair_string_ints](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#typedef-pair-string-ints)**  |
| typedef std::pair< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > | **[pair_strings](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#typedef-pair-strings)**  |

## Functions

|                | Name           |
| -------------- | -------------- |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[mass_es_from_gauge_es](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-mass-es-from-gauge-es)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) gauge_es, const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssm, double tol, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) context, bool pterror_only)<br>as above but do test against tol internally  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[mass_es_from_gauge_es](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-mass-es-from-gauge-es)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) gauge_es, double & max_mixing, const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssm)<br>Version returning maximum mixing.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[mass_es_from_gauge_es](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-mass-es-from-gauge-es)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) gauge_es, std::vector< double > & gauge_composition, const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssm)<br>Version returning gauge composition of identified mass eigenstate.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[mass_es_from_gauge_es](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-mass-es-from-gauge-es)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) gauge_es, double & max_mixing, std::vector< double > & gauge_composition, const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssm) |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[gauge_es_from_mass_es](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-gauge-es-from-mass-es)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) mass_es, const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssm, double tol, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) context, bool pterror_only)<br>as above but do test against tol internally  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[gauge_es_from_mass_es](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-gauge-es-from-mass-es)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) mass_es, double & max_mixing, const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssm)<br>Version returning maximum mixing.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[gauge_es_from_mass_es](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-gauge-es-from-mass-es)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) mass_es, std::vector< double > & mass_composition, const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssm)<br>Version returning mass composition of identified gauge eigenstate.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[gauge_es_from_mass_es](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-gauge-es-from-mass-es)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) mass_es, double & max_mixing, std::vector< double > & mass_composition, const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssm) |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[mass_es_closest_to_family](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-mass-es-closest-to-family)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) familystate, const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssm, double tol, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) context, bool pterror_only) |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[mass_es_closest_to_family](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-mass-es-closest-to-family)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) familystate, std::vector< double > & gauge_composition, const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssm) |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[mass_es_closest_to_family](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-mass-es-closest-to-family)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) familystate, double & sum_sqr_mix, const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssm)<br>Version returning the square sum of gauge mixing elements.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[mass_es_closest_to_family](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-mass-es-closest-to-family)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) familystate, std::vector< double > & gauge_composition, std::vector< double > & off_family_mixing, const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssm) |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[family_state_closest_to_mass_es](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-family-state-closest-to-mass-es)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) mass_es, const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssm, double tol, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) context, bool pterror_only) |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[family_state_closest_to_mass_es](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-family-state-closest-to-mass-es)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) mass_es, std::vector< double > & mass_comp, const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssm) |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[family_state_closest_to_mass_es](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-family-state-closest-to-mass-es)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) mass_es, double & sum_sqr_mix, const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssm) |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[family_state_closest_to_mass_es](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-family-state-closest-to-mass-es)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) mass_es, double & sum_sqr_mix, std::vector< double > & mass_comp, const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssm) |
| std::vector< double > | **[family_state_mix_matrix](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-family-state-mix-matrix)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) type, int generation, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & mass_es1, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & mass_es2, const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssm, double tol, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) context, bool pterror_only)<br>Get the family mixing matrix and corresponding mass eigenstates, then check for interfamily mixing.  |
| std::vector< double > | **[family_state_mix_matrix](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-family-state-mix-matrix)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) type, int generation, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & mass_es1, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & mass_es2, const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssm) |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), [p_int_string](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#typedef-p-int-string) > | **[init_gauge_label_to_index_type](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-init-gauge-label-to-index-type)**()<br>map from gauge eigenstate strings to string, index pairs  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), [p_int_string](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#typedef-p-int-string) > | **[init_mass_label_to_index_type](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-init-mass-label-to-index-type)**()<br>map from mass eigenstate strings to string, index pairs  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), pair_string_ints > | **[init_familystate_label](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-init-familystate-label)**()<br>map to extract info from family state  |
| std::map< [p_int_string](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#typedef-p-int-string), std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > > | **[init_type_family_to_gauge_states](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-init-type-family-to-gauge-states)**() |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > > | **[init_family_state_to_gauge_state](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-init-family-state-to-gauge-state)**() |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > > | **[init_gauge_es_to_family_states](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-init-gauge-es-to-family-states)**() |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > > | **[init_type_to_vec_of_mass_es](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-init-type-to-vec-of-mass-es)**() |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > > | **[init_type_to_vec_of_gauge_es](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-init-type-to-vec-of-gauge-es)**() |
| void | **[add_MODSEL_disclaimer](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-add-modsel-disclaimer)**([SLHAstruct](/documentation/code/namespaces/namespacegambit/#typedef-slhastruct) & slha, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & object)<br>Add a disclaimer about the absence of a MODSEL block in a generated SLHAea object.  |
| void | **[attempt_to_add_SLHA1_mixing](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-attempt-to-add-slha1-mixing)**(const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & block, [SLHAstruct](/documentation/code/namespaces/namespacegambit/#typedef-slhastruct) & slha, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & type, const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & spec, double tol, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & s1, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & s2, bool pterror)<br>Simple helper function for adding missing SLHA1 2x2 family mixing matrices to an SLHAea object.  |
| void | **[add_MSSM_spectrum_to_SLHAea](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-add-mssm-spectrum-to-slhaea)**(const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssmspec, [SLHAstruct](/documentation/code/namespaces/namespacegambit/#typedef-slhastruct) & slha, int slha_version)<br>Add an entire MSSM spectrum to an SLHAea object.  |
| std::vector< double > | **[get_Pole_Mixing_col](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-get-pole-mixing-col)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) type, int gauge_index, const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssm) |
| std::vector< double > | **[get_Pole_Mixing_row](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-get-pole-mixing-row)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) type, int mass_index, const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssm) |
| std::vector< double > | **[get_mass_comp_for_gauge](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-get-mass-comp-for-gauge)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) gauge_es, const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssm) |
| double | **[get_mixing_element](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-get-mixing-element)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) gauge_es, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) mass_es, const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssm) |
| std::vector< double > | **[get_gauge_comp_for_mass](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-get-gauge-comp-for-mass)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) mass_es, const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssm) |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[mass_es_from_gauge_es](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-mass-es-from-gauge-es)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) gauge_es, const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssm) |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[gauge_es_from_mass_es](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-gauge-es-from-mass-es)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) mass_es, const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssm) |
| [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) | **[identify_mass_ess_for_family](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-identify-mass-ess-for-family)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) type, int family, const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssm) |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[mass_es_closest_to_family](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-mass-es-closest-to-family)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) familystate, const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssm) |
| std::vector< double > | **[get_gauge_comp_for_family_state](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-get-gauge-comp-for-family-state)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) familystate, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & mass_es, const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssm) |
| double | **[get_gauge_admix_for_family_state](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#function-get-gauge-admix-for-family-state)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) familystate, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) gauge_es, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & mass_es, const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & mssm) |

## Attributes

|                | Name           |
| -------------- | -------------- |
| const std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), [p_int_string](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#typedef-p-int-string) > | **[gauge_label_to_index_type](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#variable-gauge-label-to-index-type)**  |
| const std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), [p_int_string](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#typedef-p-int-string) > | **[mass_label_to_index_type](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#variable-mass-label-to-index-type)**  |
| const std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), pair_string_ints > | **[familystate_label](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#variable-familystate-label)**  |
| const std::map< [p_int_string](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#typedef-p-int-string), std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > > | **[type_family_to_gauge_states](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#variable-type-family-to-gauge-states)**  |
| const std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > > | **[family_state_to_gauge_state](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#variable-family-state-to-gauge-state)**  |
| const std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > > | **[gauge_es_to_family_states](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#variable-gauge-es-to-family-states)**  |
| const std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > > | **[type_to_vec_of_mass_es](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#variable-type-to-vec-of-mass-es)**  |
| const std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > > | **[type_to_vec_of_gauge_es](/documentation/code/namespaces/namespacegambit_1_1slhahelp/#variable-type-to-vec-of-gauge-es)**  |

## Types Documentation

### typedef p_int_string

```
typedef std::pair<int,str> Gambit::slhahelp::p_int_string;
```

Typedefs for pairs that we will use in maps. 

### typedef pair_ints

```
typedef std::pair<int,int> Gambit::slhahelp::pair_ints;
```


### typedef pair_string_ints

```
typedef std::pair<str,pair_ints> Gambit::slhahelp::pair_string_ints;
```


### typedef pair_strings

```
typedef std::pair<str,str> Gambit::slhahelp::pair_strings;
```



## Functions Documentation

### function mass_es_from_gauge_es

```
str mass_es_from_gauge_es(
    str gauge_es,
    const SubSpectrum & mssm,
    double tol,
    str context,
    bool pterror_only
)
```

as above but do test against tol internally 

***************** Gauge <-> Mass Eigenstate Helpers **************** Identifies the mass eigenstate with largest gauge eigenstate content.

Version that tests internally agains a user-requested tolerance, either raising a GAMBIT error (if pterror_only = false) or invalidating a point. 


### function mass_es_from_gauge_es

```
str mass_es_from_gauge_es(
    str gauge_es,
    double & max_mixing,
    const SubSpectrum & mssm
)
```

Version returning maximum mixing. 

as above but doesn't fill a gauge_composition vector would have a slight efficiency saving if we didn't use wrapper and avoided skipped gauge_composition entirely but at the cost of a lot of code duplication 


### function mass_es_from_gauge_es

```
str mass_es_from_gauge_es(
    str gauge_es,
    std::vector< double > & gauge_composition,
    const SubSpectrum & mssm
)
```

Version returning gauge composition of identified mass eigenstate. 

as above but doesn't fill max_mixing would have a slight efficiency saving if we didn't use wrapper and avoided skipped max_mixing entirely but at the cost of a lot of code duplication 


### function mass_es_from_gauge_es

```
str mass_es_from_gauge_es(
    str gauge_es,
    double & max_mixing,
    std::vector< double > & gauge_composition,
    const SubSpectrum & mssm
)
```


Version returning maximum mixing and full gauge composition of identified mass eigenstate.

indentifies the state with largest gauge_es content also fills largest max_mixing and full gauge_composition 


passed in massstate to be set

make sure this is zero to start

retrive type from the gauge_es string

iterate over vector of strings for mass states

passed in massstate to be set

make sure this is zero to start

retrive type from the gauge_es string

iterate over vector of strings for mass states


### function gauge_es_from_mass_es

```
str gauge_es_from_mass_es(
    str mass_es,
    const SubSpectrum & mssm,
    double tol,
    str context,
    bool pterror_only
)
```

as above but do test against tol internally 

Identifies the gauge eigenstate with largest mass eigenstate content.

Version that tests internally agains a user-requested tolerance, either raising a GAMBIT error (if pterror_only = false) or invalidating a point. 


### function gauge_es_from_mass_es

```
str gauge_es_from_mass_es(
    str mass_es,
    double & max_mixing,
    const SubSpectrum & mssm
)
```

Version returning maximum mixing. 

as above but doesn't fill a gauge_composition vector would have a slight efficiency saving if we didn't use wrapper and avoided skipped gauge_composition entirely but at the cost of a lot of code duplication 


### function gauge_es_from_mass_es

```
str gauge_es_from_mass_es(
    str mass_es,
    std::vector< double > & mass_composition,
    const SubSpectrum & mssm
)
```

Version returning mass composition of identified gauge eigenstate. 

as above but doesn't fill max_mixing would have a slight efficiency saving if we didn't use wrapper and avoided skipped max_mixing entirely but at the cost of a lot of code duplication 


### function gauge_es_from_mass_es

```
str gauge_es_from_mass_es(
    str mass_es,
    double & max_mixing,
    std::vector< double > & mass_composition,
    const SubSpectrum & mssm
)
```


Version returning maximum mixing and full mass composition of identified gauge eigenstate.

identifies gauge_es with largest mass_es content also fills largest max_mixing and full mass_composition 


passed in massstate to be set

start with zero

retrive type from the gauge_es string

iterate over vector of strings for mass states

passed in massstate to be set

start with zero

retrive type from the gauge_es string

iterate over vector of strings for mass states


### function mass_es_closest_to_family

```
str mass_es_closest_to_family(
    str familystate,
    const SubSpectrum & mssm,
    double tol,
    str context,
    bool pterror_only
)
```


Identifies the mass eigenstate that best matches the requested family state.

Version that tests internally agains a user-requested tolerance for family mixing, either raising a GAMBIT error (if pterror_only = false) or invalidating a point.

identifies the mass_es that is closest match to specified family does tol-test internally to check correctness of assumptions 


### function mass_es_closest_to_family

```
str mass_es_closest_to_family(
    str familystate,
    std::vector< double > & gauge_composition,
    const SubSpectrum & mssm
)
```


Version returning mixing elements of the resulting mass eigenstate into the two gauge eigenstates of the requested family. To test against family mixing, check that the square sum of elements of this mixing matrix row are sufficiently close to 1. That is, compare gauge_composition(1)^2 + gauge_composition(2)^2 to 1-tolerance.

identifies the mass_es that is closest match to specified family state and fills mixture of the two gauge states with same family into std::vector gauge_composition 


### function mass_es_closest_to_family

```
str mass_es_closest_to_family(
    str familystate,
    double & sum_sqr_mix,
    const SubSpectrum & mssm
)
```

Version returning the square sum of gauge mixing elements. 

identifies the mass_es that is closest match to specified family state and fills sqr_sum_mix with the square sum of each of the two mixings into gauge_es of that family 


### function mass_es_closest_to_family

```
str mass_es_closest_to_family(
    str familystate,
    std::vector< double > & gauge_composition,
    std::vector< double > & off_family_mixing,
    const SubSpectrum & mssm
)
```


Version returning mixing elements of the resulting mass eigenstate into the two gauge eigenstates of the requested family, and off-family mixing.

identifies the mass_es that is closest match to specified family state and fills mixture of the two gauge states with same family into std::vector gauge_composition also fills remaining off-family mixings into a second vector 


extract info from strings via maps

extract info from strings via maps


### function family_state_closest_to_mass_es

```
str family_state_closest_to_mass_es(
    str mass_es,
    const SubSpectrum & mssm,
    double tol,
    str context,
    bool pterror_only
)
```


Identifies the family state that best matches the requested mass eigenstate.

Version that tests internally agains a user-requested tolerance for family mixing, either raising a GAMBIT error (if pterror_only = false) or invalidating a point.

wrapper for overloaded version returns family state that best matches the given mass_es and fills the mixing of the matching mass_es into gauge eigenstates 


### function family_state_closest_to_mass_es

```
str family_state_closest_to_mass_es(
    str mass_es,
    std::vector< double > & mass_comp,
    const SubSpectrum & mssm
)
```


Version returning the mass eigenstate composition of the gauge eigenstate that best matches the requested mass eigenstate.

wrapper for overloaded version returns family state that best matches the given mass_es and fills the mixing of the matching mass_es into gauge eigenstates 


### function family_state_closest_to_mass_es

```
str family_state_closest_to_mass_es(
    str mass_es,
    double & sum_sqr_mix,
    const SubSpectrum & mssm
)
```


Version returning the summed squares of the contributions to the gauge eigenstate that best matches the requested mass eigenstate, of the two mass eigenstates that look most like the resulting family. (Seriously, just use the tol version.) To test against family mixing, you can check that this square of elements is sufficiently close to 1.

wrapper for overloaded version returns family state that best matches the given mass_es fills a double with the sum of the square mixings to gauge_es of the matching family 


### function family_state_closest_to_mass_es

```
str family_state_closest_to_mass_es(
    str mass_es,
    double & sum_sqr_mix,
    std::vector< double > & mass_comp,
    const SubSpectrum & mssm
)
```


Version returning the mass eigenstate composition of the best-matching gauge eigenstate, and the summed squares of the contributions to this from the two mass eigenstates that look most like the resulting family.

returns family state that best matches the given mass_es fills a double with the sum of the square mixings to gauge_es of the matching family and fills the mixing of the matching gauge_es into mass eigenstates 


get gauge_es with largest mixing to this mass_es

get family states for the same generation as this gauge_es

extractindex of mass-es and mass_ess_other from strings

choose mass ordering for family state which matches mass ordering of mass_es

subrtact 1 fgrom indices to deal with different indexing

get gauge_es with largest mixing to this mass_es

get family states for the same generation as this gauge_es

extractindex of mass-es and mass_ess_other from strings

choose mass ordering for family state which matches mass ordering of mass_es

subrtact 1 fgrom indices to deal with different indexing


### function family_state_mix_matrix

```
std::vector< double > family_state_mix_matrix(
    str type,
    int generation,
    str & mass_es1,
    str & mass_es2,
    const SubSpectrum & mssm,
    double tol,
    str context,
    bool pterror_only
)
```

Get the family mixing matrix and corresponding mass eigenstates, then check for interfamily mixing. 

Identifies the two mass eigenstates which best match a requested family, as well as the resulting 2x2 family mixing matrix between them. The matrix has the form (Mix_{11}, Mix_{12}, Mix_{21}, Mix_{22}).

Version that tests internally agains a user-requested tolerance for family mixing, either raising a GAMBIT error (if pterror_only = false) or invalidating a point. 


### function family_state_mix_matrix

```
std::vector< double > family_state_mix_matrix(
    str type,
    int generation,
    str & mass_es1,
    str & mass_es2,
    const SubSpectrum & mssm
)
```


Version that leaves the test up to the user. To test that there is negligible family mixing, you can check that for both rows of the family mixing matrix, the sum of squares of elements is sufficently close to 1. That is, check Mix_{11}^2 + Mix_{12}^2 > 1-tolerance && Mix_{21}^2 + Mix_{22}^2 > 1-tolerance. where vec is the std::vector returned by this method

identifies the two mass_es which best matches specified family state storing them in strings and then returns the 2by2 mixing matrix for that family state in the form (Mix_{11}, Mix_{12}, Mix_{21}, Mix_{22}) It also stores the mixing elements for the gauge states that don't belong to the correct family for this state in a std::vector The latter should have entries which are zero in absense of family mixing 


get mass_es using one of our routines

need to turn type and family into a string should simplify the number of translations we do!

get index of right family states (ie gauge states with same family as requested family state

Put row 1 and row 2 into the same vector to return

get mass_es using one of our routines

need to turn type and family into a string should simplify the number of translations we do!

get index of right family states (ie gauge states with same family as requested family state

Put row 1 and row 2 into the same vector to return


### function init_gauge_label_to_index_type

```
std::map< str, p_int_string > init_gauge_label_to_index_type()
```

map from gauge eigenstate strings to string, index pairs 

### function init_mass_label_to_index_type

```
std::map< str, p_int_string > init_mass_label_to_index_type()
```

map from mass eigenstate strings to string, index pairs 

### function init_familystate_label

```
std::map< str, pair_string_ints > init_familystate_label()
```

map to extract info from family state 

### function init_type_family_to_gauge_states

```
std::map< p_int_string, std::vector< str > > init_type_family_to_gauge_states()
```


map to obtain left_right gauge_pairs from state info helps us reuse other routiones with string arguments 


### function init_family_state_to_gauge_state

```
std::map< str, std::vector< str > > init_family_state_to_gauge_state()
```


maps directly from family string to left_right gauge_pairs helps us reuse other routines that take string arguments 


### function init_gauge_es_to_family_states

```
std::map< str, std::vector< str > > init_gauge_es_to_family_states()
```


maps directly from gauge_es string to familystates helps us reuse other routines that take string arguments 


### function init_type_to_vec_of_mass_es

```
std::map< str, std::vector< str > > init_type_to_vec_of_mass_es()
```


map from string representing type (ie up-squarks, down-squarks or charged sleptons) to appropriate set of mass eigenstates 


### function init_type_to_vec_of_gauge_es

```
std::map< str, std::vector< str > > init_type_to_vec_of_gauge_es()
```


map from string representing type (ie up-squarks, down-squarks or charged sleptons) to appropriate set of gauge eigenstates 


### function add_MODSEL_disclaimer

```
void add_MODSEL_disclaimer(
    SLHAstruct & slha,
    const str & object
)
```

Add a disclaimer about the absence of a MODSEL block in a generated SLHAea object. 

### function attempt_to_add_SLHA1_mixing

```
void attempt_to_add_SLHA1_mixing(
    const str & block,
    SLHAstruct & slha,
    const str & type,
    const SubSpectrum & spec,
    double tol,
    str & s1,
    str & s2,
    bool pterror
)
```

Simple helper function for adding missing SLHA1 2x2 family mixing matrices to an SLHAea object. 

Simple helper function for for adding missing SLHA1 2x2 family mixing matrices to an SLHAea object. 


### function add_MSSM_spectrum_to_SLHAea

```
void add_MSSM_spectrum_to_SLHAea(
    const SubSpectrum & mssmspec,
    SLHAstruct & slha,
    int slha_version
)
```

Add an entire MSSM spectrum to an SLHAea object. 

### function get_Pole_Mixing_col

```
std::vector< double > get_Pole_Mixing_col(
    str type,
    int gauge_index,
    const SubSpectrum & mssm
)
```


### function get_Pole_Mixing_row

```
std::vector< double > get_Pole_Mixing_row(
    str type,
    int mass_index,
    const SubSpectrum & mssm
)
```


Mix_{row, col}. Iterate through column index with row index fixed


### function get_mass_comp_for_gauge

```
std::vector< double > get_mass_comp_for_gauge(
    str gauge_es,
    const SubSpectrum & mssm
)
```


returns vector representing composition of requested gauge state in terms of the slha2 mass eigenstates (~u_1 ...~u_6 etc) which is just a column in the mixing matrix 


extract info from string via map


### function get_mixing_element

```
double get_mixing_element(
    str gauge_es,
    str mass_es,
    const SubSpectrum & mssm
)
```


routine to return mass state admixure for given gauge state in the end this is a trival routine but may help 


extract info from maps

types should match but getting both allows us to throw error

throw exception in gambit

will need to add mssm object to cal method in gambit


### function get_gauge_comp_for_mass

```
std::vector< double > get_gauge_comp_for_mass(
    str mass_es,
    const SubSpectrum & mssm
)
```


returns vector representing composition of requested mass eigenstate in terms of the slha2 gauge eigenstates (~u_L,~c_L,...~t_R etc) which is just a row in the mixing matrix just wraps get_Pole_Mixing_row after extracting info from string 


extract info using map


### function mass_es_from_gauge_es

```
str mass_es_from_gauge_es(
    str gauge_es,
    const SubSpectrum & mssm
)
```


as above but doesn't fill max_mixing or gauge_composition would have a slight efficiency saving if we didn't use wrapper and avoided skipped max_mixing entirely but at the cost of a lot of code duplication 


### function gauge_es_from_mass_es

```
str gauge_es_from_mass_es(
    str mass_es,
    const SubSpectrum & mssm
)
```


as above but doesn't fill max_mixing or gauge_composition would have a slight efficiency saving if we didn't use wrapper and avoided skipped max_mixing entirely but at the cost of a lot of code duplication 


### function identify_mass_ess_for_family

```
sspair identify_mass_ess_for_family(
    str type,
    int family,
    const SubSpectrum & mssm
)
```


identify the two mass eigenstate corresponding to the approximate family states, e.g. stops ("~u",3), smuons ("~mu", 2) etc Note: when there is family mixing there's no good definition ~t_1, ~t_2 etc if defined as the states you get from diagonalising a 2by2 mass (sub)matrix then extensive manipulations would be required So here we identify the mass eigenstates closest to the family ones which is a better defined question when there is family mixing prsesent and more useful here anyway returns a pair of strings labling the lighter one first 


need to turn type and family into a string need to simplify the number of translations we do.

finds the mass_es with the largets mixing to passed gauge_es


### function mass_es_closest_to_family

```
str mass_es_closest_to_family(
    str familystate,
    const SubSpectrum & mssm
)
```


identify the mass eigenstate corresponding to family state takes string and returns only requested state I suspect this is the more useful one 


### function get_gauge_comp_for_family_state

```
std::vector< double > get_gauge_comp_for_family_state(
    str familystate,
    str & mass_es,
    const SubSpectrum & mssm
)
```


returns vector with composition of closest the mass eigenstate to give family state in terms of gauge eigenstates and stores mass eigenstate in mass_es 


extract info from strings via maps


### function get_gauge_admix_for_family_state

```
double get_gauge_admix_for_family_state(
    str familystate,
    str gauge_es,
    str & mass_es,
    const SubSpectrum & mssm
)
```


returns admix of gauge eigenstate in the mass eigenstate closest to the given family state and stores mass eigenstate in mass_es 


types should match but getting both allows us to throw error

throw error in gambit

get mass_es using one of our routines

extract info from strings via maps



## Attributes Documentation

### variable gauge_label_to_index_type

```
const std::map< str, p_int_string > gauge_label_to_index_type = init_gauge_label_to_index_type();
```


Known maps filled at initialisation 


### variable mass_label_to_index_type

```
const std::map< str, p_int_string > mass_label_to_index_type = init_mass_label_to_index_type();
```


### variable familystate_label

```
const std::map< str, pair_string_ints > familystate_label = init_familystate_label();
```


### variable type_family_to_gauge_states

```
const std::map< p_int_string, std::vector< str > > type_family_to_gauge_states = init_type_family_to_gauge_states();
```


### variable family_state_to_gauge_state

```
const std::map< str, std::vector< str > > family_state_to_gauge_state = init_family_state_to_gauge_state();
```


### variable gauge_es_to_family_states

```
const std::map< str, std::vector< str > > gauge_es_to_family_states = init_gauge_es_to_family_states();
```


### variable type_to_vec_of_mass_es

```
const std::map< str, std::vector< str > > type_to_vec_of_mass_es = init_type_to_vec_of_mass_es();
```


### variable type_to_vec_of_gauge_es

```
const std::map< str, std::vector< str > > type_to_vec_of_gauge_es = init_type_to_vec_of_gauge_es();
```





-------------------------------

Updated on 2022-09-07 at 23:22:07 +0000