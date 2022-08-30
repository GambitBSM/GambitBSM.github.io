---
title: "Installation for Linux"
description: ""
date: 2022-07-01T22:31:46+01:00
lastmod: 2022-07-01T22:31:46+01:00
draft: false
images: []
menu:
  documentation:
    parent: "installation"
weight: 30
---

{{< alert icon="ⓘ" context="info">}}

**Info**: If you intend to build the entirety of GAMBIT without optimisation, at least 10GB of RAM is required. Building with optimisation (for performance-critical applications) may require more than 20GB of RAM. If your system does not meet these requirements then consider [only partially building GAMBIT](/documentation/help/common_problems_and_questions#gambit-builds-extremely-slowly), or using the [Docker image](/documentation/installation/docker_usage).

{{< /alert >}}

### Installing dependencies

GAMBIT is built using Cmake, and has a number of compulsory dependencies. Provided for each dependency is some basic information and installation instructions.

Before installing a dependency make sure to check if it is already present on your system, as multiple different installs of dependencies can cause issues during the build process. This can be done using the `whereis $PACKAGE_NAME` command which searches your system for the package's binary, source, or manual files. Additionally, the version number of many packages can be checked using `$PACKAGE_NAME --version`. 

{{< alert icon="⚠" context="danger">}}

**Common Problem**: [I don't know how to install a package](/documentation/help/common_problems_and_questions#i-don-t-know-how-to-install-a-package).

{{< /alert >}}

{{< alert icon="⚠" context="danger">}}

**Common Problem**: [I can't or don't want to install dependencies system-wide](/documentation/help/common_problems_and_questions#i-can-t-or-don-t-want-to-install-dependencies-system-wide).

{{< /alert >}}

{{< alert icon="⚠" context="danger">}}

**Common Problem**: [My system cannot find an installed package](/documentation/help/common_problems_and_questions#my-system-cannot-find-an-installed-package).

{{< /alert >}}

##### C++ compiler

GAMBIT requires one of `gcc` (GNU Compiler Collection) `>= 5.1`, `llvm clang >= 10`, or `icc` (Intel C/C++ Compiler) `>= 15.0.2`. It is likely that one of these is already present on your system. 

| Package name | Available via major Linux package managers | Can be build from source | Notes |
| --- | --- | --- | --- |
| `gcc` | Yes | [Yes ⧉](https://gcc.gnu.org/install/index.html) | - |
| `clang` | Yes | [Yes ⧉](https://clang.llvm.org/get_started.html) | - |
| `icc` | No | [Yes ⧉](http://registrationcenter-download.intel.com/akdlm/irc_nas/1855/l_cc_p_10.1.026_INSTALL.htm) | Can be downloaded as part of the [Intel oneAPI Base Toolkit ⧉](https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit.html#gs.a3697a), which also includes the `ifort` Fortran compiler (see next section). |

##### Fortran compiler

GAMBIT requires either `gfortran` (GNU Fortran Compiler) `>= 5.1` or `ifort` (Intel Fortran Compiler) `>= 15.0.2`. `gfortran` is associated with `gcc` and `ifort` is associated with `icc`, so depending on your C++ compiler you may already have a Fortran compiler installed.

*Installation*: `gfortran` is available via all major Linux package managers, see the [GFortran installation page ⧉](https://fortran-lang.org/learn/os_setup/install_gfortran#linux) for more information. `ifort` has been superceded by Intel oneAPI (see previous section), however it can still be downloaded from [Intel's standalone component page ⧉](https://www.intel.com/content/www/us/en/developer/articles/tool/oneapi-standalone-components.html#fortran).

| Package name | Available via major Linux package managers | Can be build from source | Notes |
| --- | --- | --- | --- |
| `gfortran` | Yes | [Yes ⧉](https://gcc.gnu.org/install/index.html) | - |
| `clang` | Yes | [Yes ⧉](https://clang.llvm.org/get_started.html) | - |
| `icc` | No | [Yes ⧉](http://registrationcenter-download.intel.com/akdlm/irc_nas/1855/l_cc_p_10.1.026_INSTALL.htm) | Can be downloaded as part of the [Intel oneAPI Base Toolkit ⧉](https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit.html#gs.a3697a), which also includes the `ifort` Fortran compiler (see next section). |

##### Cmake

*Info*: GAMBIT requires `cmake >= 2.8.12`.

---

*Installation*: Cmake source code or pre-built binaries can be downloaded from the [Cmake installation page ⧉](https://cmake.org/install/).

##### Python

*Info*: GAMBIT requires `python >= 2.7`. Python 2 and Python 3 are developed separately, but both are supported.

---

*Installation*: `python3` is available via all major Linux package managers. Alternatively, source code for both Python 3 and Python 2 can be downloaded from the [Python source releases page ⧉](https://www.python.org/downloads/source/). You might consider installing [Anaconda ⧉](https://www.anaconda.com/) instead, which packages Python along with various libraries and tools designed for scientific computing.

##### Python modules

*Info*: GAMBIT requires the Python modules `future`, `datetime`, `pyyaml`, `os`, `re`, `sys`, `getopt`, `shutil`, and `itertools`. It is good practice to install these within a virtual environment rather than system-wide; see [I can't or don't want to install dependencies system-wide](/documentation/help/common_problems_and_questions#i-can-t-or-don-t-want-to-install-dependencies-system-wide). 

---

*Installation*: There are a number of Python package managers, however `pip` is the most common. If you have an up-to-date installation of Python then this should already be installed, otherwise refer to the [Pip installation page ⧉](https://pip.pypa.io/en/stable/installation/). If you have Python 3 installed then you can optionally use the command `pip3` in place of `pip`. The individual modules can be installed using `pip install $MODULE_NAME`, and a list of installed modules can be viewed using `pip list`. Note that `os`, `sys`, `getopt`, `shutil`, and `itertools` are part of the Python Standard Library and should already be packaged with Python (attempting to install them with `pip` will result in `ERROR: No matching distribution found for $MODULE_NAME`).

{{< alert icon="ⓘ" context="info">}}

**Info**: Other package managers for Python modules are available, such as [Pipenv ⧉](https://pipenv.pypa.io/en/latest/) and [Poetry ⧉](https://python-poetry.org/). However, to avoid errors in the build process you should make sure to install all the Python modules using the same method.

{{< /alert >}}

##### Git

*Info*: GAMBIT requires the Git source control software.

---

*Installation*: `git` is available via all major Linux package managers. Alternatively, instructions for installing Git from source can be found on the [Git installation page ⧉](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

##### Boost

*Info*: GAMBIT requires `boost >= 1.48`. Boost is a set of commonly-used C++ libraries.

---

*Installation*: Boost needs to be installed from source. Refer to the [Boost user manual ⧉](https://www.boost.org/doc/libs/1_80_0/tools/build/doc/html/index.html#bbv2.installation) for installation instructions.

##### GNU Scientific Library (GSL)

*Info*: GAMBIT requires `gsl >= 2.1`. GSL is a C software library written for scientific applications.

---

*Installation*: 