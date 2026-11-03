---
title: "namespace Gambit::ColliderBit::CMS"
description: "CMS-specific efficiency and smearing functions for super fast detector simulation. "

---

# namespace Gambit::ColliderBit::CMS

CMS-specific efficiency and smearing functions for super fast detector simulation. 

## Functions

|                | Name           |
| -------------- | -------------- |
| const HEPUtils::BinnedFn2D< double > | **[eff2DTau_SUS_16_039](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-eff2dtau-sus-16-039)**({0., 2.3} , {0., 25., 30., 35., 40., 45., 50., 60., 70., 80., DBL_MAX} , {0.38 *0.95, 0.48 *0.95, 0.5 *0.95, 0.49 *0.95, 0.51 *0.95, 0.49 *0.95, 0.47 *0.95, 0.45 *0.95, 0.48 *0.95, 0.5 *0.95} ) |
| const HEPUtils::BinnedFn2D< double > | **[eff2DBJet_CSVv2_Loose](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-eff2dbjet-csvv2-loose)**({0., DBL_MAX} , {0., 25., 40., 60., 80., 100., 150., 200., 250., 300., 400., 500., DBL_MAX } , { 0.0, 0.78, 0.80, 0.82, 0.83, 0.84, 0.825, 0.82, 0.81, 0.8, 0.795, 0.79 } ) |
| const HEPUtils::BinnedFn2D< double > | **[eff2DBJet_DeepCSV_Loose](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-eff2dbjet-deepcsv-loose)**({0., DBL_MAX} , {0., 25., 40., 60., 80., 100., 150., 200., 250., 300., 400., 500., DBL_MAX } , { 0.0, 0.807, 0.830, 0.847, 0.854, 0.861, 0.866, 0.860, 0.857, 0.855, 0.849, 0.843 } ) |
| const HEPUtils::BinnedFn2D< double > | **[eff2DBJet_CSVv2_Medium](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-eff2dbjet-csvv2-medium)**({0., DBL_MAX} , {0., 25., 40., 60., 80., 100., 150., 200., 250., 300., 400., 500., DBL_MAX} , { 0.0, 0.58, 0.61, 0.63, 0.64, 0.65, 0.62, 0.6, 0.58, 0.56, 0.52, 0.48 } ) |
| const HEPUtils::BinnedFn2D< double > | **[eff2DBJet_DeepCSV_Medium](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-eff2dbjet-deepcsv-medium)**({0., DBL_MAX} , {0., 25., 40., 60., 80., 100., 150., 200., 250., 300., 400., 500., DBL_MAX} , { 0.0, 0.633, 0.667, 0.683, 0.688, 0.687, 0.678, 0.655, 0.635, 0.610, 0.585, 0.519 } ) |
| const HEPUtils::BinnedFn2D< double > | **[eff2DBJet_CSVv2_Tight](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-eff2dbjet-csvv2-tight)**({0., DBL_MAX} , {0., 25., 40., 60., 80., 100., 150., 200., 250., 300., 400., 500., DBL_MAX} , { 0.0, 0.4997, 0.5081, 0.5104, 0.5085, 0.4994, 0.4790, 0.4481, 0.4184, 0.3798, 0.3394, 0.3 } ) |
| const HEPUtils::BinnedFn2D< double > | **[eff2DBJet_DeepCSV_Tight](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-eff2dbjet-deepcsv-tight)**({0., DBL_MAX} , {0., 25., 40., 60., 80., 100., 150., 200., 250., 300., 400., 500., DBL_MAX} , { 0.0, 0.450, 0.492, 0.508, 0.513, 0.506, 0.485, 0.447, 0.411, 0.370, 0.330, 0.253 } ) |
| void | **[smearElectronEnergy](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-smearelectronenergy)**(std::vector< HEPUtils::Particle * > & electrons)<br>Randomly smear the supplied electrons' momenta by parameterised resolutions.  |
| void | **[smearMuonMomentum](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-smearmuonmomentum)**(std::vector< HEPUtils::Particle * > & muons)<br>Randomly smear the supplied muons' momenta by parameterised resolutions.  |
| void | **[smearJets](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-smearjets)**(std::vector< HEPUtils::Jet * > & jets)<br>Randomly smear the supplied jets' momenta by parameterised resolutions.  |
| void | **[smearTaus](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-smeartaus)**(std::vector< HEPUtils::Particle * > & taus)<br>Randomly smear the supplied hadronic taus' momenta by parameterised resolutions.  |
| const HEPUtils::BinnedFn2D< double > | **[eff2DEl_Tracking](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-eff2del-tracking)**({0, 1.5, 2.5, DBL_MAX} , {0, 0.1, 1.0, DBL_MAX} , { 0., 0.70, 0.95, 0., 0.60, 0.85, 0., 0., 0. } )<br>Representative Electron, Muon, Tau and B-tagging efficiencies for the WPs of the identification techniques used in SUSY analyses.  |
| const HEPUtils::BinnedFn2D< double > | **[eff2DEl_Generic](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-eff2del-generic)**({0, 1.5, 2.5, DBL_MAX} , {0, 10., DBL_MAX} , { 0., 0.95, 0., 0.85, 0., 0. } ) |
| const HEPUtils::BinnedFn2D< double > | **[eff2DEl_SUS_16_039](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-eff2del-sus-16-039)**({0., 0.8, 1.442, 1.556, 2., 2.5, DBL_MAX} , {0., 10., 15., 20., 25., 30., 40., 50., DBL_MAX} , { 0.0, 0.95, 0.507, 0.619, 0.682, 0.742, 0.798, 0.863, 0.0, 0.95, 0.429, 0.546, 0.619, 0.710, 0.734, 0.833, 0.0, 0.95, 0.256, 0.221, 0.315, 0.351, 0.373, 0.437, 0.0, 0.85, 0.249, 0.404, 0.423, 0.561, 0.642, 0.749, 0.0, 0.85, 0.195, 0.245, 0.380, 0.441, 0.533, 0.644, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 } ) |
| const HEPUtils::BinnedFn2D< double > | **[eff2DEl_SUS_19_008](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-eff2del-sus-19-008)**({0., 0.8, 1.442, 1.556, 2., 2.5, DBL_MAX} , {0., 10., 15., 20., 25., 30., 40., 50., DBL_MAX} , { 0.0, 0.95, 0.330, 0.412, 0.487, 0.561, 0.615, 0.701, 0.0, 0.95, 0.276, 0.367, 0.434, 0.520, 0.575, 0.660, 0.0, 0.95, 0.202, 0.170, 0.224, 0.261, 0.275, 0.341, 0.0, 0.85, 0.210, 0.288, 0.358, 0.434, 0.493, 0.586, 0.0, 0.85, 0.146, 0.200, 0.246, 0.314, 0.382, 0.456, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 } ) |
| const HEPUtils::BinnedFn2D< double > | **[eff2DEl_SUS_18_004](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-eff2del-sus-18-004)**({0., DBL_MAX} , {0., 4.25, 6.25, 8.75, 12.5, 17.5, 22.5, 27.5, DBL_MAX} , { 0.0, 0.30, 0.34, 0.38, 0.46, 0.54, 0.62, 0.7 } )<br>Efficiencies for the [CMS](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/) 2021 soft lepton analysis SUS-18-004.  |
| const HEPUtils::BinnedFn2D< double > | **[eff2DMu_Tracking](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-eff2dmu-tracking)**({0, 1.5, 2.5, DBL_MAX} , {0, 0.1, 1.0, DBL_MAX} , { 0, 0.75, 0.99, 0, 0.70, 0.98, 0, 0, 0 } ) |
| const HEPUtils::BinnedFn2D< double > | **[eff2DMu_Generic](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-eff2dmu-generic)**({0.0, 2.4, DBL_MAX} , {0.0, 10.0, 1000.0, DBL_MAX} , { 0.0, 0.95, 0.0, 0.0, 0.0, 0.0 } )<br>Randomly filter the supplied particle list by parameterised muon efficiency.  |
| const HEPUtils::BinnedFn2D< double > | **[eff2DMu_SUS_16_039](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-eff2dmu-sus-16-039)**({0., 0.9, 1.2, 2.1, 2.4, DBL_MAX} , {0., 10., 15., 20., 25., 30., 40., 50., DBL_MAX} , { 0.0, 0.704, 0.797, 0.855, 0.880, 0.906, 0.927, 0.931, 0.0, 0.639, 0.776, 0.836, 0.875, 0.898, 0.940, 0.930, 0.0, 0.596, 0.715, 0.840, 0.862, 0.891, 0.906, 0.925, 0.0, 0.522, 0.720, 0.764, 0.803, 0.807, 0.885, 0.877, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 } ) |
| const HEPUtils::BinnedFn2D< double > | **[eff2DMu_SUS_19_008](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-eff2dmu-sus-19-008)**({0., 0.9, 1.2, 2.1, 2.4, DBL_MAX} , {0., 10., 15., 20., 25., 30., 40., 50., DBL_MAX} , { 0.0, 0.527, 0.639, 0.723, 0.801, 0.858, 0.887, 0.926, 0.0, 0.482, 0.596, 0.695, 0.755, 0.831, 0.870, 0.917, 0.0, 0.498, 0.585, 0.683, 0.743, 0.807, 0.851, 0.896, 0.0, 0.441, 0.522, 0.604, 0.677, 0.744, 0.793, 0.834, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 } ) |
| const HEPUtils::BinnedFn2D< double > | **[eff2DMu_SUS_18_004](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-eff2dmu-sus-18-004)**({0., DBL_MAX} , {0., 1.75, 4.25, 6.25, 8.75, 12.5, 17.5, 22.5, 27.5, DBL_MAX} , { 0.0, 0.691, 0.70, 0.715, 0.73, 0.76, 0.79, 0.82, 0.85 } )<br>Efficiencies for the [CMS](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/) 2021 soft lepton analysis SUS-18-004.  |

## Attributes

|                | Name           |
| -------------- | -------------- |
| const double | **[effTau_Generic](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#variable-efftau-generic)** <br>Randomly filter the supplied particle list by parameterised tau efficiency.  |
| const double | **[misIDBJet_CSVv2_Loose](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#variable-misidbjet-csvv2-loose)**  |
| const double | **[misIDBJet_DeepCSV_Loose](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#variable-misidbjet-deepcsv-loose)**  |
| const double | **[misIDBJet_CSVv2_Medium](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#variable-misidbjet-csvv2-medium)**  |
| const double | **[misIDBJet_DeepCSV_Medium](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#variable-misidbjet-deepcsv-medium)**  |
| const double | **[misIDBJet_CSVv2_Tight](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#variable-misidbjet-csvv2-tight)**  |
| const double | **[misIDBJet_DeepCSV_Tight](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#variable-misidbjet-deepcsv-tight)**  |
| const std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), HEPUtils::BinnedFn2D< double > > | **[eff2DEl](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#variable-eff2del)** <br>{@  |
| const std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), HEPUtils::BinnedFn2D< double > > | **[eff2DMu](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#variable-eff2dmu)**  |
| const std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), double > | **[effTau](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#variable-efftau)**  |
| const std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), HEPUtils::BinnedFn2D< double > > | **[eff2DTau](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#variable-eff2dtau)**  |
| const std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), HEPUtils::BinnedFn2D< double > > | **[eff2DBJet](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#variable-eff2dbjet)**  |
| const std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), double > | **[misIDBJet](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#variable-misidbjet)**  |


## Functions Documentation

### function eff2DTau_SUS_16_039

```
static const HEPUtils::BinnedFn2D< double > eff2DTau_SUS_16_039(
    {0., 2.3} ,
    {0., 25., 30., 35., 40., 45., 50., 60., 70., 80., DBL_MAX} ,
    {0.38 *0.95, 0.48 *0.95, 0.5 *0.95, 0.49 *0.95, 0.51 *0.95, 0.49 *0.95, 0.47 *0.95, 0.45 *0.95, 0.48 *0.95, 0.5 *0.95} 
)
```


### function eff2DBJet_CSVv2_Loose

```
static const HEPUtils::BinnedFn2D< double > eff2DBJet_CSVv2_Loose(
    {0., DBL_MAX} ,
    {0., 25., 40., 60., 80., 100., 150., 200., 250., 300., 400., 500., DBL_MAX } ,
    { 0.0, 0.78, 0.80, 0.82, 0.83, 0.84, 0.825, 0.82, 0.81, 0.8, 0.795, 0.79 } 
)
```


### function eff2DBJet_DeepCSV_Loose

```
static const HEPUtils::BinnedFn2D< double > eff2DBJet_DeepCSV_Loose(
    {0., DBL_MAX} ,
    {0., 25., 40., 60., 80., 100., 150., 200., 250., 300., 400., 500., DBL_MAX } ,
    { 0.0, 0.807, 0.830, 0.847, 0.854, 0.861, 0.866, 0.860, 0.857, 0.855, 0.849, 0.843 } 
)
```


### function eff2DBJet_CSVv2_Medium

```
static const HEPUtils::BinnedFn2D< double > eff2DBJet_CSVv2_Medium(
    {0., DBL_MAX} ,
    {0., 25., 40., 60., 80., 100., 150., 200., 250., 300., 400., 500., DBL_MAX} ,
    { 0.0, 0.58, 0.61, 0.63, 0.64, 0.65, 0.62, 0.6, 0.58, 0.56, 0.52, 0.48 } 
)
```


### function eff2DBJet_DeepCSV_Medium

```
static const HEPUtils::BinnedFn2D< double > eff2DBJet_DeepCSV_Medium(
    {0., DBL_MAX} ,
    {0., 25., 40., 60., 80., 100., 150., 200., 250., 300., 400., 500., DBL_MAX} ,
    { 0.0, 0.633, 0.667, 0.683, 0.688, 0.687, 0.678, 0.655, 0.635, 0.610, 0.585, 0.519 } 
)
```


### function eff2DBJet_CSVv2_Tight

```
static const HEPUtils::BinnedFn2D< double > eff2DBJet_CSVv2_Tight(
    {0., DBL_MAX} ,
    {0., 25., 40., 60., 80., 100., 150., 200., 250., 300., 400., 500., DBL_MAX} ,
    { 0.0, 0.4997, 0.5081, 0.5104, 0.5085, 0.4994, 0.4790, 0.4481, 0.4184, 0.3798, 0.3394, 0.3 } 
)
```


### function eff2DBJet_DeepCSV_Tight

```
static const HEPUtils::BinnedFn2D< double > eff2DBJet_DeepCSV_Tight(
    {0., DBL_MAX} ,
    {0., 25., 40., 60., 80., 100., 150., 200., 250., 300., 400., 500., DBL_MAX} ,
    { 0.0, 0.450, 0.492, 0.508, 0.513, 0.506, 0.485, 0.447, 0.411, 0.370, 0.330, 0.253 } 
)
```


### function smearElectronEnergy

```
inline void smearElectronEnergy(
    std::vector< HEPUtils::Particle * > & electrons
)
```

Randomly smear the supplied electrons' momenta by parameterised resolutions. 

Function that mimics the DELPHES electron energy resolution. We need to smear E, then recalculate pT, then reset the 4-vector. 


### function smearMuonMomentum

```
inline void smearMuonMomentum(
    std::vector< HEPUtils::Particle * > & muons
)
```

Randomly smear the supplied muons' momenta by parameterised resolutions. 

Function that mimics the DELPHES muon momentum resolution. We need to smear pT, then recalculate E, then reset the 4-vector. 


### function smearJets

```
inline void smearJets(
    std::vector< HEPUtils::Jet * > & jets
)
```

Randomly smear the supplied jets' momenta by parameterised resolutions. 

**Todo**: Update cf. Matthias study for [ATLAS](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1atlas/)

Function that mimics the DELPHES jet momentum resolution. We need to smear pT, then recalculate E, then reset the 4-vector


TodoThis is the [ATLAS](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1atlas/) number... I can't find values for the [CMS](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/) parameterisation, cf. [https://cds.cern.ch/record/1339945/files/JME-10-014-pas.pdf](https://cds.cern.ch/record/1339945/files/JME-10-014-pas.pdf)[https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideJetResolution](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideJetResolution)[https://github.com/adrager/cmssw/blob/CMSSW_7_2_X/CondFormats/JetMETObjects/test/TestCorrections.C](https://github.com/adrager/cmssw/blob/CMSSW_7_2_X/CondFormats/JetMETObjects/test/TestCorrections.C)


### function smearTaus

```
inline void smearTaus(
    std::vector< HEPUtils::Particle * > & taus
)
```

Randomly smear the supplied hadronic taus' momenta by parameterised resolutions. 

**Todo**: Update cf. Matthias study for [ATLAS](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1atlas/)

We need to smear pT, then recalculate E, then reset the 4-vector. Same as for jets, but on a vector of particles. (?)


TodoIs this the best way to smear? Should we preserve the mean jet energy, or pT, or direction? 


### function eff2DEl_Tracking

```
static const HEPUtils::BinnedFn2D< double > eff2DEl_Tracking(
    {0, 1.5, 2.5, DBL_MAX} ,
    {0, 0.1, 1.0, DBL_MAX} ,
    { 0., 0.70, 0.95, 0., 0.60, 0.85, 0., 0., 0. } 
)
```

Representative Electron, Muon, Tau and B-tagging efficiencies for the WPs of the identification techniques used in SUSY analyses. 

Electron efficiencies Randomly filter the supplied particle list by parameterised electron tracking efficiency 


### function eff2DEl_Generic

```
static const HEPUtils::BinnedFn2D< double > eff2DEl_Generic(
    {0, 1.5, 2.5, DBL_MAX} ,
    {0, 10., DBL_MAX} ,
    { 0., 0.95, 0., 0.85, 0., 0. } 
)
```


**Note**: 

  * Should be applied after the electron energy smearing 
  * Eff values currently identical to those in [ATLAS](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1atlas/) (AB, 2016-01-24) 


Randomly filter the supplied particle list by parameterised electron efficiency 


### function eff2DEl_SUS_16_039

```
static const HEPUtils::BinnedFn2D< double > eff2DEl_SUS_16_039(
    {0., 0.8, 1.442, 1.556, 2., 2.5, DBL_MAX} ,
    {0., 10., 15., 20., 25., 30., 40., 50., DBL_MAX} ,
    { 0.0, 0.95, 0.507, 0.619, 0.682, 0.742, 0.798, 0.863, 0.0, 0.95, 0.429, 0.546, 0.619, 0.710, 0.734, 0.833, 0.0, 0.95, 0.256, 0.221, 0.315, 0.351, 0.373, 0.437, 0.0, 0.85, 0.249, 0.404, 0.423, 0.561, 0.642, 0.749, 0.0, 0.85, 0.195, 0.245, 0.380, 0.441, 0.533, 0.644, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 } 
)
```


### function eff2DEl_SUS_19_008

```
static const HEPUtils::BinnedFn2D< double > eff2DEl_SUS_19_008(
    {0., 0.8, 1.442, 1.556, 2., 2.5, DBL_MAX} ,
    {0., 10., 15., 20., 25., 30., 40., 50., DBL_MAX} ,
    { 0.0, 0.95, 0.330, 0.412, 0.487, 0.561, 0.615, 0.701, 0.0, 0.95, 0.276, 0.367, 0.434, 0.520, 0.575, 0.660, 0.0, 0.95, 0.202, 0.170, 0.224, 0.261, 0.275, 0.341, 0.0, 0.85, 0.210, 0.288, 0.358, 0.434, 0.493, 0.586, 0.0, 0.85, 0.146, 0.200, 0.246, 0.314, 0.382, 0.456, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 } 
)
```


### function eff2DEl_SUS_18_004

```
static const HEPUtils::BinnedFn2D< double > eff2DEl_SUS_18_004(
    {0., DBL_MAX} ,
    {0., 4.25, 6.25, 8.75, 12.5, 17.5, 22.5, 27.5, DBL_MAX} ,
    { 0.0, 0.30, 0.34, 0.38, 0.46, 0.54, 0.62, 0.7 } 
)
```

Efficiencies for the [CMS](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/) 2021 soft lepton analysis SUS-18-004. 

### function eff2DMu_Tracking

```
static const HEPUtils::BinnedFn2D< double > eff2DMu_Tracking(
    {0, 1.5, 2.5, DBL_MAX} ,
    {0, 0.1, 1.0, DBL_MAX} ,
    { 0, 0.75, 0.99, 0, 0.70, 0.98, 0, 0, 0 } 
)
```


**Note**: Eff values currently identical to those in [ATLAS](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1atlas/) (AB, 2016-01-24) 

Muon efficiencies Randomly filter the supplied particle list by parameterised muon tracking efficiency 


### function eff2DMu_Generic

```
static const HEPUtils::BinnedFn2D< double > eff2DMu_Generic(
    {0.0, 2.4, DBL_MAX} ,
    {0.0, 10.0, 1000.0, DBL_MAX} ,
    { 0.0, 0.95, 0.0, 0.0, 0.0, 0.0 } 
)
```

Randomly filter the supplied particle list by parameterised muon efficiency. 

### function eff2DMu_SUS_16_039

```
static const HEPUtils::BinnedFn2D< double > eff2DMu_SUS_16_039(
    {0., 0.9, 1.2, 2.1, 2.4, DBL_MAX} ,
    {0., 10., 15., 20., 25., 30., 40., 50., DBL_MAX} ,
    { 0.0, 0.704, 0.797, 0.855, 0.880, 0.906, 0.927, 0.931, 0.0, 0.639, 0.776, 0.836, 0.875, 0.898, 0.940, 0.930, 0.0, 0.596, 0.715, 0.840, 0.862, 0.891, 0.906, 0.925, 0.0, 0.522, 0.720, 0.764, 0.803, 0.807, 0.885, 0.877, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 } 
)
```


### function eff2DMu_SUS_19_008

```
static const HEPUtils::BinnedFn2D< double > eff2DMu_SUS_19_008(
    {0., 0.9, 1.2, 2.1, 2.4, DBL_MAX} ,
    {0., 10., 15., 20., 25., 30., 40., 50., DBL_MAX} ,
    { 0.0, 0.527, 0.639, 0.723, 0.801, 0.858, 0.887, 0.926, 0.0, 0.482, 0.596, 0.695, 0.755, 0.831, 0.870, 0.917, 0.0, 0.498, 0.585, 0.683, 0.743, 0.807, 0.851, 0.896, 0.0, 0.441, 0.522, 0.604, 0.677, 0.744, 0.793, 0.834, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 } 
)
```


### function eff2DMu_SUS_18_004

```
static const HEPUtils::BinnedFn2D< double > eff2DMu_SUS_18_004(
    {0., DBL_MAX} ,
    {0., 1.75, 4.25, 6.25, 8.75, 12.5, 17.5, 22.5, 27.5, DBL_MAX} ,
    { 0.0, 0.691, 0.70, 0.715, 0.73, 0.76, 0.79, 0.82, 0.85 } 
)
```

Efficiencies for the [CMS](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/) 2021 soft lepton analysis SUS-18-004. 


## Attributes Documentation

### variable effTau_Generic

```
static const double effTau_Generic = 0.6;
```

Randomly filter the supplied particle list by parameterised tau efficiency. 

**Note**: No delete, because this should only ever be applied to copies of the Event Particle* vectors in [Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/) routines 

Tau efficiencies 


### variable misIDBJet_CSVv2_Loose

```
static const double misIDBJet_CSVv2_Loose = 0.089;
```


**Note**: All digitized from [https://twiki.cern.ch/twiki/pub/CMSPublic/SUSMoriond2017ObjectsEfficiency/btag_eff_CSVv2_DeepCSV.pdf](https://twiki.cern.ch/twiki/pub/CMSPublic/SUSMoriond2017ObjectsEfficiency/btag_eff_CSVv2_DeepCSV.pdf) From [https://twiki.cern.ch/twiki/bin/view/CMSPublic/SUSMoriond2017ObjectsEfficiency](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SUSMoriond2017ObjectsEfficiency) Missing identification efficiencies are taken from Table 2 of 1712.07158 

B-tagging efficiencies 


### variable misIDBJet_DeepCSV_Loose

```
static const double misIDBJet_DeepCSV_Loose = 0.11;
```


### variable misIDBJet_CSVv2_Medium

```
static const double misIDBJet_CSVv2_Medium = 0.009;
```


### variable misIDBJet_DeepCSV_Medium

```
static const double misIDBJet_DeepCSV_Medium = 0.011;
```


### variable misIDBJet_CSVv2_Tight

```
static const double misIDBJet_CSVv2_Tight = 0.001;
```


### variable misIDBJet_DeepCSV_Tight

```
static const double misIDBJet_DeepCSV_Tight = 0.001;
```


### variable eff2DEl

```
static const std::map< str, HEPUtils::BinnedFn2D< double > > eff2DEl =
        {
          {"Tracking",   eff2DEl_Tracking},
          {"Generic",    eff2DEl_Generic},
          {"SUS_16_039", eff2DEl_SUS_16_039},
          {"SUS_19_008", eff2DEl_SUS_19_008},
          {"SUS-18-004", eff2DEl_SUS_18_004}
        };
```

{@ 

### variable eff2DMu

```
static const std::map< str, HEPUtils::BinnedFn2D< double > > eff2DMu =
        {
          {"Tracking",   eff2DMu_Tracking},
          {"Generic",    eff2DMu_Generic},
          {"SUS_16_039", eff2DMu_SUS_16_039},
          {"SUS_19_008", eff2DMu_SUS_19_008},
          {"SUS-18-004", eff2DMu_SUS_18_004}

        };
```


### variable effTau

```
static const std::map< str, double > effTau =
        {
          {"Generic", effTau_Generic}
        };
```


### variable eff2DTau

```
static const std::map< str, HEPUtils::BinnedFn2D< double > > eff2DTau =
        {
          {"SUS_16_039", eff2DTau_SUS_16_039}
        };
```


### variable eff2DBJet

```
static const std::map< str, HEPUtils::BinnedFn2D< double > > eff2DBJet =
        {
          {"CSVv2Loose", eff2DBJet_CSVv2_Loose},
          {"DeepCSVLoose", eff2DBJet_DeepCSV_Loose},
          {"CSVv2Medium", eff2DBJet_CSVv2_Medium},
          {"DeepCSVMedium", eff2DBJet_DeepCSV_Medium},
          {"CSVv2Tight", eff2DBJet_CSVv2_Tight},
          {"DeepCSVTight", eff2DBJet_DeepCSV_Tight},
        };
```


### variable misIDBJet

```
static const std::map< str, double > misIDBJet =
        {
          {"CSVv2Loose", misIDBJet_CSVv2_Loose},
          {"DeepCSVLoose", misIDBJet_DeepCSV_Loose},
          {"CSVv2Medium", misIDBJet_CSVv2_Medium},
          {"DeepCSVMedium", misIDBJet_DeepCSV_Medium},
          {"CSVv2Tight", misIDBJet_CSVv2_Tight},
          {"DeepCSVTight", misIDBJet_DeepCSV_Tight},
        };
```





-------------------------------

Updated on 2026-11-03 at 14:50:43 +0000