---
title: "namespace Gambit::Models"
description: "Forward declaration of [Models::ModelFunctorClaw]() class for use in constructors. "

---

# namespace Gambit::Models

Forward declaration of [Models::ModelFunctorClaw]() class for use in constructors. 

## Namespaces

| Name           |
| -------------- |
| **[Gambit::Models::PARENT](/documentation/code/namespaces/namespacegambit_1_1models_1_1parent/)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| struct | **[Gambit::Models::DiracSingletDM_Z2Model](/documentation/code/classes/structgambit_1_1models_1_1diracsingletdm__z2model/)**  |
| class | **[Gambit::Models::DiracSingletDM_Z2SimpleSpec](/documentation/code/classes/classgambit_1_1models_1_1diracsingletdm__z2simplespec/)**  |
| struct | **[Gambit::Models::DMEFTModel](/documentation/code/classes/structgambit_1_1models_1_1dmeftmodel/)** <br>Simple DMEFT model object.  |
| class | **[Gambit::Models::DMEFTSimpleSpec](/documentation/code/classes/classgambit_1_1models_1_1dmeftsimplespec/)**  |
| struct | **[Gambit::Models::MajoranaSingletDM_Z2Model](/documentation/code/classes/structgambit_1_1models_1_1majoranasingletdm__z2model/)**  |
| class | **[Gambit::Models::MajoranaSingletDM_Z2SimpleSpec](/documentation/code/classes/classgambit_1_1models_1_1majoranasingletdm__z2simplespec/)**  |
| class | **[Gambit::Models::ModelFunctorClaw](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/)**  |
| class | **[Gambit::Models::partmap](/documentation/code/classes/classgambit_1_1models_1_1partmap/)**  |
| class | **[Gambit::Models::safe_param_map](/documentation/code/classes/classgambit_1_1models_1_1safe__param__map/)**  |
| struct | **[Gambit::Models::ScalarSingletDM_Z2Model](/documentation/code/classes/structgambit_1_1models_1_1scalarsingletdm__z2model/)**  |
| class | **[Gambit::Models::ScalarSingletDM_Z2SimpleSpec](/documentation/code/classes/classgambit_1_1models_1_1scalarsingletdm__z2simplespec/)**  |
| struct | **[Gambit::Models::ScalarSingletDM_Z3Model](/documentation/code/classes/structgambit_1_1models_1_1scalarsingletdm__z3model/)**  |
| class | **[Gambit::Models::ScalarSingletDM_Z3SimpleSpec](/documentation/code/classes/classgambit_1_1models_1_1scalarsingletdm__z3simplespec/)**  |
| struct | **[Gambit::Models::VectorSingletDM_Z2Model](/documentation/code/classes/structgambit_1_1models_1_1vectorsingletdm__z2model/)**  |
| class | **[Gambit::Models::VectorSingletDM_Z2SimpleSpec](/documentation/code/classes/classgambit_1_1models_1_1vectorsingletdm__z2simplespec/)**  |

## Types

|                | Name           |
| -------------- | -------------- |
| typedef std::string | **[str](/documentation/code/namespaces/namespacegambit_1_1models/#typedef-str)**  |
| typedef std::vector< [primary_model_functor](/documentation/code/classes/classgambit_1_1primary__model__functor/) * > | **[primodel_vec](/documentation/code/namespaces/namespacegambit_1_1models/#typedef-primodel-vec)**  |
| typedef std::map< str, [primary_model_functor](/documentation/code/classes/classgambit_1_1primary__model__functor/) * > | **[activemodel_map](/documentation/code/namespaces/namespacegambit_1_1models/#typedef-activemodel-map)**  |
| typedef std::map< std::string, [primary_model_functor](/documentation/code/classes/classgambit_1_1primary__model__functor/) * >::const_iterator | **[activemodel_it](/documentation/code/namespaces/namespacegambit_1_1models/#typedef-activemodel-it)**  |

## Functions

|                | Name           |
| -------------- | -------------- |
| [ModelFunctorClaw](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/) & | **[ModelDB](/documentation/code/namespaces/namespacegambit_1_1models/#function-modeldb)**()<br>Claw accessor function.  |
| void | **[set_many_to_one](/documentation/code/namespaces/namespacegambit_1_1models/#function-set-many-to-one)**([ModelParameters](/documentation/code/classes/classgambit_1_1modelparameters/) & myP, const std::vector< std::string > & v, const double value) |
| [partmap](/documentation/code/classes/classgambit_1_1models_1_1partmap/) & | **[ParticleDB](/documentation/code/namespaces/namespacegambit_1_1models/#function-particledb)**()<br>Database accessor function.  |
| void | **[define_particles](/documentation/code/namespaces/namespacegambit_1_1models/#function-define-particles)**([partmap](/documentation/code/classes/classgambit_1_1models_1_1partmap/) * )<br>Declare redirected constructor.  |

## Types Documentation

### typedef str

```
typedef std::string Gambit::Models::str;
```


### typedef primodel_vec

```
typedef std::vector<primary_model_functor*> Gambit::Models::primodel_vec;
```


### typedef activemodel_map

```
typedef std::map<str, primary_model_functor *> Gambit::Models::activemodel_map;
```


### typedef activemodel_it

```
typedef std::map<std::string,primary_model_functor*>::const_iterator Gambit::Models::activemodel_it;
```



## Functions Documentation

### function ModelDB

```
ModelFunctorClaw & ModelDB()
```

Claw accessor function. 

### function set_many_to_one

```
inline void set_many_to_one(
    ModelParameters & myP,
    const std::vector< std::string > & v,
    const double value
)
```


### function ParticleDB

```
partmap & ParticleDB()
```

Database accessor function. 

### function define_particles

```
void define_particles(
    partmap * 
)
```

Declare redirected constructor. 





-------------------------------

Updated on 2022-09-08 at 02:27:27 +0000