---
title: "class Gambit::model_functor"
description: "Functors specific to [ModelParameters]() objects. "

---

# class Gambit::model_functor



Functors specific to [ModelParameters]() objects. 


`#include <functors.hpp>`

Inherits from [Gambit::module_functor< ModelParameters >](/documentation/code/classes/classgambit_1_1module__functor/), [Gambit::module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/), [Gambit::functor](/documentation/code/classes/classgambit_1_1functor/)

Inherited by [Gambit::primary_model_functor](/documentation/code/classes/classgambit_1_1primary__model__functor/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[model_functor](/documentation/code/classes/classgambit_1_1model__functor/#function-model-functor)**(void(*)([ModelParameters](/documentation/code/classes/classgambit_1_1modelparameters/) &) inputFunction, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) func_name, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) func_capability, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) result_type, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) origin_name, [Models::ModelFunctorClaw](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/) & claw)<br>Constructor.  |
| void | **[setModelName](/documentation/code/classes/classgambit_1_1model__functor/#function-setmodelname)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) model_name)<br>Function for setting the model name for a [ModelParameters]() object. Mainly for better error messages.  |
| void | **[addParameter](/documentation/code/classes/classgambit_1_1model__functor/#function-addparameter)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) parname)<br>Function for adding a new parameter to the map inside the [ModelParameters]() object.  |
| void | **[donateParameters](/documentation/code/classes/classgambit_1_1model__functor/#function-donateparameters)**([model_functor](/documentation/code/classes/classgambit_1_1model__functor/) & receiver)<br>Function for handing over parameter identities to another [model_functor](/documentation/code/classes/classgambit_1_1model__functor/).  |
| virtual | **[~model_functor](/documentation/code/classes/classgambit_1_1model__functor/#function-model-functor)**()<br>Destructor.  |

## Additional inherited members

**Public Functions inherited from [Gambit::module_functor< ModelParameters >](/documentation/code/classes/classgambit_1_1module__functor/)**

|                | Name           |
| -------------- | -------------- |
| | **[module_functor](/documentation/code/classes/classgambit_1_1module__functor/#function-module-functor)**(void(*)(TYPE &) inputFunction, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) func_name, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) func_capability, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) result_type, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) origin_name, [Models::ModelFunctorClaw](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/) & claw)<br>Constructor.  |
| virtual | **[~module_functor](/documentation/code/classes/classgambit_1_1module__functor/#function-module-functor)**()<br>Destructor.  |
| virtual void | **[setPrintRequirement](/documentation/code/classes/classgambit_1_1module__functor/#function-setprintrequirement)**(bool flag)<br>Setter for indicating if the wrapped function's result should to be printed.  |
| virtual bool | **[requiresPrinting](/documentation/code/classes/classgambit_1_1module__functor/#function-requiresprinting)**() const<br>Getter indicating if the wrapped function's result should to be printed.  |
| virtual void | **[calculate](/documentation/code/classes/classgambit_1_1module__functor/#function-calculate)**()<br>Calculate method.  |
| const TYPE & | **[operator()](/documentation/code/classes/classgambit_1_1module__functor/#function-operator)**(int index)<br>Operation (return value)  |
| [safe_ptr](/documentation/code/classes/classgambit_1_1safe__ptr/)< TYPE > | **[valuePtr](/documentation/code/classes/classgambit_1_1module__functor/#function-valueptr)**()<br>Alternative to operation (returns a safe pointer to value)  |
| virtual void | **[print](/documentation/code/classes/classgambit_1_1module__functor/#function-print)**([Printers::BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/) * printer, const int pointID, int index)<br>Printer function.  |
| virtual void | **[print](/documentation/code/classes/classgambit_1_1module__functor/#function-print)**([Printers::BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/) * printer, const int pointID)<br>Printer function (no-thread-index short-circuit)  |

**Protected Functions inherited from [Gambit::module_functor< ModelParameters >](/documentation/code/classes/classgambit_1_1module__functor/)**

|                | Name           |
| -------------- | -------------- |
| virtual void | **[init_memory](/documentation/code/classes/classgambit_1_1module__functor/#function-init-memory)**()<br>Initialise the memory of this functor.  |

**Protected Attributes inherited from [Gambit::module_functor< ModelParameters >](/documentation/code/classes/classgambit_1_1module__functor/)**

|                | Name           |
| -------------- | -------------- |
| void(*)(TYPE &) | **[myFunction](/documentation/code/classes/classgambit_1_1module__functor/#variable-myfunction)** <br>Internal storage of function pointer.  |
| TYPE * | **[myValue](/documentation/code/classes/classgambit_1_1module__functor/#variable-myvalue)** <br>Internal pointer to storage location of function value.  |
| bool | **[myPrintFlag](/documentation/code/classes/classgambit_1_1module__functor/#variable-myprintflag)** <br>Flag to select whether or not the results of this functor should be sent to the printer object.  |

**Public Functions inherited from [Gambit::module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/)**

|                | Name           |
| -------------- | -------------- |
| | **[module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/#function-module-functor-common)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) func_name, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) func_capability, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) result_type, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) origin_name, [Models::ModelFunctorClaw](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/) & claw)<br>Constructor.  |
| virtual | **[~module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/#function-module-functor-common)**()<br>Destructor.  |
| virtual double | **[getRuntimeAverage](/documentation/code/classes/classgambit_1_1module__functor__common/#function-getruntimeaverage)**()<br>Getter for averaged runtime.  |
| virtual void | **[reset](/documentation/code/classes/classgambit_1_1module__functor__common/#function-reset)**()<br>Reset functor.  |
| virtual void | **[notifyOfInvalidation](/documentation/code/classes/classgambit_1_1module__functor__common/#function-notifyofinvalidation)**(const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & msg)<br>Tell the functor that it invalidated the current point in model space, pass a message explaining why, and throw an exception.  |
| virtual double | **[getInvalidationRate](/documentation/code/classes/classgambit_1_1module__functor__common/#function-getinvalidationrate)**()<br>Getter for invalidation rate.  |
| virtual void | **[setFadeRate](/documentation/code/classes/classgambit_1_1module__functor__common/#function-setfaderate)**(double new_rate)<br>Setter for the fade rate.  |
| virtual void | **[setTimingPrintRequirement](/documentation/code/classes/classgambit_1_1module__functor__common/#function-settimingprintrequirement)**(bool flag)<br>Setter for indicating if the timing data for this function's execution should be printed.  |
| virtual bool | **[requiresTimingPrinting](/documentation/code/classes/classgambit_1_1module__functor__common/#function-requirestimingprinting)**() const<br>Getter indicating if the timing data for this function's execution should be printed.  |
| bool | **[getActiveModelFlag](/documentation/code/classes/classgambit_1_1module__functor__common/#function-getactivemodelflag)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) model)<br>Indicate whether or not a known model is activated or not.  |
| [safe_ptr](/documentation/code/classes/classgambit_1_1safe__ptr/)< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > | **[getChosenReqFromGroup](/documentation/code/classes/classgambit_1_1module__functor__common/#function-getchosenreqfromgroup)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) group)<br>Return a safe pointer to a string indicating which backend requirement has been activated for a given backend group.  |
| virtual void | **[iterate](/documentation/code/classes/classgambit_1_1module__functor__common/#function-iterate)**(long long iteration)<br>Execute a single iteration in the loop managed by this functor.  |
| virtual void | **[init_myCurrentIteration_if_NULL](/documentation/code/classes/classgambit_1_1module__functor__common/#function-init-mycurrentiteration-if-null)**()<br>Initialise the array holding the current iteration(s) of this functor.  |
| virtual void | **[setIteration](/documentation/code/classes/classgambit_1_1module__functor__common/#function-setiteration)**(long long iteration)<br>Setter for setting the iteration number in the loop in which this functor runs.  |
| virtual [omp_safe_ptr](/documentation/code/classes/classgambit_1_1omp__safe__ptr/)< long long > | **[iterationPtr](/documentation/code/classes/classgambit_1_1module__functor__common/#function-iterationptr)**()<br>Return a safe pointer to the iteration number in the loop in which this functor runs.  |
| virtual void | **[setCanBeLoopManager](/documentation/code/classes/classgambit_1_1module__functor__common/#function-setcanbeloopmanager)**(bool canManage)<br>Setter for specifying whether this is permitted to be a manager functor, which runs other functors nested in a loop.  |
| virtual bool | **[canBeLoopManager](/documentation/code/classes/classgambit_1_1module__functor__common/#function-canbeloopmanager)**()<br>Getter for revealing whether this is permitted to be a manager functor.  |
| virtual void | **[setLoopManagerCapType](/documentation/code/classes/classgambit_1_1module__functor__common/#function-setloopmanagercaptype)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) cap, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) t)<br>Setter for specifying the capability required of a manager functor, if it is to run this functor nested in a loop.  |
| virtual [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[loopManagerCapability](/documentation/code/classes/classgambit_1_1module__functor__common/#function-loopmanagercapability)**()<br>Getter for revealing the required capability of the wrapped function's loop manager.  |
| virtual [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[loopManagerType](/documentation/code/classes/classgambit_1_1module__functor__common/#function-loopmanagertype)**()<br>Getter for revealing the required type of the wrapped function's loop manager.  |
| virtual [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[loopManagerName](/documentation/code/classes/classgambit_1_1module__functor__common/#function-loopmanagername)**()<br>Getter for revealing the name of the wrapped function's assigned loop manager.  |
| virtual [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[loopManagerOrigin](/documentation/code/classes/classgambit_1_1module__functor__common/#function-loopmanagerorigin)**()<br>Getter for revealing the module of the wrapped function's assigned loop manager.  |
| virtual void | **[breakLoopFromManagedFunctor](/documentation/code/classes/classgambit_1_1module__functor__common/#function-breakloopfrommanagedfunctor)**()<br>Tell the manager of the loop in which this functor runs that it is time to break the loop.  |
| virtual [safe_ptr](/documentation/code/classes/classgambit_1_1safe__ptr/)< bool > | **[loopIsDone](/documentation/code/classes/classgambit_1_1module__functor__common/#function-loopisdone)**()<br>Return a safe pointer to the flag indicating that a loop managed by this functor should break now.  |
| virtual void | **[resetLoop](/documentation/code/classes/classgambit_1_1module__functor__common/#function-resetloop)**()<br>Provide a way to reset the flag indicating that a loop managed by this functor should break.  |
| virtual void | **[breakLoop](/documentation/code/classes/classgambit_1_1module__functor__common/#function-breakloop)**()<br>Tell the functor that the loop it manages should break now.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > | **[dependencies](/documentation/code/classes/classgambit_1_1module__functor__common/#function-dependencies)**()<br>Getter for listing currently activated dependencies.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > | **[backendclassloading](/documentation/code/classes/classgambit_1_1module__functor__common/#function-backendclassloading)**()<br>Getter for listing backends that require class loading.  |
| virtual std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > | **[backendgroups](/documentation/code/classes/classgambit_1_1module__functor__common/#function-backendgroups)**()<br>Getter for listing backend requirement groups.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > | **[backendreqs](/documentation/code/classes/classgambit_1_1module__functor__common/#function-backendreqs)**()<br>Getter for listing all backend requirements.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > | **[backendreqs](/documentation/code/classes/classgambit_1_1module__functor__common/#function-backendreqs)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) group)<br>Getter for listing backend requirements from a specific group.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > | **[backendspermitted](/documentation/code/classes/classgambit_1_1module__functor__common/#function-backendspermitted)**([sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) quant)<br>Getter for listing permitted backends.  |
| virtual std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > | **[backendreq_tags](/documentation/code/classes/classgambit_1_1module__functor__common/#function-backendreq-tags)**([sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) quant)<br>Getter for listing tags associated with backend requirements.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > | **[forcematchingbackend](/documentation/code/classes/classgambit_1_1module__functor__common/#function-forcematchingbackend)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) tag)<br>Getter for listing backend requirements that must be resolved from the same backend.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > | **[backend_conditional_dependencies](/documentation/code/classes/classgambit_1_1module__functor__common/#function-backend-conditional-dependencies)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) req, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) type, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) be, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) ver)<br>Getter for listing backend-specific conditional dependencies (4-string version)  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > | **[backend_conditional_dependencies](/documentation/code/classes/classgambit_1_1module__functor__common/#function-backend-conditional-dependencies)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) req, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) type, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) be)<br>Getter for backend-specific conditional dependencies (3-string version)  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > | **[backend_conditional_dependencies](/documentation/code/classes/classgambit_1_1module__functor__common/#function-backend-conditional-dependencies)**([functor](/documentation/code/classes/classgambit_1_1functor/) * be_functor)<br>Getter for backend-specific conditional dependencies (backend functor pointer version)  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > | **[model_conditional_dependencies](/documentation/code/classes/classgambit_1_1module__functor__common/#function-model-conditional-dependencies)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) model)<br>Getter for listing model-specific conditional dependencies.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > | **[model_conditional_backend_reqs](/documentation/code/classes/classgambit_1_1module__functor__common/#function-model-conditional-backend-reqs)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) model)<br>Getter for listing model-specific conditional backend requirements.  |
| void | **[setDependency](/documentation/code/classes/classgambit_1_1module__functor__common/#function-setdependency)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) dep, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) dep_type, void(*)([functor](/documentation/code/classes/classgambit_1_1functor/) *, [module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/) *) resolver, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) purpose ="")<br>Add and activate unconditional dependencies.  |
| void | **[setConditionalDependency](/documentation/code/classes/classgambit_1_1module__functor__common/#function-setconditionaldependency)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) dep, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) dep_type)<br>Add conditional dependency-type pairs in advance of later conditions.  |
| void | **[setBackendConditionalDependency](/documentation/code/classes/classgambit_1_1module__functor__common/#function-setbackendconditionaldependency)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) req, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) be, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) ver, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) dep, void(*)([functor](/documentation/code/classes/classgambit_1_1functor/) *, [module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/) *) resolver)<br>Add a backend conditional dependency for multiple backend versions.  |
| void | **[setBackendConditionalDependencySingular](/documentation/code/classes/classgambit_1_1module__functor__common/#function-setbackendconditionaldependencysingular)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) req, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) be, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) ver, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) dep, void(*)([functor](/documentation/code/classes/classgambit_1_1functor/) *, [module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/) *) resolver)<br>Add a backend conditional dependency for a single backend version.  |
| void | **[setModelConditionalDependency](/documentation/code/classes/classgambit_1_1module__functor__common/#function-setmodelconditionaldependency)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) model, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) dep, void(*)([functor](/documentation/code/classes/classgambit_1_1functor/) *, [module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/) *) resolver)<br>Add a model conditional dependency for multiple models.  |
| void | **[setModelConditionalDependencySingular](/documentation/code/classes/classgambit_1_1module__functor__common/#function-setmodelconditionaldependencysingular)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) model, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) dep, void(*)([functor](/documentation/code/classes/classgambit_1_1functor/) *, [module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/) *) resolver)<br>Add a model conditional dependency for a single model.  |
| void | **[makeBackendRuleForModel](/documentation/code/classes/classgambit_1_1module__functor__common/#function-makebackendruleformodel)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) model, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) tag)<br>Add a rule for activating backend requirements according to the model being scanned.  |
| void | **[setBackendReq](/documentation/code/classes/classgambit_1_1module__functor__common/#function-setbackendreq)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) group, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) req, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) tags, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) type, void(*)([functor](/documentation/code/classes/classgambit_1_1functor/) *) resolver) |
| void | **[setModelConditionalBackendReq](/documentation/code/classes/classgambit_1_1module__functor__common/#function-setmodelconditionalbackendreq)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) model, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) req, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) type)<br>Add a model conditional backend requirement for multiple models.  |
| void | **[setModelConditionalBackendReqSingular](/documentation/code/classes/classgambit_1_1module__functor__common/#function-setmodelconditionalbackendreqsingular)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) model, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) req, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) type)<br>Add a model conditional backend requirement for a single model.  |
| void | **[makeBackendOptionRule](/documentation/code/classes/classgambit_1_1module__functor__common/#function-makebackendoptionrule)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) be_and_ver, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) tag)<br>Add a rule for dictating which backends can be used to fulfill which backend requirements.  |
| void | **[setPermittedBackend](/documentation/code/classes/classgambit_1_1module__functor__common/#function-setpermittedbackend)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) req, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) be, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) ver)<br>Add a single permitted backend version.  |
| void | **[makeBackendMatchingRule](/documentation/code/classes/classgambit_1_1module__functor__common/#function-makebackendmatchingrule)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) tag)<br>Add one or more rules for forcing backends reqs with the same tags to always be resolved from the same backend.  |
| void | **[setRequiredClassloader](/documentation/code/classes/classgambit_1_1module__functor__common/#function-setrequiredclassloader)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) be, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) ver, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) safe_ver)<br>Add a rule indicating that classes from a given backend must be available.  |
| virtual void | **[notifyOfBackends](/documentation/code/classes/classgambit_1_1module__functor__common/#function-notifyofbackends)**(std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > > be_ver_map)<br>Indicate to the functor which backends are actually loaded and working.  |
| virtual void | **[setNestedList](/documentation/code/classes/classgambit_1_1module__functor__common/#function-setnestedlist)**(std::vector< [functor](/documentation/code/classes/classgambit_1_1functor/) * > & newNestedList)<br>Set the ordered list of pointers to other functors that should run nested in a loop managed by this one.  |
| virtual void | **[resolveDependency](/documentation/code/classes/classgambit_1_1module__functor__common/#function-resolvedependency)**([functor](/documentation/code/classes/classgambit_1_1functor/) * dep_functor)<br>Resolve a dependency using a pointer to another functor object.  |
| virtual void | **[resolveLoopManager](/documentation/code/classes/classgambit_1_1module__functor__common/#function-resolveloopmanager)**([functor](/documentation/code/classes/classgambit_1_1functor/) * dep_functor)<br>Set this functor's loop manager (if it has one)  |
| virtual void | **[resolveBackendReq](/documentation/code/classes/classgambit_1_1module__functor__common/#function-resolvebackendreq)**([functor](/documentation/code/classes/classgambit_1_1functor/) * be_functor)<br>Resolve a backend requirement using a pointer to another functor object.  |
| virtual void | **[notifyOfModel](/documentation/code/classes/classgambit_1_1module__functor__common/#function-notifyofmodel)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) model)<br>Notify the functor that a certain model is being scanned, so that it can activate its dependencies and backend reqs accordingly.  |
| virtual void | **[notifyOfDependee](/documentation/code/classes/classgambit_1_1module__functor__common/#function-notifyofdependee)**([functor](/documentation/code/classes/classgambit_1_1functor/) * dependent_functor)<br>Notify the functor that another functor depends on it.  |
| virtual [invalid_point_exception](/documentation/code/classes/classgambit_1_1invalid__point__exception/) * | **[retrieve_invalid_point_exception](/documentation/code/classes/classgambit_1_1module__functor__common/#function-retrieve-invalid-point-exception)**()<br>Retrieve the previously saved exception generated when this functor invalidated the current point in model space.  |

**Protected Functions inherited from [Gambit::module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/)**

|                | Name           |
| -------------- | -------------- |
| virtual void | **[reset](/documentation/code/classes/classgambit_1_1module__functor__common/#function-reset)**(int thread_num)<br>Reset functor for one thread only.  |
| virtual void | **[acknowledgeInvalidation](/documentation/code/classes/classgambit_1_1module__functor__common/#function-acknowledgeinvalidation)**([invalid_point_exception](/documentation/code/classes/classgambit_1_1invalid__point__exception/) & e, [functor](/documentation/code/classes/classgambit_1_1functor/) * f =NULL)<br>Acknowledge that this functor invalidated the current point in model space.  |
| virtual void | **[startTiming](/documentation/code/classes/classgambit_1_1module__functor__common/#function-starttiming)**(int thread_num)<br>Do pre-calculate timing things.  |
| virtual void | **[finishTiming](/documentation/code/classes/classgambit_1_1module__functor__common/#function-finishtiming)**(int thread_num)<br>Do post-calculate timing things.  |
| virtual void | **[init_memory](/documentation/code/classes/classgambit_1_1module__functor__common/#function-init-memory)**()<br>Initialise the memory of this functor.  |
| void | **[fill_activeModelFlags](/documentation/code/classes/classgambit_1_1module__functor__common/#function-fill-activemodelflags)**()<br>Construct the list of known models only if it doesn't yet exist.  |
| [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) | **[retrieve_conditional_dep_type_pair](/documentation/code/classes/classgambit_1_1module__functor__common/#function-retrieve-conditional-dep-type-pair)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) dep)<br>Retrieve full conditional dependency-type pair from conditional dependency only.  |
| void | **[check_missing_LogTag](/documentation/code/classes/classgambit_1_1module__functor__common/#function-check-missing-logtag)**()<br>Check if an appropriate LogTag for this functor is missing from the logging system.  |
| void | **[entering_multithreaded_region](/documentation/code/classes/classgambit_1_1module__functor__common/#function-entering-multithreaded-region)**() |
| void | **[leaving_multithreaded_region](/documentation/code/classes/classgambit_1_1module__functor__common/#function-leaving-multithreaded-region)**() |

**Protected Attributes inherited from [Gambit::module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/)**

|                | Name           |
| -------------- | -------------- |
| bool | **[myTimingPrintFlag](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-mytimingprintflag)** <br>Flag to select whether or not the timing data for this function's execution should be printed;.  |
| std::chrono::time_point< std::chrono::system_clock > * | **[start](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-start)** <br>Beginning and end timing points.  |
| std::chrono::time_point< std::chrono::system_clock > * | **[end](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-end)**  |
| bool | **[point_exception_raised](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-point-exception-raised)** <br>A flag indicating whether or not this functor has invalidated the current point.  |
| [invalid_point_exception](/documentation/code/classes/classgambit_1_1invalid__point__exception/) | **[raised_point_exception](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-raised-point-exception)** <br>An exception raised because this functor has invalidated the current point.  |
| double | **[runtime_average](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-runtime-average)** <br>Averaged runtime in ns.  |
| double | **[fadeRate](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-faderate)** <br>Fade rate for average runtime.  |
| double | **[pInvalidation](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-pinvalidation)** <br>Probability that functors invalidates point in model parameter space.  |
| bool * | **[needs_recalculating](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-needs-recalculating)** <br>Needs recalculating or not?  |
| bool * | **[already_printed](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-already-printed)** <br>Has result already been sent to the printer?  |
| bool * | **[already_printed_timing](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-already-printed-timing)** <br>Has timing data already been sent to the printer?  |
| bool | **[iCanManageLoops](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-icanmanageloops)** <br>Flag indicating whether this function can manage a loop over other functions.  |
| bool | **[myLoopIsDone](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-myloopisdone)** <br>Flag indicating whether this function is ready to finish its loop (only relevant if iCanManageLoops = true)  |
| bool | **[iRunNested](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-irunnested)** <br>Flag indicating whether this function can run nested in a loop over functions.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[myLoopManagerCapability](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-myloopmanagercapability)** <br>Capability of a function that mangages a loop that this function can run inside of.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[myLoopManagerType](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-myloopmanagertype)** <br>Capability of a function that mangages a loop that this function can run inside of.  |
| [functor](/documentation/code/classes/classgambit_1_1functor/) * | **[myLoopManager](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-myloopmanager)** <br>Pointer to the functor that mangages the loop that this function runs inside of.  |
| std::vector< [functor](/documentation/code/classes/classgambit_1_1functor/) * > | **[myNestedFunctorList](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-mynestedfunctorlist)** <br>Vector of functors that have been set up to run nested within this one.  |
| long long * | **[myCurrentIteration](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-mycurrentiteration)** <br>Pointer to counters for iterations of nested functor loop.  |
| const int | **[globlMaxThreads](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-globlmaxthreads)** <br>Maximum number of OpenMP threads this MPI process is permitted to launch in total.  |
| std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > | **[myGroups](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-mygroups)** <br>Internal list of backend groups that this functor's requirements fall into.  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > | **[chosenReqsFromGroups](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-chosenreqsfromgroups)** <br>Map from groups to backend reqs, indicating which backend req has been activated for which backend group.  |
| std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > | **[myBackendReqs](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-mybackendreqs)** <br>Set of all backend requirement-type string pairs.  |
| std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > | **[myResolvableBackendReqs](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-myresolvablebackendreqs)** <br>Set of all backend requirement-type string pairs currently available for resolution.  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > > | **[myGroupedBackendReqs](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-mygroupedbackendreqs)** <br>Set of backend requirement-type string pairs for specific backend groups.  |
| std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > | **[myDependencies](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-mydependencies)** <br>Vector of dependency-type string pairs.  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > | **[myConditionalDependencies](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-myconditionaldependencies)** <br>Map of conditional dependencies to their types.  |
| std::map< std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) >, std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > > | **[myBackendConditionalDependencies](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-mybackendconditionaldependencies)** <br>Map from (vector with 4 strings: backend req, type, backend, version) to (set of {conditional dependency-type} pairs)  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > > | **[myModelConditionalDependencies](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-mymodelconditionaldependencies)** <br>Map from models to (set of {conditional dependency-type} pairs)  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > > | **[myModelConditionalBackendReqs](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-mymodelconditionalbackendreqs)** <br>Map from models to (set of {conditional backend requirement-type} pairs)  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), bool > | **[activeModelFlags](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-activemodelflags)** <br>Map from known models to flags indicating if they are activated or not (known = allowed, in allowed groups or conditions for conditional dependencies)  |
| std::map< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair), void(*)([functor](/documentation/code/classes/classgambit_1_1functor/) *, [module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/) *)> | **[dependency_map](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-dependency-map)**  |
| std::map< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair), [functor](/documentation/code/classes/classgambit_1_1functor/) * > | **[dependency_functor_map](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-dependency-functor-map)**  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > | **[backendreq_types](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-backendreq-types)** <br>Map from backend requirements to their required types.  |
| std::map< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair), [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > | **[backendreq_groups](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-backendreq-groups)** <br>Map from backend requirements to their designated groups.  |
| std::map< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair), std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > > | **[backendreq_tagmap](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-backendreq-tagmap)** <br>Map from backend requirements to their rule tags.  |
| std::map< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair), void(*)([functor](/documentation/code/classes/classgambit_1_1functor/) *)> | **[backendreq_map](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-backendreq-map)**  |
| std::map< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair), std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > > | **[permitted_map](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-permitted-map)** <br>Map from (backend requirement-type pairs) to (set of permitted {backend-version} pairs)  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > > | **[myForcedMatches](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-myforcedmatches)** <br>Map from tags to sets of matching (backend requirement-type pairs) that are forced to use the same backend.  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > > | **[required_classloading_backends](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-required-classloading-backends)** <br>Map from required classloading backends to their versions.  |
| std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > | **[missing_backends](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-missing-backends)** <br>Vector of required backends currently missing.  |
| timespec | **[tp](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-tp)** <br>Internal timespec object.  |
| int | **[myLogTag](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-mylogtag)** <br>Integer LogTag, for tagging log messages.  |
| bool | **[signal_mode_locked](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-signal-mode-locked)**  |

**Friends inherited from [Gambit::module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/)**

|                | Name           |
| -------------- | -------------- |
| void | **[FunctorHelp::entering_multithreaded_region](/documentation/code/classes/classgambit_1_1module__functor__common/#friend-functorhelpentering-multithreaded-region)**([module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/) & ) <br>Connectors to external helper functions (to decouple signal handling from this class)  |
| void | **[FunctorHelp::leaving_multithreaded_region](/documentation/code/classes/classgambit_1_1module__functor__common/#friend-functorhelpleaving-multithreaded-region)**([module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/) & )  |

**Public Functions inherited from [Gambit::functor](/documentation/code/classes/classgambit_1_1functor/)**

|                | Name           |
| -------------- | -------------- |
| virtual double | **[getRuntimeAverage](/documentation/code/classes/classgambit_1_1functor/#function-getruntimeaverage)**() |
| virtual double | **[getInvalidationRate](/documentation/code/classes/classgambit_1_1functor/#function-getinvalidationrate)**() |
| virtual void | **[setFadeRate](/documentation/code/classes/classgambit_1_1functor/#function-setfaderate)**(double ) |
| virtual void | **[notifyOfInvalidation](/documentation/code/classes/classgambit_1_1functor/#function-notifyofinvalidation)**(const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & ) |
| virtual void | **[reset](/documentation/code/classes/classgambit_1_1functor/#function-reset)**() |
| | **[functor](/documentation/code/classes/classgambit_1_1functor/#function-functor)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) func_name, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) func_capability, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) result_type, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) origin_name, [Models::ModelFunctorClaw](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/) & claw)<br>Constructor.  |
| virtual | **[~functor](/documentation/code/classes/classgambit_1_1functor/#function-functor)**() |
| virtual void | **[calculate](/documentation/code/classes/classgambit_1_1functor/#function-calculate)**()<br>Virtual [calculate()](); needs to be redefined in daughters.  |
| virtual void | **[reset_and_calculate](/documentation/code/classes/classgambit_1_1functor/#function-reset-and-calculate)**()<br>Reset-then-recalculate method.  |
| void | **[setStatus](/documentation/code/classes/classgambit_1_1functor/#function-setstatus)**(int stat) |
| virtual void | **[setInUse](/documentation/code/classes/classgambit_1_1functor/#function-setinuse)**(bool )<br>Set the inUse flag (must be overridden in derived class to have any effect).  |
| void | **[setPurpose](/documentation/code/classes/classgambit_1_1functor/#function-setpurpose)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) purpose)<br>Setter for purpose (relevant only for next-to-output functors)  |
| void | **[setVertexID](/documentation/code/classes/classgambit_1_1functor/#function-setvertexid)**(int ID)<br>Setter for vertex ID (used in printer system)  |
| void | **[setTimingVertexID](/documentation/code/classes/classgambit_1_1functor/#function-settimingvertexid)**(int ID)<br>Set ID for timing 'vertex' (used in printer system)  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[name](/documentation/code/classes/classgambit_1_1functor/#function-name)**() const<br>Getter for the wrapped function's name.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[capability](/documentation/code/classes/classgambit_1_1functor/#function-capability)**() const<br>Getter for the wrapped function's reported capability.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[type](/documentation/code/classes/classgambit_1_1functor/#function-type)**() const<br>Getter for the wrapped function's reported return type.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[origin](/documentation/code/classes/classgambit_1_1functor/#function-origin)**() const<br>Getter for the wrapped function's origin (module or backend name)  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[version](/documentation/code/classes/classgambit_1_1functor/#function-version)**() const<br>Getter for the version of the wrapped function's origin (module or backend)  |
| virtual [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[safe_version](/documentation/code/classes/classgambit_1_1functor/#function-safe-version)**() const<br>Getter for the 'safe' incarnation of the version of the wrapped function's origin (module or backend)  |
| int | **[status](/documentation/code/classes/classgambit_1_1functor/#function-status)**() const |
| [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) | **[quantity](/documentation/code/classes/classgambit_1_1functor/#function-quantity)**() const<br>Getter for the overall quantity provided by the wrapped function (capability-type pair)  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[purpose](/documentation/code/classes/classgambit_1_1functor/#function-purpose)**() const<br>Getter for purpose (relevant for output nodes, aka helper structures for the dep. resolution)  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[citationKey](/documentation/code/classes/classgambit_1_1functor/#function-citationkey)**() const<br>Getter for the citation key.  |
| int | **[vertexID](/documentation/code/classes/classgambit_1_1functor/#function-vertexid)**() const<br>Getter for vertex ID.  |
| int | **[timingVertexID](/documentation/code/classes/classgambit_1_1functor/#function-timingvertexid)**() const<br>Getter for timing vertex ID.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[label](/documentation/code/classes/classgambit_1_1functor/#function-label)**() const<br>Getter for string label.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[timingLabel](/documentation/code/classes/classgambit_1_1functor/#function-timinglabel)**() const<br>Getter for the printer timing label.  |
| virtual bool | **[requiresPrinting](/documentation/code/classes/classgambit_1_1functor/#function-requiresprinting)**() const<br>Getter indicating if the wrapped function's result should to be printed.  |
| virtual bool | **[requiresTimingPrinting](/documentation/code/classes/classgambit_1_1functor/#function-requirestimingprinting)**() const<br>Getter indicating if the timing data for this function's execution should be printed.  |
| virtual void | **[setPrintRequirement](/documentation/code/classes/classgambit_1_1functor/#function-setprintrequirement)**(bool flag)<br>Setter for indicating if the wrapped function's result should to be printed.  |
| virtual void | **[setTimingPrintRequirement](/documentation/code/classes/classgambit_1_1functor/#function-settimingprintrequirement)**(bool flag)<br>Setter for indicating if the timing data for this function's execution should be printed.  |
| virtual void | **[setNestedList](/documentation/code/classes/classgambit_1_1functor/#function-setnestedlist)**(std::vector< [functor](/documentation/code/classes/classgambit_1_1functor/) * > & )<br>Set the ordered list of pointers to other functors that should run nested in a loop managed by this one.  |
| virtual void | **[setIteration](/documentation/code/classes/classgambit_1_1functor/#function-setiteration)**(long long )<br>Set the iteration number in a loop in which this functor runs.  |
| virtual bool | **[canBeLoopManager](/documentation/code/classes/classgambit_1_1functor/#function-canbeloopmanager)**()<br>Getter for revealing whether this is permitted to be a manager functor.  |
| virtual [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[loopManagerCapability](/documentation/code/classes/classgambit_1_1functor/#function-loopmanagercapability)**()<br>Getter for revealing the required capability of the wrapped function's loop manager.  |
| virtual [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[loopManagerType](/documentation/code/classes/classgambit_1_1functor/#function-loopmanagertype)**()<br>Getter for revealing the required type of the wrapped function's loop manager.  |
| virtual [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[loopManagerName](/documentation/code/classes/classgambit_1_1functor/#function-loopmanagername)**()<br>Getter for revealing the name of the wrapped function's assigned loop manager.  |
| virtual [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[loopManagerOrigin](/documentation/code/classes/classgambit_1_1functor/#function-loopmanagerorigin)**()<br>Getter for revealing the module of the wrapped function's assigned loop manager.  |
| virtual void | **[breakLoop](/documentation/code/classes/classgambit_1_1functor/#function-breakloop)**()<br>Tell the functor that the loop it manages should break now.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > | **[dependencies](/documentation/code/classes/classgambit_1_1functor/#function-dependencies)**()<br>Getter for listing currently activated dependencies.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > | **[backendclassloading](/documentation/code/classes/classgambit_1_1functor/#function-backendclassloading)**()<br>Getter for listing backends that require class loading.  |
| virtual std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > | **[backendgroups](/documentation/code/classes/classgambit_1_1functor/#function-backendgroups)**()<br>Getter for listing backend requirement groups.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > | **[backendreqs](/documentation/code/classes/classgambit_1_1functor/#function-backendreqs)**()<br>Getter for listing all backend requirements.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > | **[backendreqs](/documentation/code/classes/classgambit_1_1functor/#function-backendreqs)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) )<br>Getter for listing backend requirements from a specific group.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > | **[backendspermitted](/documentation/code/classes/classgambit_1_1functor/#function-backendspermitted)**([sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) )<br>Getter for listing permitted backends.  |
| virtual std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > | **[backendreq_tags](/documentation/code/classes/classgambit_1_1functor/#function-backendreq-tags)**([sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) )<br>Getter for listing tags associated with backend requirements.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > | **[forcematchingbackend](/documentation/code/classes/classgambit_1_1functor/#function-forcematchingbackend)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) )<br>Getter for listing backend requirements that must be resolved from the same backend.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > | **[backend_conditional_dependencies](/documentation/code/classes/classgambit_1_1functor/#function-backend-conditional-dependencies)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) , [str](/documentation/code/namespaces/namespacegambit/#typedef-str) , [str](/documentation/code/namespaces/namespacegambit/#typedef-str) , [str](/documentation/code/namespaces/namespacegambit/#typedef-str) )<br>Getter for listing backend-specific conditional dependencies (4-string version)  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > | **[backend_conditional_dependencies](/documentation/code/classes/classgambit_1_1functor/#function-backend-conditional-dependencies)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) req, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) type, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) be)<br>Getter for backend-specific conditional dependencies (3-string version)  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > | **[backend_conditional_dependencies](/documentation/code/classes/classgambit_1_1functor/#function-backend-conditional-dependencies)**([functor](/documentation/code/classes/classgambit_1_1functor/) * be_functor)<br>Getter for backend-specific conditional dependencies (backend functor pointer version)  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > | **[model_conditional_dependencies](/documentation/code/classes/classgambit_1_1functor/#function-model-conditional-dependencies)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) )<br>Getter for listing model-specific conditional dependencies.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > | **[model_conditional_backend_reqs](/documentation/code/classes/classgambit_1_1functor/#function-model-conditional-backend-reqs)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) )<br>Getter for listing model-specific conditional backend requirements.  |
| virtual void | **[resolveDependency](/documentation/code/classes/classgambit_1_1functor/#function-resolvedependency)**([functor](/documentation/code/classes/classgambit_1_1functor/) * )<br>Resolve a dependency using a pointer to another functor object.  |
| virtual void | **[resolveLoopManager](/documentation/code/classes/classgambit_1_1functor/#function-resolveloopmanager)**([functor](/documentation/code/classes/classgambit_1_1functor/) * )<br>Set this functor's loop manager (if it has one)  |
| virtual void | **[resolveBackendReq](/documentation/code/classes/classgambit_1_1functor/#function-resolvebackendreq)**([functor](/documentation/code/classes/classgambit_1_1functor/) * )<br>Resolve a backend requirement using a pointer to another functor object.  |
| virtual void | **[notifyOfModel](/documentation/code/classes/classgambit_1_1functor/#function-notifyofmodel)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) )<br>Notify the functor that a certain model is being scanned, so that it can activate itself accordingly.  |
| virtual void | **[notifyOfDependee](/documentation/code/classes/classgambit_1_1functor/#function-notifyofdependee)**([functor](/documentation/code/classes/classgambit_1_1functor/) * )<br>Notify the functor that it is being used to fill a dependency of another functor.  |
| virtual void | **[notifyOfBackends](/documentation/code/classes/classgambit_1_1functor/#function-notifyofbackends)**(std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > > )<br>Indicate to the functor which backends are actually loaded and working.  |
| virtual void | **[print](/documentation/code/classes/classgambit_1_1functor/#function-print)**([Printers::BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/) * printer, const int pointID, int thread_num)<br>Printer function.  |
| virtual void | **[print](/documentation/code/classes/classgambit_1_1functor/#function-print)**([Printers::BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/) * printer, const int pointID)<br>Printer function (no-thread-index short-circuit)  |
| virtual [invalid_point_exception](/documentation/code/classes/classgambit_1_1invalid__point__exception/) * | **[retrieve_invalid_point_exception](/documentation/code/classes/classgambit_1_1functor/#function-retrieve-invalid-point-exception)**()<br>Retrieve the previously saved exception generated when this functor invalidated the current point in model space.  |
| void | **[notifyOfIniOptions](/documentation/code/classes/classgambit_1_1functor/#function-notifyofinioptions)**(const [Options](/documentation/code/classes/classgambit_1_1options/) & opt) |
| template <typename TYPE \> <br>void | **[setOption](/documentation/code/classes/classgambit_1_1functor/#function-setoption)**(const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & key, const TYPE val)<br>Set an option for the functor directly (for use in standalone executables).  |
| [safe_ptr](/documentation/code/classes/classgambit_1_1safe__ptr/)< [Options](/documentation/code/classes/classgambit_1_1options/) > | **[getOptions](/documentation/code/classes/classgambit_1_1functor/#function-getoptions)**()<br>Return a safe pointer to the options that this functor is supposed to run with (e.g. from the ini file).  |
| void | **[notifyOfSubCaps](/documentation/code/classes/classgambit_1_1functor/#function-notifyofsubcaps)**(const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & subcap_string)<br>Notify the functor about a string in [YAML](/documentation/code/namespaces/namespaceyaml/) that contains the sub-capability information (for use in standalones)  |
| void | **[notifyOfSubCaps](/documentation/code/classes/classgambit_1_1functor/#function-notifyofsubcaps)**(const [Options](/documentation/code/classes/classgambit_1_1options/) & subcaps)<br>Notify the functor about an instance of the options class that contains sub-capability information.  |
| template <typename TYPE \> <br>void | **[setSubCap](/documentation/code/classes/classgambit_1_1functor/#function-setsubcap)**(const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & key, const TYPE val)<br>Set a sub-capability (subcap)for the functor directly (for use in standalone executables).  |
| [safe_ptr](/documentation/code/classes/classgambit_1_1safe__ptr/)< [Options](/documentation/code/classes/classgambit_1_1options/) > | **[getSubCaps](/documentation/code/classes/classgambit_1_1functor/#function-getsubcaps)**()<br>Return a safe pointer to the subcaps that this functor realises it is supposed to facilitate downstream calculation of.  |
| [safe_ptr](/documentation/code/classes/classgambit_1_1safe__ptr/)< std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > > | **[getDependees](/documentation/code/classes/classgambit_1_1functor/#function-getdependees)**()<br>Return a safe pointer to the vector of all capability,type pairs of functors arranged downstream of this one in the dependency tree.  |
| bool | **[allModelsAllowed](/documentation/code/classes/classgambit_1_1functor/#function-allmodelsallowed)**()<br>Test whether the functor is allowed to be used with all models.  |
| bool | **[modelAllowed](/documentation/code/classes/classgambit_1_1functor/#function-modelallowed)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) model)<br>Test whether the functor is always allowed (either explicitly or implicitly) to be used with a given model.  |
| bool | **[modelExplicitlyAllowed](/documentation/code/classes/classgambit_1_1functor/#function-modelexplicitlyallowed)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) model)<br>Test whether the functor is explictly always allowed to be used with a given model.  |
| void | **[setAllowedModel](/documentation/code/classes/classgambit_1_1functor/#function-setallowedmodel)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) model)<br>Add a model to the internal list of models for which this functor is allowed to be used.  |
| bool | **[modelComboAllowed](/documentation/code/classes/classgambit_1_1functor/#function-modelcomboallowed)**(std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > combo)<br>Test whether the functor is allowed (either explicitly or implicitly) to be used with a given combination of models.  |
| bool | **[modelComboExplicitlyAllowed](/documentation/code/classes/classgambit_1_1functor/#function-modelcomboexplicitlyallowed)**(std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > combo)<br>Test whether the functor has been explictly allowed to be used with a given combination of models.  |
| void | **[setModelGroup](/documentation/code/classes/classgambit_1_1functor/#function-setmodelgroup)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) group, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) contents)<br>Add a model group definition to the internal list of model groups.  |
| void | **[setAllowedModelGroupCombo](/documentation/code/classes/classgambit_1_1functor/#function-setallowedmodelgroupcombo)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) groups)<br>Add a combination of model groups to the internal list of combinations for which this functor is allowed to be used.  |

**Protected Functions inherited from [Gambit::functor](/documentation/code/classes/classgambit_1_1functor/)**

|                | Name           |
| -------------- | -------------- |
| virtual void | **[reset](/documentation/code/classes/classgambit_1_1functor/#function-reset)**(int )<br>Reset functor for one thread only.  |
| void | **[failBigTime](/documentation/code/classes/classgambit_1_1functor/#function-failbigtime)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) method)<br>Attempt to retrieve a dependency or model parameter that has not been resolved.  |
| bool | **[allowed_parent_or_friend_exists](/documentation/code/classes/classgambit_1_1functor/#function-allowed-parent-or-friend-exists)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) model)<br>Test if there is a model in the functor's allowedModels list as which this model can be interpreted.  |
| bool | **[in_allowed_combo](/documentation/code/classes/classgambit_1_1functor/#function-in-allowed-combo)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) model)<br>Check that a model is actually part of a combination that is allowed to be used with this functor.  |
| bool | **[contains_anything_interpretable_as_member_of](/documentation/code/classes/classgambit_1_1functor/#function-contains-anything-interpretable-as-member-of)**(std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > combo, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) group)<br>Test whether any of the entries in a given model group is a valid interpretation of any members in a given combination.  |
| bool | **[has_common_elements](/documentation/code/classes/classgambit_1_1functor/#function-has-common-elements)**(std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > combo, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) group)<br>Work out whether a given combination of models and a model group have any elements in common.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[find_friend_or_parent_model_in_map](/documentation/code/classes/classgambit_1_1functor/#function-find-friend-or-parent-model-in-map)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) model, std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > > karta)<br>Try to find a parent or friend model in some user-supplied map from models to sspair vectors.  |

**Protected Attributes inherited from [Gambit::functor](/documentation/code/classes/classgambit_1_1functor/)**

|                | Name           |
| -------------- | -------------- |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[myName](/documentation/code/classes/classgambit_1_1functor/#variable-myname)** <br>Internal storage of the function name.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[myCapability](/documentation/code/classes/classgambit_1_1functor/#variable-mycapability)** <br>Internal storage of exactly what the function calculates.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[myType](/documentation/code/classes/classgambit_1_1functor/#variable-mytype)** <br>Internal storage of the type of what the function calculates.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[myOrigin](/documentation/code/classes/classgambit_1_1functor/#variable-myorigin)** <br>Internal storage of the name of the module or backend to which the function belongs.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[myVersion](/documentation/code/classes/classgambit_1_1functor/#variable-myversion)** <br>Internal storage of the version of the module or backend to which the function belongs.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[myPurpose](/documentation/code/classes/classgambit_1_1functor/#variable-mypurpose)** <br>Purpose of the function (relevant for output and next-to-output functors)  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[myCitationKey](/documentation/code/classes/classgambit_1_1functor/#variable-mycitationkey)** <br>Citation key: BibTex key of the reference.  |
| const [Models::ModelFunctorClaw](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/) * | **[myClaw](/documentation/code/classes/classgambit_1_1functor/#variable-myclaw)** <br>Bound model functor claw, for checking relationships between models.  |
| const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[myLabel](/documentation/code/classes/classgambit_1_1functor/#variable-mylabel)** <br>String label, used to label functor results for printer system.  |
| const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[myTimingLabel](/documentation/code/classes/classgambit_1_1functor/#variable-mytiminglabel)** <br>String label, used to label functor timing data for printer system.  |
| int | **[myStatus](/documentation/code/classes/classgambit_1_1functor/#variable-mystatus)**  |
| int | **[myVertexID](/documentation/code/classes/classgambit_1_1functor/#variable-myvertexid)** <br>Internal storage of the vertex ID number used by the printer system to identify functors.  |
| int | **[myTimingVertexID](/documentation/code/classes/classgambit_1_1functor/#variable-mytimingvertexid)** <br>ID assigned by printers to the timing data output stream.  |
| bool | **[verbose](/documentation/code/classes/classgambit_1_1functor/#variable-verbose)** <br>Debug flag.  |
| [Options](/documentation/code/classes/classgambit_1_1options/) | **[myOptions](/documentation/code/classes/classgambit_1_1functor/#variable-myoptions)** <br>Internal storage of function options, as a [YAML](/documentation/code/namespaces/namespaceyaml/) node.  |
| [Options](/documentation/code/classes/classgambit_1_1options/) | **[mySubCaps](/documentation/code/classes/classgambit_1_1functor/#variable-mysubcaps)** <br>Internal storage of function sub-capabilities, as a [YAML](/documentation/code/namespaces/namespaceyaml/) node.  |
| std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > | **[myDependees](/documentation/code/classes/classgambit_1_1functor/#variable-mydependees)** <br>List of all capability,type pairs of functors downstream of this one in the dependency tree.  |
| std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > | **[allowedModels](/documentation/code/classes/classgambit_1_1functor/#variable-allowedmodels)** <br>List of allowed models.  |
| std::set< std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > > | **[allowedGroupCombos](/documentation/code/classes/classgambit_1_1functor/#variable-allowedgroupcombos)** <br>List of allowed model group combinations.  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > > | **[modelGroups](/documentation/code/classes/classgambit_1_1functor/#variable-modelgroups)** <br>Map from model group names to group contents.  |


## Public Functions Documentation

### function model_functor

```
model_functor(
    void(*)(ModelParameters &) inputFunction,
    str func_name,
    str func_capability,
    str result_type,
    str origin_name,
    Models::ModelFunctorClaw & claw
)
```

Constructor. 

Model functor class method definitions.

Constructor 


### function setModelName

```
void setModelName(
    str model_name
)
```

Function for setting the model name for a [ModelParameters]() object. Mainly for better error messages. 

### function addParameter

```
void addParameter(
    str parname
)
```

Function for adding a new parameter to the map inside the [ModelParameters]() object. 

### function donateParameters

```
void donateParameters(
    model_functor & receiver
)
```

Function for handing over parameter identities to another [model_functor](/documentation/code/classes/classgambit_1_1model__functor/). 

Copy the model name as well


### function ~model_functor

```
inline virtual ~model_functor()
```

Destructor. 

-------------------------------

Updated on 2022-09-08 at 02:27:26 +0000