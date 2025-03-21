---
title: "file DarkBit/SimpleHist.hpp"

description: "[No description available]"

---

# file DarkBit/SimpleHist.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::DarkBit](/documentation/code/namespaces/namespacegambit_1_1darkbit/)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| struct | **[Gambit::DarkBit::SimpleHist](/documentation/code/classes/structgambit_1_1darkbit_1_1simplehist/)** <br>Histogram class for cascade decays.  |

## Detailed Description


**Author**: Lars A. Dal ([l.a.dal@fys.uio.no](mailto:l.a.dal@fys.uio.no)) 

**Date**: 2015 Feb

Type definition header for DarkBit SimpleHist types.



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Type definition header for DarkBit SimpleHist
///  types.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Lars A. Dal
///          (l.a.dal@fys.uio.no)
///  \date 2015 Feb
///
///  *********************************************


#ifndef __SimpleHist_hpp__
#define __SimpleHist_hpp__

#include <vector>
#include <map>

#include "gambit/Utils/util_types.hpp"
#include "gambit/cmake/cmake_variables.hpp"
#include "gambit/Elements/daFunk.hpp"


namespace Gambit
{

  namespace DarkBit
  {

    /// Histogram class for cascade decays
    struct SimpleHist
    {

        // Functions

        SimpleHist(){}

        SimpleHist(int nBins, double Emin, double Emax, bool logscale);

        /// Constructor taking lower bins edges as input.
        /// Last element will be used as upper bin edge for upper bin (Vector with N elements will give N-1 bins).
        SimpleHist(std::vector<double> binLower);

        /// Add an entry to histogram
        void addEvent(double E, double weight=1.0);

        /// Add an entry to a specified bin
        void addToBin(int bin, double weight=1.0);

        /// Add a box spectrum to the histogram
        void addBox(double Emin, double Emax, double weight=1.0);

        /// Add content of input histogram as weights.
        /// Important: Input histogram MUST have identical binning for this to give correct results.
        void addHistAsWeights_sameBin(SimpleHist &in);

        /// Get error for a specified bin
        double getError(int bin) const;

        /// Get relative error for a specified bin
        double getRelError(int bin) const;

        /// Divide all histogram bins by the respective bin size
        void divideByBinSize();

        /// Multiply all bin contents by x
        void multiply(double x);

        /// Find bin index for given value
        int findIndex(double val) const;

        /// Retrieve size of given bins
        double binSize(int bin) const;

        /// Get central value of bin
        double binCenter(int bin) const;

        /// Double get central values of all bins
        std::vector<double> getBinCenters() const;

        const std::vector<double>& getBinValues() const;

        void getEdges(double& lower, double& upper) const;

        // Variables
        std::vector<double> binLower;
        std::vector<double> binVals;
        /// Sum of the squares of all weights
        std::vector<double> wtSq;
        int nBins;
    };

    typedef std::map<str, std::map<str, Gambit::DarkBit::SimpleHist> > simpleHistContainter;
    typedef std::map<str, int> stringIntMap;
    typedef std::map<str, daFunk::Funk> stringFunkMap;

  }

}

#endif // defined __SimpleHist_hpp__
```


-------------------------------

Updated on 2025-02-12 at 16:10:35 +0000
