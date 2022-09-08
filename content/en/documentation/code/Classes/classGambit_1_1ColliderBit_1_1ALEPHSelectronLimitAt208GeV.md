---
title: "class Gambit::ColliderBit::ALEPHSelectronLimitAt208GeV"
description: "A class to contain the limit data from ALEPH_PLB526_2002_206, figure 3a. "

---

# class Gambit::ColliderBit::ALEPHSelectronLimitAt208GeV



A class to contain the limit data from ALEPH_PLB526_2002_206, figure 3a. 


`#include <ALEPHSleptonLimits.hpp>`

Inherits from [Gambit::ColliderBit::BaseLimitContainer](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual [P2](/documentation/code/classes/classgambit_1_1colliderbit_1_1p2/) | **[convertPt](/documentation/code/classes/classgambit_1_1colliderbit_1_1alephselectronlimitat208gev/)**(double x, double y) const<br>Convert a point from pixel units to axis units.  |
| virtual bool | **[isWithinExclusionRegion](/documentation/code/classes/classgambit_1_1colliderbit_1_1alephselectronlimitat208gev/)**(double x, double y, double mZ) const<br>Check to see if the point is within the exclusion region.  |
| | **[ALEPHSelectronLimitAt208GeV](/documentation/code/classes/classgambit_1_1colliderbit_1_1alephselectronlimitat208gev/)**() |

## Additional inherited members

**Protected Types inherited from [Gambit::ColliderBit::BaseLimitContainer](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)**

|                | Name           |
| -------------- | -------------- |
| typedef std::vector< [P2](/documentation/code/classes/classgambit_1_1colliderbit_1_1p2/) > | **[Corners](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)**  |
| typedef std::vector< [LineSegment](/documentation/code/classes/classgambit_1_1colliderbit_1_1linesegment/) > | **[Contours](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)**  |
| typedef Contours * | **[ContoursPointer](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)**  |
| typedef std::map< unsigned, Contours * > | **[LimitContours](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)**  |
| typedef std::pair< unsigned, Contours * > | **[LimitContourEntry](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)**  |

**Public Functions inherited from [Gambit::ColliderBit::BaseLimitContainer](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)**

|                | Name           |
| -------------- | -------------- |
| | **[BaseLimitContainer](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)**() |
| virtual | **[~BaseLimitContainer](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)**() |
| virtual double | **[specialLimit](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)**(double , double ) const<br>Return the limit value outside of the exclusion region.  |
| double | **[limitAverage](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)**(double x, double y, double mZ) const<br>Two-pi averaging interpolator to find limits between limit curves.  |
| void | **[dumpPlotData](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)**(double xlow, double xhigh, double ylow, double yhigh, double mZ, std::string filename, int ngrid =100) const<br>Dump limit average data into a file for average debugging.  |
| void | **[dumpLightPlotData](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)**(std::string filename, int nperLine =20) const<br>Dump input limit contour data into a file for limit debugging.  |

**Protected Attributes inherited from [Gambit::ColliderBit::BaseLimitContainer](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)**

|                | Name           |
| -------------- | -------------- |
| std::vector< double > | **[_limitValuesSorted](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)**  |
| LimitContours | **[_limitContours](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)**  |
| [P2](/documentation/code/classes/classgambit_1_1colliderbit_1_1p2/) | **[_externalPoint](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)**  |


## Public Functions Documentation

### function convertPt

```
virtual P2 convertPt(
    double x,
    double y
) const
```

Convert a point from pixel units to axis units. 

**Reimplements**: [Gambit::ColliderBit::BaseLimitContainer::convertPt](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)


### function isWithinExclusionRegion

```
virtual bool isWithinExclusionRegion(
    double x,
    double y,
    double mZ
) const
```

Check to see if the point is within the exclusion region. 

**Reimplements**: [Gambit::ColliderBit::BaseLimitContainer::isWithinExclusionRegion](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)


### function ALEPHSelectronLimitAt208GeV

```
ALEPHSelectronLimitAt208GeV()
```


-------------------------------

Updated on 2022-09-08 at 01:05:16 +0000