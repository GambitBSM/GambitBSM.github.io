---
title: "class Gambit::ColliderBit::L3SelectronLimitAt205GeV"
description: "A class to contain the limit data from L3_PLB580_2004_37, figure 2a. "

---

# class Gambit::ColliderBit::L3SelectronLimitAt205GeV



A class to contain the limit data from L3_PLB580_2004_37, figure 2a. 


`#include <L3SleptonLimits.hpp>`

Inherits from [Gambit::ColliderBit::BaseLimitContainer](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual [P2](/documentation/code/classes/classgambit_1_1colliderbit_1_1p2/) | **[convertPt](/documentation/code/classes/classgambit_1_1colliderbit_1_1l3selectronlimitat205gev/#function-gambitcolliderbitl3selectronlimitat205gev-convertpt)**(double x, double y) const<br>Convert a point from pixel units to axis units.  |
| virtual bool | **[isWithinExclusionRegion](/documentation/code/classes/classgambit_1_1colliderbit_1_1l3selectronlimitat205gev/#function-gambitcolliderbitl3selectronlimitat205gev-iswithinexclusionregion)**(double x, double y, double mZ) const<br>Check to see if the point is within the exclusion region.  |
| | **[L3SelectronLimitAt205GeV](/documentation/code/classes/classgambit_1_1colliderbit_1_1l3selectronlimitat205gev/#function-gambitcolliderbitl3selectronlimitat205gev-l3selectronlimitat205gev)**() |

## Additional inherited members

**Protected Types inherited from [Gambit::ColliderBit::BaseLimitContainer](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)**

|                | Name           |
| -------------- | -------------- |
| typedef std::vector< [P2](/documentation/code/classes/classgambit_1_1colliderbit_1_1p2/) > | **[Corners](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/#typedef-gambitcolliderbitbaselimitcontainer-corners)**  |
| typedef std::vector< [LineSegment](/documentation/code/classes/classgambit_1_1colliderbit_1_1linesegment/) > | **[Contours](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/#typedef-gambitcolliderbitbaselimitcontainer-contours)**  |
| typedef Contours * | **[ContoursPointer](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/#typedef-gambitcolliderbitbaselimitcontainer-contourspointer)**  |
| typedef std::map< unsigned, Contours * > | **[LimitContours](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/#typedef-gambitcolliderbitbaselimitcontainer-limitcontours)**  |
| typedef std::pair< unsigned, Contours * > | **[LimitContourEntry](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/#typedef-gambitcolliderbitbaselimitcontainer-limitcontourentry)**  |

**Public Functions inherited from [Gambit::ColliderBit::BaseLimitContainer](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)**

|                | Name           |
| -------------- | -------------- |
| | **[BaseLimitContainer](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/#function-gambitcolliderbitbaselimitcontainer-baselimitcontainer)**() |
| virtual | **[~BaseLimitContainer](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/#function-gambitcolliderbitbaselimitcontainer-baselimitcontainer)**() |
| virtual double | **[specialLimit](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/#function-gambitcolliderbitbaselimitcontainer-speciallimit)**(double , double ) const<br>Return the limit value outside of the exclusion region.  |
| double | **[limitAverage](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/#function-gambitcolliderbitbaselimitcontainer-limitaverage)**(double x, double y, double mZ) const<br>Two-pi averaging interpolator to find limits between limit curves.  |
| void | **[dumpPlotData](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/#function-gambitcolliderbitbaselimitcontainer-dumpplotdata)**(double xlow, double xhigh, double ylow, double yhigh, double mZ, std::string filename, int ngrid =100) const<br>Dump limit average data into a file for average debugging.  |
| void | **[dumpLightPlotData](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/#function-gambitcolliderbitbaselimitcontainer-dumplightplotdata)**(std::string filename, int nperLine =20) const<br>Dump input limit contour data into a file for limit debugging.  |

**Protected Attributes inherited from [Gambit::ColliderBit::BaseLimitContainer](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)**

|                | Name           |
| -------------- | -------------- |
| std::vector< double > | **[_limitValuesSorted](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/#variable-gambitcolliderbitbaselimitcontainer-limitvaluessorted)**  |
| LimitContours | **[_limitContours](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/#variable-gambitcolliderbitbaselimitcontainer-limitcontours)**  |
| [P2](/documentation/code/classes/classgambit_1_1colliderbit_1_1p2/) | **[_externalPoint](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/#variable-gambitcolliderbitbaselimitcontainer-externalpoint)**  |


## Public Functions Documentation

### function convertPt

```
virtual P2 convertPt(
    double x,
    double y
) const
```

Convert a point from pixel units to axis units. 

**Reimplements**: [Gambit::ColliderBit::BaseLimitContainer::convertPt](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/#function-gambitcolliderbitbaselimitcontainer-convertpt)


### function isWithinExclusionRegion

```
virtual bool isWithinExclusionRegion(
    double x,
    double y,
    double mZ
) const
```

Check to see if the point is within the exclusion region. 

**Reimplements**: [Gambit::ColliderBit::BaseLimitContainer::isWithinExclusionRegion](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/#function-gambitcolliderbitbaselimitcontainer-iswithinexclusionregion)


### function L3SelectronLimitAt205GeV

```
L3SelectronLimitAt205GeV()
```


-------------------------------

Updated on 2022-09-08 at 01:48:55 +0000