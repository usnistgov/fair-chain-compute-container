# Manifest Specification for FAIR Containerized Computational Software (FAIR-CCS) 
<img src="logo.png" alt="container-based workflow" width="200" height="200">

## Purpose
This document describes a manifest file accompanying 
each containerized software algorithm (a computational tool) in order to
1. make computational tools interoperable with other tools in terms of their inputs and outputs, 
2. chain multiple tools into computational workflows to perform complex computations, and 
3. execute workflows in distributed computational environments, 
such as computer clusters, computer clouds, and high-performance
computing (HPC) environments. Overall, the goal is to create
Findable, Accessible, Interoperable, and Reusable (FAIR) Containerized 
Computational Software (FAIR-CCS). 

## Terminology
*Computational Software* is interchangeably used with the word *tool* or *algorithm* (computational tool or algorithm). 
In the context of *interoperable computational software*, computational tool or algorithm is also denoted as a *plugin* 
(computational plugin) 
since it is plugged into a chain of algorithms (i.e., a computational workflow) based on its interoperability property.   

## Folder Structure
This repository for the specification of a manifest file consists of:
- `schema` folder: JSON schema with all supported fields (entries)  
    - The schema for a manifest file consists of sections describing inputs, outputs, UI, and resource requirements. The sections for `inputs` and `outputs` allow chaining containers’ inputs and outputs. The section `ui` allows on-the-fly generation of web user interface for collecting input arguments for running an application packaged in the container. The section `resourceRequirements` allows schedulers of container-based workflows to optimally choose computational nodes for running containers on distributed computational resources.
- `docs` folder: Documentation about each field in a manifest file and general guidelines for building interoperable containerized computational tools
- `sample-tools` folder: Image thresholding and cropping algorithms packaged into interoperable containerized tools
- `request-for-feedback` folder: A list of questions about the manifest file to provide feedback on 

## Origin
A prototype of a container manifest was designed and tested by the Web Image Processing Pipelines project 
developed at NIST. The discussions about specifications of a container manifest file 
began at the 1st workshop on Interoperability of Web Computational Plugins for Large Microscopy Image Analyses
[URL](https://www.nist.gov/news-events/events/2019/12/interoperability-web-computational-plugins-large-microscopy-image).
The workshop report can be found at this [URL](https://www.nist.gov/publications/interoperability-web-computational-plugins-large-microscopy-image-analyses).
Additional contributions to the specifications of a container manifest file came from the Polus-AI project developed at 
NCATS NIH.

## Motivation
- With the increasing size of collected data, distributed computational environments provide an acceleration option 
for completing data analyses over very large data collections and for federated learning over many data collections. 
- In order to run heterogeneous analysis tools 
written in multiple programming languages and with many dependencies on other software libraries, 
containerization of tools offers a valuable solution for software
execution in distributed computational environments with heterogeneous hardware and software configuration at 
each computational node. 
- To facilitate reuse of tools and creations of increasingly complex computational analyses (workflows), 
containerized software tools must be interoperable as they are chained into workflows. The motivation behind this
manifest specification lies in defining fields describing each containerized software tool so that 
the tools can be chained into workflows and executed in distributed computational environments.

## Existing Interoperable Containerized Tools for Application Use Cases
The initial application use cases come from biomedical microscopy imaging domain since the advancements 
in microscope designs and acquisition automations have enabled generating terabyte-sized image collections 
in a relative short time spans. Examples of existing software tools for microscopy imaging use cases can be found 
in the [GitHub repositories at NIST](https://github.com/usnistgov/WIPP/tree/master/plugins) and 
[at NCATS NIH](https://github.com/PolusAI/polus-plugins). The software tools can also be searched and found via a tool registry, 
currently available for NIST tools at [this URL](https://wipp-plugins.nist.gov/).

Other application use cases can be supported, for example, chemistry analyses, molecular modeling, genomics, 
or bioinformatics. The manifest specification is mainly focused on information 
pertinent to container execution and chaining into workflows (while being agnostic to the application context 
of container execution).


## Assistance in Building Interoperable Containerized Tools

- [Containerized Tool Manifest](./schema/manifest.schema.json) - JSON schema that defines manifest file entries

- [Documentation](./docs/README.md)
    - [Manifest Schema documentation](./docs/manifest.md) - In-depth documentation of the manifest JSON schema
    - [Best practices](./docs/best-practices.md) - Best practices and guidelines for building interoperable containerized tools
- [Online Manifest Generator](https://usnistgov.github.io/WIPP-Plugin-Manifest-generator/) - Online creation and validation of manifest files 

- [Simple examples](./sample-tools) of interoperable containerized tools
    - [Basic thresholding in Python](./sample-tools/python-threshold) - Example of interoperable containerized tool for image thresholding 
    - [Image crop operation in Python](./sample-tools/python-crop) - Example of interoperable containerized tool for image cropping 


## Learn by example

- Under construction


## Contacts

Please, do not hesitate to [send email to our team](mailto:wipp-team@nist.gov) if the current specification should be modified to meet your needs





