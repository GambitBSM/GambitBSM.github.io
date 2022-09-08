---
title: "class Gambit::BibTeX"

description: "[No description available]"

---

# class Gambit::BibTeX



[No description available]

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BibTeX](/documentation/code/classes/classgambit_1_1bibtex/)**([str](/documentation/code/namespaces/namespacegambit/) bibtex_file) |
| const [str](/documentation/code/namespaces/namespacegambit/) | **[filename](/documentation/code/classes/classgambit_1_1bibtex/)**() const |
| const std::vector< [str](/documentation/code/namespaces/namespacegambit/) > | **[getBibTeXEntries](/documentation/code/classes/classgambit_1_1bibtex/)**() const |
| const std::map< [str](/documentation/code/namespaces/namespacegambit/), std::map< [str](/documentation/code/namespaces/namespacegambit/), [str](/documentation/code/namespaces/namespacegambit/) > > | **[getBibTeXData](/documentation/code/classes/classgambit_1_1bibtex/)**() const |
| void | **[dropBibTeXFile](/documentation/code/classes/classgambit_1_1bibtex/)**([str](/documentation/code/namespaces/namespacegambit/) output_filename) const |
| void | **[dropBibTeXFile](/documentation/code/classes/classgambit_1_1bibtex/)**(std::vector< [str](/documentation/code/namespaces/namespacegambit/) > & citation_keys, [str](/documentation/code/namespaces/namespacegambit/) output_filename) const |
| void | **[dropTeXFile](/documentation/code/classes/classgambit_1_1bibtex/)**(std::vector< [str](/documentation/code/namespaces/namespacegambit/) > & citation_keys, [str](/documentation/code/namespaces/namespacegambit/) tex_filename, [str](/documentation/code/namespaces/namespacegambit/) bibtex_filename) const |
| void | **[addCitationKey](/documentation/code/classes/classgambit_1_1bibtex/)**(std::vector< [str](/documentation/code/namespaces/namespacegambit/) > & citationKeys, [str](/documentation/code/namespaces/namespacegambit/) bibkey) |

## Public Functions Documentation

### function BibTeX

```
BibTeX(
    str bibtex_file
)
```


### function filename

```
const str filename() const
```


### function getBibTeXEntries

```
const std::vector< str > getBibTeXEntries() const
```


### function getBibTeXData

```
const std::map< str, std::map< str, str > > getBibTeXData() const
```


### function dropBibTeXFile

```
void dropBibTeXFile(
    str output_filename
) const
```


### function dropBibTeXFile

```
void dropBibTeXFile(
    std::vector< str > & citation_keys,
    str output_filename
) const
```


### function dropTeXFile

```
void dropTeXFile(
    std::vector< str > & citation_keys,
    str tex_filename,
    str bibtex_filename
) const
```


### function addCitationKey

```
static void addCitationKey(
    std::vector< str > & citationKeys,
    str bibkey
)
```


-------------------------------

Updated on 2022-09-08 at 01:05:15 +0000