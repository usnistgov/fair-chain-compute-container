# Best Practices and Guidelines for Building Interoperable Computational Containers

This page summarizes best practices and guidelines for creating Interoperable and Chainable Computational Containers.  

## Software code guidelines

- Executable shall be able to run headless from a command-line
- Executable shall be able to read required and optional parameters from a Command-Line Interface (CLI)
    - Preferred format for CLI parameters: long options ("--argName value")
    - Examples of argument parsing libraries: Python [argparse](https://docs.python.org/3/library/argparse.html), Java [Apache Commons CLI](https://commons.apache.org/proper/commons-cli/usage.html), C++ [argparse](https://github.com/p-ranav/argparse)
- Logging should be meaningful to allow for debugging, different logging levels can be offered
- Input parameters should be sanity checked before starting the computational operations (i.e. check for presence of required parameters, validity of parameter values) and errors should be logged to inform user of potential parameter misconfiguration
- Source code should be open source and each version shall be approprietely tagged to ensure traceability and reproducibility of the computational results
- Source code should follow the code language best practices and be commented

## Container best practices

- The container image shall be created following the [Open Container Initiative (OCI) Image Format](https://github.com/opencontainers/image-spec) specification
    - When using Docker and Dockerfiles, the [Docker best practices for writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/) should be followed 
- The container image shall be built taking into account the [Singularity Best Practices for Docker images](https://docs.sylabs.io/guides/3.0/user-guide/singularity_and_docker.html#best-practices) in order to ensure interoperability in HPC environments, notably:
    - Placing necessary files in `$HOME` and `$TMP` should be avoided since it is common-practice in Singularity to automatically mount host folder to this location inside of the container during the execution
    - Using `WORKDIR` instruction before the final `ENTRYPOINT` or `CMD` instruction in the Dockerfile should be avoided since the `WORKDIR` instruction may be ignored by the Singularity runtime and result in the executable not being found. Use absolute path in `ENTRYPOINT` or `CMD` instructions instead.
