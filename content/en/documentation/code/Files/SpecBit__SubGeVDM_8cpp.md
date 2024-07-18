---
title: "file src/SpecBit_SubGeVDM.cpp"

description: "[No description available]"

---

# file src/SpecBit_SubGeVDM.cpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::SpecBit](/documentation/code/namespaces/namespacegambit_1_1specbit/)**  |

## Detailed Description


**Author**: Felix Kahlhoefer ([kahlhoefer@kit.edu](mailto:kahlhoefer@kit.edu)) 

**Date**: 2022 May

Functions of module SpecBit

SpecBit module functions related to the SubGeVDM model.



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Functions of module SpecBit
///
///  SpecBit module functions related to the
///  SubGeVDM model.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Felix Kahlhoefer
///          (kahlhoefer@kit.edu)
///  \date 2022 May
///
///  *********************************************

#include <string>
#include <sstream>

#include "gambit/Elements/gambit_module_headers.hpp"

#include "gambit/Elements/spectrum.hpp"
#include "gambit/Utils/stream_overloads.hpp"
#include "gambit/Utils/util_macros.hpp"

#include "gambit/SpecBit/SpecBit_rollcall.hpp"
#include "gambit/SpecBit/SpecBit_helpers.hpp"
#include "gambit/SpecBit/QedQcdWrapper.hpp"
#include "gambit/Models/SimpleSpectra/SMHiggsSimpleSpec.hpp"
#include "gambit/Models/SimpleSpectra/SubGeVDMSimpleSpec.hpp"

// Switch for debug mode
//#define SPECBIT_DEBUG

namespace Gambit
{

  namespace SpecBit
  {
    using namespace LogTags;

    /// Get a (simple) Spectrum object wrapper for the SubGeVDM model
    void get_SubGeVDM_spectrum(Spectrum& result)
    {
      using namespace Pipes::get_SubGeVDM_spectrum;
      const SMInputs& sminputs = *Dep::SMINPUTS;

      // Mass cut on the dark photon mass mAp >= 2 mDM
      bool dark_photon_mass_cut = runOptions->getValueOrDef<bool>(true, "dark_photon_mass_cut");
      if(dark_photon_mass_cut and *Param.at("mAp") < 2. * *Param.at("mDM"))
      {
        std::stringstream msg;
        msg << "Parameter point [mDM, mAp] = [" << *Param.at("mDM") << ", " << *Param.at("mAp") << "] is invalid. Dark photon mass must satisfy mAp >= 2 mDM. ";
        invalid_point().raise(msg.str());
      }

      // Initialise an object to carry the Singlet plus Higgs sector information
      Models::SubGeVDMModel SubGeVmodel;

      // quantities needed to fill container spectrum, intermediate calculations
      double alpha_em = 1.0 / sminputs.alphainv;
      double C = alpha_em * pi / (sminputs.GF * pow(2,0.5));
      double sinW2 = 0.5 - pow( 0.25 - C/pow(sminputs.mZ,2) , 0.5);
      double cosW2 = 0.5 + pow( 0.25 - C/pow(sminputs.mZ,2) , 0.5);
      double e = pow( 4*pi*( alpha_em ),0.5) ;

      double vev        = 1. / sqrt(sqrt(2.)*sminputs.GF);
      SubGeVmodel.vev        = vev;
      SubGeVmodel.SubGeV_DMPoleMass = *Param.at("mDM");
      SubGeVmodel.SubGeV_ApPoleMass = *Param.at("mAp");
      SubGeVmodel.SubGeV_gDM   = *Param.at("gDM");
      SubGeVmodel.SubGeV_kappa   = *Param.at("kappa");

      // Standard model
      SubGeVmodel.sinW2 = sinW2;

      // gauge couplings
      SubGeVmodel.g1 = sqrt(5/3) * e / sqrt(cosW2);
      SubGeVmodel.g2 = e / sqrt(sinW2);
      SubGeVmodel.g3   = pow( 4*pi*( sminputs.alphaS ),0.5) ;

      // Yukawas
      double sqrt2v = pow(2.0,0.5)/vev;
      SubGeVmodel.Yu[0] = sqrt2v * sminputs.mU;
      SubGeVmodel.Yu[1] = sqrt2v * sminputs.mCmC;
      SubGeVmodel.Yu[2] = sqrt2v * sminputs.mT;
      SubGeVmodel.Ye[0] = sqrt2v * sminputs.mE;
      SubGeVmodel.Ye[1] = sqrt2v * sminputs.mMu;
      SubGeVmodel.Ye[2] = sqrt2v * sminputs.mTau;
      SubGeVmodel.Yd[0] = sqrt2v * sminputs.mD;
      SubGeVmodel.Yd[1] = sqrt2v * sminputs.mS;
      SubGeVmodel.Yd[2] = sqrt2v * sminputs.mBmB;

      // Create a SubSpectrum object to wrap the EW sector information
      Models::SubGeVDMSimpleSpec SubGeVspec(SubGeVmodel);

      // Retrieve any mass cuts
      static const Spectrum::mc_info mass_cut = runOptions->getValueOrDef<Spectrum::mc_info>(Spectrum::mc_info(), "mass_cut");
      static const Spectrum::mr_info mass_ratio_cut = runOptions->getValueOrDef<Spectrum::mr_info>(Spectrum::mr_info(), "mass_ratio_cut");

      // We don't supply a LE subspectrum here; an SMSimpleSpec will therefore be automatically created from 'sminputs'
      result = Spectrum(SubGeVspec,sminputs,&Param,mass_cut,mass_ratio_cut);

    }

    // print spectrum out, stripped down copy from MSSM version with variable names changed
    void fill_map_from_SubGeVDM_spectrum(std::map<std::string,double>&, const Spectrum&);

    void get_SubGeVDM_spectrum_as_map (std::map<std::string,double>& specmap)
    {
      using namespace Pipes::get_SubGeVDM_spectrum_as_map;
      const Spectrum& SubGeVdmspec(*Dep::SubGeVDM_spectrum);
      fill_map_from_SubGeVDM_spectrum(specmap, SubGeVdmspec);
    }

    void fill_map_from_SubGeVDM_spectrum(std::map<std::string,double>& specmap, const Spectrum& SubGeVdmspec)
    {
      /// Add everything... use spectrum contents routines to automate task
      static const SpectrumContents::SubGeVDM contents;
      static const std::vector<SpectrumParameter> required_parameters = contents.all_parameters();

      for(std::vector<SpectrumParameter>::const_iterator it = required_parameters.begin();
           it != required_parameters.end(); ++it)
      {
         const Par::Tags        tag   = it->tag();
         const std::string      name  = it->name();
         const std::vector<int> shape = it->shape();

         /// Verification routine should have taken care of invalid shapes etc, so won't check for that here.

         // Check scalar case
         if(shape.size()==1 and shape[0]==1)
         {
           std::ostringstream label;
           label << name <<" "<< Par::toString.at(tag);
           specmap[label.str()] = SubGeVdmspec.get_HE().get(tag,name);
         }
         // Check vector case
         else if(shape.size()==1 and shape[0]>1)
         {
           for(int i = 1; i<=shape[0]; ++i) {
             std::ostringstream label;
             label << name <<"_"<<i<<" "<< Par::toString.at(tag);
             specmap[label.str()] = SubGeVdmspec.get_HE().get(tag,name,i);
           }
         }
         // Check matrix case
         else if(shape.size()==2)
         {
           for(int i = 1; i<=shape[0]; ++i) {
             for(int j = 1; j<=shape[0]; ++j) {
               std::ostringstream label;
               label << name <<"_("<<i<<","<<j<<") "<<Par::toString.at(tag);
               specmap[label.str()] = SubGeVdmspec.get_HE().get(tag,name,i,j);
             }
           }
         }
         // Deal with all other cases
         else
         {
           // ERROR
           std::ostringstream errmsg;
           errmsg << "Error, invalid parameter received while converting SubGeVDM_spectrum to map of strings! This should no be possible if the spectrum content verification routines were working correctly; they must be buggy, please report this.";
           errmsg << "Problematic parameter was: "<< tag <<", " << name << ", shape="<< shape;
           utils_error().forced_throw(LOCAL_INFO,errmsg.str());
         }
      }

    }

  } // end namespace SpecBit
} // end namespace Gambit
```


-------------------------------

Updated on 2024-07-18 at 13:53:32 +0000
