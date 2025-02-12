---
title: "namespace Gambit::ColliderBit::CMS"
description: "CMS-specific efficiency and smearing functions for super fast detector simulation. "

---

# namespace Gambit::ColliderBit::CMS

CMS-specific efficiency and smearing functions for super fast detector simulation. 

## Functions

|                | Name           |
| -------------- | -------------- |
| void | **[applyElectronTrackingEff](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-applyelectrontrackingeff)**(std::vector< const HEPUtils::Particle * > & electrons)<br>Randomly filter the supplied particle list by parameterised electron tracking efficiency.  |
| void | **[applyElectronEff](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-applyelectroneff)**(std::vector< const HEPUtils::Particle * > & electrons) |
| void | **[applyMuonTrackEff](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-applymuontrackeff)**(std::vector< const HEPUtils::Particle * > & muons) |
| void | **[applyMuonEff](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-applymuoneff)**(std::vector< const HEPUtils::Particle * > & muons)<br>Randomly filter the supplied particle list by parameterised muon efficiency.  |
| void | **[applyTauEfficiency](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-applytauefficiency)**(std::vector< const HEPUtils::Particle * > & taus)<br>Randomly filter the supplied particle list by parameterised tau efficiency.  |
| void | **[smearElectronEnergy](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-smearelectronenergy)**(std::vector< HEPUtils::Particle * > & electrons)<br>Randomly smear the supplied electrons' momenta by parameterised resolutions.  |
| void | **[smearMuonMomentum](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-smearmuonmomentum)**(std::vector< HEPUtils::Particle * > & muons)<br>Randomly smear the supplied muons' momenta by parameterised resolutions.  |
| void | **[smearJets](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-smearjets)**(std::vector< HEPUtils::Jet * > & jets)<br>Randomly smear the supplied jets' momenta by parameterised resolutions.  |
| void | **[smearTaus](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-smeartaus)**(std::vector< HEPUtils::Particle * > & taus)<br>Randomly smear the supplied hadronic taus' momenta by parameterised resolutions.  |
| void | **[applyCSVv2MediumBtagEff](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-applycsvv2mediumbtageff)**(std::vector< const HEPUtils::Jet * > & bjets) |
| void | **[applyCSVv2MediumBtagEff](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-applycsvv2mediumbtageff)**(std::vector< HEPUtils::Jet * > & bjets) |
| void | **[applyCSVv2LooseBtagEff](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-applycsvv2loosebtageff)**(std::vector< const HEPUtils::Jet * > & bjets) |
| void | **[applyCSVv2LooseBtagEff](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-applycsvv2loosebtageff)**(std::vector< HEPUtils::Jet * > & bjets) |
| void | **[applyCSVv2TightBtagEff](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-applycsvv2tightbtageff)**(std::vector< const HEPUtils::Jet * > & bjets) |
| void | **[applyCSVv2TightBtagEff](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-applycsvv2tightbtageff)**(std::vector< HEPUtils::Jet * > & bjets) |
| void | **[applyBtagMisId](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-applybtagmisid)**(double mis_id_prob, std::vector< const HEPUtils::Jet * > & jets, std::vector< const HEPUtils::Jet * > & bjets)<br>Apply user-specified b-tag misidentification rate (flat)  |
| void | **[applyBtagMisId](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-applybtagmisid)**(double mis_id_prob, std::vector< HEPUtils::Jet * > & jets, std::vector< HEPUtils::Jet * > & bjets) |
| void | **[applyCSVv2LooseBtagMisId](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-applycsvv2loosebtagmisid)**(std::vector< const HEPUtils::Jet * > & jets, std::vector< const HEPUtils::Jet * > & bjets) |
| void | **[applyCSVv2LooseBtagMisId](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-applycsvv2loosebtagmisid)**(std::vector< HEPUtils::Jet * > & jets, std::vector< HEPUtils::Jet * > & bjets) |
| void | **[applyCSVv2LooseBtagEffAndMisId](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-applycsvv2loosebtageffandmisid)**(std::vector< const HEPUtils::Jet * > & jets, std::vector< const HEPUtils::Jet * > & bjets)<br>Apply both b-tag efficiency and misidentification rate for CSVv2 loose WP.  |
| void | **[applyCSVv2LooseBtagEffAndMisId](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-applycsvv2loosebtageffandmisid)**(std::vector< HEPUtils::Jet * > & jets, std::vector< HEPUtils::Jet * > & bjets) |
| void | **[applyCSVv2MediumBtagMisId](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-applycsvv2mediumbtagmisid)**(std::vector< const HEPUtils::Jet * > & jets, std::vector< const HEPUtils::Jet * > & bjets) |
| void | **[applyCSVv2MediumBtagMisId](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-applycsvv2mediumbtagmisid)**(std::vector< HEPUtils::Jet * > & jets, std::vector< HEPUtils::Jet * > & bjets) |
| void | **[applyCSVv2MediumBtagEffAndMisId](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-applycsvv2mediumbtageffandmisid)**(std::vector< const HEPUtils::Jet * > & jets, std::vector< const HEPUtils::Jet * > & bjets)<br>Apply both b-tag efficiency and misidentification rate for CSVv2 medium WP.  |
| void | **[applyCSVv2MediumBtagEffAndMisId](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-applycsvv2mediumbtageffandmisid)**(std::vector< HEPUtils::Jet * > & jets, std::vector< HEPUtils::Jet * > & bjets) |
| const HEPUtils::BinnedFn2D< double > | **[eff2DEl_SUS_16_039](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-eff2del-sus-16-039)**({0., 0.8, 1.442, 1.556, 2., 2.5, DBL_MAX} , {0., 10., 15., 20., 25., 30., 40., 50., DBL_MAX} , { 0.0, 0.95, 0.507, 0.619, 0.682, 0.742, 0.798, 0.863, 0.0, 0.95, 0.429, 0.546, 0.619, 0.710, 0.734, 0.833, 0.0, 0.95, 0.256, 0.221, 0.315, 0.351, 0.373, 0.437, 0.0, 0.85, 0.249, 0.404, 0.423, 0.561, 0.642, 0.749, 0.0, 0.85, 0.195, 0.245, 0.380, 0.441, 0.533, 0.644, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 } ) |
| const HEPUtils::BinnedFn2D< double > | **[eff2DMu_SUS_16_039](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-eff2dmu-sus-16-039)**({0., 0.9, 1.2, 2.1, 2.4, DBL_MAX} , {0., 10., 15., 20., 25., 30., 40., 50., DBL_MAX} , { 0.0, 0.704, 0.797, 0.855, 0.880, 0.906, 0.927, 0.931, 0.0, 0.639, 0.776, 0.836, 0.875, 0.898, 0.940, 0.930, 0.0, 0.596, 0.715, 0.840, 0.862, 0.891, 0.906, 0.925, 0.0, 0.522, 0.720, 0.764, 0.803, 0.807, 0.885, 0.877, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 } ) |
| const HEPUtils::BinnedFn2D< double > | **[eff2DTau_SUS_16_039](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-eff2dtau-sus-16-039)**({0., 2.3} , {0., 25., 30., 35., 40., 45., 50., 60., 70., 80., DBL_MAX} , {0.38 *0.95, 0.48 *0.95, 0.5 *0.95, 0.49 *0.95, 0.51 *0.95, 0.49 *0.95, 0.47 *0.95, 0.45 *0.95, 0.48 *0.95, 0.5 *0.95} ) |
| const HEPUtils::BinnedFn2D< double > | **[eff2DEl_SUS_19_008](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-eff2del-sus-19-008)**({0., 0.8, 1.442, 1.556, 2., 2.5, DBL_MAX} , {0., 10., 15., 20., 25., 30., 40., 50., DBL_MAX} , { 0.0, 0.95, 0.330, 0.412, 0.487, 0.561, 0.615, 0.701, 0.0, 0.95, 0.276, 0.367, 0.434, 0.520, 0.575, 0.660, 0.0, 0.95, 0.202, 0.170, 0.224, 0.261, 0.275, 0.341, 0.0, 0.85, 0.210, 0.288, 0.358, 0.434, 0.493, 0.586, 0.0, 0.85, 0.146, 0.200, 0.246, 0.314, 0.382, 0.456, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 } ) |
| const HEPUtils::BinnedFn2D< double > | **[eff2DMu_SUS_19_008](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#function-eff2dmu-sus-19-008)**({0., 0.9, 1.2, 2.1, 2.4, DBL_MAX} , {0., 10., 15., 20., 25., 30., 40., 50., DBL_MAX} , { 0.0, 0.527, 0.639, 0.723, 0.801, 0.858, 0.887, 0.926, 0.0, 0.482, 0.596, 0.695, 0.755, 0.831, 0.870, 0.917, 0.0, 0.498, 0.585, 0.683, 0.743, 0.807, 0.851, 0.896, 0.0, 0.441, 0.522, 0.604, 0.677, 0.744, 0.793, 0.834, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 } ) |

## Attributes

|                | Name           |
| -------------- | -------------- |
| const std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), HEPUtils::BinnedFn2D< double > > | **[eff2DEl](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#variable-eff2del)**  |
| const std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), HEPUtils::BinnedFn2D< double > > | **[eff2DMu](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#variable-eff2dmu)**  |
| const std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), HEPUtils::BinnedFn2D< double > > | **[eff2DTau](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1cms/#variable-eff2dtau)**  |


## Functions Documentation

### function applyElectronTrackingEff

```
inline void applyElectronTrackingEff(
    std::vector< const HEPUtils::Particle * > & electrons
)
```

Randomly filter the supplied particle list by parameterised electron tracking efficiency. 

### function applyElectronEff

```
inline void applyElectronEff(
    std::vector< const HEPUtils::Particle * > & electrons
)
```


**Note**: 

  * Should be applied after the electron energy smearing 
  * Eff values currently identical to those in [ATLAS](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1atlas/) (AB, 2016-01-24) 


Randomly filter the supplied particle list by parameterised electron efficiency 


### function applyMuonTrackEff

```
inline void applyMuonTrackEff(
    std::vector< const HEPUtils::Particle * > & muons
)
```


**Note**: Eff values currently identical to those in [ATLAS](/documentation/code/namespaces/namespacegambit_1_1colliderbit_1_1atlas/) (AB, 2016-01-24) 

Randomly filter the supplied particle list by parameterised muon tracking efficiency 


### function applyMuonEff

```
inline void applyMuonEff(
    std::vector< const HEPUtils::Particle * > & muons
)
```

Randomly filter the supplied particle list by parameterised muon efficiency. 

### function applyTauEfficiency

```
inline void applyTauEfficiency(
    std::vector< const HEPUtils::Particle * > & taus
)
```

Randomly filter the supplied particle list by parameterised tau efficiency. 

**Note**: No delete, because this should only ever be applied to copies of the Event Particle* vectors in [Analysis](/documentation/code/classes/classgambit_1_1colliderbit_1_1analysis/) routines 

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


### function applyCSVv2MediumBtagEff

```
inline void applyCSVv2MediumBtagEff(
    std::vector< const HEPUtils::Jet * > & bjets
)
```


**Note**: Numbers digitized from [https://twiki.cern.ch/twiki/pub/CMSPublic/SUSMoriond2017ObjectsEfficiency/btag_eff_CSVv2_DeepCSV.pdf](https://twiki.cern.ch/twiki/pub/CMSPublic/SUSMoriond2017ObjectsEfficiency/btag_eff_CSVv2_DeepCSV.pdf)

Apply efficiency function to CSVv2 medium WP b-tagged jets 


### function applyCSVv2MediumBtagEff

```
inline void applyCSVv2MediumBtagEff(
    std::vector< HEPUtils::Jet * > & bjets
)
```


### function applyCSVv2LooseBtagEff

```
inline void applyCSVv2LooseBtagEff(
    std::vector< const HEPUtils::Jet * > & bjets
)
```


**Note**: Numbers digitized from [https://twiki.cern.ch/twiki/pub/CMSPublic/SUSMoriond2017ObjectsEfficiency/btag_eff_CSVv2_DeepCSV.pdf](https://twiki.cern.ch/twiki/pub/CMSPublic/SUSMoriond2017ObjectsEfficiency/btag_eff_CSVv2_DeepCSV.pdf)

Apply efficiency function to CSVv2 loose WP b-tagged jets 


### function applyCSVv2LooseBtagEff

```
inline void applyCSVv2LooseBtagEff(
    std::vector< HEPUtils::Jet * > & bjets
)
```


### function applyCSVv2TightBtagEff

```
inline void applyCSVv2TightBtagEff(
    std::vector< const HEPUtils::Jet * > & bjets
)
```


**Note**: Numbers digitized from [https://twiki.cern.ch/twiki/pub/CMSPublic/SUSMoriond2017ObjectsEfficiency/btag_eff_CSVv2_DeepCSV.pdf](https://twiki.cern.ch/twiki/pub/CMSPublic/SUSMoriond2017ObjectsEfficiency/btag_eff_CSVv2_DeepCSV.pdf)

Apply efficiency function to CSVv2 tight WP b-tagged jets 


### function applyCSVv2TightBtagEff

```
inline void applyCSVv2TightBtagEff(
    std::vector< HEPUtils::Jet * > & bjets
)
```


### function applyBtagMisId

```
inline void applyBtagMisId(
    double mis_id_prob,
    std::vector< const HEPUtils::Jet * > & jets,
    std::vector< const HEPUtils::Jet * > & bjets
)
```

Apply user-specified b-tag misidentification rate (flat) 

### function applyBtagMisId

```
inline void applyBtagMisId(
    double mis_id_prob,
    std::vector< HEPUtils::Jet * > & jets,
    std::vector< HEPUtils::Jet * > & bjets
)
```


### function applyCSVv2LooseBtagMisId

```
inline void applyCSVv2LooseBtagMisId(
    std::vector< const HEPUtils::Jet * > & jets,
    std::vector< const HEPUtils::Jet * > & bjets
)
```


**Note**: Numbers from Table 2 in [https://arxiv.org/pdf/1712.07158.pdf](https://arxiv.org/pdf/1712.07158.pdf)

Apply b-tag misidentification rate for CSVv2 loose WP 


### function applyCSVv2LooseBtagMisId

```
inline void applyCSVv2LooseBtagMisId(
    std::vector< HEPUtils::Jet * > & jets,
    std::vector< HEPUtils::Jet * > & bjets
)
```


### function applyCSVv2LooseBtagEffAndMisId

```
inline void applyCSVv2LooseBtagEffAndMisId(
    std::vector< const HEPUtils::Jet * > & jets,
    std::vector< const HEPUtils::Jet * > & bjets
)
```

Apply both b-tag efficiency and misidentification rate for CSVv2 loose WP. 

### function applyCSVv2LooseBtagEffAndMisId

```
inline void applyCSVv2LooseBtagEffAndMisId(
    std::vector< HEPUtils::Jet * > & jets,
    std::vector< HEPUtils::Jet * > & bjets
)
```


### function applyCSVv2MediumBtagMisId

```
inline void applyCSVv2MediumBtagMisId(
    std::vector< const HEPUtils::Jet * > & jets,
    std::vector< const HEPUtils::Jet * > & bjets
)
```


**Note**: Numbers from Table 2 in [https://arxiv.org/pdf/1712.07158.pdf](https://arxiv.org/pdf/1712.07158.pdf)

Apply b-tag misidentification rate for CSVv2 medium WP 


### function applyCSVv2MediumBtagMisId

```
inline void applyCSVv2MediumBtagMisId(
    std::vector< HEPUtils::Jet * > & jets,
    std::vector< HEPUtils::Jet * > & bjets
)
```


### function applyCSVv2MediumBtagEffAndMisId

```
inline void applyCSVv2MediumBtagEffAndMisId(
    std::vector< const HEPUtils::Jet * > & jets,
    std::vector< const HEPUtils::Jet * > & bjets
)
```

Apply both b-tag efficiency and misidentification rate for CSVv2 medium WP. 

### function applyCSVv2MediumBtagEffAndMisId

```
inline void applyCSVv2MediumBtagEffAndMisId(
    std::vector< HEPUtils::Jet * > & jets,
    std::vector< HEPUtils::Jet * > & bjets
)
```


### function eff2DEl_SUS_16_039

```
static const HEPUtils::BinnedFn2D< double > eff2DEl_SUS_16_039(
    {0., 0.8, 1.442, 1.556, 2., 2.5, DBL_MAX} ,
    {0., 10., 15., 20., 25., 30., 40., 50., DBL_MAX} ,
    { 0.0, 0.95, 0.507, 0.619, 0.682, 0.742, 0.798, 0.863, 0.0, 0.95, 0.429, 0.546, 0.619, 0.710, 0.734, 0.833, 0.0, 0.95, 0.256, 0.221, 0.315, 0.351, 0.373, 0.437, 0.0, 0.85, 0.249, 0.404, 0.423, 0.561, 0.642, 0.749, 0.0, 0.85, 0.195, 0.245, 0.380, 0.441, 0.533, 0.644, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 } 
)
```


Representative Muon and Electron efficiencies for the WPs of the identification techniques used in SUSY analyses From [https://twiki.cern.ch/twiki/bin/view/CMSPublic/SUSMoriond2017ObjectsEfficiency](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SUSMoriond2017ObjectsEfficiency) {@ 


### function eff2DMu_SUS_16_039

```
static const HEPUtils::BinnedFn2D< double > eff2DMu_SUS_16_039(
    {0., 0.9, 1.2, 2.1, 2.4, DBL_MAX} ,
    {0., 10., 15., 20., 25., 30., 40., 50., DBL_MAX} ,
    { 0.0, 0.704, 0.797, 0.855, 0.880, 0.906, 0.927, 0.931, 0.0, 0.639, 0.776, 0.836, 0.875, 0.898, 0.940, 0.930, 0.0, 0.596, 0.715, 0.840, 0.862, 0.891, 0.906, 0.925, 0.0, 0.522, 0.720, 0.764, 0.803, 0.807, 0.885, 0.877, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 } 
)
```


### function eff2DTau_SUS_16_039

```
static const HEPUtils::BinnedFn2D< double > eff2DTau_SUS_16_039(
    {0., 2.3} ,
    {0., 25., 30., 35., 40., 45., 50., 60., 70., 80., DBL_MAX} ,
    {0.38 *0.95, 0.48 *0.95, 0.5 *0.95, 0.49 *0.95, 0.51 *0.95, 0.49 *0.95, 0.47 *0.95, 0.45 *0.95, 0.48 *0.95, 0.5 *0.95} 
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


### function eff2DMu_SUS_19_008

```
static const HEPUtils::BinnedFn2D< double > eff2DMu_SUS_19_008(
    {0., 0.9, 1.2, 2.1, 2.4, DBL_MAX} ,
    {0., 10., 15., 20., 25., 30., 40., 50., DBL_MAX} ,
    { 0.0, 0.527, 0.639, 0.723, 0.801, 0.858, 0.887, 0.926, 0.0, 0.482, 0.596, 0.695, 0.755, 0.831, 0.870, 0.917, 0.0, 0.498, 0.585, 0.683, 0.743, 0.807, 0.851, 0.896, 0.0, 0.441, 0.522, 0.604, 0.677, 0.744, 0.793, 0.834, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 } 
)
```



## Attributes Documentation

### variable eff2DEl

```
static const std::map< str, HEPUtils::BinnedFn2D< double > > eff2DEl =
      {
        {"SUS_16_039", eff2DEl_SUS_16_039},
        {"SUS_19_008", eff2DEl_SUS_19_008}
      };
```


### variable eff2DMu

```
static const std::map< str, HEPUtils::BinnedFn2D< double > > eff2DMu =
      {
        {"SUS_16_039", eff2DMu_SUS_16_039},
        {"SUS_19_008", eff2DMu_SUS_19_008}

      };
```


### variable eff2DTau

```
static const std::map< str, HEPUtils::BinnedFn2D< double > > eff2DTau =
      {
        {"SUS_16_039", eff2DTau_SUS_16_039}
      };
```





-------------------------------

Updated on 2025-02-12 at 16:10:32 +0000