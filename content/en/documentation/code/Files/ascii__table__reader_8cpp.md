---
title: "file src/ascii_table_reader.cpp"

description: "[No description available]"

---

# file src/ascii_table_reader.cpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |

## Detailed Description


**Author**: Christoph Weniger [c.weniger@uva.nl](mailto:c.weniger@uva.nl)

**Date**: Dec 2014

Simple reader for ASCII tables



------------------

Authors (add name and date if you modify):



------------------




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
///
///  \author Christoph Weniger
///          <c.weniger@uva.nl>
///  \date Dec 2014
///
///  *********************************************

#include "gambit/Utils/ascii_table_reader.hpp"

namespace Gambit
{


  int ASCIItableReader::read(std::string filename)
  {
    std::ifstream in(filename.c_str(), std::ios::binary);
    if (in.fail())
    {
      std::ostringstream errmsg;
      errmsg << "Failed to read file '"<< filename <<"'. Check if file exists.";
      utils_error().raise(LOCAL_INFO, errmsg.str());
    }
    std::string line;
    while(std::getline(in, line))
    {
      if (line[0] == '#') continue;  // Ignore comments lines, starting with "#"
      std::stringstream ss(line);

      size_t i = 0;
      double tmp;
      while(ss >> tmp)
      {
        if ( i+1 > data.size() ) data.resize(i+1);
        data[i].push_back(tmp);
        i++;
      }
    }
    in.close();
    return 0;
  }


  void ASCIItableReader::setcolnames(std::vector<std::string> names)
  {
    if ( (int) names.size() == ncol )
    {
      size_t i = 0;
      for (auto it = names.begin(); it != names.end(); it++)
      {
        colnames[*it] = i;
        i++;
      }
    }
    else
    {
      std::cout << "Warning in ASCIItableReader: Column number incompatible." << std::endl;
    }
  }


}
```


-------------------------------

Updated on 2022-09-08 at 02:27:28 +0000
