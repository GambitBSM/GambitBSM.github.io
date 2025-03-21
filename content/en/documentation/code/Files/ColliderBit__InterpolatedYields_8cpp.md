---
title: "file src/ColliderBit_InterpolatedYields.cpp"

description: "[No description available]"

---

# file src/ColliderBit_InterpolatedYields.cpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::ColliderBit](/documentation/code/namespaces/namespacegambit_1_1colliderbit/)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Gambit::ColliderBit::Model_analysis_info](/documentation/code/classes/classgambit_1_1colliderbit_1_1model__analysis__info/)**  |
| struct | **[Gambit::ColliderBit::_gsl_target_func_params](/documentation/code/classes/structgambit_1_1colliderbit_1_1__gsl__target__func__params/)** <br>A struct to contain parameters for the GSL optimiser target function.  |
| class | **[Gambit::ColliderBit::Dijet_analysis_info](/documentation/code/classes/classgambit_1_1colliderbit_1_1dijet__analysis__info/)** <br>A class to hold analysis information for DiJets (specific to DMsimp models)  |

## Detailed Description


**Author**: 

  * Martin White ([martin.white@adelaide.edu.au](mailto:martin.white@adelaide.edu.au))
  * Andre Scaffidi ([andre.scaffidi@adelaide.edu.au](mailto:andre.scaffidi@adelaide.edu.au)) 
  * Tomas Gonzalo ([tomas.gonzalo@kit.edu](mailto:tomas.gonzalo@kit.edu)) 
  * Anders Kvellestad ([anders.kvellestad@fys.uio.no](mailto:anders.kvellestad@fys.uio.no)) 
  * Chris Chang ([christopher.chang@uq.net.au](mailto:christopher.chang@uq.net.au)) 
  * Taylor R. Gray ([gray@chalmers.se](mailto:gray@chalmers.se)) 


**Date**: 

  * 2019 Aug
  * 2021 Apr, 2023 Nov
  * 2021 May
  * 2022 June
  * 2023 Oct


Functions for LHC analyses that use tabulated interpolations rather than direct MC simulation. For now this functionality is specific to the DMEFT and DMsimp models, but it will be turned into a general feature in ColliderBit.



------------------

Authors (add name and date if you modify):


Analyses based on: arxiv:1711.03301 and [https://journals.aps.org/prd/abstract/10.1103/PhysRevD.97.092005](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.97.092005) 139invfb analysis based on arXiv:2102.10874

BEAMDUMP analyses based on: arXiv:1609.01770, arXiv:2307.02404, arXiv:1107.4580, arXiv:1807.06137



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Functions for LHC analyses that use tabulated interpolations
///  rather than direct MC simulation. For now this functionality
///  is specific to the DMEFT and DMsimp models, but it will be turned into
///  a general feature in ColliderBit.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Martin White
///          (martin.white@adelaide.edu.au)
///
///  \author Andre Scaffidi
///          (andre.scaffidi@adelaide.edu.au)
///  \date 2019 Aug
///
///  \author Tomas Gonzalo
///          (tomas.gonzalo@kit.edu)
///  \date 2021 Apr, 2023 Nov
///
///  \author Anders Kvellestad
///          (anders.kvellestad@fys.uio.no)
///  \date 2021 May
///
///  \author Chris Chang
///          (christopher.chang@uq.net.au)
///  \date 2022 June
///
///  \author Taylor R. Gray
///          (gray@chalmers.se)
///  \date 2023 Oct
///
///  Analyses based on: arxiv:1711.03301 and https://journals.aps.org/prd/abstract/10.1103/PhysRevD.97.092005
///  139invfb analysis based on arXiv:2102.10874
///
///  BEAMDUMP analyses based on:
///     arXiv:1609.01770, arXiv:2307.02404, arXiv:1107.4580, arXiv:1807.06137
///
///  *********************************************

// Needs GSL 2
#include <gsl/gsl_math.h>
#include <gsl/gsl_interp2d.h>
#include <gsl/gsl_spline2d.h>
#include <gsl/gsl_sf_gamma.h>

#include "Eigen/Eigenvalues"
#include "Eigen/Eigen"

#include "multimin/multimin.hpp"

#include "gambit/ColliderBit/analyses/Analysis.hpp"
#include "gambit/Elements/gambit_module_headers.hpp"
#include "gambit/ColliderBit/ColliderBit_rollcall.hpp"
#include "gambit/Utils/interp_collection.hpp"
#include "gambit/Utils/file_lock.hpp"
#include "gambit/Utils/util_macros.hpp"
#include "gambit/ColliderBit/Utils.hpp"


// #define COLLIDERBIT_DEBUG_PROFILING
// #define COLLIDERBIT_DEBUG
// #define DEBUG_PREFIX "DEBUG: OMP thread " << omp_get_thread_num() << ":  "

namespace Gambit
{

  namespace ColliderBit
  {

    // =========== Useful stuff ===========

    /// A minimal class with analysis info, maps for containing collections of 1D/2D/4D/5D interpolators
    /// and some helper functions for adding and accessing the interpolators, and for
    /// adding a background covariance matrix. Currently this class is tailored specifically
    /// for the DMEFT/DMsimp models -- it will be generalized in the future.
    class Model_analysis_info
    {
      public:

        // Standard analysis info:

        str name;
        double lumi_invfb;
        size_t n_signal_regions;
        std::vector<int> obsnum;
        std::vector<double> bkgnum;
        std::vector<double> bkgerr;
        Eigen::MatrixXd bkgcov;

        // A map to hold any extra non-standard numbers we might need for a given analysis.
        // For the DMSIMP/DMEFT-specific cases we'll use this to store the MET spectrum bin limits
        std::map<str, std::vector<double>> extra_info; // Any additional analysis-specific numbers

        // Maps containing 1D and 2D interpolators
        std::map<str,std::unique_ptr<Utils::interp1d_gsl_collection>> interp1d;
        std::map<str,std::unique_ptr<Utils::interp2d_gsl_collection>> interp2d;

        // Maps containing 4D and 5D interpolators
        std::map<str,std::unique_ptr<Utils::interp4d_collection>> interp4d;
        std::map<str,std::unique_ptr<Utils::interp5d_collection>> interp5d;

        // Helper functions

        void add_bkgcov(const std::vector< std::vector<double>>& bkgcov_in)
        {
          assert( bkgcov_in.size() > 0 && bkgcov_in.size() == n_signal_regions );
          assert( bkgcov_in[0].size() > 0 && bkgcov_in[0].size() == n_signal_regions );

          // Fill our Eigen matrix
          bkgcov = Eigen::MatrixXd(n_signal_regions, n_signal_regions);
          for (size_t i = 0; i < n_signal_regions; i++)
          {
            bkgcov.row(i) = Eigen::VectorXd::Map(&bkgcov_in[i][0], bkgcov_in[i].size());
          }
        }

        void add_interp1d(str name, str filename, std::vector<str> colnames)
        {
          assert (interp1d.count(name) == 0); // Make sure we're not overwriting an existing entry
          interp1d[name] = std::unique_ptr<Utils::interp1d_gsl_collection>(new Utils::interp1d_gsl_collection(name, filename, colnames));
        }

        void add_interp2d(str name, str filename, std::vector<str> colnames)
        {
          assert (interp2d.count(name) == 0); // Make sure we're not overwriting an existing entry
          interp2d[name] = std::unique_ptr<Utils::interp2d_gsl_collection>(new Utils::interp2d_gsl_collection(name, filename, colnames));
        }

        void add_interp4d(str name, str filename, std::vector<str> colnames, bool allow_missing_points)
        {
          assert (interp4d.count(name) == 0); // Make sure we're not overwriting an existing entry
          interp4d[name] = std::unique_ptr<Utils::interp4d_collection>(new Utils::interp4d_collection(name, filename, colnames, allow_missing_points, 0.0));
        }

        void add_interp5d(str name, str filename, std::vector<str> colnames, bool allow_missing_points)
        {
          assert (interp5d.count(name) == 0); // Make sure we're not overwriting an existing entry
          interp5d[name] = std::unique_ptr<Utils::interp5d_collection>(new Utils::interp5d_collection(name, filename, colnames, allow_missing_points, 0.0));
        }

        // Call the correct interpolation creator depending on number of dimensions
        void add_interpNd(str name, str filename, std::vector<str> colnames, int N, bool allow_missing_points)
        {
          if (N == 1)
          {
            add_interp1d(name, filename, colnames);
          } else if (N == 2)
          {
            add_interp2d(name, filename, colnames);
          } else if (N == 4)
          {
            add_interp4d(name, filename, colnames, allow_missing_points);
          } else if (N == 5)
          {
            add_interp5d(name, filename, colnames, allow_missing_points);
          } else
          {
            ColliderBit_error().raise(LOCAL_INFO, "ERROR! ColliderBit_InterpolatedYields: Trying to call an interpolator that doesn't exist.");
          }

        }

        bool has_interp1d(str name) const
        {
          return interp1d.find(name) != interp1d.end();
        }

        const Utils::interp1d_gsl_collection& get_interp1d(str name) const
        {
          if(not has_interp1d(name))
            ColliderBit_error().raise(LOCAL_INFO, "ERROR! Interpolator does not have a 1d collection");
          return *interp1d.at(name);
        }

        bool has_interp2d(str name) const
        {
          return interp2d.find(name) != interp2d.end();
        }

        const Utils::interp2d_gsl_collection& get_interp2d(str name) const
        {
          if(not has_interp2d(name))
            ColliderBit_error().raise(LOCAL_INFO, "ERROR! Interpolator does not have a 2d collection");
          return *interp2d.at(name);
        }

        bool has_interp4d(str name) const
        {
          return interp4d.find(name) != interp4d.end();
        }

        Utils::interp4d_collection& get_interp4d(str name) const
        {
          if(not has_interp4d(name))
            ColliderBit_error().raise(LOCAL_INFO, "ERROR! Interpolator does not have a 4d collection");
          return *interp4d.at(name);
        }

        bool has_interp5d(str name) const
        {
          return interp5d.find(name) != interp5d.end();
        }

        Utils::interp5d_collection& get_interp5d(str name) const
        {
          if(not has_interp5d(name))
            ColliderBit_error().raise(LOCAL_INFO, "ERROR! Interpolator does not have a 5d collection");
          return *interp5d.at(name);
        }

    };

    /// A struct to contain parameters for the GSL optimiser target function
    struct _gsl_target_func_params
    {
      double lambda;
      AnalysisDataPointers adata_ptrs_original;
      std::vector<str> skip_analyses;
      bool use_covar;
      bool use_marg;
      bool combine_nocovar_SRs;
      bool use_fulllikes;
    };


    /// A global map from analysis name to Model_analysis_info instance.
    /// This map is initialized by the function fill_analysis_info_map,
    /// which is called the first time DMEFT_results run.
    std::map<str,Model_analysis_info> analysis_info_map;


    // =========== Forward declarations ===========

    /// Forward declaration of funtion in LHC_likelihoods
    // @todo Interpolation will not currently work with the FullLikes backend. None of the currently written interpolation analysis require this.
    void fill_analysis_loglikes(const AnalysisData&, AnalysisLogLikes&, bool, bool, bool, bool, bool (*FullLikes_FileExists)(const str&), int (*FullLikes_ReadIn)(const str&, const str&), double (*FullLikes_Evaluate)(std::map<str,double>&,const str&), const std::string);

    /// Forward declarations of functions in this file
    void DMEFT_fill_analysis_info_map();
    void DMsimp_fill_analysis_info_map(std::map<str,str>, std::map<str,std::vector<str>>, int);
    void SubGeVDM_fill_analysis_info_map(std::map<str,str>, std::map<str,std::vector<str>>);

    void DMEFT_results(AnalysisDataPointers&);
    void DMEFT_results_profiled(AnalysisDataPointers&);
    void DMEFT_results_cutoff(AnalysisDataPointers&);
    void DMsimpVectorMedScalarDM_monojet_results(AnalysisDataPointers&);
    void DMsimpVectorMedMajoranaDM_monojet_results(AnalysisDataPointers&);
    void DMsimpVectorMedDiracDM_monojet_results(AnalysisDataPointers&);
    void SubGeVDM_results(AnalysisDataPointers&);

    void get_DMEFT_signal_yields_dim6_operator(std::vector<double>&, const str, const Model_analysis_info&, double, double, double, double);
    void get_DMEFT_signal_yields_dim7_operator(std::vector<double>&, const str, const Model_analysis_info&, double, double, double);
    void get_DMsimpVectorMedScalarDM_signal_yields(std::vector<double>&, const Model_analysis_info&, double, double, double, double);
    void get_DMsimpVectorMedMajoranaDM_signal_yields(std::vector<double>&, const Model_analysis_info&, double, double, double, double);
    void get_DMsimpVectorMedDiracDM_signal_yields(std::vector<double>&, const Model_analysis_info&, double, double, double, double, double);
    void get_SubGeVDM_scalar_signal_yields(std::vector<double>&, const Model_analysis_info&, double, double, double, double);
    void get_SubGeVDM_fermion_signal_yields(std::vector<double>&, const Model_analysis_info&, double, double, double, double);

    void get_DMEFT_signal_yields_dim6_operator(std::vector<double>&, const str, const Model_analysis_info&, double, double, double, double);
    void get_DMEFT_signal_yields_dim7_operator(std::vector<double>&, const str, const Model_analysis_info&, double, double, double);
    void get_DMsimpVectorMedScalarDM_signal_yields(std::vector<double>&, const Model_analysis_info&, double, double, double, double);
    void get_DMsimpVectorMedMajoranaDM_signal_yields(std::vector<double>&, const Model_analysis_info&, double, double, double, double);
    void get_DMsimpVectorMedDiracDM_signal_yields(std::vector<double>&, const Model_analysis_info&, double, double, double, double, double);
    void get_DMsimpVectorMedVectorDM_signal_yields(std::vector<double>&, const Model_analysis_info&, double, double, double, double);

    void get_all_DMEFT_signal_yields(std::vector<double>&, const Model_analysis_info&, const Spectrum&);
    void get_all_DMsimp_signal_yields(std::vector<double>&, const Model_analysis_info&, const Spectrum&, str&);
    void get_all_SubGeVDM_signal_yields(std::vector<double>&, const Model_analysis_info&, const Spectrum&, str&);


    void signal_modifier_function(AnalysisData&, double, double);
    void signal_cutoff_function(AnalysisData&, double);

    void _gsl_target_func(const size_t, const double*, void*, double*);

    void calc_DMEFT_profiled_LHC_nuisance_params(map_str_dbl&);

    void InterpolatedMCInfo(MCLoopInfo&);


    // =========== Functions ===========

    /// A function to fill the analysis_info_map given an analysis
    /// This is where all the analysis-specific numbers and file names go.
    void fill_analysis_info_map(str current_analysis_name, Model_analysis_info* current_ainfo)
    {

      // Helper variables
      std::vector<str> colnames;
      std::vector<std::vector<double>> bkgcov;
      Model_analysis_info empty_analysis_info;

      //
      // New analysis: CMS_13TeV_MONOJET_36invfb_interpolated
      //

      // Analysis name
      if (current_analysis_name == "CMS_13TeV_MONOJET_36invfb_interpolated")
      {
        current_ainfo->name = current_analysis_name;
        current_ainfo->lumi_invfb = 36.1;

        current_ainfo->obsnum = {136865, 74340, 42540, 25316, 15653, 10092, 8298, 4906, 2987, 2032, 1514,
                               926, 557, 316, 233, 172, 101, 65, 46, 26, 31, 29};
        current_ainfo->bkgnum = {134500., 73400., 42320., 25490., 15430., 10160., 8480., 4865., 2970., 1915., 1506.,
                               844., 526., 325., 223., 169., 107., 88.1, 52.8, 25.0, 25.5, 26.9};
        current_ainfo->bkgerr = {3700., 2000., 810., 490., 310., 170., 140., 95., 49., 33., 32.,
                               18., 14., 12., 9., 8., 6., 5.3, 3.9, 2.5, 2.6, 2.8};
        assert(current_ainfo->obsnum.size() == current_ainfo->bkgerr.size());
        assert(current_ainfo->obsnum.size() == current_ainfo->bkgerr.size());
        current_ainfo->n_signal_regions = current_ainfo->obsnum.size(); // = 22

        current_ainfo->extra_info["metmins"] = {250., 280., 310., 340., 370., 400., 430., 470., 510., 550., 590.,
                                              640., 690., 740., 790., 840., 900., 960., 1020., 1090., 1160., 1250.};
        assert(current_ainfo->obsnum.size() == current_ainfo->extra_info["metmins"].size());

        // Construct the background covariance matrix
        bkgcov = {
          {  1.37e+07,  7.18e+06,  2.58e+06,  1.54e+06,  9.29e+05,  4.28e+05,  3.26e+05,  2.04e+05,  8.34e+04,  5.37e+04,  4.62e+04,  2.33e+04,  1.45e+04,  1.20e+04,  6.66e+03,  7.99e+03,  4.00e+03,  1.57e+03,  0.00e+00,  1.30e+03,  3.85e+02, -4.14e+02 },
          {  7.18e+06,  4.00e+06,  1.38e+06,  8.43e+05,  5.02e+05,  2.28e+05,  1.74e+05,  1.05e+05,  4.51e+04,  2.84e+04,  2.30e+04,  1.22e+04,  7.56e+03,  6.48e+03,  3.24e+03,  4.00e+03,  2.28e+03,  1.06e+03,  1.56e+02,  8.00e+02,  3.64e+02, -1.68e+02 },
          {  2.58e+06,  1.38e+06,  6.56e+05,  3.57e+05,  2.18e+05,  1.07e+05,  8.73e+04,  5.31e+04,  2.34e+04,  1.50e+04,  1.35e+04,  7.00e+03,  4.20e+03,  3.30e+03,  2.26e+03,  1.81e+03,  1.12e+03,  6.44e+02,  2.21e+02,  3.04e+02,  1.47e+02,  2.27e+01 },
          {  1.54e+06,  8.43e+05,  3.57e+05,  2.40e+05,  1.32e+05,  6.58e+04,  5.14e+04,  3.17e+04,  1.44e+04,  9.22e+03,  8.15e+03,  4.06e+03,  2.88e+03,  2.00e+03,  1.32e+03,  1.25e+03,  7.06e+02,  3.64e+02,  5.73e+01,  1.59e+02,  7.64e+01, -2.74e+01 },
          {  9.29e+05,  5.02e+05,  2.18e+05,  1.32e+05,  9.61e+04,  4.11e+04,  3.21e+04,  1.88e+04,  8.81e+03,  5.73e+03,  5.46e+03,  2.57e+03,  1.78e+03,  1.34e+03,  6.98e+02,  9.18e+02,  4.28e+02,  1.64e+02,  3.63e+01,  1.32e+02,  1.05e+02, -8.68e+00 },
          {  4.28e+05,  2.28e+05,  1.07e+05,  6.58e+04,  4.11e+04,  2.89e+04,  1.76e+04,  1.07e+04,  5.16e+03,  2.92e+03,  2.83e+03,  1.62e+03,  9.76e+02,  8.77e+02,  3.82e+02,  4.49e+02,  2.04e+02,  1.08e+02,  9.94e+01,  1.02e+02,  3.98e+01,  4.76e+00 },
          {  3.26e+05,  1.74e+05,  8.73e+04,  5.14e+04,  3.21e+04,  1.76e+04,  1.96e+04,  9.18e+03,  4.39e+03,  2.82e+03,  2.46e+03,  1.39e+03,  9.21e+02,  7.39e+02,  5.17e+02,  3.70e+02,  2.35e+02,  9.65e+01,  8.19e+01,  4.20e+01,  1.82e+01,  3.14e+01 },
          {  2.04e+05,  1.04e+05,  5.31e+04,  3.17e+04,  1.88e+04,  1.07e+04,  9.18e+03,  9.02e+03,  2.61e+03,  1.72e+03,  1.70e+03,  8.55e+02,  4.52e+02,  4.67e+02,  2.48e+02,  2.66e+02,  1.54e+02,  5.04e+01,  3.33e+01,  1.19e+01,  3.21e+01,  7.98e+00 },
          {  8.34e+04,  4.51e+04,  2.34e+04,  1.44e+04,  8.81e+03,  5.16e+03,  4.39e+03,  2.61e+03,  2.40e+03,  9.22e+02,  8.94e+02,  4.67e+02,  2.13e+02,  2.41e+02,  1.41e+02,  1.29e+02,  4.70e+01,  4.41e+01,  7.64e+00,  2.08e+01,  2.55e+01,  5.49e+00 },
          {  5.37e+04,  2.84e+04,  1.50e+04,  9.22e+03,  5.73e+03,  2.92e+03,  2.82e+03,  1.72e+03,  9.22e+02,  1.09e+03,  5.17e+02,  3.03e+02,  1.62e+02,  1.47e+02,  8.91e+01,  8.18e+01,  3.17e+01,  2.10e+01,  1.29e+00,  7.42e+00,  7.72e+00,  4.62e+00 },
          {  4.62e+04,  2.30e+04,  1.35e+04,  8.15e+03,  5.46e+03,  2.83e+03,  2.46e+03,  1.70e+03,  8.94e+02,  5.17e+02,  1.02e+03,  2.65e+02,  1.57e+02,  1.61e+02,  9.22e+01,  7.94e+01,  3.84e+01,  3.39e+00, -1.25e+00,  1.44e+01,  3.33e+00, -8.96e-01 },
          {  2.33e+04,  1.22e+04,  7.00e+03,  4.06e+03,  2.57e+03,  1.62e+03,  1.39e+03,  8.55e+02,  4.67e+02,  3.03e+02,  2.65e+02,  3.24e+02,  8.57e+01,  9.07e+01,  5.83e+01,  3.02e+01,  2.70e+01,  2.00e+01,  7.02e+00,  2.25e+00,  5.15e+00,  7.06e+00 },
          {  1.45e+04,  7.56e+03,  4.20e+03,  2.88e+03,  1.78e+03,  9.76e+02,  9.21e+02,  4.52e+02,  2.13e+02,  1.62e+02,  1.57e+02,  8.57e+01,  1.96e+02,  5.21e+01,  3.91e+01,  3.92e+01,  2.69e+01,  8.90e+00,  6.55e+00,  0.00e+00,  1.46e+00,  1.57e+00 },
          {  1.20e+04,  6.48e+03,  3.30e+03,  2.00e+03,  1.34e+03,  8.77e+02,  7.39e+02,  4.67e+02,  2.41e+02,  1.47e+02,  1.61e+02,  9.07e+01,  5.21e+01,  1.44e+02,  3.02e+01,  2.02e+01,  1.44e+01,  3.18e+00,  4.68e-01,  4.50e+00,  2.18e+00,  3.02e+00 },
          {  6.66e+03,  3.24e+03,  2.26e+03,  1.32e+03,  6.98e+02,  3.82e+02,  5.17e+02,  2.48e+02,  1.41e+02,  8.91e+01,  9.22e+01,  5.83e+01,  3.91e+01,  3.02e+01,  8.10e+01,  1.15e+01,  1.19e+01,  7.63e+00,  3.16e+00, -2.25e-01,  1.40e+00,  2.52e+00 },
          {  7.99e+03,  4.00e+03,  1.81e+03,  1.25e+03,  9.18e+02,  4.49e+02,  3.70e+02,  2.66e+02,  1.29e+02,  8.18e+01,  7.94e+01,  3.02e+01,  3.92e+01,  2.02e+01,  1.15e+01,  6.40e+01,  1.92e+00, -1.27e+00, -3.12e-01,  1.40e+00,  2.70e+00, -6.72e-01 },
          {  4.00e+03,  2.28e+03,  1.12e+03,  7.06e+02,  4.28e+02,  2.04e+02,  2.35e+02,  1.54e+02,  4.70e+01,  3.17e+01,  3.84e+01,  2.70e+01,  2.69e+01,  1.44e+01,  1.19e+01,  1.92e+00,  3.60e+01,  5.09e+00,  3.74e+00, -1.65e+00,  1.40e+00,  1.51e+00 },
          {  1.57e+03,  1.06e+03,  6.44e+02,  3.64e+02,  1.64e+02,  1.08e+02,  9.65e+01,  5.04e+01,  4.41e+01,  2.10e+01,  3.39e+00,  2.00e+01,  8.90e+00,  3.18e+00,  7.63e+00, -1.27e+00,  5.09e+00,  2.81e+01,  6.20e-01, -1.19e+00,  5.51e-01, -4.45e-01 },
          {  0.00e+00,  1.56e+02,  2.21e+02,  5.73e+01,  3.63e+01,  9.95e+01,  8.19e+01,  3.33e+01,  7.64e+00,  1.29e+00, -1.25e+00,  7.02e+00,  6.55e+00,  4.68e-01,  3.16e+00, -3.12e-01,  3.74e+00,  6.20e-01,  1.52e+01,  7.80e-01,  3.04e-01,  1.64e+00 },
          {  1.30e+03,  8.00e+02,  3.04e+02,  1.59e+02,  1.32e+02,  1.02e+02,  4.20e+01,  1.19e+01,  2.08e+01,  7.42e+00,  1.44e+01,  2.25e+00,  0.00e+00,  4.50e+00, -2.25e-01,  1.40e+00, -1.65e+00, -1.19e+00,  7.80e-01,  6.25e+00,  1.30e-01,  6.30e-01 },
          {  3.85e+02,  3.64e+02,  1.47e+02,  7.64e+01,  1.05e+02,  3.98e+01,  1.82e+01,  3.21e+01,  2.55e+01,  7.72e+00,  3.33e+00,  5.15e+00,  1.46e+00,  2.18e+00,  1.40e+00,  2.70e+00,  1.40e+00,  5.51e-01,  3.04e-01,  1.30e-01,  6.76e+00,  5.82e-01 },
          { -4.14e+02, -1.68e+02,  2.27e+01, -2.74e+01, -8.68e+00,  4.76e+00,  3.14e+01,  7.98e+00,  5.49e+00,  4.62e+00, -8.96e-01,  7.06e+00,  1.57e+00,  3.02e+00,  2.52e+00, -6.72e-01,  1.51e+00, -4.45e-01,  1.64e+00,  6.30e-01,  5.82e-01,  7.84e+00 }
        };
        // Save it
        current_ainfo->add_bkgcov(bkgcov);

      }

      //
      // New analysis: ATLAS_13TeV_MONOJET_139invfb_interpolated
      //

      if (current_analysis_name == "ATLAS_13TeV_MONOJET_139invfb_interpolated")
      {
        // Create an entry in the global analysis_info_map and point the reference current_ainfo to it
        analysis_info_map[current_analysis_name] = Model_analysis_info();
        current_ainfo = &(analysis_info_map[current_analysis_name]);

        current_ainfo->name = current_analysis_name;
        current_ainfo->lumi_invfb = 139.0;

        current_ainfo->obsnum = {1791624, 752328, 313912, 141036, 102888, 29458, 10203, 3986, 1663, 738, 413+187+207};
        current_ainfo->bkgnum = {1783000., 753000., 314000., 140100., 101600., 29200., 10000., 3870., 1640., 754., 359.+182.+218.};
        current_ainfo->bkgerr = {26000., 9000., 3500., 1600., 1200., 400., 180., 80., 40., 20., sqrt(10*10+6*6+9*9)};
        assert(current_ainfo->obsnum.size() == current_ainfo->bkgnum.size());
        assert(current_ainfo->obsnum.size() == current_ainfo->bkgerr.size());
        current_ainfo->n_signal_regions = current_ainfo->obsnum.size();

        current_ainfo->extra_info["metmins"] = {200., 250., 300., 350., 400., 500., 600., 700., 800., 900., 1000.};
        assert(current_ainfo->obsnum.size() == current_ainfo->extra_info["metmins"].size());

      }

      //
      // New analysis: CMS_13TeV_MONOJET_137invfb_interpolated (https://www.hepdata.net/record/ins1894408)
      // Note: This analysis contains three copies of the same signal regions, with different luminosities.
      //       The appropriate scaling is applied to the values in the data file
      if (current_analysis_name == "CMS_13TeV_MONOJET_137invfb_interpolated")
      {

        current_ainfo->name = current_analysis_name;
        current_ainfo->lumi_invfb = 137.0;

        // Separate Bins
        current_ainfo->obsnum = {136865,74340,42540,25316,15653,10092,8298,4906,2987,2032,1514,926,557,316,233,172,101,65,46,26,31,29,
                                 176171,96067,54789,32767,20209,12910,10653,6487,3955,2587,1957,1151,721,455,298,244,146,89,65,39,35,40,
                                 191829,104522,59398,35833,21854,14266,11730,8639,5406,3285,2671,1613,965,640,424,319,191,117,96,55,43,70};

        // Separate Bins
        current_ainfo->bkgnum = {135004.8633,73681.17188,42448.17627,25541.23718,15454.10522,10162.67578,8473.070068,4853.264771,2960.103455,1906.687012,1498.361874,
          839.2151833,523.393774,322.8404999,221.0696697,167.221384,106.2168646,87.38325834,52.36919761,24.69706476,25.22828668,26.60783306,
          169737.7734,93266.63818,54175.54321,32232.16919,19798.24585,12816.66046,10626.91895,6407.873535,3903.657227,2519.861908,1929.788399,1181.808949,713.7919903,456.2266827,294.6278095,231.1669064,
          146.4085865,87.26129293,69.26482379,32.26833493,30.64801991,37.35177219,
          178470.1172,97428.42041,55592.1936,33037.12646,20714.72168,13209.00696,10991.22192,7836.975708,4914.64386,3065.690918,2428.390121,
          1441.82806,903.5198212,603.2915592,385.5468988,271.7485714,176.4562798,117.7774644,75.91881871,48.49774301,35.87580353,53.36183757};


        // bkgerr for the 2016 search is taken from above
        current_ainfo->bkgerr = {3514.65,1904.73,822.14,513.41,315.39,195.49,168.65,106.33,67.100,50.317,39.654,26.098,17.781,13.166,10.191,9.560,6.974,6.924,4.716,3.150,3.049,3.098,3706.95,1975.68,1117.22,
           665.78,413.29,266.21,217.70,133.23,84.55,58.43,45.84,30.83,21.29,16.28,11.86,10.18,7.442,5.391,4.733,3.230,3.124,3.328,
           3615.00,1896.81,1059.45,618.12,391.42,250.28,213.74,152.06,101.04,66.79,55.08,35.64,24.56,18.99,14.01,10.78,8.488,6.519,5.176,3.762,3.394,4.059};
        assert(current_ainfo->obsnum.size() == current_ainfo->bkgnum.size());
        assert(current_ainfo->obsnum.size() == current_ainfo->bkgerr.size());
        current_ainfo->n_signal_regions = current_ainfo->obsnum.size();

        // Construct the background covariance matrix
        bkgcov = {
          {12352763.4, 6458394.867, 2464750.837, 1514431.404, 898793.8461, 437646.4144, 377857.6261, 216898.8756, 100131.7426, 75505.18217, 52912.50268, 33250.16046, 17179.20302, 12365.09557, 6837.031881, 7266.816132, 3812.640002, 4303.669912, 1540.716589, 827.5964166, 1107.13207, 904.9881262, 220800.7392, 90163.48212, 39196.88759, 23744.97141, 17377.52317, 9370.330135, 2928.757998, 4452.51128, -1713.496482, 312.2226492, -55.25546233, 1572.924736, 554.1075651, 1118.481593, -490.7103398, -341.114241, -44.77498695, 340.8509019, -98.39530342, -110.1766936, 271.0935343, 143.5383758, 439879.5384, 212409.5503, 140493.1883, 71683.80747, 25941.15478, 22392.10864, 13040.61433, 23091.29594, 13214.87186, 5376.047223, 3014.408717, 3385.144538, 515.3964082, 1845.243786, -771.374651, 854.9087742, 42.18572303, 1221.267656, -109.8043719, 48.99872145, 170.272321, 117.5851365},
          {6458394.867, 3628011.061, 1345050.487, 835487.4572, 492787.8894, 242195.2283, 208353.813, 118037.7008, 54183.29573, 41388.68374, 29046.50256, 18213.67784, 9486.543104, 6853.968134, 3631.35278, 4004.9864, 2035.636967, 2361.107083, 774.4787659, 485.4568224, 575.3434007, 473.7366642, 188768.5861, 82573.25413, 37891.14143, 23042.60648, 13959.62261, 8039.516298, 5062.390974, 4817.675048, 266.8279891, 1418.126963, 819.0888956, 1395.416016, 426.8847773, 945.9130149, -107.7605714, -9.673390176, 85.77823834, 232.1420615, 28.40415796, 15.42017657, 159.6403163, 91.36649548, 335700.3183, 169229.7946, 107441.6449, 57530.29403, 26698.69573, 17782.28201, 13685.45039, 16128.60889, 9252.363235, 4169.789462, 3478.671821, 2021.603436, 676.9799044, 1353.390415, -120.2899834, 539.343198, 104.9900766, 625.1391541, -64.31825933, -43.88893136, 163.4437339, 122.3765556},
          {2464750.837, 1345050.487, 675913.8055, 373545.4376, 220670.2092, 123435.689, 106586.0664, 58981.10077, 32421.07086, 23213.31687, 16589.96668, 10021.7358, 5561.890987, 4074.856625, 2388.190089, 2141.263512, 1222.754637, 1252.898777, 511.556458, 337.9964554, 323.047423, 299.3891806, 75258.73468, 27341.94224, 8548.370667, 7903.418314, 6775.179879, 1887.929192, 1731.898853, 1738.565436, 46.95832966, 813.9137052, 374.0816464, 392.779846, 452.8522355, 453.1266133, -28.48157415, 95.6614313, -34.23435982, 184.005074, -33.8948519, -25.74723177, 97.31521789, 84.86874535, 175674.245, 87173.02776, 50481.56475, 26339.21394, 12045.20872, 6734.941483, 6064.149674, 6862.084602, 3608.620719, 1395.885561, 1634.757665, 1222.974196, 584.377065, 536.3161812, -60.42520352, 341.1989909, 5.229396464, 270.5109439, -13.96567868, 27.17719111, 92.34381722, 121.5203094},
          {1514431.404, 835487.4572, 373545.4376, 263593.7812, 135767.8059, 76245.13928, 64285.70028, 36377.63207, 18746.57512, 13686.62784, 10061.13682, 6177.970437, 3393.375334, 2270.116341, 1335.049222, 1241.955472, 674.5062549, 749.5407656, 311.6281862, 176.9060149, 201.1474819, 181.7392054, 48759.52569, 19609.30096, 6197.477438, 4987.251749, 5171.551265, 2180.823759, 1138.16555, 1551.345119, 56.19026175, 423.1872088, 277.2760848, 245.3466629, 329.0682335, 286.0337448, -66.77556012, 49.92928655, -5.050017867, 52.10379914, -18.92300432, -5.216034189, 49.40470295, 13.07226592, 105414.4449, 55470.72565, 33962.24805, 17081.49673, 7443.99313, 5096.214852, 3764.340482, 4481.180021, 2705.758775, 1068.625095, 989.3479815, 805.7784228, 418.215059, 396.9324511, 34.41434205, 139.1066363, 6.089127507, 163.7496422, -18.57722738, 31.15819231, 52.80129406, 31.44833382},
          {898793.8461, 492787.8894, 220670.2092, 135767.8059, 99471.41155, 45674.29195, 38946.60024, 22365.44799, 11770.08243, 8759.193202, 6268.02859, 3811.064218, 2148.816223, 1503.476782, 811.7630826, 766.1407399, 446.1000624, 433.2843491, 235.0100273, 102.9184611, 112.1584797, 112.699909, 35273.9197, 14446.45574, 6077.612266, 4460.394447, 4253.841117, 2487.536328, 2220.457855, 1806.261159, 379.6266776, 468.6956791, 265.5777412, 233.4245741, 323.5336059, 113.6689469, -5.421589384, 36.59827223, -31.50578412, 42.06143645, -5.226416318, -16.60638259, 36.14961422, 16.59234498, 67147.36232, 36137.99093, 21121.20986, 10913.812, 6462.338842, 3978.987721, 3394.607725, 3490.441441, 1576.546181, 978.956386, 887.0380432, 461.1765741, 261.4596744, 155.1823201, -7.789837987, 93.82329367, 13.95609686, 120.0262436, -8.177066978, 16.76327764, 13.79563254, 29.0441436},
          {437646.4144, 242195.2283, 123435.689, 76245.13928, 45674.29195, 38216.46482, 23799.53712, 13564.55176, 7775.854986, 5695.169789, 4164.61363, 2526.550304, 1422.598039, 1004.589001, 580.5833674, 497.8424079, 292.0478964, 293.2634033, 157.8323282, 70.16585618, 70.71390793, 66.37789476, 12725.18686, 5825.4754, 600.3875471, 2295.62498, 2122.485937, 1163.76366, 960.3069292, 912.3581558, 323.8670127, 463.9442777, 435.6409372, 233.9196654, 227.9938527, 158.0137548, -9.585901299, 23.45706535, -1.783457224, 48.05857253, 0.6050507381, -11.93276918, 20.59707581, 23.5249513, 43204.45743, 20528.90281, 12118.69637, 6266.756735, 3418.450314, 2314.581176, 2229.408924, 1944.236821, 1115.031676, 578.2503238, 633.9008334, 380.5594137, 146.7177549, 185.6326566, 52.39911793, 93.83097465, 0.03520313089, 57.30879948, 7.358016749, 13.26469595, -3.437616789, 16.15003463},
          {377857.6261, 208353.813, 106586.0664, 64285.70028, 38946.60024, 23799.53712, 28444.34259, 11873.67902, 6917.752943, 4860.535904, 3619.789982, 2228.669947, 1290.870452, 843.2657205, 525.3694244, 443.7693245, 264.0767719, 276.6482379, 132.4252724, 56.66178264, 67.19998879, 66.5158866, 22185.7645, 10270.55074, 3859.832927, 3185.024224, 3132.441119, 1576.199056, 1392.194225, 1106.618943, 535.745892, 330.1497183, 308.998604, 186.5546578, 184.3108069, 45.29993949, 13.67141325, 53.09483934, -25.06477303, 38.18427911, 6.274788503, 1.623739866, 17.37553626, 12.9439778, 22784.56755, 8650.103416, 6026.579068, 2546.919679, 1236.441353, 1168.703684, 1094.222557, 1098.594455, 839.3335347, 221.6730676, 284.265322, 210.8402636, 66.29162184, 121.1640057, 18.43744959, 35.46553893, -8.389749681, 35.05829587, 2.672881378, 5.996031102, 8.709688038, 5.728862796},
          {216898.8756, 118037.7008, 58981.10077, 36377.63207, 22365.44799, 13564.55176, 11873.67902, 11307.1171, 3973.268689, 2750.939902, 2211.011257, 1304.603254, 758.906037, 503.072805, 313.0413877, 263.0365487, 167.3292932, 164.4143988, 67.37621473, 26.3198512, 35.44135894, 45.92754496, 11619.90261, 4309.147121, 1816.706057, 1720.916621, 1510.932816, 1238.970198, 924.8735095, 747.1323, 299.1115322, 399.359235, 233.9983896, 156.9180928, 146.5867493, 89.42944837, 33.09241083, 49.33333435, -5.864139961, 11.52843107, 8.103515749, 13.46856767, 17.54201655, 5.354193652, 13228.99733, 5451.635083, 3623.563758, 1907.348106, 1056.932204, 1078.611848, 960.4193086, 846.6100139, 675.0725858, 305.6121785, 198.523863, 286.0286712, 117.1400376, 74.08202602, 54.03742088, 54.82382874, 29.73361249, 26.38351906, -0.3870342456, 7.022810006, 11.92216815, 12.26544884},
          {100131.7426, 54183.29573, 32421.07086, 18746.57512, 11770.08243, 7775.854986, 6917.752943, 3973.268689, 4501.955368, 1633.202839, 1266.293104, 787.9334912, 469.2471713, 317.6811086, 207.9541959, 178.5599039, 105.4845912, 95.27526745, 49.48523626, 24.64053897, 27.73073215, 28.28530428, 7317.482881, 3289.434551, 1124.149715, 1081.116556, 698.7830819, 624.6503975, 700.8891295, 322.5871873, 199.4202164, 223.3844065, 167.4957104, 74.41523267, 57.40949176, 49.84390313, 24.31252211, 27.15445165, 2.653156982, 6.432759823, -4.179494681, 5.110431555, 10.38425619, 8.932528143, 7517.04327, 3648.127181, 2472.273758, 781.6801036, 735.6566084, 568.772197, 709.3725401, 562.5941784, 364.8477749, 221.1375414, 218.2007778, 147.7393287, 120.8913437, 44.7087457, 29.07998106, 41.58661171, 13.43790445, 18.32728856, 4.706802307, 2.854391733, 5.748188247, 7.669678321},
          {75505.18217, 41388.68374, 23213.31687, 13686.62784, 8759.193202, 5695.169789, 4860.535904, 2750.939902, 1633.202839, 2531.791646, 939.6024473, 578.6050986, 354.6025168, 217.9238262, 131.8525824, 124.4783063, 66.72801014, 67.98518779, 37.47611024, 17.01918279, 16.89909414, 20.69370768, -1815.169897, -1478.176292, -1334.743816, -417.1761402, -74.61846138, 22.33263903, 150.9210869, 126.1114509, 42.63683323, 43.64540631, 29.68885656, 32.53390077, 36.45341204, 11.23189339, -2.479254203, 3.27838929, -5.899905526, 5.496684138, -0.9119386206, 4.509600507, 0.5700451657, 1.679388756, 4638.860958, 2842.816359, 1325.111473, 658.9291514, 556.3248917, 451.7383426, 379.8639373, 336.9884972, 220.4131638, 110.2855355, 75.51732727, 53.45270262, 43.44214845, 47.43582948, 9.117313402, 18.27100511, -13.54362095, 14.45339855, 3.93055022, -2.315761656, -2.348008619, 0.06123302462},
          {52912.50268, 29046.50256, 16589.96668, 10061.13682, 6268.02859, 4164.61363, 3619.789982, 2211.011257, 1266.293104, 939.6024473, 1572.430921, 432.2925292, 257.9189232, 183.6886756, 108.1477093, 84.83350805, 56.95453216, 52.47104933, 27.96099569, 13.30997093, 12.53836448, 15.84449184, 272.2711753, 314.3726507, -126.1999361, 370.2788131, 170.8350642, 230.8908339, 307.7153745, 227.6188766, 78.75609625, 118.6021506, 64.14300913, 55.29914562, 35.14660755, 12.00586455, -3.301776945, 21.30303157, -2.897585484, 9.347469458, -3.720658271, -0.4324677038, 3.24738392, 0.8879566884, 3770.255938, 1694.621607, 767.8563373, 506.0217101, 475.7697137, 263.7992199, 511.8357953, 420.3266971, 239.3821451, 156.4616244, 121.4719779, 98.54813902, 69.20279732, 50.06568056, 14.49095702, 5.01069122, 4.06584351, 4.05044551, 3.379636135, -1.83919345, 2.504156597, 1.389083341},
          {33250.16046, 18213.67784, 10021.7358, 6177.970437, 3811.064218, 2526.550304, 2228.669947, 1304.603254, 787.9334912, 578.6050986, 432.2925292, 681.0922928, 156.3841989, 107.287739, 64.1432745, 51.36795927, 32.37875406, 38.24573139, 14.28308049, 7.906113413, 10.79787154, 7.507435485, 1796.557537, 899.517532, 251.0080624, 353.5794149, 378.2814449, 237.101378, 268.0084839, 162.4618741, 76.01037729, 83.38167904, 65.81726935, 35.9795267, 33.8745905, 24.82739466, 7.079014116, 5.75868363, 2.406953721, 1.443132374, -0.7625438, 1.304062305, 3.671331377, 1.795839245, 4591.608469, 2187.772519, 1138.926563, 778.103376, 433.1645454, 344.0349982, 417.8134643, 272.3796914, 201.4634385, 80.17586408, 72.87281273, 79.63504018, 45.026084, 32.08928032, 15.44715518, 22.21533239, 3.360985369, 7.155638021, 4.953661443, -1.542108249, 1.558816544, 3.567380033},
          {17179.20302, 9486.543104, 5561.890987, 3393.375334, 2148.816223, 1422.598039, 1290.870452, 758.906037, 469.2471713, 354.6025168, 257.9189232, 156.3841989, 316.1810822, 57.47702812, 41.20667349, 33.42248358, 19.16557633, 19.36921393, 8.847467662, 6.154026479, 5.342310204, 5.767782386, 1022.96295, 286.3230051, 26.91692906, 141.2370259, 201.5998143, 126.6301037, 129.9508152, 120.9447317, 73.51115999, 65.79338903, 42.21259648, 37.36522255, 10.24308984, 11.02813414, 13.93816589, 4.176478031, -0.002569657956, 2.497446134, 0.1709024706, 1.285350695, 2.387290022, 1.704397239, 4420.708428, 2032.306623, 1371.55958, 610.4122463, 413.9643847, 314.3834246, 293.6790564, 197.5650024, 130.8500801, 83.678634, 61.71908078, 48.53103181, 30.33006804, 21.42948207, 7.930949259, 3.089259972, 3.00050516, 5.173357132, 1.626035293, 1.285221005, 2.857367965, 0.2259709354},
          {12365.09557, 6853.968134, 4074.856625, 2270.116341, 1503.476782, 1004.589001, 843.2657205, 503.072805, 317.6811086, 217.9238262, 183.6886756, 107.287739, 57.47702812, 173.3437785, 28.62478112, 24.21002819, 12.49765785, 11.62762055, 7.20330875, 3.717207753, 2.371063335, 3.55367105, -709.2560531, -107.5198636, -104.6994837, 65.57010173, 65.67038099, 36.97455607, 8.107464472, 68.47641775, -7.078920953, 27.14291355, 24.03345055, 11.79127599, 11.67397579, 1.21709443, 1.986591357, 7.305988896, -0.791413641, 1.341360241, 0.8578117519, 0.6923617832, 0.4640530312, 1.77801802, 3774.957411, 1862.681765, 1101.774103, 685.8827083, 405.8569798, 292.8199441, 237.0945028, 201.9642141, 128.9879113, 66.42014924, 70.37129948, 31.00717994, 31.4579487, 16.81184607, 10.62625506, 9.577750674, 3.955740843, 4.140031149, 4.843029012, 0.9948950473, 1.311938076, -0.180715315},
          {6837.031881, 3631.35278, 2388.190089, 1335.049222, 811.7630826, 580.5833674, 525.3694244, 313.0413877, 207.9541959, 131.8525824, 108.1477093, 64.1432745, 41.20667349, 28.62478112, 103.8492129, 13.84091037, 10.43204891, 9.522182671, 3.802863325, 3.511796046, 2.987108312, 3.188849338, 243.152003, 323.2732429, 131.1543894, 212.6251256, 169.1311418, 83.4865554, 71.8734051, 41.80320712, 42.37960686, 36.9741515, 20.15852029, 13.08943387, 7.22981033, 2.31861098, 3.336406655, 3.882416212, -0.4484249856, 2.553550481, 1.322076289, 0.05120324145, -0.4667193653, 0.04049499429, 1756.945839, 942.3021572, 442.7284225, 263.7392097, 132.927272, 148.4542433, 113.8805468, 87.98889594, 62.72218852, 35.98047254, 36.33208592, 23.13220286, 15.04611107, 7.713192988, 7.713254492, 3.316046089, 1.901480575, 1.861822896, 1.121858442, -0.741198561, 0.4660948576, 2.028979472},
          {7266.816132, 4004.9864, 2141.263512, 1241.955472, 766.1407399, 497.8424079, 443.7693245, 263.0365487, 178.5599039, 124.4783063, 84.83350805, 51.36795927, 33.42248358, 24.21002819, 13.84091037, 91.40154605, 6.449279266, 9.06960838, 3.507355316, 2.373575305, 2.003232621, 2.969078318, 765.6234137, 412.1139619, 232.6979179, 162.1294819, 119.0533052, 96.09383794, 81.76024944, 63.66889043, 39.56823288, 34.29893875, 20.17994357, 13.76438432, 16.00486051, 2.394260155, 3.165748388, 5.823151507, 1.638651131, 2.701544419, 0.8529080017, 1.274566069, 1.376763298, 0.8941155952, 532.3182882, 200.5655249, 123.3361608, 73.66079935, 43.09897062, 51.42054125, 48.50506364, 61.14835884, 25.34217929, 19.38106448, 19.4863284, 13.45897228, 14.33030689, 9.11910054, 7.739550918, 2.955139058, 0.1635705517, 2.467636942, 1.982110048, 0.06210888991, 0.983416606, -0.08603436246},
          {3812.640002, 2035.636967, 1222.754637, 674.5062549, 446.1000624, 292.0478964, 264.0767719, 167.3292932, 105.4845912, 66.72801014, 56.95453216, 32.37875406, 19.16557633, 12.49765785, 10.43204891, 6.449279266, 48.65143585, 4.402941628, 2.049840421, 1.552989288, 1.620253097, 1.223981729, -126.5262242, -95.11084266, -13.53867569, -27.6338571, 11.24894796, -0.1246173474, 37.25026693, 11.07868975, 8.142977967, 18.73822875, 3.357570558, 5.839008986, 5.051462389, 4.966994399, 2.190923316, 3.912522224, 0.2130799131, 0.05019531823, -0.002147562721, 0.37896781, 0.8473537315, 1.454026101, 405.6315825, 120.071825, 85.51077071, 40.0993913, 19.64217494, 33.26442306, 44.27443874, 28.35918932, 20.67498824, 2.074817923, 9.601811353, 2.310418748, 3.82321052, 3.820164345, 1.277247258, 3.096347798, 0.009957962764, 1.582505862, 1.052466759, 1.256114315, 0.5537127236, 0.8350097416},
          {4303.669912, 2361.107083, 1252.898777, 749.5407656, 433.2843491, 293.2634033, 276.6482379, 164.4143988, 95.27526745, 67.98518779, 52.47104933, 38.24573139, 19.36921393, 11.62762055, 9.522182671, 9.06960838, 4.402941628, 47.9349719, 2.019636691, 1.091356548, 1.47522231, 1.070968825, 1293.296492, 744.3715609, 394.5827013, 238.1887455, 168.5799728, 128.7865685, 84.54023765, 48.40231012, 38.60237825, 17.77180422, 21.13464962, 15.72987862, 9.316825188, 3.81252124, 3.171653837, 5.349999923, 0.2915379789, 2.192015984, 1.676395773, 1.106381378, 0.02695139897, 0.02399281625, 105.8591614, 122.4051285, 145.3429426, 126.618617, 54.14163627, 30.75732307, 52.09716233, 33.45773593, 31.22110784, 13.06888689, 13.70620037, 10.446059, 3.426537291, 4.180415353, 3.854442474, 3.172813137, 3.498189599, 1.911807707, 2.936060305, 1.03545886, 0.7150422923, 0.6092942172},
          {1540.716589, 774.4787659, 511.556458, 311.6281862, 235.0100273, 157.8323282, 132.4252724, 67.37621473, 49.48523626, 37.47611024, 27.96099569, 14.28308049, 8.847467662, 7.20330875, 3.802863325, 3.507355316, 2.049840421, 2.019636691, 22.240881, 0.7514875288, 0.4827164677, 0.6401523356, 103.2422031, 98.4023148, 52.67326425, 62.0616055, 56.56626002, 17.71408, 38.7525153, 14.31692352, 12.91641868, 9.721573038, 9.322033186, 8.333771168, 1.980373662, 0.8788104283, 1.404148919, 1.76398992, -0.6461679126, -0.3324815042, 0.6764996966, 0.08082465835, -0.2453738843, 0.2828676017, 1000.662193, 469.1050591, 311.900704, 155.7057978, 83.85351102, 71.04295878, 66.8937023, 39.84776895, 27.16745833, 16.49151705, 15.39235992, 8.519301865, 6.051266134, 4.988161228, 3.528527715, 1.903779425, 0.6153935733, 1.877563742, 0.4088185021, 0.5173346697, 0.5368543574, 0.7303244815},
          {827.5964166, 485.4568224, 337.9964554, 176.9060149, 102.9184611, 70.16585618, 56.66178264, 26.3198512, 24.64053897, 17.01918279, 13.30997093, 7.906113413, 6.154026479, 3.717207753, 3.511796046, 2.373575305, 1.552989288, 1.091356548, 0.7514875288, 9.923062967, 0.391394724, 0.4531678137, 130.5636116, 43.89302343, 2.306488298, 16.90701428, 12.93168197, 17.48449093, 11.77069247, 3.746314996, 9.871706432, 4.343128353, 6.004645164, 2.664340914, 1.702121753, 0.607518321, 1.846196822, 0.9397388285, 0.5988512006, 0.8139089333, 0.01815952339, 0.3033896259, 0.1770417719, 0.9142236231, 124.0944129, 8.875214213, 7.070590128, 12.76007031, 6.238652243, 6.581337044, 9.578844737, 7.568565905, 1.525667919, 4.038243073, 1.303084703, 2.968339843, 1.051746696, 1.282396429, 0.6345819547, 1.464847513, 0.5733386592, 0.08291818562, 0.767571954, -0.1591799049, -0.009546834946, -0.2772611512},
          {1107.13207, 575.3434007, 323.047423, 201.1474819, 112.1584797, 70.71390793, 67.19998879, 35.44135894, 27.73073215, 16.89909414, 12.53836448, 10.79787154, 5.342310204, 2.371063335, 2.987108312, 2.003232621, 1.620253097, 1.47522231, 0.4827164677, 0.391394724, 9.293727856, 0.1916185721, 17.11379841, 101.3824864, 36.90959918, 28.47470821, 37.18036715, 18.91471913, 16.59328546, 10.92782946, 7.821439598, 7.127071009, 3.430265774, 4.358015167, 3.668541644, 0.5011753578, 0.7256668776, 0.9994144473, 0.5780591403, 0.5806569536, 0.2665871165, 0.5275990747, 0.3393929753, 0.2265699315, 137.6122665, 140.8950062, 60.95622324, 12.42313264, 28.00952165, 15.13838374, 11.91513304, 14.72316219, 7.660580391, 6.07460927, 5.029116416, 3.750303389, 3.314792871, 1.20778476, 0.510200417, 0.4039354771, 0.4962106256, 0.3859618064, -0.17741699, 0.3387056982, 0.6301101696, 0.1156510186},
          {904.9881262, 473.7366642, 299.3891806, 181.7392054, 112.699909, 66.37789476, 66.5158866, 45.92754496, 28.28530428, 20.69370768, 15.84449184, 7.507435485, 5.767782386, 3.55367105, 3.188849338, 2.969078318, 1.223981729, 1.070968825, 0.6401523356, 0.4531678137, 0.1916185721, 9.599124485, -132.1214789, -78.67863043, -61.15481896, -35.23909319, -17.4451641, -4.80883633, 6.679122464, 1.837493261, 6.052315594, 2.483936103, 6.32590812, 0.5172994157, 0.9842477955, 0.7272427451, 0.3542879228, 1.296311952, 1.073341831, -0.2319373646, 0.2051247745, 0.1063766275, 0.09812925307, 0.188688236, 391.2335323, 213.0906671, 100.2131191, 49.13269736, 50.42296256, 23.22575228, 14.44235204, 17.82102145, 11.32504025, 7.703241575, 7.019966788, 3.11842956, 3.215945241, 0.9202517217, 2.50362071, 1.19344087, -0.01334545332, 1.2008844, 0.7502604484, -0.05711961391, 0.07833836911, -0.2716696238},
          {220800.7392, 188768.5861, 75258.73468, 48759.52569, 35273.9197, 12725.18686, 22185.7645, 11619.90261, 7317.482881, -1815.169897, 272.2711753, 1796.557537, 1022.96295, -709.2560531, 243.152003, 765.6234137, -126.5262242, 1293.296492, 103.2422031, 130.5636116, 17.11379841, -132.1214789, 13741508.2, 7012223.046, 3902117.032, 2308842.958, 1408829.597, 874089.6562, 704949.5194, 415359.6263, 248470.0644, 159372.9975, 119602.5378, 72252.70315, 42582.11866, 30055.4765, 17531.50336, 14540.73526, 8152.660018, 5001.517144, 4227.385332, 1829.349357, 2159.071161, 1758.978544, 1132856.475, 608567.5879, 354372.6254, 213328.332, 137671.231, 88341.58863, 63321.87793, 47700.17404, 38096.64761, 17894.00271, 17463.84546, 6201.535517, 4524.820085, 2690.050236, 1974.931117, 2127.432351, 84.88679246, 664.350596, 274.6944656, 632.2702019, 219.4002956, 214.621503},
          {90163.48212, 82573.25413, 27341.94224, 19609.30096, 14446.45574, 5825.4754, 10270.55074, 4309.147121, 3289.434551, -1478.176292, 314.3726507, 899.517532, 286.3230051, -107.5198636, 323.2732429, 412.1139619, -95.11084266, 744.3715609, 98.4023148, 43.89302343, 101.3824864, -78.67863043, 7012223.046, 3903321.442, 2114781.989, 1254085.886, 764833.9244, 474415.4289, 382263.6752, 223859.1872, 134630.5039, 86271.87792, 64434.20229, 39011.32241, 22826.66525, 16315.82334, 9214.317626, 7913.501982, 4474.489635, 2648.534742, 2274.902354, 949.2329982, 1221.755619, 888.8075873, 676248.303, 360990.2259, 211909.7133, 130193.9925, 81031.42464, 51150.09722, 36945.59585, 26564.6108, 21729.60443, 10343.24292, 10389.8681, 3997.119639, 3144.78249, 2029.613258, 1472.341755, 1329.860516, -5.05143028, 468.303197, 154.3800703, 324.2727354, 154.4921703, 101.7214878},
          {39196.88759, 37891.14143, 8548.370667, 6197.477438, 6077.612266, 600.3875471, 3859.832927, 1816.706057, 1124.149715, -1334.743816, -126.1999361, 251.0080624, 26.91692906, -104.6994837, 131.1543894, 232.6979179, -13.53867569, 394.5827013, 52.67326425, 2.306488298, 36.90959918, -61.15481896, 3902117.032, 2114781.989, 1248180.63, 707257.3508, 430898.6232, 268957.1689, 217296.0043, 127400.667, 76798.67851, 49134.07446, 36727.07709, 22169.26647, 12986.23918, 9262.212594, 5373.890201, 4503.531999, 2611.365967, 1475.05644, 1333.790167, 561.3011847, 719.1579473, 504.329726, 391501.0402, 211216.0138, 126887.4795, 78013.37639, 49465.38025, 31611.4467, 23452.6411, 16635.56708, 13064.65145, 6860.925358, 6695.225105, 2410.484769, 1808.077288, 1251.893203, 1057.248137, 748.0219207, 123.2452762, 286.0610777, 109.4186277, 211.3865361, 115.0045901, 139.5553672},
          {23744.97141, 23042.60648, 7903.418314, 4987.251749, 4460.394447, 2295.62498, 3185.024224, 1720.916621, 1081.116556, -417.1761402, 370.2788131, 353.5794149, 141.2370259, 65.57010173, 212.6251256, 162.1294819, -27.6338571, 238.1887455, 62.0616055, 16.90701428, 28.47470821, -35.23909319, 2308842.958, 1254085.886, 707257.3508, 443265.6074, 258636.2213, 161420.5055, 130563.812, 76764.6285, 46387.39428, 29618.53684, 22407.75214, 13548.62421, 7941.244175, 5557.267731, 3211.298519, 2726.701537, 1566.152677, 903.3613537, 789.6744439, 350.7806833, 443.5222154, 332.9996805, 279402.1411, 152720.2627, 89773.82779, 56672.71362, 35821.53321, 22989.4366, 17529.82375, 12671.00706, 9770.98086, 5246.542826, 4783.054164, 2128.164575, 1525.064566, 1022.117638, 719.4741045, 535.9137258, 166.1119091, 214.9911891, 113.0549879, 130.3843451, 82.82925647, 84.72970069},
          {17377.52317, 13959.62261, 6775.179879, 5171.551265, 4253.841117, 2122.485937, 3132.441119, 1510.932816, 698.7830819, -74.61846138, 170.8350642, 378.2814449, 201.5998143, 65.67038099, 169.1311418, 119.0533052, 11.24894796, 168.5799728, 56.56626002, 12.93168197, 37.18036715, -17.4451641, 1408829.597, 764833.9244, 430898.6232, 258636.2213, 170808.9639, 99558.82503, 80329.95102, 47503.17615, 28800.10718, 18605.82403, 13844.64794, 8524.777511, 5002.121205, 3495.42256, 2049.283558, 1753.65689, 978.7823237, 571.5128878, 490.6321031, 229.2283591, 282.1459775, 215.6898836, 162451.6285, 88427.61006, 54021.34122, 33952.78362, 20826.38435, 13591.90364, 10524.10688, 7644.636058, 5950.299707, 3123.286168, 2966.683785, 1195.523775, 975.2564298, 642.7618997, 444.5610749, 337.1096338, 77.41811558, 151.1200338, 94.08456488, 86.79120967, 53.85764508, 51.41789208},
          {9370.330135, 8039.516298, 1887.929192, 2180.823759, 2487.536328, 1163.76366, 1576.199056, 1238.970198, 624.6503975, 22.33263903, 230.8908339, 237.101378, 126.6301037, 36.97455607, 83.4865554, 96.09383794, -0.1246173474, 128.7865685, 17.71408, 17.48449093, 18.91471913, -4.80883633, 874089.6562, 474415.4289, 268957.1689, 161420.5055, 99558.82503, 70869.32595, 51710.47035, 30695.60401, 18716.66812, 12115.59049, 9065.352955, 5528.485718, 3311.930374, 2326.897438, 1415.086393, 1191.03104, 675.0994919, 386.987261, 350.9191229, 151.877866, 175.0465421, 141.3675108, 121714.1005, 65255.07293, 39796.34341, 24944.54094, 15584.0728, 10767.35236, 8322.700055, 6095.781014, 4533.677425, 2540.031699, 2253.712285, 1165.946379, 780.2510863, 584.1501517, 360.5361192, 259.045005, 120.3837089, 111.302063, 63.01379939, 69.82736327, 46.41074454, 49.88946879},
          {2928.757998, 5062.390974, 1731.898853, 1138.16555, 2220.457855, 960.3069292, 1392.194225, 924.8735095, 700.8891295, 150.9210869, 307.7153745, 268.0084839, 129.9508152, 8.107464472, 71.8734051, 81.76024944, 37.25026693, 84.54023765, 38.7525153, 11.77069247, 16.59328546, 6.679122464, 704949.5194, 382263.6752, 217296.0043, 130563.812, 80329.95102, 51710.47035, 47392.4364, 25151.32166, 15394.30577, 9894.812837, 7565.653393, 4588.396092, 2704.013263, 1922.915319, 1132.862457, 980.3173537, 574.3032908, 329.360209, 308.7530513, 131.2975385, 169.4081569, 135.6704998, 97750.44841, 52692.34184, 31151.35581, 20099.82296, 12411.91254, 8414.69074, 6673.308656, 4831.543001, 3780.355269, 2009.503624, 1765.985239, 863.6890407, 647.994207, 463.2067122, 294.7884287, 207.8735991, 100.4304055, 96.30574094, 59.18092734, 51.04241568, 35.79549611, 37.89944522},
          {4452.51128, 4817.675048, 1738.565436, 1551.345119, 1806.261159, 912.3581558, 1106.618943, 747.1323, 322.5871873, 126.1114509, 227.6188766, 162.4618741, 120.9447317, 68.47641775, 41.80320712, 63.66889043, 11.07868975, 48.40231012, 14.31692352, 3.746314996, 10.92782946, 1.837493261, 415359.6263, 223859.1872, 127400.667, 76764.6285, 47503.17615, 30695.60401, 25151.32166, 17750.50073, 9137.011358, 5959.482506, 4525.740298, 2848.495334, 1682.3361, 1156.36593, 725.7272215, 606.4024615, 358.9966913, 199.32844, 189.3192503, 88.44015359, 93.75833774, 89.10844942, 71171.87209, 38905.8754, 22367.27401, 14216.79433, 9113.189265, 6101.629587, 4861.789986, 3551.248301, 2616.672123, 1615.451391, 1331.943406, 679.2280663, 438.141051, 344.9663155, 213.124425, 156.1537639, 64.71010442, 67.41045006, 39.2949112, 48.71391345, 28.04003385, 33.34021439},
          {-1713.496482, 266.8279891, 46.95832966, 56.19026175, 379.6266776, 323.8670127, 535.745892, 299.1115322, 199.4202164, 42.63683323, 78.75609625, 76.01037729, 73.51115999, -7.078920953, 42.37960686, 39.56823288, 8.142977967, 38.60237825, 12.91641868, 9.871706432, 7.821439598, 6.052315594, 248470.0644, 134630.5039, 76798.67851, 46387.39428, 28800.10718, 18716.66812, 15394.30577, 9137.011358, 7148.268428, 3665.617444, 2780.165583, 1744.32124, 1013.637583, 721.2213448, 446.7626651, 378.1159009, 226.7100753, 130.8505844, 111.970125, 60.41995556, 63.59328337, 55.5998438, 45005.3444, 24875.94908, 14918.5289, 9176.160541, 5628.34674, 3888.809142, 3092.937738, 2260.972309, 1729.379269, 1028.101881, 846.8168757, 462.0007865, 280.1338058, 202.2078365, 137.590184, 92.68478178, 64.25409672, 58.61786884, 30.60790534, 28.18834446, 12.62521308, 21.79605349},
          {312.2226492, 1418.126963, 813.9137052, 423.1872088, 468.6956791, 463.9442777, 330.1497183, 399.359235, 223.3844065, 43.64540631, 118.6021506, 83.38167904, 65.79338903, 27.14291355, 36.9741515, 34.29893875, 18.73822875, 17.77180422, 9.721573038, 4.343128353, 7.127071009, 2.483936103, 159372.9975, 86271.87792, 49134.07446, 29618.53684, 18605.82403, 12115.59049, 9894.812837, 5959.482506, 3665.617444, 3414.214477, 1832.376344, 1141.183631, 713.2262489, 506.7710051, 301.2067518, 254.2222569, 144.9406298, 90.42549315, 79.44650037, 37.52792071, 40.70922441, 42.73268308, 23839.38869, 12958.71511, 7975.54845, 4853.740125, 2921.547394, 2030.118905, 1767.113434, 1356.925002, 1030.127145, 574.3729678, 525.3935678, 255.5444911, 193.710283, 141.7685742, 79.77576307, 55.54210024, 30.52115095, 31.24719873, 20.72684777, 11.44080524, 12.82616962, 11.59843484},
          {-55.25546233, 819.0888956, 374.0816464, 277.2760848, 265.5777412, 435.6409372, 308.998604, 233.9983896, 167.4957104, 29.68885656, 64.14300913, 65.81726935, 42.21259648, 24.03345055, 20.15852029, 20.17994357, 3.357570558, 21.13464962, 9.322033186, 6.004645164, 3.430265774, 6.32590812, 119602.5378, 64434.20229, 36727.07709, 22407.75214, 13844.64794, 9065.352955, 7565.653393, 4525.740298, 2780.165583, 1832.376344, 2100.886384, 868.92357, 524.5804354, 369.9284564, 234.070981, 199.6514037, 124.432658, 73.15225662, 64.99263203, 31.36470469, 33.92441178, 33.42257481, 20645.59276, 11203.23855, 6291.509763, 4345.41277, 2641.109945, 1753.99741, 1460.19678, 1135.974762, 853.2519754, 528.7678796, 458.9496027, 235.9779417, 154.2519009, 116.3772074, 84.11835505, 51.44290032, 25.97914017, 33.41725764, 18.75065737, 13.99799139, 5.878579041, 7.77105568},
          {1572.924736, 1395.416016, 392.779846, 245.3466629, 233.4245741, 233.9196654, 186.5546578, 156.9180928, 74.41523267, 32.53390077, 55.29914562, 35.9795267, 37.36522255, 11.79127599, 13.08943387, 13.76438432, 5.839008986, 15.72987862, 8.333771168, 2.664340914, 4.358015167, 0.5172994157, 72252.70315, 39011.32241, 22169.26647, 13548.62421, 8524.777511, 5528.485718, 4588.396092, 2848.495334, 1744.32124, 1141.183631, 868.92357, 950.4306049, 330.7015313, 244.9022231, 156.5168087, 125.4401893, 75.81489373, 41.24993662, 40.44954808, 18.9570625, 19.30510467, 24.87866468, 15168.57939, 8707.653092, 4617.198292, 3114.571437, 1984.991136, 1305.915995, 1128.352722, 822.2973192, 624.2720873, 378.1384698, 301.1511794, 175.578183, 123.4669238, 97.35461516, 57.45943384, 47.07659869, 26.26568033, 14.7779272, 13.5216477, 11.08617417, 11.10508486, 6.694244522},
          {554.1075651, 426.8847773, 452.8522355, 329.0682335, 323.5336059, 227.9938527, 184.3108069, 146.5867493, 57.40949176, 36.45341204, 35.14660755, 33.8745905, 10.24308984, 11.67397579, 7.22981033, 16.00486051, 5.051462389, 9.316825188, 1.980373662, 1.702121753, 3.668541644, 0.9842477955, 42582.11866, 22826.66525, 12986.23918, 7941.244175, 5002.121205, 3311.930374, 2704.013263, 1682.3361, 1013.637583, 713.2262489, 524.5804354, 330.7015313, 453.3186408, 151.5331001, 91.75025446, 86.43288743, 45.51660107, 27.58022039, 26.80096606, 13.89720568, 13.97545664, 14.70927928, 8670.818681, 4895.653757, 3124.931972, 1793.191782, 1166.679523, 808.5123542, 676.2640872, 492.3104345, 362.669919, 213.7291036, 183.9427721, 106.0064952, 74.9532595, 44.69384116, 32.61474729, 27.58811426, 11.09541129, 13.29427249, 7.661442577, 5.769851361, 4.000549434, 6.164922142},
          {1118.481593, 945.9130149, 453.1266133, 286.0337448, 113.6689469, 158.0137548, 45.29993949, 89.42944837, 49.84390313, 11.23189339, 12.00586455, 24.82739466, 11.02813414, 1.21709443, 2.31861098, 2.394260155, 4.966994399, 3.81252124, 0.8788104283, 0.607518321, 0.5011753578, 0.7272427451, 30055.4765, 16315.82334, 9262.212594, 5557.267731, 3495.42256, 2326.897438, 1922.915319, 1156.36593, 721.2213448, 506.7710051, 369.9284564, 244.9022231, 151.5331001, 265.1841098, 68.71319389, 58.45474144, 33.18123679, 18.19369065, 19.65608631, 10.28582852, 9.794761199, 12.22601621, 3978.706517, 2273.260147, 1433.07944, 900.2015586, 570.7074348, 418.5728182, 362.0041639, 258.1690813, 191.9100106, 123.4169245, 118.3557501, 59.84236898, 44.41689534, 36.30446186, 18.85918474, 16.23302811, 10.80622084, 7.646017996, 3.351135756, 4.693133551, 2.808877, 3.354545952},
          {-490.7103398, -107.7605714, -28.48157415, -66.77556012, -5.421589384, -9.585901299, 13.67141325, 33.09241083, 24.31252211, -2.479254203, -3.301776945, 7.079014116, 13.93816589, 1.986591357, 3.336406655, 3.165748388, 2.190923316, 3.171653837, 1.404148919, 1.846196822, 0.7256668776, 0.3542879228, 17531.50336, 9214.317626, 5373.890201, 3211.298519, 2049.283558, 1415.086393, 1132.862457, 725.7272215, 446.7626651, 301.2067518, 234.070981, 156.5168087, 91.75025446, 68.71319389, 140.703159, 38.2715098, 21.00711625, 13.92655135, 11.8785427, 6.079855896, 6.507971966, 7.776334873, 2414.393039, 1145.774338, 799.2200889, 548.0100049, 347.2145007, 270.358556, 249.6313904, 169.7000392, 137.1420288, 84.62698106, 78.1750648, 46.54610994, 25.80679766, 22.33297677, 16.75533083, 10.81749608, 5.230435391, 6.339176093, 5.922879713, 3.091934222, 2.711142456, 1.509979773},
          {-341.114241, -9.673390176, 95.6614313, 49.92928655, 36.59827223, 23.45706535, 53.09483934, 49.33333435, 27.15445165, 3.27838929, 21.30303157, 5.75868363, 4.176478031, 7.305988896, 3.882416212, 5.823151507, 3.912522224, 5.349999923, 1.76398992, 0.9397388285, 0.9994144473, 1.296311952, 14540.73526, 7913.501982, 4503.531999, 2726.701537, 1753.65689, 1191.03104, 980.3173537, 606.4024615, 378.1159009, 254.2222569, 199.6514037, 125.4401893, 86.43288743, 58.45474144, 38.2715098, 103.7047876, 18.18087709, 11.67990015, 10.75183274, 5.26503906, 5.210259693, 5.592998528, 3015.040718, 1730.607605, 1045.121419, 708.9569729, 437.8353405, 291.7270262, 235.7402893, 200.7212296, 145.5098673, 84.92723147, 85.93813346, 46.71300464, 29.46775284, 18.40995781, 21.69005382, 11.71465546, 6.730322444, 7.323570289, 4.222823501, 2.566968535, 2.565665635, 2.152127477},
          {-44.77498695, 85.77823834, -34.23435982, -5.050017867, -31.50578412, -1.783457224, -25.06477303, -5.864139961, 2.653156982, -5.899905526, -2.897585484, 2.406953721, -0.002569657956, -0.791413641, -0.4484249856, 1.638651131, 0.2130799131, 0.2915379789, -0.6461679126, 0.5988512006, 0.5780591403, 1.073341831, 8152.660018, 4474.489635, 2611.365967, 1566.152677, 978.7823237, 675.0994919, 574.3032908, 358.9966913, 226.7100753, 144.9406298, 124.432658, 75.81489373, 45.51660107, 33.18123679, 21.00711625, 18.18087709, 55.38426869, 8.115016982, 5.999492024, 3.273877406, 3.324706632, 4.208712844, 1487.698916, 948.4676883, 525.4359042, 358.4657446, 233.3697081, 165.1242111, 114.0976934, 111.0490032, 78.45600588, 43.0333708, 41.43684891, 27.38324379, 12.937434, 12.07038826, 10.45555434, 6.239035846, 2.678568331, 3.560621146, 2.179624126, 0.7047812374, 1.421513518, 1.807389874},
          {340.8509019, 232.1420615, 184.005074, 52.10379914, 42.06143645, 48.05857253, 38.18427911, 11.52843107, 6.432759823, 5.496684138, 9.347469458, 1.443132374, 2.497446134, 1.341360241, 2.553550481, 2.701544419, 0.05019531823, 2.192015984, -0.3324815042, 0.8139089333, 0.5806569536, -0.2319373646, 5001.517144, 2648.534742, 1475.05644, 903.3613537, 571.5128878, 386.987261, 329.360209, 199.32844, 130.8505844, 90.42549315, 73.15225662, 41.24993662, 27.58022039, 18.19369065, 13.92655135, 11.67990015, 8.115016982, 29.06521702, 2.981973617, 1.855235323, 1.473269585, 2.057044544, 904.2218444, 553.2617508, 253.1373132, 209.4042208, 128.4411207, 67.30457073, 49.33820706, 44.95279224, 33.58954574, 24.22053787, 24.51864679, 10.95657929, 9.390089979, 10.54758738, 3.401878395, 1.85984143, 2.314225051, 2.531055186, 1.615105526, 0.864532486, 0.3440013996, 1.094438063},
          {-98.39530342, 28.40415796, -33.8948519, -18.92300432, -5.226416318, 0.6050507381, 6.274788503, 8.103515749, -4.179494681, -0.9119386206, -3.720658271, -0.7625438, 0.1709024706, 0.8578117519, 1.322076289, 0.8529080017, -0.002147562721, 1.676395773, 0.6764996966, 0.01815952339, 0.2665871165, 0.2051247745, 4227.385332, 2274.902354, 1333.790167, 789.6744439, 490.6321031, 350.9191229, 308.7530513, 189.3192503, 111.970125, 79.44650037, 64.99263203, 40.44954808, 26.80096606, 19.65608631, 11.8785427, 10.75183274, 5.999492024, 2.981973617, 22.40109464, 2.138134058, 1.873549355, 2.212005539, 756.5854664, 391.6912758, 258.3868781, 159.3761116, 103.8126493, 70.56892497, 38.84953011, 51.4280712, 38.87657698, 25.55317404, 22.5250282, 11.62664697, 8.968896332, 5.579953064, 2.940726008, 2.147763504, 1.575942771, 1.847233145, 1.488189324, 1.130175294, 0.4240060426, 0.6168076243},
          {-110.1766936, 15.42017657, -25.74723177, -5.216034189, -16.60638259, -11.93276918, 1.623739866, 13.46856767, 5.110431555, 4.509600507, -0.4324677038, 1.304062305, 1.285350695, 0.6923617832, 0.05120324145, 1.274566069, 0.37896781, 1.106381378, 0.08082465835, 0.3033896259, 0.5275990747, 0.1063766275, 1829.349357, 949.2329982, 561.3011847, 350.7806833, 229.2283591, 151.877866, 131.2975385, 88.44015359, 60.41995556, 37.52792071, 31.36470469, 18.9570625, 13.89720568, 10.28582852, 6.079855896, 5.26503906, 3.273877406, 1.855235323, 2.138134058, 10.43298022, 1.0583084, 1.481560072, 523.183154, 261.9256744, 169.3397574, 106.7210782, 66.27286913, 49.47903716, 52.51830036, 32.32105351, 21.0421396, 11.82980521, 13.86533471, 11.50456679, 5.185018197, 3.903525914, 3.390063831, 2.912484378, 2.116121733, 0.6326565304, 1.0759214, 0.6429168884, 0.3664242547, 0.3919385763},
          {271.0935343, 159.6403163, 97.31521789, 49.40470295, 36.14961422, 20.59707581, 17.37553626, 17.54201655, 10.38425619, 0.5700451657, 3.24738392, 3.671331377, 2.387290022, 0.4640530312, -0.4667193653, 1.376763298, 0.8473537315, 0.02695139897, -0.2453738843, 0.1770417719, 0.3393929753, 0.09812925307, 2159.071161, 1221.755619, 719.1579473, 443.5222154, 282.1459775, 175.0465421, 169.4081569, 93.75833774, 63.59328337, 40.70922441, 33.92441178, 19.30510467, 13.97545664, 9.794761199, 6.507971966, 5.210259693, 3.324706632, 1.473269585, 1.873549355, 1.0583084, 9.760258251, 1.56092307, 347.9616255, 146.3479761, 104.9963204, 64.6305252, 36.23304992, 24.12165481, 20.68676758, 20.01939526, 20.42349344, 10.04246237, 4.496355517, 5.409193358, 2.545637114, 3.27176308, 0.899951682, 0.9334531642, 1.680418418, 0.9547321489, 0.8017114449, 0.7050590906, 0.4215447344, 0.4295759504},
          {143.5383758, 91.36649548, 84.86874535, 13.07226592, 16.59234498, 23.5249513, 12.9439778, 5.354193652, 8.932528143, 1.679388756, 0.8879566884, 1.795839245, 1.704397239, 1.77801802, 0.04049499429, 0.8941155952, 1.454026101, 0.02399281625, 0.2828676017, 0.9142236231, 0.2265699315, 0.188688236, 1758.978544, 888.8075873, 504.329726, 332.9996805, 215.6898836, 141.3675108, 135.6704998, 89.10844942, 55.5998438, 42.73268308, 33.42257481, 24.87866468, 14.70927928, 12.22601621, 7.776334873, 5.592998528, 4.208712844, 2.057044544, 2.212005539, 1.481560072, 1.56092307, 11.07431694, 723.2710899, 401.2934068, 269.3045929, 137.8188581, 101.303505, 66.35069405, 54.49627804, 44.4664588, 28.70265533, 23.68079454, 23.0240654, 8.107287289, 7.31333113, 5.448854143, 4.693040056, 3.240082301, 1.871857431, 1.204852812, 1.382081627, 0.5568566802, 0.9874023752, 0.1907629104},
          {439879.5384, 335700.3183, 175674.245, 105414.4449, 67147.36232, 43204.45743, 22784.56755, 13228.99733, 7517.04327, 4638.860958, 3770.255938, 4591.608469, 4420.708428, 3774.957411, 1756.945839, 532.3182882, 405.6315825, 105.8591614, 1000.662193, 124.0944129, 137.6122665, 391.2335323, 1132856.475, 676248.303, 391501.0402, 279402.1411, 162451.6285, 121714.1005, 97750.44841, 71171.87209, 45005.3444, 23839.38869, 20645.59276, 15168.57939, 8670.818681, 3978.706517, 2414.393039, 3015.040718, 1487.698916, 904.2218444, 756.5854664, 523.183154, 347.9616255, 723.2710899, 13068191.37, 6551879.44, 3595432.986, 2062331.57, 1290054.367, 791719.1241, 653095.147, 460077.5227, 291025.9392, 178390.7263, 144968.4266, 83314.5584, 52907.0255, 37892.02254, 24086.46938, 16802.46159, 9926.319489, 5571.398529, 4211.809437, 2469.630688, 2312.805086, 3518.762797},
          {212409.5503, 169229.7946, 87173.02776, 55470.72565, 36137.99093, 20528.90281, 8650.103416, 5451.635083, 3648.127181, 2842.816359, 1694.621607, 2187.772519, 2032.306623, 1862.681765, 942.3021572, 200.5655249, 120.071825, 122.4051285, 469.1050591, 8.875214213, 140.8950062, 213.0906671, 608567.5879, 360990.2259, 211216.0138, 152720.2627, 88427.61006, 65255.07293, 52692.34184, 38905.8754, 24875.94908, 12958.71511, 11203.23855, 8707.653092, 4895.653757, 2273.260147, 1145.774338, 1730.607605, 948.4676883, 553.2617508, 391.6912758, 261.9256744, 146.3479761, 401.2934068, 6551879.44, 3597879.878, 1911409.306, 1101788.695, 687789.176, 423182.1572, 350688.4965, 246362.5123, 155494.9851, 95647.33124, 76591.37274, 44176.33742, 28352.90276, 19979.0781, 12577.73846, 8966.384678, 5299.337851, 3083.91343, 2180.052363, 1252.972058, 1231.2964, 1881.848989},
          {140493.1883, 107441.6449, 50481.56475, 33962.24805, 21121.20986, 12118.69637, 6026.579068, 3623.563758, 2472.273758, 1325.111473, 767.8563373, 1138.926563, 1371.55958, 1101.774103, 442.7284225, 123.3361608, 85.51077071, 145.3429426, 311.900704, 7.070590128, 60.95622324, 100.2131191, 354372.6254, 211909.7133, 126887.4795, 89773.82779, 54021.34122, 39796.34341, 31151.35581, 22367.27401, 14918.5289, 7975.54845, 6291.509763, 4617.198292, 3124.931972, 1433.07944, 799.2200889, 1045.121419, 525.4359042, 253.1373132, 258.3868781, 169.3397574, 104.9963204, 269.3045929, 3595432.986, 1911409.306, 1122440.531, 619159.1379, 385877.7457, 239223.3747, 197886.1597, 138938.2433, 88036.67581, 53954.44841, 43540.33319, 25249.15907, 15950.88488, 11366.76325, 7015.242204, 5047.011894, 2997.582138, 1784.096136, 1229.668548, 748.4358365, 648.3200466, 1029.798123},
          {71683.80747, 57530.29403, 26339.21394, 17081.49673, 10913.812, 6266.756735, 2546.919679, 1907.348106, 781.6801036, 658.9291514, 506.0217101, 778.103376, 610.4122463, 685.8827083, 263.7392097, 73.66079935, 40.0993913, 126.618617, 155.7057978, 12.76007031, 12.42313264, 49.13269736, 213328.332, 130193.9925, 78013.37639, 56672.71362, 33952.78362, 24944.54094, 20099.82296, 14216.79433, 9176.160541, 4853.740125, 4345.41277, 3114.571437, 1793.191782, 900.2015586, 548.0100049, 708.9569729, 358.4657446, 209.4042208, 159.3761116, 106.7210782, 64.6305252, 137.8188581, 2062331.57, 1101788.695, 619159.1379, 382075.4485, 225575.1145, 140644.804, 116896.5613, 81973.66558, 52249.88289, 31810.94626, 25757.84319, 14987.33075, 9429.263174, 6786.875676, 4213.664429, 3038.252515, 1799.276957, 1079.34261, 779.2048669, 464.0519374, 415.0355169, 640.0452968},
          {25941.15478, 26698.69573, 12045.20872, 7443.99313, 6462.338842, 3418.450314, 1236.441353, 1056.932204, 735.6566084, 556.3248917, 475.7697137, 433.1645454, 413.9643847, 405.8569798, 132.927272, 43.09897062, 19.64217494, 54.14163627, 83.85351102, 6.238652243, 28.00952165, 50.42296256, 137671.231, 81031.42464, 49465.38025, 35821.53321, 20826.38435, 15584.0728, 12411.91254, 9113.189265, 5628.34674, 2921.547394, 2641.109945, 1984.991136, 1166.679523, 570.7074348, 347.2145007, 437.8353405, 233.3697081, 128.4411207, 103.8126493, 66.27286913, 36.23304992, 101.303505, 1290054.367, 687789.176, 385877.7457, 225575.1145, 153211.3713, 88752.93919, 73604.09787, 51749.81291, 33014.36257, 20341.26959, 16323.95933, 9541.362768, 6072.206982, 4277.734479, 2700.812941, 1966.509917, 1158.464354, 687.068436, 522.3715515, 313.5698375, 289.9078535, 408.3827892},
          {22392.10864, 17782.28201, 6734.941483, 5096.214852, 3978.987721, 2314.581176, 1168.703684, 1078.611848, 568.772197, 451.7383426, 263.7992199, 344.0349982, 314.3834246, 292.8199441, 148.4542433, 51.42054125, 33.26442306, 30.75732307, 71.04295878, 6.581337044, 15.13838374, 23.22575228, 88341.58863, 51150.09722, 31611.4467, 22989.4366, 13591.90364, 10767.35236, 8414.69074, 6101.629587, 3888.809142, 2030.118905, 1753.99741, 1305.915995, 808.5123542, 418.5728182, 270.358556, 291.7270262, 165.1242111, 67.30457073, 70.56892497, 49.47903716, 24.12165481, 66.35069405, 791719.1241, 423182.1572, 239223.3747, 140644.804, 88752.93919, 62639.37716, 47091.60435, 33192.57134, 21051.69657, 13094.54326, 10635.14358, 6119.530696, 3947.927753, 2766.15371, 1787.100606, 1267.504929, 731.9013365, 456.9964823, 339.3371978, 199.3537642, 185.7758149, 261.8874627},
          {13040.61433, 13685.45039, 6064.149674, 3764.340482, 3394.607725, 2229.408924, 1094.222557, 960.4193086, 709.3725401, 379.8639373, 511.8357953, 417.8134643, 293.6790564, 237.0945028, 113.8805468, 48.50506364, 44.27443874, 52.09716233, 66.8937023, 9.578844737, 11.91513304, 14.44235204, 63321.87793, 36945.59585, 23452.6411, 17529.82375, 10524.10688, 8322.700055, 6673.308656, 4861.789986, 3092.937738, 1767.113434, 1460.19678, 1128.352722, 676.2640872, 362.0041639, 249.6313904, 235.7402893, 114.0976934, 49.33820706, 38.84953011, 52.51830036, 20.68676758, 54.49627804, 653095.147, 350688.4965, 197886.1597, 116896.5613, 73604.09787, 47091.60435, 45685.71477, 27874.95031, 18144.15641, 11209.78594, 9050.485118, 5243.809796, 3329.148386, 2387.14637, 1531.124811, 1102.009035, 683.6024922, 425.0704004, 302.5108041, 179.9792153, 156.954227, 241.7451437},
          {23091.29594, 16128.60889, 6862.084602, 4481.180021, 3490.441441, 1944.236821, 1098.594455, 846.6100139, 562.5941784, 336.9884972, 420.3266971, 272.3796914, 197.5650024, 201.9642141, 87.98889594, 61.14835884, 28.35918932, 33.45773593, 39.84776895, 7.568565905, 14.72316219, 17.82102145, 47700.17404, 26564.6108, 16635.56708, 12671.00706, 7644.636058, 6095.781014, 4831.543001, 3551.248301, 2260.972309, 1356.925002, 1135.974762, 822.2973192, 492.3104345, 258.1690813, 169.7000392, 200.7212296, 111.0490032, 44.95279224, 51.4280712, 32.32105351, 20.01939526, 44.4664588, 460077.5227, 246362.5123, 138938.2433, 81973.66558, 51749.81291, 33192.57134, 27874.95031, 23112.99489, 12819.44477, 8071.472715, 6501.173637, 3845.40887, 2443.710486, 1703.925174, 1067.001292, 776.1043209, 491.5042636, 299.4559235, 220.7177574, 130.1870369, 121.2345481, 178.5491182},
          {13214.87186, 9252.363235, 3608.620719, 2705.758775, 1576.546181, 1115.031676, 839.3335347, 675.0725858, 364.8477749, 220.4131638, 239.3821451, 201.4634385, 130.8500801, 128.9879113, 62.72218852, 25.34217929, 20.67498824, 31.22110784, 27.16745833, 1.525667919, 7.660580391, 11.32504025, 38096.64761, 21729.60443, 13064.65145, 9770.98086, 5950.299707, 4533.677425, 3780.355269, 2616.672123, 1729.379269, 1030.127145, 853.2519754, 624.2720873, 362.669919, 191.9100106, 137.1420288, 145.5098673, 78.45600588, 33.58954574, 38.87657698, 21.0421396, 20.42349344, 28.70265533, 291025.9392, 155494.9851, 88036.67581, 52249.88289, 33014.36257, 21051.69657, 18144.15641, 12819.44477, 10208.60765, 5163.901003, 4182.274497, 2529.201771, 1609.880412, 1137.207538, 720.3704844, 531.9877878, 330.3627378, 218.7023242, 151.3138349, 95.62720146, 82.07452682, 114.7431131},
          {5376.047223, 4169.789462, 1395.885561, 1068.625095, 978.956386, 578.2503238, 221.6730676, 305.6121785, 221.1375414, 110.2855355, 156.4616244, 80.17586408, 83.678634, 66.42014924, 35.98047254, 19.38106448, 2.074817923, 13.06888689, 16.49151705, 4.038243073, 6.07460927, 7.703241575, 17894.00271, 10343.24292, 6860.925358, 5246.542826, 3123.286168, 2540.031699, 2009.503624, 1615.451391, 1028.101881, 574.3729678, 528.7678796, 378.1384698, 213.7291036, 123.4169245, 84.62698106, 84.92723147, 43.0333708, 24.22053787, 25.55317404, 11.82980521, 10.04246237, 23.68079454, 178390.7263, 95647.33124, 53954.44841, 31810.94626, 20341.26959, 13094.54326, 11209.78594, 8071.472715, 5163.901003, 4460.522215, 2664.037597, 1606.605577, 1029.264059, 730.1985382, 465.840455, 351.1281097, 214.7644643, 139.7442893, 104.512415, 63.03562637, 56.17395623, 78.39407691},
          {3014.408717, 3478.671821, 1634.757665, 989.3479815, 887.0380432, 633.9008334, 284.265322, 198.523863, 218.2007778, 75.51732727, 121.4719779, 72.87281273, 61.71908078, 70.37129948, 36.33208592, 19.4863284, 9.601811353, 13.70620037, 15.39235992, 1.303084703, 5.029116416, 7.019966788, 17463.84546, 10389.8681, 6695.225105, 4783.054164, 2966.683785, 2253.712285, 1765.985239, 1331.943406, 846.8168757, 525.3935678, 458.9496027, 301.1511794, 183.9427721, 118.3557501, 78.1750648, 85.93813346, 41.43684891, 24.51864679, 22.5250282, 13.86533471, 4.496355517, 23.0240654, 144968.4266, 76591.37274, 43540.33319, 25757.84319, 16323.95933, 10635.14358, 9050.485118, 6501.173637, 4182.274497, 2664.037597, 3033.76681, 1298.790296, 834.6444861, 592.8751987, 391.1509205, 274.7611769, 178.9131722, 118.8647213, 81.85501644, 49.84675512, 45.00435936, 71.7919713},
          {3385.144538, 2021.603436, 1222.974196, 805.7784228, 461.1765741, 380.5594137, 210.8402636, 286.0286712, 147.7393287, 53.45270262, 98.54813902, 79.63504018, 48.53103181, 31.00717994, 23.13220286, 13.45897228, 2.310418748, 10.446059, 8.519301865, 2.968339843, 3.750303389, 3.11842956, 6201.535517, 3997.119639, 2410.484769, 2128.164575, 1195.523775, 1165.946379, 863.6890407, 679.2280663, 462.0007865, 255.5444911, 235.9779417, 175.578183, 106.0064952, 59.84236898, 46.54610994, 46.71300464, 27.38324379, 10.95657929, 11.62664697, 11.50456679, 5.409193358, 8.107287289, 83314.5584, 44176.33742, 25249.15907, 14987.33075, 9541.362768, 6119.530696, 5243.809796, 3845.40887, 2529.201771, 1606.605577, 1298.790296, 1270.500838, 534.6763696, 359.8951879, 232.1061056, 165.7958805, 111.4689697, 70.35721033, 51.73790027, 29.70299959, 31.13666495, 44.4116086},
          {515.3964082, 676.9799044, 584.377065, 418.215059, 261.4596744, 146.7177549, 66.29162184, 117.1400376, 120.8913437, 43.44214845, 69.20279732, 45.026084, 30.33006804, 31.4579487, 15.04611107, 14.33030689, 3.82321052, 3.426537291, 6.051266134, 1.051746696, 3.314792871, 3.215945241, 4524.820085, 3144.78249, 1808.077288, 1525.064566, 975.2564298, 780.2510863, 647.994207, 438.141051, 280.1338058, 193.710283, 154.2519009, 123.4669238, 74.9532595, 44.41689534, 25.80679766, 29.46775284, 12.937434, 9.390089979, 8.968896332, 5.185018197, 2.545637114, 7.31333113, 52907.0255, 28352.90276, 15950.88488, 9429.263174, 6072.206982, 3947.927753, 3329.148386, 2443.710486, 1609.880412, 1029.264059, 834.6444861, 534.6763696, 603.3916073, 231.6534595, 160.1621698, 111.4335277, 69.50313128, 44.85680745, 34.2792807, 19.68369726, 19.99355854, 26.93309603},
          {1845.243786, 1353.390415, 536.3161812, 396.9324511, 155.1823201, 185.6326566, 121.1640057, 74.08202602, 44.7087457, 47.43582948, 50.06568056, 32.08928032, 21.42948207, 16.81184607, 7.713192988, 9.11910054, 3.820164345, 4.180415353, 4.988161228, 1.282396429, 1.20778476, 0.9202517217, 2690.050236, 2029.613258, 1251.893203, 1022.117638, 642.7618997, 584.1501517, 463.2067122, 344.9663155, 202.2078365, 141.7685742, 116.3772074, 97.35461516, 44.69384116, 36.30446186, 22.33297677, 18.40995781, 12.07038826, 10.54758738, 5.579953064, 3.903525914, 3.27176308, 5.448854143, 37892.02254, 19979.0781, 11366.76325, 6786.875676, 4277.734479, 2766.15371, 2387.14637, 1703.925174, 1137.207538, 730.1985382, 592.8751987, 359.8951879, 231.6534595, 360.5953758, 106.5426938, 78.03221285, 46.99238166, 30.72728161, 21.45654996, 16.25847451, 14.79388871, 20.69429363},
          {-771.374651, -120.2899834, -60.42520352, 34.41434205, -7.789837987, 52.39911793, 18.43744959, 54.03742088, 29.07998106, 9.117313402, 14.49095702, 15.44715518, 7.930949259, 10.62625506, 7.713254492, 7.739550918, 1.277247258, 3.854442474, 3.528527715, 0.6345819547, 0.510200417, 2.50362071, 1974.931117, 1472.341755, 1057.248137, 719.4741045, 444.5610749, 360.5361192, 294.7884287, 213.124425, 137.590184, 79.77576307, 84.11835505, 57.45943384, 32.61474729, 18.85918474, 16.75533083, 21.69005382, 10.45555434, 3.401878395, 2.940726008, 3.390063831, 0.899951682, 4.693040056, 24086.46938, 12577.73846, 7015.242204, 4213.664429, 2700.812941, 1787.100606, 1531.124811, 1067.001292, 720.3704844, 465.840455, 391.1509205, 232.1061056, 160.1621698, 106.5426938, 196.2845371, 53.70111459, 33.26487078, 22.03703922, 16.37014338, 10.0166109, 9.956643701, 13.82620804},
          {854.9087742, 539.343198, 341.1989909, 139.1066363, 93.82329367, 93.83097465, 35.46553893, 54.82382874, 41.58661171, 18.27100511, 5.01069122, 22.21533239, 3.089259972, 9.577750674, 3.316046089, 2.955139058, 3.096347798, 3.172813137, 1.903779425, 1.464847513, 0.4039354771, 1.19344087, 2127.432351, 1329.860516, 748.0219207, 535.9137258, 337.1096338, 259.045005, 207.8735991, 156.1537639, 92.68478178, 55.54210024, 51.44290032, 47.07659869, 27.58811426, 16.23302811, 10.81749608, 11.71465546, 6.239035846, 1.85984143, 2.147763504, 2.912484378, 0.9334531642, 3.240082301, 16802.46159, 8966.384678, 5047.011894, 3038.252515, 1966.509917, 1267.504929, 1102.009035, 776.1043209, 531.9877878, 351.1281097, 274.7611769, 165.7958805, 111.4335277, 78.03221285, 53.70111459, 116.2197155, 21.73452634, 17.61043671, 12.14892181, 7.094178012, 6.123933033, 9.950553003},
          {42.18572303, 104.9900766, 5.229396464, 6.089127507, 13.95609686, 0.03520313089, -8.389749681, 29.73361249, 13.43790445, -13.54362095, 4.06584351, 3.360985369, 3.00050516, 3.955740843, 1.901480575, 0.1635705517, 0.009957962764, 3.498189599, 0.6153935733, 0.5733386592, 0.4962106256, -0.01334545332, 84.88679246, -5.05143028, 123.2452762, 166.1119091, 77.41811558, 120.3837089, 100.4304055, 64.71010442, 64.25409672, 30.52115095, 25.97914017, 26.26568033, 11.09541129, 10.80622084, 5.230435391, 6.730322444, 2.678568331, 2.314225051, 1.575942771, 2.116121733, 1.680418418, 1.871857431, 9926.319489, 5299.337851, 2997.582138, 1799.276957, 1158.464354, 731.9013365, 683.6024922, 491.5042636, 330.3627378, 214.7644643, 178.9131722, 111.4689697, 69.50313128, 46.99238166, 33.26487078, 21.73452634, 72.05201132, 10.8786309, 8.246859343, 5.234928382, 4.517557581, 6.903840615},
          {1221.267656, 625.1391541, 270.5109439, 163.7496422, 120.0262436, 57.30879948, 35.05829587, 26.38351906, 18.32728856, 14.45339855, 4.05044551, 7.155638021, 5.173357132, 4.140031149, 1.861822896, 2.467636942, 1.582505862, 1.911807707, 1.877563742, 0.08291818562, 0.3859618064, 1.2008844, 664.350596, 468.303197, 286.0610777, 214.9911891, 151.1200338, 111.302063, 96.30574094, 67.41045006, 58.61786884, 31.24719873, 33.41725764, 14.7779272, 13.29427249, 7.646017996, 6.339176093, 7.323570289, 3.560621146, 2.531055186, 1.847233145, 0.6326565304, 0.9547321489, 1.204852812, 5571.398529, 3083.91343, 1784.096136, 1079.34261, 687.068436, 456.9964823, 425.0704004, 299.4559235, 218.7023242, 139.7442893, 118.8647213, 70.35721033, 44.85680745, 30.72728161, 22.03703922, 17.61043671, 10.8786309, 42.50348736, 5.522554085, 3.660735762, 3.645432844, 4.868882202},
          {-109.8043719, -64.31825933, -13.96567868, -18.57722738, -8.177066978, 7.358016749, 2.672881378, -0.3870342456, 4.706802307, 3.93055022, 3.379636135, 4.953661443, 1.626035293, 4.843029012, 1.121858442, 1.982110048, 1.052466759, 2.936060305, 0.4088185021, 0.767571954, -0.17741699, 0.7502604484, 274.6944656, 154.3800703, 109.4186277, 113.0549879, 94.08456488, 63.01379939, 59.18092734, 39.2949112, 30.60790534, 20.72684777, 18.75065737, 13.5216477, 7.661442577, 3.351135756, 5.922879713, 4.222823501, 2.179624126, 1.615105526, 1.488189324, 1.0759214, 0.8017114449, 1.382081627, 4211.809437, 2180.052363, 1229.668548, 779.2048669, 522.3715515, 339.3371978, 302.5108041, 220.7177574, 151.3138349, 104.512415, 81.85501644, 51.73790027, 34.2792807, 21.45654996, 16.37014338, 12.14892181, 8.246859343, 5.522554085, 26.78764813, 2.782795732, 2.60202909, 3.407258263},
          {48.99872145, -43.88893136, 27.17719111, 31.15819231, 16.76327764, 13.26469595, 5.996031102, 7.022810006, 2.854391733, -2.315761656, -1.83919345, -1.542108249, 1.285221005, 0.9948950473, -0.741198561, 0.06210888991, 1.256114315, 1.03545886, 0.5173346697, -0.1591799049, 0.3387056982, -0.05711961391, 632.2702019, 324.2727354, 211.3865361, 130.3843451, 86.79120967, 69.82736327, 51.04241568, 48.71391345, 28.18834446, 11.44080524, 13.99799139, 11.08617417, 5.769851361, 4.693133551, 3.091934222, 2.566968535, 0.7047812374, 0.864532486, 1.130175294, 0.6429168884, 0.7050590906, 0.5568566802, 2469.630688, 1252.972058, 748.4358365, 464.0519374, 313.5698375, 199.3537642, 179.9792153, 130.1870369, 95.62720146, 63.03562637, 49.84675512, 29.70299959, 19.68369726, 16.25847451, 10.0166109, 7.094178012, 5.234928382, 3.660735762, 2.782795732, 14.15483687, 1.313729707, 2.321724668},
          {170.272321, 163.4437339, 92.34381722, 52.80129406, 13.79563254, -3.437616789, 8.709688038, 11.92216815, 5.748188247, -2.348008619, 2.504156597, 1.558816544, 2.857367965, 1.311938076, 0.4660948576, 0.983416606, 0.5537127236, 0.7150422923, 0.5368543574, -0.009546834946, 0.6301101696, 0.07833836911, 219.4002956, 154.4921703, 115.0045901, 82.82925647, 53.85764508, 46.41074454, 35.79549611, 28.04003385, 12.62521308, 12.82616962, 5.878579041, 11.10508486, 4.000549434, 2.808877, 2.711142456, 2.565665635, 1.421513518, 0.3440013996, 0.4240060426, 0.3664242547, 0.4215447344, 0.9874023752, 2312.805086, 1231.2964, 648.3200466, 415.0355169, 289.9078535, 185.7758149, 156.954227, 121.2345481, 82.07452682, 56.17395623, 45.00435936, 31.13666495, 19.99355854, 14.79388871, 9.956643701, 6.123933033, 4.517557581, 3.645432844, 2.60202909, 1.313729707, 11.52041738, 2.284164118},
          {117.5851365, 122.3765556, 121.5203094, 31.44833382, 29.0441436, 16.15003463, 5.728862796, 12.26544884, 7.669678321, 0.06123302462, 1.389083341, 3.567380033, 0.2259709354, -0.180715315, 2.028979472, -0.08603436246, 0.8350097416, 0.6092942172, 0.7303244815, -0.2772611512, 0.1156510186, -0.2716696238, 214.621503, 101.7214878, 139.5553672, 84.72970069, 51.41789208, 49.88946879, 37.89944522, 33.34021439, 21.79605349, 11.59843484, 7.77105568, 6.694244522, 6.164922142, 3.354545952, 1.509979773, 2.152127477, 1.807389874, 1.094438063, 0.6168076243, 0.3919385763, 0.4295759504, 0.1907629104, 3518.762797, 1881.848989, 1029.798123, 640.0452968, 408.3827892, 261.8874627, 241.7451437, 178.5491182, 114.7431131, 78.39407691, 71.7919713, 44.4116086, 26.93309603, 20.69429363, 13.82620804, 9.950553003, 6.903840615, 4.868882202, 3.407258263, 2.321724668, 2.284164118, 16.47146155}
        };

        // Save it
        current_ainfo->add_bkgcov(bkgcov);

      }

      ////////////////////////////////////////////
      /// NEW BEAM DUMP content added by Taylor
      // New analysis: SubGeVBeamDump_MB_interpolated
      ////////////////////////////////////////////

      if (current_analysis_name == "SubGeVBeamDump_MBe_interpolated") // MiniBooNE electron limits
      {
        // Create an entry in the global analysis_info_map and point the reference current_ainfo to it
        analysis_info_map[current_analysis_name] = Model_analysis_info();
        current_ainfo = &(analysis_info_map[current_analysis_name]);

        current_ainfo->name = current_analysis_name;

        current_ainfo->obsnum = {0};
        current_ainfo->bkgnum = {0.0};
        current_ainfo->bkgerr = {0.0};

        assert(current_ainfo->obsnum.size() == current_ainfo->bkgnum.size());
        assert(current_ainfo->obsnum.size() == current_ainfo->bkgerr.size());
        current_ainfo->n_signal_regions = current_ainfo->obsnum.size();
      }

      if (current_analysis_name == "SubGeVBeamDump_MBN_interpolated") // MiniBooNE nucleon limits
      {
        // Create an entry in the global analysis_info_map and point the reference current_ainfo to it
        analysis_info_map[current_analysis_name] = Model_analysis_info();
        current_ainfo = &(analysis_info_map[current_analysis_name]);

        current_ainfo->name = current_analysis_name;

        current_ainfo->obsnum = {0};
        current_ainfo->bkgnum = {0.0};
        current_ainfo->bkgerr = {0.0};

        assert(current_ainfo->obsnum.size() == current_ainfo->bkgnum.size());
        assert(current_ainfo->obsnum.size() == current_ainfo->bkgerr.size());
        current_ainfo->n_signal_regions = current_ainfo->obsnum.size();
      }

      if (current_analysis_name == "SubGeVBeamDump_LSND_interpolated") // LSND electron limits
      {
        // Create an entry in the global analysis_info_map and point the reference current_ainfo to it
        analysis_info_map[current_analysis_name] = Model_analysis_info();
        current_ainfo = &(analysis_info_map[current_analysis_name]);

        current_ainfo->name = current_analysis_name;

        current_ainfo->obsnum = {242}; // not entirely sure about this number
        current_ainfo->bkgnum = {229}; 
        current_ainfo->bkgerr = {28};

        assert(current_ainfo->obsnum.size() == current_ainfo->bkgnum.size());
        assert(current_ainfo->obsnum.size() == current_ainfo->bkgerr.size());
        current_ainfo->n_signal_regions = current_ainfo->obsnum.size();
      }

      if (current_analysis_name == "SubGeVBeamDump_NA64_interpolated") // NA64 limits
      {
        // Create an entry in the global analysis_info_map and point the reference current_ainfo to it
        analysis_info_map[current_analysis_name] = Model_analysis_info();
        current_ainfo = &(analysis_info_map[current_analysis_name]);

        current_ainfo->name = current_analysis_name;

        current_ainfo->obsnum = {0};
        current_ainfo->bkgnum = {0.0};
        current_ainfo->bkgerr = {0.0};

        assert(current_ainfo->obsnum.size() == current_ainfo->bkgnum.size());
        assert(current_ainfo->obsnum.size() == current_ainfo->bkgerr.size());
        current_ainfo->n_signal_regions = current_ainfo->obsnum.size();
      }



    }

    /// A function for filling the analysis_info_map for the DMEFT model.
    void DMEFT_fill_analysis_info_map()
    {

      // Helper variables
      str current_analysis_name;
      std::vector<str> colnames;
      Model_analysis_info empty_analysis_info;
      Model_analysis_info* current_ainfo;

      //
      // New analysis: CMS_13TeV_MONOJET_36invfb_interpolated
      //

      // Analysis name
      current_analysis_name = "CMS_13TeV_MONOJET_36invfb_interpolated";

      // Create an entry in the global analysis_info_map and point the pointer current_ainfo to it
      analysis_info_map[current_analysis_name] = Model_analysis_info();
      current_ainfo = &(analysis_info_map[current_analysis_name]);

      fill_analysis_info_map(current_analysis_name, current_ainfo);

      // Create interpolated functions for the CMS analysis:

      // - 2d cross-sections
      colnames = {"mass", "theta", "xsec"};
      current_ainfo->add_interp2d("mass_theta_xsecpb_C61_C64", GAMBIT_DIR "/ColliderBit/data/DMEFT/mass_theta_xsecpb_CMS_C61_C64.txt", colnames);
      current_ainfo->add_interp2d("mass_theta_xsecpb_C62_C63", GAMBIT_DIR "/ColliderBit/data/DMEFT/mass_theta_xsecpb_CMS_C62_C63.txt", colnames);

      // - 1d cross-sections
      colnames = {"mass", "xsec"};
      current_ainfo->add_interp1d("mass_xsecpb_C71", GAMBIT_DIR "/ColliderBit/data/DMEFT/mass_xsecpb_CMS_C71.txt", colnames);
      current_ainfo->add_interp1d("mass_xsecpb_C72", GAMBIT_DIR "/ColliderBit/data/DMEFT/mass_xsecpb_CMS_C72.txt", colnames);
      current_ainfo->add_interp1d("mass_xsecpb_C73", GAMBIT_DIR "/ColliderBit/data/DMEFT/mass_xsecpb_CMS_C73.txt", colnames);
      current_ainfo->add_interp1d("mass_xsecpb_C74", GAMBIT_DIR "/ColliderBit/data/DMEFT/mass_xsecpb_CMS_C74.txt", colnames);

      // - 2d signal efficiencies
      colnames = {"mass", "theta", "SR1", "SR2", "SR3", "SR4", "SR5", "SR6", "SR7", "SR8", "SR9", "SR10",
                  "SR11", "SR12", "SR13", "SR14", "SR15", "SR16", "SR17", "SR18", "SR19", "SR20", "SR21", "SR22"};
      current_ainfo->add_interp2d("mass_theta_eff_C61_C64", GAMBIT_DIR "/ColliderBit/data/DMEFT/mass_theta_eff_CMS_C61_C64.txt", colnames);
      current_ainfo->add_interp2d("mass_theta_eff_C62_C63", GAMBIT_DIR "/ColliderBit/data/DMEFT/mass_theta_eff_CMS_C62_C63.txt", colnames);

      // - 1d signal efficiencies
      colnames = {"mass", "SR1", "SR2", "SR3", "SR4", "SR5", "SR6", "SR7", "SR8", "SR9", "SR10",
                  "SR11", "SR12", "SR13", "SR14", "SR15", "SR16", "SR17", "SR18", "SR19", "SR20", "SR21", "SR22"};
      current_ainfo->add_interp1d("mass_eff_C71", GAMBIT_DIR "/ColliderBit/data/DMEFT/mass_eff_CMS_C71.txt", colnames);
      current_ainfo->add_interp1d("mass_eff_C72", GAMBIT_DIR "/ColliderBit/data/DMEFT/mass_eff_CMS_C72.txt", colnames);
      current_ainfo->add_interp1d("mass_eff_C73", GAMBIT_DIR "/ColliderBit/data/DMEFT/mass_eff_CMS_C73.txt", colnames);
      current_ainfo->add_interp1d("mass_eff_C74", GAMBIT_DIR "/ColliderBit/data/DMEFT/mass_eff_CMS_C74.txt", colnames);

      // 'Clear' the pointer current_ainfo before moving on to the next analysis by pointing it to empty_analysis_info
      current_ainfo = &empty_analysis_info;


      //
      // New analysis: ATLAS_13TeV_MONOJET_139invfb_interpolated
      //

      // Analysis name
      current_analysis_name = "ATLAS_13TeV_MONOJET_139invfb_interpolated";

      analysis_info_map[current_analysis_name] = Model_analysis_info();
      current_ainfo = &(analysis_info_map[current_analysis_name]);

      fill_analysis_info_map(current_analysis_name, current_ainfo);

      // Create interpolated functions for the ATLAS analysis:

      // - 2d cross-sections
      colnames = {"mass", "theta", "xsec"};
      current_ainfo->add_interp2d("mass_theta_xsecpb_C61_C64", GAMBIT_DIR "/ColliderBit/data/DMEFT/mass_theta_xsecpb_ATLAS_C61_C64.txt", colnames);
      current_ainfo->add_interp2d("mass_theta_xsecpb_C62_C63", GAMBIT_DIR "/ColliderBit/data/DMEFT/mass_theta_xsecpb_ATLAS_C62_C63.txt", colnames);

      // - 1d cross-sections
      colnames = {"mass", "xsec"};
      current_ainfo->add_interp1d("mass_xsecpb_C71", GAMBIT_DIR "/ColliderBit/data/DMEFT/mass_xsecpb_ATLAS_C71.txt", colnames);
      current_ainfo->add_interp1d("mass_xsecpb_C72", GAMBIT_DIR "/ColliderBit/data/DMEFT/mass_xsecpb_ATLAS_C72.txt", colnames);
      current_ainfo->add_interp1d("mass_xsecpb_C73", GAMBIT_DIR "/ColliderBit/data/DMEFT/mass_xsecpb_ATLAS_C73.txt", colnames);
      current_ainfo->add_interp1d("mass_xsecpb_C74", GAMBIT_DIR "/ColliderBit/data/DMEFT/mass_xsecpb_ATLAS_C74.txt", colnames);

      // - 2d signal efficiencies
      colnames = {"mass", "theta", "SR1", "SR2", "SR3", "SR4", "SR5", "SR6", "SR7", "SR8", "SR9", "SR10", "SR11"};
      current_ainfo->add_interp2d("mass_theta_eff_C61_C64", GAMBIT_DIR "/ColliderBit/data/DMEFT/mass_theta_eff_ATLAS_C61_C64.txt", colnames);
      current_ainfo->add_interp2d("mass_theta_eff_C62_C63", GAMBIT_DIR "/ColliderBit/data/DMEFT/mass_theta_eff_ATLAS_C62_C63.txt", colnames);

      // - 1d signal efficiencies
      colnames = {"mass", "SR1", "SR2", "SR3", "SR4", "SR5", "SR6", "SR7", "SR8", "SR9", "SR10", "SR11"};
      current_ainfo->add_interp1d("mass_eff_C71", GAMBIT_DIR "/ColliderBit/data/DMEFT/mass_eff_ATLAS_C71.txt", colnames);
      current_ainfo->add_interp1d("mass_eff_C72", GAMBIT_DIR "/ColliderBit/data/DMEFT/mass_eff_ATLAS_C72.txt", colnames);
      current_ainfo->add_interp1d("mass_eff_C73", GAMBIT_DIR "/ColliderBit/data/DMEFT/mass_eff_ATLAS_C73.txt", colnames);
      current_ainfo->add_interp1d("mass_eff_C74", GAMBIT_DIR "/ColliderBit/data/DMEFT/mass_eff_ATLAS_C74.txt", colnames);

      // 'Clear' the pointer current_ainfo before moving on to the next analysis by pointing it to empty_analysis_info
      current_ainfo = &empty_analysis_info;

    }

    /// Results from DMEFT analyses before any modification of the MET spectrum
    void DMEFT_results(AnalysisDataPointers& result)
    {
      using namespace Pipes::DMEFT_results;

      static bool first = true;

      // In this function we need to transfer info from the DMEFT-specific Model_analysis_info objects
      // to a set of ColliderBit-native AnalysisData objects, and also fill these with the DMEFT signal prediction.

      // We need thread_local AnalysisData instances. Let's collect them in a map.
      thread_local std::map<str,AnalysisData> analysis_data_map;

      // The first time this function is run we must initialize the global analysis_info_map
      // and the thread_local analysis_data_map
      if (first)
      {
        DMEFT_fill_analysis_info_map();

        for (const std::pair<str,const Model_analysis_info&> aname_ainfo_pair : analysis_info_map)
        {
          // Extract analysis name and use it to create an AnalysisData element in the analysis_data_map
          str aname = aname_ainfo_pair.first;
          analysis_data_map[aname] = AnalysisData(aname);
        }

        first = false;
      }

      // Clear previous vectors, etc.
      result.clear();

      // Get the theory spectrum to pass on masses and parameters
      const Spectrum& spec = *Dep::DMEFT_spectrum;

      //
      // Loop over the analyses registered in the analysis_info_map
      //

      for (const std::pair<str,const Model_analysis_info&> aname_ainfo_pair : analysis_info_map)
      {
        // Extract analysis name and reference to the analysis_info instance
        str aname = aname_ainfo_pair.first;
        const Model_analysis_info& ainfo = aname_ainfo_pair.second;

        // Grab a reference to corresponding AnalysisData instance
        // and clear it before we start filling it for the current parameter point
        AnalysisData& adata = analysis_data_map.at(aname);
        adata.clear();

        // Vector to contain signal yield predictions
        std::vector<double> sr_nums(ainfo.n_signal_regions, 0.);

        // Fill the signal yield vector with DMEFT signal predictions
        get_all_DMEFT_signal_yields(sr_nums, ainfo, spec);

        // Create vector of SignalRegionData instances
        std::vector<SignalRegionData> srdata_vector;

        for (size_t sr_index = 0; sr_index < ainfo.n_signal_regions; ++sr_index)
        {
          // Generate an 'sr-N' label
          std::stringstream ss; ss << "sr-" << sr_index;

          // Construct a SignalRegionData instance and add it to srdata_vector
          SignalRegionData sr;
          sr.sr_label = ss.str();
          sr.n_obs = ainfo.obsnum.at(sr_index);
          sr.n_sig_MC = sr_nums.at(sr_index);
          sr.n_sig_scaled = sr_nums.at(sr_index);  // We have already scaled the signals in sr_nums to xsec * lumi
          sr.n_sig_MC_sys = 0.;
          sr.n_bkg = ainfo.bkgnum.at(sr_index);
          sr.n_bkg_err = ainfo.bkgerr.at(sr_index);

          srdata_vector.push_back(sr);
        }

        // Save our vector of SignalRegionData in the AnalysisData instance
        adata.srdata = srdata_vector;

        // If this analysis has a background covariance matrix, copy it to the AnalysisData instance
        if (ainfo.bkgcov.size() > 0)
        {
          adata.srcov = ainfo.bkgcov;
        }

        // Save a pointer to our AnalysisData instance in the 'result' variable
        result.push_back(&adata);

      } // End loop over analyses

    };


    /// Fill the input vector with the total DMEFT signal prediction for each SR in the given LHC analysis
    void get_all_DMEFT_signal_yields(std::vector<double>& sr_nums, const Model_analysis_info& analysis_info, const Spectrum& spec)
    {

      // Get the parameters we need from the theory spectrum
      double C61 = spec.get(Par::dimensionless, "C61");
      double C62 = spec.get(Par::dimensionless, "C62");
      double C63 = spec.get(Par::dimensionless, "C63");
      double C64 = spec.get(Par::dimensionless, "C64");
      double C71 = spec.get(Par::dimensionless, "C71");
      double C72 = spec.get(Par::dimensionless, "C72");
      double C73 = spec.get(Par::dimensionless, "C73");
      double C74 = spec.get(Par::dimensionless, "C74");
      double lambda = spec.get(Par::mass1, "Lambda");
      double m = spec.get(Par::Pole_Mass, "chi");


      // Get the dim-6 yields

      // C61+C64
      std::vector<double> sig_C61_C64(analysis_info.n_signal_regions, 0.);
      get_DMEFT_signal_yields_dim6_operator(sig_C61_C64, "C61_C64", analysis_info, m, C61, C64, lambda);

      // C62+C63
      std::vector<double> sig_C62_C63(analysis_info.n_signal_regions, 0.);
      get_DMEFT_signal_yields_dim6_operator(sig_C62_C63, "C62_C63", analysis_info, m, C62, C63, lambda);


      // Get the dim-7 yields

      // C71
      std::vector<double> sig_C71(analysis_info.n_signal_regions, 0.);
      get_DMEFT_signal_yields_dim7_operator(sig_C71, "C71", analysis_info, m, C71, lambda);

      // C72
      std::vector<double> sig_C72(analysis_info.n_signal_regions, 0.);
      get_DMEFT_signal_yields_dim7_operator(sig_C72, "C72", analysis_info, m, C72, lambda);

      // C73
      std::vector<double> sig_C73(analysis_info.n_signal_regions, 0.);
      get_DMEFT_signal_yields_dim7_operator(sig_C73, "C73", analysis_info, m, C73, lambda);

      // C74
      std::vector<double> sig_C74(analysis_info.n_signal_regions, 0.);
      get_DMEFT_signal_yields_dim7_operator(sig_C74, "C74", analysis_info, m, C74, lambda);


      // Add yields and save in sr_num
      for (size_t i = 0; i < analysis_info.n_signal_regions; ++i)
      {
        sr_nums[i] = sig_C61_C64[i] + sig_C62_C63[i] + sig_C71[i] + sig_C72[i] + sig_C73[i] + sig_C74[i];
      }
    }


    /// Fill the input vector with the DMEFT signal prediction for a given set of dim-6 operators
    void get_DMEFT_signal_yields_dim6_operator(std::vector<double>& signal_yields, const str operator_key, const Model_analysis_info& analysis_info, double m, double O1, double O2, double lambda)
    {

      // Calculate theta
      double theta;
      if (O2==0)
      {
        theta = 0.5 * pi;
      }
      else
      {
        theta = atan(O1 / O2);
        if ( O1 / O2 < 0)
        {
          theta = theta + pi;
        }
      }

      // Calculate normalisation
      double norm = O1*O1 + O2*O2;
      if (norm < 0.0)
      {
        ColliderBit_error().raise(LOCAL_INFO, "ERROR! norm < 0 in function get_DMEFT_signal_yields_dim6_operator.");
      }

      // Scaling with lambda, relative to lambda = 1000 GeV which was used to generate the data tables
      double lambda_scaling = pow(1000.0 / lambda, 4);

      // Get the interpolator collections for the given operator_key
      const Utils::interp2d_gsl_collection& xsec_interp = analysis_info.get_interp2d("mass_theta_xsecpb_" + operator_key);
      const Utils::interp2d_gsl_collection& eff_interp = analysis_info.get_interp2d("mass_theta_eff_" + operator_key);

      // Compute the signal yield for each signal region
      for (size_t sr_i = 0; sr_i < analysis_info.n_signal_regions; ++sr_i)
      {

        //
        // Get the cross-section at the point (m,theta)
        //

        double xsec_pb = 0.;
        // Check if (m,theta) point is inside interpolation region
        if (not xsec_interp.is_inside_range(m,theta))
        {
          if (theta < xsec_interp.y_min || theta > xsec_interp.y_max)
          {
            ColliderBit_error().raise(LOCAL_INFO, "ERROR! Theta parameter out of range.");
          }

          if (m < xsec_interp.x_min)
          {
            ColliderBit_error().raise(LOCAL_INFO, "Mass parameter below lowest mass point in the cross-section table.");
          }

          if (m > xsec_interp.x_min)
          {
            // Set cross-section to 0 for masses above the tabulated range
            xsec_pb = 0.;
          }
        }
        else // All is OK, let's evaluate the cross-section
        {
          xsec_pb = xsec_interp.eval(m, theta);
        }


        //
        // Get signal efficiency for signal region sr_i at the point (m,theta)
        //

        double eff = 0.;
        // Check if (m,theta) point is inside interpolation region
        if (not eff_interp.is_inside_range(m,theta))
        {
          if (theta < eff_interp.y_min || theta > eff_interp.y_max)
          {
            ColliderBit_error().raise(LOCAL_INFO, "ERROR! Theta parameter out of range.");
          }

          if (m < eff_interp.x_min)
          {
            ColliderBit_error().raise(LOCAL_INFO, "Mass parameter below lowest mass point in the signal efficiency table.");
          }

          if (m > eff_interp.x_min)
          {
            // Set efficiency to 0 for masses above the tabulated range
            eff = 0.;
          }
        }
        else // All is OK, let's evaluate the efficiency
        {
          eff = eff_interp.eval(m, theta, sr_i);
        }

        //
        // Compute signal prediction and save it in the signal_yields vector
        //

        signal_yields[sr_i] = analysis_info.lumi_invfb * (xsec_pb * 1000.) * norm * lambda_scaling * eff; // converting cross-section from pb to fb

        #ifdef COLLIDERBIT_DEBUG
        {
          cerr << std::scientific << "DEBUG:" << " operator:" << operator_key << ", analysis:" << analysis_info.name
               << ", sr_i:" << sr_i << ", m:" << m << ", theta:" << theta << ", xsec_pb:" << xsec_pb << ", eff:" << eff
               << ", lambda_scaling:" << lambda_scaling << ", norm:" << norm << ", signal:" << signal_yields[sr_i] << endl;
        }
        #endif

      }  // End loop over signal regions

    }


    /// Fill the input vector with the DMEFT signal prediction for a given dim-7 operator
    void get_DMEFT_signal_yields_dim7_operator(std::vector<double>& signal_yields, const str operator_key, const Model_analysis_info& analysis_info, double m, double O, double lambda)
    {

      // Calculate normalisation
      double norm = O*O;
      if (norm < 0.0)
      {
        ColliderBit_error().raise(LOCAL_INFO, "ERROR! norm < 0 in function get_DMEFT_signal_yields_dim7_operator.");
      }

      // Scaling with lambda, relative to lambda = 1000 GeV which was used to generate the data tables
      double lambda_scaling = pow(1000.0 / lambda, 6);

      // Get the interpolator collections for the given operator_key
      const Utils::interp1d_gsl_collection& xsec_interp = analysis_info.get_interp1d("mass_xsecpb_" + operator_key);
      const Utils::interp1d_gsl_collection& eff_interp = analysis_info.get_interp1d("mass_eff_" + operator_key);

      // Compute the signal yield for each signal region
      for (size_t sr_i = 0; sr_i < analysis_info.n_signal_regions; ++sr_i)
      {

        //
        // Get the cross-section for mass m
        //

        double xsec_pb = 0.;
        // Check if m is inside interpolation region
        if (not xsec_interp.is_inside_range(m))
        {
          if (m < xsec_interp.x_min)
          {
            ColliderBit_error().raise(LOCAL_INFO, "Mass parameter below lowest mass point in the cross-section table.");
          }

          if (m > xsec_interp.x_min)
          {
            // Set cross-section to 0 for masses above the tabulated range
            xsec_pb = 0.;
          }
        }
        else // All is OK, let's evaluate the cross-section
        {
          xsec_pb = xsec_interp.eval(m);
        }


        //
        // Get signal efficiency for signal region sr_i and mass m
        //

        double eff = 0.;
        // Check if m point is inside interpolation region
        if (not eff_interp.is_inside_range(m))
        {
          if (m < eff_interp.x_min)
          {
            ColliderBit_error().raise(LOCAL_INFO, "Mass parameter below lowest mass point in the signal efficiency table.");
          }

          if (m > eff_interp.x_min)
          {
            // Set efficiency to 0 for masses above the tabulated range
            eff = 0.;
          }
        }
        else // All is OK, let's evaluate the efficiency
        {
          eff = eff_interp.eval(m, sr_i);
        }

        //
        // Compute signal prediction and save it in the signal_yields vector
        //

        signal_yields[sr_i] = analysis_info.lumi_invfb * (xsec_pb * 1000.) * norm * lambda_scaling * eff; // converting cross-section from pb to fb

      }  // End loop over signal regions

    }


    /// Results from DMEFT analyses after profiling over the 'a' parameter in the smooth cut-off of the MET spectrum
    void DMEFT_results_profiled(AnalysisDataPointers& result)
    {
      using namespace Pipes::DMEFT_results_profiled;

      // Clear previous vectors, etc.
      result.clear();

      // Get the original AnalysisDataPointers that we will adjust
      result = *Dep::AllAnalysisNumbersUnmodified;

      // Get the best-fit nuisance parameter(s)
      map_str_dbl bestfit_nuisance_pars = *Dep::DMEFT_profiled_LHC_nuisance_params;
      double a_bestfit = bestfit_nuisance_pars.at("a");

      // Get Lambda
      const Spectrum& spec = *Dep::DMEFT_spectrum;
      double lambda = spec.get(Par::mass1, "Lambda");

      // Recalculate AnalysisData instances in "result", using the best-fit a-value
      for (AnalysisData* adata_ptr : result)
      {
        signal_modifier_function(*adata_ptr, lambda, a_bestfit);
      }
    }


    /// Results from DMEFT analyses after imposing a hard cut-off of the MET spectrum
    void DMEFT_results_cutoff(AnalysisDataPointers& result)
    {
      using namespace Pipes::DMEFT_results_cutoff;

      // Clear previous vectors, etc.
      result.clear();

      // Get the original AnalysisDataPointers that we will adjust
      result = *Dep::AllAnalysisNumbersUnmodified;

      // Get Lambda
      const Spectrum& spec = *Dep::DMEFT_spectrum;
      double lambda = spec.get(Par::mass1, "Lambda");

      // Apply the function signal_cutoff_function to each of the
      // AnalysisData instances in "result"
      for (AnalysisData* adata_ptr : result)
      {
        signal_cutoff_function(*adata_ptr, lambda);
      }
    }


    /// Function to modify the DMEFT LHC signal prediction for ETmiss bins where ETmiss > Lambda.
    /// Alt 1: Gradually turn off the ETmiss spectrum above Lambda by multiplying
    /// the spectrum with (ETmiss/Lambda)^-a
    void signal_modifier_function(AnalysisData& adata, double lambda, double a)
    {
      // Check that we have analysis info for the given analysis
      if (analysis_info_map.count(adata.analysis_name) == 0)
      {
        ColliderBit_error().raise(LOCAL_INFO, "Unknown analysis '" + adata.analysis_name +"' encountered in signal_modifier_function!");
      }

      // Get a shorthand reference to the Model_analysis_info instance
      const Model_analysis_info& ainfo = analysis_info_map.at(adata.analysis_name);

      // Modify signals
      for (size_t bin_index = 0; bin_index < ainfo.n_signal_regions; ++bin_index)
      {
        double MET_min = ainfo.extra_info.at("metmins")[bin_index];
        double weight = 1.0;

        if (lambda < MET_min)
        {
          weight = pow(MET_min / lambda, -a);

          if (weight < 1.0e-8) { weight = 0.0; }
        }

        SignalRegionData& srdata = adata[bin_index];
        srdata.n_sig_MC *= weight;
        srdata.n_sig_scaled *= weight;
      }

    }


    /// Function to modify the DMEFT LHC signal prediction for ETmiss bins where ETmiss > Lambda.
    /// Alt 2: Simply put a hard cut-off in the ETmiss spectrum for ETmiss > Lambda
    void signal_cutoff_function(AnalysisData& adata, double lambda)
    {
      // Check that we have analysis info for the given analysis
      if (analysis_info_map.count(adata.analysis_name) == 0)
      {
        ColliderBit_error().raise(LOCAL_INFO, "Unknown analysis '" + adata.analysis_name +"' encountered in signal_modifier_function!");
      }

      // Get a shorthand reference to the Model_analysis_info instance
      const Model_analysis_info& ainfo = analysis_info_map.at(adata.analysis_name);

      // Modify signals with a hard cutoff
      for (size_t bin_index = 0; bin_index < ainfo.n_signal_regions; ++bin_index)
      {
        double MET_min = ainfo.extra_info.at("metmins")[bin_index];

        if (lambda < MET_min)
        {
          SignalRegionData& srdata = adata[bin_index];
          srdata.n_sig_MC = 0.0;
          srdata.n_sig_scaled = 0.0;
        }
      }

    }


    /// A target function for the GSL optimiser
    void _gsl_target_func(const size_t /* n */ , const double* a, void* fparams, double* fval)
    {
      // Note: We don't use the first argument, it's just there for the GSL/multimin interface

      double total_loglike = 0.0;

      // Cast fparams to correct type
      _gsl_target_func_params* fpars = static_cast<_gsl_target_func_params*>(fparams);

      // Create a vector with temp AnalysisData instances by copying the original ones
      std::vector<AnalysisData> temp_adata_vec;
      for (AnalysisData* adata_ptr : fpars->adata_ptrs_original)
      {
        const str& analysis_name = adata_ptr->analysis_name;
        // If the analysis name is in skip_analyses, don't take it into account in this profiling
        if (std::find(fpars->skip_analyses.begin(), fpars->skip_analyses.end(), analysis_name) != fpars->skip_analyses.end())
        {
          continue;
        }
        // Make a copy of the AnalysisData instance that adata_ptr points to
        temp_adata_vec.push_back( AnalysisData(*adata_ptr) );
      }

      // Now loop over all the temp AnalysisData instances and calculate the total loglike for the current a-value
      for (AnalysisData& adata : temp_adata_vec)
      {
        // Grab some info about the current analysis
        const bool has_covar = adata.srcov.rows() > 0;
        const bool has_fulllikes = adata.hasFullLikes();

        // Modify the signal predictions for this analysis
        signal_modifier_function(adata, fpars->lambda, *a);

        // Compute the combined analysis loglike and add it to total_loglike
        AnalysisLogLikes analoglikes;
        analoglikes.initialize(adata);
        fill_analysis_loglikes(adata, analoglikes, fpars->use_marg, fpars->use_covar && has_covar, fpars->combine_nocovar_SRs, fpars->use_fulllikes && has_fulllikes, nullptr, nullptr, nullptr, "");
        total_loglike += analoglikes.combination_loglike;
      }

      *fval = -total_loglike;
    }



    // DMEFT: Profile the 'a' nuisance parameter, which is used to smoothly
    // suppress signal predictions for MET bins with MET > Lambda
    void calc_DMEFT_profiled_LHC_nuisance_params(map_str_dbl& result)
    {
      using namespace Pipes::calc_DMEFT_profiled_LHC_nuisance_params;

      static bool first = true;

      // Check if user has requested a fixed value for the a parameter
      static bool use_fixed_value_a = false;
      static double fixed_a = -1e99;
      if (first)
      {
        if (runOptions->hasKey("use_fixed_value_a"))
        {
          use_fixed_value_a = true;
          fixed_a = runOptions->getValue<double>("use_fixed_value_a");
        }
        first = false;
      }

      if (use_fixed_value_a)
      {
        result["a"] = fixed_a;
        return;
      }

      // Steal the list of skipped analyses from the options from the "calc_combined_LHC_LogLike" function
      std::vector<str> default_skip_analyses;  // The default is empty lists of analyses to skip
      static const std::vector<str> skip_analyses = Pipes::calc_combined_LHC_LogLike::runOptions->getValueOrDef<std::vector<str> >(default_skip_analyses, "skip_analyses");

      // Steal some settings from the "calc_LHC_LogLikes" function
      static const bool use_covar = Pipes::calc_LHC_LogLikes::runOptions->getValueOrDef<bool>(true, "use_covariances");
      // Use marginalisation rather than profiling (probably less stable)?
      static const bool use_marg = Pipes::calc_LHC_LogLikes::runOptions->getValueOrDef<bool>(false, "use_marginalising");
      // Use the naive sum of SR loglikes for analyses without known correlations?
      static const bool combine_nocovar_SRs = Pipes::calc_LHC_LogLikes::runOptions->getValueOrDef<bool>(false, "combine_SRs_without_covariances");
      // These LHC likelihoods don't use the ATLAS full likelihood system
      static const bool use_fulllikes = false;

      // Clear previous result map
      result.clear();

      // Optimiser parameters
      // Params: step1size, tol, maxiter, epsabs, simplex maxsize, method, verbosity
      // Methods:
      //  0: Fletcher-Reeves conjugate gradient
      //  1: Polak-Ribiere conjugate gradient
      //  2: Vector Broyden-Fletcher-Goldfarb-Shanno method
      //  3: Steepest descent algorithm
      //  4: Nelder-Mead simplex
      //  5: Vector Broyden-Fletcher-Goldfarb-Shanno method ver. 2
      //  6: Simplex algorithm of Nelder and Mead ver. 2
      //  7: Simplex algorithm of Nelder and Mead: random initialization

      static const double INITIAL_STEP = runOptions->getValueOrDef<double>(0.1, "nuisance_prof_initstep");
      static const double CONV_TOL = runOptions->getValueOrDef<double>(0.01, "nuisance_prof_convtol");
      static const unsigned MAXSTEPS = runOptions->getValueOrDef<unsigned>(10000, "nuisance_prof_maxsteps");
      static const double CONV_ACC = runOptions->getValueOrDef<double>(0.01, "nuisance_prof_convacc");
      static const double SIMPLEX_SIZE = runOptions->getValueOrDef<double>(1e-5, "nuisance_prof_simplexsize");
      static const unsigned METHOD = runOptions->getValueOrDef<unsigned>(6, "nuisance_prof_method");
      static const unsigned VERBOSITY = runOptions->getValueOrDef<unsigned>(0, "nuisance_prof_verbosity");

      static const struct multimin::multimin_params oparams = {INITIAL_STEP, CONV_TOL, MAXSTEPS, CONV_ACC, SIMPLEX_SIZE, METHOD, VERBOSITY};

      // Set fixed function parameters
      _gsl_target_func_params fpars;
      fpars.lambda = Dep::DMEFT_spectrum->get(Par::mass1, "Lambda");
      fpars.adata_ptrs_original = *Dep::AllAnalysisNumbersUnmodified;
      fpars.skip_analyses = skip_analyses;
      fpars.use_covar = use_covar;
      fpars.use_marg = use_marg;
      fpars.combine_nocovar_SRs = combine_nocovar_SRs;
      fpars.use_fulllikes = use_fulllikes;

      // Create a variable to store the best-fit loglike
      double minus_loglike_bestfit = 50000.;

      // Nuisance parameter(s) to be profiled
      // NOTE: Currently we only profile one parameter ('a'), but the
      //       below setup can  easily be extended to more parameters
      static const std::vector<double> init_values_a = runOptions->getValue<std::vector<double>>("init_values_a");
      static const std::pair<double,double> range_a = runOptions->getValue<std::pair<double,double>>("range_a");

      // How many times should we run the optimiser?
      static const size_t n_runs = init_values_a.size();
      size_t run_i = 0;
      double current_bestfit_a = init_values_a.at(0);
      double current_bestfit_loglike = -minus_loglike_bestfit;

      // Mute stderr while running multimin (due to verbose gsl output)?
      static bool silence_multimin = runOptions->getValueOrDef<bool>(true, "silence_multimin");

      // Do profiling n_runs times
      while (run_i < n_runs)
      {
        std::vector<double> nuisances = {init_values_a[run_i]};  // set initial guess for each nuisance parameter
        std::vector<double> nuisances_min = {range_a.first};   // min value for each nuisance parameter
        std::vector<double> nuisances_max = {range_a.second}; // max value for each nuisance parameter
        const size_t n_profile_pars = nuisances.size();
        // Choose boundary type for each nuisance param (see comment below)
        std::vector<unsigned int> boundary_types = {6};
        /*
        From multimin.cpp:
          Interval:                                       Transformation:
          0 unconstrained                                 x=y
          1 semi-closed right half line [ xmin,+infty )   x=xmin+y^2
          2 semi-closed left  half line ( -infty,xmax ]   x=xmax-y^2
          3 closed interval              [ xmin,xmax ]    x=SS+SD*sin(y)
          4 open right half line        ( xmin,+infty )   x=xmin+exp(y)
          5 open left  half line        ( -infty,xmax )   x=xmax-exp(y)
          6 open interval                ( xmin,xmax )    x=SS+SD*tanh(y)

          where SS=.5(xmin+xmax) SD=.5(xmax-xmin)
        */

        // Call the optimiser
        if (silence_multimin)
        {
          CALL_WITH_SILENCED_STDERR(
            multimin::multimin(n_profile_pars, &nuisances[0], &minus_loglike_bestfit,
                     &boundary_types[0], &nuisances_min[0], &nuisances_max[0],
                     &_gsl_target_func, nullptr, nullptr, &fpars, oparams)
          )
        }
        else
        {
          multimin::multimin(n_profile_pars, &nuisances[0], &minus_loglike_bestfit,
                   &boundary_types[0], &nuisances_min[0], &nuisances_max[0],
                   &_gsl_target_func, nullptr, nullptr, &fpars, oparams);
        }

        double run_i_bestfit_a = nuisances[0];
        double run_i_bestfit_loglike = -minus_loglike_bestfit;

        // Save info for this run
        result["a_run" + std::to_string(run_i)] = run_i_bestfit_a;
        result["loglike_run" + std::to_string(run_i)] = run_i_bestfit_loglike;

        // Update the global result?
        if (run_i_bestfit_loglike > current_bestfit_loglike)
        {
          current_bestfit_loglike = run_i_bestfit_loglike;
          current_bestfit_a = run_i_bestfit_a;
        }

        run_i++;

      } // end optimisation loop

      // Save the overall best-fit results
      result["a"] = current_bestfit_a;
      result["loglike"] = current_bestfit_loglike;


      // DEBUG: Do a grid scan of a and Lambda parameter to investigate the profiled likelihood function
      #ifdef COLLIDERBIT_DEBUG_PROFILING
        double log10_a_min = -1.0;
        double log10_a_max = 3.0;
        double step_log10_a = 0.02;

        double log10_a = log10_a_min;
        std::vector<double> a = { pow(10., log10_a) };
        double ll_val = 0.0;

        double lambda_min = 670.0;
        double lambda_max = 1070.0;
        double step_lambda = 2.0;
        double lambda = lambda_min;

        ofstream f;
        f.open("lambda_a_loglike.dat");

        while (lambda <= lambda_max)
        {
          log10_a = log10_a_min;

          while (log10_a <= log10_a_max)
          {
            cerr << "DEBUG: lambda, log10_a : " << lambda << ", " << log10_a << endl;
            a[0] = pow(10., log10_a);

            fpars.lambda = lambda;

            _gsl_target_func(n_profile_pars, &a[0], &fpars, &ll_val);

            f << fixed << setprecision(8) << fpars.lambda << "  " << a[0] << "  " << ll_val << "\n";

            log10_a += step_log10_a;
          }
          lambda += step_lambda;
        }
        f.close();
      #endif

    }


    /// This makes an MCLoopInfo object for satisfying the ColliderBit dependency chain
    /// (This will not be needed once we have a general system for simulation-less analyses.)
    void InterpolatedMCInfo(MCLoopInfo& result)
    {
      result.event_gen_BYPASS = true;
      result.reset_flags();
    }


    /// A class to hold analysis information for DiJets (specific to DMsimp models)
    class Dijet_analysis_info
    {
      public:

        str name;

        // Maps containing 1D and 2D interpolators
        std::map<str,std::unique_ptr<Utils::interp1d_gsl_collection>> interp1d;
        std::map<str,std::unique_ptr<Utils::interp2d_collection>> interp2d_simple;

        void add_interp1d(str name, str filename, std::vector<str> colnames)
        {
          assert (interp1d.count(name) == 0); // Make sure we're not overwriting an existing entry
          interp1d[name] = std::unique_ptr<Utils::interp1d_gsl_collection>(new Utils::interp1d_gsl_collection(name, filename, colnames));
        }

        void add_interp2d_simple(str name, str filename, std::vector<str> colnames)
        {
          assert (interp2d_simple.count(name) == 0); // Make sure we're not overwriting an existing entry
          interp2d_simple[name] = std::unique_ptr<Utils::interp2d_collection>(new Utils::interp2d_collection(name, filename, colnames));
        }

        const Utils::interp1d_gsl_collection& get_interp1d(str name) const
        {
          return *interp1d.at(name);
        }

        Utils::interp2d_collection& get_interp2d_simple(str name) const
        {
          return *interp2d_simple.at(name);
        }

    };

    /// A function for filling the analysis_info_map for the DMsimp models.
    void DMsimp_fill_analysis_info_map(std::map<str,str> Analysis_data_path, std::map<str,std::vector<str>> Interpolation_columns, int Ndim)
    {

      std::vector<str> default_skip_analyses;  // The default is empty lists of analyses to skip
      static const std::vector<str> skip_analyses = Pipes::calc_combined_LHC_LogLike::runOptions->getValueOrDef<std::vector<str> >(default_skip_analyses, "skip_analyses");

      // Helper variables
      str current_analysis_name;
      std::vector<str> colnames;
      Model_analysis_info empty_analysis_info;
      Model_analysis_info* current_ainfo;
      std::vector< std::vector<double>> bkgcov;

      current_analysis_name = "CMS_13TeV_MONOJET_36invfb_interpolated";

      if (std::find(skip_analyses.begin(), skip_analyses.end(), current_analysis_name) == skip_analyses.end() && Analysis_data_path[current_analysis_name] != "Skip Analysis")
      {
        if (not(Utils::file_exists(Analysis_data_path[current_analysis_name])))
        {
          ColliderBit_error().raise(LOCAL_INFO, "ERROR! MonoJet Interpolation data file missing: " + Analysis_data_path[current_analysis_name] + ". If using one of the DMsimp models, please make sure to run \"make DMsimp_data_1.0\".");
        }

        // Create an entry in the global analysis_info_map and point the pointer current_ainfo to it
        analysis_info_map[current_analysis_name] = Model_analysis_info();
        current_ainfo = &(analysis_info_map[current_analysis_name]);
        fill_analysis_info_map(current_analysis_name, current_ainfo);
        current_ainfo->add_interpNd("MonoJet_Data", Analysis_data_path[current_analysis_name], Interpolation_columns[current_analysis_name], Ndim, true);

        // 'Clear' the pointer current_ainfo before moving on to the next analysis by pointing it to empty_analysis_info
        current_ainfo = &empty_analysis_info;
      }

      // Analysis name
      current_analysis_name = "ATLAS_13TeV_MONOJET_139invfb_interpolated";

      if (std::find(skip_analyses.begin(), skip_analyses.end(), current_analysis_name) == skip_analyses.end() && Analysis_data_path[current_analysis_name] != "Skip Analysis")
      {
        if (not(Utils::file_exists(Analysis_data_path[current_analysis_name])))
        {
          ColliderBit_error().raise(LOCAL_INFO, "ERROR! MonoJet Interpolation data file missing: " + Analysis_data_path[current_analysis_name] + ". If using one of the DMsimp models, please make sure to run \"make DMsimp_data_1.0\".");
        }

        // Create an entry in the global analysis_info_map and point the reference current_ainfo to it
        analysis_info_map[current_analysis_name] = Model_analysis_info();
        current_ainfo = &(analysis_info_map[current_analysis_name]);
        fill_analysis_info_map(current_analysis_name, current_ainfo);
        current_ainfo->add_interpNd("MonoJet_Data", Analysis_data_path[current_analysis_name], Interpolation_columns[current_analysis_name], Ndim, true);

        current_ainfo = &empty_analysis_info;
      }


      current_analysis_name = "CMS_13TeV_MONOJET_137invfb_interpolated";

      if (std::find(skip_analyses.begin(), skip_analyses.end(), current_analysis_name) == skip_analyses.end() && Analysis_data_path[current_analysis_name] != "Skip Analysis")
      {
        if (not(Utils::file_exists(Analysis_data_path[current_analysis_name])))
        {
          ColliderBit_error().raise(LOCAL_INFO, "ERROR! MonoJet Interpolation data file missing: " + Analysis_data_path[current_analysis_name] + ". If using one of the DMsimp models, please make sure to run \"make DMsimp_data_1.0\".");
        }

        // Create an entry in the global analysis_info_map and point the pointer current_ainfo to it
        analysis_info_map[current_analysis_name] = Model_analysis_info();
        current_ainfo = &(analysis_info_map[current_analysis_name]);
        fill_analysis_info_map(current_analysis_name, current_ainfo);
        current_ainfo->add_interpNd("MonoJet_Data", Analysis_data_path[current_analysis_name], Interpolation_columns[current_analysis_name], Ndim, true);

        // 'Clear' the pointer current_ainfo before moving on to the next analysis by pointing it to empty_analysis_info
        current_ainfo = &empty_analysis_info;

      }

    }

    /// Loop over analyses registered in the analysis_info_map
    void get_all_signal_yields(void (*get_all_model_signal_yields)(std::vector<double>&, const Model_analysis_info&, const Spectrum&, str& modelname), const Spectrum& spec, std::map<str,AnalysisData>& analysis_data_map, AnalysisDataPointers& result, str& modelname)
    {

      // Loop over the analyses registered in the analysis_info_map
      // for (const std::pair<str,const Model_analysis_info&>& aname_ainfo_pair : analysis_info_map)
      for (const std::pair<const str, Model_analysis_info>& aname_ainfo_pair : analysis_info_map)
      {
        // Extract analysis name and reference to the analysis_info instance
        str aname = aname_ainfo_pair.first;
        const Model_analysis_info& ainfo = aname_ainfo_pair.second;

        // Grab a reference to corresponding AnalysisData instance
        // and clear it before we start filling it for the current parameter point
        AnalysisData& adata = analysis_data_map.at(aname);
        adata.clear();

        // Vector to contain signal yield predictions
        std::vector<double> sr_nums(ainfo.n_signal_regions, 0.);

        // Use the provided model-specific function pointer to fill the signal yield vector
        // with signal predictions for the given model
        get_all_model_signal_yields(sr_nums, ainfo, spec, modelname);

        // Create vector of SignalRegionData instances
        std::vector<SignalRegionData> srdata_vector;

        for (size_t sr_index = 0; sr_index < ainfo.n_signal_regions; ++sr_index)
        {
          // Generate an 'sr-N' label
          std::stringstream ss; ss << "sr-" << sr_index;

          // Construct a SignalRegionData instance and add it to srdata_vector
          SignalRegionData sr;
          sr.sr_label = ss.str();
          sr.n_obs = ainfo.obsnum.at(sr_index);
          sr.n_sig_MC = sr_nums.at(sr_index);
          sr.n_sig_scaled = sr_nums.at(sr_index);  // We have already scaled the signals in sr_nums to xsec * lumi
          sr.n_sig_MC_sys = 0.;
          sr.n_bkg = ainfo.bkgnum.at(sr_index);
          sr.n_bkg_err = ainfo.bkgerr.at(sr_index);

          srdata_vector.push_back(sr);
        }

        // Save our vector of SignalRegionData in the AnalysisData instance
        adata.srdata = srdata_vector;

        // If this analysis has a background covariance matrix, copy it to the AnalysisData instance
        if (ainfo.bkgcov.size() > 0)
        {
          adata.srcov = ainfo.bkgcov;
        }

        // Save a pointer to our AnalysisData instance in the 'result' variable
        result.push_back(&adata);

      } // End loop over analyses

    }

    /// Results from DMsimp model analyses
    void DMsimp_results(AnalysisDataPointers& result)
    {
      using namespace Pipes::DMsimp_results;

      // Clear previous vectors, etc.
      result.clear();

      static bool first = true;

      // We need thread_local AnalysisData instances. Let's collect them in a map.
      thread_local std::map<str,AnalysisData> analysis_data_map;

      // Store the locations of monojet interpolation data files to pass to DMsimp_fill_analysis_info_map
      std::map<str,str> Analysis_data_path;
      std::map<str,std::vector<str>> Interpolation_columns;
      int Ndim;

      if(ModelInUse("DMsimpVectorMedScalarDM"))
      {
        Analysis_data_path["CMS_13TeV_MONOJET_36invfb_interpolated"] = GAMBIT_DIR "/ColliderBit/data/DMsimp_data/DMsimpVectorMedScalarDM_MonoJets/ScalarDM_CMS36_MonoJet.txt";
        Analysis_data_path["ATLAS_13TeV_MONOJET_139invfb_interpolated"] = GAMBIT_DIR "/ColliderBit/data/DMsimp_data/DMsimpVectorMedScalarDM_MonoJets/ScalarDM_ATLAS139_MonoJet.txt";
        Analysis_data_path["CMS_13TeV_MONOJET_137invfb_interpolated"] = GAMBIT_DIR "/ColliderBit/data/DMsimp_data/DMsimpVectorMedScalarDM_MonoJets/ScalarDM_CMS137_MonoJet.txt";

        Interpolation_columns["CMS_13TeV_MONOJET_36invfb_interpolated"] = {"mDMmV_ratio","mass_MED","gVchi", "gq","xsec", "xsec_unc" ,
                                                                         "SR1", "SR2", "SR3", "SR4", "SR5", "SR6", "SR7", "SR8", "SR9",
                                                                         "SR10", "SR11", "SR12", "SR13", "SR14", "SR15", "SR16", "SR17",
                                                                         "SR18", "SR19", "SR20", "SR21", "SR22"};
        Interpolation_columns["ATLAS_13TeV_MONOJET_139invfb_interpolated"] = {"mDMmV_ratio","mass_MED","gVchi", "gq","xsec", "xsec_unc" ,
                                                                            "EM0","EM1", "EM2", "EM3", "EM4", "EM5", "EM6", "EM7", "EM8",
                                                                            "EM9", "EM10","EM11", "EM12"};
        Interpolation_columns["CMS_13TeV_MONOJET_137invfb_interpolated"] = {"mDMmV_ratio","mass_MED","gVchi", "gq","xsec", "xsec_unc" ,
                                                                          "SR1", "SR2", "SR3", "SR4", "SR5", "SR6", "SR7", "SR8", "SR9",
                                                                          "SR10","SR11", "SR12", "SR13", "SR14", "SR15", "SR16", "SR17",
                                                                          "SR18", "SR19", "SR20", "SR21", "SR22", "SR23", "SR24", "SR25",
                                                                          "SR26", "SR27", "SR28", "SR29", "SR30", "SR31", "SR32","SR33",
                                                                          "SR34", "SR35", "SR36", "SR37", "SR38", "SR39", "SR40", "SR41",
                                                                          "SR42", "SR43", "SR44", "SR45", "SR46", "SR47", "SR48", "SR49",
                                                                          "SR50", "SR51", "SR52", "SR53", "SR54","SR55", "SR56", "SR57",
                                                                          "SR58", "SR59", "SR60", "SR61", "SR62", "SR63", "SR64", "SR65", "SR66"};

         Ndim = 4;
      }
      else if(ModelInUse("DMsimpVectorMedMajoranaDM"))
      {
        Analysis_data_path["CMS_13TeV_MONOJET_36invfb_interpolated"] = GAMBIT_DIR "/ColliderBit/data/DMsimp_data/DMsimpVectorMedMajoranaDM_MonoJets/MajoranaDM_CMS36_MonoJet.txt";
        Analysis_data_path["ATLAS_13TeV_MONOJET_139invfb_interpolated"] = GAMBIT_DIR "/ColliderBit/data/DMsimp_data/DMsimpVectorMedMajoranaDM_MonoJets/MajoranaDM_ATLAS139_MonoJet.txt";
        Analysis_data_path["CMS_13TeV_MONOJET_137invfb_interpolated"] = GAMBIT_DIR "/ColliderBit/data/DMsimp_data/DMsimpVectorMedMajoranaDM_MonoJets/MajoranaDM_CMS137_MonoJet.txt";

        Interpolation_columns["CMS_13TeV_MONOJET_36invfb_interpolated"] = {"mDMmV_ratio","mass_MED","gAchi", "gq","xsec", "xsec_unc" ,
                                                                         "SR1", "SR2", "SR3", "SR4", "SR5", "SR6", "SR7", "SR8", "SR9",
                                                                         "SR10", "SR11", "SR12", "SR13", "SR14", "SR15", "SR16", "SR17",
                                                                         "SR18", "SR19", "SR20", "SR21", "SR22"};
        Interpolation_columns["ATLAS_13TeV_MONOJET_139invfb_interpolated"] = {"mDMmV_ratio","mass_MED","gAchi", "gq","xsec", "xsec_unc" ,
                                                                            "EM0","EM1", "EM2", "EM3", "EM4", "EM5", "EM6", "EM7", "EM8",
                                                                            "EM9", "EM10","EM11", "EM12"};
        Interpolation_columns["CMS_13TeV_MONOJET_137invfb_interpolated"] = {"mDMmV_ratio","mass_MED","gAchi", "gq","xsec", "xsec_unc" ,
                                                                          "SR1", "SR2", "SR3", "SR4", "SR5", "SR6", "SR7", "SR8", "SR9",
                                                                          "SR10","SR11", "SR12", "SR13", "SR14", "SR15", "SR16", "SR17",
                                                                          "SR18", "SR19", "SR20", "SR21", "SR22", "SR23", "SR24", "SR25",
                                                                          "SR26", "SR27", "SR28", "SR29", "SR30", "SR31", "SR32","SR33",
                                                                          "SR34", "SR35", "SR36", "SR37", "SR38", "SR39", "SR40", "SR41",
                                                                          "SR42", "SR43", "SR44", "SR45", "SR46", "SR47", "SR48", "SR49",
                                                                          "SR50", "SR51", "SR52", "SR53", "SR54","SR55", "SR56", "SR57",
                                                                          "SR58", "SR59", "SR60", "SR61", "SR62", "SR63", "SR64", "SR65", "SR66"};

         Ndim = 4;
      }
      else if(ModelInUse("DMsimpVectorMedDiracDM"))
      {
        Analysis_data_path["CMS_13TeV_MONOJET_36invfb_interpolated"] = GAMBIT_DIR "/ColliderBit/data/DMsimp_data/DMsimpVectorMedDiracDM_MonoJets/DiracDM_CMS36_MonoJet.txt";
        Analysis_data_path["ATLAS_13TeV_MONOJET_139invfb_interpolated"] = GAMBIT_DIR "/ColliderBit/data/DMsimp_data/DMsimpVectorMedDiracDM_MonoJets/DiracDM_ATLAS139_MonoJet.txt";
        Analysis_data_path["CMS_13TeV_MONOJET_137invfb_interpolated"] = GAMBIT_DIR "/ColliderBit/data/DMsimp_data/DMsimpVectorMedDiracDM_MonoJets/DiracDM_CMS137_MonoJet.txt";

        Interpolation_columns["CMS_13TeV_MONOJET_36invfb_interpolated"] = {"mDMmV_ratio","mass_MED","gVchi","gAchi", "gq","xsec", "xsec_unc" ,
                                                                         "SR1", "SR2", "SR3", "SR4", "SR5", "SR6", "SR7", "SR8", "SR9",
                                                                         "SR10", "SR11", "SR12", "SR13", "SR14", "SR15", "SR16", "SR17",
                                                                         "SR18", "SR19", "SR20", "SR21", "SR22"};
        Interpolation_columns["ATLAS_13TeV_MONOJET_139invfb_interpolated"] = {"mDMmV_ratio","mass_MED","gVchi","gAchi", "gq","xsec", "xsec_unc" ,
                                                                            "EM0","EM1", "EM2", "EM3", "EM4", "EM5", "EM6", "EM7", "EM8",
                                                                            "EM9", "EM10","EM11", "EM12"};
        Interpolation_columns["CMS_13TeV_MONOJET_137invfb_interpolated"] = {"mDMmV_ratio","mass_MED","gVchi","gAchi", "gq","xsec", "xsec_unc" ,
                                                                          "SR1", "SR2", "SR3", "SR4", "SR5", "SR6", "SR7", "SR8", "SR9",
                                                                          "SR10","SR11", "SR12", "SR13", "SR14", "SR15", "SR16", "SR17",
                                                                          "SR18", "SR19", "SR20", "SR21", "SR22", "SR23", "SR24", "SR25",
                                                                          "SR26", "SR27", "SR28", "SR29", "SR30", "SR31", "SR32","SR33",
                                                                          "SR34", "SR35", "SR36", "SR37", "SR38", "SR39", "SR40", "SR41",
                                                                          "SR42", "SR43", "SR44", "SR45", "SR46", "SR47", "SR48", "SR49",
                                                                          "SR50", "SR51", "SR52", "SR53", "SR54","SR55", "SR56", "SR57",
                                                                          "SR58", "SR59", "SR60", "SR61", "SR62", "SR63", "SR64", "SR65", "SR66"};

         Ndim = 5;
      }
      else if(ModelInUse("DMsimpVectorMedVectorDM"))
      {
        // Skipping the 36 invfb anaysis since it was not simulated for this model
        Analysis_data_path["CMS_13TeV_MONOJET_36invfb_interpolated"] = "Skip Analysis";
        Analysis_data_path["ATLAS_13TeV_MONOJET_139invfb_interpolated"] = GAMBIT_DIR "/ColliderBit/data/DMsimp_data/DMsimpVectorMedVectorDM_MonoJets/VectorDM_ATLAS139_MonoJet.txt";
        Analysis_data_path["CMS_13TeV_MONOJET_137invfb_interpolated"] = GAMBIT_DIR "/ColliderBit/data/DMsimp_data/DMsimpVectorMedVectorDM_MonoJets/VectorDM_CMS137_MonoJet.txt";

        Interpolation_columns["CMS_13TeV_MONOJET_36invfb_interpolated"] = {"mDMmV_ratio","mass_MED","gVchi", "gq","xsec", "xsec_unc" ,
                                                                         "SR1", "SR2", "SR3", "SR4", "SR5", "SR6", "SR7", "SR8", "SR9",
                                                                         "SR10", "SR11", "SR12", "SR13", "SR14", "SR15", "SR16", "SR17",
                                                                         "SR18", "SR19", "SR20", "SR21", "SR22"};
        Interpolation_columns["ATLAS_13TeV_MONOJET_139invfb_interpolated"] = {"mDMmV_ratio","mass_MED","gVchi", "gq","xsec", "xsec_unc" ,
                                                                            "EM0","EM1", "EM2", "EM3", "EM4", "EM5", "EM6", "EM7", "EM8",
                                                                            "EM9", "EM10","EM11", "EM12"};
        Interpolation_columns["CMS_13TeV_MONOJET_137invfb_interpolated"] = {"mDMmV_ratio","mass_MED","gVchi", "gq","xsec", "xsec_unc" ,
                                                                          "SR1", "SR2", "SR3", "SR4", "SR5", "SR6", "SR7", "SR8", "SR9",
                                                                          "SR10","SR11", "SR12", "SR13", "SR14", "SR15", "SR16", "SR17",
                                                                          "SR18", "SR19", "SR20", "SR21", "SR22", "SR23", "SR24", "SR25",
                                                                          "SR26", "SR27", "SR28", "SR29", "SR30", "SR31", "SR32","SR33",
                                                                          "SR34", "SR35", "SR36", "SR37", "SR38", "SR39", "SR40", "SR41",
                                                                          "SR42", "SR43", "SR44", "SR45", "SR46", "SR47", "SR48", "SR49",
                                                                          "SR50", "SR51", "SR52", "SR53", "SR54","SR55", "SR56", "SR57",
                                                                          "SR58", "SR59", "SR60", "SR61", "SR62", "SR63", "SR64", "SR65", "SR66"};

         Ndim = 4;
      }


      // The first time this function is run we must initialize the global analysis_info_map
      // and the thread_local analysis_data_map
      if (first)
      {
        DMsimp_fill_analysis_info_map(Analysis_data_path,Interpolation_columns, Ndim);

        for (const std::pair<const str, Model_analysis_info>& aname_ainfo_pair : analysis_info_map)
        {
          // Extract analysis name and use it to create an AnalysisData element in the analysis_data_map
          str aname = aname_ainfo_pair.first;
          analysis_data_map[aname] = AnalysisData(aname);
        }

        first = false;
      }

      // Retrieve the signal yields
      if(ModelInUse("DMsimpVectorMedScalarDM"))
      {
        const Spectrum& spec = *Dep::DMsimpVectorMedScalarDM_spectrum;
        str modelname = "DMsimpVectorMedScalarDM";
        get_all_signal_yields(get_all_DMsimp_signal_yields, spec, analysis_data_map, result, modelname);
      }
      else if(ModelInUse("DMsimpVectorMedMajoranaDM"))
      {
        const Spectrum& spec = *Dep::DMsimpVectorMedMajoranaDM_spectrum;
        str modelname = "DMsimpVectorMedMajoranaDM";
        get_all_signal_yields(get_all_DMsimp_signal_yields, spec, analysis_data_map, result, modelname);
      }
      else if(ModelInUse("DMsimpVectorMedDiracDM"))
      {
        const Spectrum& spec = *Dep::DMsimpVectorMedDiracDM_spectrum;
        str modelname = "DMsimpVectorMedDiracDM";
        get_all_signal_yields(get_all_DMsimp_signal_yields, spec, analysis_data_map, result, modelname);
      }
      else if(ModelInUse("DMsimpVectorMedVectorDM"))
      {
        const Spectrum& spec = *Dep::DMsimpVectorMedVectorDM_spectrum;
        str modelname = "DMsimpVectorMedVectorDM";
        get_all_signal_yields(get_all_DMsimp_signal_yields, spec, analysis_data_map, result, modelname);
      }

    }


    /// Fill the input vector with the total DMsimp signal prediction for each SR in the given LHC analysis
    void get_all_DMsimp_signal_yields(std::vector<double>& sr_nums, const Model_analysis_info& analysis_info, const Spectrum& spec, str& modelname)
    {

      // Get the yields
      std::vector<double> signal(analysis_info.n_signal_regions, 0.);

      // Get the parameters we need from the theory spectrum
      if (modelname == "DMsimpVectorMedScalarDM")
      {
        double mDM = spec.get(Par::Pole_Mass, "Xc");
        double mMed = spec.get(Par::Pole_Mass, "Y1");
        double gq = spec.get(Par::dimensionless, "gVq");
        double gVchi = spec.get(Par::dimensionless, "gVXc");
        get_DMsimpVectorMedScalarDM_signal_yields(signal, analysis_info, mDM, mMed, gq, gVchi);
      }
      else if (modelname == "DMsimpVectorMedMajoranaDM")
      {
        double mDM = spec.get(Par::Pole_Mass, "Xm");
        double mMed = spec.get(Par::Pole_Mass, "Y1");
        double gq = spec.get(Par::dimensionless, "gVq");
        double gAchi = spec.get(Par::dimensionless, "gAXm");
        get_DMsimpVectorMedMajoranaDM_signal_yields(signal, analysis_info, mDM, mMed, gq, gAchi);
      }
      else if (modelname == "DMsimpVectorMedDiracDM")
      {
        double mDM = spec.get(Par::Pole_Mass, "Xd");
        double mMed = spec.get(Par::Pole_Mass, "Y1");
        double gq = spec.get(Par::dimensionless, "gVq");
        double gVchi = spec.get(Par::dimensionless, "gVXd");
        double gAchi = spec.get(Par::dimensionless, "gAXd");
        get_DMsimpVectorMedDiracDM_signal_yields(signal, analysis_info, mDM, mMed, gq, gVchi, gAchi);
      }
      else if (modelname == "DMsimpVectorMedVectorDM")
      {
        double mDM = spec.get(Par::Pole_Mass, "~Xv");
        double mMed = spec.get(Par::Pole_Mass, "Y1");
        double gq = spec.get(Par::dimensionless, "gVq");
        double gVchi = spec.get(Par::dimensionless, "gVXv");
        get_DMsimpVectorMedVectorDM_signal_yields(signal, analysis_info, mDM, mMed, gq, gVchi);
      }

      // Add yields and save in sr_num
      for (size_t i = 0; i < analysis_info.n_signal_regions; ++i)
      {
        sr_nums[i] = signal[i];
      }
    }


    /// Fill the input vector with the signal prediction for the DMsimpVectorMedScalarDM model
    void get_DMsimpVectorMedScalarDM_signal_yields(std::vector<double>& signal_yields, const Model_analysis_info& analysis_info, double mDM, double mMed, double gq, double gVchi)
    {

      // Get the interpolator collections for the given operator_key
      Utils::interp4d_collection& xsec_interp = analysis_info.get_interp4d("MonoJet_Data");
      Utils::interp4d_collection& eff_interp = analysis_info.get_interp4d("MonoJet_Data");

      // If DM mass is far enough below the resonance, we expect the signal prediction to be roughly constant
      double mDMmV_ratio_min = 0.1;
      double mDMmV_ratio = mDM / mMed;
      if (mDMmV_ratio < mDMmV_ratio_min)
      {
        mDMmV_ratio = mDMmV_ratio_min;
      }

      // Compute the cross-section
      double xsec_pb = xsec_interp.eval(mDMmV_ratio, mMed, gVchi, gq, 0);

      // Compute the signal yield for each signal region
      for (size_t sr_i = 0; sr_i < analysis_info.n_signal_regions; ++sr_i)
      {

        double eff = eff_interp.eval(mDMmV_ratio, mMed, gVchi, gq, sr_i+2);
        double signalcounts = analysis_info.lumi_invfb * xsec_pb * 1000.0 *  eff;
        signal_yields[sr_i] = signalcounts;

        #ifdef COLLIDERBIT_DEBUG
        {
          cerr << std::scientific << "DEBUG:" << ", analysis:" << analysis_info.name
               << ", sr_i:" << sr_i << ", mDM:" << mDM << ", mMed:" << mMed << ", xsec_pb:" << xsec_pb << ", eff:" << eff
               << ", signal:" << signal_yields[sr_i] << endl;
        }
        #endif

      }  // End loop over signal regions

    }

    /// Fill the input vector with the signal prediction for the DMsimpVectorMedDiracDM model
    void get_DMsimpVectorMedDiracDM_signal_yields(std::vector<double>& signal_yields, const Model_analysis_info& analysis_info, double mDM, double mMed, double gq, double gVchi, double gAchi)
    {

      // Get the interpolator collections for the given operator_key
      Utils::interp5d_collection& xsec_interp = analysis_info.get_interp5d("MonoJet_Data");
      Utils::interp5d_collection& eff_interp = analysis_info.get_interp5d("MonoJet_Data");

      // If DM mass is far enough below the resonance, we expect the signal prediction to be roughly constant
      double mDMmV_ratio_min = 0.1;
      double mDMmV_ratio = mDM / mMed;
      if (mDMmV_ratio < mDMmV_ratio_min)
      {
        mDMmV_ratio = mDMmV_ratio_min;
      }

      // Compute the cross-section
      double xsec_pb = xsec_interp.eval(mDMmV_ratio, mMed, gVchi, gAchi, gq, 0);

      // Compute the signal yield for each signal region
      for (size_t sr_i = 0; sr_i < analysis_info.n_signal_regions; ++sr_i)
      {

        double eff = eff_interp.eval(mDMmV_ratio, mMed, gVchi, gAchi, gq, sr_i+2);
        signal_yields[sr_i] = analysis_info.lumi_invfb * xsec_pb * 1000.0 *  eff;

        #ifdef COLLIDERBIT_DEBUG
        {
          cerr << std::scientific << "DEBUG:" << ", analysis:" << analysis_info.name
               << ", sr_i:" << sr_i << ", mDM:" << mDM << ", mMed:" << mMed << ", xsec_pb:" << xsec_pb << ", eff:" << eff
               << ", signal:" << signal_yields[sr_i] << endl;
        }
        #endif

      }  // End loop over signal regions

    }

    /// Fill the input vector with the signal prediction for the DMsimpVectorMedMajoranaDM model
    void get_DMsimpVectorMedMajoranaDM_signal_yields(std::vector<double>& signal_yields, const Model_analysis_info& analysis_info, double mDM, double mMed, double gq, double gAchi)
    {

      // Get the interpolator collections for the given operator_key
      Utils::interp4d_collection& xsec_interp = analysis_info.get_interp4d("MonoJet_Data");
      Utils::interp4d_collection& eff_interp = analysis_info.get_interp4d("MonoJet_Data");

      // If DM mass is far enough below the resonance, we expect the signal prediction to be roughly constant
      double mDMmV_ratio_min = 0.1;
      double mDMmV_ratio = mDM / mMed;
      if (mDMmV_ratio < mDMmV_ratio_min)
      {
        mDMmV_ratio = mDMmV_ratio_min;
      }

      // Compute the cross-section
      double xsec_pb = xsec_interp.eval(mDMmV_ratio, mMed, gAchi, gq, 0);

      // Compute the signal yield for each signal region
      for (size_t sr_i = 0; sr_i < analysis_info.n_signal_regions; ++sr_i)
      {

        double eff = eff_interp.eval(mDMmV_ratio, mMed, gAchi, gq, sr_i+2);
        signal_yields[sr_i] = analysis_info.lumi_invfb * xsec_pb * 1000.0 *  eff;

        #ifdef COLLIDERBIT_DEBUG
        {
          cerr << std::scientific << "DEBUG:" << ", analysis:" << analysis_info.name
               << ", sr_i:" << sr_i << ", mDM:" << mDM << ", mMed:" << mMed << ", xsec_pb:" << xsec_pb << ", eff:" << eff
               << ", signal:" << signal_yields[sr_i] << endl;
        }
        #endif

      }  // End loop over signal regions

    }

    /// Fill the input vector with the signal prediction for the DMsimpVectorMedVectorDM model
    void get_DMsimpVectorMedVectorDM_signal_yields(std::vector<double>& signal_yields, const Model_analysis_info& analysis_info, double mDM, double mMed, double gq, double gVchi)
    {

      // Get the interpolator collections for the given operator_key
      Utils::interp4d_collection& xsec_interp = analysis_info.get_interp4d("MonoJet_Data");
      Utils::interp4d_collection& eff_interp = analysis_info.get_interp4d("MonoJet_Data");

      // If DM mass is far enough below the resonance, we expect the signal prediction to be roughly constant
      double mDMmV_ratio_min = 0.01;
      double mDMmV_ratio = mDM / mMed;
      if (mDMmV_ratio < mDMmV_ratio_min)
      {
        mDMmV_ratio = mDMmV_ratio_min;
      }

      // Compute the cross-section
      double xsec_pb = xsec_interp.eval(mDMmV_ratio, mMed, gVchi, gq, 0);

      // Compute the signal yield for each signal region
      for (size_t sr_i = 0; sr_i < analysis_info.n_signal_regions; ++sr_i)
      {

        double eff = eff_interp.eval(mDMmV_ratio, mMed, gVchi, gq, sr_i+2);
        signal_yields[sr_i] = analysis_info.lumi_invfb * xsec_pb * 1000.0 *  eff;

        #ifdef COLLIDERBIT_DEBUG
        {
          cerr << std::scientific << "DEBUG:" << ", analysis:" << analysis_info.name
               << ", sr_i:" << sr_i << ", mDM:" << mDM << ", mMed:" << mMed << ", xsec_pb:" << xsec_pb << ", eff:" << eff
               << ", signal:" << signal_yields[sr_i] << endl;
        }
        #endif

      }  // End loop over signal regions

    }

    /// A Map between search name and the analysis info needed
    std::map<str,Dijet_analysis_info> DMsimp_dijet_analysis_info;

    /// The di_jet searches that are to be used
    std::vector<str> dijet_searches = {{"ATLAS-CONF-2018-052"},
                                       {"CERN-EP-2017-280"},
                                       {"CERN-EP-2018-347"},
                                       {"CMS-EXO-18-012"},
                                       {"CMS-EXO-19-012"},
                                       {"DiJet_139"},
                                       {"DiJet_TLA"}};


    /// Fill the DMsimp object with the interpolation information.
    void fill_DMsimp_DiJets()
    {

      str analysis_name = "DMsimp_DiJets";
      DMsimp_dijet_analysis_info[analysis_name] = Dijet_analysis_info();

      Dijet_analysis_info* current_ainfo;

      current_ainfo = &(DMsimp_dijet_analysis_info[analysis_name]);

      // Set the analysis info:

      std::vector<str> colnames;
      colnames = {"mass", "gqlimit"};

      for (auto searchname : dijet_searches)
      {
        if (not(Utils::file_exists(GAMBIT_DIR "/ColliderBit/data/DMsimp_data/DMsimp_Dijets/"+searchname+".txt")))
        {
          ColliderBit_error().raise(LOCAL_INFO, "ERROR! DMsimp DiJet data file missing: ColliderBit/data/DMsimp_data/DMsimp_Dijets/"+searchname+".txt" + ". If using one of the DMsimp models, please make sure to run \"make DMsimp_data_1.0\".");
        }

        current_ainfo->add_interp1d(searchname, GAMBIT_DIR "/ColliderBit/data/DMsimp_data/DMsimp_Dijets/"+searchname+".txt", colnames);
      }

      // Clear the pointer
      Dijet_analysis_info empty_analysis_info;
      current_ainfo = &empty_analysis_info;

    }

    /// Perform the actual likelihood evaluation for a given di-jet search
    double DiJet_search_LogLike(str searchname, double gq, double mMed, double BR_q)
    {
      const Utils::interp1d_gsl_collection& search_gqs = DMsimp_dijet_analysis_info["DMsimp_DiJets"].get_interp1d(searchname);

      if (!search_gqs.is_inside_range(mMed))
      {
        return 0.0;
      }

      // Calculate the interpolated coupling
      double gq_limit = search_gqs.eval(mMed);

      // Compare to the input gq and form a chi2.
      double chi2 = 4.0 * pow(gq,4)*pow(BR_q,2)/pow(gq_limit,4);

      // chi2 -> loglike
      return -0.5 * chi2;
    }

    /// Loop over the di-jet analyses and calculate the most constraining likelihood
    double Total_DiJet_search_LogLike(double mMed, double gq, double BR_q)
    {

      double Min_LogLike = 0.0;

      for (auto search : dijet_searches)
      {

        // Form a log-likelihood
        double LogLike = DiJet_search_LogLike(search, gq, mMed, BR_q);

        // Select the most constraining
        if (LogLike < Min_LogLike)
        {
          Min_LogLike = LogLike;
        }
      }

      return Min_LogLike;
    }


    /// Interpolated Di-jet likelihoods from quark coupling upper limits
    /// This assumes the Narrow width approximation
    void DiJet_LogLike_DMsimp(double& result)
    {

      using namespace Pipes::DiJet_LogLike_DMsimp;

      static bool first = true;
      if (first)
      {
        fill_DMsimp_DiJets();
        first = false;
      }

      // Initialise to squash warning, these values will always be overwritten
      double mMed = 0.0;
      double gq = 0.0;

      // Pull Decay widths from CalcHEP
      DecayTable::Entry decays;

      // Get the theory spectrum to pass on masses and parameters
      if(ModelInUse("DMsimpVectorMedScalarDM"))
      {
        const Spectrum& spec = *Dep::DMsimpVectorMedScalarDM_spectrum;
        mMed = spec.get(Par::Pole_Mass, "Y1");
        gq   = spec.get(Par::dimensionless, "gVq");
        decays = *Dep::Y1_decay_rates;
      }
      else if(ModelInUse("DMsimpVectorMedMajoranaDM"))
      {
        const Spectrum& spec = *Dep::DMsimpVectorMedMajoranaDM_spectrum;
        mMed = spec.get(Par::Pole_Mass, "Y1");
        gq   = spec.get(Par::dimensionless, "gVq");
        decays = *Dep::Y1_decay_rates;
      }
      else if(ModelInUse("DMsimpVectorMedDiracDM"))
      {
        const Spectrum& spec = *Dep::DMsimpVectorMedDiracDM_spectrum;
        mMed = spec.get(Par::Pole_Mass, "Y1");
        gq   = spec.get(Par::dimensionless, "gVq");
        decays = *Dep::Y1_decay_rates;
      }
      else if(ModelInUse("DMsimpVectorMedVectorDM"))
      {
        const Spectrum& spec = *Dep::DMsimpVectorMedVectorDM_spectrum;
        mMed = spec.get(Par::Pole_Mass, "Y1");
        gq   = spec.get(Par::dimensionless, "gVq");
        decays = *Dep::Y1_decay_rates;
      }
      else
      {
        ColliderBit_error().raise(LOCAL_INFO, "ERROR! ColliderBit_InterpolatedYields: Cannot use DMsimp Dijet likelihood for this model.");
      }

      double total_width = decays.width_in_GeV;

      // The Branching ratio to quarks does not include top quarks
      double sum_BR_observed = decays.BF("ubar_1", "u_1") + decays.BF("ubar_2", "u_2") + decays.BF("dbar_3", "d_3") + decays.BF("dbar_1", "d_1") + decays.BF("dbar_2", "d_2");
      double sum_BR_nonobserved = decays.BF("ubar_3", "u_3");

      if(ModelInUse("DMsimpVectorMedScalarDM"))
      {
        sum_BR_nonobserved += decays.BF("Xc~", "Xc");
      }
      else if(ModelInUse("DMsimpVectorMedMajoranaDM"))
      {
        sum_BR_nonobserved += decays.BF("Xm", "Xm");
      }
      else if(ModelInUse("DMsimpVectorMedDiracDM"))
      {
        sum_BR_nonobserved += decays.BF("Xd~", "Xd");
      }
      else if(ModelInUse("DMsimpVectorMedVectorDM"))
      {
        sum_BR_nonobserved += decays.BF("~Xv", "~Xva");
      }
      double BR_q = sum_BR_observed / (sum_BR_observed + sum_BR_nonobserved);

      // Check that NWA is a reasonable choice (we choose this to be Width/Mass < 30%)
      if ((total_width/mMed) > 0.3)
      {
        Suspicious_point_exception().raise("Narrow Width Approximation breaks down.",30,false);
      }

      result = Total_DiJet_search_LogLike(mMed, gq, BR_q);

    }

    //// NEW BEAM-DUMP Functions ////

    /// A function for filling the analysis_info_map for the SubGeVDM_fermion and SubGeVDM_scalar models.
    void SubGeVDM_fill_analysis_info_map(std::map<str,str> Analysis_data_path, std::map<str,std::vector<str>> Interpolation_columns)
    {

      std::vector<str> default_skip_analyses;  // The default is empty lists of analyses to skip
      static const std::vector<str> skip_analyses = Pipes::calc_combined_LHC_LogLike::runOptions->getValueOrDef<std::vector<str> >(default_skip_analyses, "skip_analyses");

      // Helper variables
      str current_analysis_name;
      Model_analysis_info empty_analysis_info;
      Model_analysis_info* current_ainfo;


      // Analysis name
      current_analysis_name = "SubGeVBeamDump_MBe_interpolated";

      if (std::find(skip_analyses.begin(), skip_analyses.end(), current_analysis_name) == skip_analyses.end())
      {
        if (not(Utils::file_exists(Analysis_data_path[current_analysis_name])))
        {
          ColliderBit_error().raise(LOCAL_INFO, "ERROR! Cannot find interpolation data file: " + Analysis_data_path[current_analysis_name]);
        }

        // Create an entry in the global analysis_info_map and point the reference current_ainfo to it
        analysis_info_map[current_analysis_name] = Model_analysis_info();
        current_ainfo = &(analysis_info_map[current_analysis_name]);
        fill_analysis_info_map(current_analysis_name, current_ainfo);
        current_ainfo->add_interp2d("SubGeVBeamDump", Analysis_data_path[current_analysis_name], Interpolation_columns[current_analysis_name]);

        current_ainfo = &empty_analysis_info;
      }

      // Analysis name
      current_analysis_name = "SubGeVBeamDump_MBN_interpolated";

      if (std::find(skip_analyses.begin(), skip_analyses.end(), current_analysis_name) == skip_analyses.end())
      {
        if (not(Utils::file_exists(Analysis_data_path[current_analysis_name])))
        {
          ColliderBit_error().raise(LOCAL_INFO, "ERROR! Cannot find interpolation data file: " + Analysis_data_path[current_analysis_name]);
        }

        // Create an entry in the global analysis_info_map and point the reference current_ainfo to it
        analysis_info_map[current_analysis_name] = Model_analysis_info();
        current_ainfo = &(analysis_info_map[current_analysis_name]);
        fill_analysis_info_map(current_analysis_name, current_ainfo);
        current_ainfo->add_interp2d("SubGeVBeamDump", Analysis_data_path[current_analysis_name], Interpolation_columns[current_analysis_name]);

        current_ainfo = &empty_analysis_info;
      }

      // Analysis name
      current_analysis_name = "SubGeVBeamDump_LSND_interpolated";

      if (std::find(skip_analyses.begin(), skip_analyses.end(), current_analysis_name) == skip_analyses.end())
      {
        if (not(Utils::file_exists(Analysis_data_path[current_analysis_name])))
        {
          ColliderBit_error().raise(LOCAL_INFO, "ERROR! Cannot find interpolation data file: " + Analysis_data_path[current_analysis_name]);
        }

        // Create an entry in the global analysis_info_map and point the reference current_ainfo to it
        analysis_info_map[current_analysis_name] = Model_analysis_info();
        current_ainfo = &(analysis_info_map[current_analysis_name]);
        fill_analysis_info_map(current_analysis_name, current_ainfo);
        current_ainfo->add_interp2d("SubGeVBeamDump", Analysis_data_path[current_analysis_name], Interpolation_columns[current_analysis_name]);

        current_ainfo = &empty_analysis_info;
      }

      // Analysis name
      current_analysis_name = "SubGeVBeamDump_NA64_interpolated";

      if (std::find(skip_analyses.begin(), skip_analyses.end(), current_analysis_name) == skip_analyses.end())
      {
        if (not(Utils::file_exists(Analysis_data_path[current_analysis_name])))
        {
          ColliderBit_error().raise(LOCAL_INFO, "ERROR! Cannot find interpolation data file: " + Analysis_data_path[current_analysis_name]);
        }

        // Create an entry in the global analysis_info_map and point the reference current_ainfo to it
        analysis_info_map[current_analysis_name] = Model_analysis_info();
        current_ainfo = &(analysis_info_map[current_analysis_name]);
        fill_analysis_info_map(current_analysis_name, current_ainfo);
        current_ainfo->add_interp1d("SubGeVBeamDump", Analysis_data_path[current_analysis_name], Interpolation_columns[current_analysis_name]);

        current_ainfo = &empty_analysis_info;
      }

    }

    /// Results for the SubGeVDM_fermion and SubGeVDM_scalar model
    void SubGeVDM_results(AnalysisDataPointers& result)
    {
      using namespace Pipes::SubGeVDM_results;

      // Clear previous vectors, etc.
      result.clear();

      static bool first = true;

      // We need thread_local AnalysisData instances. Let's collect them in a map.
      thread_local std::map<str,AnalysisData> analysis_data_map;

      // Store the locations of monojet interpolation data files to pass to DMsimp_fill_analysis_info_map
      std::map<str,str> Analysis_data_path;
      std::map<str,std::vector<str>> Interpolation_columns;

      if(ModelInUse("SubGeVDM_scalar"))
      {
        Analysis_data_path["SubGeVBeamDump_MBe_interpolated"] = GAMBIT_DIR "/ColliderBit/data/SubGeVDM/BeamDump/MB_electron_scalarDM_NEvents.txt";
        Analysis_data_path["SubGeVBeamDump_MBN_interpolated"] = GAMBIT_DIR "/ColliderBit/data/SubGeVDM/BeamDump/MB_nucleon_scalarDM_NEvents.txt";
        Analysis_data_path["SubGeVBeamDump_LSND_interpolated"] = GAMBIT_DIR "/ColliderBit/data/SubGeVDM/BeamDump/LSND_scalarDM_NEvents.txt";
        Analysis_data_path["SubGeVBeamDump_NA64_interpolated"] = GAMBIT_DIR "/ColliderBit/data/SubGeVDM/BeamDump/NA64_2023.txt";

        Interpolation_columns["SubGeVBeamDump_MBe_interpolated"] = {"mDM","mAp","signal_counts"};
        Interpolation_columns["SubGeVBeamDump_MBN_interpolated"] = {"mDM","mAp","signal_counts"};
        Interpolation_columns["SubGeVBeamDump_LSND_interpolated"] = {"mDM","mAp","signal_counts"};
        Interpolation_columns["SubGeVBeamDump_NA64_interpolated"] = {"mAp","epsilon"};
      }
      else if(ModelInUse("SubGeVDM_fermion"))
      {
        Analysis_data_path["SubGeVBeamDump_MBe_interpolated"] = GAMBIT_DIR "/ColliderBit/data/SubGeVDM/BeamDump/MB_electron_fermionDM_NEvents.txt";
        Analysis_data_path["SubGeVBeamDump_MBN_interpolated"] = GAMBIT_DIR "/ColliderBit/data/SubGeVDM/BeamDump/MB_nucleon_fermionDM_NEvents.txt";
        Analysis_data_path["SubGeVBeamDump_LSND_interpolated"] = GAMBIT_DIR "/ColliderBit/data/SubGeVDM/BeamDump/LSND_fermionDM_NEvents.txt";
        Analysis_data_path["SubGeVBeamDump_NA64_interpolated"] = GAMBIT_DIR "/ColliderBit/data/SubGeVDM/BeamDump/NA64_2023.txt";

        Interpolation_columns["SubGeVBeamDump_MBe_interpolated"] = {"mDM","mAp","signal_counts"};
        Interpolation_columns["SubGeVBeamDump_MBN_interpolated"] = {"mDM","mAp","signal_counts"};
        Interpolation_columns["SubGeVBeamDump_LSND_interpolated"] = {"mDM","mAp","signal_counts"};
        Interpolation_columns["SubGeVBeamDump_NA64_interpolated"] = {"mAp","epsilon"};
      }
      else
      {
        ColliderBit_error().raise(LOCAL_INFO, "ERROR! Model not known to GAMBIT");
      }


      // The first time this function is run we must initialize the global analysis_info_map
      // and the thread_local analysis_data_map
      if (first)
      {
        SubGeVDM_fill_analysis_info_map(Analysis_data_path,Interpolation_columns);

        for (const std::pair<const str, Model_analysis_info>& aname_ainfo_pair : analysis_info_map)
        {
          // Extract analysis name and use it to create an AnalysisData element in the analysis_data_map
          str aname = aname_ainfo_pair.first;
          analysis_data_map[aname] = AnalysisData(aname);
        }

        first = false;
      }

      // Retrieve the signal yields
      const Spectrum& spec = *Dep::SubGeVDM_spectrum;
      str modelname;
      if(ModelInUse("SubGeVDM_scalar"))
        modelname = "SubGeVDM_scalar";
      else if(ModelInUse("SubGeVDM_fermion"))
        modelname = "SubGeVDM_fermion";
      get_all_signal_yields(get_all_SubGeVDM_signal_yields, spec, analysis_data_map, result, modelname);

    }

    /// Fill the input vector with the total SubGeV signal prediction for each SR in the given analysis
    void get_all_SubGeVDM_signal_yields(std::vector<double>& sr_nums, const Model_analysis_info& analysis_info, const Spectrum& spec, str& modelname)
    {

      // Get the yields
      std::vector<double> signal(analysis_info.n_signal_regions, 0.);

      // Get the parameters we need from the theory spectrum
      if(modelname == "SubGeVDM_scalar")
      {
        // TODO: If your model has more/less than 2 masses and 2 couplings, then the get_SubGeVBeamDump_MB_signal_yields function will need to be changed.
        // TODO: Would need to change mass_i and coupling_i to the relevant parameters in your model
        double mDM = spec.get(Par::Pole_Mass, "DM");
        double mAp = spec.get(Par::Pole_Mass, "Ap");
        double kappa = spec.get(Par::dimensionless, "kappa");
        double gDM = spec.get(Par::dimensionless, "gDM");
        get_SubGeVDM_scalar_signal_yields(signal, analysis_info, mDM, mAp, kappa, gDM);

        double mApmdm_ratio = mAp/mDM;
        if (mApmdm_ratio <= 2.)
          ColliderBit_error().raise(LOCAL_INFO, "ERROR! mAp/mdm <= 2., in off-shell regime"); // beam dump yield will just return 0
      }
      else if(modelname == "SubGeVDM_fermion")
      {
        double mDM = spec.get(Par::Pole_Mass, "DM");
        double mAp = spec.get(Par::Pole_Mass, "Ap");
        double kappa = spec.get(Par::dimensionless, "kappa");
        double gDM = spec.get(Par::dimensionless, "gDM");
        get_SubGeVDM_fermion_signal_yields(signal, analysis_info, mDM, mAp, kappa, gDM);

        double mApmdm_ratio = mAp/mDM;
        if (mApmdm_ratio <= 2.)
          ColliderBit_error().raise(LOCAL_INFO, "ERROR! mAp/mdm <= 2., in off-shell regime"); // beam dump yield will just return 0
      }
      // Add yields and save in sr_num
      for (size_t i = 0; i < analysis_info.n_signal_regions; ++i)
      {
        sr_nums[i] = signal[i];
      }
    }

    /// Fill the input vector with the signal prediction for the SubGeVBeamDump_MB model
    /// TODO: If you apply some scaling based on couplings, then this is where you would want to do this
    void get_SubGeVDM_scalar_signal_yields(std::vector<double>& signal_yields, const Model_analysis_info& analysis_info, double mDM, double mAp, double kappa, double gDM)
    {
      double signalcounts = 0.;

      // SubGeVBeamDump contains both 1d and 2d interpolators, check which one this is
      if(analysis_info.has_interp1d("SubGeVBeamDump"))
      {
        // Get the interpolator collections for the given operator_key
        const Utils::interp1d_gsl_collection& eps_interp = analysis_info.get_interp1d("SubGeVBeamDump");

        // If values are outside bounds give zero signal
        if(eps_interp.is_inside_range(mAp))
        {
          // Compute the signal
          // Note: The last entry in this function is the index of the column (minus the number of free params, i.e. 2)
          double kappa_interp = eps_interp.eval(mAp, 0); // mAp and eps

          double me = 0.000511; // mass of electron
          double mmu = 0.1057; // mass of muon
          double ee = 0.31343; // elementary charge
          double width_ff = 0.0;
          if (mAp > 2*me) {width_ff += pow(kappa*ee,2) * (4*pow(mAp,2)+8*pow(me,2))*sqrt(pow(mAp,2)/4-pow(me,2)) / (24*pi*pow(mAp,2));}
          if (mAp > 2*mmu) {width_ff += pow(kappa*ee,2) * (4*pow(mAp,2)+8*pow(mmu,2))*sqrt(pow(mAp,2)/4-pow(mmu,2)) / (24*pi*pow(mAp,2));}
          double width_XXscalar = pow(gDM,2)*(pow(mAp,2)-4*pow(mDM,2))/(8*pi*pow(mAp,2))*sqrt(pow(mAp,2)/4-pow(mDM,2));
        //// Gamma_VtoXX / (Gamma_VtoXX + Gamma_Vtoff)
          double BR_scalarDM  = width_XXscalar / (width_XXscalar + width_ff); // Branching ratio for scalar DM


          signalcounts = pow(kappa,2) / (pow(kappa_interp,2)) * 2.3 * BR_scalarDM;
        }

      }
      else if(analysis_info.has_interp2d("SubGeVBeamDump"))
      {
        const Utils::interp2d_gsl_collection& signal_interp = analysis_info.get_interp2d("SubGeVBeamDump");

        // If values are outside bounds give zero signal
        double signal = 0.;
        if(signal_interp.is_inside_range(mDM, mAp))
        {
          // Compute the signal
          // Note: The last entry in this function is the index of the column (minus the number of free params, i.e. 2)
          signal = signal_interp.eval(mDM, mAp, 0); // mdm and mAp
        }

        // TODO: After interpolating the signal, apply any scaling, etc that you intend to.
        double kappa_simulated  = 1e-4; // epsilon value which the data was simulated with
        double gDM_simulated    = 2.5;  // gD (dark coupling between A' and DM) value which the data was simulated with

        // TODO: change to values in numerical constants
        double me = 0.000511; // mass of electron
        double mmu = 0.1057; // mass of muon
        double ee = 0.31343; // elementary charge


        double width_ff = 0.0;
        if (mAp > 2*me) {width_ff += pow(kappa*ee,2) * (4*pow(mAp,2)+8*pow(me,2))*sqrt(pow(mAp,2)/4-pow(me,2)) / (24*pi*pow(mAp,2));}
        if (mAp > 2*mmu) {width_ff += pow(kappa*ee,2) * (4*pow(mAp,2)+8*pow(mmu,2))*sqrt(pow(mAp,2)/4-pow(mmu,2)) / (24*pi*pow(mAp,2));}

        double width_XXscalar = pow(gDM,2)*(pow(mAp,2)-4*pow(mDM,2))/(8*pi*pow(mAp,2))*sqrt(pow(mAp,2)/4-pow(mDM,2));

        //// Gamma_VtoXX / (Gamma_VtoXX + Gamma_Vtoff)
        double BR_scalarDM  = width_XXscalar / (width_XXscalar + width_ff); // Branching ratio for scalar DM
        signalcounts = signal * pow(kappa/kappa_simulated,4) * pow(gDM/gDM_simulated,2) * BR_scalarDM;

      }

      for (size_t sr_i = 0; sr_i < analysis_info.n_signal_regions; ++sr_i)
      {
        signal_yields[sr_i] = signalcounts;
      }
    }

    void get_SubGeVDM_fermion_signal_yields(std::vector<double>& signal_yields, const Model_analysis_info& analysis_info, double mDM, double mAp, double kappa, double gDM)
    {
      double signalcounts = 0.;

      // SubGeVBeamDump contains both 1d and 2d interpolators, check which one this is
      if(analysis_info.has_interp1d("SubGeVBeamDump"))
      {
        // Get the interpolator collections for the given operator_key
        const Utils::interp1d_gsl_collection& eps_interp = analysis_info.get_interp1d("SubGeVBeamDump");

        // If values are outside bounds give zero signal
        if(eps_interp.is_inside_range(mAp))
        {
          // Compute the signal
          // Note: The last entry in this function is the index of the column (minus the number of free params, i.e. 2)
          double kappa_interp = eps_interp.eval(mAp, 0); // mAp and eps

        double me = 0.000511; // mass of electron
        double mmu = 0.1057; // mass of muon
        double ee = 0.31343; // elementary charge
        double width_ff = 0.0;
        if (mAp > 2*me) {width_ff += pow(kappa*ee,2) * (4*pow(mAp,2)+8*pow(me,2))*sqrt(pow(mAp,2)/4-pow(me,2)) / (24*pi*pow(mAp,2));}
        if (mAp > 2*mmu) {width_ff += pow(kappa*ee,2) * (4*pow(mAp,2)+8*pow(mmu,2))*sqrt(pow(mAp,2)/4-pow(mmu,2)) / (24*pi*pow(mAp,2));}

        double width_XXfermion = pow(gDM,2)/3 * (4*pow(mAp,2)+8*pow(mDM,2)) * sqrt(pow(mAp,2)/4 - pow(mDM,2))/(8*pi*pow(mAp,2));
        //// Gamma_VtoXX / (Gamma_VtoXX + Gamma_Vtoff)
        double BR_fermionDM  = width_XXfermion / (width_XXfermion + width_ff); // Branching ratio for dirac fermion DM

          signalcounts = pow(kappa,2) / (pow(kappa_interp,2)) * 2.3 * BR_fermionDM;
        }
      }

      else if(analysis_info.has_interp2d("SubGeVBeamDump"))
      {
        // Get the interpolator collections for the given operator_key
        const Utils::interp2d_gsl_collection& signal_interp = analysis_info.get_interp2d("SubGeVBeamDump");

        // If values are outside bounds give zero signal
        double signal = 0.;
        if(signal_interp.is_inside_range(mDM, mAp))
        {
          // Compute the signal
          // Note: The last entry in this function is the index of the column (minus the number of free params, i.e. 2)
          signal = signal_interp.eval(mDM, mAp, 0); // mdm and mAp
        }

        // TODO: After interpolating the signal, apply any scaling, etc that you intend to.
        double kappa_simulated  = 1e-4; // epsilon value which the data was simulated with
        double gDM_simulated    = 2.5;  // gD (dark coupling between A' and DM) value which the data was simulated with

        // TODO: change to values in numerical constants
        double me = 0.000511; // mass of electron
        double mmu = 0.1057; // mass of muon
        double ee = 0.31343; // elementary charge


        double width_ff = 0.0;
        if (mAp > 2*me) {width_ff += pow(kappa*ee,2) * (4*pow(mAp,2)+8*pow(me,2))*sqrt(pow(mAp,2)/4-pow(me,2)) / (24*pi*pow(mAp,2));}
        if (mAp > 2*mmu) {width_ff += pow(kappa*ee,2) * (4*pow(mAp,2)+8*pow(mmu,2))*sqrt(pow(mAp,2)/4-pow(mmu,2)) / (24*pi*pow(mAp,2));}

        double width_XXfermion = pow(gDM,2)/3 * (4*pow(mAp,2)+8*pow(mDM,2)) * sqrt(pow(mAp,2)/4 - pow(mDM,2))/(8*pi*pow(mAp,2));

        //// Gamma_VtoXX / (Gamma_VtoXX + Gamma_Vtoff)
        double BR_fermionDM  = width_XXfermion / (width_XXfermion + width_ff); // Branching ratio for dirac fermion DM

        signalcounts = signal * pow(kappa/kappa_simulated,4) * pow(gDM/gDM_simulated,2) * BR_fermionDM;
      }

      for (size_t sr_i = 0; sr_i < analysis_info.n_signal_regions; ++sr_i)
      {
        signal_yields[sr_i] = signalcounts;
      }
    }

  } // namespace ColliderBit

} // namespace Gambit
```


-------------------------------

Updated on 2025-02-12 at 16:10:36 +0000
