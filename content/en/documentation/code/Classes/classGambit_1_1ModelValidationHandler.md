---
title: "class Gambit::ModelValidationHandler"

description: "[No description available]"

---

# class Gambit::ModelValidationHandler



[No description available] [More...](#detailed-description)


`#include <model_validation.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| [ModelValidationHandler](/documentation/code/classes/classgambit_1_1modelvalidationhandler/) & | **[getInstance](/documentation/code/classes/classgambit_1_1modelvalidationhandler/#function-getinstance)**()<br>Get the singleton instance of the handler.  |
| void | **[setModelValidationHandling](/documentation/code/classes/classgambit_1_1modelvalidationhandler/#function-setmodelvalidationhandling)**(const [ModelValidationHandling](/documentation/code/namespaces/namespacegambit/#enum-modelvalidationhandling) & h)<br>Set the handling strategy for model validation (pass, warning, or error)  |
| const [ModelValidationHandling](/documentation/code/namespaces/namespacegambit/#enum-modelvalidationhandling) & | **[getModelValidationHandling](/documentation/code/classes/classgambit_1_1modelvalidationhandler/#function-getmodelvalidationhandling)**() const<br>Get the current handling strategy for model validation.  |
| void | **[activate](/documentation/code/classes/classgambit_1_1modelvalidationhandler/#function-activate)**()<br>Activate the model validation handler.  |
| void | **[deactivate](/documentation/code/classes/classgambit_1_1modelvalidationhandler/#function-deactivate)**()<br>Deactivate the model validation handler.  |
| void | **[registerModelValidator](/documentation/code/classes/classgambit_1_1modelvalidationhandler/#function-registermodelvalidator)**(const std::string & model_name, [modelValidator](/documentation/code/namespaces/namespacegambit/#typedef-modelvalidator) f)<br>Register a model validation function for a specific model.  |
| bool | **[hasModelValidator](/documentation/code/classes/classgambit_1_1modelvalidationhandler/#function-hasmodelvalidator)**(const std::string & model_name) const<br>Check if a model validation function has been registered for a specific model.  |
| bool | **[validateModel](/documentation/code/classes/classgambit_1_1modelvalidationhandler/#function-validatemodel)**(const [ModelParameters](/documentation/code/classes/classgambit_1_1modelparameters/) & model_parameters) const<br>Validate the parameters of a model.  |
| void | **[runModelValidation](/documentation/code/classes/classgambit_1_1modelvalidationhandler/#function-runmodelvalidation)**(const [ModelParameters](/documentation/code/classes/classgambit_1_1modelparameters/) & model_parameters) const<br>Run model validation.  |
| [ModelValidationHandler](/documentation/code/classes/classgambit_1_1modelvalidationhandler/) & | **[operator=](/documentation/code/classes/classgambit_1_1modelvalidationhandler/#function-operator)**(const [ModelValidationHandler](/documentation/code/classes/classgambit_1_1modelvalidationhandler/) & ) =delete |
| [ModelValidationHandler](/documentation/code/classes/classgambit_1_1modelvalidationhandler/) & | **[operator=](/documentation/code/classes/classgambit_1_1modelvalidationhandler/#function-operator)**([ModelValidationHandler](/documentation/code/classes/classgambit_1_1modelvalidationhandler/) && ) =delete |
| | **[ModelValidationHandler](/documentation/code/classes/classgambit_1_1modelvalidationhandler/#function-modelvalidationhandler)**(const [ModelValidationHandler](/documentation/code/classes/classgambit_1_1modelvalidationhandler/) & ) =delete |
| | **[ModelValidationHandler](/documentation/code/classes/classgambit_1_1modelvalidationhandler/#function-modelvalidationhandler)**([ModelValidationHandler](/documentation/code/classes/classgambit_1_1modelvalidationhandler/) && ) =delete |

## Detailed Description

```
class Gambit::ModelValidationHandler;
```


Class for handling model validation logic. This is implemented as a singleton to ensure globally consistent model validation handling. 

## Public Functions Documentation

### function getInstance

```
static ModelValidationHandler & getInstance()
```

Get the singleton instance of the handler. 

### function setModelValidationHandling

```
void setModelValidationHandling(
    const ModelValidationHandling & h
)
```

Set the handling strategy for model validation (pass, warning, or error) 

### function getModelValidationHandling

```
const ModelValidationHandling & getModelValidationHandling() const
```

Get the current handling strategy for model validation. 

### function activate

```
void activate()
```

Activate the model validation handler. 

### function deactivate

```
void deactivate()
```

Deactivate the model validation handler. 

### function registerModelValidator

```
void registerModelValidator(
    const std::string & model_name,
    modelValidator f
)
```

Register a model validation function for a specific model. 

### function hasModelValidator

```
bool hasModelValidator(
    const std::string & model_name
) const
```

Check if a model validation function has been registered for a specific model. 

### function validateModel

```
bool validateModel(
    const ModelParameters & model_parameters
) const
```

Validate the parameters of a model. 

### function runModelValidation

```
void runModelValidation(
    const ModelParameters & model_parameters
) const
```

Run model validation. 

### function operator=

```
ModelValidationHandler & operator=(
    const ModelValidationHandler & 
) =delete
```


### function operator=

```
ModelValidationHandler & operator=(
    ModelValidationHandler && 
) =delete
```


### function ModelValidationHandler

```
ModelValidationHandler(
    const ModelValidationHandler & 
) =delete
```


### function ModelValidationHandler

```
ModelValidationHandler(
    ModelValidationHandler && 
) =delete
```


-------------------------------

Updated on 2026-11-03 at 14:50:42 +0000