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
| | **[FixedPrior](/documentation/code/classes/classgambit_1_1priors_1_1fixedprior/#function-gambitpriorsfixedprior-fixedprior)**(const std::vector< std::string > & param, const [Options](/documentation/code/classes/classgambit_1_1options/) & options) |
| | **[FixedPrior](/documentation/code/classes/classgambit_1_1priors_1_1fixedprior/#function-gambitpriorsfixedprior-fixedprior)**(const std::string & param, const [Options](/documentation/code/classes/classgambit_1_1options/) & options) |
| | **[FixedPrior](/documentation/code/classes/classgambit_1_1priors_1_1fixedprior/#function-gambitpriorsfixedprior-fixedprior)**(const std::string & name, double value) |
| virtual std::vector< std::string > | **[getShownParameters](/documentation/code/classes/classgambit_1_1priors_1_1fixedprior/#function-gambitpriorsfixedprior-getshownparameters)**() const override |
| virtual void | **[transform](/documentation/code/classes/classgambit_1_1priors_1_1fixedprior/#function-gambitpriorsfixedprior-transform)**(const std::vector< double > & , std::unordered_map< std::string, double > & ) const override<br>Transform from unit hypercube to parameter.  |
| virtual std::vector< double > | **[inverse_transform](/documentation/code/classes/classgambit_1_1priors_1_1fixedprior/#function-gambitpriorsfixedprior-inverse-transform)**(const std::unordered_map< std::string, double > & ) const override<br>Transform from parameter back to unit hypercube.  |

## Additional inherited members

**Public Functions inherited from [Gambit::Priors::BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)**

|                | Name           |
| -------------- | -------------- |
| virtual | **[~BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-gambitpriorsbaseprior-baseprior)**() =default |
| | **[BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-gambitpriorsbaseprior-baseprior)**() |
| | **[BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-gambitpriorsbaseprior-baseprior)**(const int param_size) |
| | **[BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-gambitpriorsbaseprior-baseprior)**(const std::vector< std::string > & param_names, const int param_size =0) |
| | **[BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-gambitpriorsbaseprior-baseprior)**(const std::string & param_name, const int param_size =0) |
| virtual double | **[operator()](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-gambitpriorsbaseprior-operator)**(const std::vector< double > & ) const<br>Log of PDF density.  |
| unsigned int | **[size](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-gambitpriorsbaseprior-size)**() const |
| void | **[setSize](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-gambitpriorsbaseprior-setsize)**(const unsigned int size) |
| unsigned int & | **[sizeRef](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-gambitpriorsbaseprior-sizeref)**() |
| std::vector< std::string > | **[getParameters](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-gambitpriorsbaseprior-getparameters)**() const |

**Protected Attributes inherited from [Gambit::Priors::BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)**

|                | Name           |
| -------------- | -------------- |
| std::vector< std::string > | **[param_names](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#variable-gambitpriorsbaseprior-param-names)**  |


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


**Reimplements**: [Gambit::Priors::BasePrior::getShownParameters](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-gambitpriorsbaseprior-getshownparameters)


### function transform

```
inline virtual void transform(
    const std::vector< double > & ,
    std::unordered_map< std::string, double > & 
) const override
```

Transform from unit hypercube to parameter. 

**Reimplements**: [Gambit::Priors::BasePrior::transform](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-gambitpriorsbaseprior-transform)


### function inverse_transform

```
inline virtual std::vector< double > inverse_transform(
    const std::unordered_map< std::string, double > & 
) const override
```

Transform from parameter back to unit hypercube. 

**Reimplements**: [Gambit::Priors::BasePrior::inverse_transform](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-gambitpriorsbaseprior-inverse-transform)


-------------------------------

Updated on 2022-09-08 at 02:00:49 +0000