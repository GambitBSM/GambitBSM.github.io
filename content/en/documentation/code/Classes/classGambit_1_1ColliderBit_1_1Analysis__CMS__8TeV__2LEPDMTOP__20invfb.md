---
title: "class Gambit::ColliderBit::Analysis_CMS_8TeV_2LEPDMTOP_20invfb"

description: "[No description available]"

---

# class Gambit::ColliderBit::Analysis_CMS_8TeV_2LEPDMTOP_20invfb



[No description available]

Inherits from [Gambit::ColliderBit::Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Analysis_CMS_8TeV_2LEPDMTOP_20invfb](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__8tev__2lepdmtop__20invfb/#function-gambitcolliderbitanalysis-cms-8tev-2lepdmtop-20invfb-analysis-cms-8tev-2lepdmtop-20invfb)**() |
| double | **[SmallestdPhi](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__8tev__2lepdmtop__20invfb/#function-gambitcolliderbitanalysis-cms-8tev-2lepdmtop-20invfb-smallestdphi)**(std::vector< HEPUtils::Jet * > jets, double phi_met) |
| virtual void | **[run](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__8tev__2lepdmtop__20invfb/#function-gambitcolliderbitanalysis-cms-8tev-2lepdmtop-20invfb-run)**(const HEPUtils::Event * event) |
| virtual void | **[combine](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__8tev__2lepdmtop__20invfb/#function-gambitcolliderbitanalysis-cms-8tev-2lepdmtop-20invfb-combine)**(const [Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/) * other)<br>Combine the variables of another copy of this analysis (typically on another thread) into this one.  |
| double | **[loglikelihood](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__8tev__2lepdmtop__20invfb/#function-gambitcolliderbitanalysis-cms-8tev-2lepdmtop-20invfb-loglikelihood)**() |
| virtual void | **[collect_results](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__8tev__2lepdmtop__20invfb/#function-gambitcolliderbitanalysis-cms-8tev-2lepdmtop-20invfb-collect-results)**()<br>Gather together the info for likelihood calculation.  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| virtual void | **[analysis_specific_reset](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__8tev__2lepdmtop__20invfb/#function-gambitcolliderbitanalysis-cms-8tev-2lepdmtop-20invfb-analysis-specific-reset)**()<br>Reset the analysis-specific variables.  |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| constexpr const char * | **[detector](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__8tev__2lepdmtop__20invfb/#variable-gambitcolliderbitanalysis-cms-8tev-2lepdmtop-20invfb-detector)**  |

## Additional inherited members

**Public Functions inherited from [Gambit::ColliderBit::Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)**

|                | Name           |
| -------------- | -------------- |
| void | **[analyze](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-gambitcolliderbitanalysis-analyze)**(const HEPUtils::Event & e)<br>Analyze the event (accessed by reference).  |
| void | **[analyze](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-gambitcolliderbitanalysis-analyze)**(const HEPUtils::Event * e)<br>Analyze the event (accessed by pointer).  |
| void | **[add](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-gambitcolliderbitanalysis-add)**([Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/) * other)<br>Add the results of another analysis to this one. Argument is not const, because the other needs to be able to gather its results if necessary.  |
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
| void | **[add_result](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-gambitcolliderbitanalysis-add-result)**(const [SignalRegionData](/documentation/code/classes/structgambit_1_1colliderbit_1_1signalregiondata/) & sr)<br>Add the given result to the internal results list.  |
| void | **[set_covariance](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-gambitcolliderbitanalysis-set-covariance)**(const Eigen::MatrixXd & srcov)<br>Set the covariance matrix, expressing SR correlations.  |
| void | **[set_covariance](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-gambitcolliderbitanalysis-set-covariance)**(const std::vector< std::vector< double > > & srcov)<br>A convenience function for setting the SR covariance from a nested vector/initialiser list.  |


## Public Functions Documentation

### function Analysis_CMS_8TeV_2LEPDMTOP_20invfb

```
inline Analysis_CMS_8TeV_2LEPDMTOP_20invfb()
```


### function SmallestdPhi

```
inline double SmallestdPhi(
    std::vector< HEPUtils::Jet * > jets,
    double phi_met
)
```


### function run

```
inline virtual void run(
    const HEPUtils::Event * event
)
```


**Reimplements**: [Gambit::ColliderBit::Analysis::run](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-gambitcolliderbitanalysis-run)


### function combine

```
inline virtual void combine(
    const Analysis * other
)
```

Combine the variables of another copy of this analysis (typically on another thread) into this one. 

**Reimplements**: [Gambit::ColliderBit::Analysis::combine](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-gambitcolliderbitanalysis-combine)


### function loglikelihood

```
inline double loglikelihood()
```


TodoImplement! 


### function collect_results

```
inline virtual void collect_results()
```

Gather together the info for likelihood calculation. 

**Reimplements**: [Gambit::ColliderBit::Analysis::collect_results](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-gambitcolliderbitanalysis-collect-results)


## Protected Functions Documentation

### function analysis_specific_reset

```
inline virtual void analysis_specific_reset()
```

Reset the analysis-specific variables. 

**Reimplements**: [Gambit::ColliderBit::Analysis::analysis_specific_reset](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-gambitcolliderbitanalysis-analysis-specific-reset)


## Public Attributes Documentation

### variable detector

```
static constexpr const char * detector = "CMS";
```


-------------------------------

Updated on 2022-09-08 at 01:48:55 +0000