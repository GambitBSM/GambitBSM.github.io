---
title: "class Gambit::backend_functor< typename variadic_ptr< void, ARGS... >::type, void, ARGS... >"
description: "Template specialisation for variadic void backend functions. "

---

# class Gambit::backend_functor< typename variadic_ptr< void, ARGS... >::type, void, ARGS... >



Template specialisation for variadic void backend functions.  [More...](#detailed-description)


`#include <functors.hpp>`

Inherits from [Gambit::backend_functor_common< variadic_ptr< void, ARGS... >::type, void, ARGS... >](/documentation/code/classes/classgambit_1_1backend__functor__common/), [Gambit::functor](/documentation/code/classes/classgambit_1_1functor/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[backend_functor](/documentation/code/classes/classgambit_1_1backend__functor_3_01typename_01variadic__ptr_3_01void_00_01args_8_8_8_01_4_1/)**(typename [variadic_ptr](/documentation/code/classes/structgambit_1_1variadic__ptr/)< void, ARGS... >[::type](/documentation/code/classes/classgambit_1_1functor/) , [str](/documentation/code/namespaces/namespacegambit/) , [str](/documentation/code/namespaces/namespacegambit/) , [str](/documentation/code/namespaces/namespacegambit/) , [str](/documentation/code/namespaces/namespacegambit/) , [str](/documentation/code/namespaces/namespacegambit/) , [str](/documentation/code/namespaces/namespacegambit/) , [str](/documentation/code/namespaces/namespacegambit/) , [Models::ModelFunctorClaw](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/) & )<br>Constructor.  |
| virtual | **[~backend_functor](/documentation/code/classes/classgambit_1_1backend__functor_3_01typename_01variadic__ptr_3_01void_00_01args_8_8_8_01_4_1/)**()<br>Destructor.  |
| template <typename... VARARGS\> <br>void | **[operator()](/documentation/code/classes/classgambit_1_1backend__functor_3_01typename_01variadic__ptr_3_01void_00_01args_8_8_8_01_4_1/)**(VARARGS &&... varargs)<br>Operation (execute function)  |

## Additional inherited members

**Protected Types inherited from [Gambit::backend_functor_common< variadic_ptr< void, ARGS... >::type, void, ARGS... >](/documentation/code/classes/classgambit_1_1backend__functor__common/)**

|                | Name           |
| -------------- | -------------- |
| typedef PTR_TYPE | **[funcPtrType](/documentation/code/classes/classgambit_1_1backend__functor__common/)** <br>Type of the function pointer being encapsulated.  |

**Public Functions inherited from [Gambit::backend_functor_common< variadic_ptr< void, ARGS... >::type, void, ARGS... >](/documentation/code/classes/classgambit_1_1backend__functor__common/)**

|                | Name           |
| -------------- | -------------- |
| | **[backend_functor_common](/documentation/code/classes/classgambit_1_1backend__functor__common/)**([funcPtrType](/documentation/code/classes/classgambit_1_1backend__functor__common/) inputFunction, [str](/documentation/code/namespaces/namespacegambit/) func_name, [str](/documentation/code/namespaces/namespacegambit/) func_capability, [str](/documentation/code/namespaces/namespacegambit/) result_type, [str](/documentation/code/namespaces/namespacegambit/) origin_name, [str](/documentation/code/namespaces/namespacegambit/) origin_version, [str](/documentation/code/namespaces/namespacegambit/) origin_safe_version, [str](/documentation/code/namespaces/namespacegambit/) citation_key, [Models::ModelFunctorClaw](/documentation/code/classes/classgambit_1_1models_1_1modelfunctorclaw/) & claw)<br>Constructor.  |
| virtual | **[~backend_functor_common](/documentation/code/classes/classgambit_1_1backend__functor__common/)**()<br>Destructor.  |
| void | **[updatePointer](/documentation/code/classes/classgambit_1_1backend__functor__common/)**([funcPtrType](/documentation/code/classes/classgambit_1_1backend__functor__common/) inputFunction)<br>Update the internal function pointer wrapped by the functor.  |
| [funcPtrType](/documentation/code/classes/classgambit_1_1backend__functor__common/) | **[handoutFunctionPointer](/documentation/code/classes/classgambit_1_1backend__functor__common/)**()<br>Hand out the internal function pointer wrapped by the functor.  |
| [safe_ptr](/documentation/code/classes/classgambit_1_1safe__ptr/)< bool > | **[inUsePtr](/documentation/code/classes/classgambit_1_1backend__functor__common/)**()<br>Hand out a safe pointer to this backend functor's inUse flag.  |
| virtual [str](/documentation/code/namespaces/namespacegambit/) | **[safe_version](/documentation/code/classes/classgambit_1_1backend__functor__common/)**() const<br>Getter for the 'safe' incarnation of the version of the wrapped function's origin (module or backend)  |

**Protected Functions inherited from [Gambit::backend_functor_common< variadic_ptr< void, ARGS... >::type, void, ARGS... >](/documentation/code/classes/classgambit_1_1backend__functor__common/)**

|                | Name           |
| -------------- | -------------- |
| virtual void | **[setInUse](/documentation/code/classes/classgambit_1_1backend__functor__common/)**(bool flag)<br>Set the inUse flag.  |

**Protected Attributes inherited from [Gambit::backend_functor_common< variadic_ptr< void, ARGS... >::type, void, ARGS... >](/documentation/code/classes/classgambit_1_1backend__functor__common/)**

|                | Name           |
| -------------- | -------------- |
| [funcPtrType](/documentation/code/classes/classgambit_1_1backend__functor__common/) | **[myFunction](/documentation/code/classes/classgambit_1_1backend__functor__common/)** <br>Internal storage of function pointer.  |
| int | **[myLogTag](/documentation/code/classes/classgambit_1_1backend__functor__common/)** <br>Integer LogTag, for tagging log messages.  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[mySafeVersion](/documentation/code/classes/classgambit_1_1backend__functor__common/)** <br>Internal storage of the 'safe' version of the version (for use in namespaces, variable names, etc).  |
| bool | **[inUse](/documentation/code/classes/classgambit_1_1backend__functor__common/)** <br>Flag indicating if this backend functor is actually in use in a given scan.  |

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
| virtual void | **[calculate](/documentation/code/classes/classgambit_1_1functor/)**()<br>Virtual [calculate()](); needs to be redefined in daughters.  |
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
| virtual bool | **[requiresPrinting](/documentation/code/classes/classgambit_1_1functor/)**() const<br>Getter indicating if the wrapped function's result should to be printed.  |
| virtual bool | **[requiresTimingPrinting](/documentation/code/classes/classgambit_1_1functor/)**() const<br>Getter indicating if the timing data for this function's execution should be printed.  |
| virtual void | **[setPrintRequirement](/documentation/code/classes/classgambit_1_1functor/)**(bool flag)<br>Setter for indicating if the wrapped function's result should to be printed.  |
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
| virtual void | **[print](/documentation/code/classes/classgambit_1_1functor/)**([Printers::BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/) * printer, const int pointID, int thread_num)<br>Printer function.  |
| virtual void | **[print](/documentation/code/classes/classgambit_1_1functor/)**([Printers::BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/) * printer, const int pointID)<br>Printer function (no-thread-index short-circuit)  |
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
template <typename... ARGS>
class Gambit::backend_functor< typename variadic_ptr< void, ARGS... >::type, void, ARGS... >;
```

Template specialisation for variadic void backend functions. 
## Public Functions Documentation

### function backend_functor

```
backend_functor(
    typename variadic_ptr< void, ARGS... >::type ,
    str ,
    str ,
    str ,
    str ,
    str ,
    str ,
    str ,
    Models::ModelFunctorClaw & 
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
template <typename... VARARGS>
inline void operator()(
    VARARGS &&... varargs
)
```

Operation (execute function) 

-------------------------------

Updated on 2022-09-08 at 01:05:15 +0000