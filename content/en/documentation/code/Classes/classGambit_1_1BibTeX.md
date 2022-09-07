---
title: "class Gambit::BibTeX"

description: "[No description available]"

---

# class Gambit::BibTeX



[No description available]

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BibTeX](/documentation/code/classes/classgambit_1_1bibtex/#function-bibtex)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) bibtex_file) |
| const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[filename](/documentation/code/classes/classgambit_1_1bibtex/#function-filename)**() const |
| const std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > | **[getBibTeXEntries](/documentation/code/classes/classgambit_1_1bibtex/#function-getbibtexentries)**() const |
| const std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > > | **[getBibTeXData](/documentation/code/classes/classgambit_1_1bibtex/#function-getbibtexdata)**() const |
| void | **[dropBibTeXFile](/documentation/code/classes/classgambit_1_1bibtex/#function-dropbibtexfile)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) output_filename) const |
| void | **[dropBibTeXFile](/documentation/code/classes/classgambit_1_1bibtex/#function-dropbibtexfile)**(std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > & citation_keys, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) output_filename) const |
| void | **[dropTeXFile](/documentation/code/classes/classgambit_1_1bibtex/#function-droptexfile)**(std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > & citation_keys, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) tex_filename, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) bibtex_filename) const |
| void | **[addCitationKey](/documentation/code/classes/classgambit_1_1bibtex/#function-addcitationkey)**(std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > & citationKeys, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) bibkey) |

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

Updated on 2022-09-07 at 23:22:05 +0000