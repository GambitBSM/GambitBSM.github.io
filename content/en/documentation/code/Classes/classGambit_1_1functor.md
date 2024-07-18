---
title: "class Gambit::functor"
description: "Function wrapper (functor) base class. "

---

# class Gambit::functor



Function wrapper (functor) base class. 


`#include <functors.hpp>`

Inherited by [Gambit::backend_functor_common< TYPE(*)(ARGS...), TYPE, ARGS... >](/documentation/code/classes/classgambit_1_1backend__functor__common/), [Gambit::backend_functor_common< variadic_ptr< TYPE, ARGS... >::type, TYPE, ARGS... >](/documentation/code/classes/classgambit_1_1backend__functor__common/), [Gambit::backend_functor_common< variadic_ptr< void, ARGS... >::type, void, ARGS... >](/documentation/code/classes/classgambit_1_1backend__functor__common/), [Gambit::backend_functor_common< void(*)(ARGS...), void, ARGS... >](/documentation/code/classes/classgambit_1_1backend__functor__common/), [Gambit::backend_functor_common< PTR_TYPE, TYPE, ARGS >](/documentation/code/classes/classgambit_1_1backend__functor__common/), [Gambit::module_functor_common](/documentation/code/classes/classgambit_1_1module__functor__common/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual double | **[getRuntimeAverage](/documentation/code/classes/classgambit_1_1functor/#function-getruntimeaverage)**() |
| virtual double | **[getInvalidationRate](/documentation/code/classes/classgambit_1_1functor/#function-getinvalidationrate)**() |
| virtual void | **[setFadeRate](/documentation/code/classes/classgambit_1_1functor/#function-setfaderate)**(double ) |
| virtual void | **[notifyOfInvalidation](/documentation/code/classes/classgambit_1_1functor/#function-notifyofinvalidation)**(const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & ) |
| virtual void | **[reset](/documentation/code/classes/classgambit_1_1functor/#function-reset)**() |
| | **[functor](/documentation/code/classes/classgambit_1_1functor/#function-functor)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) func_name, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) func_capability, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) result_type, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) origin_name, [Models::ModelFunctorClaw](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/) & claw)<br>Constructor.  |
| virtual | **[~functor](/documentation/code/classes/classgambit_1_1functor/#function-functor)**()<br>Destructor.  |
| virtual void | **[calculate](/documentation/code/classes/classgambit_1_1functor/#function-calculate)**()<br>Virtual [calculate()](); needs to be redefined in daughters.  |
| virtual void | **[reset_and_calculate](/documentation/code/classes/classgambit_1_1functor/#function-reset-and-calculate)**()<br>Reset-then-recalculate method.  |
| void | **[setStatus](/documentation/code/classes/classgambit_1_1functor/#function-setstatus)**([FunctorStatus](/documentation/code/namespaces/namespacegambit/#enum-functorstatus) stat)<br>Setter for status.  |
| virtual void | **[setInUse](/documentation/code/classes/classgambit_1_1functor/#function-setinuse)**(bool )<br>Set the inUse flag (must be overridden in derived class to have any effect).  |
| void | **[setPurpose](/documentation/code/classes/classgambit_1_1functor/#function-setpurpose)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) purpose)<br>Setter for purpose (relevant only for next-to-output functors)  |
| void | **[setVertexID](/documentation/code/classes/classgambit_1_1functor/#function-setvertexid)**(int ID)<br>Setter for vertex ID (used in printer system)  |
| void | **[setTimingVertexID](/documentation/code/classes/classgambit_1_1functor/#function-settimingvertexid)**(int ID)<br>Set ID for timing 'vertex' (used in printer system)  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[name](/documentation/code/classes/classgambit_1_1functor/#function-name)**() const<br>Getter for the wrapped function's name.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[capability](/documentation/code/classes/classgambit_1_1functor/#function-capability)**() const<br>Getter for the wrapped function's reported capability.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[type](/documentation/code/classes/classgambit_1_1functor/#function-type)**() const<br>Getter for the wrapped function's reported return type.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[origin](/documentation/code/classes/classgambit_1_1functor/#function-origin)**() const<br>Getter for the wrapped function's origin (module or backend name)  |
| virtual [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[version](/documentation/code/classes/classgambit_1_1functor/#function-version)**() const<br>Getter for the version of the wrapped function's origin (module or backend)  |
| virtual [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[safe_version](/documentation/code/classes/classgambit_1_1functor/#function-safe-version)**() const<br>Getter for the 'safe' incarnation of the version of the wrapped function's origin (module or backend)  |
| [FunctorStatus](/documentation/code/namespaces/namespacegambit/#enum-functorstatus) | **[status](/documentation/code/classes/classgambit_1_1functor/#function-status)**() const<br>Getter for the functors current status.  |
| bool | **[isAvailable](/documentation/code/classes/classgambit_1_1functor/#function-isavailable)**() const<br>Checks whether the functor is available (or even already activated)  |
| bool | **[isActive](/documentation/code/classes/classgambit_1_1functor/#function-isactive)**() const<br>Checks whether the functor is active.  |
| bool | **[isDisabled](/documentation/code/classes/classgambit_1_1functor/#function-isdisabled)**() const<br>Checks whether the functor is disabled (discriminant is negative)  |
| bool | **[isEnabled](/documentation/code/classes/classgambit_1_1functor/#function-isenabled)**() const<br>Checks whether the functor is enabled (discriminant is non negative)  |
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
| virtual bool | **[needsLoopManager](/documentation/code/classes/classgambit_1_1functor/#function-needsloopmanager)**()<br>Getter for revealing whether this functor needs a loop manager.  |
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
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > | **[model_conditional_dependencies](/documentation/code/classes/classgambit_1_1functor/#function-model-conditional-dependencies)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) model)<br>Getter for listing model-specific conditional dependencies (matches also on parents and friends)  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > | **[model_conditional_dependencies_exact](/documentation/code/classes/classgambit_1_1functor/#function-model-conditional-dependencies-exact)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) model)<br>Getter for listing model-specific conditional dependencies (matches on the exact model)  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > | **[model_conditional_backend_reqs](/documentation/code/classes/classgambit_1_1functor/#function-model-conditional-backend-reqs)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) model)<br>Getter for listing model-specific conditional backend requirements (matches also on parents and friends)  |
| virtual std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > | **[model_conditional_backend_reqs_exact](/documentation/code/classes/classgambit_1_1functor/#function-model-conditional-backend-reqs-exact)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) model)<br>Getter for listing model-specific conditional backend requirements (matches on the exact model)  |
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
| const std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > & | **[getAllowedModels](/documentation/code/classes/classgambit_1_1functor/#function-getallowedmodels)**()<br>Getter for listing allowed models.  |
| const std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > & | **[getConditionalModels](/documentation/code/classes/classgambit_1_1functor/#function-getconditionalmodels)**()<br>Getter for listing conditional models.  |
| const std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > > & | **[getModelGroups](/documentation/code/classes/classgambit_1_1functor/#function-getmodelgroups)**()<br>Getter for map of model groups and the set of models in each group.  |
| bool | **[allModelsAllowed](/documentation/code/classes/classgambit_1_1functor/#function-allmodelsallowed)**()<br>Test whether the functor is allowed to be used with all models.  |
| bool | **[modelAllowed](/documentation/code/classes/classgambit_1_1functor/#function-modelallowed)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) model)<br>Test whether the functor is always allowed (either explicitly or implicitly) to be used with a given model.  |
| bool | **[modelExplicitlyAllowed](/documentation/code/classes/classgambit_1_1functor/#function-modelexplicitlyallowed)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) model)<br>Test whether the functor is explictly always allowed to be used with a given model.  |
| void | **[setAllowedModel](/documentation/code/classes/classgambit_1_1functor/#function-setallowedmodel)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) model)<br>Add a model to the internal list of models for which this functor is allowed to be used.  |
| bool | **[modelComboAllowed](/documentation/code/classes/classgambit_1_1functor/#function-modelcomboallowed)**(std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > combo)<br>Test whether the functor is allowed (either explicitly or implicitly) to be used with a given combination of models.  |
| bool | **[modelComboExplicitlyAllowed](/documentation/code/classes/classgambit_1_1functor/#function-modelcomboexplicitlyallowed)**(std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > combo)<br>Test whether the functor has been explictly allowed to be used with a given combination of models.  |
| void | **[setModelGroup](/documentation/code/classes/classgambit_1_1functor/#function-setmodelgroup)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) group, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) contents)<br>Add a model group definition to the internal list of model groups.  |
| void | **[setAllowedModelGroupCombo](/documentation/code/classes/classgambit_1_1functor/#function-setallowedmodelgroupcombo)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) groups)<br>Add a combination of model groups to the internal list of combinations for which this functor is allowed to be used.  |
| void | **[addMatchedObservable](/documentation/code/classes/classgambit_1_1functor/#function-addmatchedobservable)**(const [DRes::Observable](/documentation/code/classes/structgambit_1_1dres_1_1observable/) * obs)<br>Add an observable to the set of those that this functor matches.  |
| const std::set< const [DRes::Observable](/documentation/code/classes/structgambit_1_1dres_1_1observable/) * > & | **[getMatchedObservables](/documentation/code/classes/classgambit_1_1functor/#function-getmatchedobservables)**()<br>Retrieve the set of observables that this functor matches.  |
| void | **[addMatchedModuleRule](/documentation/code/classes/classgambit_1_1functor/#function-addmatchedmodulerule)**(const [DRes::ModuleRule](/documentation/code/classes/structgambit_1_1dres_1_1modulerule/) * r)<br>Add a module rule to the set of those against which this functor has been tested and found to match.  |
| void | **[addMatchedBackendRule](/documentation/code/classes/classgambit_1_1functor/#function-addmatchedbackendrule)**(const [DRes::BackendRule](/documentation/code/classes/structgambit_1_1dres_1_1backendrule/) * r)<br>Add a backend rule to the set of those against which this functor has been tested and found to match.  |
| const std::set< const [DRes::ModuleRule](/documentation/code/classes/structgambit_1_1dres_1_1modulerule/) * > & | **[getMatchedModuleRules](/documentation/code/classes/classgambit_1_1functor/#function-getmatchedmodulerules)**()<br>Retrieve the set of module rules against which this functor has been tested and found to match.  |
| const std::set< const [DRes::BackendRule](/documentation/code/classes/structgambit_1_1dres_1_1backendrule/) * > & | **[getMatchedBackendRules](/documentation/code/classes/classgambit_1_1functor/#function-getmatchedbackendrules)**()<br>Retrieve the set of backend rules against which this functor has been tested and found to match.  |
| template <class RuleT \> <br>const std::set< RuleT * > & | **[getMatchedRules](/documentation/code/classes/classgambit_1_1functor/#function-getmatchedrules)**()<br>Retrieve matched rules by type.  |
| const std::set< const [DRes::ModuleRule](/documentation/code/classes/structgambit_1_1dres_1_1modulerule/) * > & | **[getMatchedRules](/documentation/code/classes/classgambit_1_1functor/#function-getmatchedrules)**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| virtual void | **[reset](/documentation/code/classes/classgambit_1_1functor/#function-reset)**(int )<br>Reset functor for one thread only.  |
| void | **[failBigTime](/documentation/code/classes/classgambit_1_1functor/#function-failbigtime)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) method)<br>Attempt to retrieve a dependency or model parameter that has not been resolved.  |
| bool | **[allowed_parent_or_friend_exists](/documentation/code/classes/classgambit_1_1functor/#function-allowed-parent-or-friend-exists)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) model)<br>Test if there is a model in the functor's allowedModels list as which this model can be interpreted.  |
| bool | **[in_allowed_combo](/documentation/code/classes/classgambit_1_1functor/#function-in-allowed-combo)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) model)<br>Check that a model is actually part of a combination that is allowed to be used with this functor.  |
| bool | **[contains_anything_interpretable_as_member_of](/documentation/code/classes/classgambit_1_1functor/#function-contains-anything-interpretable-as-member-of)**(std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > combo, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) group)<br>Test whether any of the entries in a given model group is a valid interpretation of any members in a given combination.  |
| bool | **[has_common_elements](/documentation/code/classes/classgambit_1_1functor/#function-has-common-elements)**(std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > combo, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) group)<br>Work out whether a given combination of models and a model group have any elements in common.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[find_friend_or_parent_model_in_map](/documentation/code/classes/classgambit_1_1functor/#function-find-friend-or-parent-model-in-map)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) model, std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > > karta)<br>Try to find a parent or friend model in some user-supplied map from models to sspair vectors.  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[myName](/documentation/code/classes/classgambit_1_1functor/#variable-myname)** <br>Internal storage of the function name.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[myCapability](/documentation/code/classes/classgambit_1_1functor/#variable-mycapability)** <br>Internal storage of exactly what the function calculates.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[myType](/documentation/code/classes/classgambit_1_1functor/#variable-mytype)** <br>Internal storage of the type of what the function calculates.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[myOrigin](/documentation/code/classes/classgambit_1_1functor/#variable-myorigin)** <br>Internal storage of the name of the module or backend to which the function belongs.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[myPurpose](/documentation/code/classes/classgambit_1_1functor/#variable-mypurpose)** <br>Purpose of the function (relevant for output and next-to-output functors)  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[myCitationKey](/documentation/code/classes/classgambit_1_1functor/#variable-mycitationkey)** <br>Citation key: BibTex key of the reference.  |
| const [Models::ModelFunctorClaw](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/) * | **[myClaw](/documentation/code/classes/classgambit_1_1functor/#variable-myclaw)** <br>Bound model functor claw, for checking relationships between models.  |
| const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[myLabel](/documentation/code/classes/classgambit_1_1functor/#variable-mylabel)** <br>String label, used to label functor results for printer system.  |
| const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[myTimingLabel](/documentation/code/classes/classgambit_1_1functor/#variable-mytiminglabel)** <br>String label, used to label functor timing data for printer system.  |
| [FunctorStatus](/documentation/code/namespaces/namespacegambit/#enum-functorstatus) | **[myStatus](/documentation/code/classes/classgambit_1_1functor/#variable-mystatus)** <br>Status:  |
| int | **[myVertexID](/documentation/code/classes/classgambit_1_1functor/#variable-myvertexid)** <br>Internal storage of the vertex ID number used by the printer system to identify functors.  |
| int | **[myTimingVertexID](/documentation/code/classes/classgambit_1_1functor/#variable-mytimingvertexid)** <br>ID assigned by printers to the timing data output stream.  |
| bool | **[verbose](/documentation/code/classes/classgambit_1_1functor/#variable-verbose)** <br>Debug flag.  |
| [Options](/documentation/code/classes/classgambit_1_1options/) | **[myOptions](/documentation/code/classes/classgambit_1_1functor/#variable-myoptions)** <br>Internal storage of function options, as a [YAML](/documentation/code/namespaces/namespaceyaml/) node.  |
| [Options](/documentation/code/classes/classgambit_1_1options/) | **[mySubCaps](/documentation/code/classes/classgambit_1_1functor/#variable-mysubcaps)** <br>Internal storage of function sub-capabilities, as a [YAML](/documentation/code/namespaces/namespaceyaml/) node.  |
| std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > | **[myDependees](/documentation/code/classes/classgambit_1_1functor/#variable-mydependees)** <br>List of all capability,type pairs of functors downstream of this one in the dependency tree.  |
| std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > | **[allowedModels](/documentation/code/classes/classgambit_1_1functor/#variable-allowedmodels)** <br>List of allowed models.  |
| std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > | **[conditionalModels](/documentation/code/classes/classgambit_1_1functor/#variable-conditionalmodels)** <br>List of conditional models.  |
| std::set< std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > > | **[allowedGroupCombos](/documentation/code/classes/classgambit_1_1functor/#variable-allowedgroupcombos)** <br>List of allowed model group combinations.  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), std::set< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > > | **[modelGroups](/documentation/code/classes/classgambit_1_1functor/#variable-modelgroups)** <br>Map from model group names to group contents.  |
| std::set< const [DRes::Observable](/documentation/code/classes/structgambit_1_1dres_1_1observable/) * > | **[matched_observables](/documentation/code/classes/classgambit_1_1functor/#variable-matched-observables)** <br>The set of observables that this functor matches.  |
| std::set< const [DRes::ModuleRule](/documentation/code/classes/structgambit_1_1dres_1_1modulerule/) * > | **[matched_module_rules](/documentation/code/classes/classgambit_1_1functor/#variable-matched-module-rules)** <br>Set of module rules against which this functor has been tested and found to match.  |
| std::set< const [DRes::BackendRule](/documentation/code/classes/structgambit_1_1dres_1_1backendrule/) * > | **[matched_backend_rules](/documentation/code/classes/classgambit_1_1functor/#variable-matched-backend-rules)** <br>Set of backend rules against which this functor has been tested and found to match.  |

## Public Functions Documentation

### function getRuntimeAverage

```
virtual double getRuntimeAverage()
```


**Reimplemented by**: [Gambit::module_functor_common::getRuntimeAverage](/documentation/code/classes/classgambit_1_1module__functor__common/#function-getruntimeaverage)


Interfaces for runtime optimization Need to be implemented by daughters 


### function getInvalidationRate

```
virtual double getInvalidationRate()
```


**Reimplemented by**: [Gambit::module_functor_common::getInvalidationRate](/documentation/code/classes/classgambit_1_1module__functor__common/#function-getinvalidationrate)


### function setFadeRate

```
virtual void setFadeRate(
    double 
)
```


**Reimplemented by**: [Gambit::module_functor_common::setFadeRate](/documentation/code/classes/classgambit_1_1module__functor__common/#function-setfaderate)


### function notifyOfInvalidation

```
virtual void notifyOfInvalidation(
    const str & 
)
```


**Reimplemented by**: [Gambit::module_functor_common::notifyOfInvalidation](/documentation/code/classes/classgambit_1_1module__functor__common/#function-notifyofinvalidation)


### function reset

```
virtual void reset()
```


**Reimplemented by**: [Gambit::module_functor_common::reset](/documentation/code/classes/classgambit_1_1module__functor__common/#function-reset)


### function functor

```
functor(
    str func_name,
    str func_capability,
    str result_type,
    str origin_name,
    Models::ModelFunctorClaw & claw
)
```

Constructor. 

### function ~functor

```
inline virtual ~functor()
```

Destructor. 

### function calculate

```
virtual void calculate()
```

Virtual [calculate()](); needs to be redefined in daughters. 

**Reimplemented by**: [Gambit::module_functor::calculate](/documentation/code/classes/classgambit_1_1module__functor/#function-calculate), [Gambit::module_functor::calculate](/documentation/code/classes/classgambit_1_1module__functor/#function-calculate), [Gambit::module_functor< void >::calculate](/documentation/code/classes/classgambit_1_1module__functor_3_01void_01_4/#function-calculate)


### function reset_and_calculate

```
virtual void reset_and_calculate()
```

Reset-then-recalculate method. 

### function setStatus

```
void setStatus(
    FunctorStatus stat
)
```

Setter for status. 

### function setInUse

```
inline virtual void setInUse(
    bool 
)
```

Set the inUse flag (must be overridden in derived class to have any effect). 

**Reimplemented by**: [Gambit::backend_functor_common::setInUse](/documentation/code/classes/classgambit_1_1backend__functor__common/#function-setinuse), [Gambit::backend_functor_common::setInUse](/documentation/code/classes/classgambit_1_1backend__functor__common/#function-setinuse), [Gambit::backend_functor_common::setInUse](/documentation/code/classes/classgambit_1_1backend__functor__common/#function-setinuse), [Gambit::backend_functor_common::setInUse](/documentation/code/classes/classgambit_1_1backend__functor__common/#function-setinuse), [Gambit::backend_functor_common::setInUse](/documentation/code/classes/classgambit_1_1backend__functor__common/#function-setinuse)


### function setPurpose

```
void setPurpose(
    str purpose
)
```

Setter for purpose (relevant only for next-to-output functors) 

### function setVertexID

```
void setVertexID(
    int ID
)
```

Setter for vertex ID (used in printer system) 

### function setTimingVertexID

```
void setTimingVertexID(
    int ID
)
```

Set ID for timing 'vertex' (used in printer system) 

Acquire ID for timing 'vertex' (used in printer system) 


### function name

```
str name() const
```

Getter for the wrapped function's name. 

### function capability

```
str capability() const
```

Getter for the wrapped function's reported capability. 

### function type

```
str type() const
```

Getter for the wrapped function's reported return type. 

### function origin

```
str origin() const
```

Getter for the wrapped function's origin (module or backend name) 

### function version

```
virtual str version() const
```

Getter for the version of the wrapped function's origin (module or backend) 

**Reimplemented by**: [Gambit::backend_functor_common::version](/documentation/code/classes/classgambit_1_1backend__functor__common/#function-version), [Gambit::backend_functor_common::version](/documentation/code/classes/classgambit_1_1backend__functor__common/#function-version), [Gambit::backend_functor_common::version](/documentation/code/classes/classgambit_1_1backend__functor__common/#function-version), [Gambit::backend_functor_common::version](/documentation/code/classes/classgambit_1_1backend__functor__common/#function-version), [Gambit::backend_functor_common::version](/documentation/code/classes/classgambit_1_1backend__functor__common/#function-version)


### function safe_version

```
virtual str safe_version() const
```

Getter for the 'safe' incarnation of the version of the wrapped function's origin (module or backend) 

**Reimplemented by**: [Gambit::backend_functor_common::safe_version](/documentation/code/classes/classgambit_1_1backend__functor__common/#function-safe-version), [Gambit::backend_functor_common::safe_version](/documentation/code/classes/classgambit_1_1backend__functor__common/#function-safe-version), [Gambit::backend_functor_common::safe_version](/documentation/code/classes/classgambit_1_1backend__functor__common/#function-safe-version), [Gambit::backend_functor_common::safe_version](/documentation/code/classes/classgambit_1_1backend__functor__common/#function-safe-version), [Gambit::backend_functor_common::safe_version](/documentation/code/classes/classgambit_1_1backend__functor__common/#function-safe-version)


### function status

```
FunctorStatus status() const
```

Getter for the functors current status. 

### function isAvailable

```
bool isAvailable() const
```

Checks whether the functor is available (or even already activated) 

Checks whether the functor is available (or even already activate) 


### function isActive

```
bool isActive() const
```

Checks whether the functor is active. 

Checks whether the functor is active (or even hyperactive) 


### function isDisabled

```
bool isDisabled() const
```

Checks whether the functor is disabled (discriminant is negative) 

### function isEnabled

```
bool isEnabled() const
```

Checks whether the functor is enabled (discriminant is non negative) 

### function quantity

```
sspair quantity() const
```

Getter for the overall quantity provided by the wrapped function (capability-type pair) 

### function purpose

```
str purpose() const
```

Getter for purpose (relevant for output nodes, aka helper structures for the dep. resolution) 

### function citationKey

```
str citationKey() const
```

Getter for the citation key. 

Getter for citation key. 


### function vertexID

```
int vertexID() const
```

Getter for vertex ID. 

### function timingVertexID

```
int timingVertexID() const
```

Getter for timing vertex ID. 

### function label

```
str label() const
```

Getter for string label. 

Getter for the printer label. 


### function timingLabel

```
str timingLabel() const
```

Getter for the printer timing label. 

### function requiresPrinting

```
virtual bool requiresPrinting() const
```

Getter indicating if the wrapped function's result should to be printed. 

**Reimplemented by**: [Gambit::module_functor::requiresPrinting](/documentation/code/classes/classgambit_1_1module__functor/#function-requiresprinting), [Gambit::module_functor::requiresPrinting](/documentation/code/classes/classgambit_1_1module__functor/#function-requiresprinting)


### function requiresTimingPrinting

```
virtual bool requiresTimingPrinting() const
```

Getter indicating if the timing data for this function's execution should be printed. 

**Reimplemented by**: [Gambit::module_functor_common::requiresTimingPrinting](/documentation/code/classes/classgambit_1_1module__functor__common/#function-requirestimingprinting)


### function setPrintRequirement

```
virtual void setPrintRequirement(
    bool flag
)
```

Setter for indicating if the wrapped function's result should to be printed. 

**Reimplemented by**: [Gambit::module_functor::setPrintRequirement](/documentation/code/classes/classgambit_1_1module__functor/#function-setprintrequirement), [Gambit::module_functor::setPrintRequirement](/documentation/code/classes/classgambit_1_1module__functor/#function-setprintrequirement)


### function setTimingPrintRequirement

```
virtual void setTimingPrintRequirement(
    bool flag
)
```

Setter for indicating if the timing data for this function's execution should be printed. 

**Reimplemented by**: [Gambit::module_functor_common::setTimingPrintRequirement](/documentation/code/classes/classgambit_1_1module__functor__common/#function-settimingprintrequirement)


Setter for indicating if the timing data for this functor should be printed. 


### function setNestedList

```
virtual void setNestedList(
    std::vector< functor * > & 
)
```

Set the ordered list of pointers to other functors that should run nested in a loop managed by this one. 

**Reimplemented by**: [Gambit::module_functor_common::setNestedList](/documentation/code/classes/classgambit_1_1module__functor__common/#function-setnestedlist)


### function setIteration

```
virtual void setIteration(
    long long 
)
```

Set the iteration number in a loop in which this functor runs. 

**Reimplemented by**: [Gambit::module_functor_common::setIteration](/documentation/code/classes/classgambit_1_1module__functor__common/#function-setiteration)


### function canBeLoopManager

```
virtual bool canBeLoopManager()
```

Getter for revealing whether this is permitted to be a manager functor. 

**Reimplemented by**: [Gambit::module_functor_common::canBeLoopManager](/documentation/code/classes/classgambit_1_1module__functor__common/#function-canbeloopmanager)


### function needsLoopManager

```
virtual bool needsLoopManager()
```

Getter for revealing whether this functor needs a loop manager. 

**Reimplemented by**: [Gambit::module_functor_common::needsLoopManager](/documentation/code/classes/classgambit_1_1module__functor__common/#function-needsloopmanager)


### function loopManagerCapability

```
virtual str loopManagerCapability()
```

Getter for revealing the required capability of the wrapped function's loop manager. 

**Reimplemented by**: [Gambit::module_functor_common::loopManagerCapability](/documentation/code/classes/classgambit_1_1module__functor__common/#function-loopmanagercapability)


### function loopManagerType

```
virtual str loopManagerType()
```

Getter for revealing the required type of the wrapped function's loop manager. 

**Reimplemented by**: [Gambit::module_functor_common::loopManagerType](/documentation/code/classes/classgambit_1_1module__functor__common/#function-loopmanagertype)


### function loopManagerName

```
virtual str loopManagerName()
```

Getter for revealing the name of the wrapped function's assigned loop manager. 

**Reimplemented by**: [Gambit::module_functor_common::loopManagerName](/documentation/code/classes/classgambit_1_1module__functor__common/#function-loopmanagername)


### function loopManagerOrigin

```
virtual str loopManagerOrigin()
```

Getter for revealing the module of the wrapped function's assigned loop manager. 

**Reimplemented by**: [Gambit::module_functor_common::loopManagerOrigin](/documentation/code/classes/classgambit_1_1module__functor__common/#function-loopmanagerorigin)


### function breakLoop

```
virtual void breakLoop()
```

Tell the functor that the loop it manages should break now. 

**Reimplemented by**: [Gambit::module_functor_common::breakLoop](/documentation/code/classes/classgambit_1_1module__functor__common/#function-breakloop)


### function dependencies

```
virtual std::set< sspair > dependencies()
```

Getter for listing currently activated dependencies. 

**Reimplemented by**: [Gambit::module_functor_common::dependencies](/documentation/code/classes/classgambit_1_1module__functor__common/#function-dependencies)


### function backendclassloading

```
virtual std::set< sspair > backendclassloading()
```

Getter for listing backends that require class loading. 

**Reimplemented by**: [Gambit::module_functor_common::backendclassloading](/documentation/code/classes/classgambit_1_1module__functor__common/#function-backendclassloading)


### function backendgroups

```
virtual std::set< str > backendgroups()
```

Getter for listing backend requirement groups. 

**Reimplemented by**: [Gambit::module_functor_common::backendgroups](/documentation/code/classes/classgambit_1_1module__functor__common/#function-backendgroups)


### function backendreqs

```
virtual std::set< sspair > backendreqs()
```

Getter for listing all backend requirements. 

**Reimplemented by**: [Gambit::module_functor_common::backendreqs](/documentation/code/classes/classgambit_1_1module__functor__common/#function-backendreqs)


### function backendreqs

```
virtual std::set< sspair > backendreqs(
    str 
)
```

Getter for listing backend requirements from a specific group. 

**Reimplemented by**: [Gambit::module_functor_common::backendreqs](/documentation/code/classes/classgambit_1_1module__functor__common/#function-backendreqs)


### function backendspermitted

```
virtual std::set< sspair > backendspermitted(
    sspair 
)
```

Getter for listing permitted backends. 

**Reimplemented by**: [Gambit::module_functor_common::backendspermitted](/documentation/code/classes/classgambit_1_1module__functor__common/#function-backendspermitted)


### function backendreq_tags

```
virtual std::set< str > backendreq_tags(
    sspair 
)
```

Getter for listing tags associated with backend requirements. 

**Reimplemented by**: [Gambit::module_functor_common::backendreq_tags](/documentation/code/classes/classgambit_1_1module__functor__common/#function-backendreq-tags)


### function forcematchingbackend

```
virtual std::set< sspair > forcematchingbackend(
    str 
)
```

Getter for listing backend requirements that must be resolved from the same backend. 

**Reimplemented by**: [Gambit::module_functor_common::forcematchingbackend](/documentation/code/classes/classgambit_1_1module__functor__common/#function-forcematchingbackend)


### function backend_conditional_dependencies

```
virtual std::set< sspair > backend_conditional_dependencies(
    str ,
    str ,
    str ,
    str 
)
```

Getter for listing backend-specific conditional dependencies (4-string version) 

**Reimplemented by**: [Gambit::module_functor_common::backend_conditional_dependencies](/documentation/code/classes/classgambit_1_1module__functor__common/#function-backend-conditional-dependencies)


### function backend_conditional_dependencies

```
virtual std::set< sspair > backend_conditional_dependencies(
    str req,
    str type,
    str be
)
```

Getter for backend-specific conditional dependencies (3-string version) 

**Reimplemented by**: [Gambit::module_functor_common::backend_conditional_dependencies](/documentation/code/classes/classgambit_1_1module__functor__common/#function-backend-conditional-dependencies)


### function backend_conditional_dependencies

```
virtual std::set< sspair > backend_conditional_dependencies(
    functor * be_functor
)
```

Getter for backend-specific conditional dependencies (backend functor pointer version) 

**Reimplemented by**: [Gambit::module_functor_common::backend_conditional_dependencies](/documentation/code/classes/classgambit_1_1module__functor__common/#function-backend-conditional-dependencies)


### function model_conditional_dependencies

```
virtual std::set< sspair > model_conditional_dependencies(
    str model
)
```

Getter for listing model-specific conditional dependencies (matches also on parents and friends) 

**Reimplemented by**: [Gambit::module_functor_common::model_conditional_dependencies](/documentation/code/classes/classgambit_1_1module__functor__common/#function-model-conditional-dependencies)


### function model_conditional_dependencies_exact

```
virtual std::set< sspair > model_conditional_dependencies_exact(
    str model
)
```

Getter for listing model-specific conditional dependencies (matches on the exact model) 

**Reimplemented by**: [Gambit::module_functor_common::model_conditional_dependencies_exact](/documentation/code/classes/classgambit_1_1module__functor__common/#function-model-conditional-dependencies-exact)


### function model_conditional_backend_reqs

```
virtual std::set< sspair > model_conditional_backend_reqs(
    str model
)
```

Getter for listing model-specific conditional backend requirements (matches also on parents and friends) 

**Reimplemented by**: [Gambit::module_functor_common::model_conditional_backend_reqs](/documentation/code/classes/classgambit_1_1module__functor__common/#function-model-conditional-backend-reqs)


### function model_conditional_backend_reqs_exact

```
virtual std::set< sspair > model_conditional_backend_reqs_exact(
    str model
)
```

Getter for listing model-specific conditional backend requirements (matches on the exact model) 

**Reimplemented by**: [Gambit::module_functor_common::model_conditional_backend_reqs_exact](/documentation/code/classes/classgambit_1_1module__functor__common/#function-model-conditional-backend-reqs-exact)


### function resolveDependency

```
virtual void resolveDependency(
    functor * 
)
```

Resolve a dependency using a pointer to another functor object. 

**Reimplemented by**: [Gambit::module_functor_common::resolveDependency](/documentation/code/classes/classgambit_1_1module__functor__common/#function-resolvedependency)


### function resolveLoopManager

```
virtual void resolveLoopManager(
    functor * 
)
```

Set this functor's loop manager (if it has one) 

**Reimplemented by**: [Gambit::module_functor_common::resolveLoopManager](/documentation/code/classes/classgambit_1_1module__functor__common/#function-resolveloopmanager)


### function resolveBackendReq

```
virtual void resolveBackendReq(
    functor * 
)
```

Resolve a backend requirement using a pointer to another functor object. 

**Reimplemented by**: [Gambit::module_functor_common::resolveBackendReq](/documentation/code/classes/classgambit_1_1module__functor__common/#function-resolvebackendreq)


### function notifyOfModel

```
virtual void notifyOfModel(
    str 
)
```

Notify the functor that a certain model is being scanned, so that it can activate itself accordingly. 

**Reimplemented by**: [Gambit::module_functor_common::notifyOfModel](/documentation/code/classes/classgambit_1_1module__functor__common/#function-notifyofmodel)


Notify the functor that a certain model is being scanned, so that it can activate its dependencies accordingly. 


### function notifyOfDependee

```
virtual void notifyOfDependee(
    functor * 
)
```

Notify the functor that it is being used to fill a dependency of another functor. 

**Reimplemented by**: [Gambit::module_functor_common::notifyOfDependee](/documentation/code/classes/classgambit_1_1module__functor__common/#function-notifyofdependee)


### function notifyOfBackends

```
virtual void notifyOfBackends(
    std::map< str, std::set< str > > 
)
```

Indicate to the functor which backends are actually loaded and working. 

**Reimplemented by**: [Gambit::module_functor_common::notifyOfBackends](/documentation/code/classes/classgambit_1_1module__functor__common/#function-notifyofbackends)


### function print

```
virtual void print(
    Printers::BasePrinter * printer,
    const int pointID,
    int thread_num
)
```

Printer function. 

**Reimplemented by**: [Gambit::module_functor< void >::print](/documentation/code/classes/classgambit_1_1module__functor_3_01void_01_4/#function-print), [Gambit::module_functor::print](/documentation/code/classes/classgambit_1_1module__functor/#function-print), [Gambit::module_functor::print](/documentation/code/classes/classgambit_1_1module__functor/#function-print)


Print function. 


### function print

```
virtual void print(
    Printers::BasePrinter * printer,
    const int pointID
)
```

Printer function (no-thread-index short-circuit) 

**Reimplemented by**: [Gambit::module_functor< void >::print](/documentation/code/classes/classgambit_1_1module__functor_3_01void_01_4/#function-print), [Gambit::module_functor::print](/documentation/code/classes/classgambit_1_1module__functor/#function-print), [Gambit::module_functor::print](/documentation/code/classes/classgambit_1_1module__functor/#function-print)


### function retrieve_invalid_point_exception

```
virtual invalid_point_exception * retrieve_invalid_point_exception()
```

Retrieve the previously saved exception generated when this functor invalidated the current point in model space. 

**Reimplemented by**: [Gambit::module_functor_common::retrieve_invalid_point_exception](/documentation/code/classes/classgambit_1_1module__functor__common/#function-retrieve-invalid-point-exception)


### function notifyOfIniOptions

```
void notifyOfIniOptions(
    const Options & opt
)
```


Notify the functor about an instance of the options class that contains information from its corresponding ini-file entry in the auxiliaries or observables section. 


### function setOption

```
template <typename TYPE >
inline void setOption(
    const str & key,
    const TYPE val
)
```

Set an option for the functor directly (for use in standalone executables). 

### function getOptions

```
safe_ptr< Options > getOptions()
```

Return a safe pointer to the options that this functor is supposed to run with (e.g. from the ini file). 

### function notifyOfSubCaps

```
void notifyOfSubCaps(
    const str & subcap_string
)
```

Notify the functor about a string in [YAML](/documentation/code/namespaces/namespaceyaml/) that contains the sub-capability information (for use in standalones) 

### function notifyOfSubCaps

```
void notifyOfSubCaps(
    const Options & subcaps
)
```

Notify the functor about an instance of the options class that contains sub-capability information. 

### function setSubCap

```
template <typename TYPE >
inline void setSubCap(
    const str & key,
    const TYPE val
)
```

Set a sub-capability (subcap)for the functor directly (for use in standalone executables). 

### function getSubCaps

```
safe_ptr< Options > getSubCaps()
```

Return a safe pointer to the subcaps that this functor realises it is supposed to facilitate downstream calculation of. 

### function getDependees

```
safe_ptr< std::set< sspair > > getDependees()
```

Return a safe pointer to the vector of all capability,type pairs of functors arranged downstream of this one in the dependency tree. 

### function getAllowedModels

```
const std::set< str > & getAllowedModels()
```

Getter for listing allowed models. 

### function getConditionalModels

```
const std::set< str > & getConditionalModels()
```

Getter for listing conditional models. 

### function getModelGroups

```
const std::map< str, std::set< str > > & getModelGroups()
```

Getter for map of model groups and the set of models in each group. 

### function allModelsAllowed

```
bool allModelsAllowed()
```

Test whether the functor is allowed to be used with all models. 

### function modelAllowed

```
bool modelAllowed(
    str model
)
```

Test whether the functor is always allowed (either explicitly or implicitly) to be used with a given model. 

Test whether the functor is allowed (either explicitly or implicitly) to be used with a given model. 


### function modelExplicitlyAllowed

```
bool modelExplicitlyAllowed(
    str model
)
```

Test whether the functor is explictly always allowed to be used with a given model. 

Test whether the functor has been explictly allowed to be used with a given model. 


### function setAllowedModel

```
void setAllowedModel(
    str model
)
```

Add a model to the internal list of models for which this functor is allowed to be used. 

### function modelComboAllowed

```
bool modelComboAllowed(
    std::set< str > combo
)
```

Test whether the functor is allowed (either explicitly or implicitly) to be used with a given combination of models. 

### function modelComboExplicitlyAllowed

```
bool modelComboExplicitlyAllowed(
    std::set< str > combo
)
```

Test whether the functor has been explictly allowed to be used with a given combination of models. 

### function setModelGroup

```
void setModelGroup(
    str group,
    str contents
)
```

Add a model group definition to the internal list of model groups. 

### function setAllowedModelGroupCombo

```
void setAllowedModelGroupCombo(
    str groups
)
```

Add a combination of model groups to the internal list of combinations for which this functor is allowed to be used. 

Add a model group combination to the internal list of combinations for which this functor is allowed to be used. 


### function addMatchedObservable

```
void addMatchedObservable(
    const DRes::Observable * obs
)
```

Add an observable to the set of those that this functor matches. 

### function getMatchedObservables

```
const std::set< const DRes::Observable * > & getMatchedObservables()
```

Retrieve the set of observables that this functor matches. 

### function addMatchedModuleRule

```
void addMatchedModuleRule(
    const DRes::ModuleRule * r
)
```

Add a module rule to the set of those against which this functor has been tested and found to match. 

### function addMatchedBackendRule

```
void addMatchedBackendRule(
    const DRes::BackendRule * r
)
```

Add a backend rule to the set of those against which this functor has been tested and found to match. 

### function getMatchedModuleRules

```
const std::set< const DRes::ModuleRule * > & getMatchedModuleRules()
```

Retrieve the set of module rules against which this functor has been tested and found to match. 

### function getMatchedBackendRules

```
const std::set< const DRes::BackendRule * > & getMatchedBackendRules()
```

Retrieve the set of backend rules against which this functor has been tested and found to match. 

### function getMatchedRules

```
template <class RuleT >
const std::set< RuleT * > & getMatchedRules()
```

Retrieve matched rules by type. 

### function getMatchedRules

```
const std::set< const DRes::ModuleRule * > & getMatchedRules()
```


## Protected Functions Documentation

### function reset

```
virtual void reset(
    int 
)
```

Reset functor for one thread only. 

**Reimplemented by**: [Gambit::module_functor_common::reset](/documentation/code/classes/classgambit_1_1module__functor__common/#function-reset)


### function failBigTime

```
static void failBigTime(
    str method
)
```

Attempt to retrieve a dependency or model parameter that has not been resolved. 

### function allowed_parent_or_friend_exists

```
inline bool allowed_parent_or_friend_exists(
    str model
)
```

Test if there is a model in the functor's allowedModels list as which this model can be interpreted. 

### function in_allowed_combo

```
inline bool in_allowed_combo(
    str model
)
```

Check that a model is actually part of a combination that is allowed to be used with this functor. 

### function contains_anything_interpretable_as_member_of

```
inline bool contains_anything_interpretable_as_member_of(
    std::set< str > combo,
    str group
)
```

Test whether any of the entries in a given model group is a valid interpretation of any members in a given combination. 

### function has_common_elements

```
inline bool has_common_elements(
    std::set< str > combo,
    str group
)
```

Work out whether a given combination of models and a model group have any elements in common. 

### function find_friend_or_parent_model_in_map

```
str find_friend_or_parent_model_in_map(
    str model,
    std::map< str, std::set< sspair > > karta
)
```

Try to find a parent or friend model in some user-supplied map from models to sspair vectors. 

Try to find a parent or friend model in some user-supplied map from models to sspair vectors Preferentially returns the 'least removed' parent or friend, i.e. less steps back in the model lineage. 


## Protected Attributes Documentation

### variable myName

```
str myName;
```

Internal storage of the function name. 

### variable myCapability

```
str myCapability;
```

Internal storage of exactly what the function calculates. 

### variable myType

```
str myType;
```

Internal storage of the type of what the function calculates. 

### variable myOrigin

```
str myOrigin;
```

Internal storage of the name of the module or backend to which the function belongs. 

### variable myPurpose

```
str myPurpose;
```

Purpose of the function (relevant for output and next-to-output functors) 

### variable myCitationKey

```
str myCitationKey;
```

Citation key: BibTex key of the reference. 

### variable myClaw

```
const Models::ModelFunctorClaw * myClaw;
```

Bound model functor claw, for checking relationships between models. 

### variable myLabel

```
const str myLabel;
```

String label, used to label functor results for printer system. 

### variable myTimingLabel

```
const str myTimingLabel;
```

String label, used to label functor timing data for printer system. 

### variable myStatus

```
FunctorStatus myStatus;
```

Status: 

### variable myVertexID

```
int myVertexID;
```

Internal storage of the vertex ID number used by the printer system to identify functors. 

### variable myTimingVertexID

```
int myTimingVertexID;
```

ID assigned by printers to the timing data output stream. 

### variable verbose

```
bool verbose;
```

Debug flag. 

### variable myOptions

```
Options myOptions;
```

Internal storage of function options, as a [YAML](/documentation/code/namespaces/namespaceyaml/) node. 

### variable mySubCaps

```
Options mySubCaps;
```

Internal storage of function sub-capabilities, as a [YAML](/documentation/code/namespaces/namespaceyaml/) node. 

### variable myDependees

```
std::set< sspair > myDependees;
```

List of all capability,type pairs of functors downstream of this one in the dependency tree. 

### variable allowedModels

```
std::set< str > allowedModels;
```

List of allowed models. 

### variable conditionalModels

```
std::set< str > conditionalModels;
```

List of conditional models. 

### variable allowedGroupCombos

```
std::set< std::set< str > > allowedGroupCombos;
```

List of allowed model group combinations. 

### variable modelGroups

```
std::map< str, std::set< str > > modelGroups;
```

Map from model group names to group contents. 

### variable matched_observables

```
std::set< const DRes::Observable * > matched_observables;
```

The set of observables that this functor matches. 

### variable matched_module_rules

```
std::set< const DRes::ModuleRule * > matched_module_rules;
```

Set of module rules against which this functor has been tested and found to match. 

### variable matched_backend_rules

```
std::set< const DRes::BackendRule * > matched_backend_rules;
```

Set of backend rules against which this functor has been tested and found to match. 

-------------------------------

Updated on 2024-07-18 at 13:53:30 +0000