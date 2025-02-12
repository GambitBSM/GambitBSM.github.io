---
title: "class Gambit::Priors::RangePrior1D"
description: "Template class for 1d priors which need only a range option in their constructor. "

---

# class Gambit::Priors::RangePrior1D



Template class for 1d priors which need only a "range" option in their constructor.  [More...](#detailed-description)


`#include <flat_log.hpp>`

Inherits from [Gambit::Priors::BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[RangePrior1D](/documentation/code/classes/classgambit_1_1priors_1_1rangeprior1d/#function-rangeprior1d)**(const std::vector< std::string > & param, const [Options](/documentation/code/classes/classgambit_1_1options/) & options) |
| virtual void | **[transform](/documentation/code/classes/classgambit_1_1priors_1_1rangeprior1d/#function-transform)**(hyper_cube_ref< double > unit, std::unordered_map< std::string, double > & physical) const override<br>Transform from unit hypercube to physical parameter.  |
| virtual void | **[inverse_transform](/documentation/code/classes/classgambit_1_1priors_1_1rangeprior1d/#function-inverse-transform)**(const std::unordered_map< std::string, double > & physical, hyper_cube_ref< double > unit) const override<br>Transform from physical parameter to unit hypercube.  |
| virtual double | **[log_prior_density](/documentation/code/classes/classgambit_1_1priors_1_1rangeprior1d/#function-log-prior-density)**(const std::unordered_map< std::string, double > & ) const override<br>Log of prior density.  |

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
template <class T >
class Gambit::Priors::RangePrior1D;
```

Template class for 1d priors which need only a "range" option in their constructor. 
## Public Functions Documentation

### function RangePrior1D

```
inline RangePrior1D(
    const std::vector< std::string > & param,
    const Options & options
)
```


### function transform

```
inline virtual void transform(
    hyper_cube_ref< double > unit,
    std::unordered_map< std::string, double > & physical
) const override
```

Transform from unit hypercube to physical parameter. 

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

Updated on 2025-02-12 at 15:36:39 +0000