---
title: "class Gambit::ColliderBit::Analysis_CMS_13TeV_2OSLEP_confnote_36invfb"

description: "[No description available]"

---

# class Gambit::ColliderBit::Analysis_CMS_13TeV_2OSLEP_confnote_36invfb



[No description available]

Inherits from [Gambit::ColliderBit::Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)

## Public Classes

|                | Name           |
| -------------- | -------------- |
| struct | **[ptComparison](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__confnote__36invfb_1_1ptcomparison/)**  |
| struct | **[ptJetComparison](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__confnote__36invfb_1_1ptjetcomparison/)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Analysis_CMS_13TeV_2OSLEP_confnote_36invfb](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__confnote__36invfb/#function-gambitcolliderbitanalysis-cms-13tev-2oslep-confnote-36invfb-analysis-cms-13tev-2oslep-confnote-36invfb)**() |
| virtual void | **[run](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__confnote__36invfb/#function-gambitcolliderbitanalysis-cms-13tev-2oslep-confnote-36invfb-run)**(const HEPUtils::Event * event) |
| virtual void | **[combine](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__confnote__36invfb/#function-gambitcolliderbitanalysis-cms-13tev-2oslep-confnote-36invfb-combine)**(const [Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/) * other)<br>Combine the variables of another copy of this analysis (typically on another thread) into this one.  |
| virtual void | **[collect_results](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__confnote__36invfb/#function-gambitcolliderbitanalysis-cms-13tev-2oslep-confnote-36invfb-collect-results)**()<br>Gather together the info for likelihood calculation.  |
| double | **[get_mjj](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__confnote__36invfb/#function-gambitcolliderbitanalysis-cms-13tev-2oslep-confnote-36invfb-get-mjj)**(vector< const HEPUtils::Jet * > jets) |
| double | **[get_mT2](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__confnote__36invfb/#function-gambitcolliderbitanalysis-cms-13tev-2oslep-confnote-36invfb-get-mt2)**(vector< const HEPUtils::Particle * > leptons, vector< const HEPUtils::Jet * > bjets, HEPUtils::P4 met) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| virtual void | **[analysis_specific_reset](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__confnote__36invfb/#function-gambitcolliderbitanalysis-cms-13tev-2oslep-confnote-36invfb-analysis-specific-reset)**()<br>Reset the analysis-specific variables.  |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| constexpr const char * | **[detector](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__confnote__36invfb/#variable-gambitcolliderbitanalysis-cms-13tev-2oslep-confnote-36invfb-detector)**  |
| struct [Gambit::ColliderBit::Analysis_CMS_13TeV_2OSLEP_confnote_36invfb::ptComparison](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__confnote__36invfb_1_1ptcomparison/) | **[comparePt](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__confnote__36invfb/#variable-gambitcolliderbitanalysis-cms-13tev-2oslep-confnote-36invfb-comparept)**  |
| struct [Gambit::ColliderBit::Analysis_CMS_13TeV_2OSLEP_confnote_36invfb::ptJetComparison](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__confnote__36invfb_1_1ptjetcomparison/) | **[compareJetPt](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__cms__13tev__2oslep__confnote__36invfb/#variable-gambitcolliderbitanalysis-cms-13tev-2oslep-confnote-36invfb-comparejetpt)**  |

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

### function Analysis_CMS_13TeV_2OSLEP_confnote_36invfb

```
inline Analysis_CMS_13TeV_2OSLEP_confnote_36invfb()
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


### function collect_results

```
inline virtual void collect_results()
```

Gather together the info for likelihood calculation. 

**Reimplements**: [Gambit::ColliderBit::Analysis::collect_results](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-gambitcolliderbitanalysis-collect-results)


### function get_mjj

```
inline double get_mjj(
    vector< const HEPUtils::Jet * > jets
)
```


### function get_mT2

```
inline double get_mT2(
    vector< const HEPUtils::Particle * > leptons,
    vector< const HEPUtils::Jet * > bjets,
    HEPUtils::P4 met
)
```


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


### variable comparePt

```
struct Gambit::ColliderBit::Analysis_CMS_13TeV_2OSLEP_confnote_36invfb::ptComparison comparePt;
```


### variable compareJetPt

```
struct Gambit::ColliderBit::Analysis_CMS_13TeV_2OSLEP_confnote_36invfb::ptJetComparison compareJetPt;
```


-------------------------------

Updated on 2022-09-08 at 01:48:55 +0000