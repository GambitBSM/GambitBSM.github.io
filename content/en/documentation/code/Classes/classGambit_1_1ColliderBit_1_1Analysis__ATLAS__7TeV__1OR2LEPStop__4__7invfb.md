---
title: "class Gambit::ColliderBit::Analysis_ATLAS_7TeV_1OR2LEPStop_4_7invfb"

description: "[No description available]"

---

# class Gambit::ColliderBit::Analysis_ATLAS_7TeV_1OR2LEPStop_4_7invfb



[No description available]

Inherits from [Gambit::ColliderBit::Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)

## Public Types

|                | Name           |
| -------------- | -------------- |
| enum| **[cutflowEnum](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__7tev__1or2lepstop__4__7invfb/)** { CUTFLOWMAP =(f)} |
| enum| **[varEnum](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__7tev__1or2lepstop__4__7invfb/)** { VARMAP =(f)} |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| std::vector< double > | **[calcNuPz](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__7tev__1or2lepstop__4__7invfb/)**(double Mw, P4 metMom, P4 lepMom) |
| P4 | **[getBestHadronicTop](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__7tev__1or2lepstop__4__7invfb/)**(std::vector< const Jet * > bJets, std::vector< const Jet * > lightJets, const P4 & leptonMom, const P4 & metMom, double width, double mean) |
| double | **[calcMt](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__7tev__1or2lepstop__4__7invfb/)**(P4 metVec, P4 lepVec) |
| double | **[calcSqrtSSubMin](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__7tev__1or2lepstop__4__7invfb/)**(P4 visibleSubsystem, P4 invisbleSubsystem) |
| void | **[getBJets](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__7tev__1or2lepstop__4__7invfb/)**(std::vector< const Jet * > & jets, std::vector< const Jet * > * bJets, std::vector< const Jet * > * lightJets) |
| | **[Analysis_ATLAS_7TeV_1OR2LEPStop_4_7invfb](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__7tev__1or2lepstop__4__7invfb/)**() |
| virtual void | **[run](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__7tev__1or2lepstop__4__7invfb/)**(const HEPUtils::Event * event) |
| virtual void | **[combine](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__7tev__1or2lepstop__4__7invfb/)**(const [Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/) * other)<br>Combine the variables of another copy of this analysis (typically on another thread) into this one.  |
| virtual void | **[collect_results](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__7tev__1or2lepstop__4__7invfb/)**()<br>Gather together the info for likelihood calculation.  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| virtual void | **[analysis_specific_reset](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__7tev__1or2lepstop__4__7invfb/)**()<br>Reset the analysis-specific variables.  |
| void | **[incrementCut](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__7tev__1or2lepstop__4__7invfb/)**(int cutIndex) |
| void | **[saveCutFlow](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__7tev__1or2lepstop__4__7invfb/)**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| constexpr const char * | **[detector](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__7tev__1or2lepstop__4__7invfb/)**  |
| const std::vector< std::string > | **[cutflowNames](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__7tev__1or2lepstop__4__7invfb/)**  |
| const std::vector< std::string > | **[varNames](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__7tev__1or2lepstop__4__7invfb/)**  |
| std::map< std::string, std::vector< double > > | **[varResults](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__7tev__1or2lepstop__4__7invfb/)**  |
| std::map< std::string, int > | **[cutflows](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__7tev__1or2lepstop__4__7invfb/)**  |
| double | **[num1LSR](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__7tev__1or2lepstop__4__7invfb/)**  |
| double | **[num2LSR1](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__7tev__1or2lepstop__4__7invfb/)**  |
| double | **[num2LSR2](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__7tev__1or2lepstop__4__7invfb/)**  |

## Additional inherited members

**Public Functions inherited from [Gambit::ColliderBit::Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)**

|                | Name           |
| -------------- | -------------- |
| void | **[analyze](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)**(const HEPUtils::Event & e)<br>Analyze the event (accessed by reference).  |
| void | **[analyze](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)**(const HEPUtils::Event * e)<br>Analyze the event (accessed by pointer).  |
| void | **[add](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)**([Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/) * other)<br>Add the results of another analysis to this one. Argument is not const, because the other needs to be able to gather its results if necessary.  |
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
| void | **[add_result](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)**(const [SignalRegionData](/documentation/code/classes/structgambit_1_1colliderbit_1_1signalregiondata/) & sr)<br>Add the given result to the internal results list.  |
| void | **[set_covariance](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)**(const Eigen::MatrixXd & srcov)<br>Set the covariance matrix, expressing SR correlations.  |
| void | **[set_covariance](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)**(const std::vector< std::vector< double > > & srcov)<br>A convenience function for setting the SR covariance from a nested vector/initialiser list.  |


## Public Types Documentation

### enum cutflowEnum

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| CUTFLOWMAP | =(f)|   |




### enum varEnum

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| VARMAP | =(f)|   |




## Public Functions Documentation

### function calcNuPz

```
inline std::vector< double > calcNuPz(
    double Mw,
    P4 metMom,
    P4 lepMom
)
```


### function getBestHadronicTop

```
inline P4 getBestHadronicTop(
    std::vector< const Jet * > bJets,
    std::vector< const Jet * > lightJets,
    const P4 & leptonMom,
    const P4 & metMom,
    double width,
    double mean
)
```


### function calcMt

```
inline double calcMt(
    P4 metVec,
    P4 lepVec
)
```


### function calcSqrtSSubMin

```
inline double calcSqrtSSubMin(
    P4 visibleSubsystem,
    P4 invisbleSubsystem
)
```


### function getBJets

```
inline void getBJets(
    std::vector< const Jet * > & jets,
    std::vector< const Jet * > * bJets,
    std::vector< const Jet * > * lightJets
)
```


We assume that b jets have previously been 100% tagged


### function Analysis_ATLAS_7TeV_1OR2LEPStop_4_7invfb

```
inline Analysis_ATLAS_7TeV_1OR2LEPStop_4_7invfb()
```


The constructor that should initialize some variables 


### function run

```
inline virtual void run(
    const HEPUtils::Event * event
)
```


**Parameters**: 

  * **event** an event contain particle and jet information 


**Reimplements**: [Gambit::ColliderBit::Analysis::run](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)


Performs the main part of the analysis 


### function combine

```
inline virtual void combine(
    const Analysis * other
)
```

Combine the variables of another copy of this analysis (typically on another thread) into this one. 

**Parameters**: 

  * **other** results from another thread 


**Reimplements**: [Gambit::ColliderBit::Analysis::combine](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)


Adds results from other threads if OMP_NUM_THREAD != 1 


### function collect_results

```
inline virtual void collect_results()
```

Gather together the info for likelihood calculation. 

**Reimplements**: [Gambit::ColliderBit::Analysis::collect_results](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)


## Protected Functions Documentation

### function analysis_specific_reset

```
inline virtual void analysis_specific_reset()
```

Reset the analysis-specific variables. 

**Reimplements**: [Gambit::ColliderBit::Analysis::analysis_specific_reset](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)


### function incrementCut

```
inline void incrementCut(
    int cutIndex
)
```


### function saveCutFlow

```
inline void saveCutFlow()
```


## Public Attributes Documentation

### variable detector

```
static constexpr const char * detector = "ATLAS";
```


### variable cutflowNames

```
const std::vector< std::string > cutflowNames = {CUTFLOWMAP(g)};
```


### variable varNames

```
const std::vector< std::string > varNames = {VARMAP(g)};
```


### variable varResults

```
std::map< std::string, std::vector< double > > varResults;
```


### variable cutflows

```
std::map< std::string, int > cutflows;
```


### variable num1LSR

```
double num1LSR =0;
```


### variable num2LSR1

```
double num2LSR1 =0;
```


### variable num2LSR2

```
double num2LSR2 =0;
```


-------------------------------

Updated on 2022-09-08 at 01:05:17 +0000