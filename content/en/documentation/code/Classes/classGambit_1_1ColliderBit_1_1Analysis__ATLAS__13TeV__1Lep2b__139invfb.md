---
title: "class Gambit::ColliderBit::Analysis_ATLAS_13TeV_1Lep2b_139invfb"

description: "[No description available]"

---

# class Gambit::ColliderBit::Analysis_ATLAS_13TeV_1Lep2b_139invfb



[No description available]

Inherits from [Gambit::ColliderBit::Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Analysis_ATLAS_13TeV_1Lep2b_139invfb](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__1lep2b__139invfb/#function-analysis-atlas-13tev-1lep2b-139invfb)**() |
| void | **[LeptonJetOverlapRemoval](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__1lep2b__139invfb/#function-leptonjetoverlapremoval)**(vector< const HEPUtils::Particle * > & leptons, vector< const HEPUtils::Jet * > & jets) |
| void | **[JetLeptonOverlapRemoval](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__1lep2b__139invfb/#function-jetleptonoverlapremoval)**(vector< const HEPUtils::Jet * > & jets, vector< const HEPUtils::Particle * > & leptons, double DeltaRMax) |
| void | **[ParticleOverlapRemoval](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__1lep2b__139invfb/#function-particleoverlapremoval)**(vector< const HEPUtils::Particle * > & particles1, vector< const HEPUtils::Particle * > & particles2, double DeltaRMax) |
| bool | **[sortJetsByPt](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__1lep2b__139invfb/#function-sortjetsbypt)**(const HEPUtils::Jet * jet1, const HEPUtils::Jet * jet2) |
| virtual void | **[run](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__1lep2b__139invfb/#function-run)**(const HEPUtils::Event * event) |
| virtual void | **[combine](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__1lep2b__139invfb/#function-combine)**(const [Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/) * other)<br>Combine the variables of another copy of this analysis (typically on another thread) into this one.  |
| virtual void | **[collect_results](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__1lep2b__139invfb/#function-collect-results)**()<br>Gather together the info for likelihood calculation.  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| virtual void | **[analysis_specific_reset](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__1lep2b__139invfb/#function-analysis-specific-reset)**()<br>Reset the analysis-specific variables.  |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| std::map< string, [EventCounter](/documentation/code/classes/classgambit_1_1colliderbit_1_1eventcounter/) > | **[_counters](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__1lep2b__139invfb/#variable-counters)**  |
| constexpr const char * | **[detector](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__1lep2b__139invfb/#variable-detector)**  |

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

### function Analysis_ATLAS_13TeV_1Lep2b_139invfb

```
inline Analysis_ATLAS_13TeV_1Lep2b_139invfb()
```


### function LeptonJetOverlapRemoval

```
inline void LeptonJetOverlapRemoval(
    vector< const HEPUtils::Particle * > & leptons,
    vector< const HEPUtils::Jet * > & jets
)
```


### function JetLeptonOverlapRemoval

```
inline void JetLeptonOverlapRemoval(
    vector< const HEPUtils::Jet * > & jets,
    vector< const HEPUtils::Particle * > & leptons,
    double DeltaRMax
)
```


### function ParticleOverlapRemoval

```
inline void ParticleOverlapRemoval(
    vector< const HEPUtils::Particle * > & particles1,
    vector< const HEPUtils::Particle * > & particles2,
    double DeltaRMax
)
```


### function sortJetsByPt

```
inline bool sortJetsByPt(
    const HEPUtils::Jet * jet1,
    const HEPUtils::Jet * jet2
)
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


## Protected Functions Documentation

### function analysis_specific_reset

```
inline virtual void analysis_specific_reset()
```

Reset the analysis-specific variables. 

**Reimplements**: [Gambit::ColliderBit::Analysis::analysis_specific_reset](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-analysis-specific-reset)


## Public Attributes Documentation

### variable _counters

```
std::map< string, EventCounter > _counters = {
        {"WREM_cuts_0", EventCounter("WREM_cuts_0")},
        {"STCREM_cuts_0", EventCounter("STCREM_cuts_0")},
        {"TRHMEM_cuts_0", EventCounter("TRHMEM_cuts_0")},
        {"TRMMEM_cuts_0", EventCounter("TRMMEM_cuts_0")},
        {"TRLMEM_cuts_0", EventCounter("TRLMEM_cuts_0")},
        {"SRHMEM_mct2_0", EventCounter("SRHMEM_mct2_0")},
        {"SRHMEM_mct2_1", EventCounter("SRHMEM_mct2_1")},
        {"SRHMEM_mct2_2", EventCounter("SRHMEM_mct2_2")},
        {"SRMMEM_mct2_0", EventCounter("SRMMEM_mct2_0")},
        {"SRMMEM_mct2_1", EventCounter("SRMMEM_mct2_1")},
        {"SRMMEM_mct2_2", EventCounter("SRMMEM_mct2_2")},
        {"SRLMEM_mct2_0", EventCounter("SRLMEM_mct2_0")},
        {"SRLMEM_mct2_1", EventCounter("SRLMEM_mct2_1")},
        {"SRLMEM_mct2_2", EventCounter("SRLMEM_mct2_2")},
      };
```


### variable detector

```
static constexpr const char * detector = "ATLAS";
```


-------------------------------

Updated on 2025-02-12 at 15:36:38 +0000