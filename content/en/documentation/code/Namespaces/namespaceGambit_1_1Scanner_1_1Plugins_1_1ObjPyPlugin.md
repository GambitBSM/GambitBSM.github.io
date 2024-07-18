---
title: "namespace Gambit::Scanner::Plugins::ObjPyPlugin"

description: "[No description available]"

---

# namespace Gambit::Scanner::Plugins::ObjPyPlugin

[No description available]

## Functions

|                | Name           |
| -------------- | -------------- |
| EXPORT_SYMBOLS [pluginData](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugindata/) *& | **[pythonPluginData](/documentation/code/namespaces/namespacegambit_1_1scanner_1_1plugins_1_1objpyplugin/#function-pythonplugindata)**()<br>A function to export Python plugin data.  |
| EXPORT_SYMBOLS double | **[run](/documentation/code/namespaces/namespacegambit_1_1scanner_1_1plugins_1_1objpyplugin/#function-run)**(py::object & func, map_doub_type_ & map)<br>A function to execute a Python function with a map of doubles as an argument.  |
| template <typename T \> <br>T | **[get_inifile_value](/documentation/code/namespaces/namespacegambit_1_1scanner_1_1plugins_1_1objpyplugin/#function-get-inifile-value)**(const std::string & in)<br>A function to retrieve a value from the ini file.  |
| template <typename T \> <br>T | **[get_inifile_value](/documentation/code/namespaces/namespacegambit_1_1scanner_1_1plugins_1_1objpyplugin/#function-get-inifile-value)**(const std::string & in, const T & defaults)<br>A function to retrieve a value from the ini file with a default value.  |
| YAML::Node | **[get_inifile_node](/documentation/code/namespaces/namespacegambit_1_1scanner_1_1plugins_1_1objpyplugin/#function-get-inifile-node)**(const std::string & in)<br>A function to retrieve a node from the ini file.  |
| YAML::Node | **[get_inifile_node](/documentation/code/namespaces/namespacegambit_1_1scanner_1_1plugins_1_1objpyplugin/#function-get-inifile-node)**()<br>A function to retrieve the root node from the ini file.  |
| template <typename T \> <br>T & | **[get_input_value](/documentation/code/namespaces/namespacegambit_1_1scanner_1_1plugins_1_1objpyplugin/#function-get-input-value)**(int i)<br>A function to retrieve an input value of a specified type.  |
| [Gambit::Scanner::printer_interface](/documentation/code/namespaces/namespacegambit_1_1scanner/#typedef-printer-interface) & | **[get_printer](/documentation/code/namespaces/namespacegambit_1_1scanner_1_1plugins_1_1objpyplugin/#function-get-printer)**()<br>A function to retrieve the printer interface.  |
| [Gambit::Scanner::prior_interface](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/) & | **[get_prior](/documentation/code/namespaces/namespacegambit_1_1scanner_1_1plugins_1_1objpyplugin/#function-get-prior)**()<br>A function to retrieve the prior interface.  |
| std::vector< std::string > & | **[get_keys](/documentation/code/namespaces/namespacegambit_1_1scanner_1_1plugins_1_1objpyplugin/#function-get-keys)**()<br>A function to retrieve the keys.  |
| void | **[set_dimension](/documentation/code/namespaces/namespacegambit_1_1scanner_1_1plugins_1_1objpyplugin/#function-set-dimension)**(unsigned int val)<br>A function to set the dimension.  |
| void | **[print_parameters](/documentation/code/namespaces/namespacegambit_1_1scanner_1_1plugins_1_1objpyplugin/#function-print-parameters)**(std::unordered_map< std::string, double > & key_map)<br>A function to print parameters.  |


## Functions Documentation

### function pythonPluginData

```
EXPORT_SYMBOLS pluginData *& pythonPluginData()
```

A function to export Python plugin data. 

**Return**: Returns a reference to a pointer to the [pluginData](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugindata/) object. 

This function is used to export data related to the Python plugin. It returns a reference to a pointer to the [pluginData](/documentation/code/classes/structgambit_1_1scanner_1_1plugins_1_1plugindata/) object.


### function run

```
EXPORT_SYMBOLS double run(
    py::object & func,
    map_doub_type_ & map
)
```

A function to execute a Python function with a map of doubles as an argument. 

**Parameters**: 

  * **func** The Python function to be executed. 
  * **map** The map of doubles to be passed as an argument to the Python function. 


**Return**: Returns the result of the Python function execution as a double. 

This function is used to execute a Python function that is passed as an argument. The function is executed with a map of doubles as its argument.


### function get_inifile_value

```
template <typename T >
inline T get_inifile_value(
    const std::string & in
)
```

A function to retrieve a value from the ini file. 

**Parameters**: 

  * **in** The key for the value to be retrieved. 


**Template Parameters**: 

  * **T** The type of the value to be retrieved. 


**Return**: Returns the value from the ini file associated with the given key. If the key does not exist, an error message is printed and a default-constructed object of type T is returned. 

This function is used to retrieve a value of a specified type from the ini file. The key for the value is passed as a parameter to the function.


### function get_inifile_value

```
template <typename T >
T get_inifile_value(
    const std::string & in,
    const T & defaults
)
```

A function to retrieve a value from the ini file with a default value. 

**Parameters**: 

  * **in** The key for the value to be retrieved. 
  * **defaults** The default value to be returned if the key does not exist in the ini file. 


**Template Parameters**: 

  * **T** The type of the value to be retrieved. 


**Return**: Returns the value from the ini file associated with the given key. If the key does not exist, the default value is returned. 

This function is used to retrieve a value of a specified type from the ini file. The key for the value is passed as a parameter to the function. If the key does not exist in the ini file, a default value is returned.


### function get_inifile_node

```
inline YAML::Node get_inifile_node(
    const std::string & in
)
```

A function to retrieve a node from the ini file. 

**Parameters**: 

  * **in** The key for the node to be retrieved. 


**Return**: Returns the node from the ini file associated with the given key. 

This function is used to retrieve a node from the ini file. The key for the node is passed as a parameter to the function.


### function get_inifile_node

```
inline YAML::Node get_inifile_node()
```

A function to retrieve the root node from the ini file. 

**Return**: Returns the root node from the ini file. 

This function is used to retrieve the root node from the ini file. No parameters are required as it always returns the root node.


### function get_input_value

```
template <typename T >
T & get_input_value(
    int i
)
```

A function to retrieve an input value of a specified type. 

**Parameters**: 

  * **i** The index of the input value to be retrieved. 


**Template Parameters**: 

  * **T** The type of the input value to be retrieved. 


**Return**: Returns a reference to the input value at the given index. 

This function is used to retrieve an input value of a specified type from the input data. The index of the input value is passed as a parameter to the function.


### function get_printer

```
inline Gambit::Scanner::printer_interface & get_printer()
```

A function to retrieve the printer interface. 

**Return**: Returns a reference to the printer interface. 

This function is used to retrieve the printer interface from the plugin data. No parameters are required as it always returns the printer interface.


### function get_prior

```
inline Gambit::Scanner::prior_interface & get_prior()
```

A function to retrieve the prior interface. 

**Return**: Returns a reference to the prior interface. 

This function is used to retrieve the prior interface from the plugin data. No parameters are required as it always returns the prior interface.


### function get_keys

```
std::vector< std::string > & get_keys()
```

A function to retrieve the keys. 

**Return**: Returns a reference to the vector of keys. 

This function is used to retrieve the keys from the input data. No parameters are required as it always returns the keys.


### function set_dimension

```
void set_dimension(
    unsigned int val
)
```

A function to set the dimension. 

**Parameters**: 

  * **val** The value to be set as the dimension. 


This function is used to set the dimension in the input data. The dimension value is passed as a parameter to the function.


### function print_parameters

```
void print_parameters(
    std::unordered_map< std::string, double > & key_map
)
```

A function to print parameters. 

**Parameters**: 

  * **key_map** The map of parameters to be printed. 


This function is used to print parameters from the input data. The parameters are passed as a map where the key is the parameter name and the value is the parameter value.






-------------------------------

Updated on 2024-07-18 at 13:53:32 +0000