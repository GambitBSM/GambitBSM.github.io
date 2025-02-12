---
title: "struct Gambit::ColliderBit::AnalysisLogLikes"
description: "Container for loglike information for an analysis. "

---

# struct Gambit::ColliderBit::AnalysisLogLikes



Container for loglike information for an analysis. 


`#include <AnalysisLogLikes.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[AnalysisLogLikes](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysisloglikes/#function-analysisloglikes)**() |
| void | **[initialize](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysisloglikes/#function-initialize)**(const [AnalysisData](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysisdata/) & adata_in, const std::vector< std::string > & alt_loglike_keys ={}) |
| void | **[set_no_signal_result_combination](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysisloglikes/#function-set-no-signal-result-combination)**(std::string combination_sr_label_in, int combination_sr_index_in) |
| void | **[set_no_signal_result_all_SRs](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysisloglikes/#function-set-no-signal-result-all-srs)**(std::string combination_sr_label_in, int combination_sr_index_in) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| std::vector< std::string > | **[sr_labels](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysisloglikes/#variable-sr-labels)**  |
| std::vector< double > | **[sr_loglikes](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysisloglikes/#variable-sr-loglikes)**  |
| std::map< std::string, std::vector< double > > | **[alt_sr_loglikes](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysisloglikes/#variable-alt-sr-loglikes)**  |
| std::string | **[combination_sr_label](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysisloglikes/#variable-combination-sr-label)**  |
| int | **[combination_sr_index](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysisloglikes/#variable-combination-sr-index)**  |
| double | **[combination_loglike](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysisloglikes/#variable-combination-loglike)**  |
| std::map< std::string, double > | **[alt_combination_loglikes](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysisloglikes/#variable-alt-combination-loglikes)**  |

## Public Functions Documentation

### function AnalysisLogLikes

```
inline AnalysisLogLikes()
```


### function initialize

```
inline void initialize(
    const AnalysisData & adata_in,
    const std::vector< std::string > & alt_loglike_keys ={}
)
```


### function set_no_signal_result_combination

```
inline void set_no_signal_result_combination(
    std::string combination_sr_label_in,
    int combination_sr_index_in
)
```


### function set_no_signal_result_all_SRs

```
inline void set_no_signal_result_all_SRs(
    std::string combination_sr_label_in,
    int combination_sr_index_in
)
```


## Public Attributes Documentation

### variable sr_labels

```
std::vector< std::string > sr_labels;
```


### variable sr_loglikes

```
std::vector< double > sr_loglikes;
```


### variable alt_sr_loglikes

```
std::map< std::string, std::vector< double > > alt_sr_loglikes;
```


### variable combination_sr_label

```
std::string combination_sr_label;
```


### variable combination_sr_index

```
int combination_sr_index;
```


### variable combination_loglike

```
double combination_loglike;
```


### variable alt_combination_loglikes

```
std::map< std::string, double > alt_combination_loglikes;
```


-------------------------------

Updated on 2025-02-12 at 15:36:39 +0000