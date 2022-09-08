---
title: "class Gambit::module_functor_common"
description: "Functor derived class for module functions. "

---

# class Gambit::module_functor_common



Functor derived class for module functions. 


`#include <functors.hpp>`

Inherits from [Gambit::functor](/documentation/code/classes/classgambit_1_1functor/)

Inherited by [Gambit::module_functor< ModelParameters >](/documentation/code/classes/classgambit_1_1module__functor/), [Gambit::module_functor< TYPE >](/documentation/code/classes/classgambit_1_1module__functor/), [Gambit::module_functor< void >](/documentation/code/classes/classgambit_1_1module__functor_3_01void_01_4/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-module-functor-common)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) func_name, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) func_capability, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) result_type, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) origin_name, [Models::ModelFunctorClaw](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/) & claw)<br>Constructor.  |
| virtual | **[~module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-module-functor-common)**()<br>Destructor.  |
| virtual double | **[getRuntimeAverage](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-getruntimeaverage)**()<br>Getter for averaged runtime.  |
| virtual void | **[reset](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-reset)**()<br>Reset functor.  |
| virtual void | **[notifyOfInvalidation](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-notifyofinvalidation)**(const [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) & msg)<br>Tell the functor that it invalidated the current point in model space, pass a message explaining why, and throw an exception.  |
| virtual double | **[getInvalidationRate](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-getinvalidationrate)**()<br>Getter for invalidation rate.  |
| virtual void | **[setFadeRate](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-setfaderate)**(double new_rate)<br>Setter for the fade rate.  |
| virtual void | **[setTimingPrintRequirement](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-settimingprintrequirement)**(bool flag)<br>Setter for indicating if the timing data for this function's execution should be printed.  |
| virtual bool | **[requiresTimingPrinting](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-requirestimingprinting)**() const<br>Getter indicating if the timing data for this function's execution should be printed.  |
| bool | **[getActiveModelFlag](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-getactivemodelflag)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) model)<br>Indicate whether or not a known model is activated or not.  |
| [safe_ptr](/documentation/code/classes/classgambit_1_1safe__ptr/)< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) > | **[getChosenReqFromGroup](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-getchosenreqfromgroup)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) group)<br>Return a safe pointer to a string indicating which backend requirement has been activated for a given backend group.  |
| virtual void | **[iterate](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-iterate)**(long long iteration)<br>Execute a single iteration in the loop managed by this functor.  |
| virtual void | **[init_myCurrentIteration_if_NULL](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-init-mycurrentiteration-if-null)**()<br>Initialise the array holding the current iteration(s) of this functor.  |
| virtual void | **[setIteration](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-setiteration)**(long long iteration)<br>Setter for setting the iteration number in the loop in which this functor runs.  |
| virtual [omp_safe_ptr](/documentation/code/classes/classgambit_1_1omp__safe__ptr/)< long long > | **[iterationPtr](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-iterationptr)**()<br>Return a safe pointer to the iteration number in the loop in which this functor runs.  |
| virtual void | **[setCanBeLoopManager](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-setcanbeloopmanager)**(bool canManage)<br>Setter for specifying whether this is permitted to be a manager functor, which runs other functors nested in a loop.  |
| virtual bool | **[canBeLoopManager](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-canbeloopmanager)**()<br>Getter for revealing whether this is permitted to be a manager functor.  |
| virtual void | **[setLoopManagerCapType](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-setloopmanagercaptype)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) cap, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) t)<br>Setter for specifying the capability required of a manager functor, if it is to run this functor nested in a loop.  |
| virtual [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[loopManagerCapability](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-loopmanagercapability)**()<br>Getter for revealing the required capability of the wrapped function's loop manager.  |
| virtual [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[loopManagerType](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-loopmanagertype)**()<br>Getter for revealing the required type of the wrapped function's loop manager.  |
| virtual [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[loopManagerName](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-loopmanagername)**()<br>Getter for revealing the name of the wrapped function's assigned loop manager.  |
| virtual [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[loopManagerOrigin](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-loopmanagerorigin)**()<br>Getter for revealing the module of the wrapped function's assigned loop manager.  |
| virtual void | **[breakLoopFromManagedFunctor](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-breakloopfrommanagedfunctor)**()<br>Tell the manager of the loop in which this functor runs that it is time to break the loop.  |
| virtual [safe_ptr](/documentation/code/classes/classgambit_1_1safe__ptr/)< bool > | **[loopIsDone](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-loopisdone)**()<br>Return a safe pointer to the flag indicating that a loop managed by this functor should break now.  |
| virtual void | **[resetLoop](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-resetloop)**()<br>Provide a way to reset the flag indicating that a loop managed by this functor should break.  |
| virtual void | **[breakLoop](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-breakloop)**()<br>Tell the functor that the loop it manages should break now.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-gambit-sspair) > | **[dependencies](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-dependencies)**()<br>Getter for listing currently activated dependencies.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-gambit-sspair) > | **[backendclassloading](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-backendclassloading)**()<br>Getter for listing backends that require class loading.  |
| virtual std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) > | **[backendgroups](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-backendgroups)**()<br>Getter for listing backend requirement groups.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-gambit-sspair) > | **[backendreqs](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-backendreqs)**()<br>Getter for listing all backend requirements.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-gambit-sspair) > | **[backendreqs](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-backendreqs)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) group)<br>Getter for listing backend requirements from a specific group.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-gambit-sspair) > | **[backendspermitted](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-backendspermitted)**([sspair](/documentation/code/namespaces/namespacegambit/#typedef-gambit-sspair) quant)<br>Getter for listing permitted backends.  |
| virtual std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) > | **[backendreq_tags](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-backendreq-tags)**([sspair](/documentation/code/namespaces/namespacegambit/#typedef-gambit-sspair) quant)<br>Getter for listing tags associated with backend requirements.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-gambit-sspair) > | **[forcematchingbackend](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-forcematchingbackend)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) tag)<br>Getter for listing backend requirements that must be resolved from the same backend.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-gambit-sspair) > | **[backend_conditional_dependencies](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-backend-conditional-dependencies)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) req, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) type, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) be, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) ver)<br>Getter for listing backend-specific conditional dependencies (4-string version)  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-gambit-sspair) > | **[backend_conditional_dependencies](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-backend-conditional-dependencies)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) req, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) type, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) be)<br>Getter for backend-specific conditional dependencies (3-string version)  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-gambit-sspair) > | **[backend_conditional_dependencies](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-backend-conditional-dependencies)**([functor](/documentation/code/classes/classgambit_1_1functor/) * be_functor)<br>Getter for backend-specific conditional dependencies (backend functor pointer version)  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-gambit-sspair) > | **[model_conditional_dependencies](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-model-conditional-dependencies)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) model)<br>Getter for listing model-specific conditional dependencies.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-gambit-sspair) > | **[model_conditional_backend_reqs](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-model-conditional-backend-reqs)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) model)<br>Getter for listing model-specific conditional backend requirements.  |
| void | **[setDependency](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-setdependency)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) dep, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) dep_type, void(*)([functor](/documentation/code/classes/classgambit_1_1functor/) *, [module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/) *) resolver, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) purpose ="")<br>Add and activate unconditional dependencies.  |
| void | **[setConditionalDependency](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-setconditionaldependency)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) dep, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) dep_type)<br>Add conditional dependency-type pairs in advance of later conditions.  |
| void | **[setBackendConditionalDependency](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-setbackendconditionaldependency)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) req, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) be, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) ver, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) dep, void(*)([functor](/documentation/code/classes/classgambit_1_1functor/) *, [module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/) *) resolver)<br>Add a backend conditional dependency for multiple backend versions.  |
| void | **[setBackendConditionalDependencySingular](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-setbackendconditionaldependencysingular)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) req, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) be, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) ver, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) dep, void(*)([functor](/documentation/code/classes/classgambit_1_1functor/) *, [module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/) *) resolver)<br>Add a backend conditional dependency for a single backend version.  |
| void | **[setModelConditionalDependency](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-setmodelconditionaldependency)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) model, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) dep, void(*)([functor](/documentation/code/classes/classgambit_1_1functor/) *, [module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/) *) resolver)<br>Add a model conditional dependency for multiple models.  |
| void | **[setModelConditionalDependencySingular](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-setmodelconditionaldependencysingular)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) model, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) dep, void(*)([functor](/documentation/code/classes/classgambit_1_1functor/) *, [module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/) *) resolver)<br>Add a model conditional dependency for a single model.  |
| void | **[makeBackendRuleForModel](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-makebackendruleformodel)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) model, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) tag)<br>Add a rule for activating backend requirements according to the model being scanned.  |
| void | **[setBackendReq](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-setbackendreq)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) group, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) req, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) tags, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) type, void(*)([functor](/documentation/code/classes/classgambit_1_1functor/) *) resolver) |
| void | **[setModelConditionalBackendReq](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-setmodelconditionalbackendreq)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) model, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) req, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) type)<br>Add a model conditional backend requirement for multiple models.  |
| void | **[setModelConditionalBackendReqSingular](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-setmodelconditionalbackendreqsingular)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) model, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) req, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) type)<br>Add a model conditional backend requirement for a single model.  |
| void | **[makeBackendOptionRule](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-makebackendoptionrule)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) be_and_ver, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) tag)<br>Add a rule for dictating which backends can be used to fulfill which backend requirements.  |
| void | **[setPermittedBackend](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-setpermittedbackend)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) req, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) be, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) ver)<br>Add a single permitted backend version.  |
| void | **[makeBackendMatchingRule](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-makebackendmatchingrule)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) tag)<br>Add one or more rules for forcing backends reqs with the same tags to always be resolved from the same backend.  |
| void | **[setRequiredClassloader](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-setrequiredclassloader)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) be, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) ver, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) safe_ver)<br>Add a rule indicating that classes from a given backend must be available.  |
| virtual void | **[notifyOfBackends](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-notifyofbackends)**(std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str), std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) > > be_ver_map)<br>Indicate to the functor which backends are actually loaded and working.  |
| virtual void | **[setNestedList](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-setnestedlist)**(std::vector< [functor](/documentation/code/classes/classgambit_1_1functor/) * > & newNestedList)<br>Set the ordered list of pointers to other functors that should run nested in a loop managed by this one.  |
| virtual void | **[resolveDependency](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-resolvedependency)**([functor](/documentation/code/classes/classgambit_1_1functor/) * dep_functor)<br>Resolve a dependency using a pointer to another functor object.  |
| virtual void | **[resolveLoopManager](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-resolveloopmanager)**([functor](/documentation/code/classes/classgambit_1_1functor/) * dep_functor)<br>Set this functor's loop manager (if it has one)  |
| virtual void | **[resolveBackendReq](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-resolvebackendreq)**([functor](/documentation/code/classes/classgambit_1_1functor/) * be_functor)<br>Resolve a backend requirement using a pointer to another functor object.  |
| virtual void | **[notifyOfModel](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-notifyofmodel)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) model)<br>Notify the functor that a certain model is being scanned, so that it can activate its dependencies and backend reqs accordingly.  |
| virtual void | **[notifyOfDependee](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-notifyofdependee)**([functor](/documentation/code/classes/classgambit_1_1functor/) * dependent_functor)<br>Notify the functor that another functor depends on it.  |
| virtual [invalid_point_exception](/documentation/code/classes/classgambit_1_1invalid__point__exception/) * | **[retrieve_invalid_point_exception](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-retrieve-invalid-point-exception)**()<br>Retrieve the previously saved exception generated when this functor invalidated the current point in model space.  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| virtual void | **[reset](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-reset)**(int thread_num)<br>Reset functor for one thread only.  |
| virtual void | **[acknowledgeInvalidation](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-acknowledgeinvalidation)**([invalid_point_exception](/documentation/code/classes/classgambit_1_1invalid__point__exception/) & e, [functor](/documentation/code/classes/classgambit_1_1functor/) * f =NULL)<br>Acknowledge that this functor invalidated the current point in model space.  |
| virtual void | **[startTiming](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-starttiming)**(int thread_num)<br>Do pre-calculate timing things.  |
| virtual void | **[finishTiming](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-finishtiming)**(int thread_num)<br>Do post-calculate timing things.  |
| virtual void | **[init_memory](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-init-memory)**()<br>Initialise the memory of this functor.  |
| void | **[fill_activeModelFlags](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-fill-activemodelflags)**()<br>Construct the list of known models only if it doesn't yet exist.  |
| [sspair](/documentation/code/namespaces/namespacegambit/#typedef-gambit-sspair) | **[retrieve_conditional_dep_type_pair](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-retrieve-conditional-dep-type-pair)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) dep)<br>Retrieve full conditional dependency-type pair from conditional dependency only.  |
| void | **[check_missing_LogTag](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-check-missing-logtag)**()<br>Check if an appropriate LogTag for this functor is missing from the logging system.  |
| void | **[entering_multithreaded_region](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-entering-multithreaded-region)**() |
| void | **[leaving_multithreaded_region](/documentation/code/classes/classgambit_1_1module__functor__common/#function-gambitmodule-functor-common-leaving-multithreaded-region)**() |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| bool | **[myTimingPrintFlag](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-mytimingprintflag)** <br>Flag to select whether or not the timing data for this function's execution should be printed;.  |
| std::chrono::time_point< std::chrono::system_clock > * | **[start](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-start)** <br>Beginning and end timing points.  |
| std::chrono::time_point< std::chrono::system_clock > * | **[end](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-end)**  |
| bool | **[point_exception_raised](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-point-exception-raised)** <br>A flag indicating whether or not this functor has invalidated the current point.  |
| [invalid_point_exception](/documentation/code/classes/classgambit_1_1invalid__point__exception/) | **[raised_point_exception](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-raised-point-exception)** <br>An exception raised because this functor has invalidated the current point.  |
| double | **[runtime_average](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-runtime-average)** <br>Averaged runtime in ns.  |
| double | **[fadeRate](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-faderate)** <br>Fade rate for average runtime.  |
| double | **[pInvalidation](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-pinvalidation)** <br>Probability that functors invalidates point in model parameter space.  |
| bool * | **[needs_recalculating](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-needs-recalculating)** <br>Needs recalculating or not?  |
| bool * | **[already_printed](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-already-printed)** <br>Has result already been sent to the printer?  |
| bool * | **[already_printed_timing](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-already-printed-timing)** <br>Has timing data already been sent to the printer?  |
| bool | **[iCanManageLoops](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-icanmanageloops)** <br>Flag indicating whether this function can manage a loop over other functions.  |
| bool | **[myLoopIsDone](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-myloopisdone)** <br>Flag indicating whether this function is ready to finish its loop (only relevant if iCanManageLoops = true)  |
| bool | **[iRunNested](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-irunnested)** <br>Flag indicating whether this function can run nested in a loop over functions.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[myLoopManagerCapability](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-myloopmanagercapability)** <br>Capability of a function that mangages a loop that this function can run inside of.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[myLoopManagerType](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-myloopmanagertype)** <br>Capability of a function that mangages a loop that this function can run inside of.  |
| [functor](/documentation/code/classes/classgambit_1_1functor/) * | **[myLoopManager](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-myloopmanager)** <br>Pointer to the functor that mangages the loop that this function runs inside of.  |
| std::vector< [functor](/documentation/code/classes/classgambit_1_1functor/) * > | **[myNestedFunctorList](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-mynestedfunctorlist)** <br>Vector of functors that have been set up to run nested within this one.  |
| long long * | **[myCurrentIteration](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-mycurrentiteration)** <br>Pointer to counters for iterations of nested functor loop.  |
| const int | **[globlMaxThreads](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-globlmaxthreads)** <br>Maximum number of OpenMP threads this MPI process is permitted to launch in total.  |
| std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) > | **[myGroups](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-mygroups)** <br>Internal list of backend groups that this functor's requirements fall into.  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str), [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) > | **[chosenReqsFromGroups](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-chosenreqsfromgroups)** <br>Map from groups to backend reqs, indicating which backend req has been activated for which backend group.  |
| std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-gambit-sspair) > | **[myBackendReqs](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-mybackendreqs)** <br>Set of all backend requirement-type string pairs.  |
| std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-gambit-sspair) > | **[myResolvableBackendReqs](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-myresolvablebackendreqs)** <br>Set of all backend requirement-type string pairs currently available for resolution.  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str), std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-gambit-sspair) > > | **[myGroupedBackendReqs](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-mygroupedbackendreqs)** <br>Set of backend requirement-type string pairs for specific backend groups.  |
| std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-gambit-sspair) > | **[myDependencies](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-mydependencies)** <br>Vector of dependency-type string pairs.  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str), [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) > | **[myConditionalDependencies](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-myconditionaldependencies)** <br>Map of conditional dependencies to their types.  |
| std::map< std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) >, std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-gambit-sspair) > > | **[myBackendConditionalDependencies](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-mybackendconditionaldependencies)** <br>Map from (vector with 4 strings: backend req, type, backend, version) to (set of {conditional dependency-type} pairs)  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str), std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-gambit-sspair) > > | **[myModelConditionalDependencies](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-mymodelconditionaldependencies)** <br>Map from models to (set of {conditional dependency-type} pairs)  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str), std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-gambit-sspair) > > | **[myModelConditionalBackendReqs](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-mymodelconditionalbackendreqs)** <br>Map from models to (set of {conditional backend requirement-type} pairs)  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str), bool > | **[activeModelFlags](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-activemodelflags)** <br>Map from known models to flags indicating if they are activated or not (known = allowed, in allowed groups or conditions for conditional dependencies)  |
| std::map< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-gambit-sspair), void(*)([functor](/documentation/code/classes/classgambit_1_1functor/) *, [module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/) *)> | **[dependency_map](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-dependency-map)**  |
| std::map< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-gambit-sspair), [functor](/documentation/code/classes/classgambit_1_1functor/) * > | **[dependency_functor_map](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-dependency-functor-map)**  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str), [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) > | **[backendreq_types](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-backendreq-types)** <br>Map from backend requirements to their required types.  |
| std::map< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-gambit-sspair), [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) > | **[backendreq_groups](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-backendreq-groups)** <br>Map from backend requirements to their designated groups.  |
| std::map< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-gambit-sspair), std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) > > | **[backendreq_tagmap](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-backendreq-tagmap)** <br>Map from backend requirements to their rule tags.  |
| std::map< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-gambit-sspair), void(*)([functor](/documentation/code/classes/classgambit_1_1functor/) *)> | **[backendreq_map](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-backendreq-map)**  |
| std::map< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-gambit-sspair), std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-gambit-sspair) > > | **[permitted_map](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-permitted-map)** <br>Map from (backend requirement-type pairs) to (set of permitted {backend-version} pairs)  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str), std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-gambit-sspair) > > | **[myForcedMatches](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-myforcedmatches)** <br>Map from tags to sets of matching (backend requirement-type pairs) that are forced to use the same backend.  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str), std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) > > | **[required_classloading_backends](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-required-classloading-backends)** <br>Map from required classloading backends to their versions.  |
| std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) > | **[missing_backends](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-missing-backends)** <br>Vector of required backends currently missing.  |
| timespec | **[tp](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-tp)** <br>Internal timespec object.  |
| int | **[myLogTag](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-mylogtag)** <br>Integer LogTag, for tagging log messages.  |
| bool | **[signal_mode_locked](/documentation/code/classes/classgambit_1_1module__functor__common/#variable-gambitmodule-functor-common-signal-mode-locked)**  |

## Friends

|                | Name           |
| -------------- | -------------- |
| void | **[FunctorHelp::entering_multithreaded_region](/documentation/code/classes/classgambit_1_1module__functor__common/#friend-gambitmodule-functor-common-functorhelpentering-multithreaded-region)**([module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/) & ) <br>Connectors to external helper functions (to decouple signal handling from this class)  |
| void | **[FunctorHelp::leaving_multithreaded_region](/documentation/code/classes/classgambit_1_1module__functor__common/#friend-gambitmodule-functor-common-functorhelpleaving-multithreaded-region)**([module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/) & )  |

## Additional inherited members

**Public Functions inherited from [Gambit::functor](/documentation/code/classes/classgambit_1_1functor/)**

|                | Name           |
| -------------- | -------------- |
| | **[functor](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-functor)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) func_name, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) func_capability, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) result_type, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) origin_name, [Models::ModelFunctorClaw](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/) & claw)<br>Constructor.  |
| virtual | **[~functor](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-functor)**() |
| virtual void | **[calculate](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-calculate)**()<br>Virtual [calculate()](); needs to be redefined in daughters.  |
| virtual void | **[reset_and_calculate](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-reset-and-calculate)**()<br>Reset-then-recalculate method.  |
| void | **[setStatus](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-setstatus)**(int stat) |
| virtual void | **[setInUse](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-setinuse)**(bool )<br>Set the inUse flag (must be overridden in derived class to have any effect).  |
| void | **[setPurpose](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-setpurpose)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) purpose)<br>Setter for purpose (relevant only for next-to-output functors)  |
| void | **[setVertexID](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-setvertexid)**(int ID)<br>Setter for vertex ID (used in printer system)  |
| void | **[setTimingVertexID](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-settimingvertexid)**(int ID)<br>Set ID for timing 'vertex' (used in printer system)  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[name](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-name)**() const<br>Getter for the wrapped function's name.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[capability](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-capability)**() const<br>Getter for the wrapped function's reported capability.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[type](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-type)**() const<br>Getter for the wrapped function's reported return type.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[origin](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-origin)**() const<br>Getter for the wrapped function's origin (module or backend name)  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[version](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-version)**() const<br>Getter for the version of the wrapped function's origin (module or backend)  |
| virtual [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[safe_version](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-safe-version)**() const<br>Getter for the 'safe' incarnation of the version of the wrapped function's origin (module or backend)  |
| int | **[status](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-status)**() const |
| [sspair](/documentation/code/namespaces/namespacegambit/#typedef-gambit-sspair) | **[quantity](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-quantity)**() const<br>Getter for the overall quantity provided by the wrapped function (capability-type pair)  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[purpose](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-purpose)**() const<br>Getter for purpose (relevant for output nodes, aka helper structures for the dep. resolution)  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[citationKey](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-citationkey)**() const<br>Getter for the citation key.  |
| int | **[vertexID](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-vertexid)**() const<br>Getter for vertex ID.  |
| int | **[timingVertexID](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-timingvertexid)**() const<br>Getter for timing vertex ID.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[label](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-label)**() const<br>Getter for string label.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[timingLabel](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-timinglabel)**() const<br>Getter for the printer timing label.  |
| virtual bool | **[requiresPrinting](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-requiresprinting)**() const<br>Getter indicating if the wrapped function's result should to be printed.  |
| virtual void | **[setPrintRequirement](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-setprintrequirement)**(bool flag)<br>Setter for indicating if the wrapped function's result should to be printed.  |
| virtual void | **[print](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-print)**([Printers::BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/) * printer, const int pointID, int thread_num)<br>Printer function.  |
| virtual void | **[print](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-print)**([Printers::BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/) * printer, const int pointID)<br>Printer function (no-thread-index short-circuit)  |
| void | **[notifyOfIniOptions](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-notifyofinioptions)**(const [Options](/documentation/code/classes/classgambit_1_1options/) & opt) |
| template <typename TYPE \> <br>void | **[setOption](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-setoption)**(const [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) & key, const TYPE val)<br>Set an option for the functor directly (for use in standalone executables).  |
| [safe_ptr](/documentation/code/classes/classgambit_1_1safe__ptr/)< [Options](/documentation/code/classes/classgambit_1_1options/) > | **[getOptions](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-getoptions)**()<br>Return a safe pointer to the options that this functor is supposed to run with (e.g. from the ini file).  |
| void | **[notifyOfSubCaps](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-notifyofsubcaps)**(const [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) & subcap_string)<br>Notify the functor about a string in [YAML](/documentation/code/namespaces/namespaceyaml/) that contains the sub-capability information (for use in standalones)  |
| void | **[notifyOfSubCaps](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-notifyofsubcaps)**(const [Options](/documentation/code/classes/classgambit_1_1options/) & subcaps)<br>Notify the functor about an instance of the options class that contains sub-capability information.  |
| template <typename TYPE \> <br>void | **[setSubCap](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-setsubcap)**(const [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) & key, const TYPE val)<br>Set a sub-capability (subcap)for the functor directly (for use in standalone executables).  |
| [safe_ptr](/documentation/code/classes/classgambit_1_1safe__ptr/)< [Options](/documentation/code/classes/classgambit_1_1options/) > | **[getSubCaps](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-getsubcaps)**()<br>Return a safe pointer to the subcaps that this functor realises it is supposed to facilitate downstream calculation of.  |
| [safe_ptr](/documentation/code/classes/classgambit_1_1safe__ptr/)< std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-gambit-sspair) > > | **[getDependees](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-getdependees)**()<br>Return a safe pointer to the vector of all capability,type pairs of functors arranged downstream of this one in the dependency tree.  |
| bool | **[allModelsAllowed](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-allmodelsallowed)**()<br>Test whether the functor is allowed to be used with all models.  |
| bool | **[modelAllowed](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-modelallowed)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) model)<br>Test whether the functor is always allowed (either explicitly or implicitly) to be used with a given model.  |
| bool | **[modelExplicitlyAllowed](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-modelexplicitlyallowed)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) model)<br>Test whether the functor is explictly always allowed to be used with a given model.  |
| void | **[setAllowedModel](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-setallowedmodel)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) model)<br>Add a model to the internal list of models for which this functor is allowed to be used.  |
| bool | **[modelComboAllowed](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-modelcomboallowed)**(std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) > combo)<br>Test whether the functor is allowed (either explicitly or implicitly) to be used with a given combination of models.  |
| bool | **[modelComboExplicitlyAllowed](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-modelcomboexplicitlyallowed)**(std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) > combo)<br>Test whether the functor has been explictly allowed to be used with a given combination of models.  |
| void | **[setModelGroup](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-setmodelgroup)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) group, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) contents)<br>Add a model group definition to the internal list of model groups.  |
| void | **[setAllowedModelGroupCombo](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-setallowedmodelgroupcombo)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) groups)<br>Add a combination of model groups to the internal list of combinations for which this functor is allowed to be used.  |

**Protected Functions inherited from [Gambit::functor](/documentation/code/classes/classgambit_1_1functor/)**

|                | Name           |
| -------------- | -------------- |
| void | **[failBigTime](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-failbigtime)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) method)<br>Attempt to retrieve a dependency or model parameter that has not been resolved.  |
| bool | **[allowed_parent_or_friend_exists](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-allowed-parent-or-friend-exists)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) model)<br>Test if there is a model in the functor's allowedModels list as which this model can be interpreted.  |
| bool | **[in_allowed_combo](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-in-allowed-combo)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) model)<br>Check that a model is actually part of a combination that is allowed to be used with this functor.  |
| bool | **[contains_anything_interpretable_as_member_of](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-contains-anything-interpretable-as-member-of)**(std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) > combo, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) group)<br>Test whether any of the entries in a given model group is a valid interpretation of any members in a given combination.  |
| bool | **[has_common_elements](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-has-common-elements)**(std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) > combo, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) group)<br>Work out whether a given combination of models and a model group have any elements in common.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[find_friend_or_parent_model_in_map](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-find-friend-or-parent-model-in-map)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) model, std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str), std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-gambit-sspair) > > karta)<br>Try to find a parent or friend model in some user-supplied map from models to sspair vectors.  |

**Protected Attributes inherited from [Gambit::functor](/documentation/code/classes/classgambit_1_1functor/)**

|                | Name           |
| -------------- | -------------- |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[myName](/documentation/code/classes/classgambit_1_1functor/#variable-gambitfunctor-myname)** <br>Internal storage of the function name.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[myCapability](/documentation/code/classes/classgambit_1_1functor/#variable-gambitfunctor-mycapability)** <br>Internal storage of exactly what the function calculates.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[myType](/documentation/code/classes/classgambit_1_1functor/#variable-gambitfunctor-mytype)** <br>Internal storage of the type of what the function calculates.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[myOrigin](/documentation/code/classes/classgambit_1_1functor/#variable-gambitfunctor-myorigin)** <br>Internal storage of the name of the module or backend to which the function belongs.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[myVersion](/documentation/code/classes/classgambit_1_1functor/#variable-gambitfunctor-myversion)** <br>Internal storage of the version of the module or backend to which the function belongs.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[myPurpose](/documentation/code/classes/classgambit_1_1functor/#variable-gambitfunctor-mypurpose)** <br>Purpose of the function (relevant for output and next-to-output functors)  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[myCitationKey](/documentation/code/classes/classgambit_1_1functor/#variable-gambitfunctor-mycitationkey)** <br>Citation key: BibTex key of the reference.  |
| const [Models::ModelFunctorClaw](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/) * | **[myClaw](/documentation/code/classes/classgambit_1_1functor/#variable-gambitfunctor-myclaw)** <br>Bound model functor claw, for checking relationships between models.  |
| const [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[myLabel](/documentation/code/classes/classgambit_1_1functor/#variable-gambitfunctor-mylabel)** <br>String label, used to label functor results for printer system.  |
| const [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[myTimingLabel](/documentation/code/classes/classgambit_1_1functor/#variable-gambitfunctor-mytiminglabel)** <br>String label, used to label functor timing data for printer system.  |
| int | **[myStatus](/documentation/code/classes/classgambit_1_1functor/#variable-gambitfunctor-mystatus)**  |
| int | **[myVertexID](/documentation/code/classes/classgambit_1_1functor/#variable-gambitfunctor-myvertexid)** <br>Internal storage of the vertex ID number used by the printer system to identify functors.  |
| int | **[myTimingVertexID](/documentation/code/classes/classgambit_1_1functor/#variable-gambitfunctor-mytimingvertexid)** <br>ID assigned by printers to the timing data output stream.  |
| bool | **[verbose](/documentation/code/classes/classgambit_1_1functor/#variable-gambitfunctor-verbose)** <br>Debug flag.  |
| [Options](/documentation/code/classes/classgambit_1_1options/) | **[myOptions](/documentation/code/classes/classgambit_1_1functor/#variable-gambitfunctor-myoptions)** <br>Internal storage of function options, as a [YAML](/documentation/code/namespaces/namespaceyaml/) node.  |
| [Options](/documentation/code/classes/classgambit_1_1options/) | **[mySubCaps](/documentation/code/classes/classgambit_1_1functor/#variable-gambitfunctor-mysubcaps)** <br>Internal storage of function sub-capabilities, as a [YAML](/documentation/code/namespaces/namespaceyaml/) node.  |
| std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-gambit-sspair) > | **[myDependees](/documentation/code/classes/classgambit_1_1functor/#variable-gambitfunctor-mydependees)** <br>List of all capability,type pairs of functors downstream of this one in the dependency tree.  |
| std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) > | **[allowedModels](/documentation/code/classes/classgambit_1_1functor/#variable-gambitfunctor-allowedmodels)** <br>List of allowed models.  |
| std::set< std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) > > | **[allowedGroupCombos](/documentation/code/classes/classgambit_1_1functor/#variable-gambitfunctor-allowedgroupcombos)** <br>List of allowed model group combinations.  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str), std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) > > | **[modelGroups](/documentation/code/classes/classgambit_1_1functor/#variable-gambitfunctor-modelgroups)** <br>Map from model group names to group contents.  |


## Public Functions Documentation

### function module_functor_common

```
module_functor_common(
    str func_name,
    str func_capability,
    str result_type,
    str origin_name,
    Models::ModelFunctorClaw & claw
)
```

Constructor. 

### function ~module_functor_common

```
virtual ~module_functor_common()
```

Destructor. 

### function getRuntimeAverage

```
virtual double getRuntimeAverage()
```

Getter for averaged runtime. 

**Reimplements**: [Gambit::functor::getRuntimeAverage](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-getruntimeaverage)


### function reset

```
virtual void reset()
```

Reset functor. 

**Reimplements**: [Gambit::functor::reset](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-reset)


Reset functor for all threads. 


### function notifyOfInvalidation

```
virtual void notifyOfInvalidation(
    const str & msg
)
```

Tell the functor that it invalidated the current point in model space, pass a message explaining why, and throw an exception. 

**Reimplements**: [Gambit::functor::notifyOfInvalidation](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-notifyofinvalidation)


### function getInvalidationRate

```
virtual double getInvalidationRate()
```

Getter for invalidation rate. 

**Reimplements**: [Gambit::functor::getInvalidationRate](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-getinvalidationrate)


### function setFadeRate

```
virtual void setFadeRate(
    double new_rate
)
```

Setter for the fade rate. 

**Reimplements**: [Gambit::functor::setFadeRate](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-setfaderate)


### function setTimingPrintRequirement

```
virtual void setTimingPrintRequirement(
    bool flag
)
```

Setter for indicating if the timing data for this function's execution should be printed. 

**Reimplements**: [Gambit::functor::setTimingPrintRequirement](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-settimingprintrequirement)


### function requiresTimingPrinting

```
virtual bool requiresTimingPrinting() const
```

Getter indicating if the timing data for this function's execution should be printed. 

**Reimplements**: [Gambit::functor::requiresTimingPrinting](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-requirestimingprinting)


### function getActiveModelFlag

```
bool getActiveModelFlag(
    str model
)
```

Indicate whether or not a known model is activated or not. 

### function getChosenReqFromGroup

```
safe_ptr< str > getChosenReqFromGroup(
    str group
)
```

Return a safe pointer to a string indicating which backend requirement has been activated for a given backend group. 

### function iterate

```
virtual void iterate(
    long long iteration
)
```

Execute a single iteration in the loop managed by this functor. 

### function init_myCurrentIteration_if_NULL

```
virtual void init_myCurrentIteration_if_NULL()
```

Initialise the array holding the current iteration(s) of this functor. 

### function setIteration

```
virtual void setIteration(
    long long iteration
)
```

Setter for setting the iteration number in the loop in which this functor runs. 

**Reimplements**: [Gambit::functor::setIteration](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-setiteration)


### function iterationPtr

```
virtual omp_safe_ptr< long long > iterationPtr()
```

Return a safe pointer to the iteration number in the loop in which this functor runs. 

### function setCanBeLoopManager

```
virtual void setCanBeLoopManager(
    bool canManage
)
```

Setter for specifying whether this is permitted to be a manager functor, which runs other functors nested in a loop. 

### function canBeLoopManager

```
virtual bool canBeLoopManager()
```

Getter for revealing whether this is permitted to be a manager functor. 

**Reimplements**: [Gambit::functor::canBeLoopManager](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-canbeloopmanager)


### function setLoopManagerCapType

```
virtual void setLoopManagerCapType(
    str cap,
    str t
)
```

Setter for specifying the capability required of a manager functor, if it is to run this functor nested in a loop. 

Setter for specifying the capability and type required of a manager functor, if it is to run this functor nested in a loop. 


### function loopManagerCapability

```
virtual str loopManagerCapability()
```

Getter for revealing the required capability of the wrapped function's loop manager. 

**Reimplements**: [Gambit::functor::loopManagerCapability](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-loopmanagercapability)


### function loopManagerType

```
virtual str loopManagerType()
```

Getter for revealing the required type of the wrapped function's loop manager. 

**Reimplements**: [Gambit::functor::loopManagerType](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-loopmanagertype)


### function loopManagerName

```
virtual str loopManagerName()
```

Getter for revealing the name of the wrapped function's assigned loop manager. 

**Reimplements**: [Gambit::functor::loopManagerName](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-loopmanagername)


### function loopManagerOrigin

```
virtual str loopManagerOrigin()
```

Getter for revealing the module of the wrapped function's assigned loop manager. 

**Reimplements**: [Gambit::functor::loopManagerOrigin](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-loopmanagerorigin)


### function breakLoopFromManagedFunctor

```
virtual void breakLoopFromManagedFunctor()
```

Tell the manager of the loop in which this functor runs that it is time to break the loop. 

### function loopIsDone

```
virtual safe_ptr< bool > loopIsDone()
```

Return a safe pointer to the flag indicating that a loop managed by this functor should break now. 

### function resetLoop

```
virtual void resetLoop()
```

Provide a way to reset the flag indicating that a loop managed by this functor should break. 

### function breakLoop

```
virtual void breakLoop()
```

Tell the functor that the loop it manages should break now. 

**Reimplements**: [Gambit::functor::breakLoop](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-breakloop)


### function dependencies

```
virtual std::set< sspair > dependencies()
```

Getter for listing currently activated dependencies. 

**Reimplements**: [Gambit::functor::dependencies](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-dependencies)


### function backendclassloading

```
virtual std::set< sspair > backendclassloading()
```

Getter for listing backends that require class loading. 

**Reimplements**: [Gambit::functor::backendclassloading](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-backendclassloading)


### function backendgroups

```
virtual std::set< str > backendgroups()
```

Getter for listing backend requirement groups. 

**Reimplements**: [Gambit::functor::backendgroups](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-backendgroups)


### function backendreqs

```
virtual std::set< sspair > backendreqs()
```

Getter for listing all backend requirements. 

**Reimplements**: [Gambit::functor::backendreqs](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-backendreqs)


### function backendreqs

```
virtual std::set< sspair > backendreqs(
    str group
)
```

Getter for listing backend requirements from a specific group. 

**Reimplements**: [Gambit::functor::backendreqs](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-backendreqs)


### function backendspermitted

```
virtual std::set< sspair > backendspermitted(
    sspair quant
)
```

Getter for listing permitted backends. 

**Reimplements**: [Gambit::functor::backendspermitted](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-backendspermitted)


### function backendreq_tags

```
virtual std::set< str > backendreq_tags(
    sspair quant
)
```

Getter for listing tags associated with backend requirements. 

**Reimplements**: [Gambit::functor::backendreq_tags](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-backendreq-tags)


### function forcematchingbackend

```
virtual std::set< sspair > forcematchingbackend(
    str tag
)
```

Getter for listing backend requirements that must be resolved from the same backend. 

**Reimplements**: [Gambit::functor::forcematchingbackend](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-forcematchingbackend)


### function backend_conditional_dependencies

```
virtual std::set< sspair > backend_conditional_dependencies(
    str req,
    str type,
    str be,
    str ver
)
```

Getter for listing backend-specific conditional dependencies (4-string version) 

**Reimplements**: [Gambit::functor::backend_conditional_dependencies](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-backend-conditional-dependencies)


### function backend_conditional_dependencies

```
virtual std::set< sspair > backend_conditional_dependencies(
    str req,
    str type,
    str be
)
```

Getter for backend-specific conditional dependencies (3-string version) 

**Reimplements**: [Gambit::functor::backend_conditional_dependencies](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-backend-conditional-dependencies)


### function backend_conditional_dependencies

```
virtual std::set< sspair > backend_conditional_dependencies(
    functor * be_functor
)
```

Getter for backend-specific conditional dependencies (backend functor pointer version) 

**Reimplements**: [Gambit::functor::backend_conditional_dependencies](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-backend-conditional-dependencies)


### function model_conditional_dependencies

```
virtual std::set< sspair > model_conditional_dependencies(
    str model
)
```

Getter for listing model-specific conditional dependencies. 

**Reimplements**: [Gambit::functor::model_conditional_dependencies](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-model-conditional-dependencies)


### function model_conditional_backend_reqs

```
virtual std::set< sspair > model_conditional_backend_reqs(
    str model
)
```

Getter for listing model-specific conditional backend requirements. 

**Reimplements**: [Gambit::functor::model_conditional_backend_reqs](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-model-conditional-backend-reqs)


### function setDependency

```
void setDependency(
    str dep,
    str dep_type,
    void(*)(functor *, module_functor_common *) resolver,
    str purpose =""
)
```

Add and activate unconditional dependencies. 

### function setConditionalDependency

```
void setConditionalDependency(
    str dep,
    str dep_type
)
```

Add conditional dependency-type pairs in advance of later conditions. 

### function setBackendConditionalDependency

```
void setBackendConditionalDependency(
    str req,
    str be,
    str ver,
    str dep,
    void(*)(functor *, module_functor_common *) resolver
)
```

Add a backend conditional dependency for multiple backend versions. 

### function setBackendConditionalDependencySingular

```
void setBackendConditionalDependencySingular(
    str req,
    str be,
    str ver,
    str dep,
    void(*)(functor *, module_functor_common *) resolver
)
```

Add a backend conditional dependency for a single backend version. 

### function setModelConditionalDependency

```
void setModelConditionalDependency(
    str model,
    str dep,
    void(*)(functor *, module_functor_common *) resolver
)
```

Add a model conditional dependency for multiple models. 

### function setModelConditionalDependencySingular

```
void setModelConditionalDependencySingular(
    str model,
    str dep,
    void(*)(functor *, module_functor_common *) resolver
)
```

Add a model conditional dependency for a single model. 

### function makeBackendRuleForModel

```
void makeBackendRuleForModel(
    str model,
    str tag
)
```

Add a rule for activating backend requirements according to the model being scanned. 

### function setBackendReq

```
void setBackendReq(
    str group,
    str req,
    str tags,
    str type,
    void(*)(functor *) resolver
)
```


Add an unconditional backend requirement The info gets updated later if this turns out to be contitional on a model.

Add an unconditional backend requirement The info gets updated later if this turns out to be conditional on a model. 


### function setModelConditionalBackendReq

```
void setModelConditionalBackendReq(
    str model,
    str req,
    str type
)
```

Add a model conditional backend requirement for multiple models. 

### function setModelConditionalBackendReqSingular

```
void setModelConditionalBackendReqSingular(
    str model,
    str req,
    str type
)
```

Add a model conditional backend requirement for a single model. 

### function makeBackendOptionRule

```
void makeBackendOptionRule(
    str be_and_ver,
    str tag
)
```

Add a rule for dictating which backends can be used to fulfill which backend requirements. 

### function setPermittedBackend

```
void setPermittedBackend(
    str req,
    str be,
    str ver
)
```

Add a single permitted backend version. 

### function makeBackendMatchingRule

```
void makeBackendMatchingRule(
    str tag
)
```

Add one or more rules for forcing backends reqs with the same tags to always be resolved from the same backend. 

Add one or more rules that force backends reqs with the same tag to always be resolved from the same backend. 


### function setRequiredClassloader

```
void setRequiredClassloader(
    str be,
    str ver,
    str safe_ver
)
```

Add a rule indicating that classes from a given backend must be available. 

### function notifyOfBackends

```
virtual void notifyOfBackends(
    std::map< str, std::set< str > > be_ver_map
)
```

Indicate to the functor which backends are actually loaded and working. 

**Reimplements**: [Gambit::functor::notifyOfBackends](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-notifyofbackends)


### function setNestedList

```
virtual void setNestedList(
    std::vector< functor * > & newNestedList
)
```

Set the ordered list of pointers to other functors that should run nested in a loop managed by this one. 

**Reimplements**: [Gambit::functor::setNestedList](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-setnestedlist)


### function resolveDependency

```
virtual void resolveDependency(
    functor * dep_functor
)
```

Resolve a dependency using a pointer to another functor object. 

**Reimplements**: [Gambit::functor::resolveDependency](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-resolvedependency)


### function resolveLoopManager

```
virtual void resolveLoopManager(
    functor * dep_functor
)
```

Set this functor's loop manager (if it has one) 

**Reimplements**: [Gambit::functor::resolveLoopManager](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-resolveloopmanager)


### function resolveBackendReq

```
virtual void resolveBackendReq(
    functor * be_functor
)
```

Resolve a backend requirement using a pointer to another functor object. 

**Reimplements**: [Gambit::functor::resolveBackendReq](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-resolvebackendreq)


### function notifyOfModel

```
virtual void notifyOfModel(
    str model
)
```

Notify the functor that a certain model is being scanned, so that it can activate its dependencies and backend reqs accordingly. 

**Reimplements**: [Gambit::functor::notifyOfModel](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-notifyofmodel)


### function notifyOfDependee

```
virtual void notifyOfDependee(
    functor * dependent_functor
)
```

Notify the functor that another functor depends on it. 

**Reimplements**: [Gambit::functor::notifyOfDependee](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-notifyofdependee)


### function retrieve_invalid_point_exception

```
virtual invalid_point_exception * retrieve_invalid_point_exception()
```

Retrieve the previously saved exception generated when this functor invalidated the current point in model space. 

**Reimplements**: [Gambit::functor::retrieve_invalid_point_exception](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-retrieve-invalid-point-exception)


## Protected Functions Documentation

### function reset

```
virtual void reset(
    int thread_num
)
```

Reset functor for one thread only. 

**Reimplements**: [Gambit::functor::reset](/documentation/code/classes/classgambit_1_1functor/#function-gambitfunctor-reset)


### function acknowledgeInvalidation

```
virtual void acknowledgeInvalidation(
    invalid_point_exception & e,
    functor * f =NULL
)
```

Acknowledge that this functor invalidated the current point in model space. 

### function startTiming

```
virtual void startTiming(
    int thread_num
)
```

Do pre-calculate timing things. 

### function finishTiming

```
virtual void finishTiming(
    int thread_num
)
```

Do post-calculate timing things. 

### function init_memory

```
virtual void init_memory()
```

Initialise the memory of this functor. 

**Reimplemented by**: [Gambit::module_functor::init_memory](/documentation/code/classes/classgambit_1_1module__functor/#function-gambitmodule-functor-init-memory), [Gambit::module_functor::init_memory](/documentation/code/classes/classgambit_1_1module__functor/#function-gambitmodule-functor-init-memory)


### function fill_activeModelFlags

```
void fill_activeModelFlags()
```

Construct the list of known models only if it doesn't yet exist. 

### function retrieve_conditional_dep_type_pair

```
sspair retrieve_conditional_dep_type_pair(
    str dep
)
```

Retrieve full conditional dependency-type pair from conditional dependency only. 

### function check_missing_LogTag

```
void check_missing_LogTag()
```

Check if an appropriate LogTag for this functor is missing from the logging system. 

### function entering_multithreaded_region

```
inline void entering_multithreaded_region()
```


### function leaving_multithreaded_region

```
inline void leaving_multithreaded_region()
```


## Protected Attributes Documentation

### variable myTimingPrintFlag

```
bool myTimingPrintFlag;
```

Flag to select whether or not the timing data for this function's execution should be printed;. 

### variable start

```
std::chrono::time_point< std::chrono::system_clock > * start;
```

Beginning and end timing points. 

### variable end

```
std::chrono::time_point< std::chrono::system_clock > * end;
```


### variable point_exception_raised

```
bool point_exception_raised;
```

A flag indicating whether or not this functor has invalidated the current point. 

### variable raised_point_exception

```
invalid_point_exception raised_point_exception;
```

An exception raised because this functor has invalidated the current point. 

### variable runtime_average

```
double runtime_average;
```

Averaged runtime in ns. 

### variable fadeRate

```
double fadeRate;
```

Fade rate for average runtime. 

### variable pInvalidation

```
double pInvalidation;
```

Probability that functors invalidates point in model parameter space. 

### variable needs_recalculating

```
bool * needs_recalculating;
```

Needs recalculating or not? 

### variable already_printed

```
bool * already_printed;
```

Has result already been sent to the printer? 

### variable already_printed_timing

```
bool * already_printed_timing;
```

Has timing data already been sent to the printer? 

### variable iCanManageLoops

```
bool iCanManageLoops;
```

Flag indicating whether this function can manage a loop over other functions. 

### variable myLoopIsDone

```
bool myLoopIsDone;
```

Flag indicating whether this function is ready to finish its loop (only relevant if iCanManageLoops = true) 

### variable iRunNested

```
bool iRunNested;
```

Flag indicating whether this function can run nested in a loop over functions. 

### variable myLoopManagerCapability

```
str myLoopManagerCapability;
```

Capability of a function that mangages a loop that this function can run inside of. 

### variable myLoopManagerType

```
str myLoopManagerType;
```

Capability of a function that mangages a loop that this function can run inside of. 

### variable myLoopManager

```
functor * myLoopManager;
```

Pointer to the functor that mangages the loop that this function runs inside of. 

### variable myNestedFunctorList

```
std::vector< functor * > myNestedFunctorList;
```

Vector of functors that have been set up to run nested within this one. 

### variable myCurrentIteration

```
long long * myCurrentIteration;
```

Pointer to counters for iterations of nested functor loop. 

### variable globlMaxThreads

```
const int globlMaxThreads;
```

Maximum number of OpenMP threads this MPI process is permitted to launch in total. 

### variable myGroups

```
std::set< str > myGroups;
```

Internal list of backend groups that this functor's requirements fall into. 

### variable chosenReqsFromGroups

```
std::map< str, str > chosenReqsFromGroups;
```

Map from groups to backend reqs, indicating which backend req has been activated for which backend group. 

### variable myBackendReqs

```
std::set< sspair > myBackendReqs;
```

Set of all backend requirement-type string pairs. 

### variable myResolvableBackendReqs

```
std::set< sspair > myResolvableBackendReqs;
```

Set of all backend requirement-type string pairs currently available for resolution. 

### variable myGroupedBackendReqs

```
std::map< str, std::set< sspair > > myGroupedBackendReqs;
```

Set of backend requirement-type string pairs for specific backend groups. 

### variable myDependencies

```
std::set< sspair > myDependencies;
```

Vector of dependency-type string pairs. 

### variable myConditionalDependencies

```
std::map< str, str > myConditionalDependencies;
```

Map of conditional dependencies to their types. 

### variable myBackendConditionalDependencies

```
std::map< std::vector< str >, std::set< sspair > > myBackendConditionalDependencies;
```

Map from (vector with 4 strings: backend req, type, backend, version) to (set of {conditional dependency-type} pairs) 

### variable myModelConditionalDependencies

```
std::map< str, std::set< sspair > > myModelConditionalDependencies;
```

Map from models to (set of {conditional dependency-type} pairs) 

### variable myModelConditionalBackendReqs

```
std::map< str, std::set< sspair > > myModelConditionalBackendReqs;
```

Map from models to (set of {conditional backend requirement-type} pairs) 

### variable activeModelFlags

```
std::map< str, bool > activeModelFlags;
```

Map from known models to flags indicating if they are activated or not (known = allowed, in allowed groups or conditions for conditional dependencies) 

### variable dependency_map

```
std::map< sspair, void(*)(functor *, module_functor_common *)> dependency_map;
```


Map from (dependency-type pairs) to (pointers to templated void functions that set dependency functor pointers) 


### variable dependency_functor_map

```
std::map< sspair, functor * > dependency_functor_map;
```


Map from (dependency-type pairs) to pointers to functors used to resolve them that set dependency functor pointers) 


### variable backendreq_types

```
std::map< str, str > backendreq_types;
```

Map from backend requirements to their required types. 

### variable backendreq_groups

```
std::map< sspair, str > backendreq_groups;
```

Map from backend requirements to their designated groups. 

### variable backendreq_tagmap

```
std::map< sspair, std::set< str > > backendreq_tagmap;
```

Map from backend requirements to their rule tags. 

### variable backendreq_map

```
std::map< sspair, void(*)(functor *)> backendreq_map;
```


Map from (backend requirement-type pairs) to (pointers to templated void functions that set backend requirement functor pointers) 


### variable permitted_map

```
std::map< sspair, std::set< sspair > > permitted_map;
```

Map from (backend requirement-type pairs) to (set of permitted {backend-version} pairs) 

### variable myForcedMatches

```
std::map< str, std::set< sspair > > myForcedMatches;
```

Map from tags to sets of matching (backend requirement-type pairs) that are forced to use the same backend. 

### variable required_classloading_backends

```
std::map< str, std::set< str > > required_classloading_backends;
```

Map from required classloading backends to their versions. 

### variable missing_backends

```
std::vector< str > missing_backends;
```

Vector of required backends currently missing. 

### variable tp

```
timespec tp;
```

Internal timespec object. 

### variable myLogTag

```
int myLogTag;
```

Integer LogTag, for tagging log messages. 

### variable signal_mode_locked

```
bool signal_mode_locked = true;
```


While locked, prevent this function switching off threadsafe* emergency signal handling. *The emergency signal handling cannot be made completely threadsafe; it can still cause lockups and memory corruption if it occurs at an inopportune time. "soft" shutdown is always preferable. 


## Friends

### friend FunctorHelp::entering_multithreaded_region

```
friend void FunctorHelp::entering_multithreaded_region(
    module_functor_common & 
);
```

Connectors to external helper functions (to decouple signal handling from this class) 

### friend FunctorHelp::leaving_multithreaded_region

```
friend void FunctorHelp::leaving_multithreaded_region(
    module_functor_common & 
);
```


-------------------------------

Updated on 2022-09-08 at 01:48:54 +0000