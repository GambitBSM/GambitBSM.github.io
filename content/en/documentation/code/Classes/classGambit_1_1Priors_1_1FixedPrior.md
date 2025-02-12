---
title: "class Gambit::Priors::FixedPrior"
description: "A fixed parameter. "

---

# class Gambit::Priors::FixedPrior



A fixed parameter. 


`#include <fixed_same_as.hpp>`

Inherits from [Gambit::Priors::BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[FixedPrior](/documentation/code/classes/classgambit_1_1priors_1_1fixedprior/#function-fixedprior)**(const std::vector< std::string > & param, const [Options](/documentation/code/classes/classgambit_1_1options/) & options) |
| | **[FixedPrior](/documentation/code/classes/classgambit_1_1priors_1_1fixedprior/#function-fixedprior)**(const std::string & param, const [Options](/documentation/code/classes/classgambit_1_1options/) & options) |
| | **[FixedPrior](/documentation/code/classes/classgambit_1_1priors_1_1fixedprior/#function-fixedprior)**(const std::string & name, double value) |
| virtual std::vector< std::string > | **[getShownParameters](/documentation/code/classes/classgambit_1_1priors_1_1fixedprior/#function-getshownparameters)**() const override |
| virtual void | **[transform](/documentation/code/classes/classgambit_1_1priors_1_1fixedprior/#function-transform)**(hyper_cube_ref< double > unit, std::unordered_map< std::string, double > & physical) const override<br>Transform from unit hypercube to physical parameter.  |
| virtual void | **[inverse_transform](/documentation/code/classes/classgambit_1_1priors_1_1fixedprior/#function-inverse-transform)**(const std::unordered_map< std::string, double > & physical, hyper_cube_ref< double > unit) const override<br>Transform from physical parameter to unit hypercube.  |
| virtual double | **[log_prior_density](/documentation/code/classes/classgambit_1_1priors_1_1fixedprior/#function-log-prior-density)**(const std::unordered_map< std::string, double > & ) const override<br>Log of prior density.  |

## Additional inherited members

**Public Functions inherited from [Gambit::Priors::BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)**

|                | Name           |
| -------------- | -------------- |
| virtual | **[~BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-baseprior)**() =default |
| | **[BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-baseprior)**() |
| | **[BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-baseprior)**(const int param_size) |
| | **[BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-baseprior)**(const std::vector< std::string > & param_names, const int param_size =0) |
| | **[BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-baseprior)**(const std::string & param_name, const int param_size =0) |
| unsigned int | **[size](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-size)**() const |
| void | **[setSize](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-setsize)**(const unsigned int size) |
| unsigned int & | **[sizeRef](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-sizeref)**() |
| std::vector< std::string > | **[getParameters](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-getparameters)**() const |

**Protected Attributes inherited from [Gambit::Priors::BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)**

|                | Name           |
| -------------- | -------------- |
| std::vector< std::string > | **[param_names](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#variable-param-names)**  |


## Public Functions Documentation

### function FixedPrior

```
inline FixedPrior(
    const std::vector< std::string > & param,
    const Options & options
)
```


### function FixedPrior

```
inline FixedPrior(
    const std::string & param,
    const Options & options
)
```


### function FixedPrior

```
inline FixedPrior(
    const std::string & name,
    double value
)
```


### function getShownParameters

```
inline virtual std::vector< std::string > getShownParameters() const override
```


**Reimplements**: [Gambit::Priors::BasePrior::getShownParameters](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-getshownparameters)


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