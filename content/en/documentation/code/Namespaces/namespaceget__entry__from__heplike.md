---
title: "namespace get_entry_from_heplike"

description: "[No description available]"

---

# namespace get_entry_from_heplike

[No description available]

## Attributes

|                | Name           |
| -------------- | -------------- |
| | **[topdown](/documentation/code/namespaces/namespaceget__entry__from__heplike/)**  |
| | **[filename](/documentation/code/namespaces/namespaceget__entry__from__heplike/)**  |
| string | **[request](/documentation/code/namespaces/namespaceget__entry__from__heplike/)**  |



## Attributes Documentation

### variable topdown

```
topdown;
```


### variable filename

```
filename =  os.path.join(root, name);
```


### variable request

```
string request =  r'{}'.format(load(f, Loader=Loader)[str(sys.argv[2])]);
```





-------------------------------

Updated on 2022-09-08 at 01:05:15 +0000