---
title: "file Utils/ascii_table_reader.hpp"

description: "[No description available]"

---

# file Utils/ascii_table_reader.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Gambit::ASCIItableReader](/documentation/code/classes/classgambit_1_1asciitablereader/)**  |

## Detailed Description


Simple reader for ASCII tables



------------------

Authors (add name and date if you modify): 




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Simple reader for ASCII tables
///
///  *********************************************
///
///  Authors (add name and date if you modify):
//
///  \author Christoph Weniger
///          <c.weniger@uva.nl>
///  \date Dec 2014
///
///  *********************************************

#include <iostream>
#include <cstdlib>
#include <fstream>
#include <vector>
#include <map>
#include <sstream>

#include "gambit/Utils/standalone_error_handlers.hpp"
#include "gambit/Utils/local_info.hpp"

#ifndef __ASCIItableReader__
#define __ASCIItableReader__

// Usage:
//    ASCIItableReader ascii(filename);
//    ascii.setcolnames("mass", "BR1", "BR2");
//    std::cout << ascii["mass"][0] << std::endl;
//    std::cout << ascii["BR1"][1] << std::endl;
//    std::cout << ascii["BR2"][2] << std::endl;

namespace Gambit
{
  class ASCIItableReader
  {
    public:
      ASCIItableReader(std::string filename)
      {
        read(filename);
        ncol = data.size();
        nrow = data[0].size();
      };
      ASCIItableReader() : ncol(0), nrow(0) {};  // Dummy initializer
      ~ASCIItableReader() {}

      int read(std::string filename);
      void setcolnames(std::vector<std::string> names);

      template <typename... Args>
      void setcolnames(std::string name, Args... args)
      {
        std::vector<std::string> vec;
        vec.push_back(name);
        setcolnames(vec, args...);
      }
      template <typename... Args>
      void setcolnames(std::vector<std::string> vec, std::string name, Args... args)
      {
        vec.push_back(name);
        setcolnames(vec, args...);
      }

      const std::vector<double> & operator[] (int i) { return data[i]; };
      const std::vector<double> & operator[] (std::string name) { return data[colnames[name]]; };
      int getncol() { return ncol; }
      int getnrow() { return nrow; }

    private:
      std::vector<std::vector<double> > data;
      std::map<std::string, int> colnames;
      int ncol;
      int nrow;
  };
}

#endif // defined __ASCIItableReader__
```


-------------------------------

Updated on 2025-02-12 at 16:10:33 +0000
