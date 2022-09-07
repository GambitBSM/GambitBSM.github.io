---
title: "namespace find_all_gambit_bits"

description: "[No description available]"

---

# namespace find_all_gambit_bits

[No description available]

## Functions

|                | Name           |
| -------------- | -------------- |
| def | **[get_bits_from_directory_list](/documentation/code/namespaces/namespacefind__all__gambit__bits/#function-get-bits-from-directory-list)**(gambit_directory gambit_directory) |
| def | **[write_list_to_yaml](/documentation/code/namespaces/namespacefind__all__gambit__bits/#function-write-list-to-yaml)**(list_of_bits list_of_bits, output_file output_file, yaml_key yaml_key ="gambit_bits") |

## Attributes

|                | Name           |
| -------------- | -------------- |
| | **[parser](/documentation/code/namespaces/namespacefind__all__gambit__bits/#variable-parser)**  |
| | **[required](/documentation/code/namespaces/namespacefind__all__gambit__bits/#variable-required)**  |
| | **[True](/documentation/code/namespaces/namespacefind__all__gambit__bits/#variable-true)**  |
| | **[help](/documentation/code/namespaces/namespacefind__all__gambit__bits/#variable-help)**  |
| | **[args](/documentation/code/namespaces/namespacefind__all__gambit__bits/#variable-args)**  |


## Functions Documentation

### function get_bits_from_directory_list

```
def get_bits_from_directory_list(
    gambit_directory gambit_directory
)
```




```
Get Gambit Bits.

Return a sorted list of directory names with "Bit" in the name. 
This effectively generates a list of all available Bits in Gambit based on the established nameing scheme inside the Gambit repository.

Args:
    gambit_directory (str): Directory to search in. To work properly this has to be the Gambit source directory.

Returns:
    list: sorted list of Gambit Bits, except ScannerBit
```


### function write_list_to_yaml

```
def write_list_to_yaml(
    list_of_bits list_of_bits,
    output_file output_file,
    yaml_key yaml_key ="gambit_bits"
)
```




```
Write given list to a yaml file.

Args:
    list_of_bits list(str): List of Gambit Bits.
    output_file (str): Path/name for the output file.
    yaml_key (str): Key which is used to write the yaml file.
```



## Attributes Documentation

### variable parser

```
parser =  argparse.ArgumentParser(description=);
```


### variable required

```
required;
```


### variable True

```
True;
```


### variable help

```
help;
```


### variable args

```
args =  parser.parse_args();
```





-------------------------------

Updated on 2022-09-07 at 23:22:07 +0000