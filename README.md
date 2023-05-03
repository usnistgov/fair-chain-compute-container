# Manifest Specification for Interoperable Containerized Computational Software (ICCS) 

## Purpose
This document describes a manifest file accompanying 
each containerized software algorithm (a computational tool) in order 
1. to make computational tools interoperable with other tools in terms of their inputs and outputs, 
2. to chain multiple tools into computational workflows to perform complex computations, and 
3. to execute workflows in distributed computational environments, 
such as computer clusters, computer clouds, and high-performance
computing (HPC) environments.

## Terminology
*Computational Software* is interchangeably used with the word *tool* or *algorithm* (computational tool or algorithm). 
In the context of *interoperable computational software*, computational tool or algorithm is also denoted as a *plugin* 
(computational plugin) 
since it is plugged into a chain of algorithms (i.e., a computational workflow) based on its interoperability property.   

## Folder Structure
The specification of a manifest file consists of 
- schema folder: JSON schema with all supported fields (entries)  
- docs folder: documentation about each field in a manifest file
- examples folder: Python and Java based image thresholding algorithms packaged into interoperable containerized tools
- request for feedback folder: A list of questions about the manifest file to provide feedback on 

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
for completing data analyses over very large data collections. 
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
in the GitHub repositories at NIST [URL](https://github.com/usnistgov/WIPP/tree/master/plugins) and at NCATS NIH 
[URL](https://github.com/PolusAI/polus-plugins). The software tools can also be searched and found via a tool registry, 
currently available for NIST tools at [URL](https://wipp-plugins.nist.gov/).

Other application use cases can be supported, for example, chemistry analyses, molecular modeling, genomics, 
or bioinformatics. The manifest specification is mainly focused on information 
pertinent to container execution and chaining into workflows (while being agnostic to the application context 
of container execution).


## Assistance in Building Interoperable Containerized Tools

- JSON schema that defines manifest file entries TO BE UPDATED [URL](https://github.com/usnistgov/WIPP-Plugins-base-templates/blob/master/plugin-manifest/schema/wipp-plugin-manifest-schema.json)
- Online creation and validation of manifest files  TO BE UPDATED [URL](https://usnistgov.github.io/WIPP-Plugin-Manifest-generator/)
- Example of an interoperable containerized tool for image thresholding [Basic thresholding in Python](sample-plugins/python-threshold)
- Step-by-step tutorial about building interoperable containerized tools TO BE UPDATED [URL](WIPP-plugins-tutorial-1.pdf)
- Best practices for containerizing software
- Best practices for exposing user interfaces using manifest entries


## Frequently Asked Questions

- How do I implement conditional input parameters for my container? [Answer]()


## Contacts

Please, do not hesitate to send email to [email]() if the current specification should be modified to meet your needs





