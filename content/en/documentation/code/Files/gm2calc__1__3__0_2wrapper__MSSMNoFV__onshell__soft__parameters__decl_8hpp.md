---
title: "file gm2calc_1_3_0/gm2calc_1_3_0/wrapper_MSSMNoFV_onshell_soft_parameters_decl.hpp"

description: "[No description available]"

---

# file gm2calc_1_3_0/gm2calc_1_3_0/wrapper_MSSMNoFV_onshell_soft_parameters_decl.hpp

[No description available]

## Functions

|                | Name           |
| -------------- | -------------- |
| namespace | **[CAT_3](/documentation/code/files/gm2calc__1__3__0_2wrapper__mssmnofv__onshell__soft__parameters__decl_8hpp/#function-cat-3)**(BACKENDNAME , _ , SAFE_VERSION ) |


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
#ifndef __wrapper_MSSMNoFV_onshell_soft_parameters_decl_gm2calc_1_3_0_hpp__
#define __wrapper_MSSMNoFV_onshell_soft_parameters_decl_gm2calc_1_3_0_hpp__

#include <cstddef>
#include <Eigen/Core>
#include <ostream>
#include "forward_decls_wrapper_classes.hpp"
#include "gambit/Backends/wrapperbase.hpp"
#include "abstract_MSSMNoFV_onshell_soft_parameters.hpp"
#include "wrapper_MSSMNoFV_onshell_susy_parameters_decl.hpp"

#include "identification.hpp"

namespace CAT_3(BACKENDNAME,_,SAFE_VERSION)
{
   
   namespace gm2calc
   {
      
      class MSSMNoFV_onshell_soft_parameters : public MSSMNoFV_onshell_susy_parameters
      {
            // Member variables: 
         public:
            // -- Static factory pointers: 
            static Abstract_MSSMNoFV_onshell_soft_parameters* (*__factory0)();
            static Abstract_MSSMNoFV_onshell_soft_parameters* (*__factory1)(const gm2calc::MSSMNoFV_onshell_susy_parameters&, const Eigen::Matrix<double, 3, 3, 0>&, const Eigen::Matrix<double, 3, 3, 0>&, const Eigen::Matrix<double, 3, 3, 0>&, double, const Eigen::Matrix<double, 3, 3, 0>&, const Eigen::Matrix<double, 3, 3, 0>&, double, double, const Eigen::Matrix<double, 3, 3, 0>&, const Eigen::Matrix<double, 3, 3, 0>&, const Eigen::Matrix<double, 3, 3, 0>&, double, double, double);
      
            // -- Other member variables: 
      
            // Member functions: 
         public:
            void print(std::ostream& arg_1) const;
      
            void clear();
      
            void set_TYd(const Eigen::Matrix<double, 3, 3, 0>& TYd_);
      
            void set_TYd(int i, int k, double value);
      
            void set_TYe(const Eigen::Matrix<double, 3, 3, 0>& TYe_);
      
            void set_TYe(int i, int k, double value);
      
            void set_TYu(const Eigen::Matrix<double, 3, 3, 0>& TYu_);
      
            void set_TYu(int i, int k, double value);
      
            void set_BMu(double BMu_);
      
            void set_mq2(const Eigen::Matrix<double, 3, 3, 0>& mq2_);
      
            void set_mq2(int i, int k, double value);
      
            void set_ml2(const Eigen::Matrix<double, 3, 3, 0>& ml2_);
      
            void set_ml2(int i, int k, double value);
      
            void set_mHd2(double mHd2_);
      
            void set_mHu2(double mHu2_);
      
            void set_md2(const Eigen::Matrix<double, 3, 3, 0>& md2_);
      
            void set_md2(int i, int k, double value);
      
            void set_mu2(const Eigen::Matrix<double, 3, 3, 0>& mu2_);
      
            void set_mu2(int i, int k, double value);
      
            void set_me2(const Eigen::Matrix<double, 3, 3, 0>& me2_);
      
            void set_me2(int i, int k, double value);
      
            void set_MassB(double MassB_);
      
            void set_MassWB(double MassWB_);
      
            void set_MassG(double MassG_);
      
            const ::Eigen::Matrix<double, 3, 3, 0>& get_TYd() const;
      
            double get_TYd(int i, int k) const;
      
            const ::Eigen::Matrix<double, 3, 3, 0>& get_TYe() const;
      
            double get_TYe(int i, int k) const;
      
            const ::Eigen::Matrix<double, 3, 3, 0>& get_TYu() const;
      
            double get_TYu(int i, int k) const;
      
            double get_BMu() const;
      
            const ::Eigen::Matrix<double, 3, 3, 0>& get_mq2() const;
      
            double get_mq2(int i, int k) const;
      
            const ::Eigen::Matrix<double, 3, 3, 0>& get_ml2() const;
      
            double get_ml2(int i, int k) const;
      
            double get_mHd2() const;
      
            double get_mHu2() const;
      
            const ::Eigen::Matrix<double, 3, 3, 0>& get_md2() const;
      
            double get_md2(int i, int k) const;
      
            const ::Eigen::Matrix<double, 3, 3, 0>& get_mu2() const;
      
            double get_mu2(int i, int k) const;
      
            const ::Eigen::Matrix<double, 3, 3, 0>& get_me2() const;
      
            double get_me2(int i, int k) const;
      
            double get_MassB() const;
      
            double get_MassWB() const;
      
            double get_MassG() const;
      
      
            // Wrappers for original constructors: 
         public:
            MSSMNoFV_onshell_soft_parameters();
            MSSMNoFV_onshell_soft_parameters(const gm2calc::MSSMNoFV_onshell_susy_parameters& arg_1, const Eigen::Matrix<double, 3, 3, 0>& TYd_, const Eigen::Matrix<double, 3, 3, 0>& TYe_, const Eigen::Matrix<double, 3, 3, 0>& TYu_, double BMu_, const Eigen::Matrix<double, 3, 3, 0>& mq2_, const Eigen::Matrix<double, 3, 3, 0>& ml2_, double mHd2_, double mHu2_, const Eigen::Matrix<double, 3, 3, 0>& md2_, const Eigen::Matrix<double, 3, 3, 0>& mu2_, const Eigen::Matrix<double, 3, 3, 0>& me2_, double MassB_, double MassWB_, double MassG_);
      
            // Special pointer-based constructor: 
            MSSMNoFV_onshell_soft_parameters(Abstract_MSSMNoFV_onshell_soft_parameters* in);
      
            // Copy constructor: 
            MSSMNoFV_onshell_soft_parameters(const MSSMNoFV_onshell_soft_parameters& in);
      
            // Assignment operator: 
            MSSMNoFV_onshell_soft_parameters& operator=(const MSSMNoFV_onshell_soft_parameters& in);
      
            // Destructor: 
            ~MSSMNoFV_onshell_soft_parameters();
      
            // Returns correctly casted pointer to Abstract class: 
            Abstract_MSSMNoFV_onshell_soft_parameters* get_BEptr() const;
      
      };
   }
   
}


#include "gambit/Backends/backend_undefs.hpp"

#endif /* __wrapper_MSSMNoFV_onshell_soft_parameters_decl_gm2calc_1_3_0_hpp__ */
```


-------------------------------

Updated on 2025-02-12 at 16:10:36 +0000
