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

**Info**: 

- If you intend to build the entirety of GAMBIT without optimisation, at least 10GB of RAM is required. Building with optimisation (for performance-critical applications) may require more than 20GB of RAM. If your system does not meet these requirements then consider [only partially building GAMBIT](/documentation/help/common_problems_and_questions#gambit-builds-extremely-slowly), or using the [Docker image](/documentation/installation/docker_usage).
- This guide assumes some knowledge of `bash` and the Linux command line. See the [Linux command line tutorial ⧉](https://www.linux.com/training-tutorials/how-use-linux-command-line-basics-cli/) for a basic introduction.
- If you encounter issues while following this guide then please refer to the "Common Problem" boxes or the [Common Problems and Questions](/documentation/help/common_problems_and_questions/) page.

{{< /alert >}}

### Installing compulsory dependencies

GAMBIT has a number of compulsory dependencies, which must be installed for GAMBIT to be built and run. Some basic information is provided for each dependency.

{{< alert icon="⚠" context="danger">}}

**Common Problems**: 

- [I don't know how to check if a package is already installed](/documentation/help/common_problems_and_questions#i-don-t-know-how-to-check-if-a-package-is-already-installed)
- [I don't know how to install packages](/documentation/help/common_problems_and_questions#i-don-t-know-how-to-install-packages)
- [I can't or don't want to install dependencies system-wide](/documentation/help/common_problems_and_questions#i-can-t-or-don-t-want-to-install-dependencies-system-wide)
- [My system cannot find an installed package](/documentation/help/common_problems_and_questions#my-system-cannot-find-an-installed-package)

{{< /alert >}}

##### C++ compiler

One of:
- GCC (GNU Compiler Collection) ≥ 5.1, 
- LLVM Clang ≥ 10 
- ICC (Intel C/C++ Compiler) ≥ 15.0.2

<details>
  <summary>More info</summary>
  Gambit is written mainly in C++. It is likely that one of these compilers is already present on your system. 

  | Package name | Available via major Linux package managers | Binaries available | Can be built from source | Notes |
  | --- | --- | --- | --- | --- |
  | `gcc` | Yes | [Yes ⧉](https://gcc.gnu.org/install/binaries.html) | [Yes ⧉](https://gcc.gnu.org/install/) | - |
  | `clang` | Yes | [Yes ⧉](https://releases.llvm.org/download.html) | [Yes ⧉](https://clang.llvm.org/get_started.html) | - |
  | `icc` | No | Yes | No | Binaries can be downloaded as part of the [Intel oneAPI Base Toolkit ⧉](https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit.html#gs.a3697a) (which also includes the Ifort Fortran compiler) or from the [standalone component page ⧉](https://www.intel.com/content/www/us/en/developer/articles/tool/oneapi-standalone-components.html). |
</details>

##### Fortran compiler

One of: 
- GFortran (GNU Fortran Compiler) ≥ 5.1 
- ifort (Intel Fortran Compiler) ≥ 15.0.2

<details>
  <summary>More info</summary>

  Some parts of GAMBIT are written in Fortran. GFortran is associated with GCC and ifort is associated with ICC, so depending on your C++ compiler you may already have a Fortran compiler installed.

  | Package name | Available via major Linux package managers | Binaries available | Can be built from source | Notes |
  | --- | --- | --- | --- | --- |
  | `gcc-gfortran` | [Yes ⧉](https://fortran-lang.org/learn/os_setup/install_gfortran#linux) | [Yes ⧉](https://gcc.gnu.org/wiki/GFortranBinaries) | [Yes ⧉](https://gcc.gnu.org/install/) as part of GCC | - |
  | `ifort` | No | Yes | No | Binaries can be downloaded as part of the [Intel oneAPI Base Toolkit ⧉](https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit.html#gs.a3697a) (which also includes the ICC C++ compiler) or from the [standalone component page ⧉](https://www.intel.com/content/www/us/en/developer/articles/tool/oneapi-standalone-components.html). |
</details>

##### Cmake ≥ 2.8.12

<details>
  <summary>More info</summary>

  GAMBIT uses the Cmake build system.

  | Package name | Available via major Linux package managers | Binaries available | Can be built from source | Notes |
  | --- | --- | --- | --- | --- |
  | `cmake` | Yes | [Yes ⧉](https://cmake.org/download/) | [Yes ⧉](https://cmake.org/install/) | - |
</details>

##### Python + modules

Python ≥ 2.7, and Python modules `future`, `datetime`, `pyyaml`, `re`, `os`, `sys`, `getopt`, `shutil`, and `itertools`

<details>
  <summary>More info</summary>

  Python 2 and Python 3 are developed separately, but both are supported. You might consider installing [Anaconda ⧉](https://www.anaconda.com/) instead, which packages Python along with various libraries and tools designed for scientific computing.

  | Package name | Available via major Linux package managers | Binaries available | Can be built from source | Notes |
  | --- | --- | --- | --- | --- |
  | `python3` | Yes | [Yes ⧉](http://www.aixtools.net/index.php/python3) | [Yes ⧉](https://www.python.org/downloads/source/) | - |
  | `python2` | No | [Yes ⧉](http://www.aixtools.net/index.php/python2) | [Yes ⧉](https://www.python.org/downloads/source/) | - |

  It is good practice to install Python modules within a virtual environment rather than system-wide; see [I can't or don't want to install dependencies system-wide](/documentation/help/common_problems_and_questions#i-can-t-or-don-t-want-to-install-dependencies-system-wide). 

  There are a number of Python package managers, however `pip` is the most common. If you have an up-to-date installation of Python then this should already be installed, otherwise refer to the [Pip installation page ⧉](https://pip.pypa.io/en/stable/installation/). If you have Python 3 installed then you can optionally use the command `pip3` in place of `pip`. The individual modules can be installed using `pip install $MODULE_NAME`, and a list of installed modules can be viewed using `pip list`. Note that `re`, `os`, `sys`, `getopt`, `shutil`, and `itertools` are part of the Python Standard Library and should already be packaged with Python (attempting to install them with `pip` will result in `ERROR: No matching distribution found for $MODULE_NAME`).

  {{< alert icon="ⓘ" context="info">}}

  **Info**: Other package managers for Python modules are available, such as [Pipenv ⧉](https://pipenv.pypa.io/en/latest/) and [Poetry ⧉](https://python-poetry.org/). However, to avoid errors in the build process you should make sure to install all the Python modules using the same method.

  {{< /alert >}}
  </details>

##### Git

<details>
  <summary>More info</summary>
  Git is used for version control.

  | Package name | Available via major Linux package managers | Binaries available | Can be built from source | Notes |
  | --- | --- | --- | --- | --- |
  | `git` | [Yes ⧉](https://git-scm.com/download/linux) | No | [Yes ⧉](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) | - |
</details>

##### Boost ≥ 1.48

<details>
  <summary>More info</summary>
  Boost is a set of commonly-used C++ libraries.

  | Package name | Available via major Linux package managers | Binaries available | Can be built from source | Notes |
  | --- | --- | --- | --- | --- |
  | `boost` | Yes | No | [Yes ⧉](https://www.boost.org/doc/libs/1_80_0/more/getting_started/unix-variants.html) | Most of the components of Boost are header-only. |
</details>

##### GSL (GNU Scientific Library) ≥ 2.1

<details>
  <summary>More info</summary>
  GSL is a C software library written for scientific applications.

  | Package name | Available via major Linux package managers | Binaries available | Can be built from source | Notes |
  | --- | --- | --- | --- | --- |
  | `gsl` | Yes | No | [Yes ⧉](https://www.gnu.org/software/gsl/) | - |
</details>

##### Eigen ≥ 3.1.0

<details>
  <summary>More info</summary>
  Eigen is a header-only C++ library for linear algebra.

  | Package name | Available via major Linux package managers | Binaries available | Can be built from source | Notes |
  | --- | --- | --- | --- | --- |
  | `eigen` | No | No | [Yes ⧉](http://eigen.tuxfamily.org/index.php?title=Main_Page#Download) | Eigen is a header-only library, so does not need to built. Installation involves simply downloading the folder of header files. |
</details>

##### LAPACK (Linear Algebra Package)

<details>
  <summary>More info</summary>
  LAPACK is a Fortran library for numerical linear algebra.

  | Package name | Available via major Linux package managers | Binaries available | Can be built from source | Notes |
  | --- | --- | --- | --- | --- |
  | `lapack` | Yes | [Yes ⧉](https://netlib.org/lapack/archives/) | [Yes ⧉](https://netlib.org/clapack/CLAPACK-3.1.1/INSTALL/lawn81.pdf) | - |
</details>

##### pkg-config

<details>
  <summary>More info</summary>
  pkg-config is a tool which makes sure correct compiler options are used on the command line.

  | Package name | Available via major Linux package managers | Binaries available | Can be built from source | Notes |
  | --- | --- | --- | --- | --- |
  | `pkg-config` | No | No | [Yes ⧉](https://pkgconfig.freedesktop.org/releases/) | - |
</details>

### Installing optional dependencies

GAMBIT has a number of optional dependencies which you may wish to install depending on how you plan to use GAMBIT.

<details>
  <summary>Show optional dependencies</summary>
  

  - HDF5 (for use of the hdf5 printer)
  - MPI (required for parallel sampling)
  - axel (speeds up downloads of backends and scanners)
  - graphviz (required for model hierarchy and dependency tree plots)
  - ROOT (required for RestFrames support in ColliderBit, or the GreAT scanner from ScannerBit)
  - Mathematica 7.0 or greater (required for the use of Mathematica backends and GUM)
  - UUID (required for the use of the WSTP interface for Mathematica backends and GUM)
  - X11 development libraries (required for the use of GUM)
  - Boost compiled libraries (required for the use of GUM):
      - Boost.Python
      - Boost.Filesystem
      - Boost.System
  - Python modules:
      - `cython` (required for using the classy backend)
      - `scipy` (required for using the MontePython or DarkAges backends)
      - `numpy` ≥ 1.12 (required for using the classy or DarkAges backends)
      - `dill` (required for using the DarkAges backend)
      - `pandas`, `numexpr` (required for using the MontePython backend)
      - `h5py` (required to use hdf5 utilities located in gambit/Printers/scripts)

</details>

### Downloading GAMBIT

GAMBIT source code can be obtained either by cloning the GitHub repository from the [GitHub page ⧉](https://github.com/GambitBSM) or by downloading a compressed `.zip` or `.tar.gz` file. In both cases you should download the most recent version available.

##### Cloning the repository

To clone the repository of version `*.*` into a specified `$FOLDER`, use the command:

```
git clone https://github.com/GambitBSM/gambit_*.*.git $FOLDER
```

##### Downloading compressed folders

To instead download a `.zip` or `.tar.gz` file, visit the [releases page ⧉](https://github.com/GambitBSM/gambit_2.2/tags) or run one of the following commands:

```
wget https://github.com/GambitBSM/gambit_2.2/archive/refs/tags/v*.*.*.zip       # Download .zip file
wget https://github.com/GambitBSM/gambit_2.2/archive/refs/tags/v*.*.*.tar.gz    # Download .tar.gz file
```

Note that these files have versions of the form `*.*.*`. Once downloaded, the files can be extracted via either:

```bash
tar -xvf v*.*.*.tar.gz    # Extract .tar.gz file
unzip v*.*.*.zip          # Extract .zip file
```

### Building GAMBIT

Navigate to the folder containing GAMBIT source code. Create a `build` directory and run Cmake:

```
mkdir build
cd build
cmake ..
```

{{< alert icon="ⓘ" context="info">}}

**Info**: 

- If you need to re-run Cmake, make sure to remove the `build` directory via `rm -r build` and start over. Otherwise Cmake will use the cached settings from the previous run.
- Every time you run CMake, a detailed log file is generated at `/build/CMakeFiles/CMakeOutput.log`. This is useful for debugging.

{{< /alert >}}

The `cmake` command will automatically try to find the packages it needs to build GAMBIT. However, it will probably need some help via optional flags. Commonly used flags are listed below; You can add these to the `cmake` command using the syntax `FLAG=VALUE`.
  
  | Flag | Value | Description |
  | --- | --- | --- |
  | `-DCMAKE_BUILD_TYPE` | `Release`, `Debug` or `None` | Sets the build type |
  | `-Ditch` | Semi-colon separated list of `Bits` and other components | Ditches parts of GAMBIT that you don't intend to use |
  | `-DBoost_INCLUDE_DIR` | Path | Shows CMake where to find the Boost `include` directory |
  | `-DEIGEN3_INCLUDE_DIR` | Path | Shows CMake where to find the Eigen `include` directory |
  | `-DPYTHON_EXECUTABLE` | Path | Shows CMake where to find the Python executable. If working from a virtual environment, this will default to the executable in the environment's directory |
  | `-DPYTHON_INCLUDE_DIR` | Path | Shows CMake where to find the Python `include` directory |
  | `-DPYTHON_LIBRARY` | Path | Shows CMake where to find the Python library folder |
  | `-DGSL_INCLUDE_DIR` | Path | Shows CMake where to find the GSL `include` directory |
  | `-DGSL_LIBRARY` | Path | Shows CMake where to find the GSL library folder |
  | `-DBUILD_FS_MODELS` | Semi-colon separated list of models | Defines which FlexibleSUSY models to build (model names must correspond to directories in `/contrib/MassSpectra/flexiblesusy/models`) |
  | `-DCMAKE_C_COMPILER` | Path | Sets the C compiler |
  | `-DCMAKE_C_flags` | C compiler flags | Adds additional C compiler flags |
  | `-DCMAKE_CXX_COMPILER` | Path | Sets the C++ compiler |
  | `-DCMAKE_CXX_FLAGS` | C++ compiler flags | Adds additional C++ compiler flags |
  | `-DCMAKE_Fortran_COMPILER` | Path | Sets the Fortran compiler |
  | `-DCMAKE_Fortran_FLAGS` | Fortran compiler flags | Adds additional Fortran compiler flags |
  | `-DWITH_HEPMC` | `On` or `Off` | Switches HepMC on or off |
  | `-DWITH_RESTFRAMES` | `On` or `Off` | Switches RestFrames on or off |
  | `-DWITH_ROOT` | `On` or `Off` | Switches ROOT on or off |
  | `-DPYTHIA_OPT` | `On` or `Off` | Switches Intel's multi-file interprocedural optimisation on or off (for use with Pythia) |
  | `-DCMAKE_VERBOSE_MAKEFILE` | `On` or `Off` | Switches verbose build output on or off, useful for debugging |
  | `-DWITH_MPI` | `On` or `Off` | Switches MPI on or off |
  | `-DSUPPRESS_LIBRARY_WARNINGS` | `On` or `Off` | Enables or disables suppression of some common compiler warnings that are due to external library headers |
  | `-DHAVE_GRAPHVIZ` | `On` or `Off` | Enables or disables the creation of Graphviz files |

A full list of flags and their values can be found at `/build/CMakeCache.txt` after every run.

Examples of `cmake` commands can be found on the [Configuration Examples](/documentation/help/configuration_examples) page.

{{< alert icon="⚠" context="danger">}}

**Common Problem**: [GAMBIT builds extremely slowly](/documentation/help/common_problems_and_questions#gambit-builds-extremely-slowly)

{{< /alert >}}

