---
title: "class Gambit::ColliderBit::Analysis_CMS_13TeV_2OSLEP_for_stop_36invfb"

description: "[No description available]"

---

# class Gambit::ColliderBit::Analysis_CMS_13TeV_2OSLEP_for_stop_36invfb



[No description available]

Inherits from [Gambit::ColliderBit::Analysis_CMS_13TeV_2OSLEP_chargino_stop_36invfb](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__chargino__stop__36invfb/), [Gambit::ColliderBit::Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Analysis_CMS_13TeV_2OSLEP_for_stop_36invfb](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__for__stop__36invfb/)**() |
| virtual void | **[collect_results](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__for__stop__36invfb/)**()<br>Gather together the info for likelihood calculation.  |

## Additional inherited members

**Public Classes inherited from [Gambit::ColliderBit::Analysis_CMS_13TeV_2OSLEP_chargino_stop_36invfb](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__chargino__stop__36invfb/)**

|                | Name           |
| -------------- | -------------- |
| struct | **[ptComparison](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__chargino__stop__36invfb_1_1ptcomparison/)**  |

**Public Functions inherited from [Gambit::ColliderBit::Analysis_CMS_13TeV_2OSLEP_chargino_stop_36invfb](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__chargino__stop__36invfb/)**

|                | Name           |
| -------------- | -------------- |
| | **[Analysis_CMS_13TeV_2OSLEP_chargino_stop_36invfb](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__chargino__stop__36invfb/)**() |
| virtual void | **[run](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__chargino__stop__36invfb/)**(const HEPUtils::Event * event) |
| virtual void | **[combine](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__chargino__stop__36invfb/)**(const [Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/) * other)<br>Combine the variables of another copy of this analysis (typically on another thread) into this one.  |

**Protected Functions inherited from [Gambit::ColliderBit::Analysis_CMS_13TeV_2OSLEP_chargino_stop_36invfb](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__chargino__stop__36invfb/)**

|                | Name           |
| -------------- | -------------- |
| virtual void | **[analysis_specific_reset](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__chargino__stop__36invfb/)**()<br>Reset the analysis-specific variables.  |

**Public Attributes inherited from [Gambit::ColliderBit::Analysis_CMS_13TeV_2OSLEP_chargino_stop_36invfb](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__chargino__stop__36invfb/)**

|                | Name           |
| -------------- | -------------- |
| constexpr const char * | **[detector](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__chargino__stop__36invfb/)**  |
| struct [Gambit::ColliderBit::Analysis_CMS_13TeV_2OSLEP_chargino_stop_36invfb::ptComparison](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__chargino__stop__36invfb_1_1ptcomparison/) | **[comparePt](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__chargino__stop__36invfb/)**  |

**Protected Attributes inherited from [Gambit::ColliderBit::Analysis_CMS_13TeV_2OSLEP_chargino_stop_36invfb](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__chargino__stop__36invfb/)**

|                | Name           |
| -------------- | -------------- |
| std::map< string, [EventCounter](/documentation/code/classes/classgambit_1_1colliderbit_1_1eventcounter/) > | **[_counters](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__chargino__stop__36invfb/)**  |
| [Cutflow](/documentation/code/classes/structgambit_1_1colliderbit_1_1cutflow/) | **[_cutflow](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__chargino__stop__36invfb/)**  |
| const size_t | **[NUMSR_stop](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__chargino__stop__36invfb/)**  |
| const size_t | **[NUMSR_chargino](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__chargino__stop__36invfb/)**  |

**Public Functions inherited from [Gambit::ColliderBit::Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)**

|                | Name           |
| -------------- | -------------- |
| void | **[analyze](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)**(const HEPUtils::Event & e)<br>Analyze the event (accessed by reference).  |
| void | **[analyze](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)**(const HEPUtils::Event * e)<br>Analyze the event (accessed by pointer).  |
| void | **[add](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)**([Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/) * other)<br>Add the results of another analysis to this one. Argument is not const, because the other needs to be able to gather its results if necessary.  |
| virtual void | **[combine](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)**(const [Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/) * other) =0<br>Add the analysis-specific variables of another analysis to this one.  |
| | **[Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)**()<br>Construction.  |
| virtual | **[~Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)**()<br>Destruction.  |
| void | **[reset](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)**()<br>Public method to reset this instance for reuse, avoiding the need for "new" or "delete".  |
| double | **[luminosity](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)**() const<br>Return the integrated luminosity.  |
| void | **[set_luminosity](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)**(double lumi)<br>Set the integrated luminosity.  |
| void | **[set_analysis_name](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)**([str](/documentation/code/namespaces/namespacegambit/) aname)<br>Set the analysis name.  |
| [str](/documentation/code/namespaces/namespacegambit/) | **[analysis_name](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)**()<br>Get the analysis name.  |
| const [AnalysisData](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysisdata/) & | **[get_results](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)**()<br>Get the collection of [SignalRegionData]() for likelihood computation.  |
| const [AnalysisData](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysisdata/) & | **[get_results](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)**([str](/documentation/code/namespaces/namespacegambit/) & warning)<br>An overload of [get_results()](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/) with some additional consistency checks.  |
| [AnalysisData](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysisdata/) * | **[get_results_ptr](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)**()<br>Get a (non-const!) pointer to _results.  |
| [AnalysisData](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysisdata/) * | **[get_results_ptr](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)**([str](/documentation/code/namespaces/namespacegambit/) & warning)<br>An overload of [get_results_ptr()](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/) with some additional consistency checks.  |
| void | **[scale](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)**(double xsec_per_event)<br>Scale by xsec per event.  |

**Protected Functions inherited from [Gambit::ColliderBit::Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)**

|                | Name           |
| -------------- | -------------- |
| virtual void | **[run](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)**(const HEPUtils::Event * ) =0 |
| void | **[add_result](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)**(const [SignalRegionData](/documentation/code/classes/structgambit_1_1colliderbit_1_1signalregiondata/) & sr)<br>Add the given result to the internal results list.  |
| void | **[set_covariance](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)**(const Eigen::MatrixXd & srcov)<br>Set the covariance matrix, expressing SR correlations.  |
| void | **[set_covariance](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)**(const std::vector< std::vector< double > > & srcov)<br>A convenience function for setting the SR covariance from a nested vector/initialiser list.  |
| virtual void | **[analysis_specific_reset](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)**() =0<br>Reset the analysis-specific variables.  |


## Public Functions Documentation

### function Analysis_CMS_13TeV_2OSLEP_for_stop_36invfb

```
inline Analysis_CMS_13TeV_2OSLEP_for_stop_36invfb()
```


### function collect_results

```
inline virtual void collect_results()
```

Gather together the info for likelihood calculation. 

**Reimplements**: [Gambit::ColliderBit::Analysis_CMS_13TeV_2OSLEP_chargino_stop_36invfb::collect_results](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__chargino__stop__36invfb/)


-------------------------------

Updated on 2022-09-08 at 01:05:17 +0000