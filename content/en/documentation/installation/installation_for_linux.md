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

# Installation for Linux

{{< alert icon="ⓘ" context="info">}}

**Info**: 

- If you intend to build the entirety of GAMBIT without optimisation, at least 10GB of RAM is required. Building with optimisation (for performance-critical applications) may require more than 20GB of RAM. If your system does not meet these requirements then consider [only partially building GAMBIT](/documentation/help/common_problems_and_questions#gambit-builds-extremely-slowly), or using the [Docker image](/documentation/installation/docker_usage).
- This guide assumes some knowledge of `bash` and the Linux command line. See the [Linux command line tutorial ⧉](https://www.linux.com/training-tutorials/how-use-linux-command-line-basics-cli/) for a basic introduction.
- If you encounter issues while following this guide then please refer to the "Common Problems" boxes or the [Common Problems and Questions](/documentation/help/common_problems_and_questions/) page.

{{< /alert >}}

### Installing compulsory dependencies

GAMBIT has a number of compulsory dependencies, which must be installed for GAMBIT to be built and run. Some basic information is provided for each dependency. When given the option, **it is almost always better to install from source than from a package manager**. Installing from source means that the package will be present on your system in the same structure and configuration as the developers intended, which cannot always be guaranteed when using package managers. This might save you some headaches when you configure CMake to build GAMBIT.

{{< alert icon="⚠" context="danger">}}

**Common Problems**: 

- [I don't know how to check if a package is already installed](/documentation/help/common_problems_and_questions#i-don-t-know-how-to-check-if-a-package-is-already-installed)
- [I don't know how to install packages](/documentation/help/common_problems_and_questions#i-don-t-know-how-to-install-packages)
- [I can't or don't want to install dependencies system-wide](/documentation/help/common_problems_and_questions#i-can-t-or-don-t-want-to-install-dependencies-system-wide)
- [My system cannot find an installed package](/documentation/help/common_problems_and_questions#my-system-cannot-find-an-installed-package)

{{< /alert >}}

##### C/C++ compiler

One of:
- GCC (GNU Compiler Collection) ≥ 9, 
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
- GFortran (GNU Fortran Compiler) ≥ 9 
- ifort (Intel Fortran Compiler) ≥ 15.0.2

<details>
  <summary>More info</summary>

  Some parts of GAMBIT are written in Fortran. GFortran is associated with GCC and ifort is associated with ICC, so depending on your C++ compiler you may already have a Fortran compiler installed.

  | Package name | Available via major Linux package managers | Binaries available | Can be built from source | Notes |
  | --- | --- | --- | --- | --- |
  | `gcc-gfortran` | [Yes ⧉](https://fortran-lang.org/learn/os_setup/install_gfortran#linux) | [Yes ⧉](https://gcc.gnu.org/wiki/GFortranBinaries) | [Yes ⧉](https://gcc.gnu.org/install/) as part of GCC | - |
  | `ifort` | No | Yes | No | Binaries can be downloaded as part of the [Intel oneAPI Base Toolkit ⧉](https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit.html#gs.a3697a) (which also includes the ICC C++ compiler) or from the [standalone component page ⧉](https://www.intel.com/content/www/us/en/developer/articles/tool/oneapi-standalone-components.html). |
</details>

##### Cmake ≥ 3.2.3

<details>
  <summary>More info</summary>

  GAMBIT uses the Cmake build system.

  | Package name | Available via major Linux package managers | Binaries available | Can be built from source | Notes |
  | --- | --- | --- | --- | --- |
  | `cmake` | Yes | [Yes ⧉](https://cmake.org/download/) | [Yes ⧉](https://cmake.org/install/) | - |
</details>

##### Python + modules

GAMBIT needs Python 3, and Python modules `numpy`, `future`, `datetime`, `pyyaml`, `re`, `os`, `sys`, `getopt`, `shutil`, and `itertools`

{{< alert icon="ⓘ" context="info">}}

**Info**: In addition to a standard Python installation, you will also need the optional Python Developer Package which includes extra libraries and header files.

{{< /alert >}}

<details>
  <summary>More info</summary>

  Depending on your current Python installation you might consider installing [Anaconda ⧉](https://www.anaconda.com/) instead, which packages Python along with various libraries and tools designed for scientific computing.

  | Package name | Available via major Linux package managers | Binaries available | Can be built from source | Notes |
  | --- | --- | --- | --- | --- |
  | `python3` | Yes | [Yes ⧉](http://www.aixtools.net/index.php/python3) | [Yes ⧉](https://www.python.org/downloads/source/) | - |
  | `python-dev` or `python-devel` or numbered variation | Yes | No | No | - |

  It is good practice to install Python modules within a virtual environment rather than system-wide; see [I can't or don't want to install dependencies system-wide](/documentation/help/common_problems_and_questions#i-can-t-or-don-t-want-to-install-dependencies-system-wide). 

  There are a number of Python package managers, however `pip` is the most common. If you have an up-to-date installation of Python then this should already be installed, otherwise refer to the [Pip installation page ⧉](https://pip.pypa.io/en/stable/installation/). With Python 3 the command to use may be `pip3` in place of `pip`. The individual modules can be installed using `pip install $MODULE_NAME`, and a list of installed modules can be viewed using `pip list`. Note that `re`, `os`, `sys`, `getopt`, `shutil`, and `itertools` are part of the Python Standard Library and should already be packaged with Python (attempting to install them with `pip` will result in `ERROR: No matching distribution found for $MODULE_NAME`).

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
  | `lapack` | Yes | [Yes ⧉](https://netlib.org/lapack/archives/) | [Yes ⧉](https://netlib.org/lapack/) | - |
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

The `cmake` command will automatically try to find the packages it needs to build GAMBIT. However, it will probably need some help via optional flags. Commonly used flags are listed below; you can add these to the `cmake` command using the syntax `FLAG=VALUE`.

If CMake cannot find a package then try adding a relevant flag. For example, Boost will usually require the addition of the `-DBoost_INCLUDE_DIR` flag pointing to the `include` subdirectory of the Boost installation directory.

A full list of flags and their values can be found at `/build/CMakeCache.txt` after every run, and examples of `cmake` commands can be found on the [Configuration Examples](/documentation/help/configuration_examples) page.

{{< alert icon="ⓘ" context="info">}}

**Info**: 

- If you need to re-run Cmake, make sure to remove the `build` directory via `rm -r build` and start over. Otherwise Cmake will use the cached settings from the previous run.
- Every time you run CMake, a detailed log file is generated at `/build/CMakeFiles/CMakeOutput.log`. This is useful for debugging.
- All `LIBRARY` or `LIBRARIES` flags should point to either the `lib` subdirectory of a package's installation directory, or a shared library file. Shared library files have the extension `.so` and are usually of the form `libPACKAGE_NAME.so`.

{{< /alert >}}

{{< alert icon="⚠" context="danger">}}

**Common Problems**: 

- [CMake is finding Python backends in a different place to the interpreter](/documentation/help/common_problems_and_questions#cmake-is-finding-python-backends-in-a-different-place-to-the-interpreter)
- [CMake cannot find the LAPACK libraries](/documentation/help/common_problems_and_questions#cmake-cannot-find-the-lapack-libraries)
- [Changing CMake flags does not change the output](/documentation/help/common_problems_and_questions#changing-cmake-flags-does-not-change-the-output)

{{< /alert >}}
  
  | Flag | Value | Description |
  | --- | --- | --- |
  | `-DBoost_INCLUDE_DIR` | Path | Shows CMake where to find the Boost `include` directory. |
  | `-DEIGEN3_INCLUDE_DIR` | Path | Shows CMake where to find the Eigen `include` directory. Since Eigen is header-only, point this towards the folder containing the downloaded headers. |
  | `-DGSL_CONFIG_EXECUTABLE` | Path | Shows CMake where to find the GSL config executable, usually located within the GSL install directory at `bin/gsl-config`. |
  | `-DGSL_INCLUDE_DIRS` | Path | Shows CMake where to find the GSL `include` directory. |
  | `-DGSL_LIBRARY` | Path | Shows CMake where to find the GSL `lib` directory. |
  | `-DPYTHON_EXECUTABLE` | Path | Shows CMake where to find the Python executable. If working from a virtual environment, this will default to the executable in the environment's `bin` directory. |
  | `-DPYTHON_INCLUDE_DIR` | Path | Shows CMake where to find the system's Python `include` directory, for example `/usr/include/python3.10`. |
  | `-DPYTHON_LIBRARY` | Path | Shows CMake where to find the system's Python library file. For example, `/usr/lib64/libpython3.10.so.1.0`. |
  | `-DLAPACK_LIBRARIES` | Path | Shows CMake where to find the LAPACK library file. For example, `/usr/lib64/liblapack.so.3`. |
  | `-DBLAS_LIBRARIES` | Path | Shows CMake where to find the Blas library file. For example, `/usr/lib64/libblas.so.3`. |
  | `-DPKG_CONFIG_EXECUTABLE` | Path | Shows CMake where to find the pkg-config config executable, usually located within the pkg-config install directory at `bin/pkg-config`. |
  | `DPKG_CONFIG_PATH` | Path | Shows CMake where to find the pkg-config installation directory. |
  | `-Ditch` | Semi-colon separated list of `Bits` and other components, surrounded by quotation marks | Ditches parts of GAMBIT that you don't intend to use. |
  | `-DCMAKE_BUILD_TYPE` | `Release`, `Debug` or `None` | Sets the build type |
  | `-DBUILD_FS_MODELS` | Semi-colon separated list of models, surrounded by quotation marks | Defines which FlexibleSUSY models to build (model names must correspond to directories in `/contrib/MassSpectra/flexiblesusy/models`). |
  | `-DCMAKE_C_COMPILER` | Path | Sets the C compiler. |
  | `-DCMAKE_C_flags` | C compiler flags | Adds additional C compiler flags. |
  | `-DCMAKE_CXX_COMPILER` | Path | Sets the C++ compiler. |
  | `-DCMAKE_CXX_FLAGS` | C++ compiler flags | Adds additional C++ compiler flags. |
  | `-DCMAKE_Fortran_COMPILER` | Path | Sets the Fortran compiler. |
  | `-DCMAKE_Fortran_FLAGS` | Fortran compiler flags | Adds additional Fortran compiler flags. |
  | `-DWITH_HEPMC` | `On` or `Off` | Switches HepMC on or off. |
  | `-DWITH_RESTFRAMES` | `On` or `Off` | Switches RestFrames on or off. |
  | `-DWITH_ROOT` | `On` or `Off` | Switches ROOT on or off. |
  | `-DPYTHIA_OPT` | `On` or `Off` | Switches Intel's multi-file interprocedural optimisation on or off (for use with Pythia). |
  | `-DCMAKE_VERBOSE_MAKEFILE` | `On` or `Off` | Switches verbose build output on or off, useful for debugging. |
  | `-DWITH_MPI` | `On` or `Off` | Switches MPI on or off. |
  | `-DWITH_YODA` | `On` or `Off` | Switches Yoda on or off. |
  | `-DSUPPRESS_LIBRARY_WARNINGS` | `On` or `Off` | Enables or disables suppression of some common compiler warnings that are due to external library headers. |
  | `-DHAVE_GRAPHVIZ` | `On` or `Off` | Enables or disables the creation of Graphviz files. |

Next, build GAMBIT's scanners, specifying the number of cores to use:

```
make -j$NUMBER_OF_CORES scanners
```

Then re-run CMake:

```
cmake ..
```

{{< alert icon="ⓘ" context="info">}}

**Info**: CMake caches the flags (and their values) for each run. Because you have already run CMake, you do not need to specify any flags this time around.

{{< /alert >}}

Then finally build GAMBIT:

```
make -j$NUMBER_OF_CORES gambit
```

{{< alert icon="⚠" context="danger">}}

**Common Problems**: 

- [GAMBIT builds extremely slowly](/documentation/help/common_problems_and_questions#gambit-builds-extremely-slowly)
- [Python header files are not found](/documentation/help/common_problems_and_questions#python-header-files-are-not-found)

{{< /alert >}}

### Using GAMBIT

Now that GAMBIT has been built, there should be a `gambit` executable in the directory above the `build` subdirectory. You can view the installed scanners using `./gambit scanners` and the installed backends using `./gambit backends`. You can also control the installation of backends using the following:

```
make -j$NUMBER_OF_CORES backends         # Install all backends
make -j$NUMBER_OF_CORES $BACKEND_NAME    # Install specific backend
make clean-$BACKEND_NAME                 # Clean specific backend
```

For basic guidance on how to use GAMBIT, please see the [tutorials section](/documentation/tutorials/).
