---
title: "class Gambit::ColliderBit::BaseLimitContainer"
description: "Base class for experimental limit curve interpolation. "

---

# class Gambit::ColliderBit::BaseLimitContainer



Base class for experimental limit curve interpolation. 


`#include <BaseLimitContainer.hpp>`

Inherited by [Gambit::ColliderBit::ALEPHSelectronLimitAt208GeV](/documentation/code/classes/classgambit_1_1colliderbit_1_1alephselectronlimitat208gev/), [Gambit::ColliderBit::ALEPHSmuonLimitAt208GeV](/documentation/code/classes/classgambit_1_1colliderbit_1_1alephsmuonlimitat208gev/), [Gambit::ColliderBit::ALEPHStauLimitAt208GeV](/documentation/code/classes/classgambit_1_1colliderbit_1_1alephstaulimitat208gev/), [Gambit::ColliderBit::L3ChargedGauginoSmallDeltaMAnySneutrinoLimitAt188pt6GeV](/documentation/code/classes/classgambit_1_1colliderbit_1_1l3chargedgauginosmalldeltamanysneutrinolimitat188pt6gev/), [Gambit::ColliderBit::L3ChargedGauginoSmallDeltaMWithHeavySneutrinoLimitAt188pt6GeV](/documentation/code/classes/classgambit_1_1colliderbit_1_1l3chargedgauginosmalldeltamwithheavysneutrinolimitat188pt6gev/), [Gambit::ColliderBit::L3ChargedHiggsinoSmallDeltaMLimitAt188pt6GeV](/documentation/code/classes/classgambit_1_1colliderbit_1_1l3chargedhiggsinosmalldeltamlimitat188pt6gev/), [Gambit::ColliderBit::L3CharginoAllChannelsLimitAt188pt6GeV](/documentation/code/classes/classgambit_1_1colliderbit_1_1l3charginoallchannelslimitat188pt6gev/), [Gambit::ColliderBit::L3CharginoLeptonicLimitAt188pt6GeV](/documentation/code/classes/classgambit_1_1colliderbit_1_1l3charginoleptoniclimitat188pt6gev/), [Gambit::ColliderBit::L3NeutralinoAllChannelsLimitAt188pt6GeV](/documentation/code/classes/classgambit_1_1colliderbit_1_1l3neutralinoallchannelslimitat188pt6gev/), [Gambit::ColliderBit::L3NeutralinoLeptonicLimitAt188pt6GeV](/documentation/code/classes/classgambit_1_1colliderbit_1_1l3neutralinoleptoniclimitat188pt6gev/), [Gambit::ColliderBit::L3SelectronLimitAt205GeV](/documentation/code/classes/classgambit_1_1colliderbit_1_1l3selectronlimitat205gev/), [Gambit::ColliderBit::L3SmuonLimitAt205GeV](/documentation/code/classes/classgambit_1_1colliderbit_1_1l3smuonlimitat205gev/), [Gambit::ColliderBit::L3StauLimitAt205GeV](/documentation/code/classes/classgambit_1_1colliderbit_1_1l3staulimitat205gev/), [Gambit::ColliderBit::OPALCharginoAllChannelsLimitAt208GeV](/documentation/code/classes/classgambit_1_1colliderbit_1_1opalcharginoallchannelslimitat208gev/), [Gambit::ColliderBit::OPALCharginoHadronicLimitAt208GeV](/documentation/code/classes/classgambit_1_1colliderbit_1_1opalcharginohadroniclimitat208gev/), [Gambit::ColliderBit::OPALCharginoLeptonicLimitAt208GeV](/documentation/code/classes/classgambit_1_1colliderbit_1_1opalcharginoleptoniclimitat208gev/), [Gambit::ColliderBit::OPALCharginoSemiLeptonicLimitAt208GeV](/documentation/code/classes/classgambit_1_1colliderbit_1_1opalcharginosemileptoniclimitat208gev/), [Gambit::ColliderBit::OPALDegenerateCharginoLimitAt208GeV](/documentation/code/classes/classgambit_1_1colliderbit_1_1opaldegeneratecharginolimitat208gev/), [Gambit::ColliderBit::OPALNeutralinoHadronicLimitAt208GeV](/documentation/code/classes/classgambit_1_1colliderbit_1_1opalneutralinohadroniclimitat208gev/), [Gambit::ColliderBit::OPALNeutralinoHadronicViaZLimitAt208GeV](/documentation/code/classes/classgambit_1_1colliderbit_1_1opalneutralinohadronicviazlimitat208gev/)

## Protected Types

|                | Name           |
| -------------- | -------------- |
| typedef std::vector< [P2](/documentation/code/classes/classgambit_1_1colliderbit_1_1p2/) > | **[Corners](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)**  |
| typedef std::vector< [LineSegment](/documentation/code/classes/classgambit_1_1colliderbit_1_1linesegment/) > | **[Contours](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)**  |
| typedef Contours * | **[ContoursPointer](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)**  |
| typedef std::map< unsigned, Contours * > | **[LimitContours](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)**  |
| typedef std::pair< unsigned, Contours * > | **[LimitContourEntry](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BaseLimitContainer](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)**() |
| virtual | **[~BaseLimitContainer](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)**() |
| virtual [P2](/documentation/code/classes/classgambit_1_1colliderbit_1_1p2/) | **[convertPt](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)**(double x, double y) const =0<br>Convert a point from pixel units to axis units, creating a [P2]().  |
| virtual bool | **[isWithinExclusionRegion](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)**(double x, double y, double mZ) const =0<br>Check to see if the point is within the exclusion region.  |
| virtual double | **[specialLimit](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)**(double , double ) const<br>Return the limit value outside of the exclusion region.  |
| double | **[limitAverage](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)**(double x, double y, double mZ) const<br>Two-pi averaging interpolator to find limits between limit curves.  |
| void | **[dumpPlotData](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)**(double xlow, double xhigh, double ylow, double yhigh, double mZ, std::string filename, int ngrid =100) const<br>Dump limit average data into a file for average debugging.  |
| void | **[dumpLightPlotData](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)**(std::string filename, int nperLine =20) const<br>Dump input limit contour data into a file for limit debugging.  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| std::vector< double > | **[_limitValuesSorted](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)**  |
| LimitContours | **[_limitContours](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)**  |
| [P2](/documentation/code/classes/classgambit_1_1colliderbit_1_1p2/) | **[_externalPoint](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)**  |

## Protected Types Documentation

### typedef Corners

```
typedef std::vector<P2> Gambit::ColliderBit::BaseLimitContainer::Corners;
```


### typedef Contours

```
typedef std::vector<LineSegment> Gambit::ColliderBit::BaseLimitContainer::Contours;
```


### typedef ContoursPointer

```
typedef Contours* Gambit::ColliderBit::BaseLimitContainer::ContoursPointer;
```


### typedef LimitContours

```
typedef std::map<unsigned, Contours*> Gambit::ColliderBit::BaseLimitContainer::LimitContours;
```


### typedef LimitContourEntry

```
typedef std::pair<unsigned, Contours*> Gambit::ColliderBit::BaseLimitContainer::LimitContourEntry;
```


## Public Functions Documentation

### function BaseLimitContainer

```
inline BaseLimitContainer()
```


### function ~BaseLimitContainer

```
virtual ~BaseLimitContainer()
```


### function convertPt

```
virtual P2 convertPt(
    double x,
    double y
) const =0
```

Convert a point from pixel units to axis units, creating a [P2](). 

**Reimplemented by**: [Gambit::ColliderBit::ALEPHSelectronLimitAt208GeV::convertPt](/documentation/code/classes/classgambit_1_1colliderbit_1_1alephselectronlimitat208gev/), [Gambit::ColliderBit::ALEPHSmuonLimitAt208GeV::convertPt](/documentation/code/classes/classgambit_1_1colliderbit_1_1alephsmuonlimitat208gev/), [Gambit::ColliderBit::ALEPHStauLimitAt208GeV::convertPt](/documentation/code/classes/classgambit_1_1colliderbit_1_1alephstaulimitat208gev/), [Gambit::ColliderBit::L3CharginoAllChannelsLimitAt188pt6GeV::convertPt](/documentation/code/classes/classgambit_1_1colliderbit_1_1l3charginoallchannelslimitat188pt6gev/), [Gambit::ColliderBit::L3CharginoLeptonicLimitAt188pt6GeV::convertPt](/documentation/code/classes/classgambit_1_1colliderbit_1_1l3charginoleptoniclimitat188pt6gev/), [Gambit::ColliderBit::L3NeutralinoAllChannelsLimitAt188pt6GeV::convertPt](/documentation/code/classes/classgambit_1_1colliderbit_1_1l3neutralinoallchannelslimitat188pt6gev/), [Gambit::ColliderBit::L3NeutralinoLeptonicLimitAt188pt6GeV::convertPt](/documentation/code/classes/classgambit_1_1colliderbit_1_1l3neutralinoleptoniclimitat188pt6gev/), [Gambit::ColliderBit::L3SelectronLimitAt205GeV::convertPt](/documentation/code/classes/classgambit_1_1colliderbit_1_1l3selectronlimitat205gev/), [Gambit::ColliderBit::L3SmuonLimitAt205GeV::convertPt](/documentation/code/classes/classgambit_1_1colliderbit_1_1l3smuonlimitat205gev/), [Gambit::ColliderBit::L3StauLimitAt205GeV::convertPt](/documentation/code/classes/classgambit_1_1colliderbit_1_1l3staulimitat205gev/), [Gambit::ColliderBit::L3ChargedGauginoSmallDeltaMWithHeavySneutrinoLimitAt188pt6GeV::convertPt](/documentation/code/classes/classgambit_1_1colliderbit_1_1l3chargedgauginosmalldeltamwithheavysneutrinolimitat188pt6gev/), [Gambit::ColliderBit::L3ChargedGauginoSmallDeltaMAnySneutrinoLimitAt188pt6GeV::convertPt](/documentation/code/classes/classgambit_1_1colliderbit_1_1l3chargedgauginosmalldeltamanysneutrinolimitat188pt6gev/), [Gambit::ColliderBit::L3ChargedHiggsinoSmallDeltaMLimitAt188pt6GeV::convertPt](/documentation/code/classes/classgambit_1_1colliderbit_1_1l3chargedhiggsinosmalldeltamlimitat188pt6gev/), [Gambit::ColliderBit::OPALCharginoHadronicLimitAt208GeV::convertPt](/documentation/code/classes/classgambit_1_1colliderbit_1_1opalcharginohadroniclimitat208gev/), [Gambit::ColliderBit::OPALCharginoSemiLeptonicLimitAt208GeV::convertPt](/documentation/code/classes/classgambit_1_1colliderbit_1_1opalcharginosemileptoniclimitat208gev/), [Gambit::ColliderBit::OPALCharginoLeptonicLimitAt208GeV::convertPt](/documentation/code/classes/classgambit_1_1colliderbit_1_1opalcharginoleptoniclimitat208gev/), [Gambit::ColliderBit::OPALCharginoAllChannelsLimitAt208GeV::convertPt](/documentation/code/classes/classgambit_1_1colliderbit_1_1opalcharginoallchannelslimitat208gev/), [Gambit::ColliderBit::OPALNeutralinoHadronicLimitAt208GeV::convertPt](/documentation/code/classes/classgambit_1_1colliderbit_1_1opalneutralinohadroniclimitat208gev/), [Gambit::ColliderBit::OPALNeutralinoHadronicViaZLimitAt208GeV::convertPt](/documentation/code/classes/classgambit_1_1colliderbit_1_1opalneutralinohadronicviazlimitat208gev/), [Gambit::ColliderBit::OPALDegenerateCharginoLimitAt208GeV::convertPt](/documentation/code/classes/classgambit_1_1colliderbit_1_1opaldegeneratecharginolimitat208gev/)


### function isWithinExclusionRegion

```
virtual bool isWithinExclusionRegion(
    double x,
    double y,
    double mZ
) const =0
```

Check to see if the point is within the exclusion region. 

**Reimplemented by**: [Gambit::ColliderBit::ALEPHSelectronLimitAt208GeV::isWithinExclusionRegion](/documentation/code/classes/classgambit_1_1colliderbit_1_1alephselectronlimitat208gev/), [Gambit::ColliderBit::ALEPHSmuonLimitAt208GeV::isWithinExclusionRegion](/documentation/code/classes/classgambit_1_1colliderbit_1_1alephsmuonlimitat208gev/), [Gambit::ColliderBit::ALEPHStauLimitAt208GeV::isWithinExclusionRegion](/documentation/code/classes/classgambit_1_1colliderbit_1_1alephstaulimitat208gev/), [Gambit::ColliderBit::L3CharginoAllChannelsLimitAt188pt6GeV::isWithinExclusionRegion](/documentation/code/classes/classgambit_1_1colliderbit_1_1l3charginoallchannelslimitat188pt6gev/), [Gambit::ColliderBit::L3CharginoLeptonicLimitAt188pt6GeV::isWithinExclusionRegion](/documentation/code/classes/classgambit_1_1colliderbit_1_1l3charginoleptoniclimitat188pt6gev/), [Gambit::ColliderBit::L3NeutralinoAllChannelsLimitAt188pt6GeV::isWithinExclusionRegion](/documentation/code/classes/classgambit_1_1colliderbit_1_1l3neutralinoallchannelslimitat188pt6gev/), [Gambit::ColliderBit::L3NeutralinoLeptonicLimitAt188pt6GeV::isWithinExclusionRegion](/documentation/code/classes/classgambit_1_1colliderbit_1_1l3neutralinoleptoniclimitat188pt6gev/), [Gambit::ColliderBit::L3SelectronLimitAt205GeV::isWithinExclusionRegion](/documentation/code/classes/classgambit_1_1colliderbit_1_1l3selectronlimitat205gev/), [Gambit::ColliderBit::L3SmuonLimitAt205GeV::isWithinExclusionRegion](/documentation/code/classes/classgambit_1_1colliderbit_1_1l3smuonlimitat205gev/), [Gambit::ColliderBit::L3StauLimitAt205GeV::isWithinExclusionRegion](/documentation/code/classes/classgambit_1_1colliderbit_1_1l3staulimitat205gev/), [Gambit::ColliderBit::L3ChargedGauginoSmallDeltaMWithHeavySneutrinoLimitAt188pt6GeV::isWithinExclusionRegion](/documentation/code/classes/classgambit_1_1colliderbit_1_1l3chargedgauginosmalldeltamwithheavysneutrinolimitat188pt6gev/), [Gambit::ColliderBit::L3ChargedGauginoSmallDeltaMAnySneutrinoLimitAt188pt6GeV::isWithinExclusionRegion](/documentation/code/classes/classgambit_1_1colliderbit_1_1l3chargedgauginosmalldeltamanysneutrinolimitat188pt6gev/), [Gambit::ColliderBit::L3ChargedHiggsinoSmallDeltaMLimitAt188pt6GeV::isWithinExclusionRegion](/documentation/code/classes/classgambit_1_1colliderbit_1_1l3chargedhiggsinosmalldeltamlimitat188pt6gev/), [Gambit::ColliderBit::OPALDegenerateCharginoLimitAt208GeV::isWithinExclusionRegion](/documentation/code/classes/classgambit_1_1colliderbit_1_1opaldegeneratecharginolimitat208gev/), [Gambit::ColliderBit::OPALCharginoHadronicLimitAt208GeV::isWithinExclusionRegion](/documentation/code/classes/classgambit_1_1colliderbit_1_1opalcharginohadroniclimitat208gev/), [Gambit::ColliderBit::OPALCharginoSemiLeptonicLimitAt208GeV::isWithinExclusionRegion](/documentation/code/classes/classgambit_1_1colliderbit_1_1opalcharginosemileptoniclimitat208gev/), [Gambit::ColliderBit::OPALCharginoLeptonicLimitAt208GeV::isWithinExclusionRegion](/documentation/code/classes/classgambit_1_1colliderbit_1_1opalcharginoleptoniclimitat208gev/), [Gambit::ColliderBit::OPALCharginoAllChannelsLimitAt208GeV::isWithinExclusionRegion](/documentation/code/classes/classgambit_1_1colliderbit_1_1opalcharginoallchannelslimitat208gev/), [Gambit::ColliderBit::OPALNeutralinoHadronicLimitAt208GeV::isWithinExclusionRegion](/documentation/code/classes/classgambit_1_1colliderbit_1_1opalneutralinohadroniclimitat208gev/), [Gambit::ColliderBit::OPALNeutralinoHadronicViaZLimitAt208GeV::isWithinExclusionRegion](/documentation/code/classes/classgambit_1_1colliderbit_1_1opalneutralinohadronicviazlimitat208gev/)


### function specialLimit

```
virtual double specialLimit(
    double ,
    double 
) const
```

Return the limit value outside of the exclusion region. 

### function limitAverage

```
double limitAverage(
    double x,
    double y,
    double mZ
) const
```

Two-pi averaging interpolator to find limits between limit curves. 

### function dumpPlotData

```
void dumpPlotData(
    double xlow,
    double xhigh,
    double ylow,
    double yhigh,
    double mZ,
    std::string filename,
    int ngrid =100
) const
```

Dump limit average data into a file for average debugging. 

### function dumpLightPlotData

```
void dumpLightPlotData(
    std::string filename,
    int nperLine =20
) const
```

Dump input limit contour data into a file for limit debugging. 

## Protected Attributes Documentation

### variable _limitValuesSorted

```
std::vector< double > _limitValuesSorted;
```


**Note**: Inherited classes must fill the following members: 

### variable _limitContours

```
LimitContours _limitContours;
```


### variable _externalPoint

```
P2 _externalPoint;
```


-------------------------------

Updated on 2022-09-08 at 01:05:17 +0000