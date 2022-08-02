---
title: 'class Gambit::ColliderBit::Analysis_ATLAS_13TeV_RJ3L_lowmass_36invfb'

description: "[No description available]"

---








[No description available]

Inherits from [Gambit::ColliderBit::Analysis](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis/)

Inherited by [Gambit::ColliderBit::Analysis_ATLAS_13TeV_RJ3L_2Lep2Jets_36invfb](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__rj3l__2lep2jets__36invfb/), [Gambit::ColliderBit::Analysis_ATLAS_13TeV_RJ3L_3Lep_36invfb](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__rj3l__3lep__36invfb/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Analysis_ATLAS_13TeV_RJ3L_lowmass_36invfb](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__rj3l__lowmass__36invfb/#function-analysis-atlas-13tev-rj3l-lowmass-36invfb)**() |
| virtual void | **[run](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__rj3l__lowmass__36invfb/#function-run)**(const HEPUtils::Event * event) |
| virtual void | **[combine](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__rj3l__lowmass__36invfb/#function-combine)**(const [Analysis](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis/) * other)<br>Combine the variables of another copy of this analysis (typically on another thread) into this one.  |
| virtual void | **[collect_results](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__rj3l__lowmass__36invfb/#function-collect-results)**()<br>Gather together the info for likelihood calculation.  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| virtual void | **[analysis_specific_reset](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__rj3l__lowmass__36invfb/#function-analysis-specific-reset)**()<br>Reset the analysis-specific variables.  |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| constexpr const char * | **[detector](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__rj3l__lowmass__36invfb/#variable-detector)**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| std::map< string, [EventCounter](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1eventcounter/) > | **[_counters](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__rj3l__lowmass__36invfb/#variable--counters)**  |

## Additional inherited members

**Public Functions inherited from [Gambit::ColliderBit::Analysis](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis/)**

|                | Name           |
| -------------- | -------------- |
| void | **[analyze](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis/#function-analyze)**(const HEPUtils::Event & e)<br>Analyze the event (accessed by reference).  |
| void | **[analyze](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis/#function-analyze)**(const HEPUtils::Event * e)<br>Analyze the event (accessed by pointer).  |
| void | **[add](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis/#function-add)**([Analysis](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis/) * other)<br>Add the results of another analysis to this one. Argument is not const, because the other needs to be able to gather its results if necessary.  |
| | **[Analysis](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis/#function-analysis)**()<br>Construction.  |
| virtual | **[~Analysis](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis/#function-~analysis)**()<br>Destruction.  |
| void | **[reset](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis/#function-reset)**()<br>Public method to reset this instance for reuse, avoiding the need for "new" or "delete".  |
| double | **[luminosity](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis/#function-luminosity)**() const<br>Return the integrated luminosity.  |
| void | **[set_luminosity](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis/#function-set-luminosity)**(double lumi)<br>Set the integrated luminosity.  |
| void | **[set_analysis_name](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis/#function-set-analysis-name)**(str aname)<br>Set the analysis name.  |
| str | **[analysis_name](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis/#function-analysis-name)**()<br>Get the analysis name.  |
| const [AnalysisData](/documentation/code/darkbit_development/classes/structgambit_1_1colliderbit_1_1analysisdata/) & | **[get_results](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis/#function-get-results)**()<br>Get the collection of [SignalRegionData]() for likelihood computation.  |
| const [AnalysisData](/documentation/code/darkbit_development/classes/structgambit_1_1colliderbit_1_1analysisdata/) & | **[get_results](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis/#function-get-results)**(str & warning)<br>An overload of [get_results()](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis/#function-get-results) with some additional consistency checks.  |
| [AnalysisData](/documentation/code/darkbit_development/classes/structgambit_1_1colliderbit_1_1analysisdata/) * | **[get_results_ptr](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis/#function-get-results-ptr)**()<br>Get a (non-const!) pointer to _results.  |
| [AnalysisData](/documentation/code/darkbit_development/classes/structgambit_1_1colliderbit_1_1analysisdata/) * | **[get_results_ptr](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis/#function-get-results-ptr)**(str & warning)<br>An overload of [get_results_ptr()](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis/#function-get-results-ptr) with some additional consistency checks.  |
| void | **[scale](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis/#function-scale)**(double xsec_per_event)<br>Scale by xsec per event.  |

**Protected Functions inherited from [Gambit::ColliderBit::Analysis](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis/)**

|                | Name           |
| -------------- | -------------- |
| void | **[add_result](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis/#function-add-result)**(const [SignalRegionData](/documentation/code/darkbit_development/classes/structgambit_1_1colliderbit_1_1signalregiondata/) & sr)<br>Add the given result to the internal results list.  |
| void | **[set_covariance](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis/#function-set-covariance)**(const Eigen::MatrixXd & srcov)<br>Set the covariance matrix, expressing SR correlations.  |
| void | **[set_covariance](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis/#function-set-covariance)**(const std::vector< std::vector< double > > & srcov)<br>A convenience function for setting the SR covariance from a nested vector/initialiser list.  |


## Public Functions Documentation

### function Analysis_ATLAS_13TeV_RJ3L_lowmass_36invfb

```
inline Analysis_ATLAS_13TeV_RJ3L_lowmass_36invfb()
```


### function run

```
inline virtual void run(
    const HEPUtils::Event * event
)
```


**Reimplements**: [Gambit::ColliderBit::Analysis::run](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis/#function-run)


We assume that b jets have previously been 100% tagged


Variables for the compressed/Intermediate tree

Defined in the PP-frame

Defined in the P-frame


### function combine

```
inline virtual void combine(
    const Analysis * other
)
```

Combine the variables of another copy of this analysis (typically on another thread) into this one. 

**Reimplements**: [Gambit::ColliderBit::Analysis::combine](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis/#function-combine)


### function collect_results

```
inline virtual void collect_results()
```

Gather together the info for likelihood calculation. 

**Reimplements**: [Gambit::ColliderBit::Analysis::collect_results](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis/#function-collect-results)


**Reimplemented by**: [Gambit::ColliderBit::Analysis_ATLAS_13TeV_RJ3L_2Lep2Jets_36invfb::collect_results](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__rj3l__2lep2jets__36invfb/#function-collect-results), [Gambit::ColliderBit::Analysis_ATLAS_13TeV_RJ3L_3Lep_36invfb::collect_results](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__rj3l__3lep__36invfb/#function-collect-results)


## Protected Functions Documentation

### function analysis_specific_reset

```
inline virtual void analysis_specific_reset()
```

Reset the analysis-specific variables. 

**Reimplements**: [Gambit::ColliderBit::Analysis::analysis_specific_reset](/documentation/code/darkbit_development/classes/classgambit_1_1colliderbit_1_1analysis/#function-analysis-specific-reset)


## Public Attributes Documentation

### variable detector

```
static constexpr const char * detector = "ATLAS";
```


## Protected Attributes Documentation

### variable _counters

```
std::map< string, EventCounter > _counters = {
        {"2L2JHIGH", EventCounter("2L2JHIGH")},
        {"2L2JINT", EventCounter("2L2JINT")},
        {"2L2JLOW", EventCounter("2L2JLOW")},
        {"2L2JCOMP", EventCounter("2L2JCOMP")},
        {"3LHIGH", EventCounter("3LHIGH")},
        {"3LINT", EventCounter("3LINT")},
        {"3LLOW", EventCounter("3LLOW")},
        {"3LCOMP", EventCounter("3LCOMP")},
      };
```


-------------------------------

Updated on 2022-08-01 at 17:41:23 +0000