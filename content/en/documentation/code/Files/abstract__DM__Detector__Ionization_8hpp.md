---
title: "file obscura_1_1_0/abstract_DM_Detector_Ionization.hpp"

description: "[No description available]"

---

# file obscura_1_1_0/abstract_DM_Detector_Ionization.hpp

[No description available]

## Functions

|                | Name           |
| -------------- | -------------- |
| namespace | **[CAT_3](/documentation/code/files/abstract__dm__detector__ionization_8hpp/#function-cat-3)**(BACKENDNAME , _ , SAFE_VERSION ) |


## Functions Documentation

### function CAT_3

```
namespace CAT_3(
    BACKENDNAME ,
    _ ,
    SAFE_VERSION 
)
```




## Source code

```
#ifndef __abstract_DM_Detector_Ionization_obscura_1_1_0_hpp__
#define __abstract_DM_Detector_Ionization_obscura_1_1_0_hpp__

#include <cstddef>
#include <iostream>
#include <vector>
#include <string>
#include "gambit/Backends/abstractbase.hpp"
#include "forward_decls_abstract_classes.hpp"
#include "forward_decls_wrapper_classes.hpp"
#include "wrapper_DM_Particle_decl.hpp"
#include "wrapper_DM_Distribution_decl.hpp"
#include "wrapper_DM_Detector_decl.hpp"

#include "identification.hpp"

namespace CAT_3(BACKENDNAME,_,SAFE_VERSION)
{
    
    
    namespace obscura
    {
        class Abstract_DM_Detector_Ionization : virtual public obscura::Abstract_DM_Detector
        {
            public:
    
                virtual double Maximum_Energy_Deposit__BOSS(obscura::Abstract_DM_Particle&, const obscura::Abstract_DM_Distribution&) const =0;
    
                virtual double Minimum_DM_Speed__BOSS(obscura::Abstract_DM_Particle&) const =0;
    
                virtual double Minimum_DM_Mass__BOSS(obscura::Abstract_DM_Particle&, const obscura::Abstract_DM_Distribution&) const =0;
    
                virtual double dRdE__BOSS(double, const obscura::Abstract_DM_Particle&, obscura::Abstract_DM_Distribution&) =0;
    
                virtual double DM_Signals_Total__BOSS(const obscura::Abstract_DM_Particle&, obscura::Abstract_DM_Distribution&) =0;
    
                virtual ::std::vector<double> DM_Signals_Binned__BOSS(const obscura::Abstract_DM_Particle&, obscura::Abstract_DM_Distribution&) =0;
    
                virtual double R_ne__BOSS(unsigned int, const obscura::Abstract_DM_Particle&, obscura::Abstract_DM_Distribution&) =0;
    
                virtual void Use_Electron_Threshold(unsigned int, unsigned int) =0;
    
                virtual void Use_Electron_Threshold__BOSS(unsigned int) =0;
    
                virtual void Use_Electron_Bins(unsigned int, unsigned int) =0;
    
                virtual double R_S2__BOSS(unsigned int, const obscura::Abstract_DM_Particle&, obscura::Abstract_DM_Distribution&, std::vector<double>) =0;
    
                virtual double R_S2__BOSS(unsigned int, const obscura::Abstract_DM_Particle&, obscura::Abstract_DM_Distribution&) =0;
    
                virtual void Use_PE_Threshold(double, double, unsigned int, unsigned int) =0;
    
                virtual void Import_Trigger_Efficiency_PE(std::string) =0;
    
                virtual void Import_Acceptance_Efficiency_PE(std::string) =0;
    
                virtual void Use_PE_Bins(double, double, const std::vector<unsigned int>&) =0;
    
                virtual void Print_Summary(int) const =0;
    
                virtual void Print_Summary__BOSS() const =0;
    
            public:
                using obscura::Abstract_DM_Detector::pointer_assign__BOSS;
                virtual void pointer_assign__BOSS(Abstract_DM_Detector_Ionization*) =0;
                virtual Abstract_DM_Detector_Ionization* pointer_copy__BOSS() =0;
    
            private:
                DM_Detector_Ionization* wptr;
                bool delete_wrapper;
            public:
                DM_Detector_Ionization* get_wptr() { return wptr; }
                void set_wptr(DM_Detector_Ionization* wptr_in) { wptr = wptr_in; }
                bool get_delete_wrapper() { return delete_wrapper; }
                void set_delete_wrapper(bool del_wrp_in) { delete_wrapper = del_wrp_in; }
    
            public:
                Abstract_DM_Detector_Ionization()
                {
                    wptr = 0;
                    delete_wrapper = false;
                }
    
                Abstract_DM_Detector_Ionization(const Abstract_DM_Detector_Ionization& in) : 
                    obscura::Abstract_DM_Detector(in)
                {
                    wptr = 0;
                    delete_wrapper = false;
                }
    
                Abstract_DM_Detector_Ionization& operator=(const Abstract_DM_Detector_Ionization&) { return *this; }
    
                virtual void init_wrapper() =0;
    
                DM_Detector_Ionization* get_init_wptr()
                {
                    init_wrapper();
                    return wptr;
                }
    
                DM_Detector_Ionization& get_init_wref()
                {
                    init_wrapper();
                    return *wptr;
                }
    
                virtual ~Abstract_DM_Detector_Ionization() =0;
        };
    }
    
}


#include "gambit/Backends/backend_undefs.hpp"


#endif /* __abstract_DM_Detector_Ionization_obscura_1_1_0_hpp__ */
```


-------------------------------

Updated on 2024-07-18 at 13:53:35 +0000
