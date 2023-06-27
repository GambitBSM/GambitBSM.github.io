---
title: "Docker Usage"
description: "Guide on how to run GAMBIT using the pre-build Docker image."
date: 2022-07-01T22:31:46+01:00
lastmod: 2022-07-01T22:31:46+01:00
draft: false
images: []
menu:
  documentation:
    parent: "installation"
weight: 20
---

# Docker Usage

A pre-built version of GAMBIT is available as a Docker image which can be downloaded and run locally. This is useful for trying out GAMBIT and following the [tutorials on this site](/documentation/tutorials/the_gambit_interface/) without the need to build GAMBIT from source.

{{< alert icon="ⓘ" context="info">}}

**Info**:
- The current Docker image is based on GAMBIT v2.4.0.
- The Docker engine requires administrator privileges in order to be activated. Therefore it may be less suited for use on shared clusters.

{{< /alert >}}

### Setting up the Docker image

##### Install the Docker Engine

The Docker Engine is available for Windows, macOS and Linux. Follow [Docker's installation guide ⧉](https://docs.docker.com/engine/install/) to install it on your system.

##### Download the Docker image

The Docker image download is around 6GB. To download the Docker image, from the command line run:

```
docker pull gambitbsm/gambit-pippi
```

Then to run the Docker container run:

```
docker run -it gambitbsm/gambit-pippi
```

This will give you a `bash` shell with GAMBIT pre-built and ready to run. To quit this GAMBIT environment, type `exit`.

{{< alert icon="⚠" context="danger">}}

**Common Problem**: [I cannot start or run Docker on Linux](/documentation/help/common_problems_and_questions#i-cannot-start-or-run-docker-on-linux)

{{< /alert >}}

### Using the Docker image

You will need to re-run the Docker container each time you wish to use GAMBIT. For basic guidance on how to use GAMBIT, please see the [tutorials section](/documentation/tutorials/).
