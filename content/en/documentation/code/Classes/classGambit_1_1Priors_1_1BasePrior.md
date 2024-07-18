---
title: "class Gambit::Priors::BasePrior"
description: "Abstract base class for priors. "

---

# class Gambit::Priors::BasePrior



Abstract base class for priors. 


`#include <base_prior.hpp>`

Inherited by [Gambit::Priors::Cauchy](/documentation/code/classes/classgambit_1_1priors_1_1cauchy/), [Gambit::Priors::CompositePrior](/documentation/code/classes/classgambit_1_1priors_1_1compositeprior/), [Gambit::Priors::DoubleLogFlatJoin](/documentation/code/classes/classgambit_1_1priors_1_1doublelogflatjoin/), [Gambit::Priors::Dummy](/documentation/code/classes/classgambit_1_1priors_1_1dummy/), [Gambit::Priors::FixedPrior](/documentation/code/classes/classgambit_1_1priors_1_1fixedprior/), [Gambit::Priors::Gaussian](/documentation/code/classes/classgambit_1_1priors_1_1gaussian/), [Gambit::Priors::LogNormal](/documentation/code/classes/classgambit_1_1priors_1_1lognormal/), [Gambit::Priors::MultiPriors](/documentation/code/classes/classgambit_1_1priors_1_1multipriors/), [Gambit::Priors::None](/documentation/code/classes/classgambit_1_1priors_1_1none/), [Gambit::Priors::Plugin](/documentation/code/classes/classgambit_1_1priors_1_1plugin/), [Gambit::Priors::RangePrior1D< T >](/documentation/code/classes/classgambit_1_1priors_1_1rangeprior1d/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual | **[~BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-baseprior)**() =default |
| | **[BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-baseprior)**() |
| | **[BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-baseprior)**(const int param_size) |
| | **[BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-baseprior)**(const std::vector< std::string > & param_names, const int param_size =0) |
| | **[BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-baseprior)**(const std::string & param_name, const int param_size =0) |
| virtual void | **[transform](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-transform)**(hyper_cube_ref< double > unit, std::unordered_map< std::string, double > & physical) const =0<br>Transform from unit hypercube to physical parameter.  |
| void | **[transform](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-transform)**(const std::vector< double > & unit, std::unordered_map< std::string, double > & physical) const |
| std::unordered_map< std::string, double > | **[transform](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-transform)**(const std::vector< double > & unit) const |
| virtual void | **[inverse_transform](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-inverse-transform)**(const std::unordered_map< std::string, double > & physical, hyper_cube_ref< double > unit) const =0<br>Transform from physical parameter to unit hypercube.  |
| void | **[inverse_transform](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-inverse-transform)**(const std::unordered_map< std::string, double > & physical, std::vector< double > & unit) const |
| std::vector< double > | **[inverse_transform](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-inverse-transform)**(const std::unordered_map< std::string, double > & physical) const |
| virtual double | **[log_prior_density](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-log-prior-density)**(const std::unordered_map< std::string, double > & ) const =0<br>Log of prior density.  |
| virtual std::vector< std::string > | **[getShownParameters](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-getshownparameters)**() const |
| unsigned int | **[size](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-size)**() const |
| void | **[setSize](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-setsize)**(const unsigned int size) |
| unsigned int & | **[sizeRef](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-sizeref)**() |
| std::vector< std::string > | **[getParameters](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-getparameters)**() const |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| std::vector< std::string > | **[param_names](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#variable-param-names)**  |

## Public Functions Documentation

### function ~BasePrior

```
virtual ~BasePrior() =default
```


### function BasePrior

```
inline BasePrior()
```


### function BasePrior

```
inline explicit BasePrior(
    const int param_size
)
```


### function BasePrior

```
inline explicit BasePrior(
    const std::vector< std::string > & param_names,
    const int param_size =0
)
```


### function BasePrior

```
inline explicit BasePrior(
    const std::string & param_name,
    const int param_size =0
)
```


### function transform

```
virtual void transform(
    hyper_cube_ref< double > unit,
    std::unordered_map< std::string, double > & physical
) const =0
```

Transform from unit hypercube to physical parameter. 

**Reimplemented by**: [Gambit::Priors::DoubleLogFlatJoin::transform](/documentation/code/classes/classgambit_1_1priors_1_1doublelogflatjoin/#function-transform), [Gambit::Priors::RangePrior1D::transform](/documentation/code/classes/classgambit_1_1priors_1_1rangeprior1d/#function-transform), [Gambit::Priors::Cauchy::transform](/documentation/code/classes/classgambit_1_1priors_1_1cauchy/#function-transform), [Gambit::Priors::CompositePrior::transform](/documentation/code/classes/classgambit_1_1priors_1_1compositeprior/#function-transform), [Gambit::Priors::Dummy::transform](/documentation/code/classes/classgambit_1_1priors_1_1dummy/#function-transform), [Gambit::Priors::Gaussian::transform](/documentation/code/classes/classgambit_1_1priors_1_1gaussian/#function-transform), [Gambit::Priors::LogNormal::transform](/documentation/code/classes/classgambit_1_1priors_1_1lognormal/#function-transform), [Gambit::Priors::Plugin::transform](/documentation/code/classes/classgambit_1_1priors_1_1plugin/#function-transform), [Gambit::Priors::None::transform](/documentation/code/classes/classgambit_1_1priors_1_1none/#function-transform), [Gambit::Priors::FixedPrior::transform](/documentation/code/classes/classgambit_1_1priors_1_1fixedprior/#function-transform), [Gambit::Priors::MultiPriors::transform](/documentation/code/classes/classgambit_1_1priors_1_1multipriors/#function-transform)


### function transform

```
inline void transform(
    const std::vector< double > & unit,
    std::unordered_map< std::string, double > & physical
) const
```


### function transform

```
inline std::unordered_map< std::string, double > transform(
    const std::vector< double > & unit
) const
```


### function inverse_transform

```
virtual void inverse_transform(
    const std::unordered_map< std::string, double > & physical,
    hyper_cube_ref< double > unit
) const =0
```

Transform from physical parameter to unit hypercube. 

**Reimplemented by**: [Gambit::Priors::DoubleLogFlatJoin::inverse_transform](/documentation/code/classes/classgambit_1_1priors_1_1doublelogflatjoin/#function-inverse-transform), [Gambit::Priors::None::inverse_transform](/documentation/code/classes/classgambit_1_1priors_1_1none/#function-inverse-transform), [Gambit::Priors::Plugin::inverse_transform](/documentation/code/classes/classgambit_1_1priors_1_1plugin/#function-inverse-transform), [Gambit::Priors::Cauchy::inverse_transform](/documentation/code/classes/classgambit_1_1priors_1_1cauchy/#function-inverse-transform), [Gambit::Priors::CompositePrior::inverse_transform](/documentation/code/classes/classgambit_1_1priors_1_1compositeprior/#function-inverse-transform), [Gambit::Priors::Dummy::inverse_transform](/documentation/code/classes/classgambit_1_1priors_1_1dummy/#function-inverse-transform), [Gambit::Priors::RangePrior1D::inverse_transform](/documentation/code/classes/classgambit_1_1priors_1_1rangeprior1d/#function-inverse-transform), [Gambit::Priors::Gaussian::inverse_transform](/documentation/code/classes/classgambit_1_1priors_1_1gaussian/#function-inverse-transform), [Gambit::Priors::LogNormal::inverse_transform](/documentation/code/classes/classgambit_1_1priors_1_1lognormal/#function-inverse-transform), [Gambit::Priors::FixedPrior::inverse_transform](/documentation/code/classes/classgambit_1_1priors_1_1fixedprior/#function-inverse-transform), [Gambit::Priors::MultiPriors::inverse_transform](/documentation/code/classes/classgambit_1_1priors_1_1multipriors/#function-inverse-transform)


### function inverse_transform

```
inline void inverse_transform(
    const std::unordered_map< std::string, double > & physical,
    std::vector< double > & unit
) const
```


### function inverse_transform

```
inline std::vector< double > inverse_transform(
    const std::unordered_map< std::string, double > & physical
) const
```


### function log_prior_density

```
virtual double log_prior_density(
    const std::unordered_map< std::string, double > & 
) const =0
```

Log of prior density. 

**Reimplemented by**: [Gambit::Priors::DoubleLogFlatJoin::log_prior_density](/documentation/code/classes/classgambit_1_1priors_1_1doublelogflatjoin/#function-log-prior-density), [Gambit::Priors::Dummy::log_prior_density](/documentation/code/classes/classgambit_1_1priors_1_1dummy/#function-log-prior-density), [Gambit::Priors::None::log_prior_density](/documentation/code/classes/classgambit_1_1priors_1_1none/#function-log-prior-density), [Gambit::Priors::Gaussian::log_prior_density](/documentation/code/classes/classgambit_1_1priors_1_1gaussian/#function-log-prior-density), [Gambit::Priors::LogNormal::log_prior_density](/documentation/code/classes/classgambit_1_1priors_1_1lognormal/#function-log-prior-density), [Gambit::Priors::Cauchy::log_prior_density](/documentation/code/classes/classgambit_1_1priors_1_1cauchy/#function-log-prior-density), [Gambit::Priors::CompositePrior::log_prior_density](/documentation/code/classes/classgambit_1_1priors_1_1compositeprior/#function-log-prior-density), [Gambit::Priors::FixedPrior::log_prior_density](/documentation/code/classes/classgambit_1_1priors_1_1fixedprior/#function-log-prior-density), [Gambit::Priors::MultiPriors::log_prior_density](/documentation/code/classes/classgambit_1_1priors_1_1multipriors/#function-log-prior-density), [Gambit::Priors::RangePrior1D::log_prior_density](/documentation/code/classes/classgambit_1_1priors_1_1rangeprior1d/#function-log-prior-density), [Gambit::Priors::Plugin::log_prior_density](/documentation/code/classes/classgambit_1_1priors_1_1plugin/#function-log-prior-density)


### function getShownParameters

```
inline virtual std::vector< std::string > getShownParameters() const
```


**Reimplemented by**: [Gambit::Priors::CompositePrior::getShownParameters](/documentation/code/classes/classgambit_1_1priors_1_1compositeprior/#function-getshownparameters), [Gambit::Priors::FixedPrior::getShownParameters](/documentation/code/classes/classgambit_1_1priors_1_1fixedprior/#function-getshownparameters), [Gambit::Priors::MultiPriors::getShownParameters](/documentation/code/classes/classgambit_1_1priors_1_1multipriors/#function-getshownparameters)


### function size

```
inline unsigned int size() const
```


### function setSize

```
inline void setSize(
    const unsigned int size
)
```


### function sizeRef

```
inline unsigned int & sizeRef()
```


### function getParameters

```
inline std::vector< std::string > getParameters() const
```


## Protected Attributes Documentation

### variable param_names

```
std::vector< std::string > param_names;
```


-------------------------------

Updated on 2024-07-18 at 13:53:32 +0000