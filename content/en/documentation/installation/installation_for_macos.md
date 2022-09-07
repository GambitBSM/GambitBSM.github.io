---
title: "Installation for macOS"
description: ""
date: 2022-07-01T22:31:46+01:00
lastmod: 2022-07-01T22:31:46+01:00
draft: false
images: []
menu:
  documentation:
    parent: "installation"
weight: 50 
---

{{< alert icon="ⓘ" context="info">}}
**Info**: This guide has been reproduced from [Aaron Vincent's personal page ⧉](https://www.queensu.ca/academia/vincent/getting-gambit-run-osx-mojave)
{{< /alert >}}

1) Install Xcode command line tools
2) Install [Homebrew ⧉](https://brew.sh/)
3) Install the following packages using `brew install XXX`:

```
brew install gcc lapack boost gsl wget eigen pkg-config cmake libomp
```

3.5) On a fresh copy of OSX, linking will be fine; however you may find that, many of these will not be properly linked, since many `/usr/local/bin` directories are not owned by the owner (??!) `brew doctor` will tell you what is not linked, then `brew link XXX` will tell you what needs an ownership change, each of which can be done in the form (where you just need to change the relevant path):

```
sudo chown -R `whoami`:admin /usr/local/bin
```

1) open-mpi needs to be installed separately (i.e. without Homebrew). Go to https://www.open-mpi.org and follow the installation instructions.
2) get Gambit:

```
git clone https://github.com/patscott/gambit_1.1.git
```

(or whatever the repo you want is)

6) build gambit

```
cd gambit mkdir build
```

Now, gcc on OSX is a lie. It really calls clang. You want:

```
cmake -D CMAKE_CXX_COMPILER=g++-8 -D CMAKE_C_COMPILER=gcc-8 -D CMAKE_Fortran_COMPILER=gfortran-8 ..
```

7) make the scanners:

```
make -j4 scanners
```

(4 can be replaced by however many cores you have, you fancy person)

8) do the cmake step again

```
cmake -D CMAKE_CXX_COMPILER=g++-8 -D CMAKE_C_COMPILER=gcc-8 -D CMAKE_Fortran_COMPILER=gfortran-8 ..
```

9) actually build gambit

```
make -j4 gambit
```

10) if that worked, test it!

```
cd .. ./gambit backends ./gambit scanners
```

and make whatever you need by going back to the build

11) you should be in business. If gambit throws an error that looks pythony, try

```
export PYTHONHOME=/usr/lib/python2.7/ export PYTHONPATH=/usr/lib/python2.7/
```

(it complains about pythonhome, but really needs both...)