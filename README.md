# README

This repository contains WIPP Plugin base Docker images and Dockerfile templates (usage examples), as well as information about WIPP Plugin manifests.

## What is a WIPP plugin?
A WIPP plugin (to be used in the [WIPP - Web Image Processing Pipelines system](https://github.com/usnistgov/WIPP)) consists of:
- a computational program packaged as a Docker image,
- a JSON manifest file describing the plugin.

## Base Docker images for WIPP plugins
- wipp/wipp-plugins-base:java-openjdk8
- wipp/wipp-plugins-base:c++-htgs-fastimage
- wipp/wipp-plugins-base:python3-tesnorflow-skimage
- wipp/wipp-plugins-base:imagej-fiji

## Dockerfile templates for WIPP plugins
- Java programm using `wipp/wipp-plugins-base:java-openjdk8`
- C++ program using `wipp/wipp-plugins-base:c++-htgs-fastimage`
- Python3/Tensorflow program using `wipp/wipp-plugins-base:python3-tensorflow-skimage`
- ImageJ macro using `wipp/wipp-plugins-base:imagej-fiji`

## JSON manifests for WIPP plugins
The JSON manifest describes the inputs and outputs of the plugin, specifies the Docker image of the plugin, and provides general information about the plugin (such as description, author, code repository, etc.).

### Examples of WIPP plugins manifests
Learn by example: the following link provides a list of WIPP plugins maintained by the WIPP team, along with their JSON manifests.  
[WIPP Plugins on Github](https://github.com/usnistgov/WIPP/tree/master/plugins)

### Supported input data types
- "collection": path to a WIPP images collection folder,
- "stitchingVector": path to a WIPP stitching vectors collection folder,
- "tensorflowModel": path to a WIPP Tensorflow model folder,
- "csvCollection": path to a WIPP CSV collection folder,
- "notebook": path to a Jupyter notebook file,
- "string",
- "number",
- "integer",
- "enum",
- "array": array of strings that will concatenated as a single string,
- "boolean".

### Supported output data types
- "collection": path to a WIPP images collection folder,
- "stitchingVector": path to a WIPP stitching vectors collection folder,
- "tensorflowModel": path to a WIPP Tensorflow model folder,
- "csvCollection": path to a WIPP CSV collection folder.
