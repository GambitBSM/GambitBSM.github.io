---
title: "class Gambit::Scanner::Scanner_Plugin_Function< ret(args...)>"
description: "Objective functor made up a single plugin. "

---

# class Gambit::Scanner::Scanner_Plugin_Function< ret(args...)>



Objective functor made up a single plugin.  [More...](#detailed-description)


`#include <plugin_factory.hpp>`

Inherits from [Gambit::Scanner::Plugins::Plugin_Interface< ret(args...)>](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1plugin__interface_3_01ret_07args_8_8_8_08_4/), [Gambit::Scanner::Function_Base< ret(args...)>](/documentation/code/classes/classgambit_1_1scanner_1_1function__base_3_01ret_07args_8_8_8_08_4/), [Gambit::Scanner::Plugins::Plugin_Interface_Base](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1plugin__interface__base/), [Gambit::Scanner::Plugins::Plugin_Main_Interface_Base< ret(args...)>](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1plugin__main__interface__base_3_01ret_07args_8_8_8_08_4/), boost::enable_shared_from_this< Function_Base< ret(args...)> >

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Scanner_Plugin_Function](/documentation/code/classes/classgambit_1_1scanner_1_1scanner__plugin__function_3_01ret_07args_8_8_8_08_4/#function-gambitscannerscanner-plugin-function-retargs-scanner-plugin-function)**(const std::vector< std::string > & params, const std::string & name) |
| ret | **[main](/documentation/code/classes/classgambit_1_1scanner_1_1scanner__plugin__function_3_01ret_07args_8_8_8_08_4/#function-gambitscannerscanner-plugin-function-retargs-main)**(const args &... in) |

## Additional inherited members

**Public Functions inherited from [Gambit::Scanner::Plugins::Plugin_Interface< ret(args...)>](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1plugin__interface_3_01ret_07args_8_8_8_08_4/)**

|                | Name           |
| -------------- | -------------- |
| template <typename... plug_args\> <br>| **[Plugin_Interface](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1plugin__interface_3_01ret_07args_8_8_8_08_4/#function-gambitscannerpluginsplugin-interface-retargs-plugin-interface)**(const std::string & type, const std::string & name, const plug_args &... inputs) |
| ret | **[operator()](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1plugin__interface_3_01ret_07args_8_8_8_08_4/#function-gambitscannerpluginsplugin-interface-retargs-operator)**(const args &... params) |

**Public Functions inherited from [Gambit::Scanner::Function_Base< ret(args...)>](/documentation/code/classes/classgambit_1_1scanner_1_1function__base_3_01ret_07args_8_8_8_08_4/)**

|                | Name           |
| -------------- | -------------- |
| | **[Function_Base](/documentation/code/classes/classgambit_1_1scanner_1_1function__base_3_01ret_07args_8_8_8_08_4/#function-gambitscannerfunction-base-retargs-function-base)**(double offset =0.) |
| virtual double | **[purposeModifier](/documentation/code/classes/classgambit_1_1scanner_1_1function__base_3_01ret_07args_8_8_8_08_4/#function-gambitscannerfunction-base-retargs-purposemodifier)**(double ret_val) |
| virtual | **[~Function_Base](/documentation/code/classes/classgambit_1_1scanner_1_1function__base_3_01ret_07args_8_8_8_08_4/#function-gambitscannerfunction-base-retargs-function-base)**() |
| ret | **[operator()](/documentation/code/classes/classgambit_1_1scanner_1_1function__base_3_01ret_07args_8_8_8_08_4/#function-gambitscannerfunction-base-retargs-operator)**(const args &... params) |
| void | **[setPurpose](/documentation/code/classes/classgambit_1_1scanner_1_1function__base_3_01ret_07args_8_8_8_08_4/#function-gambitscannerfunction-base-retargs-setpurpose)**(const std::string p) |
| void | **[setPrinter](/documentation/code/classes/classgambit_1_1scanner_1_1function__base_3_01ret_07args_8_8_8_08_4/#function-gambitscannerfunction-base-retargs-setprinter)**([printer](/documentation/code/namespaces/namespacegambit_1_1scanner/#typedef-gambitscanner-printer) * p) |
| void | **[setPrior](/documentation/code/classes/classgambit_1_1scanner_1_1function__base_3_01ret_07args_8_8_8_08_4/#function-gambitscannerfunction-base-retargs-setprior)**([Priors::BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/) * p) |
| [printer](/documentation/code/namespaces/namespacegambit_1_1scanner/#typedef-gambitscanner-printer) & | **[getPrinter](/documentation/code/classes/classgambit_1_1scanner_1_1function__base_3_01ret_07args_8_8_8_08_4/#function-gambitscannerfunction-base-retargs-getprinter)**() |
| [printer](/documentation/code/namespaces/namespacegambit_1_1scanner/#typedef-gambitscanner-printer) & | **[getPrinter](/documentation/code/classes/classgambit_1_1scanner_1_1function__base_3_01ret_07args_8_8_8_08_4/#function-gambitscannerfunction-base-retargs-getprinter)**() const |
| [Priors::BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/) & | **[getPrior](/documentation/code/classes/classgambit_1_1scanner_1_1function__base_3_01ret_07args_8_8_8_08_4/#function-gambitscannerfunction-base-retargs-getprior)**() |
| std::vector< std::string > | **[getParameters](/documentation/code/classes/classgambit_1_1scanner_1_1function__base_3_01ret_07args_8_8_8_08_4/#function-gambitscannerfunction-base-retargs-getparameters)**() |
| std::vector< std::string > | **[getShownParameters](/documentation/code/classes/classgambit_1_1scanner_1_1function__base_3_01ret_07args_8_8_8_08_4/#function-gambitscannerfunction-base-retargs-getshownparameters)**() |
| std::string | **[getPurpose](/documentation/code/classes/classgambit_1_1scanner_1_1function__base_3_01ret_07args_8_8_8_08_4/#function-gambitscannerfunction-base-retargs-getpurpose)**() const |
| int | **[getRank](/documentation/code/classes/classgambit_1_1scanner_1_1function__base_3_01ret_07args_8_8_8_08_4/#function-gambitscannerfunction-base-retargs-getrank)**() const |
| void | **[setRank](/documentation/code/classes/classgambit_1_1scanner_1_1function__base_3_01ret_07args_8_8_8_08_4/#function-gambitscannerfunction-base-retargs-setrank)**(int r) |
| double | **[getPurposeOffset](/documentation/code/classes/classgambit_1_1scanner_1_1function__base_3_01ret_07args_8_8_8_08_4/#function-gambitscannerfunction-base-retargs-getpurposeoffset)**() const |
| void | **[setPurposeOffset](/documentation/code/classes/classgambit_1_1scanner_1_1function__base_3_01ret_07args_8_8_8_08_4/#function-gambitscannerfunction-base-retargs-setpurposeoffset)**(double os) |
| unsigned long long int | **[getPtID](/documentation/code/classes/classgambit_1_1scanner_1_1function__base_3_01ret_07args_8_8_8_08_4/#function-gambitscannerfunction-base-retargs-getptid)**() const |
| void | **[setPtID](/documentation/code/classes/classgambit_1_1scanner_1_1function__base_3_01ret_07args_8_8_8_08_4/#function-gambitscannerfunction-base-retargs-setptid)**(unsigned long long int pID) |
| unsigned long long int | **[getNextPtID](/documentation/code/classes/classgambit_1_1scanner_1_1function__base_3_01ret_07args_8_8_8_08_4/#function-gambitscannerfunction-base-retargs-getnextptid)**() const |
| void | **[tell_scanner_early_shutdown_in_progress](/documentation/code/classes/classgambit_1_1scanner_1_1function__base_3_01ret_07args_8_8_8_08_4/#function-gambitscannerfunction-base-retargs-tell-scanner-early-shutdown-in-progress)**()<br>Tell ScannerBit that we are aborting the scan and it should tell the scanner plugin to stop, and return control to the calling code.  |
| void | **[disable_external_shutdown](/documentation/code/classes/classgambit_1_1scanner_1_1function__base_3_01ret_07args_8_8_8_08_4/#function-gambitscannerfunction-base-retargs-disable-external-shutdown)**() |
| bool | **[scanner_can_quit](/documentation/code/classes/classgambit_1_1scanner_1_1function__base_3_01ret_07args_8_8_8_08_4/#function-gambitscannerfunction-base-retargs-scanner-can-quit)**()<br>Check whether likelihood container is supposed to control early shutdown of scan.  |
| void | **[switch_to_alternate_min_LogL](/documentation/code/classes/classgambit_1_1scanner_1_1function__base_3_01ret_07args_8_8_8_08_4/#function-gambitscannerfunction-base-retargs-switch-to-alternate-min-logl)**() |
| bool | **[check_for_switch_to_alternate_min_LogL](/documentation/code/classes/classgambit_1_1scanner_1_1function__base_3_01ret_07args_8_8_8_08_4/#function-gambitscannerfunction-base-retargs-check-for-switch-to-alternate-min-logl)**()<br>Checks if some process has triggered the 'switch_to_alternate_min_LogL' function.  |

**Friends inherited from [Gambit::Scanner::Function_Base< ret(args...)>](/documentation/code/classes/classgambit_1_1scanner_1_1function__base_3_01ret_07args_8_8_8_08_4/)**

|                | Name           |
| -------------- | -------------- |
| class | **[Function_Deleter< ret(args...)>](/documentation/code/classes/classgambit_1_1scanner_1_1function__base_3_01ret_07args_8_8_8_08_4/#friend-gambitscannerfunction-base-retargs-function-deleter-retargs)**  |
| class | **[scan_ptr< ret(args...)>](/documentation/code/classes/classgambit_1_1scanner_1_1function__base_3_01ret_07args_8_8_8_08_4/#friend-gambitscannerfunction-base-retargs-scan-ptr-retargs)**  |

**Public Functions inherited from [Gambit::Scanner::Plugins::Plugin_Interface_Base](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1plugin__interface__base/)**

|                | Name           |
| -------------- | -------------- |
| | **[Plugin_Interface_Base](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1plugin__interface__base/#function-gambitscannerpluginsplugin-interface-base-plugin-interface-base)**() |
| YAML::Node | **[operator[]](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1plugin__interface__base/#function-gambitscannerpluginsplugin-interface-base-operator)**(const std::string & key) |
| | **[~Plugin_Interface_Base](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1plugin__interface__base/#function-gambitscannerpluginsplugin-interface-base-plugin-interface-base)**() |

**Protected Functions inherited from [Gambit::Scanner::Plugins::Plugin_Interface_Base](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1plugin__interface__base/)**

|                | Name           |
| -------------- | -------------- |
| template <typename... plug_args\> <br>const std::map< [type_index](/documentation/code/classes/structgambit_1_1type__index/), void * > & | **[initPlugin](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1plugin__interface__base/#function-gambitscannerpluginsplugin-interface-base-initplugin)**(const std::string & type, const std::string & name, const plug_args &... inputs) |

**Public Functions inherited from [Gambit::Scanner::Plugins::Plugin_Main_Interface_Base< ret(args...)>](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1plugin__main__interface__base_3_01ret_07args_8_8_8_08_4/)**

|                | Name           |
| -------------- | -------------- |
| | **[Plugin_Main_Interface_Base](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1plugin__main__interface__base_3_01ret_07args_8_8_8_08_4/#function-gambitscannerpluginsplugin-main-interface-base-retargs-plugin-main-interface-base)**() |
| int | **[enterMain](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1plugin__main__interface__base_3_01ret_07args_8_8_8_08_4/#function-gambitscannerpluginsplugin-main-interface-base-retargs-entermain)**(const std::string & name, const std::map< [type_index](/documentation/code/classes/structgambit_1_1type__index/), void * > & index_map) |
| ret | **[operator()](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1plugin__main__interface__base_3_01ret_07args_8_8_8_08_4/#function-gambitscannerpluginsplugin-main-interface-base-retargs-operator)**(const args &... params) |


## Detailed Description

```
template <typename ret ,
typename... args>
class Gambit::Scanner::Scanner_Plugin_Function< ret(args...)>;
```

Objective functor made up a single plugin. 
## Public Functions Documentation

### function Scanner_Plugin_Function

```
inline Scanner_Plugin_Function(
    const std::vector< std::string > & params,
    const std::string & name
)
```


### function main

```
inline ret main(
    const args &... in
)
```


-------------------------------

Updated on 2022-09-08 at 01:48:56 +0000