---
title: "class Gambit::Priors::Cauchy"
description: "Multi-dimensional [Cauchy]() prior. "

---

# class Gambit::Priors::Cauchy



Multi-dimensional [Cauchy]() prior.  [More...](#detailed-description)


`#include <cauchy.hpp>`

Inherits from [Gambit::Priors::BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Cauchy](/documentation/code/classes/classgambit_1_1priors_1_1cauchy/#function-cauchy)**(const std::vector< std::string > & param, const [Options](/documentation/code/classes/classgambit_1_1options/) & options) |
| virtual void | **[transform](/documentation/code/classes/classgambit_1_1priors_1_1cauchy/#function-transform)**(hyper_cube_ref< double > unitpars, std::unordered_map< std::string, double > & outputMap) const<br>Transformation from unit interval to the [Cauchy](/documentation/code/classes/classgambit_1_1priors_1_1cauchy/).  |
| virtual void | **[inverse_transform](/documentation/code/classes/classgambit_1_1priors_1_1cauchy/#function-inverse-transform)**(const std::unordered_map< std::string, double > & physical, hyper_cube_ref< double > unit) const override<br>Transform from physical parameter to unit hypercube.  |
| virtual double | **[log_prior_density](/documentation/code/classes/classgambit_1_1priors_1_1cauchy/#function-log-prior-density)**(const std::unordered_map< std::string, double > & ) const override<br>Log of prior density.  |

## Additional inherited members

**Public Functions inherited from [Gambit::Priors::BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)**

|                | Name           |
| -------------- | -------------- |
| virtual | **[~BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-baseprior)**() =default |
| | **[BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-baseprior)**() |
| | **[BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-baseprior)**(const int param_size) |
| | **[BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-baseprior)**(const std::vector< std::string > & param_names, const int param_size =0) |
| | **[BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-baseprior)**(const std::string & param_name, const int param_size =0) |
| virtual std::vector< std::string > | **[getShownParameters](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-getshownparameters)**() const |
| unsigned int | **[size](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-size)**() const |
| void | **[setSize](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-setsize)**(const unsigned int size) |
| unsigned int & | **[sizeRef](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-sizeref)**() |
| std::vector< std::string > | **[getParameters](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-getparameters)**() const |

**Protected Attributes inherited from [Gambit::Priors::BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)**

|                | Name           |
| -------------- | -------------- |
| std::vector< std::string > | **[param_names](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#variable-param-names)**  |


## Detailed Description

```
class Gambit::Priors::Cauchy;
```

Multi-dimensional [Cauchy]() prior. 

This is a [multivariate \(t\)-distribution](https://en.wikipedia.org/wiki/Multivariate_t-distribution) with \(\nu = 1\) degree of freedom.

Defined by a scale matrix, \(\Sigma\), and a location vector.

If the scale matrix is diagonal,it may instead be specified by the square-roots of its diagonal entries, denoted \(\gamma\). 

## Public Functions Documentation

### function Cauchy

```
Cauchy(
    const std::vector< std::string > & param,
    const Options & options
)
```


### function transform

```
inline virtual void transform(
    hyper_cube_ref< double > unitpars,
    std::unordered_map< std::string, double > & outputMap
) const
```

Transformation from unit interval to the [Cauchy](/documentation/code/classes/classgambit_1_1priors_1_1cauchy/). 

**Reimplements**: [Gambit::Priors::BasePrior::transform](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-transform)


### function inverse_transform

```
inline virtual void inverse_transform(
    const std::unordered_map< std::string, double > & physical,
    hyper_cube_ref< double > unit
) const override
```

Transform from physical parameter to unit hypercube. 

**Reimplements**: [Gambit::Priors::BasePrior::inverse_transform](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-inverse-transform)


### function log_prior_density

```
inline virtual double log_prior_density(
    const std::unordered_map< std::string, double > & 
) const override
```

Log of prior density. 

**Reimplements**: [Gambit::Priors::BasePrior::log_prior_density](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-log-prior-density)


-------------------------------

Updated on 2025-02-12 at 16:10:32 +0000