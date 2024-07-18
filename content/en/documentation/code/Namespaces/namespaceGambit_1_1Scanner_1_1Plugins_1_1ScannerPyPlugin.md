---
title: "namespace Gambit::Scanner::Plugins::ScannerPyPlugin"

description: "[No description available]"

---

# namespace Gambit::Scanner::Plugins::ScannerPyPlugin

[No description available]

## Classes

|                | Name           |
| -------------- | -------------- |
| struct | **[Gambit::Scanner::Plugins::ScannerPyPlugin::like_hypercube](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1like__hypercube/)** <br>A derived class of [like_ptr_base]() for managing [Function_Base](/documentation/code/classes/classgambit_1_1scanner_1_1function__base/) objects related to hypercubes.  |
| struct | **[Gambit::Scanner::Plugins::ScannerPyPlugin::like_physical](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1like__physical/)** <br>A derived class of [like_ptr_base]() for managing [Function_Base](/documentation/code/classes/classgambit_1_1scanner_1_1function__base/) objects related to physical properties.  |
| struct | **[Gambit::Scanner::Plugins::ScannerPyPlugin::like_prior_physical](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1like__prior__physical/)** <br>A derived class of [like_ptr_base]() for managing [Function_Base](/documentation/code/classes/classgambit_1_1scanner_1_1function__base/) objects related to physical priors.  |
| class | **[Gambit::Scanner::Plugins::ScannerPyPlugin::like_ptr_base](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1like__ptr__base/)** <br>A class that wraps a shared pointer to a [Function_Base](/documentation/code/classes/classgambit_1_1scanner_1_1function__base/) object.  |
| struct | **[Gambit::Scanner::Plugins::ScannerPyPlugin::prior_physical](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1prior__physical/)** <br>A derived class of [like_ptr_base](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1like__ptr__base/) for managing [Function_Base](/documentation/code/classes/classgambit_1_1scanner_1_1function__base/) objects related to physical priors.  |
| class | **[Gambit::Scanner::Plugins::ScannerPyPlugin::scanner_base](/documentation/code/classes/classgambit_1_1scanner_1_1plugins_1_1scannerpyplugin_1_1scanner__base/)** <br>A base class for scanner functionality.  |

## Functions

|                | Name           |
| -------------- | -------------- |
| EXPORT_SYMBOLS [pluginData](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugindata/) *& | **[pythonPluginData](/documentation/code/namespaces/namespacegambit_1_1scanner_1_1plugins_1_1scannerpyplugin/#function-pythonplugindata)**()<br>A function to export Python plugin data.  |
| template <typename T \> <br>T | **[get_inifile_value](/documentation/code/namespaces/namespacegambit_1_1scanner_1_1plugins_1_1scannerpyplugin/#function-get-inifile-value)**(const std::string & in)<br>A function to retrieve a value from the INI file.  |
| template <typename T \> <br>T | **[get_inifile_value](/documentation/code/namespaces/namespacegambit_1_1scanner_1_1plugins_1_1scannerpyplugin/#function-get-inifile-value)**(const std::string & in, const T & defaults)<br>A function to retrieve a value from the INI file.  |
| YAML::Node | **[get_inifile_node](/documentation/code/namespaces/namespacegambit_1_1scanner_1_1plugins_1_1scannerpyplugin/#function-get-inifile-node)**(const std::string & in)<br>A function to retrieve a node from the INI file.  |
| YAML::Node | **[get_inifile_node](/documentation/code/namespaces/namespacegambit_1_1scanner_1_1plugins_1_1scannerpyplugin/#function-get-inifile-node)**()<br>A function to retrieve the root node from the INI file.  |
| template <typename T \> <br>T & | **[get_input_value](/documentation/code/namespaces/namespacegambit_1_1scanner_1_1plugins_1_1scannerpyplugin/#function-get-input-value)**(int i)<br>A function to retrieve an input value by index.  |
| [Gambit::Scanner::printer_interface](/documentation/code/namespaces/namespacegambit_1_1scanner/#typedef-printer-interface) & | **[get_printer](/documentation/code/namespaces/namespacegambit_1_1scanner_1_1plugins_1_1scannerpyplugin/#function-get-printer)**()<br>A function to retrieve the printer interface.  |
| [Gambit::Scanner::prior_interface](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/) & | **[get_prior](/documentation/code/namespaces/namespacegambit_1_1scanner_1_1plugins_1_1scannerpyplugin/#function-get-prior)**()<br>A function to retrieve the prior interface.  |
| unsigned int & | **[get_dimension](/documentation/code/namespaces/namespacegambit_1_1scanner_1_1plugins_1_1scannerpyplugin/#function-get-dimension)**()<br>A function to retrieve the dimension.  |
| std::shared_ptr< [Gambit::Scanner::Function_Base](/documentation/code/classes/classgambit_1_1scanner_1_1function__base/)< double(std::unordered_map< std::string, double > &)> > | **[get_purpose](/documentation/code/namespaces/namespacegambit_1_1scanner_1_1plugins_1_1scannerpyplugin/#function-get-purpose)**(const std::string & purpose)<br>A function to retrieve a function object based on its purpose.  |


## Functions Documentation

### function pythonPluginData

```
EXPORT_SYMBOLS pluginData *& pythonPluginData()
```

A function to export Python plugin data. 

**Return**: Returns a reference to a pointer to the [pluginData](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugindata/) object. 

This function is used to export data related to the Python plugin. It returns a reference to a pointer to the [pluginData](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugindata/) object.


### function get_inifile_value

```
template <typename T >
T get_inifile_value(
    const std::string & in
)
```

A function to retrieve a value from the INI file. 

**Parameters**: 

  * **in** The key for which the value is to be retrieved from the INI file. 


**Template Parameters**: 

  * **T** The type of the value to be retrieved from the INI file. 


**Return**: Returns the value associated with the given key in the INI file. 

This function is used to retrieve a value from the INI file based on a given key. The key is passed as a parameter to the function.


### function get_inifile_value

```
template <typename T >
T get_inifile_value(
    const std::string & in,
    const T & defaults
)
```

A function to retrieve a value from the INI file. 

**Parameters**: 

  * **in** The key for which the value is to be retrieved from the INI file. 
  * **defaults** The default value to be returned if the key is not found in the INI file. 


**Template Parameters**: 

  * **T** The type of the value to be retrieved from the INI file. 


**Return**: Returns the value associated with the given key in the INI file, or the default value if the key is not found. 

This function is used to retrieve a value from the INI file based on a given key. If the key is not found, a default value is returned.


### function get_inifile_node

```
inline YAML::Node get_inifile_node(
    const std::string & in
)
```

A function to retrieve a node from the INI file. 

**Parameters**: 

  * **in** The key for which the node is to be retrieved from the INI file. 


**Return**: Returns the YAML::Node associated with the given key in the INI file. 

This function is used to retrieve a YAML::Node from the INI file based on a given key. The key is passed as a parameter to the function.


### function get_inifile_node

```
inline YAML::Node get_inifile_node()
```

A function to retrieve the root node from the INI file. 

**Return**: Returns the root YAML::Node of the INI file. 

This function is used to retrieve the root YAML::Node from the INI file.


### function get_input_value

```
template <typename T >
T & get_input_value(
    int i
)
```

A function to retrieve an input value by index. 

**Parameters**: 

  * **i** The index of the input value to be retrieved. 


**Template Parameters**: 

  * **T** The type of the input value to be retrieved. 


**Return**: Returns a reference to the input value at the given index. 

This function is used to retrieve an input value from a data structure based on the given index.


### function get_printer

```
inline Gambit::Scanner::printer_interface & get_printer()
```

A function to retrieve the printer interface. 

**Return**: Returns a reference to the printer interface. 

This function is used to retrieve a reference to the printer interface from the Gambit::Scanner namespace.


### function get_prior

```
inline Gambit::Scanner::prior_interface & get_prior()
```

A function to retrieve the prior interface. 

**Return**: Returns a reference to the prior interface. 

This function is used to retrieve a reference to the prior interface from the Gambit::Scanner namespace.


### function get_dimension

```
inline unsigned int & get_dimension()
```

A function to retrieve the dimension. 

**Return**: Returns a reference to the dimension. 

This function is used to retrieve a reference to the dimension. The dimension could represent various aspects depending on the context, such as the dimension of a data structure, a mathematical space, etc.


### function get_purpose

```
inline std::shared_ptr< Gambit::Scanner::Function_Base< double(std::unordered_map< std::string, double > &)> > get_purpose(
    const std::string & purpose
)
```

A function to retrieve a function object based on its purpose. 

**Parameters**: 

  * **purpose** The purpose of the function to be retrieved. 


**Return**: Returns a shared pointer to the function object associated with the given purpose. 

This function is used to retrieve a function object from the Gambit::Scanner namespace based on its purpose. The purpose is passed as a parameter to the function.






-------------------------------

Updated on 2024-07-18 at 13:53:32 +0000