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

A pre-built version of GAMBIT is available as a Docker image which can be downloaded and run locally. This is useful for trying out GAMBIT and following the [examples on this site](/documentation/examples/colliderbit/) without the need to build GAMBIT from source.

{{< alert icon="ⓘ" context="info">}}

**Info**:
- The current Docker image is based on GAMBIT v1.1.3, which is outdated and will not provide the latest features.
- The Docker engine requires administrator privileges in order to be activated. Therefore its use is not recommended on shared clusters.

{{< /alert >}}

### Setting up the Docker image

##### Install the Docker Engine

The Docker Engine is available for Windows, macOS and Linux. Follow [Docker's installation guide](https://docs.docker.com/engine/install/) to install it on your system.

##### Download the Docker image

The Docker image download is around 6GB. To download the Docker image, from the command line run:

```
docker pull gambitbsm/gambit-pippi
```

Then to run the Docker container run:

```
docker run -it gambitbsm/gambit-pippi
```

This will give you a `bash` shell with GAMBIT pre-built and ready to run.

{{< alert icon="⚠" context="danger">}}

**Common Problem**: Linux users may have difficulty starting the Docker daemon. See [here](/documentation/help/common_problems_and_questions#docker-not-starting) for more information.

{{< /alert >}}

### Using the Docker image

You will need to re-run the Docker container each time you wish to use GAMBIT. For basic guidance on how to use GAMBIT, please see the [Examples](/documentation/examples/) section.
