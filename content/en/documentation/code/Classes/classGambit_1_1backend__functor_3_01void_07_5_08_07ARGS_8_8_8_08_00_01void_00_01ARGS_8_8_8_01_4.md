---
title: "class Gambit::backend_functor< void(*)(ARGS...), void, ARGS... >"
description: "Template specialisation for non-variadic, void backend functions. "

---

# class Gambit::backend_functor< void(*)(ARGS...), void, ARGS... >



Template specialisation for non-variadic, void backend functions.  [More...](#detailed-description)


`#include <functors.hpp>`

Inherits from [Gambit::backend_functor_common< void(*)(ARGS...), void, ARGS... >](/documentation/code/classes/classgambit_1_1backend__functor__common/), [Gambit::functor](/documentation/code/classes/classgambit_1_1functor/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[backend_functor](/documentation/code/classes/classgambit_1_1backend__functor_3_01void_07_5_08_07args_8_8_8_08_00_01void_00_01args_8_8_8_01_4/#function-backend-functor)**(void(*)(ARGS...) inputFunction, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) func_name, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) func_capability, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) result_type, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) origin_name, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) origin_version, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) safe_version, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) citation_key, [Models::ModelFunctorClaw](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/) & claw)<br>Constructor.  |
| virtual | **[~backend_functor](/documentation/code/classes/classgambit_1_1backend__functor_3_01void_07_5_08_07args_8_8_8_08_00_01void_00_01args_8_8_8_01_4/#function-backend-functor)**()<br>Destructor.  |
| void | **[operator()](/documentation/code/classes/classgambit_1_1backend__functor_3_01void_07_5_08_07args_8_8_8_08_00_01void_00_01args_8_8_8_01_4/#function-operator)**(ARGS &&... args)<br>Operation (execute function)  |

## Additional inherited members

**Protected Types inherited from [Gambit::backend_functor_common< void(*)(ARGS...), void, ARGS... >](/documentation/code/classes/classgambit_1_1backend__functor__common/)**

|                | Name           |
| -------------- | -------------- |
| typedef PTR_TYPE | **[funcPtrType](/documentation/code/classes/classgambit_1_1backend__functor__common/#typedef-funcptrtype)** <br>Type of the function pointer being encapsulated.  |

**Public Functions inherited from [Gambit::backend_functor_common< void(*)(ARGS...), void, ARGS... >](/documentation/code/classes/classgambit_1_1backend__functor__common/)**

|                | Name           |
| -------------- | -------------- |
| | **[backend_functor_common](/documentation/code/classes/classgambit_1_1backend__functor__common/#function-backend-functor-common)**([funcPtrType](/documentation/code/classes/classgambit_1_1backend__functor__common/#typedef-funcptrtype) inputFunction, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) func_name, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) func_capability, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) result_type, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) origin_name, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) origin_version, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) origin_safe_version, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) citation_key, [Models::ModelFunctorClaw](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/) & claw)<br>Constructor.  |
| virtual | **[~backend_functor_common](/documentation/code/classes/classgambit_1_1backend__functor__common/#function-backend-functor-common)**()<br>Destructor.  |
| void | **[updatePointer](/documentation/code/classes/classgambit_1_1backend__functor__common/#function-updatepointer)**([funcPtrType](/documentation/code/classes/classgambit_1_1backend__functor__common/#typedef-funcptrtype) inputFunction)<br>Update the internal function pointer wrapped by the functor.  |
| [funcPtrType](/documentation/code/classes/classgambit_1_1backend__functor__common/#typedef-funcptrtype) | **[handoutFunctionPointer](/documentation/code/classes/classgambit_1_1backend__functor__common/#function-handoutfunctionpointer)**()<br>Hand out the internal function pointer wrapped by the functor.  |
| [safe_ptr](/documentation/code/classes/classgambit_1_1safe__ptr/)< bool > | **[inUsePtr](/documentation/code/classes/classgambit_1_1backend__functor__common/#function-inuseptr)**()<br>Hand out a safe pointer to this backend functor's inUse flag.  |
| virtual [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[safe_version](/documentation/code/classes/classgambit_1_1backend__functor__common/#function-safe-version)**() const<br>Getter for the 'safe' incarnation of the version of the wrapped function's origin (module or backend)  |

**Protected Functions inherited from [Gambit::backend_functor_common< void(*)(ARGS...), void, ARGS... >](/documentation/code/classes/classgambit_1_1backend__functor__common/)**

|                | Name           |
| -------------- | -------------- |
| virtual void | **[setInUse](/documentation/code/classes/classgambit_1_1backend__functor__common/#function-setinuse)**(bool flag)<br>Set the inUse flag.  |

**Protected Attributes inherited from [Gambit::backend_functor_common< void(*)(ARGS...), void, ARGS... >](/documentation/code/classes/classgambit_1_1backend__functor__common/)**

|                | Name           |
| -------------- | -------------- |
| [funcPtrType](/documentation/code/classes/classgambit_1_1backend__functor__common/#typedef-funcptrtype) | **[myFunction](/documentation/code/classes/classgambit_1_1backend__functor__common/#variable-myfunction)** <br>Internal storage of function pointer.  |
| int | **[myLogTag](/documentation/code/classes/classgambit_1_1backend__functor__common/#variable-mylogtag)** <br>Integer LogTag, for tagging log messages.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[mySafeVersion](/documentation/code/classes/classgambit_1_1backend__functor__common/#variable-mysafeversion)** <br>Internal storage of the 'safe' version of the version (for use in namespaces, variable names, etc).  |
| bool | **[inUse](/documentation/code/classes/classgambit_1_1backend__functor__common/#variable-inuse)** <br>Flag indicating if this backend functor is actually in use in a given scan.  |

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


## Detailed Description

```
template <typename... ARGS>
class Gambit::backend_functor< void(*)(ARGS...), void, ARGS... >;
```

Template specialisation for non-variadic, void backend functions. 
## Public Functions Documentation

### function backend_functor

```
backend_functor(
    void(*)(ARGS...) inputFunction,
    str func_name,
    str func_capability,
    str result_type,
    str origin_name,
    str origin_version,
    str safe_version,
    str citation_key,
    Models::ModelFunctorClaw & claw
)
```

Constructor. 

### function ~backend_functor

```
inline virtual ~backend_functor()
```

Destructor. 

### function operator()

```
void operator()(
    ARGS &&... args
)
```

Operation (execute function) 

Operation (execute function and return value) 


-------------------------------

Updated on 2022-09-08 at 02:22:59 +0000