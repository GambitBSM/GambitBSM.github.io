---
title: "class Gambit::Models::ModelFunctorClaw"

description: "[No description available]"

---

# class Gambit::Models::ModelFunctorClaw



[No description available] [More...](#detailed-description)


`#include <models.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| primodel_vec | **[getPrimaryModelFunctorsToActivate](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/#function-getprimarymodelfunctorstoactivate)**(std::set< str > selectedmodels, const primodel_vec & primaryModelFunctors) |
| [primary_model_functor](/documentation/code/classes/classgambit_1_1primary__model__functor/) * | **[getPrimaryModelFunctor](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/#function-getprimarymodelfunctor)**(const std::string modelname, const primodel_vec & primaryModelFunctors) const<br>Searches primary model functor list for specified model.  |
| void | **[checkPrimaryModelFunctorUsage](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/#function-checkprimarymodelfunctorusage)**(const activemodel_map & activeModelFunctors) const |
| void | **[declare_model](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/#function-declare-model)**(const str & model, const str & parent)<br>Add a new model to the model database.  |
| void | **[add_friend](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/#function-add-friend)**(const str & model, const str & newfriend)<br>Add a friend, and all its friends and ancestors, to a model's list of friends.  |
| bool | **[model_exists](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/#function-model-exists)**(const str & model) const<br>Indicate whether a model is recognised by GAMBIT or not.  |
| str | **[list_models](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/#function-list-models)**() const<br>List all the models recognised by GAMBIT.  |
| void | **[verify_model](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/#function-verify-model)**(const str & model) const<br>Verify that a string matches a model recognised by GAMBIT, crash otherwise.  |
| const std::set< str > & | **[get_allmodels](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/#function-get-allmodels)**() const<br>Return set of all models recognised by GAMBIT.  |
| std::set< str > | **[get_activemodels](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/#function-get-activemodels)**() const<br>Return the set of active models;.  |
| std::vector< str > | **[get_lineage](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/#function-get-lineage)**(const str & model) const<br>Retrieve the lineage for a given model.  |
| std::set< str > | **[get_friends](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/#function-get-friends)**(const str & model) const<br>Retrieve the friends for a given model.  |
| std::set< str > | **[get_best_friends](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/#function-get-best-friends)**(const str & model) const<br>Retrieve the best friends for a given model.  |
| std::vector< str > | **[get_descendants](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/#function-get-descendants)**(const str & model) const<br>Retrieve the descendants for a given model.  |
| str | **[get_parent](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/#function-get-parent)**(const str & model) const<br>Retrieve the parent model for a given model.  |
| bool | **[descended_from](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/#function-descended-from)**(const str & model1, const str & model2) const<br>Check if model 1 is descended from model 2.  |
| bool | **[ancestor_of](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/#function-ancestor-of)**(const str & model1, const str & model2) const<br>Check if model 1 is an ancestor of model 2.  |
| bool | **[downstream_of](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/#function-downstream-of)**(const str & model1, const str & model2) const<br>Check if model 1 exists somewhere downstream of (and can be therefore be interpreted as a) model 2.  |
| bool | **[upstream_of](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/#function-upstream-of)**(const str & model1, const str & model2) const<br>Check if model 1 exists somewhere upstream of model 2, allowing model 2 to be interpreted as model 1.  |
| | **[ModelFunctorClaw](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/#function-modelfunctorclaw)**()<br>Constructor.  |
| | **[~ModelFunctorClaw](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/#function-modelfunctorclaw)**()<br>Destructor.  |

## Detailed Description

```
class Gambit::Models::ModelFunctorClaw;
```


[Models](/documentation/code/namespaces/namespacegambit_1_1models/) object that performs initialisation and checking operations on a [primary_model_functor](/documentation/code/classes/classgambit_1_1primary__model__functor/) list. 

## Public Functions Documentation

### function getPrimaryModelFunctorsToActivate

```
primodel_vec getPrimaryModelFunctorsToActivate(
    std::set< str > selectedmodels,
    const primodel_vec & primaryModelFunctors
)
```


Model activation function

Returns a vector of primary_model_functors to be activated, according to the model(s) being scanned

[ModelFunctorClaw](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/) function definitions [Models](/documentation/code/namespaces/namespacegambit_1_1models/) object the performs initialisation and checking operations on a [primary_model_functor](/documentation/code/classes/classgambit_1_1primary__model__functor/) list. Model activation function Returns a vector of primary_model_functors to be activated, according to the model(s) being scanned 


### function getPrimaryModelFunctor

```
primary_model_functor * getPrimaryModelFunctor(
    const std::string modelname,
    const primodel_vec & primaryModelFunctors
) const
```

Searches primary model functor list for specified model. 

Searches primary model functor list for specificed model. 


### function checkPrimaryModelFunctorUsage

```
void checkPrimaryModelFunctorUsage(
    const activemodel_map & activeModelFunctors
) const
```


Active model functor "usefulness" checker

Checks that all the active primary model functors are actually used for something in the dependency tree. If not throws an error to warn the user. 


### function declare_model

```
void declare_model(
    const str & model,
    const str & parent
)
```

Add a new model to the model database. 

### function add_friend

```
void add_friend(
    const str & model,
    const str & newfriend
)
```

Add a friend, and all its friends and ancestors, to a model's list of friends. 

### function model_exists

```
bool model_exists(
    const str & model
) const
```

Indicate whether a model is recognised by GAMBIT or not. 

### function list_models

```
str list_models() const
```

List all the models recognised by GAMBIT. 

### function verify_model

```
void verify_model(
    const str & model
) const
```

Verify that a string matches a model recognised by GAMBIT, crash otherwise. 

### function get_allmodels

```
const std::set< str > & get_allmodels() const
```

Return set of all models recognised by GAMBIT. 

### function get_activemodels

```
std::set< str > get_activemodels() const
```

Return the set of active models;. 

Retrieve the internally stored vector of activated models. 


### function get_lineage

```
std::vector< str > get_lineage(
    const str & model
) const
```

Retrieve the lineage for a given model. 

### function get_friends

```
std::set< str > get_friends(
    const str & model
) const
```

Retrieve the friends for a given model. 

### function get_best_friends

```
std::set< str > get_best_friends(
    const str & model
) const
```

Retrieve the best friends for a given model. 

### function get_descendants

```
std::vector< str > get_descendants(
    const str & model
) const
```

Retrieve the descendants for a given model. 

### function get_parent

```
str get_parent(
    const str & model
) const
```

Retrieve the parent model for a given model. 

Retrieve the parents for a given model. 


### function descended_from

```
bool descended_from(
    const str & model1,
    const str & model2
) const
```

Check if model 1 is descended from model 2. 

### function ancestor_of

```
bool ancestor_of(
    const str & model1,
    const str & model2
) const
```

Check if model 1 is an ancestor of model 2. 

### function downstream_of

```
bool downstream_of(
    const str & model1,
    const str & model2
) const
```

Check if model 1 exists somewhere downstream of (and can be therefore be interpreted as a) model 2. 

### function upstream_of

```
bool upstream_of(
    const str & model1,
    const str & model2
) const
```

Check if model 1 exists somewhere upstream of model 2, allowing model 2 to be interpreted as model 1. 

### function ModelFunctorClaw

```
inline ModelFunctorClaw()
```

Constructor. 

### function ~ModelFunctorClaw

```
inline ~ModelFunctorClaw()
```

Destructor. 

-------------------------------

Updated on 2024-07-18 at 13:53:31 +0000