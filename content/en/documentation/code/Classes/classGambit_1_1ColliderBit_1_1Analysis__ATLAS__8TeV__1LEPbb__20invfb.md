---
title: "class Gambit::ColliderBit::Analysis_ATLAS_8TeV_1LEPbb_20invfb"

description: "[No description available]"

---

# class Gambit::ColliderBit::Analysis_ATLAS_8TeV_1LEPbb_20invfb



[No description available]

Inherits from [Gambit::ColliderBit::Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)

## Public Classes

|                | Name           |
| -------------- | -------------- |
| struct | **[jetComparison](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysis__atlas__8tev__1lepbb__20invfb_1_1jetcomparison/)**  |
| struct | **[particleComparison](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysis__atlas__8tev__1lepbb__20invfb_1_1particlecomparison/)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Analysis_ATLAS_8TeV_1LEPbb_20invfb](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__8tev__1lepbb__20invfb/#function-analysis-atlas-8tev-1lepbb-20invfb)**() |
| virtual void | **[run](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__8tev__1lepbb__20invfb/#function-run)**(const HEPUtils::Event * event) |
| virtual void | **[combine](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__8tev__1lepbb__20invfb/#function-combine)**(const [Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/) * other)<br>Combine the variables of another copy of this analysis (typically on another thread) into this one.  |
| virtual void | **[collect_results](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__8tev__1lepbb__20invfb/#function-collect-results)**()<br>Gather together the info for likelihood calculation.  |
| bool | **[isLeadingBJets](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__8tev__1lepbb__20invfb/#function-isleadingbjets)**(vector< const HEPUtils::Jet * > jets, vector< const HEPUtils::Jet * > bjets) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| virtual void | **[analysis_specific_reset](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__8tev__1lepbb__20invfb/#function-analysis-specific-reset)**()<br>Reset the analysis-specific variables.  |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| constexpr const char * | **[detector](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__8tev__1lepbb__20invfb/#variable-detector)**  |
| struct [Gambit::ColliderBit::Analysis_ATLAS_8TeV_1LEPbb_20invfb::particleComparison](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysis__atlas__8tev__1lepbb__20invfb_1_1particlecomparison/) | **[compareParticlePt](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__8tev__1lepbb__20invfb/#variable-compareparticlept)**  |
| struct [Gambit::ColliderBit::Analysis_ATLAS_8TeV_1LEPbb_20invfb::jetComparison](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysis__atlas__8tev__1lepbb__20invfb_1_1jetcomparison/) | **[compareJetPt](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__8tev__1lepbb__20invfb/#variable-comparejetpt)**  |

## Additional inherited members

**Public Functions inherited from [Gambit::ColliderBit::Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)**

|                | Name           |
| -------------- | -------------- |
| void | **[analyze](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-analyze)**(const HEPUtils::Event & e)<br>Analyze the event (accessed by reference).  |
| void | **[analyze](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-analyze)**(const HEPUtils::Event * e)<br>Analyze the event (accessed by pointer).  |
| void | **[add](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-add)**([Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/) * other)<br>Add the results of another analysis to this one. Argument is not const, because the other needs to be able to gather its results if necessary.  |
| | **[Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-analysis)**()<br>Construction.  |
| virtual | **[~Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-analysis)**()<br>Destruction.  |
| void | **[reset](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-reset)**()<br>Public method to reset this instance for reuse, avoiding the need for "new" or "delete".  |
| double | **[luminosity](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-luminosity)**() const<br>Return the integrated luminosity.  |
| void | **[set_luminosity](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-set-luminosity)**(double lumi)<br>Set the integrated luminosity.  |
| void | **[set_analysis_name](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-set-analysis-name)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) aname)<br>Set the analysis name.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[analysis_name](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-analysis-name)**()<br>Get the analysis name.  |
| const [AnalysisData](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysisdata/) & | **[get_results](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-get-results)**()<br>Get the collection of [SignalRegionData]() for likelihood computation.  |
| const [AnalysisData](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysisdata/) & | **[get_results](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-get-results)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) & warning)<br>An overload of [get_results()](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-get-results) with some additional consistency checks.  |
| [AnalysisData](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysisdata/) * | **[get_results_ptr](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-get-results-ptr)**()<br>Get a (non-const!) pointer to _results.  |
| [AnalysisData](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysisdata/) * | **[get_results_ptr](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-get-results-ptr)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) & warning)<br>An overload of [get_results_ptr()](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-get-results-ptr) with some additional consistency checks.  |
| void | **[scale](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-scale)**(double xsec_per_event)<br>Scale by xsec per event.  |

**Protected Functions inherited from [Gambit::ColliderBit::Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)**

|                | Name           |
| -------------- | -------------- |
| void | **[add_result](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-add-result)**(const [SignalRegionData](/documentation/code/classes/structgambit_1_1colliderbit_1_1signalregiondata/) & sr)<br>Add the given result to the internal results list.  |
| void | **[set_covariance](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-set-covariance)**(const Eigen::MatrixXd & srcov)<br>Set the covariance matrix, expressing SR correlations.  |
| void | **[set_covariance](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-set-covariance)**(const std::vector< std::vector< double > > & srcov)<br>A convenience function for setting the SR covariance from a nested vector/initialiser list.  |
| void | **[set_bkgjson](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-set-bkgjson)**(const std::string & bkgpath)<br>A convenience function for setting the path to the [ATLAS]() FullLikes BKG Json file.  |


## Public Functions Documentation

### function Analysis_ATLAS_8TeV_1LEPbb_20invfb

```
inline Analysis_ATLAS_8TeV_1LEPbb_20invfb()
```


### function run

```
inline virtual void run(
    const HEPUtils::Event * event
)
```


**Reimplements**: [Gambit::ColliderBit::Analysis::run](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-run)


### function combine

```
inline virtual void combine(
    const Analysis * other
)
```

Combine the variables of another copy of this analysis (typically on another thread) into this one. 

**Reimplements**: [Gambit::ColliderBit::Analysis::combine](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-combine)


### function collect_results

```
inline virtual void collect_results()
```

Gather together the info for likelihood calculation. 

**Reimplements**: [Gambit::ColliderBit::Analysis::collect_results](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-collect-results)


### function isLeadingBJets

```
inline bool isLeadingBJets(
    vector< const HEPUtils::Jet * > jets,
    vector< const HEPUtils::Jet * > bjets
)
```


## Protected Functions Documentation

### function analysis_specific_reset

```
inline virtual void analysis_specific_reset()
```

Reset the analysis-specific variables. 

**Reimplements**: [Gambit::ColliderBit::Analysis::analysis_specific_reset](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-analysis-specific-reset)


## Public Attributes Documentation

### variable detector

```
static constexpr const char * detector = "ATLAS";
```


### variable compareParticlePt

```
struct Gambit::ColliderBit::Analysis_ATLAS_8TeV_1LEPbb_20invfb::particleComparison compareParticlePt;
```


### variable compareJetPt

```
struct Gambit::ColliderBit::Analysis_ATLAS_8TeV_1LEPbb_20invfb::jetComparison compareJetPt;
```


-------------------------------

Updated on 2025-02-12 at 16:10:31 +0000