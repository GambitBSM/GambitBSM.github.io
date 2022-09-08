---
title: "class Gambit::BEfunction_bucket< typename variadic_ptr< TYPE, ARGS... >::type, TYPE, ARGS... >"
description: "Partial specialisation for variadic backend functions. "

---

# class Gambit::BEfunction_bucket< typename variadic_ptr< TYPE, ARGS... >::type, TYPE, ARGS... >



Partial specialisation for variadic backend functions.  [More...](#detailed-description)


`#include <safety_bucket.hpp>`

Inherits from [Gambit::BEfunction_bucket_common< variadic_ptr< TYPE, ARGS... >::type, TYPE, ARGS... >](/documentation/code/classes/classgambit_1_1befunction__bucket__common/), [Gambit::BE_bucket_base](/documentation/code/classes/classgambit_1_1be__bucket__base/), [Gambit::safety_bucket_base](/documentation/code/classes/classgambit_1_1safety__bucket__base/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BEfunction_bucket](/documentation/code/classes/classgambit_1_1befunction__bucket_3_01typename_01variadic__ptr_3_01type_00_01args_8_8_8_01_4_1_15dd60a923b4ad82c804e05a59e6e7510/#function-gambitbefunction-bucket-typename-variadic-ptr-type-args-type-type-args-befunction-bucket)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) mym, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) myf, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) me, [backend_functor](/documentation/code/classes/classgambit_1_1backend__functor/)< typename [variadic_ptr](/documentation/code/classes/structgambit_1_1variadic__ptr/)< TYPE, ARGS... >::type, TYPE, ARGS... > * functor_ptr_in =NULL)<br>Constructor for variadic [BEfunction_bucket](/documentation/code/classes/classgambit_1_1befunction__bucket/).  |
| template <typename... VARARGS\> <br>TYPE | **[operator()](/documentation/code/classes/classgambit_1_1befunction__bucket_3_01typename_01variadic__ptr_3_01type_00_01args_8_8_8_01_4_1_15dd60a923b4ad82c804e05a59e6e7510/#function-gambitbefunction-bucket-typename-variadic-ptr-type-args-type-type-args-operator)**(VARARGS &&... varargs)<br>Call backend function.  |

## Additional inherited members

**Public Functions inherited from [Gambit::BEfunction_bucket_common< variadic_ptr< TYPE, ARGS... >::type, TYPE, ARGS... >](/documentation/code/classes/classgambit_1_1befunction__bucket__common/)**

|                | Name           |
| -------------- | -------------- |
| | **[BEfunction_bucket_common](/documentation/code/classes/classgambit_1_1befunction__bucket__common/#function-gambitbefunction-bucket-common-befunction-bucket-common)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) mym, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) myf, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) me, [backend_functor](/documentation/code/classes/classgambit_1_1backend__functor/)< PTR_TYPE, TYPE, ARGS... > * functor_ptr_in =NULL)<br>Constructor for [BEfunction_bucket_common](/documentation/code/classes/classgambit_1_1befunction__bucket__common/).  |
| void | **[initialize](/documentation/code/classes/classgambit_1_1befunction__bucket__common/#function-gambitbefunction-bucket-common-initialize)**([backend_functor](/documentation/code/classes/classgambit_1_1backend__functor/)< PTR_TYPE, TYPE, ARGS... > * functor_ptr_in)<br>Initialize this bucket with a functor pointer.  |
| PTR_TYPE | **[pointer](/documentation/code/classes/classgambit_1_1befunction__bucket__common/#function-gambitbefunction-bucket-common-pointer)**()<br>Return the underlying function pointer.  |

**Protected Attributes inherited from [Gambit::BEfunction_bucket_common< variadic_ptr< TYPE, ARGS... >::type, TYPE, ARGS... >](/documentation/code/classes/classgambit_1_1befunction__bucket__common/)**

|                | Name           |
| -------------- | -------------- |
| [backend_functor](/documentation/code/classes/classgambit_1_1backend__functor/)< PTR_TYPE, TYPE, ARGS... > * | **[_functor_ptr](/documentation/code/classes/classgambit_1_1befunction__bucket__common/#variable-gambitbefunction-bucket-common-functor-ptr)**  |

**Public Functions inherited from [Gambit::BE_bucket_base](/documentation/code/classes/classgambit_1_1be__bucket__base/)**

|                | Name           |
| -------------- | -------------- |
| | **[BE_bucket_base](/documentation/code/classes/classgambit_1_1be__bucket__base/#function-gambitbe-bucket-base-be-bucket-base)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) mym, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) myf, [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) me)<br>Constructor for [BE_bucket_base](/documentation/code/classes/classgambit_1_1be__bucket__base/).  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[backend](/documentation/code/classes/classgambit_1_1be__bucket__base/#function-gambitbe-bucket-base-backend)**()<br>Get backend name.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[version](/documentation/code/classes/classgambit_1_1be__bucket__base/#function-gambitbe-bucket-base-version)**()<br>Get version information.  |

**Public Functions inherited from [Gambit::safety_bucket_base](/documentation/code/classes/classgambit_1_1safety__bucket__base/)**

|                | Name           |
| -------------- | -------------- |
| | **[safety_bucket_base](/documentation/code/classes/classgambit_1_1safety__bucket__base/#function-gambitsafety-bucket-base-safety-bucket-base)**([str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) myinfo)<br>Master constructor.  |
| bool | **[active](/documentation/code/classes/classgambit_1_1safety__bucket__base/#function-gambitsafety-bucket-base-active)**() |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[name](/documentation/code/classes/classgambit_1_1safety__bucket__base/#function-gambitsafety-bucket-base-name)**()<br>Get capability name.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[origin](/documentation/code/classes/classgambit_1_1safety__bucket__base/#function-gambitsafety-bucket-base-origin)**()<br>Get name of origin (module/backend).  |

**Protected Functions inherited from [Gambit::safety_bucket_base](/documentation/code/classes/classgambit_1_1safety__bucket__base/)**

|                | Name           |
| -------------- | -------------- |
| void | **[dieGracefully](/documentation/code/classes/classgambit_1_1safety__bucket__base/#function-gambitsafety-bucket-base-diegracefully)**() const<br>Failure message invoked when the user tries to access the object before it is initialized.  |

**Protected Attributes inherited from [Gambit::safety_bucket_base](/documentation/code/classes/classgambit_1_1safety__bucket__base/)**

|                | Name           |
| -------------- | -------------- |
| [functor](/documentation/code/classes/classgambit_1_1functor/) * | **[_functor_base_ptr](/documentation/code/classes/classgambit_1_1safety__bucket__base/#variable-gambitsafety-bucket-base-functor-base-ptr)**  |
| bool | **[_initialized](/documentation/code/classes/classgambit_1_1safety__bucket__base/#variable-gambitsafety-bucket-base-initialized)**  |
| const [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) | **[whoami](/documentation/code/classes/classgambit_1_1safety__bucket__base/#variable-gambitsafety-bucket-base-whoami)**  |


## Detailed Description

```
template <typename TYPE ,
typename... ARGS>
class Gambit::BEfunction_bucket< typename variadic_ptr< TYPE, ARGS... >::type, TYPE, ARGS... >;
```

Partial specialisation for variadic backend functions. 
## Public Functions Documentation

### function BEfunction_bucket

```
inline BEfunction_bucket(
    str mym,
    str myf,
    str me,
    backend_functor< typename variadic_ptr< TYPE, ARGS... >::type, TYPE, ARGS... > * functor_ptr_in =NULL
)
```

Constructor for variadic [BEfunction_bucket](/documentation/code/classes/classgambit_1_1befunction__bucket/). 

### function operator()

```
template <typename... VARARGS>
inline TYPE operator()(
    VARARGS &&... varargs
)
```

Call backend function. 

-------------------------------

Updated on 2022-09-08 at 02:00:46 +0000