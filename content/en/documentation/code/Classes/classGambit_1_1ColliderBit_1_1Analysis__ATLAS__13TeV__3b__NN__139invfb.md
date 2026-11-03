---
title: "class Gambit::ColliderBit::Analysis_ATLAS_13TeV_3b_NN_139invfb"

description: "[No description available]"

---

# class Gambit::ColliderBit::Analysis_ATLAS_13TeV_3b_NN_139invfb



[No description available]

Inherits from [Gambit::ColliderBit::Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| double | **[JVT_eff](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__3b__nn__139invfb/#function-jvt-eff)**(const Jet & j) |
| double | **[JVT_eff](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__3b__nn__139invfb/#function-jvt-eff)**(const Jet * j) |
| void | **[apply_JVT](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__3b__nn__139invfb/#function-apply-jvt)**(const vector< const Jet * > & jsIn, vector< const Jet * > & jsOut) |
| void | **[trimJets](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__3b__nn__139invfb/#function-trimjets)**(const vector< FJNS::PseudoJet > & pjs_in, vector< Jet > & js_out, const double frac =0.1, const double minPt =0., const double maxEta =6., const double minPt_twosubJets =0.) |
| double | **[transverse_mass](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__3b__nn__139invfb/#function-transverse-mass)**(HEPUtils::P4 pmiss, HEPUtils::P4 p4) |
| void | **[normalise_nn_kinematics](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__3b__nn__139invfb/#function-normalise-nn-kinematics)**(vector< float > & nn_inputs) const |
| void | **[normalise_nn_parameters](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__3b__nn__139invfb/#function-normalise-nn-parameters)**(vector< float > & nn_inputs) const |
| | **[Analysis_ATLAS_13TeV_3b_NN_139invfb](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__3b__nn__139invfb/#function-analysis-atlas-13tev-3b-nn-139invfb)**() |
| virtual void | **[run](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__3b__nn__139invfb/#function-run)**(const HEPUtils::Event * event) |
| void | **[combine](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__3b__nn__139invfb/#function-combine)**(const [Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/) * other)<br>Combine the variables of another copy of this analysis (typically on another thread) into this one.  |
| virtual void | **[collect_results](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__3b__nn__139invfb/#function-collect-results)**()<br>Gather together the info for likelihood calculation.  |
| virtual void | **[analysis_specific_reset](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__3b__nn__139invfb/#function-analysis-specific-reset)**()<br>Reset the analysis-specific variables.  |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| constexpr const char * | **[detector](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__3b__nn__139invfb/#variable-detector)**  |
| const vector< float > | **[_normalisation_means](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__3b__nn__139invfb/#variable-normalisation-means)**  |
| const vector< float > | **[_normalisation_devs](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__3b__nn__139invfb/#variable-normalisation-devs)**  |
| const vector< pair< size_t, size_t > > | **[_gtt_param_points](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__3b__nn__139invfb/#variable-gtt-param-points)**  |
| const vector< pair< size_t, size_t > > | **[_gbb_param_points](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__3b__nn__139invfb/#variable-gbb-param-points)**  |

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

### function JVT_eff

```
static inline double JVT_eff(
    const Jet & j
)
```


### function JVT_eff

```
static inline double JVT_eff(
    const Jet * j
)
```


### function apply_JVT

```
static inline void apply_JVT(
    const vector< const Jet * > & jsIn,
    vector< const Jet * > & jsOut
)
```


### function trimJets

```
static inline void trimJets(
    const vector< FJNS::PseudoJet > & pjs_in,
    vector< Jet > & js_out,
    const double frac =0.1,
    const double minPt =0.,
    const double maxEta =6.,
    const double minPt_twosubJets =0.
)
```


### function transverse_mass

```
static inline double transverse_mass(
    HEPUtils::P4 pmiss,
    HEPUtils::P4 p4
)
```


### function normalise_nn_kinematics

```
inline void normalise_nn_kinematics(
    vector< float > & nn_inputs
) const
```


### function normalise_nn_parameters

```
inline void normalise_nn_parameters(
    vector< float > & nn_inputs
) const
```


### function Analysis_ATLAS_13TeV_3b_NN_139invfb

```
inline Analysis_ATLAS_13TeV_3b_NN_139invfb()
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
inline void combine(
    const Analysis * other
)
```

Combine the variables of another copy of this analysis (typically on another thread) into this one. 

### function collect_results

```
inline virtual void collect_results()
```

Gather together the info for likelihood calculation. 

**Reimplements**: [Gambit::ColliderBit::Analysis::collect_results](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/#function-collect-results)


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


### variable _normalisation_means

```
const vector< float > _normalisation_means = {348.82672119140625, 0.001224843435920775, 0.011215382255613804, 35.01051712036133, 0.4123765528202057, 205.96482849121094, 0.000866758287884295, 0.0026113702915608883, 21.943532943725586, 0.5219350457191467, 131.5203399658203, 0.0014234248083084822, 0.0028221921529620886, 14.679434776306152, 0.4859117269515991, 89.95111083984375, 0.0024308657739311457, 0.003201194340363145, 10.921121597290039, 0.41861748695373535, 51.72813415527344, 0.002211648505181074, 0.001059219939634204, 6.8958611488342285, 0.2480594962835312, 29.507577896118164, 0.0014721028273925185, 0.0011491943150758743, 4.127583026885986, 0.1373944729566574, 16.116954803466797, 0.0008737104362808168, 0.0005380049697123468, 2.326930522918701, 0.07252819091081619, 8.416145324707031, 0.000563444453291595, 0.0004173719498794526, 1.2422566413879395, 0.036873701959848404, 4.170749664306641, 0.0005186111084185541, 0.0001961462403414771, 0.6271772384643555, 0.017829529941082, 1.9352974891662598, 2.8667405786109157e-05, 0.00025558529887348413, 0.2950354516506195, 0.008070512674748898, 388.2679443359375, 0.0005678863381035626, 0.010501296259462833, 75.08436584472656, 201.22515869140625, 0.0007426381343975663, -0.0012021028669551015, 37.745521545410156, 86.0351333618164, 0.0001722413144307211, 0.00024551310343667865, 14.23154354095459, 28.54050636291504, 7.828087836969644e-05, 0.0004572096804622561, 4.361158847808838, 52.769752502441406, 0.00055172317661345, -0.004927645903080702, 0.03030405007302761, 3.7328639030456543, 3.698996079037897e-05, 9.778635285329074e-05, 0.0030516863334923983, 0.23780983686447144, -1.23310519484221e-05, -5.973678707960062e-05, 0.0002457579248584807, 0.009709575213491917, -7.139377089515619e-07, 9.422020411875565e-06, 1.2358904314169195e-05, 272.284423828125, 3.157931327819824, 0.5684433579444885, 1924.33984375, 813.9981079101562};
```


### variable _normalisation_devs

```
const vector< float > _normalisation_devs = {260.26678466796875, 1.043735384941101, 1.8061413764953613, 31.465930938720703, 0.48998895287513733, 158.85206604003906, 1.0634719133377075, 1.8049265146255493, 19.196178436279297, 0.49979639053344727, 95.81076049804688, 1.1140797138214111, 1.8063502311706543, 10.480488777160645, 0.499955415725708, 61.92335510253906, 1.1796157360076904, 1.806037187576294, 6.566783428192139, 0.48769065737724304, 46.49405288696289, 1.0528481006622314, 1.561020016670227, 5.663470268249512, 0.41597431898117065, 36.96717834472656, 0.8779095411300659, 1.279522180557251, 4.860283851623535, 0.33421754837036133, 28.791873931884766, 0.6928571462631226, 1.0022454261779785, 3.9111227989196777, 0.25323963165283203, 19.419239044189453, 0.5242016315460205, 0.7574199438095093, 2.817417860031128, 0.1853451132774353, 13.448785781860352, 0.3827989995479584, 0.5529165267944336, 2.029693365097046, 0.13118404150009155, 9.043235778808594, 0.26963910460472107, 0.3887377977371216, 1.4025100469589233, 0.08914224058389664, 286.4169921875, 0.8792079091072083, 1.7478116750717163, 76.41952514648438, 198.80892944335938, 0.7650731801986694, 1.5172309875488281, 50.877689361572266, 126.01263427734375, 0.6058558821678162, 1.156052827835083, 26.713064193725586, 68.72575378417969, 0.40241798758506775, 0.740081787109375, 13.1954927444458, 83.16204071044922, 0.7241584062576294, 1.3046456575393677, 0.05489525943994522, 19.12066078186035, 0.24320338666439056, 0.42904603481292725, 0.01846902072429657, 4.206113815307617, 0.07045941799879074, 0.12233318388462067, 0.005232449620962143, 0.7187768816947937, 0.016513027250766754, 0.027744540944695473, 0.001166886300779879, 239.20870971679688, 1.8090277910232544, 0.48885977268218994, 471.8238525390625, 555.2835693359375};
```


### variable _gtt_param_points

```
const vector< pair< size_t, size_t > > _gtt_param_points {{1900,1400}, {1800,1}, {2100,1}, {2300,1200}};
```


### variable _gbb_param_points

```
const vector< pair< size_t, size_t > > _gbb_param_points {{2000,1800}, {2100,1600}, {2300,1000}, {2800,1400}};
```


-------------------------------

Updated on 2026-11-03 at 14:50:43 +0000