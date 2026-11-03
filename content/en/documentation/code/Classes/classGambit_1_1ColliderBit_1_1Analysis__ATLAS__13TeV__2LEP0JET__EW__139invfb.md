---
title: "class Gambit::ColliderBit::Analysis_ATLAS_13TeV_2LEP0JET_EW_139invfb"

description: "[No description available]"

---

# class Gambit::ColliderBit::Analysis_ATLAS_13TeV_2LEP0JET_EW_139invfb



[No description available]

Inherits from [Gambit::ColliderBit::Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)

## Public Classes

|                | Name           |
| -------------- | -------------- |
| struct | **[pt_sort](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysis__atlas__13tev__2lep0jet__ew__139invfb_1_1pt__sort/)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Analysis_ATLAS_13TeV_2LEP0JET_EW_139invfb](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__2lep0jet__ew__139invfb/#function-analysis-atlas-13tev-2lep0jet-ew-139invfb)**() |
| void | **[addMVABDT](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__2lep0jet__ew__139invfb/#function-addmvabdt)**(const std::string & name, const std::string & fname1, const std::string & fname2) |
| virtual [MVA](/documentation/code/classes/classmva/) * | **[getMVA](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__2lep0jet__ew__139invfb/#function-getmva)**(const std::string & name) |
| vector< const Particle * > | **[filterLeptons](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__2lep0jet__ew__139invfb/#function-filterleptons)**(vector< const Particle * > & cands, float ptCut, float etaCut) |
| vector< const Jet * > | **[filterJets](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__2lep0jet__ew__139invfb/#function-filterjets)**(vector< const Jet * > & cands, float ptCut, float etaCut) |
| void | **[sortObjectsByPt](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__2lep0jet__ew__139invfb/#function-sortobjectsbypt)**(vector< const Particle * > & cands) |
| int | **[countObjects](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__2lep0jet__ew__139invfb/#function-countobjects)**(vector< const Particle * > & cands, float ptCut, float etaCut) |
| int | **[countObjects](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__2lep0jet__ew__139invfb/#function-countobjects)**(vector< const Jet * > & cands, float ptCut, float etaCut) |
| float | **[calcMT2](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__2lep0jet__ew__139invfb/#function-calcmt2)**(const Particle & o1, const Particle & o2, const P4 & met) |
| float | **[calcAMT2](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__2lep0jet__ew__139invfb/#function-calcamt2)**(const Particle & o1, const Particle & o2, const P4 & met, float m1, float m2) |
| float | **[calcMTauTau](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__2lep0jet__ew__139invfb/#function-calcmtautau)**(const Particle & o1, const Particle & o2, const P4 & met) |
| vector< const Particle * > | **[LeptonLeptonOverlapRemoval](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__2lep0jet__ew__139invfb/#function-leptonleptonoverlapremoval)**(vector< const Particle * > & cands, vector< const Particle * > & others, std::function< float(const Particle *, const Particle *)> radiusFunc) |
| vector< const Jet * > | **[JetLeptonOverlapRemoval](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__2lep0jet__ew__139invfb/#function-jetleptonoverlapremoval)**(vector< const Jet * > & cands, vector< const Particle * > & others, std::function< float(const Jet *, const Particle *)> radiusFunc) |
| vector< const Particle * > | **[LeptonJetOverlapRemoval](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__2lep0jet__ew__139invfb/#function-leptonjetoverlapremoval)**(vector< const Particle * > & cands, vector< const Jet * > & others, std::function< float(const Particle *, const Jet *)> radiusFunc) |
| vector< const Particle * > | **[LeptonLeptonOverlapRemoval](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__2lep0jet__ew__139invfb/#function-leptonleptonoverlapremoval)**(vector< const Particle * > & cands, vector< const Particle * > & others, float deltaR) |
| vector< const Jet * > | **[JetLeptonOverlapRemoval](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__2lep0jet__ew__139invfb/#function-jetleptonoverlapremoval)**(vector< const Jet * > & cands, vector< const Particle * > & others, float deltaR) |
| vector< const Particle * > | **[LeptonJetOverlapRemoval](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__2lep0jet__ew__139invfb/#function-leptonjetoverlapremoval)**(vector< const Particle * > & cands, vector< const Jet * > & others, float deltaR) |
| double | **[calcMETSignificance](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__2lep0jet__ew__139invfb/#function-calcmetsignificance)**(vector< const Particle * > & electrons, vector< const Particle * > & photons, vector< const Particle * > & muons, vector< const Jet * > & jets, vector< const Particle * > & taus, HEPUtils::P4 & metVec, double met) |
| double | **[calcMETSignificance](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__2lep0jet__ew__139invfb/#function-calcmetsignificance)**(const HEPUtils::Event & event, bool applyOverlapRemoval) |
| vector< const Particle * > | **[getObjects](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__2lep0jet__ew__139invfb/#function-getobjects)**(const HEPUtils::Event * event, std::string type, double ptcut, double etacut) |
| vector< const Jet * > | **[getJets](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__2lep0jet__ew__139invfb/#function-getjets)**(const HEPUtils::Event * event, double ptcut, double etacut) |
| virtual void | **[run](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__2lep0jet__ew__139invfb/#function-run)**(const HEPUtils::Event * event)<br>Main Run Function.  |
| virtual void | **[collect_results](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__2lep0jet__ew__139invfb/#function-collect-results)**()<br>Register results objects with the results for each SR; obs & bkg numbers from the CONF note.  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| virtual void | **[analysis_specific_reset](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__2lep0jet__ew__139invfb/#function-analysis-specific-reset)**()<br>Reset the analysis-specific variables.  |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| constexpr const char * | **[detector](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__2lep0jet__ew__139invfb/#variable-detector)**  |

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
| void | **[set_detector_name](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-set-detector-name)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) detname)<br>Set the detector name.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[detector_name](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-detector-name)**()<br>Get the detector name.  |
| void | **[set_collider_name](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-set-collider-name)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) collname)<br>Set the collider name.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[collider_name](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-collider-name)**()<br>Get the collider name.  |
| const [AnalysisData](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysisdata/) & | **[get_results](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-get-results)**()<br>Get the collection of [SignalRegionData]() for likelihood computation.  |
| const [AnalysisData](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysisdata/) & | **[get_results](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-get-results)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) & warning)<br>An overload of [get_results()](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-get-results) with some additional consistency checks.  |
| [AnalysisData](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysisdata/) * | **[get_results_ptr](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-get-results-ptr)**()<br>Get a (non-const!) pointer to _results.  |
| [AnalysisData](/documentation/code/classes/structgambit_1_1colliderbit_1_1analysisdata/) * | **[get_results_ptr](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-get-results-ptr)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) & warning)<br>An overload of [get_results_ptr()](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-get-results-ptr) with some additional consistency checks.  |
| const [Cutflows](/documentation/code/classes/structgambit_1_1colliderbit_1_1cutflows/) & | **[get_cutflows](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-get-cutflows)**()<br>Get the cutflows.  |
| void | **[scale](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-scale)**(double xsec_per_event)<br>Scale by xsec per event.  |
| void | **[set_store_accepted_event_IDs](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-set-store-accepted-event-ids)**(bool setting)<br>Set the store_accepted_event_IDs bool for the [EventCounter]() instances in this analysis.  |
| void | **[addCuts](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-addcuts)**(std::vector< std::string > & ) |
| template <typename First ,typename... Rest\> <br>void | **[addCuts](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-addcuts)**(std::vector< std::string > & v, First && first, Rest &&... rest) |
| template <typename... Cuts\> <br>void | **[defineSignalRegion](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-definesignalregion)**(const std::string & name, Cuts &&... cuts) |
| template <typename... Cuts\> <br>void | **[defineSignalRegions](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-definesignalregions)**(const std::string & baseName, int count, const Cuts &... cuts) |

**Protected Functions inherited from [Gambit::ColliderBit::Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)**

|                | Name           |
| -------------- | -------------- |
| void | **[add_result](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-add-result)**(const [SignalRegionData](/documentation/code/classes/structgambit_1_1colliderbit_1_1signalregiondata/) & sr)<br>Add the given result to the internal results list.  |
| void | **[add_cutflows](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-add-cutflows)**(const [Cutflows](/documentation/code/classes/structgambit_1_1colliderbit_1_1cutflows/) & cf)<br>Add cutflows to the internal results list.  |
| void | **[set_covariance](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-set-covariance)**(const Eigen::MatrixXd & srcov)<br>Set the covariance matrix, expressing SR correlations.  |
| void | **[set_covariance](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-set-covariance)**(const std::vector< std::vector< double > > & srcov)<br>A convenience function for setting the SR covariance from a nested vector/initialiser list.  |
| void | **[set_bkgjson](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-set-bkgjson)**(const std::string & bkgpath)<br>A convenience function for setting the path to the [ATLAS]() FullLikes BKG Json file.  |

**Protected Attributes inherited from [Gambit::ColliderBit::Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)**

|                | Name           |
| -------------- | -------------- |
| [Cutflows](/documentation/code/classes/structgambit_1_1colliderbit_1_1cutflows/) | **[_cutflows](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#variable-cutflows)**  |
| std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), [EventCounter](/documentation/code/classes/classgambit_1_1colliderbit_1_1eventcounter/) > & | **[_counters](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#variable-counters)**  |


## Public Functions Documentation

### function Analysis_ATLAS_13TeV_2LEP0JET_EW_139invfb

```
inline Analysis_ATLAS_13TeV_2LEP0JET_EW_139invfb()
```


### function addMVABDT

```
inline void addMVABDT(
    const std::string & name,
    const std::string & fname1,
    const std::string & fname2
)
```


### function getMVA

```
inline virtual MVA * getMVA(
    const std::string & name
)
```


### function filterLeptons

```
inline vector< const Particle * > filterLeptons(
    vector< const Particle * > & cands,
    float ptCut,
    float etaCut
)
```


### function filterJets

```
inline vector< const Jet * > filterJets(
    vector< const Jet * > & cands,
    float ptCut,
    float etaCut
)
```


### function sortObjectsByPt

```
inline void sortObjectsByPt(
    vector< const Particle * > & cands
)
```


### function countObjects

```
inline int countObjects(
    vector< const Particle * > & cands,
    float ptCut,
    float etaCut
)
```


### function countObjects

```
inline int countObjects(
    vector< const Jet * > & cands,
    float ptCut,
    float etaCut
)
```


### function calcMT2

```
inline float calcMT2(
    const Particle & o1,
    const Particle & o2,
    const P4 & met
)
```


### function calcAMT2

```
inline float calcAMT2(
    const Particle & o1,
    const Particle & o2,
    const P4 & met,
    float m1,
    float m2
)
```


### function calcMTauTau

```
inline float calcMTauTau(
    const Particle & o1,
    const Particle & o2,
    const P4 & met
)
```


### function LeptonLeptonOverlapRemoval

```
inline vector< const Particle * > LeptonLeptonOverlapRemoval(
    vector< const Particle * > & cands,
    vector< const Particle * > & others,
    std::function< float(const Particle *, const Particle *)> radiusFunc
)
```


### function JetLeptonOverlapRemoval

```
inline vector< const Jet * > JetLeptonOverlapRemoval(
    vector< const Jet * > & cands,
    vector< const Particle * > & others,
    std::function< float(const Jet *, const Particle *)> radiusFunc
)
```


### function LeptonJetOverlapRemoval

```
inline vector< const Particle * > LeptonJetOverlapRemoval(
    vector< const Particle * > & cands,
    vector< const Jet * > & others,
    std::function< float(const Particle *, const Jet *)> radiusFunc
)
```


### function LeptonLeptonOverlapRemoval

```
inline vector< const Particle * > LeptonLeptonOverlapRemoval(
    vector< const Particle * > & cands,
    vector< const Particle * > & others,
    float deltaR
)
```


### function JetLeptonOverlapRemoval

```
inline vector< const Jet * > JetLeptonOverlapRemoval(
    vector< const Jet * > & cands,
    vector< const Particle * > & others,
    float deltaR
)
```


### function LeptonJetOverlapRemoval

```
inline vector< const Particle * > LeptonJetOverlapRemoval(
    vector< const Particle * > & cands,
    vector< const Jet * > & others,
    float deltaR
)
```


### function calcMETSignificance

```
inline double calcMETSignificance(
    vector< const Particle * > & electrons,
    vector< const Particle * > & photons,
    vector< const Particle * > & muons,
    vector< const Jet * > & jets,
    vector< const Particle * > & taus,
    HEPUtils::P4 & metVec,
    double met
)
```


### function calcMETSignificance

```
inline double calcMETSignificance(
    const HEPUtils::Event & event,
    bool applyOverlapRemoval
)
```


### function getObjects

```
inline vector< const Particle * > getObjects(
    const HEPUtils::Event * event,
    std::string type,
    double ptcut,
    double etacut
)
```


### function getJets

```
inline vector< const Jet * > getJets(
    const HEPUtils::Event * event,
    double ptcut,
    double etacut
)
```


### function run

```
inline virtual void run(
    const HEPUtils::Event * event
)
```

Main Run Function. 

**Reimplements**: [Gambit::ColliderBit::Analysis::run](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-run)


### function collect_results

```
inline virtual void collect_results()
```

Register results objects with the results for each SR; obs & bkg numbers from the CONF note. 

**Reimplements**: [Gambit::ColliderBit::Analysis::collect_results](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-collect-results)


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


-------------------------------

Updated on 2026-11-03 at 14:50:42 +0000