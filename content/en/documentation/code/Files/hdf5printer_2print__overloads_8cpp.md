---
title: "file hdf5printer/hdf5printer/print_overloads.cpp"

description: "[No description available]"

---

# file hdf5printer/hdf5printer/print_overloads.cpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::Printers](/documentation/code/namespaces/namespacegambit_1_1printers/)** <br>Forward declaration.  |

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[PRINT](/documentation/code/files/hdf5printer_2print__overloads_8cpp/#define-print)**(TYPE) <br>Templatable print functions.  |
|  | **[PRINTAS](/documentation/code/files/hdf5printer_2print__overloads_8cpp/#define-printas)**(INTYPE, OUTTYPE)  |

## Detailed Description


**Author**: 

  * Ben Farmer ([benjamin.farmer@fysik.su.se](mailto:benjamin.farmer@fysik.su.se)) 
  * Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 


**Date**: 

  * 2015 May
  * 2017 March


HDF5 interface printer class print function overloads. Add a new overload of the _print function in this file if you want to be able to print a new type.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define PRINT

```
#define PRINT(
    TYPE
)
       _print(TYPE const& value, const std::string& label, const int vID, const uint rank, const ulong pID) \
       { template_print(value,label,vID,rank,pID); }
```

Templatable print functions. 

PRINT FUNCTIONS Need to define one of these for every type we want to print! 


### define PRINTAS

```
#define PRINTAS(
    INTYPE,
    OUTTYPE
)
    _print(INTYPE const& value, const std::string& label, const int vID, const uint rank, const ulong pID) \
    { template_print((OUTTYPE)value,label,vID,rank,pID); }
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  HDF5 interface printer class print function
///  overloads.  Add a new overload of the _print
///  function in this file if you want to be able
///  to print a new type.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Ben Farmer
///          (benjamin.farmer@fysik.su.se)
///  \date 2015 May
///
///  \author Pat Scott
///          (p.scott@imperial.ac.uk)
///  \date 2017 March
///
///  *********************************************


#include "gambit/Printers/printers/hdf5printer.hpp"
#include "gambit/Printers/printers/common_print_overloads.hpp"


namespace Gambit
{
  namespace Printers
  {

    /// @{ PRINT FUNCTIONS
    /// Need to define one of these for every type we want to print!

    /// Templatable print functions
    #define PRINT(TYPE) _print(TYPE const& value, const std::string& label, const int vID, const uint rank, const ulong pID) \
       { template_print(value,label,vID,rank,pID); }
    void HDF5Printer::PRINT(int      )
    void HDF5Printer::PRINT(uint     )
    void HDF5Printer::PRINT(long     )
    void HDF5Printer::PRINT(ulong    )
    void HDF5Printer::PRINT(float    )
    void HDF5Printer::PRINT(double   )
    #undef PRINT

    #define PRINTAS(INTYPE,OUTTYPE) _print(INTYPE const& value, const std::string& label, const int vID, const uint rank, const ulong pID) \
    { template_print((OUTTYPE)value,label,vID,rank,pID); }
    void HDF5Printer::PRINTAS(longlong, long)
    void HDF5Printer::PRINTAS(ulonglong, ulong)
    #undef PRINTAS

    /// Bools can't quite use the template print function directly, since there
    /// are some issues with bools and MPI/HDF5 types. Easier to just convert
    /// the bool to an int first.
    void HDF5Printer::_print(bool const& value, const std::string& label, const int vID, const unsigned int mpirank, const unsigned long pointID)
    {
      unsigned int val_as_uint = value;
      template_print(val_as_uint,label,vID,mpirank,pointID);
    }

    void HDF5Printer::_print(std::vector<double> const& value, const std::string& label, const int vID, const unsigned int mpirank, const unsigned long pointID)
    {
      // We will write to several 'double' buffers, rather than a single vector buffer.
      // Change this once a vector buffer is actually available
      // Retrieve the buffer manager for buffers with the desired output type
      auto& buffer_manager = get_mybuffermanager<double>(pointID,mpirank);

#ifdef HDEBUG_MODE
      std::cout<<"printing vector<double>: "<<label<<std::endl;
      std::cout<<"pointID: "<<pointID<<", mpirank: "<<mpirank<<std::endl;
#endif

      for(unsigned int i=0;i<value.size();i++)
      {
        // Might want to find some way to avoid doing this every single loop, seems kind of wasteful.
        std::stringstream ss;
        ss<<label<<"["<<i<<"]";
        //labels.push_back(ss.str());

        // Write to each buffer
        //buffer_manager.get_buffer(vID, i, ss.str()).append(value[i]);
        PPIDpair ppid(pointID,mpirank);
        if(synchronised)
        {
          // Write the data to the selected buffer ("just works" for simple numeric types)
          buffer_manager.get_buffer(vID, i, ss.str()).append(value[i],ppid);
        }
        else
        {
          // Queue up a desynchronised ("random access") dataset write to previous scan iteration
          if(not seen_PPID_before(ppid))
          {
            add_PPID_to_list(ppid);
          }
          buffer_manager.get_buffer(vID, i, ss.str()).RA_write(value[i],ppid,primary_printer->global_index_lookup);
        }
      }
    }

    void HDF5Printer::_print(const map_str_dbl& map, const std::string& label, const int vID, const unsigned int mpirank, const unsigned long pointID)
    {
      // Retrieve the buffer manager for buffers with this type
      auto& buffer_manager = get_mybuffermanager<double>(pointID,mpirank);

      unsigned int i=0; // index for each buffer
      for (map_str_dbl::const_iterator it = map.begin(); it != map.end(); it++)
      {
        std::stringstream ss;
        ss<<label<<"::"<<it->first;
        PPIDpair ppid(pointID,mpirank);
        if(synchronised)
        {
          // Write the data to the selected buffer ("just works" for simple numeric types)
          buffer_manager.get_buffer(vID, i, ss.str()).append(it->second,ppid);
        }
        else
        {
          // Queue up a desynchronised ("random access") dataset write to previous scan iteration
          if(not seen_PPID_before(ppid))
          {
            add_PPID_to_list(ppid);
          }
          buffer_manager.get_buffer(vID, i, ss.str()).RA_write(it->second,ppid,primary_printer->global_index_lookup);
        }
        i++;
      }
    }

    void HDF5Printer::_print(const map_str_str& map, const std::string& label, const int vID, const unsigned int mpirank, const unsigned long pointID)
    {
      // Retrieve the buffer manager for buffers with this type
      auto& buffer_manager = get_mybuffermanager<double>(pointID,mpirank);

      unsigned int i=0; // index for each buffer
      for (std::map<std::string, std::string>::const_iterator
           it = map.begin(); it != map.end(); it++)
      {
        std::stringstream ss;
        ss<<label<<"::"<<it->first<<":"<<it->second;
        PPIDpair ppid(pointID,mpirank);
        // Write to each buffer
        //buffer_manager.get_buffer(vID, i, ss.str()).append(it->second);
        if(synchronised)
        {
          // Write the data to the selected buffer ("just works" for simple numeric types)
          buffer_manager.get_buffer(vID, i, ss.str()).append(0.0,ppid);
        }
        else
        {
          // Queue up a desynchronised ("random access") dataset write to previous scan iteration
          if(not seen_PPID_before(ppid))
          {
            add_PPID_to_list(ppid);
          }
          buffer_manager.get_buffer(vID, i, ss.str()).RA_write(0.0,ppid,primary_printer->global_index_lookup);
        }
        i++;
      }
    }

    void HDF5Printer::_print(map_str_map_str_dbl const& map, const std::string& label, const int vID, const unsigned int mpirank, const unsigned long pointID)
    {
      // Retrieve the buffer manager for buffers with this type
      auto& buffer_manager = get_mybuffermanager<double>(pointID,mpirank);

      unsigned int i=0; // index for each buffer
      for (map_str_map_str_dbl::const_iterator it = map.begin(); it != map.end(); it++)
      {
        std::stringstream ss;
        ss<<label<<"::"<<it->first;
        PPIDpair ppid(pointID,mpirank);
        for (map_str_dbl::const_iterator jt = it->second.begin(); jt != it->second.end(); jt++)
        {
          str s2 = ss.str() + "::" + jt->first;
          if(synchronised)
          {
            // Write the data to the selected buffer ("just works" for simple numeric types)
            buffer_manager.get_buffer(vID, i, s2).append(jt->second,ppid);
          }
          else
          {
            // Queue up a desynchronised ("random access") dataset write to previous scan iteration
            if(not seen_PPID_before(ppid))
            {
              add_PPID_to_list(ppid);
            }
            buffer_manager.get_buffer(vID, i, s2).RA_write(jt->second,ppid,primary_printer->global_index_lookup);
          }
          i++;
        }
      }
    }

    void HDF5Printer::_print(map_intpair_dbl const& map, const std::string& label, const int vID, const unsigned int mpirank, const unsigned long pointID)
    {
      // Retrieve the buffer manager for buffers with this type
      auto& buffer_manager = get_mybuffermanager<double>(pointID,mpirank);

      unsigned int i=0; // index for each buffer
      for (std::map<std::pair<int,int>, double>::const_iterator it = map.begin(); it != map.end(); it++)
      {
        std::stringstream ss;
        ss<<label<<"::"<<it->first;
        PPIDpair ppid(pointID,mpirank);
        if(synchronised)
        {
          // Write the data to the selected buffer ("just works" for simple numeric types)
          buffer_manager.get_buffer(vID, i, ss.str()).append(it->second,ppid);
        }
        else
        {
          // Queue up a desynchronised ("random access") dataset write to previous scan iteration
          if(not seen_PPID_before(ppid))
          {
            add_PPID_to_list(ppid);
          }
          buffer_manager.get_buffer(vID, i, ss.str()).RA_write(it->second,ppid,primary_printer->global_index_lookup);
        }
        i++;
      }
    }

    // Piggyback off existing print functions to build standard overloads
    USE_COMMON_PRINT_OVERLOAD(HDF5Printer, ModelParameters)
    USE_COMMON_PRINT_OVERLOAD(HDF5Printer, triplet<double>)
    USE_COMMON_PRINT_OVERLOAD(HDF5Printer, map_const_str_dbl)
    USE_COMMON_PRINT_OVERLOAD(HDF5Printer, map_const_str_map_const_str_dbl)
    USE_COMMON_PRINT_OVERLOAD(HDF5Printer, flav_prediction)
    #ifndef SCANNER_STANDALONE
      USE_COMMON_PRINT_OVERLOAD(HDF5Printer, DM_nucleon_couplings)
      USE_COMMON_PRINT_OVERLOAD(HDF5Printer, BBN_container)
    #endif

    /// @}

  }
}

#undef DBUG
#undef DEBUG_MODE
```


-------------------------------

Updated on 2025-02-12 at 16:10:34 +0000
