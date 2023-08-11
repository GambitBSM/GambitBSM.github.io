---
title: "1 - The GAMBIT Interface"
description: ""
date: 2022-07-01T22:31:46+01:00
lastmod: 2022-07-01T22:31:46+01:00
draft: false
images: []
menu:
  documentation:
    parent: "tutorials"
weight: 10
---

# 1 - The GAMBIT Interface

{{< alert icon="ⓘ" context="info">}}
**Info**: Unless otherwise stated, all relative file paths used in the following tutorials will be relative to the GAMBIT installation directory.
{{< /alert >}}

### Introduction to the interface

The GAMBIT interface has two main parts: a **master initialisation file** which is a YAML file containing the inputs from the user, and the **GAMBIT executable** which has a number of command line options.

Using this interface, the GAMBIT workflow consists of the following steps:

1. The user inputs what is to be calculated into the YAML file, and then gives the file to the GAMBIT executable.
2. GAMBIT works out how to carry out the scan, and a dependency resolver makes sure that everything takes place in the right order.
3. The scan is made and output is returned.
4. Plots are produced by [Pippi ⧉](https://github.com/patscott/pippi).

{{< alert icon="ⓘ" context="info">}}
**Info**: If you are interested in the inner workings of GAMBIT, or would like a full reference to the `gambit` command line options and YAML file syntax, please see [the original paper ⧉](https://arxiv.org/abs/1705.07908).
{{< /alert >}}

The top level of the master initialisation file contains eight entries specified by the user:

- `Parameters` describes the scan parameters for different models.
- `Priors` describes the priors to be placed on the scan parameters.
- `ObsLikes` describes observables and likelihoods that the user would like to be calculated in a scan.
- `Rules` specifies additional rules to guide the resolution of dependencies and backend requirements.
- `Printer` provides details about how and where to store the results of the scan.
- `Scanner` provides information about the scanning algorithm to be adopted in a scan.
- `Logger` chooses options for logging GAMBIT messages during the scan.
- `KeyValues` is an additional global option section.

To run the scan, the user runs the `gambit` executable with the `-f` flag:

```
./gambit -f $PATH_TO_YAML_FILE
```

### A first example

GAMBIT ships with a number of minimal example YAML files, found in `yaml_files/`. As a first example, try running the `spartan.yaml` file:

```
./gambit -f yaml_files/spartan.yaml
```

{{< alert icon="⚠" context="danger">}}

**Common Problems**: [When I try to run a scan, I get a `GAMBIT error` which says `Inifile entry _____ does not specify a valid _____!`](/documentation/help/common_problems_and_questions/#when-i-try-to-run-a-scan-i-get-a-gambit-error-which-says-inifile-entry-does-not-specify-a-valid)

{{< /alert >}}

{{< alert icon="ⓘ" context="info">}}

**Info**: If you have built GAMBIT while ditching modules, or have only installed the compulsory dependencies, it is highly likely that you will encounter `GAMBIT has exited with fatal exception: GAMBIT error` messages when running these examples. In these cases you may need to rebuild GAMBIT with new dependencies, or edit the YAML file to change the printer etc.

{{< /alert >}}

If GAMBIT has successfully run then you should receive the message `GAMBIT has finished successfully!`. By default, the results of this run will be saved in `runs/spartan`.

This example also comes with an accompanying `.pip` file, which is used to plot the results with Pippi. First make sure you have Pippi installed, either by cloning the [GitHub repository ⧉](https://github.com/patscott/pippi) or by using the built-in command `make get-pippi`.

{{< alert icon="ⓘ" context="info">}}

**Info**: Make sure that the version of Pippi that you install matches the Python version that you are using. The GitHub repository is updated for `python3`, however `make get-pippi` may download the `python2` version.

{{< /alert >}}

Pippi also requires some additional dependencies:

- The Python packages `scipy` and `h5py`, which can be installed using `pip`.
- The Ruby plotting package `ctioga2`, which can be installed using the Ruby package manager `gem`. Full instructions can be found [here ⧉](https://ctioga2.sourceforge.net/install.html).

After installing these, you can plot the results using:

```
pippi yaml_files/spartan.pip
```

This will produce plots in `runs/spartan/plots`. Note that in order to work properly, `pippi` should be called from the base `gambit` install directory.

{{< alert icon="⚠" context="danger">}}

**Common Problems**: [Running `pippi` gives me the error `undefined symbol: rb_safe_level error`](/documentation/help/common_problems_and_questions/#running-pippi-gives-me-the-error-undefined-symbol-rb-safe-level-error)

{{< /alert >}}

If everything works correctly, you should end up with three plots which look similar to those below.

<table>
  <tr>
    <td><img src="/images/tutorial1.png" alt="tutorial1" style="width:200px">
    </td>
   <td><img src="/images/tutorial2.png" alt="tutorial2" style="width:200px">
    </td>
    <td><img src="/images/tutorial3.png" alt="tutorial3" style="width:200px"> 
    </td>
  </tr>
</table>
