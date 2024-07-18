---
title: "namespace YAML"
description: "[YAML]() overloads for mass cut and mass cut ratio constituents. "

---

# namespace YAML

[YAML]() overloads for mass cut and mass cut ratio constituents. 

## Classes

|                | Name           |
| -------------- | -------------- |
| struct | **[YAML::convert< Gambit::DRes::BackendRule >](/documentation/code/classes/structyaml_1_1convert_3_01gambit_1_1dres_1_1backendrule_01_4/)**  |
| struct | **[YAML::convert< Gambit::DRes::ModuleRule >](/documentation/code/classes/structyaml_1_1convert_3_01gambit_1_1dres_1_1modulerule_01_4/)**  |
| struct | **[YAML::convert< Gambit::DRes::Observable >](/documentation/code/classes/structyaml_1_1convert_3_01gambit_1_1dres_1_1observable_01_4/)**  |
| struct | **[YAML::convert< Gambit::nuiscorr >](/documentation/code/classes/structyaml_1_1convert_3_01gambit_1_1nuiscorr_01_4/)** <br>[YAML](/documentation/code/namespaces/namespaceyaml/) conversion structure for SuperIso SM nuisance data.  |
| struct | **[YAML::convert< sdd >](/documentation/code/classes/structyaml_1_1convert_3_01sdd_01_4/)**  |
| struct | **[YAML::convert< ssdd >](/documentation/code/classes/structyaml_1_1convert_3_01ssdd_01_4/)**  |

## Types

|                | Name           |
| -------------- | -------------- |
| typedef std::pair< std::string, std::pair< double, double > > | **[sdd](/documentation/code/namespaces/namespaceyaml/#typedef-sdd)**  |
| typedef std::pair< std::pair< std::string, std::string >, std::pair< double, double > > | **[ssdd](/documentation/code/namespaces/namespaceyaml/#typedef-ssdd)**  |

## Functions

|                | Name           |
| -------------- | -------------- |
| void | **[convert_to_module_rule](/documentation/code/namespaces/namespaceyaml/#function-convert-to-module-rule)**(const YAML::detail::iterator_value y, std::vector< [ModuleRule](/documentation/code/classes/structgambit_1_1dres_1_1modulerule/) > & v)<br>Helper function for trying to convert a [YAML](/documentation/code/namespaces/namespaceyaml/) snippet to a nested module rule.  |
| void | **[convert_to_backend_rule](/documentation/code/namespaces/namespaceyaml/#function-convert-to-backend-rule)**(const YAML::detail::iterator_value y, std::vector< [BackendRule](/documentation/code/classes/structgambit_1_1dres_1_1backendrule/) > & v)<br>Helper function for trying to convert a [YAML](/documentation/code/namespaces/namespaceyaml/) snippet to a nested backend rule.  |
| bool | **[check_field_is_valid_in_derived_rule](/documentation/code/namespaces/namespaceyaml/#function-check-field-is-valid-in-derived-rule)**(const std::string & field)<br>Throw an error if a yaml key is not one of those exclusively allowed in a module or backend rule.  |
| void | **[throw_if_field_valid_only_in_backend_rule](/documentation/code/namespaces/namespaceyaml/#function-throw-if-field-valid-only-in-backend-rule)**(const std::string & field)<br>Throw an error if a yaml key is one of those exclusively allowed in a backend rule.  |
| void | **[throw_if_field_valid_only_in_module_rule](/documentation/code/namespaces/namespaceyaml/#function-throw-if-field-valid-only-in-module-rule)**(const std::string & field)<br>Throw an error if a yaml key is one of those exclusively allowed in a module rule.  |
| void | **[forbid_both_true](/documentation/code/namespaces/namespaceyaml/#function-forbid-both-true)**(const std::string & field, bool is_in_one_block, bool is_in_other_block)<br>Throw an error if a field appears in both an if and a then block.  |
| void | **[build_rule](/documentation/code/namespaces/namespaceyaml/#function-build-rule)**(const Node & node, [Rule](/documentation/code/classes/structgambit_1_1dres_1_1rule/) & rhs)<br>Build the base-class parts of a rule from a yaml node.  |
| void | **[set_other_module_rule_fields](/documentation/code/namespaces/namespaceyaml/#function-set-other-module-rule-fields)**(const YAML::detail::iterator_value & entry, [ModuleRule](/documentation/code/classes/structgambit_1_1dres_1_1modulerule/) & rhs)<br>Set fields exclusive to module rules that can only appear as 'then' parts of a condition.  |

## Types Documentation

### typedef sdd

```
typedef std::pair<std::string, std::pair<double, double> > YAML::sdd;
```


### typedef ssdd

```
typedef std::pair<std::pair<std::string,std::string>, std::pair<double, double> > YAML::ssdd;
```



## Functions Documentation

### function convert_to_module_rule

```
void convert_to_module_rule(
    const YAML::detail::iterator_value y,
    std::vector< ModuleRule > & v
)
```

Helper function for trying to convert a [YAML](/documentation/code/namespaces/namespaceyaml/) snippet to a nested module rule. 

### function convert_to_backend_rule

```
void convert_to_backend_rule(
    const YAML::detail::iterator_value y,
    std::vector< BackendRule > & v
)
```

Helper function for trying to convert a [YAML](/documentation/code/namespaces/namespaceyaml/) snippet to a nested backend rule. 

### function check_field_is_valid_in_derived_rule

```
bool check_field_is_valid_in_derived_rule(
    const std::string & field
)
```

Throw an error if a yaml key is not one of those exclusively allowed in a module or backend rule. 

### function throw_if_field_valid_only_in_backend_rule

```
void throw_if_field_valid_only_in_backend_rule(
    const std::string & field
)
```

Throw an error if a yaml key is one of those exclusively allowed in a backend rule. 

### function throw_if_field_valid_only_in_module_rule

```
void throw_if_field_valid_only_in_module_rule(
    const std::string & field
)
```

Throw an error if a yaml key is one of those exclusively allowed in a module rule. 

### function forbid_both_true

```
void forbid_both_true(
    const std::string & field,
    bool is_in_one_block,
    bool is_in_other_block
)
```

Throw an error if a field appears in both an if and a then block. 

### function build_rule

```
void build_rule(
    const Node & node,
    Rule & rhs
)
```

Build the base-class parts of a rule from a yaml node. 

### function set_other_module_rule_fields

```
void set_other_module_rule_fields(
    const YAML::detail::iterator_value & entry,
    ModuleRule & rhs
)
```

Set fields exclusive to module rules that can only appear as 'then' parts of a condition. 





-------------------------------

Updated on 2024-07-18 at 13:53:30 +0000