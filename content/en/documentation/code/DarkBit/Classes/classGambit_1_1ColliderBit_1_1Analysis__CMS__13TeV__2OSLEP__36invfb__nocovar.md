---
title: 'class Gambit::ColliderBit::Analysis_CMS_13TeV_2OSLEP_36invfb_nocovar'

description: "[No description available]"

---








[No description available]

Inherits from [Gambit::ColliderBit::Analysis_CMS_13TeV_2OSLEP_36invfb](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__36invfb/), [Gambit::ColliderBit::Analysis](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Analysis_CMS_13TeV_2OSLEP_36invfb_nocovar](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__36invfb__nocovar/#function-analysis-cms-13tev-2oslep-36invfb-nocovar)**() |
| virtual void | **[collect_results](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__36invfb__nocovar/#function-collect-results)**()<br>Gather together the info for likelihood calculation.  |

## Additional inherited members

**Public Classes inherited from [Gambit::ColliderBit::Analysis_CMS_13TeV_2OSLEP_36invfb](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__36invfb/)**

|                | Name           |
| -------------- | -------------- |
| struct | **[ptComparison](/documentation/code/darkbit/classes/structgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__36invfb_1_1ptcomparison/)**  |
| struct | **[ptJetComparison](/documentation/code/darkbit/classes/structgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__36invfb_1_1ptjetcomparison/)**  |

**Public Functions inherited from [Gambit::ColliderBit::Analysis_CMS_13TeV_2OSLEP_36invfb](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__36invfb/)**

|                | Name           |
| -------------- | -------------- |
| | **[Analysis_CMS_13TeV_2OSLEP_36invfb](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__36invfb/#function-analysis-cms-13tev-2oslep-36invfb)**() |
| virtual void | **[run](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__36invfb/#function-run)**(const HEPUtils::Event * event) |
| virtual void | **[combine](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__36invfb/#function-combine)**(const [Analysis](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis/) * other)<br>Combine the variables of another copy of this analysis (typically on another thread) into this one.  |
| double | **[get_mjj](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__36invfb/#function-get-mjj)**(vector< const HEPUtils::Jet * > jets) |
| double | **[get_mT2](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__36invfb/#function-get-mt2)**(vector< const HEPUtils::Particle * > leptons, vector< const HEPUtils::Jet * > bjets, HEPUtils::P4 met) |

**Protected Functions inherited from [Gambit::ColliderBit::Analysis_CMS_13TeV_2OSLEP_36invfb](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__36invfb/)**

|                | Name           |
| -------------- | -------------- |
| virtual void | **[analysis_specific_reset](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__36invfb/#function-analysis-specific-reset)**()<br>Reset the analysis-specific variables.  |

**Public Attributes inherited from [Gambit::ColliderBit::Analysis_CMS_13TeV_2OSLEP_36invfb](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__36invfb/)**

|                | Name           |
| -------------- | -------------- |
| constexpr const char * | **[detector](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__36invfb/#variable-detector)**  |
| struct [Gambit::ColliderBit::Analysis_CMS_13TeV_2OSLEP_36invfb::ptComparison](/documentation/code/darkbit/classes/structgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__36invfb_1_1ptcomparison/) | **[comparePt](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__36invfb/#variable-comparept)**  |
| struct [Gambit::ColliderBit::Analysis_CMS_13TeV_2OSLEP_36invfb::ptJetComparison](/documentation/code/darkbit/classes/structgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__36invfb_1_1ptjetcomparison/) | **[compareJetPt](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__36invfb/#variable-comparejetpt)**  |

**Protected Attributes inherited from [Gambit::ColliderBit::Analysis_CMS_13TeV_2OSLEP_36invfb](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__36invfb/)**

|                | Name           |
| -------------- | -------------- |
| std::map< string, [EventCounter](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1eventcounter/) > | **[_counters](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__36invfb/#variable--counters)**  |

**Public Functions inherited from [Gambit::ColliderBit::Analysis](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis/)**

|                | Name           |
| -------------- | -------------- |
| void | **[analyze](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis/#function-analyze)**(const HEPUtils::Event & e)<br>Analyze the event (accessed by reference).  |
| void | **[analyze](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis/#function-analyze)**(const HEPUtils::Event * e)<br>Analyze the event (accessed by pointer).  |
| void | **[add](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis/#function-add)**([Analysis](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis/) * other)<br>Add the results of another analysis to this one. Argument is not const, because the other needs to be able to gather its results if necessary.  |
| virtual void | **[combine](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis/#function-combine)**(const [Analysis](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis/) * other) =0<br>Add the analysis-specific variables of another analysis to this one.  |
| | **[Analysis](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis/#function-analysis)**()<br>Construction.  |
| virtual | **[~Analysis](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis/#function-~analysis)**()<br>Destruction.  |
| void | **[reset](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis/#function-reset)**()<br>Public method to reset this instance for reuse, avoiding the need for "new" or "delete".  |
| double | **[luminosity](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis/#function-luminosity)**() const<br>Return the integrated luminosity.  |
| void | **[set_luminosity](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis/#function-set-luminosity)**(double lumi)<br>Set the integrated luminosity.  |
| void | **[set_analysis_name](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis/#function-set-analysis-name)**(str aname)<br>Set the analysis name.  |
| str | **[analysis_name](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis/#function-analysis-name)**()<br>Get the analysis name.  |
| const [AnalysisData](/documentation/code/darkbit/classes/structgambit_1_1colliderbit_1_1analysisdata/) & | **[get_results](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis/#function-get-results)**()<br>Get the collection of [SignalRegionData]() for likelihood computation.  |
| const [AnalysisData](/documentation/code/darkbit/classes/structgambit_1_1colliderbit_1_1analysisdata/) & | **[get_results](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis/#function-get-results)**(str & warning)<br>An overload of [get_results()](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis/#function-get-results) with some additional consistency checks.  |
| [AnalysisData](/documentation/code/darkbit/classes/structgambit_1_1colliderbit_1_1analysisdata/) * | **[get_results_ptr](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis/#function-get-results-ptr)**()<br>Get a (non-const!) pointer to _results.  |
| [AnalysisData](/documentation/code/darkbit/classes/structgambit_1_1colliderbit_1_1analysisdata/) * | **[get_results_ptr](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis/#function-get-results-ptr)**(str & warning)<br>An overload of [get_results_ptr()](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis/#function-get-results-ptr) with some additional consistency checks.  |
| void | **[scale](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis/#function-scale)**(double xsec_per_event)<br>Scale by xsec per event.  |

**Protected Functions inherited from [Gambit::ColliderBit::Analysis](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis/)**

|                | Name           |
| -------------- | -------------- |
| virtual void | **[run](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis/#function-run)**(const HEPUtils::Event * ) =0 |
| void | **[add_result](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis/#function-add-result)**(const [SignalRegionData](/documentation/code/darkbit/classes/structgambit_1_1colliderbit_1_1signalregiondata/) & sr)<br>Add the given result to the internal results list.  |
| void | **[set_covariance](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis/#function-set-covariance)**(const Eigen::MatrixXd & srcov)<br>Set the covariance matrix, expressing SR correlations.  |
| void | **[set_covariance](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis/#function-set-covariance)**(const std::vector< std::vector< double > > & srcov)<br>A convenience function for setting the SR covariance from a nested vector/initialiser list.  |
| virtual void | **[analysis_specific_reset](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis/#function-analysis-specific-reset)**() =0<br>Reset the analysis-specific variables.  |


## Public Functions Documentation

### function Analysis_CMS_13TeV_2OSLEP_36invfb_nocovar

```
inline Analysis_CMS_13TeV_2OSLEP_36invfb_nocovar()
```


### function collect_results

```
inline virtual void collect_results()
```

Gather together the info for likelihood calculation. 

**Reimplements**: [Gambit::ColliderBit::Analysis_CMS_13TeV_2OSLEP_36invfb::collect_results](/documentation/code/darkbit/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__36invfb/#function-collect-results)


-------------------------------

Updated on 2022-08-03 at 12:58:02 +0000