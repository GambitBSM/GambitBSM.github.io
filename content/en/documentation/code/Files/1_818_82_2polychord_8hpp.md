---
title: "file 1.18.2/1.18.2/polychord.hpp"

description: "[No description available]"

---

# file 1.18.2/1.18.2/polychord.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::PolyChord_1_18_2](/documentation/code/namespaces/namespacegambit_1_1polychord__1__18__2/)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| struct | **[Settings](/documentation/code/classes/structsettings/)**  |
| class | **[Gambit::PolyChord_1_18_2::LogLikeWrapper](/documentation/code/classes/classgambit_1_1polychord__1__18__2_1_1loglikewrapper/)** <br>Class to connect PolyChord log-likelihood function and ScannerBit likelihood function.  |

## Functions

|                | Name           |
| -------------- | -------------- |
| void | **[run_polychord](/documentation/code/files/1_818_82_2polychord_8hpp/#function-run-polychord)**(double(*)(double *, int, double *, int) loglikelihood, void(*)(int, int, int, double *, double *, double *, double, double) dumper, [Settings](/documentation/code/classes/structsettings/) ) |

## Detailed Description


**Author**: 

  * Ben Farmer ([ben.farmer@gmail.com](mailto:ben.farmer@gmail.com)) 
  * Will Handley ([wh260@cam.ac.uk](mailto:wh260@cam.ac.uk)) 
  * Patrick Stoecker ([stoecker@physik.rwth-aachen.de](mailto:stoecker@physik.rwth-aachen.de)) 
  * Anders Kvellestad ([anders.kvellestad@fys.uio.no](mailto:anders.kvellestad@fys.uio.no)) 


**Date**: 

  * 2015 January
  * 2018 May
  * May 2020
  * June 2022


ScannerBit interface to PolyChord 1.18.2

Header file



------------------

Authors (add name and date if you modify):



------------------


## Functions Documentation

### function run_polychord

```
void run_polychord(
    double(*)(double *, int, double *, int) loglikelihood,
    void(*)(int, int, int, double *, double *, double *, double, double) dumper,
    Settings 
)
```




## Source code

```
//  GAMBIT: Global and Modular BSM Inference Tool
//  *********************************************
///  \file
///
///  ScannerBit interface to PolyChord 1.18.2
///
///  Header file
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Ben Farmer
///          (ben.farmer@gmail.com)
///  \date 2015 January
///
///  \author Will Handley
///          (wh260@cam.ac.uk)
///  \date 2018 May
///
///  \author Patrick Stoecker
///          (stoecker@physik.rwth-aachen.de)
///  \date May 2020
///
///  \author Anders Kvellestad
///          (anders.kvellestad@fys.uio.no)
///  \date June 2022
///
///  *********************************************

#ifndef __polychord_hpp__
#define __polychord_hpp__

#include "gambit/ScannerBit/scanner_plugin.hpp"

// Auxilliary classes and functions needed by polychord

struct Settings
{
   int nDims;
   int nDerived;
   int nlive;
   int num_repeats;
   int nprior;
   int nfail;
   bool do_clustering;
   int feedback;
   double precision_criterion;
   double logzero;
   int max_ndead;
   double boost_posterior;
   bool posteriors;
   bool equals;
   bool cluster_posteriors;
   bool write_resume;
   bool write_paramnames;
   bool read_resume;
   bool write_stats;
   bool write_live;
   bool write_dead;
   bool write_prior;
   bool maximise;
   double compression_factor;
   std::string base_dir;
   std::string file_root;
   std::vector<double> grade_frac;
   std::vector<int> grade_dims;
   std::vector<double> loglikes;
   std::vector<int> nlives;
   int seed;

   Settings(int _nDims=0,int _nDerived=0);
};

void run_polychord( 
         double (*loglikelihood)(double*,int,double*,int),
         void (*dumper)(int,int,int,double*,double*,double*,double,double), 
         Settings);


namespace Gambit
{

   namespace PolyChord_1_18_2
   {

      /// Typedef for the ScannerBit pointer to the external loglikelihood function
      typedef Gambit::Scanner::like_ptr scanPtr;

      /// Bring printer_interface and printer names into this scope
      using Gambit::Scanner::printer_interface;
      using Gambit::Scanner::printer;

      /// Class to connect PolyChord log-likelihood function and ScannerBit likelihood function
      class LogLikeWrapper
      {
         private:
            /// Scanner pointer (points to the ScannerBit provided log-likelihood function)
            scanPtr boundLogLike;

            /// Reference to a printer_interface object
            printer_interface& boundPrinter;

         public:
            /// Constructor
            LogLikeWrapper(scanPtr, printer_interface&);
   
            /// Main interface function from PolyChord to ScannerBit-supplied loglikelihood function 
            double LogLike(double*, int, double*, int);

            /// Main interface to PolyChord dumper routine   
            void dumper(int, int, int, double*, double*, double*, double, double);

            // PolyChord Hypercube index location for each parameter
            // gambit_hypercube[paramname] = polychord_hypercube[index_map[paramname]]
            // This is required because PolyChord needs parameters to be
            // ordered slow-to-fast to exploit a speed hierarchy
            std::unordered_map<std::string, int> index_map, derived_index_map;

            /// copy of the settings in use.
            Settings boundSettings;

            /// Disable printing for speeds greater and equal than
            /// Speeds start at 0
            /// A value of -1 means that all evaluations are printed
            int printer_speed_threshold = -1;
      };

      ///@{ C-functions to pass to PolyChord for the callbacks
      double callback_loglike(double*, int, double*, int);
      void callback_dumper(int, int, int, double*, double*, double*, double, double);
      ///@}      

   } // End PolyChord namespace

} // End Gambit namespace

#endif
```


-------------------------------

Updated on 2025-02-12 at 16:10:33 +0000
