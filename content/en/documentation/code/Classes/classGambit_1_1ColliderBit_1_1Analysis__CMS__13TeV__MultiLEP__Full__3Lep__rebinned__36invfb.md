---
title: "class Gambit::ColliderBit::Analysis_CMS_13TeV_MultiLEP_Full_3Lep_rebinned_36invfb"

description: "[No description available]"

---

# class Gambit::ColliderBit::Analysis_CMS_13TeV_MultiLEP_Full_3Lep_rebinned_36invfb



[No description available]

Inherits from [Gambit::ColliderBit::Analysis_CMS_13TeV_MultiLEP_Full_36invfb](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__multilep__full__36invfb/), [Gambit::ColliderBit::Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Analysis_CMS_13TeV_MultiLEP_Full_3Lep_rebinned_36invfb](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__multilep__full__3lep__rebinned__36invfb/#function-gambitcolliderbitanalysis-cms-13tev-multilep-full-3lep-rebinned-36invfb-analysis-cms-13tev-multilep-full-3lep-rebinned-36invfb)**() |
| virtual void | **[collect_results](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__multilep__full__3lep__rebinned__36invfb/#function-gambitcolliderbitanalysis-cms-13tev-multilep-full-3lep-rebinned-36invfb-collect-results)**()<br>Gather together the info for likelihood calculation.  |

## Additional inherited members

**Public Classes inherited from [Gambit::ColliderBit::Analysis_CMS_13TeV_MultiLEP_Full_36invfb](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__multilep__full__36invfb/)**

|                | Name           |
| -------------- | -------------- |
| struct | **[ptComparison](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysis__cms__13tev__multilep__full__36invfb_1_1ptcomparison/)**  |

**Public Functions inherited from [Gambit::ColliderBit::Analysis_CMS_13TeV_MultiLEP_Full_36invfb](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__multilep__full__36invfb/)**

|                | Name           |
| -------------- | -------------- |
| | **[Analysis_CMS_13TeV_MultiLEP_Full_36invfb](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__multilep__full__36invfb/#function-gambitcolliderbitanalysis-cms-13tev-multilep-full-36invfb-analysis-cms-13tev-multilep-full-36invfb)**() |
| virtual void | **[run](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__multilep__full__36invfb/#function-gambitcolliderbitanalysis-cms-13tev-multilep-full-36invfb-run)**(const HEPUtils::Event * event) |
| virtual void | **[combine](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__multilep__full__36invfb/#function-gambitcolliderbitanalysis-cms-13tev-multilep-full-36invfb-combine)**(const [Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/) * other)<br>Combine the variables of another copy of this analysis (typically on another thread) into this one.  |
| vector< double > | **[get_mll_mT](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__multilep__full__36invfb/#function-gambitcolliderbitanalysis-cms-13tev-multilep-full-36invfb-get-mll-mt)**(vector< vector< const HEPUtils::Particle * > > pair_cont, vector< const HEPUtils::Particle * > leptons, HEPUtils::P4 met, int type) |
| double | **[get_mTmin](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__multilep__full__36invfb/#function-gambitcolliderbitanalysis-cms-13tev-multilep-full-36invfb-get-mtmin)**(vector< const HEPUtils::Particle * > leptons, HEPUtils::P4 met) |

**Protected Functions inherited from [Gambit::ColliderBit::Analysis_CMS_13TeV_MultiLEP_Full_36invfb](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__multilep__full__36invfb/)**

|                | Name           |
| -------------- | -------------- |
| virtual void | **[analysis_specific_reset](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__multilep__full__36invfb/#function-gambitcolliderbitanalysis-cms-13tev-multilep-full-36invfb-analysis-specific-reset)**()<br>Reset the analysis-specific variables.  |

**Public Attributes inherited from [Gambit::ColliderBit::Analysis_CMS_13TeV_MultiLEP_Full_36invfb](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__multilep__full__36invfb/)**

|                | Name           |
| -------------- | -------------- |
| constexpr const char * | **[detector](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__multilep__full__36invfb/#variable-gambitcolliderbitanalysis-cms-13tev-multilep-full-36invfb-detector)**  |
| struct [Gambit::ColliderBit::Analysis_CMS_13TeV_MultiLEP_Full_36invfb::ptComparison](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysis__cms__13tev__multilep__full__36invfb_1_1ptcomparison/) | **[comparePt](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__multilep__full__36invfb/#variable-gambitcolliderbitanalysis-cms-13tev-multilep-full-36invfb-comparept)**  |

**Protected Attributes inherited from [Gambit::ColliderBit::Analysis_CMS_13TeV_MultiLEP_Full_36invfb](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__multilep__full__36invfb/)**

|                | Name           |
| -------------- | -------------- |
| std::map< string, [EventCounter](/documentation/code/classes/classgambit_1_1colliderbit_1_1eventcounter/) > | **[_counters](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__multilep__full__36invfb/#variable-gambitcolliderbitanalysis-cms-13tev-multilep-full-36invfb-counters)**  |

**Public Functions inherited from [Gambit::ColliderBit::Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)**

|                | Name           |
| -------------- | -------------- |
| void | **[analyze](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-gambitcolliderbitanalysis-analyze)**(const HEPUtils::Event & e)<br>Analyze the event (accessed by reference).  |
| void | **[analyze](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-gambitcolliderbitanalysis-analyze)**(const HEPUtils::Event * e)<br>Analyze the event (accessed by pointer).  |
| void | **[add](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-gambitcolliderbitanalysis-add)**([Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/) * other)<br>Add the results of another analysis to this one. Argument is not const, because the other needs to be able to gather its results if necessary.  |
| virtual void | **[combine](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-gambitcolliderbitanalysis-combine)**(const [Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/) * other) =0<br>Add the analysis-specific variables of another analysis to this one.  |
| | **[Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-gambitcolliderbitanalysis-analysis)**()<br>Construction.  |
| virtual | **[~Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-gambitcolliderbitanalysis-analysis)**()<br>Destruction.  |
| void | **[reset](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-gambitcolliderbitanalysis-reset)**()<br>Public method to reset this instance for reuse, avoiding the need for "new" or "delete".  |
| double | **[luminosity](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-gambitcolliderbitanalysis-luminosity)**() const<br>Return the integrated luminosity.  |
| void | **[set_luminosity](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-gambitcolliderbitanalysis-set-luminosity)**(double lumi)<br>Set the integrated luminosity.  |
| void | **[set_analysis_name](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-gambitcolliderbitanalysis-set-analysis-name)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) aname)<br>Set the analysis name.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[analysis_name](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-gambitcolliderbitanalysis-analysis-name)**()<br>Get the analysis name.  |
| const [AnalysisData](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysisdata/) & | **[get_results](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-gambitcolliderbitanalysis-get-results)**()<br>Get the collection of [SignalRegionData]() for likelihood computation.  |
| const [AnalysisData](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysisdata/) & | **[get_results](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-gambitcolliderbitanalysis-get-results)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) & warning)<br>An overload of [get_results()](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-gambitcolliderbitanalysis-get-results) with some additional consistency checks.  |
| [AnalysisData](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysisdata/) * | **[get_results_ptr](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-gambitcolliderbitanalysis-get-results-ptr)**()<br>Get a (non-const!) pointer to _results.  |
| [AnalysisData](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysisdata/) * | **[get_results_ptr](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-gambitcolliderbitanalysis-get-results-ptr)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) & warning)<br>An overload of [get_results_ptr()](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-gambitcolliderbitanalysis-get-results-ptr) with some additional consistency checks.  |
| void | **[scale](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-gambitcolliderbitanalysis-scale)**(double xsec_per_event)<br>Scale by xsec per event.  |

**Protected Functions inherited from [Gambit::ColliderBit::Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)**

|                | Name           |
| -------------- | -------------- |
| virtual void | **[run](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-gambitcolliderbitanalysis-run)**(const HEPUtils::Event * ) =0 |
| void | **[add_result](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-gambitcolliderbitanalysis-add-result)**(const [SignalRegionData](/documentation/code/classes/structgambit_1_1colliderbit_1_1signalregiondata/) & sr)<br>Add the given result to the internal results list.  |
| void | **[set_covariance](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-gambitcolliderbitanalysis-set-covariance)**(const Eigen::MatrixXd & srcov)<br>Set the covariance matrix, expressing SR correlations.  |
| void | **[set_covariance](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-gambitcolliderbitanalysis-set-covariance)**(const std::vector< std::vector< double > > & srcov)<br>A convenience function for setting the SR covariance from a nested vector/initialiser list.  |
| virtual void | **[analysis_specific_reset](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-gambitcolliderbitanalysis-analysis-specific-reset)**() =0<br>Reset the analysis-specific variables.  |


## Public Functions Documentation

### function Analysis_CMS_13TeV_MultiLEP_Full_3Lep_rebinned_36invfb

```
inline Analysis_CMS_13TeV_MultiLEP_Full_3Lep_rebinned_36invfb()
```


### function collect_results

```
inline virtual void collect_results()
```

Gather together the info for likelihood calculation. 

**Reimplements**: [Gambit::ColliderBit::Analysis_CMS_13TeV_MultiLEP_Full_36invfb::collect_results](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__multilep__full__36invfb/#function-gambitcolliderbitanalysis-cms-13tev-multilep-full-36invfb-collect-results)


-------------------------------

Updated on 2022-09-08 at 01:48:55 +0000