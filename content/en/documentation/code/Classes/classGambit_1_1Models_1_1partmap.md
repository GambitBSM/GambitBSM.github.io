---
title: "class Gambit::Models::partmap"

description: "[No description available]"

---

# class Gambit::Models::partmap



[No description available]

## Public Functions

|                | Name           |
| -------------- | -------------- |
| std::pair< str, int > | **[get_antiparticle](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-get-antiparticle)**(std::pair< str, int > shortpr) const |
| std::pair< str, int > | **[get_antiparticle](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-get-antiparticle)**(str name, int index) const |
| std::pair< int, int > | **[get_antiparticle](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-get-antiparticle)**(std::pair< int, int > pdgpr) const |
| std::pair< int, int > | **[get_antiparticle](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-get-antiparticle)**(int pdgcode, int context) const |
| bool | **[has_antiparticle](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-has-antiparticle)**(std::pair< str, int > shortpr) const |
| bool | **[has_antiparticle](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-has-antiparticle)**(str name, int index) const |
| bool | **[has_antiparticle](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-has-antiparticle)**(std::pair< int, int > pdgpr) const |
| bool | **[has_antiparticle](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-has-antiparticle)**(int pdgcode, int context) const |
| bool | **[has_spinx2](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-has-spinx2)**(str long_name) const<br>Check if a particle has a spin (x2) entry, using the long name.  |
| bool | **[has_spinx2](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-has-spinx2)**(std::pair< int, int > pdgpr) const<br>Check if a particle has a spin (x2) entry, using the PDG code and context integer.  |
| bool | **[has_spinx2](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-has-spinx2)**(int pdg_code, int context) const |
| bool | **[has_spinx2](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-has-spinx2)**(std::pair< str, int > shortpr) const<br>Check if a particle has a spin (x2) entry, using the short name and index.  |
| bool | **[has_spinx2](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-has-spinx2)**(str name, int index) const |
| int | **[get_spinx2](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-get-spinx2)**(std::pair< int, int > pdgpr) const |
| int | **[get_spinx2](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-get-spinx2)**(int pdg_code, int context) const |
| int | **[get_spinx2](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-get-spinx2)**(str long_name) const |
| int | **[get_spinx2](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-get-spinx2)**(std::pair< str, int > shortpr) const |
| int | **[get_spinx2](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-get-spinx2)**(str name, int index) const |
| bool | **[has_chargex3](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-has-chargex3)**(str long_name) const<br>Check if a particle has a charge (x3) entry, using the long name.  |
| bool | **[has_chargex3](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-has-chargex3)**(std::pair< int, int > pdgpr) const<br>Check if a particle has a charge (x3) entry, using the PDG code and context integer.  |
| bool | **[has_chargex3](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-has-chargex3)**(int pdg_code, int context) const |
| bool | **[has_chargex3](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-has-chargex3)**(std::pair< str, int > shortpr) const<br>Check if a particle has a charge (x3) entry, using the short name and index.  |
| bool | **[has_chargex3](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-has-chargex3)**(str name, int index) const |
| int | **[get_chargex3](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-get-chargex3)**(std::pair< int, int > pdgpr) const |
| int | **[get_chargex3](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-get-chargex3)**(int pdg_code, int context) const |
| int | **[get_chargex3](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-get-chargex3)**(str long_name) const |
| int | **[get_chargex3](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-get-chargex3)**(std::pair< str, int > shortpr) const |
| int | **[get_chargex3](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-get-chargex3)**(str name, int index) const |
| bool | **[has_color](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-has-color)**(str long_name) const<br>Check if a particle has a color entry, using the long name.  |
| bool | **[has_color](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-has-color)**(std::pair< int, int > pdgpr) const<br>Check if a particle has a color entry, using the PDG code and context integer.  |
| bool | **[has_color](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-has-color)**(int pdg_code, int context) const |
| bool | **[has_color](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-has-color)**(std::pair< str, int > shortpr) const<br>Check if a particle has a color entry, using the short name and index.  |
| bool | **[has_color](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-has-color)**(str name, int index) const |
| int | **[get_color](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-get-color)**(std::pair< int, int > pdgpr) const |
| int | **[get_color](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-get-color)**(int pdg_code, int context) const |
| int | **[get_color](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-get-color)**(str long_name) const |
| int | **[get_color](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-get-color)**(std::pair< str, int > shortpr) const |
| int | **[get_color](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-get-color)**(str name, int index) const |
| | **[partmap](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-partmap)**()<br>Constructor.  |
| void | **[add](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-add)**(str long_name, std::pair< int, int > pdgpr, int spinx2, int chargex3, int color)<br>Add a new particle to the database.  |
| void | **[add_SM](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-add-sm)**(str long_name, std::pair< int, int > pdgpr, int spinx2, int chargex3, int color)<br>Add a new Standard Model particle to the database.  |
| void | **[add_generic](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-add-generic)**(str long_name, std::pair< int, int > pdgpr, int spinx2, int chargex3, int color)<br>Add a new generic particle class to the database.  |
| void | **[add_with_short_pair](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-add-with-short-pair)**(str long_name, std::pair< int, int > pdgpr, std::pair< str, int > shortpr, int spinx2, int chargex3, int color)<br>Add a new particle to the database with a short name and an index.  |
| void | **[add_SM_with_short_pair](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-add-sm-with-short-pair)**(str long_name, std::pair< int, int > pdgpr, std::pair< str, int > shortpr, int spinx2, int chargex3, int color)<br>Add a new Standard Model particle to the database with a short name and an index.  |
| std::pair< int, int > | **[pdg_pair](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-pdg-pair)**(str long_name) const<br>Retrieve the PDG code and context integer, from the long name.  |
| std::pair< int, int > | **[pdg_pair](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-pdg-pair)**(str short_name, int i) const<br>Retrieve the PDG code and context integer, from the short name and index.  |
| std::pair< int, int > | **[pdg_pair](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-pdg-pair)**(std::pair< str, int > shortpr) const<br>Retrieve the PDG code and context integer, from the short name and index pair.  |
| str | **[long_name](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-long-name)**(str short_name, int i) const<br>Retrieve the long name, from the short name and index.  |
| str | **[long_name](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-long-name)**(std::pair< int, int > pdgpr) const<br>Retrieve the long name, from the PDG code and context integer.  |
| str | **[long_name](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-long-name)**(int pdg_code, int context) const<br>Retrieve the long name, from the PDG code and context integer.  |
| std::pair< str, int > | **[short_name_pair](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-short-name-pair)**(str long_name) const<br>Retrieve the short name and index, from the long name.  |
| std::pair< str, int > | **[short_name_pair](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-short-name-pair)**(std::pair< int, int > pdgpr) const<br>Retrieve the short name and index, from the PDG code and context integer.  |
| std::pair< str, int > | **[short_name_pair](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-short-name-pair)**(int pdg_code, int context) const<br>Retrieve the short name and index, from the PDG code and context integer.  |
| const std::vector< std::pair< int, int > > & | **[get_SM_particles](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-get-sm-particles)**() const<br>Get a vector PDG codes and context integers of Standard Model particles in the database.  |
| const std::vector< std::pair< int, int > > & | **[get_generic_particles](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-get-generic-particles)**() const<br>Get a vector PDG codes and context integers of generic particle classes in the database.  |
| bool | **[has_particle](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-has-particle)**(str long_name) const<br>Check if a particle is in the database, using the long name.  |
| bool | **[has_particle](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-has-particle)**(str short_name, int i) const<br>Check if a particle is in the database, using the short name and index.  |
| bool | **[has_particle](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-has-particle)**(std::pair< str, int > shortpr) const |
| bool | **[has_particle](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-has-particle)**(std::pair< int, int > pdgpr) const<br>Check if a particle is in the database, using the PDG code and context integer.  |
| str | **[get_antiparticle](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-get-antiparticle)**(str lname) const<br>Get the matching anti-particle long name for a particle in the database, using the long name.  |
| bool | **[has_antiparticle](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-has-antiparticle)**(str long_name) const<br>Check if a particle has a matching anti-particle in the database, using the long name.  |
| bool | **[has_short_name](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-has-short-name)**(str long_name) const<br>Check if a particle has a short name, using the long name.  |
| bool | **[has_short_name](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-has-short-name)**(std::pair< int, int > pdgpr) const<br>Check if a particle has a short name, using the PDG code and context integer.  |
| void | **[check_contents](/documentation/code/classes/classgambit_1_1models_1_1partmap/#function-check-contents)**() const<br>For debugging: use to check the contents of the particle database.  |

## Public Functions Documentation

### function get_antiparticle

```
std::pair< str, int > get_antiparticle(
    std::pair< str, int > shortpr
) const
```


Get the matching anti-particle short name and index for a particle in the database, using the short name and index 


### function get_antiparticle

```
std::pair< str, int > get_antiparticle(
    str name,
    int index
) const
```


### function get_antiparticle

```
std::pair< int, int > get_antiparticle(
    std::pair< int, int > pdgpr
) const
```


Get the matching anti-particle PDG code and index for a particle in the database, using the PDG code and index 


Antiparticles are identified by having the opposite sign PDG code to a particle

Else assume particle is its own antiparticle (if this may not be true, use has_anti_particle to check explicitly for match)


### function get_antiparticle

```
std::pair< int, int > get_antiparticle(
    int pdgcode,
    int context
) const
```


### function has_antiparticle

```
bool has_antiparticle(
    std::pair< str, int > shortpr
) const
```


Check if a particle has a matching anti-particle in the database, using the short name and index 


### function has_antiparticle

```
bool has_antiparticle(
    str name,
    int index
) const
```


### function has_antiparticle

```
bool has_antiparticle(
    std::pair< int, int > pdgpr
) const
```


Check if a particle has a matching anti-particle in the database, using the PDG code and context integer 


Antiparticles are identified by having the opposite sign PDG code to a particle


### function has_antiparticle

```
bool has_antiparticle(
    int pdgcode,
    int context
) const
```


### function has_spinx2

```
bool has_spinx2(
    str long_name
) const
```

Check if a particle has a spin (x2) entry, using the long name. 



------------------


 Check if a particle has the spin (x2), using the long name 


### function has_spinx2

```
bool has_spinx2(
    std::pair< int, int > pdgpr
) const
```

Check if a particle has a spin (x2) entry, using the PDG code and context integer. 

Check if a particle has the spin (x2), using the PDG code and context integer 


### function has_spinx2

```
bool has_spinx2(
    int pdg_code,
    int context
) const
```


### function has_spinx2

```
bool has_spinx2(
    std::pair< str, int > shortpr
) const
```

Check if a particle has a spin (x2) entry, using the short name and index. 

Check if a particle has the spin (x2), using short name and index 


### function has_spinx2

```
bool has_spinx2(
    str name,
    int index
) const
```


### function get_spinx2

```
int get_spinx2(
    std::pair< int, int > pdgpr
) const
```


Get spin (x2) of a given particle, using the PDG code and context integer

Get spin of a given particle, using the PDG code and context integer 


### function get_spinx2

```
int get_spinx2(
    int pdg_code,
    int context
) const
```


### function get_spinx2

```
int get_spinx2(
    str long_name
) const
```


Get spin (x2) of a given particle, using the long name

Get spin of a given particle, using the long name 


### function get_spinx2

```
int get_spinx2(
    std::pair< str, int > shortpr
) const
```


Get spin (x2) of a given particle, using the short name and index

Get spin of a given particle, using short name and index 


### function get_spinx2

```
int get_spinx2(
    str name,
    int index
) const
```


### function has_chargex3

```
bool has_chargex3(
    str long_name
) const
```

Check if a particle has a charge (x3) entry, using the long name. 

Check if a particle has the charge (x3), using the long name 


### function has_chargex3

```
bool has_chargex3(
    std::pair< int, int > pdgpr
) const
```

Check if a particle has a charge (x3) entry, using the PDG code and context integer. 

Check if a particle has the charge (x3), using the PDG code and context integer 


### function has_chargex3

```
bool has_chargex3(
    int pdg_code,
    int context
) const
```


### function has_chargex3

```
bool has_chargex3(
    std::pair< str, int > shortpr
) const
```

Check if a particle has a charge (x3) entry, using the short name and index. 

Check if a particle has the charge (x3), using short name and index 


### function has_chargex3

```
bool has_chargex3(
    str name,
    int index
) const
```


### function get_chargex3

```
int get_chargex3(
    std::pair< int, int > pdgpr
) const
```


Get charge (x3) of a given particle, using the PDG code and context integer

Get charge of a given particle, using the PDG code and context integer 


### function get_chargex3

```
int get_chargex3(
    int pdg_code,
    int context
) const
```


### function get_chargex3

```
int get_chargex3(
    str long_name
) const
```


Get charge (x3) of a given particle, using the long name

Get charge of a given particle, using the long name 


### function get_chargex3

```
int get_chargex3(
    std::pair< str, int > shortpr
) const
```


Get charge (x3) of a given particle, using the short name and index

Get charge of a given particle, using short name and index 


### function get_chargex3

```
int get_chargex3(
    str name,
    int index
) const
```


### function has_color

```
bool has_color(
    str long_name
) const
```

Check if a particle has a color entry, using the long name. 

Check if a particle has color information, using the long name 


### function has_color

```
bool has_color(
    std::pair< int, int > pdgpr
) const
```

Check if a particle has a color entry, using the PDG code and context integer. 

Check if a particle has color information, using the PDG code and context integer 


### function has_color

```
bool has_color(
    int pdg_code,
    int context
) const
```


### function has_color

```
bool has_color(
    std::pair< str, int > shortpr
) const
```

Check if a particle has a color entry, using the short name and index. 

Check if a particle has color information, using short name and index 


### function has_color

```
bool has_color(
    str name,
    int index
) const
```


### function get_color

```
int get_color(
    std::pair< int, int > pdgpr
) const
```


Get color of a given particle, using the PDG code and context integer 


### function get_color

```
int get_color(
    int pdg_code,
    int context
) const
```


### function get_color

```
int get_color(
    str long_name
) const
```


Get color of a given particle, using the long name 


### function get_color

```
int get_color(
    std::pair< str, int > shortpr
) const
```


Get color of a given particle, using the short name and index

Get color of a given particle, using short name and index 


### function get_color

```
int get_color(
    str name,
    int index
) const
```


### function partmap

```
partmap()
```

Constructor. 

### function add

```
void add(
    str long_name,
    std::pair< int, int > pdgpr,
    int spinx2,
    int chargex3,
    int color
)
```

Add a new particle to the database. 

### function add_SM

```
void add_SM(
    str long_name,
    std::pair< int, int > pdgpr,
    int spinx2,
    int chargex3,
    int color
)
```

Add a new Standard Model particle to the database. 

### function add_generic

```
void add_generic(
    str long_name,
    std::pair< int, int > pdgpr,
    int spinx2,
    int chargex3,
    int color
)
```

Add a new generic particle class to the database. 

### function add_with_short_pair

```
void add_with_short_pair(
    str long_name,
    std::pair< int, int > pdgpr,
    std::pair< str, int > shortpr,
    int spinx2,
    int chargex3,
    int color
)
```

Add a new particle to the database with a short name and an index. 

### function add_SM_with_short_pair

```
void add_SM_with_short_pair(
    str long_name,
    std::pair< int, int > pdgpr,
    std::pair< str, int > shortpr,
    int spinx2,
    int chargex3,
    int color
)
```

Add a new Standard Model particle to the database with a short name and an index. 

### function pdg_pair

```
std::pair< int, int > pdg_pair(
    str long_name
) const
```

Retrieve the PDG code and context integer, from the long name. 

### function pdg_pair

```
std::pair< int, int > pdg_pair(
    str short_name,
    int i
) const
```

Retrieve the PDG code and context integer, from the short name and index. 

### function pdg_pair

```
std::pair< int, int > pdg_pair(
    std::pair< str, int > shortpr
) const
```

Retrieve the PDG code and context integer, from the short name and index pair. 

### function long_name

```
str long_name(
    str short_name,
    int i
) const
```

Retrieve the long name, from the short name and index. 

### function long_name

```
str long_name(
    std::pair< int, int > pdgpr
) const
```

Retrieve the long name, from the PDG code and context integer. 

### function long_name

```
str long_name(
    int pdg_code,
    int context
) const
```

Retrieve the long name, from the PDG code and context integer. 

### function short_name_pair

```
std::pair< str, int > short_name_pair(
    str long_name
) const
```

Retrieve the short name and index, from the long name. 

### function short_name_pair

```
std::pair< str, int > short_name_pair(
    std::pair< int, int > pdgpr
) const
```

Retrieve the short name and index, from the PDG code and context integer. 

### function short_name_pair

```
std::pair< str, int > short_name_pair(
    int pdg_code,
    int context
) const
```

Retrieve the short name and index, from the PDG code and context integer. 

### function get_SM_particles

```
const std::vector< std::pair< int, int > > & get_SM_particles() const
```

Get a vector PDG codes and context integers of Standard Model particles in the database. 

Get a vector of PDG codes and context integers of Standard Model particles in the database. 


### function get_generic_particles

```
const std::vector< std::pair< int, int > > & get_generic_particles() const
```

Get a vector PDG codes and context integers of generic particle classes in the database. 

Get a vector of PDG codes and context integers of generic particle classes in the database. 


### function has_particle

```
bool has_particle(
    str long_name
) const
```

Check if a particle is in the database, using the long name. 

### function has_particle

```
bool has_particle(
    str short_name,
    int i
) const
```

Check if a particle is in the database, using the short name and index. 

### function has_particle

```
bool has_particle(
    std::pair< str, int > shortpr
) const
```


### function has_particle

```
bool has_particle(
    std::pair< int, int > pdgpr
) const
```

Check if a particle is in the database, using the PDG code and context integer. 

### function get_antiparticle

```
str get_antiparticle(
    str lname
) const
```

Get the matching anti-particle long name for a particle in the database, using the long name. 

### function has_antiparticle

```
bool has_antiparticle(
    str long_name
) const
```

Check if a particle has a matching anti-particle in the database, using the long name. 

Check if a particle has a matching anti-particle in the database, using the long name Note: will throw an error if the particle itself is not in the database! 


### function has_short_name

```
bool has_short_name(
    str long_name
) const
```

Check if a particle has a short name, using the long name. 

### function has_short_name

```
bool has_short_name(
    std::pair< int, int > pdgpr
) const
```

Check if a particle has a short name, using the PDG code and context integer. 

### function check_contents

```
void check_contents() const
```

For debugging: use to check the contents of the particle database. 

-------------------------------

Updated on 2025-02-12 at 16:10:32 +0000