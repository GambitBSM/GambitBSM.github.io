---
title: "class Gambit::module_functor"
description: "Actual module functor type for all but TYPE=void. "

---

# class Gambit::module_functor



Actual module functor type for all but TYPE=void.  [More...](#detailed-description)


`#include <functors.hpp>`

Inherits from [Gambit::module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/), [Gambit::functor](/documentation/code/classes/classgambit_1_1functor/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[module_functor](/documentation/code/classes/classgambit_1_1module__functor/)**(void(*)(TYPE &) inputFunction, [str](/documentation/code/namespaces/namespacegambit/) func_name, [str](/documentation/code/namespaces/namespacegambit/) func_capability, [str](/documentation/code/namespaces/namespacegambit/) result_type, [str](/documentation/code/namespaces/namespacegambit/) origin_name, [Models::ModelFunctorClaw](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/) & claw)<br>Constructor.  |
| virtual | **[~module_functor](/documentation/code/classes/classgambit_1_1module__functor/)**()<br>Destructor.  |
| virtual void | **[setPrintRequirement](/documentation/code/classes/classgambit_1_1module__functor/)**(bool flag)<br>Setter for indicating if the wrapped function's result should to be printed.  |
| virtual bool | **[requiresPrinting](/documentation/code/classes/classgambit_1_1module__functor/)**() const<br>Getter indicating if the wrapped function's result should to be printed.  |
| virtual void | **[calculate](/documentation/code/classes/classgambit_1_1module__functor/)**()<br>Calculate method.  |
| const TYPE & | **[operator()](/documentation/code/classes/classgambit_1_1module__functor/)**(int index)<br>Operation (return value)  |
| [safe_ptr](/documentation/code/classes/classgambit_1_1safe__ptr/)< TYPE > | **[valuePtr](/documentation/code/classes/classgambit_1_1module__functor/)**()<br>Alternative to operation (returns a safe pointer to value)  |
| virtual void | **[print](/documentation/code/classes/classgambit_1_1module__functor/)**([Printers::BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/) * printer, const int pointID, int index)<br>Printer function.  |
| virtual void | **[print](/documentation/code/classes/classgambit_1_1module__functor/)**([Printers::BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/) * printer, const int pointID)<br>Printer function (no-thread-index short-circuit)  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| virtual void | **[init_memory](/documentation/code/classes/classgambit_1_1module__functor/)**()<br>Initialise the memory of this functor.  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| void(*)(TYPE &) | **[myFunction](/documentation/code/classes/classgambit_1_1module__functor/)** <br>Internal storage of function pointer.  |
| TYPE * | **[myValue](/documentation/code/classes/classgambit_1_1module__functor/)** <br>Internal pointer to storage location of function value.  |
| bool | **[myPrintFlag](/documentation/code/classes/classgambit_1_1module__functor/)** <br>Flag to select whether or not the results of this functor should be sent to the printer object.  |

## Additional inherited members

**Public Functions inherited from [Gambit::module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/)**

|                | Name           |
| -------------- | -------------- |
| | **[module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/)**([str](/documentation/code/namespaces/namespacegambit/) func_name, [str](/documentation/code/namespaces/namespacegambit/) func_capability, [str](/documentation/code/namespaces/namespacegambit/) result_type, [str](/documentation/code/namespaces/namespacegambit/) origin_name, [Models::ModelFunctorClaw](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/) & claw)<br>Constructor.  |
| virtual | **[~module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/)**()<br>Destructor.  |
| virtual double | **[getRuntimeAverage](/documentation/code/classes/classgambit_1_1module__functor__common/)**()<br>Getter for averaged runtime.  |
| virtual void | **[reset](/documentation/code/classes/classgambit_1_1module__functor__common/)**()<br>Reset functor.  |
| virtual void | **[notifyOfInvalidation](/documentation/code/classes/classgambit_1_1module__functor__common/)**(const [str](/documentation/code/namespaces/namespacegambit/) & msg)<br>Tell the functor that it invalidated the current point in model space, pass a message explaining why, and throw an exception.  |
| virtual double | **[getInvalidationRate](/documentation/code/classes/classgambit_1_1module__functor__common/)**()<br>Getter for invalidation rate.  |
| virtual void | **[setFadeRate](/documentation/code/classes/classgambit_1_1module__functor__common/)**(double new_rate)<br>Setter for the fade rate.  |
| virtual void | **[setTimingPrintRequirement](/documentation/code/classes/classgambit_1_1module__functor__common/)**(bool flag)<br>Setter for indicating if the timing data for this function's execution should be printed.  |
| virtual bool | **[requiresTimingPrinting](/documentation/code/classes/classgambit_1_1module__functor__common/)**() const<br>Getter indicating if the timing data for this function's execution should be printed.  |
| bool | **[getActiveModelFlag](/documentation/code/classes/classgambit_1_1module__functor__common/)**([str](/documentation/code/namespaces/namespacegambit/) model)<br>Indicate whether or not a known model is activated or not.  |
| [safe_ptr](/documentation/code/classes/classgambit_1_1safe__ptr/)< [str](/documentation/code/namespaces/namespacegambit/) > | **[getChosenReqFromGroup](/documentation/code/classes/classgambit_1_1module__functor__common/)**([str](/documentation/code/namespaces/namespacegambit/) group)<br>Return a safe pointer to a string indicating which backend requirement has been activated for a given backend group.  |
| virtual void | **[iterate](/documentation/code/classes/classgambit_1_1module__functor__common/)**(long long iteration)<br>Execute a single iteration in the loop managed by this functor.  |
| virtual void | **[init_myCurrentIteration_if_NULL](/documentation/code/classes/classgambit_1_1module__functor__common/)**()<br>Initialise the array holding the current iteration(s) of this functor.  |
| virtual void | **[setIteration](/documentation/code/classes/classgambit_1_1module__functor__common/)**(long long iteration)<br>Setter for setting the iteration number in the loop in which this functor runs.  |
| virtual [omp_safe_ptr](/documentation/code/classes/classgambit_1_1omp__safe__ptr/)< long long > | **[iterationPtr](/documentation/code/classes/classgambit_1_1module__functor__common/)**()<br>Return a safe pointer to the iteration number in the loop in which this functor runs.  |
| virtual void | **[setCanBeLoopManager](/documentation/code/classes/classgambit_1_1module__functor__common/)**(bool canManage)<br>Setter for specifying whether this is permitted to be a manager functor, which runs other functors nested in a loop.  |
| virtual bool | **[canBeLoopManager](/documentation/code/classes/classgambit_1_1module__functor__common/)**()<br>Getter for revealing whether this is permitted to be a manager functor.  |
| virtual void | **[setLoopManagerCapType](/documentation/code/classes/classgambit_1_1module__functor__common/)**([str](/documentation/code/namespaces/namespacegambit/) cap, [str](/documentation/code/namespaces/namespacegambit/) t)<br>Setter for specifying the capability required of a manager functor, if it is to run this functor nested in a loop.  |
| virtual [str](/documentation/code/namespaces/namespacegambit/) | **[loopManagerCapability](/documentation/code/classes/classgambit_1_1module__functor__common/)**()<br>Getter for revealing the required capability of the wrapped function's loop manager.  |
| virtual [str](/documentation/code/namespaces/namespacegambit/) | **[loopManagerType](/documentation/code/classes/classgambit_1_1module__functor__common/)**()<br>Getter for revealing the required type of the wrapped function's loop manager.  |
| virtual [str](/documentation/code/namespaces/namespacegambit/) | **[loopManagerName](/documentation/code/classes/classgambit_1_1module__functor__common/)**()<br>Getter for revealing the name of the wrapped function's assigned loop manager.  |
| virtual [str](/documentation/code/namespaces/namespacegambit/) | **[loopManagerOrigin](/documentation/code/classes/classgambit_1_1module__functor__common/)**()<br>Getter for revealing the module of the wrapped function's assigned loop manager.  |
| virtual void | **[breakLoopFromManagedFunctor](/documentation/code/classes/classgambit_1_1module__functor__common/)**()<br>Tell the manager of the loop in which this functor runs that it is time to break the loop.  |
| virtual [safe_ptr](/documentation/code/classes/classgambit_1_1safe__ptr/)< bool > | **[loopIsDone](/documentation/code/classes/classgambit_1_1module__functor__common/)**()<br>Return a safe pointer to the flag indicating that a loop managed by this functor should break now.  |
| virtual void | **[resetLoop](/documentation/code/classes/classgambit_1_1module__functor__common/)**()<br>Provide a way to reset the flag indicating that a loop managed by this functor should break.  |
| virtual void | **[breakLoop](/documentation/code/classes/classgambit_1_1module__functor__common/)**()<br>Tell the functor that the loop it manages should break now.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/) > | **[dependencies](/documentation/code/classes/classgambit_1_1module__functor__common/)**()<br>Getter for listing currently activated dependencies.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/) > | **[backendclassloading](/documentation/code/classes/classgambit_1_1module__functor__common/)**()<br>Getter for listing backends that require class loading.  |
| virtual std::set< [str](/documentation/code/namespaces/namespacegambit/) > | **[backendgroups](/documentation/code/classes/classgambit_1_1module__functor__common/)**()<br>Getter for listing backend requirement groups.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/) > | **[backendreqs](/documentation/code/classes/classgambit_1_1module__functor__common/)**()<br>Getter for listing all backend requirements.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/) > | **[backendreqs](/documentation/code/classes/classgambit_1_1module__functor__common/)**([str](/documentation/code/namespaces/namespacegambit/) group)<br>Getter for listing backend requirements from a specific group.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/) > | **[backendspermitted](/documentation/code/classes/classgambit_1_1module__functor__common/)**([sspair](/documentation/code/namespaces/namespacegambit/) quant)<br>Getter for listing permitted backends.  |
| virtual std::set< [str](/documentation/code/namespaces/namespacegambit/) > | **[backendreq_tags](/documentation/code/classes/classgambit_1_1module__functor__common/)**([sspair](/documentation/code/namespaces/namespacegambit/) quant)<br>Getter for listing tags associated with backend requirements.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/) > | **[forcematchingbackend](/documentation/code/classes/classgambit_1_1module__functor__common/)**([str](/documentation/code/namespaces/namespacegambit/) tag)<br>Getter for listing backend requirements that must be resolved from the same backend.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/) > | **[backend_conditional_dependencies](/documentation/code/classes/classgambit_1_1module__functor__common/)**([str](/documentation/code/namespaces/namespacegambit/) req, [str](/documentation/code/namespaces/namespacegambit/) type, [str](/documentation/code/namespaces/namespacegambit/) be, [str](/documentation/code/namespaces/namespacegambit/) ver)<br>Getter for listing backend-specific conditional dependencies (4-string version)  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/) > | **[backend_conditional_dependencies](/documentation/code/classes/classgambit_1_1module__functor__common/)**([str](/documentation/code/namespaces/namespacegambit/) req, [str](/documentation/code/namespaces/namespacegambit/) type, [str](/documentation/code/namespaces/namespacegambit/) be)<br>Getter for backend-specific conditional dependencies (3-string version)  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/) > | **[backend_conditional_dependencies](/documentation/code/classes/classgambit_1_1module__functor__common/)**([functor](/documentation/code/classes/classgambit_1_1functor/) * be_functor)<br>Getter for backend-specific conditional dependencies (backend functor pointer version)  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/) > | **[model_conditional_dependencies](/documentation/code/classes/classgambit_1_1module__functor__common/)**([str](/documentation/code/namespaces/namespacegambit/) model)<br>Getter for listing model-specific conditional dependencies.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/) > | **[model_conditional_backend_reqs](/documentation/code/classes/classgambit_1_1module__functor__common/)**([str](/documentation/code/namespaces/namespacegambit/) model)<br>Getter for listing model-specific conditional backend requirements.  |
| void | **[setDependency](/documentation/code/classes/classgambit_1_1module__functor__common/)**([str](/documentation/code/namespaces/namespacegambit/) dep, [str](/documentation/code/namespaces/namespacegambit/) dep_type, void(*)([functor](/documentation/code/classes/classgambit_1_1functor/) *, [module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/) *) resolver, [str](/documentation/code/namespaces/namespacegambit/) purpose ="")<br>Add and activate unconditional dependencies.  |
| void | **[setConditionalDependency](/documentation/code/classes/classgambit_1_1module__functor__common/)**([str](/documentation/code/namespaces/namespacegambit/) dep, [str](/documentation/code/namespaces/namespacegambit/) dep_type)<br>Add conditional dependency-type pairs in advance of later conditions.  |
| void | **[setBackendConditionalDependency](/documentation/code/classes/classgambit_1_1module__functor__common/)**([str](/documentation/code/namespaces/namespacegambit/) req, [str](/documentation/code/namespaces/namespacegambit/) be, [str](/documentation/code/namespaces/namespacegambit/) ver, [str](/documentation/code/namespaces/namespacegambit/) dep, void(*)([functor](/documentation/code/classes/classgambit_1_1functor/) *, [module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/) *) resolver)<br>Add a backend conditional dependency for multiple backend versions.  |
| void | **[setBackendConditionalDependencySingular](/documentation/code/classes/classgambit_1_1module__functor__common/)**([str](/documentation/code/namespaces/namespacegambit/) req, [str](/documentation/code/namespaces/namespacegambit/) be, [str](/documentation/code/namespaces/namespacegambit/) ver, [str](/documentation/code/namespaces/namespacegambit/) dep, void(*)([functor](/documentation/code/classes/classgambit_1_1functor/) *, [module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/) *) resolver)<br>Add a backend conditional dependency for a single backend version.  |
| void | **[setModelConditionalDependency](/documentation/code/classes/classgambit_1_1module__functor__common/)**([str](/documentation/code/namespaces/namespacegambit/) model, [str](/documentation/code/namespaces/namespacegambit/) dep, void(*)([functor](/documentation/code/classes/classgambit_1_1functor/) *, [module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/) *) resolver)<br>Add a model conditional dependency for multiple models.  |
| void | **[setModelConditionalDependencySingular](/documentation/code/classes/classgambit_1_1module__functor__common/)**([str](/documentation/code/namespaces/namespacegambit/) model, [str](/documentation/code/namespaces/namespacegambit/) dep, void(*)([functor](/documentation/code/classes/classgambit_1_1functor/) *, [module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/) *) resolver)<br>Add a model conditional dependency for a single model.  |
| void | **[makeBackendRuleForModel](/documentation/code/classes/classgambit_1_1module__functor__common/)**([str](/documentation/code/namespaces/namespacegambit/) model, [str](/documentation/code/namespaces/namespacegambit/) tag)<br>Add a rule for activating backend requirements according to the model being scanned.  |
| void | **[setBackendReq](/documentation/code/classes/classgambit_1_1module__functor__common/)**([str](/documentation/code/namespaces/namespacegambit/) group, [str](/documentation/code/namespaces/namespacegambit/) req, [str](/documentation/code/namespaces/namespacegambit/) tags, [str](/documentation/code/namespaces/namespacegambit/) type, void(*)([functor](/documentation/code/classes/classgambit_1_1functor/) *) resolver) |
| void | **[setModelConditionalBackendReq](/documentation/code/classes/classgambit_1_1module__functor__common/)**([str](/documentation/code/namespaces/namespacegambit/) model, [str](/documentation/code/namespaces/namespacegambit/) req, [str](/documentation/code/namespaces/namespacegambit/) type)<br>Add a model conditional backend requirement for multiple models.  |
| void | **[setModelConditionalBackendReqSingular](/documentation/code/classes/classgambit_1_1module__functor__common/)**([str](/documentation/code/namespaces/namespacegambit/) model, [str](/documentation/code/namespaces/namespacegambit/) req, [str](/documentation/code/namespaces/namespacegambit/) type)<br>Add a model conditional backend requirement for a single model.  |
| void | **[makeBackendOptionRule](/documentation/code/classes/classgambit_1_1module__functor__common/)**([str](/documentation/code/namespaces/namespacegambit/) be_and_ver, [str](/documentation/code/namespaces/namespacegambit/) tag)<br>Add a rule for dictating which backends can be used to fulfill which backend requirements.  |
| void | **[setPermittedBackend](/documentation/code/classes/classgambit_1_1module__functor__common/)**([str](/documentation/code/namespaces/namespacegambit/) req, [str](/documentation/code/namespaces/namespacegambit/) be, [str](/documentation/code/namespaces/namespacegambit/) ver)<br>Add a single permitted backend version.  |
| void | **[makeBackendMatchingRule](/documentation/code/classes/classgambit_1_1module__functor__common/)**([str](/documentation/code/namespaces/namespacegambit/) tag)<br>Add one or more rules for forcing backends reqs with the same tags to always be resolved from the same backend.  |
| void | **[setRequiredClassloader](/documentation/code/classes/classgambit_1_1module__functor__common/)**([str](/documentation/code/namespaces/namespacegambit/) be, [str](/documentation/code/namespaces/namespacegambit/) ver, [str](/documentation/code/namespaces/namespacegambit/) safe_ver)<br>Add a rule indicating that classes from a given backend must be available.  |
| virtual void | **[notifyOfBackends](/documentation/code/classes/classgambit_1_1module__functor__common/)**(std::map< [str](/documentation/code/namespaces/namespacegambit/), std::set< [str](/documentation/code/namespaces/namespacegambit/) > > be_ver_map)<br>Indicate to the functor which backends are actually loaded and working.  |
| virtual void | **[setNestedList](/documentation/code/classes/classgambit_1_1module__functor__common/)**(std::vector< [functor](/documentation/code/classes/classgambit_1_1functor/) * > & newNestedList)<br>Set the ordered list of pointers to other functors that should run nested in a loop managed by this one.  |
| virtual void | **[resolveDependency](/documentation/code/classes/classgambit_1_1module__functor__common/)**([functor](/documentation/code/classes/classgambit_1_1functor/) * dep_functor)<br>Resolve a dependency using a pointer to another functor object.  |
| virtual void | **[resolveLoopManager](/documentation/code/classes/classgambit_1_1module__functor__common/)**([functor](/documentation/code/classes/classgambit_1_1functor/) * dep_functor)<br>Set this functor's loop manager (if it has one)  |
| virtual void | **[resolveBackendReq](/documentation/code/classes/classgambit_1_1module__functor__common/)**([functor](/documentation/code/classes/classgambit_1_1functor/) * be_functor)<br>Resolve a backend requirement using a pointer to another functor object.  |
| virtual void | **[notifyOfModel](/documentation/code/classes/classgambit_1_1module__functor__common/)**([str](/documentation/code/namespaces/namespacegambit/) model)<br>Notify the functor that a certain model is being scanned, so that it can activate its dependencies and backend reqs accordingly.  |
| virtual void | **[notifyOfDependee](/documentation/code/classes/classgambit_1_1module__functor__common/)**([functor](/documentation/code/classes/classgambit_1_1functor/) * dependent_functor)<br>Notify the functor that another functor depends on it.  |
| virtual [invalid_point_exception](/documentation/code/classes/classgambit_1_1invalid__point__exception/) * | **[retrieve_invalid_point_exception](/documentation/code/classes/classgambit_1_1module__functor__common/)**()<br>Retrieve the previously saved exception generated when this functor invalidated the current point in model space.  |

**Protected Functions inherited from [Gambit::module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/)**

|                | Name           |
| -------------- | -------------- |
| virtual void | **[reset](/documentation/code/classes/classgambit_1_1module__functor__common/)**(int thread_num)<br>Reset functor for one thread only.  |
| virtual void | **[acknowledgeInvalidation](/documentation/code/classes/classgambit_1_1module__functor__common/)**([invalid_point_exception](/documentation/code/classes/classgambit_1_1invalid__point__exception/) & e, [functor](/documentation/code/classes/classgambit_1_1functor/) * f =NULL)<br>Acknowledge that this functor invalidated the current point in model space.  |
| virtual void | **[startTiming](/documentation/code/classes/classgambit_1_1module__functor__common/)**(int thread_num)<br>Do pre-calculate timing things.  |
| virtual void | **[finishTiming](/documentation/code/classes/classgambit_1_1module__functor__common/)**(int thread_num)<br>Do post-calculate timing things.  |
| void | **[fill_activeModelFlags](/documentation/code/classes/classgambit_1_1module__functor__common/)**()<br>Construct the list of known models only if it doesn't yet exist.  |
| [sspair](/documentation/code/namespaces/namespacegambit/) | **[retrieve_conditional_dep_type_pair](/documentation/code/classes/classgambit_1_1module__functor__common/)**([str](/documentation/code/namespaces/namespacegambit/) dep)<br>Retrieve full conditional dependency-type pair from conditional dependency only.  |
| void | **[check_missing_LogTag](/documentation/code/classes/classgambit_1_1module__functor__common/)**()<br>Check if an appropriate LogTag for this functor is missing from the logging system.  |
| void | **[entering_multithreaded_region](/documentation/code/classes/classgambit_1_1module__functor__common/)**() |
| void | **[leaving_multithreaded_region](/documentation/code/classes/classgambit_1_1module__functor__common/)**() |

**Protected Attributes inherited from [Gambit::module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/)**

|                | Name           |
| -------------- | -------------- |
| bool | **[myTimingPrintFlag](/documentation/code/classes/classgambit_1_1module__functor__common/)** <br>Flag to select whether or not the timing data for this function's execution should be printed;.  |
| std::chrono::time_point< std::chrono::system_clock > * | **[start](/documentation/code/classes/classgambit_1_1module__functor__common/)** <br>Beginning and end timing points.  |
| std::chrono::time_point< std::chrono::system_clock > * | **[end](/documentation/code/classes/classgambit_1_1module__functor__common/)**  |
| bool | **[point_exception_raised](/documentation/code/classes/classgambit_1_1module__functor__common/)** <br>A flag indicating whether or not this functor has invalidated the current point.  |
| [invalid_point_exception](/documentation/code/classes/classgambit_1_1invalid__point__exception/) | **[raised_point_exception](/documentation/code/classes/classgambit_1_1module__functor__common/)** <br>An exception raised because this functor has invalidated the current point.  |
| double | **[runtime_average](/documentation/code/classes/classgambit_1_1module__functor__common/)** <br>Averaged runtime in ns.  |
| double | **[fadeRate](/documentation/code/classes/classgambit_1_1module__functor__common/)** <br>Fade rate for average runtime.  |
| double | **[pInvalidation](/documentation/code/classes/classgambit_1_1module__functor__common/)** <br>Probability that functors invalidates point in model parameter space.  |
| bool * | **[needs_recalculating](/documentation/code/classes/classgambit_1_1module__functor__common/)** <br>Needs recalculating or not?  |
| bool * | **[already_printed](/documentation/code/classes/classgambit_1_1module__functor__common/)** <br>Has result already been sent to the printer?  |
| bool * | **[already_printed_timing](/documentation/code/classes/classgambit_1_1module__functor__common/)** <br>Has timing data already been sent to the printer?  |
| bool | **[iCanManageLoops](/documentation/code/classes/classgambit_1_1module__functor__common/)** <br>Flag indicating whether this function can manage a loop over other functions.  |
| bool | **[myLoopIsDone](/documentation/code/classes/classgambit_1_1module__functor__common/)** <br>Flag indicating whether this function is ready to finish its loop (only relevant if iCanManageLoops = true)  |
| bool | **[iRunNested](/documentation/code/classes/classgambit_1_1module__functor__common/)** <br>Flag indicating whether this function can run nested in a loop over functions.  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[myLoopManagerCapability](/documentation/code/classes/classgambit_1_1module__functor__common/)** <br>Capability of a function that mangages a loop that this function can run inside of.  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[myLoopManagerType](/documentation/code/classes/classgambit_1_1module__functor__common/)** <br>Capability of a function that mangages a loop that this function can run inside of.  |
| [functor](/documentation/code/classes/classgambit_1_1functor/) * | **[myLoopManager](/documentation/code/classes/classgambit_1_1module__functor__common/)** <br>Pointer to the functor that mangages the loop that this function runs inside of.  |
| std::vector< [functor](/documentation/code/classes/classgambit_1_1functor/) * > | **[myNestedFunctorList](/documentation/code/classes/classgambit_1_1module__functor__common/)** <br>Vector of functors that have been set up to run nested within this one.  |
| long long * | **[myCurrentIteration](/documentation/code/classes/classgambit_1_1module__functor__common/)** <br>Pointer to counters for iterations of nested functor loop.  |
| const int | **[globlMaxThreads](/documentation/code/classes/classgambit_1_1module__functor__common/)** <br>Maximum number of OpenMP threads this MPI process is permitted to launch in total.  |
| std::set< [str](/documentation/code/namespaces/namespacegambit/) > | **[myGroups](/documentation/code/classes/classgambit_1_1module__functor__common/)** <br>Internal list of backend groups that this functor's requirements fall into.  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/), [str](/documentation/code/namespaces/namespacegambit/) > | **[chosenReqsFromGroups](/documentation/code/classes/classgambit_1_1module__functor__common/)** <br>Map from groups to backend reqs, indicating which backend req has been activated for which backend group.  |
| std::set< [sspair](/documentation/code/namespaces/namespacegambit/) > | **[myBackendReqs](/documentation/code/classes/classgambit_1_1module__functor__common/)** <br>Set of all backend requirement-type string pairs.  |
| std::set< [sspair](/documentation/code/namespaces/namespacegambit/) > | **[myResolvableBackendReqs](/documentation/code/classes/classgambit_1_1module__functor__common/)** <br>Set of all backend requirement-type string pairs currently available for resolution.  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/), std::set< [sspair](/documentation/code/namespaces/namespacegambit/) > > | **[myGroupedBackendReqs](/documentation/code/classes/classgambit_1_1module__functor__common/)** <br>Set of backend requirement-type string pairs for specific backend groups.  |
| std::set< [sspair](/documentation/code/namespaces/namespacegambit/) > | **[myDependencies](/documentation/code/classes/classgambit_1_1module__functor__common/)** <br>Vector of dependency-type string pairs.  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/), [str](/documentation/code/namespaces/namespacegambit/) > | **[myConditionalDependencies](/documentation/code/classes/classgambit_1_1module__functor__common/)** <br>Map of conditional dependencies to their types.  |
| std::map< std::vector< [str](/documentation/code/namespaces/namespacegambit/) >, std::set< [sspair](/documentation/code/namespaces/namespacegambit/) > > | **[myBackendConditionalDependencies](/documentation/code/classes/classgambit_1_1module__functor__common/)** <br>Map from (vector with 4 strings: backend req, type, backend, version) to (set of {conditional dependency-type} pairs)  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/), std::set< [sspair](/documentation/code/namespaces/namespacegambit/) > > | **[myModelConditionalDependencies](/documentation/code/classes/classgambit_1_1module__functor__common/)** <br>Map from models to (set of {conditional dependency-type} pairs)  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/), std::set< [sspair](/documentation/code/namespaces/namespacegambit/) > > | **[myModelConditionalBackendReqs](/documentation/code/classes/classgambit_1_1module__functor__common/)** <br>Map from models to (set of {conditional backend requirement-type} pairs)  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/), bool > | **[activeModelFlags](/documentation/code/classes/classgambit_1_1module__functor__common/)** <br>Map from known models to flags indicating if they are activated or not (known = allowed, in allowed groups or conditions for conditional dependencies)  |
| std::map< [sspair](/documentation/code/namespaces/namespacegambit/), void(*)([functor](/documentation/code/classes/classgambit_1_1functor/) *, [module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/) *)> | **[dependency_map](/documentation/code/classes/classgambit_1_1module__functor__common/)**  |
| std::map< [sspair](/documentation/code/namespaces/namespacegambit/), [functor](/documentation/code/classes/classgambit_1_1functor/) * > | **[dependency_functor_map](/documentation/code/classes/classgambit_1_1module__functor__common/)**  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/), [str](/documentation/code/namespaces/namespacegambit/) > | **[backendreq_types](/documentation/code/classes/classgambit_1_1module__functor__common/)** <br>Map from backend requirements to their required types.  |
| std::map< [sspair](/documentation/code/namespaces/namespacegambit/), [str](/documentation/code/namespaces/namespacegambit/) > | **[backendreq_groups](/documentation/code/classes/classgambit_1_1module__functor__common/)** <br>Map from backend requirements to their designated groups.  |
| std::map< [sspair](/documentation/code/namespaces/namespacegambit/), std::set< [str](/documentation/code/namespaces/namespacegambit/) > > | **[backendreq_tagmap](/documentation/code/classes/classgambit_1_1module__functor__common/)** <br>Map from backend requirements to their rule tags.  |
| std::map< [sspair](/documentation/code/namespaces/namespacegambit/), void(*)([functor](/documentation/code/classes/classgambit_1_1functor/) *)> | **[backendreq_map](/documentation/code/classes/classgambit_1_1module__functor__common/)**  |
| std::map< [sspair](/documentation/code/namespaces/namespacegambit/), std::set< [sspair](/documentation/code/namespaces/namespacegambit/) > > | **[permitted_map](/documentation/code/classes/classgambit_1_1module__functor__common/)** <br>Map from (backend requirement-type pairs) to (set of permitted {backend-version} pairs)  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/), std::set< [sspair](/documentation/code/namespaces/namespacegambit/) > > | **[myForcedMatches](/documentation/code/classes/classgambit_1_1module__functor__common/)** <br>Map from tags to sets of matching (backend requirement-type pairs) that are forced to use the same backend.  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/), std::set< [str](/documentation/code/namespaces/namespacegambit/) > > | **[required_classloading_backends](/documentation/code/classes/classgambit_1_1module__functor__common/)** <br>Map from required classloading backends to their versions.  |
| std::vector< [str](/documentation/code/namespaces/namespacegambit/) > | **[missing_backends](/documentation/code/classes/classgambit_1_1module__functor__common/)** <br>Vector of required backends currently missing.  |
| timespec | **[tp](/documentation/code/classes/classgambit_1_1module__functor__common/)** <br>Internal timespec object.  |
| int | **[myLogTag](/documentation/code/classes/classgambit_1_1module__functor__common/)** <br>Integer LogTag, for tagging log messages.  |
| bool | **[signal_mode_locked](/documentation/code/classes/classgambit_1_1module__functor__common/)**  |

**Friends inherited from [Gambit::module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/)**

|                | Name           |
| -------------- | -------------- |
| void | **[FunctorHelp::entering_multithreaded_region](/documentation/code/classes/classgambit_1_1module__functor__common/)**([module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/) & ) <br>Connectors to external helper functions (to decouple signal handling from this class)  |
| void | **[FunctorHelp::leaving_multithreaded_region](/documentation/code/classes/classgambit_1_1module__functor__common/)**([module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/) & )  |

**Public Functions inherited from [Gambit::functor](/documentation/code/classes/classgambit_1_1functor/)**

|                | Name           |
| -------------- | -------------- |
| virtual double | **[getRuntimeAverage](/documentation/code/classes/classgambit_1_1functor/)**() |
| virtual double | **[getInvalidationRate](/documentation/code/classes/classgambit_1_1functor/)**() |
| virtual void | **[setFadeRate](/documentation/code/classes/classgambit_1_1functor/)**(double ) |
| virtual void | **[notifyOfInvalidation](/documentation/code/classes/classgambit_1_1functor/)**(const [str](/documentation/code/namespaces/namespacegambit/) & ) |
| virtual void | **[reset](/documentation/code/classes/classgambit_1_1functor/)**() |
| | **[functor](/documentation/code/classes/classgambit_1_1functor/)**([str](/documentation/code/namespaces/namespacegambit/) func_name, [str](/documentation/code/namespaces/namespacegambit/) func_capability, [str](/documentation/code/namespaces/namespacegambit/) result_type, [str](/documentation/code/namespaces/namespacegambit/) origin_name, [Models::ModelFunctorClaw](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/) & claw)<br>Constructor.  |
| virtual | **[~functor](/documentation/code/classes/classgambit_1_1functor/)**() |
| virtual void | **[reset_and_calculate](/documentation/code/classes/classgambit_1_1functor/)**()<br>Reset-then-recalculate method.  |
| void | **[setStatus](/documentation/code/classes/classgambit_1_1functor/)**(int stat) |
| virtual void | **[setInUse](/documentation/code/classes/classgambit_1_1functor/)**(bool )<br>Set the inUse flag (must be overridden in derived class to have any effect).  |
| void | **[setPurpose](/documentation/code/classes/classgambit_1_1functor/)**([str](/documentation/code/namespaces/namespacegambit/) purpose)<br>Setter for purpose (relevant only for next-to-output functors)  |
| void | **[setVertexID](/documentation/code/classes/classgambit_1_1functor/)**(int ID)<br>Setter for vertex ID (used in printer system)  |
| void | **[setTimingVertexID](/documentation/code/classes/classgambit_1_1functor/)**(int ID)<br>Set ID for timing 'vertex' (used in printer system)  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[name](/documentation/code/classes/classgambit_1_1functor/)**() const<br>Getter for the wrapped function's name.  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[capability](/documentation/code/classes/classgambit_1_1functor/)**() const<br>Getter for the wrapped function's reported capability.  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[type](/documentation/code/classes/classgambit_1_1functor/)**() const<br>Getter for the wrapped function's reported return type.  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[origin](/documentation/code/classes/classgambit_1_1functor/)**() const<br>Getter for the wrapped function's origin (module or backend name)  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[version](/documentation/code/classes/classgambit_1_1functor/)**() const<br>Getter for the version of the wrapped function's origin (module or backend)  |
| virtual [str](/documentation/code/namespaces/namespacegambit/) | **[safe_version](/documentation/code/classes/classgambit_1_1functor/)**() const<br>Getter for the 'safe' incarnation of the version of the wrapped function's origin (module or backend)  |
| int | **[status](/documentation/code/classes/classgambit_1_1functor/)**() const |
| [sspair](/documentation/code/namespaces/namespacegambit/) | **[quantity](/documentation/code/classes/classgambit_1_1functor/)**() const<br>Getter for the overall quantity provided by the wrapped function (capability-type pair)  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[purpose](/documentation/code/classes/classgambit_1_1functor/)**() const<br>Getter for purpose (relevant for output nodes, aka helper structures for the dep. resolution)  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[citationKey](/documentation/code/classes/classgambit_1_1functor/)**() const<br>Getter for the citation key.  |
| int | **[vertexID](/documentation/code/classes/classgambit_1_1functor/)**() const<br>Getter for vertex ID.  |
| int | **[timingVertexID](/documentation/code/classes/classgambit_1_1functor/)**() const<br>Getter for timing vertex ID.  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[label](/documentation/code/classes/classgambit_1_1functor/)**() const<br>Getter for string label.  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[timingLabel](/documentation/code/classes/classgambit_1_1functor/)**() const<br>Getter for the printer timing label.  |
| virtual bool | **[requiresTimingPrinting](/documentation/code/classes/classgambit_1_1functor/)**() const<br>Getter indicating if the timing data for this function's execution should be printed.  |
| virtual void | **[setTimingPrintRequirement](/documentation/code/classes/classgambit_1_1functor/)**(bool flag)<br>Setter for indicating if the timing data for this function's execution should be printed.  |
| virtual void | **[setNestedList](/documentation/code/classes/classgambit_1_1functor/)**(std::vector< [functor](/documentation/code/classes/classgambit_1_1functor/) * > & )<br>Set the ordered list of pointers to other functors that should run nested in a loop managed by this one.  |
| virtual void | **[setIteration](/documentation/code/classes/classgambit_1_1functor/)**(long long )<br>Set the iteration number in a loop in which this functor runs.  |
| virtual bool | **[canBeLoopManager](/documentation/code/classes/classgambit_1_1functor/)**()<br>Getter for revealing whether this is permitted to be a manager functor.  |
| virtual [str](/documentation/code/namespaces/namespacegambit/) | **[loopManagerCapability](/documentation/code/classes/classgambit_1_1functor/)**()<br>Getter for revealing the required capability of the wrapped function's loop manager.  |
| virtual [str](/documentation/code/namespaces/namespacegambit/) | **[loopManagerType](/documentation/code/classes/classgambit_1_1functor/)**()<br>Getter for revealing the required type of the wrapped function's loop manager.  |
| virtual [str](/documentation/code/namespaces/namespacegambit/) | **[loopManagerName](/documentation/code/classes/classgambit_1_1functor/)**()<br>Getter for revealing the name of the wrapped function's assigned loop manager.  |
| virtual [str](/documentation/code/namespaces/namespacegambit/) | **[loopManagerOrigin](/documentation/code/classes/classgambit_1_1functor/)**()<br>Getter for revealing the module of the wrapped function's assigned loop manager.  |
| virtual void | **[breakLoop](/documentation/code/classes/classgambit_1_1functor/)**()<br>Tell the functor that the loop it manages should break now.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/) > | **[dependencies](/documentation/code/classes/classgambit_1_1functor/)**()<br>Getter for listing currently activated dependencies.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/) > | **[backendclassloading](/documentation/code/classes/classgambit_1_1functor/)**()<br>Getter for listing backends that require class loading.  |
| virtual std::set< [str](/documentation/code/namespaces/namespacegambit/) > | **[backendgroups](/documentation/code/classes/classgambit_1_1functor/)**()<br>Getter for listing backend requirement groups.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/) > | **[backendreqs](/documentation/code/classes/classgambit_1_1functor/)**()<br>Getter for listing all backend requirements.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/) > | **[backendreqs](/documentation/code/classes/classgambit_1_1functor/)**([str](/documentation/code/namespaces/namespacegambit/) )<br>Getter for listing backend requirements from a specific group.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/) > | **[backendspermitted](/documentation/code/classes/classgambit_1_1functor/)**([sspair](/documentation/code/namespaces/namespacegambit/) )<br>Getter for listing permitted backends.  |
| virtual std::set< [str](/documentation/code/namespaces/namespacegambit/) > | **[backendreq_tags](/documentation/code/classes/classgambit_1_1functor/)**([sspair](/documentation/code/namespaces/namespacegambit/) )<br>Getter for listing tags associated with backend requirements.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/) > | **[forcematchingbackend](/documentation/code/classes/classgambit_1_1functor/)**([str](/documentation/code/namespaces/namespacegambit/) )<br>Getter for listing backend requirements that must be resolved from the same backend.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/) > | **[backend_conditional_dependencies](/documentation/code/classes/classgambit_1_1functor/)**([str](/documentation/code/namespaces/namespacegambit/) , [str](/documentation/code/namespaces/namespacegambit/) , [str](/documentation/code/namespaces/namespacegambit/) , [str](/documentation/code/namespaces/namespacegambit/) )<br>Getter for listing backend-specific conditional dependencies (4-string version)  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/) > | **[backend_conditional_dependencies](/documentation/code/classes/classgambit_1_1functor/)**([str](/documentation/code/namespaces/namespacegambit/) req, [str](/documentation/code/namespaces/namespacegambit/) type, [str](/documentation/code/namespaces/namespacegambit/) be)<br>Getter for backend-specific conditional dependencies (3-string version)  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/) > | **[backend_conditional_dependencies](/documentation/code/classes/classgambit_1_1functor/)**([functor](/documentation/code/classes/classgambit_1_1functor/) * be_functor)<br>Getter for backend-specific conditional dependencies (backend functor pointer version)  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/) > | **[model_conditional_dependencies](/documentation/code/classes/classgambit_1_1functor/)**([str](/documentation/code/namespaces/namespacegambit/) )<br>Getter for listing model-specific conditional dependencies.  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/) > | **[model_conditional_backend_reqs](/documentation/code/classes/classgambit_1_1functor/)**([str](/documentation/code/namespaces/namespacegambit/) )<br>Getter for listing model-specific conditional backend requirements.  |
| virtual void | **[resolveDependency](/documentation/code/classes/classgambit_1_1functor/)**([functor](/documentation/code/classes/classgambit_1_1functor/) * )<br>Resolve a dependency using a pointer to another functor object.  |
| virtual void | **[resolveLoopManager](/documentation/code/classes/classgambit_1_1functor/)**([functor](/documentation/code/classes/classgambit_1_1functor/) * )<br>Set this functor's loop manager (if it has one)  |
| virtual void | **[resolveBackendReq](/documentation/code/classes/classgambit_1_1functor/)**([functor](/documentation/code/classes/classgambit_1_1functor/) * )<br>Resolve a backend requirement using a pointer to another functor object.  |
| virtual void | **[notifyOfModel](/documentation/code/classes/classgambit_1_1functor/)**([str](/documentation/code/namespaces/namespacegambit/) )<br>Notify the functor that a certain model is being scanned, so that it can activate itself accordingly.  |
| virtual void | **[notifyOfDependee](/documentation/code/classes/classgambit_1_1functor/)**([functor](/documentation/code/classes/classgambit_1_1functor/) * )<br>Notify the functor that it is being used to fill a dependency of another functor.  |
| virtual void | **[notifyOfBackends](/documentation/code/classes/classgambit_1_1functor/)**(std::map< [str](/documentation/code/namespaces/namespacegambit/), std::set< [str](/documentation/code/namespaces/namespacegambit/) > > )<br>Indicate to the functor which backends are actually loaded and working.  |
| virtual [invalid_point_exception](/documentation/code/classes/classgambit_1_1invalid__point__exception/) * | **[retrieve_invalid_point_exception](/documentation/code/classes/classgambit_1_1functor/)**()<br>Retrieve the previously saved exception generated when this functor invalidated the current point in model space.  |
| void | **[notifyOfIniOptions](/documentation/code/classes/classgambit_1_1functor/)**(const [Options](/documentation/code/classes/classgambit_1_1options/) & opt) |
| template <typename TYPE \> <br>void | **[setOption](/documentation/code/classes/classgambit_1_1functor/)**(const [str](/documentation/code/namespaces/namespacegambit/) & key, const TYPE val)<br>Set an option for the functor directly (for use in standalone executables).  |
| [safe_ptr](/documentation/code/classes/classgambit_1_1safe__ptr/)< [Options](/documentation/code/classes/classgambit_1_1options/) > | **[getOptions](/documentation/code/classes/classgambit_1_1functor/)**()<br>Return a safe pointer to the options that this functor is supposed to run with (e.g. from the ini file).  |
| void | **[notifyOfSubCaps](/documentation/code/classes/classgambit_1_1functor/)**(const [str](/documentation/code/namespaces/namespacegambit/) & subcap_string)<br>Notify the functor about a string in [YAML](/documentation/code/namespaces/namespaceyaml/) that contains the sub-capability information (for use in standalones)  |
| void | **[notifyOfSubCaps](/documentation/code/classes/classgambit_1_1functor/)**(const [Options](/documentation/code/classes/classgambit_1_1options/) & subcaps)<br>Notify the functor about an instance of the options class that contains sub-capability information.  |
| template <typename TYPE \> <br>void | **[setSubCap](/documentation/code/classes/classgambit_1_1functor/)**(const [str](/documentation/code/namespaces/namespacegambit/) & key, const TYPE val)<br>Set a sub-capability (subcap)for the functor directly (for use in standalone executables).  |
| [safe_ptr](/documentation/code/classes/classgambit_1_1safe__ptr/)< [Options](/documentation/code/classes/classgambit_1_1options/) > | **[getSubCaps](/documentation/code/classes/classgambit_1_1functor/)**()<br>Return a safe pointer to the subcaps that this functor realises it is supposed to facilitate downstream calculation of.  |
| [safe_ptr](/documentation/code/classes/classgambit_1_1safe__ptr/)< std::set< [sspair](/documentation/code/namespaces/namespacegambit/) > > | **[getDependees](/documentation/code/classes/classgambit_1_1functor/)**()<br>Return a safe pointer to the vector of all capability,type pairs of functors arranged downstream of this one in the dependency tree.  |
| bool | **[allModelsAllowed](/documentation/code/classes/classgambit_1_1functor/)**()<br>Test whether the functor is allowed to be used with all models.  |
| bool | **[modelAllowed](/documentation/code/classes/classgambit_1_1functor/)**([str](/documentation/code/namespaces/namespacegambit/) model)<br>Test whether the functor is always allowed (either explicitly or implicitly) to be used with a given model.  |
| bool | **[modelExplicitlyAllowed](/documentation/code/classes/classgambit_1_1functor/)**([str](/documentation/code/namespaces/namespacegambit/) model)<br>Test whether the functor is explictly always allowed to be used with a given model.  |
| void | **[setAllowedModel](/documentation/code/classes/classgambit_1_1functor/)**([str](/documentation/code/namespaces/namespacegambit/) model)<br>Add a model to the internal list of models for which this functor is allowed to be used.  |
| bool | **[modelComboAllowed](/documentation/code/classes/classgambit_1_1functor/)**(std::set< [str](/documentation/code/namespaces/namespacegambit/) > combo)<br>Test whether the functor is allowed (either explicitly or implicitly) to be used with a given combination of models.  |
| bool | **[modelComboExplicitlyAllowed](/documentation/code/classes/classgambit_1_1functor/)**(std::set< [str](/documentation/code/namespaces/namespacegambit/) > combo)<br>Test whether the functor has been explictly allowed to be used with a given combination of models.  |
| void | **[setModelGroup](/documentation/code/classes/classgambit_1_1functor/)**([str](/documentation/code/namespaces/namespacegambit/) group, [str](/documentation/code/namespaces/namespacegambit/) contents)<br>Add a model group definition to the internal list of model groups.  |
| void | **[setAllowedModelGroupCombo](/documentation/code/classes/classgambit_1_1functor/)**([str](/documentation/code/namespaces/namespacegambit/) groups)<br>Add a combination of model groups to the internal list of combinations for which this functor is allowed to be used.  |

**Protected Functions inherited from [Gambit::functor](/documentation/code/classes/classgambit_1_1functor/)**

|                | Name           |
| -------------- | -------------- |
| virtual void | **[reset](/documentation/code/classes/classgambit_1_1functor/)**(int )<br>Reset functor for one thread only.  |
| void | **[failBigTime](/documentation/code/classes/classgambit_1_1functor/)**([str](/documentation/code/namespaces/namespacegambit/) method)<br>Attempt to retrieve a dependency or model parameter that has not been resolved.  |
| bool | **[allowed_parent_or_friend_exists](/documentation/code/classes/classgambit_1_1functor/)**([str](/documentation/code/namespaces/namespacegambit/) model)<br>Test if there is a model in the functor's allowedModels list as which this model can be interpreted.  |
| bool | **[in_allowed_combo](/documentation/code/classes/classgambit_1_1functor/)**([str](/documentation/code/namespaces/namespacegambit/) model)<br>Check that a model is actually part of a combination that is allowed to be used with this functor.  |
| bool | **[contains_anything_interpretable_as_member_of](/documentation/code/classes/classgambit_1_1functor/)**(std::set< [str](/documentation/code/namespaces/namespacegambit/) > combo, [str](/documentation/code/namespaces/namespacegambit/) group)<br>Test whether any of the entries in a given model group is a valid interpretation of any members in a given combination.  |
| bool | **[has_common_elements](/documentation/code/classes/classgambit_1_1functor/)**(std::set< [str](/documentation/code/namespaces/namespacegambit/) > combo, [str](/documentation/code/namespaces/namespacegambit/) group)<br>Work out whether a given combination of models and a model group have any elements in common.  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[find_friend_or_parent_model_in_map](/documentation/code/classes/classgambit_1_1functor/)**([str](/documentation/code/namespaces/namespacegambit/) model, std::map< [str](/documentation/code/namespaces/namespacegambit/), std::set< [sspair](/documentation/code/namespaces/namespacegambit/) > > karta)<br>Try to find a parent or friend model in some user-supplied map from models to sspair vectors.  |

**Protected Attributes inherited from [Gambit::functor](/documentation/code/classes/classgambit_1_1functor/)**

|                | Name           |
| -------------- | -------------- |
| [str](/documentation/code/namespaces/namespacegambit/) | **[myName](/documentation/code/classes/classgambit_1_1functor/)** <br>Internal storage of the function name.  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[myCapability](/documentation/code/classes/classgambit_1_1functor/)** <br>Internal storage of exactly what the function calculates.  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[myType](/documentation/code/classes/classgambit_1_1functor/)** <br>Internal storage of the type of what the function calculates.  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[myOrigin](/documentation/code/classes/classgambit_1_1functor/)** <br>Internal storage of the name of the module or backend to which the function belongs.  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[myVersion](/documentation/code/classes/classgambit_1_1functor/)** <br>Internal storage of the version of the module or backend to which the function belongs.  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[myPurpose](/documentation/code/classes/classgambit_1_1functor/)** <br>Purpose of the function (relevant for output and next-to-output functors)  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[myCitationKey](/documentation/code/classes/classgambit_1_1functor/)** <br>Citation key: BibTex key of the reference.  |
| const [Models::ModelFunctorClaw](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/) * | **[myClaw](/documentation/code/classes/classgambit_1_1functor/)** <br>Bound model functor claw, for checking relationships between models.  |
| const [str](/documentation/code/namespaces/namespacegambit/) | **[myLabel](/documentation/code/classes/classgambit_1_1functor/)** <br>String label, used to label functor results for printer system.  |
| const [str](/documentation/code/namespaces/namespacegambit/) | **[myTimingLabel](/documentation/code/classes/classgambit_1_1functor/)** <br>String label, used to label functor timing data for printer system.  |
| int | **[myStatus](/documentation/code/classes/classgambit_1_1functor/)**  |
| int | **[myVertexID](/documentation/code/classes/classgambit_1_1functor/)** <br>Internal storage of the vertex ID number used by the printer system to identify functors.  |
| int | **[myTimingVertexID](/documentation/code/classes/classgambit_1_1functor/)** <br>ID assigned by printers to the timing data output stream.  |
| bool | **[verbose](/documentation/code/classes/classgambit_1_1functor/)** <br>Debug flag.  |
| [Options](/documentation/code/classes/classgambit_1_1options/) | **[myOptions](/documentation/code/classes/classgambit_1_1functor/)** <br>Internal storage of function options, as a [YAML](/documentation/code/namespaces/namespaceyaml/) node.  |
| [Options](/documentation/code/classes/classgambit_1_1options/) | **[mySubCaps](/documentation/code/classes/classgambit_1_1functor/)** <br>Internal storage of function sub-capabilities, as a [YAML](/documentation/code/namespaces/namespaceyaml/) node.  |
| std::set< [sspair](/documentation/code/namespaces/namespacegambit/) > | **[myDependees](/documentation/code/classes/classgambit_1_1functor/)** <br>List of all capability,type pairs of functors downstream of this one in the dependency tree.  |
| std::set< [str](/documentation/code/namespaces/namespacegambit/) > | **[allowedModels](/documentation/code/classes/classgambit_1_1functor/)** <br>List of allowed models.  |
| std::set< std::set< [str](/documentation/code/namespaces/namespacegambit/) > > | **[allowedGroupCombos](/documentation/code/classes/classgambit_1_1functor/)** <br>List of allowed model group combinations.  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/), std::set< [str](/documentation/code/namespaces/namespacegambit/) > > | **[modelGroups](/documentation/code/classes/classgambit_1_1functor/)** <br>Map from model group names to group contents.  |


## Detailed Description

```
template <typename TYPE >
class Gambit::module_functor;
```

Actual module functor type for all but TYPE=void. 
## Public Functions Documentation

### function module_functor

```
module_functor(
    void(*)(TYPE &) inputFunction,
    str func_name,
    str func_capability,
    str result_type,
    str origin_name,
    Models::ModelFunctorClaw & claw
)
```

Constructor. 

Class methods for actual module functors for TYPE != void. 


### function ~module_functor

```
virtual ~module_functor()
```

Destructor. 

### function setPrintRequirement

```
virtual void setPrintRequirement(
    bool flag
)
```

Setter for indicating if the wrapped function's result should to be printed. 

**Reimplements**: [Gambit::functor::setPrintRequirement](/documentation/code/classes/classgambit_1_1functor/)


Setter for indicating if the wrapped function's result should be printed. 


### function requiresPrinting

```
virtual bool requiresPrinting() const
```

Getter indicating if the wrapped function's result should to be printed. 

**Reimplements**: [Gambit::functor::requiresPrinting](/documentation/code/classes/classgambit_1_1functor/)


Getter indicating if the wrapped function's result should be printed. 


### function calculate

```
virtual void calculate()
```

Calculate method. 

**Reimplements**: [Gambit::functor::calculate](/documentation/code/classes/classgambit_1_1functor/)


Calculate method (no loop-manager stuff here because only void specialisation can manage loops) 


### function operator()

```
const TYPE & operator()(
    int index
)
```

Operation (return value) 

### function valuePtr

```
safe_ptr< TYPE > valuePtr()
```

Alternative to operation (returns a safe pointer to value) 

### function print

```
virtual void print(
    Printers::BasePrinter * printer,
    const int pointID,
    int index
)
```

Printer function. 

**Reimplements**: [Gambit::functor::print](/documentation/code/classes/classgambit_1_1functor/)


### function print

```
virtual void print(
    Printers::BasePrinter * printer,
    const int pointID
)
```

Printer function (no-thread-index short-circuit) 

**Reimplements**: [Gambit::functor::print](/documentation/code/classes/classgambit_1_1functor/)


## Protected Functions Documentation

### function init_memory

```
virtual void init_memory()
```

Initialise the memory of this functor. 

**Reimplements**: [Gambit::module_functor_common::init_memory](/documentation/code/classes/classgambit_1_1module__functor__common/)


## Protected Attributes Documentation

### variable myFunction

```
void(*)(TYPE &) myFunction;
```

Internal storage of function pointer. 

### variable myValue

```
TYPE * myValue;
```

Internal pointer to storage location of function value. 

### variable myPrintFlag

```
bool myPrintFlag;
```

Flag to select whether or not the results of this functor should be sent to the printer object. 

-------------------------------

Updated on 2022-09-08 at 01:05:16 +0000