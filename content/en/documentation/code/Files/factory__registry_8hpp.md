---
title: "file Utils/factory_registry.hpp"

description: "[No description available]"

---

# file Utils/factory_registry.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Gambit::reg_elem](/documentation/code/classes/classgambit_1_1reg__elem/)**  |

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[REGISTER](/documentation/code/files/factory__registry_8hpp/#define-register)**(reg_map, tag, ...)  |
|  | **[REGISTER_ELEM](/documentation/code/files/factory__registry_8hpp/#define-register-elem)**(reg_map, tag, ...)  |
|  | **[gambit_registry](/documentation/code/files/factory__registry_8hpp/#define-gambit-registry)**  |

## Detailed Description


Utility functions used by ScannerBit and the GAMBIT printers to register available scanners and printers.



------------------


# Authors

(add name and date if you modify)

Gregory Martinez ([gregory.david.martinez@gmail.com](mailto:gregory.david.martinez@gmail.com)) 

2013 July 

2014 Feb

Pat Scott ([patscott@physics.mcgill.ca](mailto:patscott@physics.mcgill.ca)) 

2014 Mar

Ben Farmer ([ben.farmer@gmail.com](mailto:ben.farmer@gmail.com)) 

2014 May



------------------




## Macros Documentation

### define REGISTER

```
#define REGISTER(
    reg_map,
    tag,
    ...
)
REGISTER_ELEM(reg_map, #tag, __VA_ARGS__)
```


### define REGISTER_ELEM

```
#define REGISTER_ELEM(
    reg_map,
    tag,
    ...
)
namespace __gambit_registry__                                                                   \
{                                                                                               \
    namespace                                                                                   \
    {                                                                                           \
        template<>                                                                              \
        class __create_class__ < __VA_ARGS__ >                                                  \
        {                                                                                       \
        public:                                                                                 \
            __create_class__(decltype(reg_map) &creators)                                       \
            {                                                                                   \
                creators[ tag ] = __create_class__< __VA_ARGS__ >::init;                        \
            }                                                                                   \
                                                                                                \
            template<typename T, typename... args>                                              \
            static T *init(args... params)                                                      \
            {                                                                                   \
                return static_cast<T *>(new __VA_ARGS__ (std::forward<args>(params)...));       \
            }                                                                                   \
        };                                                                                      \
                                                                                                \
        template <>                                                                             \
        __create_class__ < __VA_ARGS__ > __reg_init__ < __VA_ARGS__ >::reg(reg_map);            \
    }                                                                                           \
}                                                                                                               \
```


### define gambit_registry

```
#define gambit_registry namespace __gambit_registry__                       \
{                                                   \
    namespace                                       \
    {                                               \
        template <class T>                          \
        class __create_class__ {};                  \
                                                    \
        template <class T>                          \
        struct __reg_init__                         \
        {                                           \
            static __create_class__ <T> reg;        \
        };                                          \
    }                                               \
}                                                   \
                                                    \
namespace                                           \
```


## Source code

```
//  GAMBIT: Global and Modular BSM Inference Tool
//  *********************************************
/// \file
///
///  Utility functions used by ScannerBit and the
///  GAMBIT printers to register available scanners
///  and printers.
///
///  *********************************************
///
///  Authors
///  =======
///
///  (add name and date if you modify)
///
///  \author Gregory Martinez
///          (gregory.david.martinez@gmail.com)
///  \date 2013 July
///  \date 2014 Feb
///
///  \author Pat Scott 
///          (patscott@physics.mcgill.ca)
///  \date 2014 Mar
///
///  \author Ben Farmer
///          (ben.farmer@gmail.com)
///  \date 2014 May
///
///  *********************************************

#ifndef __factory_registry_hpp__
#define __factory_registry_hpp__

#include <type_traits>
#include <utility>
#include <ostream>
#include <sstream>
#include <unordered_map>
#include <algorithm>

#define REGISTER(reg_map, tag, ...) REGISTER_ELEM(reg_map, #tag, __VA_ARGS__)

#define REGISTER_ELEM(reg_map, tag, ...)                                                        \
namespace __gambit_registry__                                                                   \
{                                                                                               \
    namespace                                                                                   \
    {                                                                                           \
        template<>                                                                              \
        class __create_class__ < __VA_ARGS__ >                                                  \
        {                                                                                       \
        public:                                                                                 \
            __create_class__(decltype(reg_map) &creators)                                       \
            {                                                                                   \
                creators[ tag ] = __create_class__< __VA_ARGS__ >::init;                        \
            }                                                                                   \
                                                                                                \
            template<typename T, typename... args>                                              \
            static T *init(args... params)                                                      \
            {                                                                                   \
                return static_cast<T *>(new __VA_ARGS__ (std::forward<args>(params)...));       \
            }                                                                                   \
        };                                                                                      \
                                                                                                \
        template <>                                                                             \
        __create_class__ < __VA_ARGS__ > __reg_init__ < __VA_ARGS__ >::reg(reg_map);            \
    }                                                                                           \
}                                                                                                               \

#define gambit_registry                             \
namespace __gambit_registry__                       \
{                                                   \
    namespace                                       \
    {                                               \
        template <class T>                          \
        class __create_class__ {};                  \
                                                    \
        template <class T>                          \
        struct __reg_init__                         \
        {                                           \
            static __create_class__ <T> reg;        \
        };                                          \
    }                                               \
}                                                   \
                                                    \
namespace                                           \


namespace Gambit
{

    template <typename T>
    class reg_elem : public std::unordered_map<std::string, T *>
    {
    private:
            
    public:
        std::string print()
        {
            std::ostringstream out;
            
            out << "The options are:  \n";
            for (auto it = this->begin(); it != this->end(); it++)
            {
                    out << "\t" << it->first << "\n";
            }
            
            return out.str();
        }
    };
}

#endif
```


-------------------------------

Updated on 2022-09-08 at 02:27:28 +0000
