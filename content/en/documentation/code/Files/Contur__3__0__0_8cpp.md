---
title: "file frontends/Contur_3_0_0.cpp"

description: "[No description available]"

---

# file frontends/Contur_3_0_0.cpp

[No description available] [More...](#detailed-description)

## Detailed Description


**Author**: 

  * Tomas Gonzalo ([tomas.gonzalo@monash.edu](mailto:tomas.gonzalo@monash.edu)) 
  * Tomasz Procter ([t.procter.1@research.gla.ac.uk](mailto:t.procter.1@research.gla.ac.uk)) 
  * Anders Kvellestad ([anders.kvellestad@fys.uio.no](mailto:anders.kvellestad@fys.uio.no)) 


**Date**: 

  * 2019 Oct
  * 2021 June 
  * 2023 May 
  * 2024 Oct
  * 2023 Feb


Fronted source for the Contur backend



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Fronted source for the Contur backend
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Tomas Gonzalo
///          (tomas.gonzalo@monash.edu)
///  \date 2019 Oct
///
/// \author Tomasz Procter
///          (t.procter.1@research.gla.ac.uk)
/// \date 2021 June
/// \date 2023 May
/// \date  2024 Oct
///
/// \author Anders Kvellestad
///          (anders.kvellestad@fys.uio.no)
/// \date 2023 Feb
///
///  *********************************************

#include "gambit/Backends/frontend_macros.hpp"
#include "gambit/Backends/frontends/Contur_3_0_0.hpp"

#ifdef HAVE_PYBIND11

  using namespace pybind11::literals;

  BE_NAMESPACE
  {

    // Helper function for setting some default arguments for Contur.
    // Used by the functions Contur_LogLike_from_stream and Contur_LogLike_from_file below.
    void Contur_add_GAMBIT_default_args(pybind11::dict& args_dict)
    {
      args_dict[pybind11::cast("QUIET")] = pybind11::bool_(true);
      args_dict[pybind11::cast("NOMULTIP")] = pybind11::bool_(true);
      args_dict[pybind11::cast("YODASTREAM_API_OUTPUT_OPTIONS")] = pybind11::list();
      args_dict[pybind11::cast("YODASTREAM_API_OUTPUT_OPTIONS")].attr("append")("LLR");
      args_dict[pybind11::cast("YODASTREAM_API_OUTPUT_OPTIONS")].attr("append")("Pool_LLR");
      args_dict[pybind11::cast("YODASTREAM_API_OUTPUT_OPTIONS")].attr("append")("Pool_tags");
    }


    Contur_output Contur_LogLike_from_stream(std::shared_ptr<std::ostringstream> yodastream, std::vector<std::string>& contur_yaml_args)
    {
      //Convert C++ ostringstream to python StringIO
      pybind11::str InputString = pybind11::cast(yodastream->str());
      pybind11::object yoda_string_IO = Contur.attr("StringIO")(InputString);
      yoda_string_IO.attr("seek")(pybind11::int_(pybind11::cast(0)));

      // Get default settings for Contur run and add a couple of our own as defaults for GAMBIT
      pybind11::dict args_dict = 
        ((Contur.attr("arg_utils").attr("get_argparser")(pybind11::cast("analysis"))).attr(
          "parse_args")(pybind11::cast(contur_yaml_args))).attr("__dict__");
      args_dict[pybind11::cast("YODASTREAM")] = yoda_string_IO;

      Contur_add_GAMBIT_default_args(args_dict);

      //Return the contur output.
      return Contur_output(Contur.attr("run_analysis").attr("main")(args_dict));
    }


    Contur_output Contur_LogLike_from_file(str& YODA_filename, std::vector<std::string>& contur_yaml_args)
    {
      // Get default settings for Contur run and add a couple of our own as defaults for GAMBIT
      pybind11::dict args_dict = 
        ((Contur.attr("arg_utils").attr("get_argparser")(pybind11::cast("analysis"))).attr(
          "parse_args")(pybind11::cast(contur_yaml_args))).attr("__dict__");
      args_dict[pybind11::cast("YODASTREAM")] = YODA_filename;

      Contur_add_GAMBIT_default_args(args_dict);

      //Run contur, get a LLR and return it
      return Contur_output(Contur.attr("run_analysis").attr("main")(args_dict));
    }


    //Appends all analyses at given beamString (e.g. 13TeV) that contur knows about to the lit of analyses
    //to study.
    void Contur_get_analyses_from_beam(std::vector<std::string>& analyses, std::string& beamString)
    {
      pybind11::list beams;
      pybind11::object theBeam;
      bool beamFound = false;
      #pragma omp critical
      {
        beams = Contur.attr("static_db").attr("get_beams")();
      }
      for (size_t  i = 0; i <= pybind11::len(beams); ++i){
        if (beams[i].attr("id").cast<std::string>() == beamString){
          theBeam = beams[i];
          beamFound = true;
          break;
        }
      }
      if (! beamFound ){
        // TODO: give appropriate warning that we're returning an empty vector.
        analyses = {};
        return;
      }
      # pragma omp critical
      {
        pybind11::list anaObjectList = Contur.attr("static_db").attr("get_analyses")(pybind11::none(), pybind11::none(), theBeam);
        for (const pybind11::handle anaObject : anaObjectList){
          analyses.push_back(anaObject.attr("name").cast<str>());
        }
      }
      
    }
  }
  END_BE_NAMESPACE

#endif

BE_INI_FUNCTION
{}
END_BE_INI_FUNCTION
```


-------------------------------

Updated on 2026-11-03 at 14:50:49 +0000
