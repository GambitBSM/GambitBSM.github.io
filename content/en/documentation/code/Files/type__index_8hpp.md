---
title: "file Utils/type_index.hpp"

description: "[No description available]"

---

# file Utils/type_index.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[std](/documentation/code/namespaces/namespacestd/)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| struct | **[Gambit::type_index](/documentation/code/classes/structgambit_1_1type__index/)**  |
| struct | **[Gambit::type_hasher](/documentation/code/classes/structgambit_1_1type__hasher/)**  |
| struct | **[Gambit::type_equal_to](/documentation/code/classes/structgambit_1_1type__equal__to/)**  |
| struct | **[std::hash< Gambit::type_index >](/documentation/code/classes/structstd_1_1hash_3_01gambit_1_1type__index_01_4/)**  |
| struct | **[std::equal_to< Gambit::type_index >](/documentation/code/classes/structstd_1_1equal__to_3_01gambit_1_1type__index_01_4/)**  |

## Detailed Description


**Author**: Gregory Martinez ([gregory.david.martinez@gmail.com](mailto:gregory.david.martinez@gmail.com)) 

**Date**: Aug 2014

Variadic utilty functions.



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Variadic utilty functions.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Gregory Martinez
///          (gregory.david.martinez@gmail.com)
///  \date Aug 2014
///
///  *********************************************

#ifndef TYPE_INDEX_HPP
#define TYPE_INDEX_HPP

#include <typeinfo>
#include <functional>
#include <string>

namespace Gambit
{
        struct type_index
        {
        public:
                friend struct type_equal_to;
                friend struct std::equal_to<Gambit::type_index>;
                
                type_index(const std::type_info& __rhs)
                : _M_target(&__rhs) { }
                
                type_index(){}
                
                const std::type_info &operator=(const std::type_info& __rhs)
                {return *(_M_target = &__rhs);}

                bool operator==(const Gambit::type_index& __rhs) const
                { return *_M_target == *__rhs._M_target; }

                bool operator!=(const Gambit::type_index& __rhs) const
                { return *_M_target != *__rhs._M_target; }

                bool operator<(const Gambit::type_index& __rhs) const
                { return _M_target->before(*__rhs._M_target); }

                bool operator<=(const Gambit::type_index& __rhs) const
                { return !__rhs._M_target->before(*_M_target); }

                bool operator>(const Gambit::type_index& __rhs) const
                { return __rhs._M_target->before(*_M_target); }

                bool operator>=(const Gambit::type_index& __rhs) const
                { return !_M_target->before(*__rhs._M_target); }

                size_t hash_code() const
                //{ return _M_target->hash_code(); }
                { return std::hash<std::string>().operator()(_M_target->name()); }

                const char* name() const
                { return _M_target->name(); }

        private:
                const std::type_info* _M_target;
        };
        
        struct type_hasher 
        {
                std::size_t operator()(const Gambit::type_index& code) const
                {
                        return code.hash_code();
                }
        };
        
        struct type_equal_to 
        {
                bool operator()(const Gambit::type_index& lhs, const Gambit::type_index& rhs) const
                {
                        return *lhs._M_target == *rhs._M_target;
                }
        };
}

namespace std
{
        template<>
        struct hash<Gambit::type_index>
        {
                size_t operator()(const Gambit::type_index& __ti) const
                { return __ti.hash_code(); }
        };
        
        template<>
        struct equal_to<Gambit::type_index>
        {
                size_t operator()(const Gambit::type_index& lhs, const Gambit::type_index& rhs) const
                { return *lhs._M_target == *rhs._M_target; }
        };
}

#endif
```


-------------------------------

Updated on 2022-09-08 at 03:08:04 +0000
