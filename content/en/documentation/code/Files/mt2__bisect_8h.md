---
title: "file ColliderBit/mt2_bisect.h"

description: "[No description available]"

---

# file ColliderBit/mt2_bisect.h

[No description available]

## Namespaces

| Name           |
| -------------- |
| **[mt2_bisect](/documentation/code/namespaces/namespacemt2__bisect/)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[mt2_bisect::mt2](/documentation/code/classes/classmt2__bisect_1_1mt2/)**  |

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[RELATIVE_PRECISION](/documentation/code/files/mt2__bisect_8h/#define-relative-precision)**  |
|  | **[ABSOLUTE_PRECISION](/documentation/code/files/mt2__bisect_8h/#define-absolute-precision)**  |
|  | **[MIN_MASS](/documentation/code/files/mt2__bisect_8h/#define-min-mass)**  |
|  | **[ZERO_MASS](/documentation/code/files/mt2__bisect_8h/#define-zero-mass)**  |
|  | **[SCANSTEP](/documentation/code/files/mt2__bisect_8h/#define-scanstep)**  |




## Macros Documentation

### define RELATIVE_PRECISION

```
#define RELATIVE_PRECISION 0.00001
```


### define ABSOLUTE_PRECISION

```
#define ABSOLUTE_PRECISION 0.0
```


### define MIN_MASS

```
#define MIN_MASS 0.1
```


### define ZERO_MASS

```
#define ZERO_MASS 0.000
```


### define SCANSTEP

```
#define SCANSTEP 0.1
```


## Source code

```
#ifndef MT2_BISECT_H
#define MT2_BISECT_H


/*The user can change the desired precision below, the larger one of the following two definitions is used. Relative precision less than 0.00001 is not guaranteed to be achievable--use with caution*/ 

#define RELATIVE_PRECISION 0.00001 //defined as precision = RELATIVE_PRECISION * scale, where scale = max{Ea, Eb}
#define ABSOLUTE_PRECISION 0.0     //absolute precision for mt2, unused by default


//Reserved for expert
#define MIN_MASS  0.1   //if ma<MINMASS and mb<MINMASS, use massless code
#define ZERO_MASS 0.000 //give massless particles a small mass
#define SCANSTEP 0.1
namespace mt2_bisect
{
class mt2
{  
   public:

      mt2();
      void   mt2_bisect();
      void   mt2_massless();
      void   set_momenta(double *pa0, double *pb0, double* pmiss0);
      void   set_mn(double mn);
      double get_mt2();
      void   print();
      int    nevt;
   private:  

      bool   solved;
      bool   momenta_set;
      double mt2_b;

      int    nsols(double Dsq);
      int    nsols_massless(double Dsq);
      inline int    signchange_n( long double t1, long double t2, long double t3, long double t4, long double t5);
      inline int    signchange_p( long double t1, long double t2, long double t3, long double t4, long double t5);
      int scan_high(double &Deltasq_high);
      int find_high(double &Deltasq_high);
      //data members
      double pax, pay, ma, Ea;
      double pmissx, pmissy;
      double pbx, pby, mb, Eb;
      double mn, mn_unscale;
     
      //auxiliary definitions
      double masq, Easq;
      double mbsq, Ebsq;
      double pmissxsq, pmissysq;
      double mnsq;

      //auxiliary coefficients
      double a1, b1, c1, a2, b2, c2, d1, e1, f1, d2, e2, f2;
      double d11, e11, f12, f10, d21, d20, e21, e20, f22, f21, f20;

      double scale;
      double precision;
};

}//end namespace mt2_bisect

#endif
```


-------------------------------

Updated on 2025-02-12 at 16:10:35 +0000
