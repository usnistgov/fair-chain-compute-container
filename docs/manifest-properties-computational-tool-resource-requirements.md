# Computational Tool Resource Requirements Schema

```txt
https://raw.githubusercontent.com/usnistgov/fair-chain-compute-container/master/schema/manifest.schema.json#/properties/resourceRequirements
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                            |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [manifest.schema.json\*](manifest.schema.json "open original schema") |


**Resource requirements** are optional and allow schedulers of container-based workflows to optimally choose computational nodes for running containers on distributed computational resources.  
Examples and documentation of schedulers and workflow management systems leveraging resource requirements:
- [Kubernetes Resource Management for Pods and Containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) allows for specifying resource `requests` and `limits` for `cpu`, `memory` and [`gpu`](https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/). Other ways of [assigning pods to nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/) can involve labels, taint and tolerations. Automatic labelling of nodes can be achieved using the [Kubernetes Node Feature Discovery add-on](https://github.com/kubernetes-sigs/node-feature-discovery), or vendor-specific add-ons such as Nvidia's [Gpu Feature Discovery](https://github.com/NVIDIA/gpu-feature-discovery/blob/main/README.md) or AMD's [Node Labeller](https://github.com/RadeonOpenCompute/k8s-device-plugin/tree/master/cmd/k8s-node-labeller).
- [CWL's resource requirements](https://www.commonwl.org/user_guide/topics/specifying-software-requirements.html) section allows for specifying a variety of [hardware resource requirements](https://www.commonwl.org/v1.0/CommandLineTool.html#ResourceRequirement) and some implementations support vendor-specific requirements for GPUs (see [*cwltool* extension for CUDA requirements](https://github.com/common-workflow-language/cwltool/blob/9ce1e47f86446c88d5818017d46492c508546076/cwltool/extensions.yml#L178)).
- Slurm's resource requests can take multiple forms, see for example [the *sbatch* documentation](https://slurm.schedmd.com/sbatch.html) for requesting [memory per node](https://slurm.schedmd.com/sbatch.html#OPT_mem), [cpus per task](https://slurm.schedmd.com/sbatch.html#OPT_cpus-per-task), a [total number of GPUs for a job](https://slurm.schedmd.com/sbatch.html#OPT_gpus) or the more generic [*gres* generic consumable resource requests](https://slurm.schedmd.com/sbatch.html#OPT_gres). Specific `feature` labels can also be assigned to nodes in the cluster and then be leveraged in requests using [*constraints*](https://slurm.schedmd.com/sbatch.html#OPT_constraint).


## resourceRequirements Type

`object` ([Computational Tool Resource Requirements](manifest-properties-computational-tool-resource-requirements.md))

## resourceRequirements Default Value

The default value is:

```json
{}
```

## resourceRequirements Examples

```json
{
  "ramMin": 2048,
  "coresMin": 1,
  "cpuAVX": true,
  "cpuAVX2": false,
  "gpu": true,
  "cudaRequirements": {
    "deviceMemoryMin": 100,
    "cudaComputeCapability": "8.0"
  }
}
```

# Computational Tool Resource Requirements Properties

| Property                              | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                     |
| :------------------------------------ | --------- | -------- | -------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ramMin](#ramMin)                     | `number`  | Optional | cannot be null | [Manifest schema](manifest-properties-computational-tool-resource-requirements-properties-minimum-ram-in-mebibytes-mi.md "https&#x3A;//raw.githubusercontent.com/usnistgov/fair-chain-compute-container/master/schema/manifest.schema.json#/properties/resourceRequirements/properties/ramMin")                                |
| [coresMin](#coresMin)                 | `number`  | Optional | cannot be null | [Manifest schema](manifest-properties-computational-tool-resource-requirements-properties-minimum-number-of-cpu-cores.md "https&#x3A;//raw.githubusercontent.com/usnistgov/fair-chain-compute-container/master/schema/manifest.schema.json#/properties/resourceRequirements/properties/coresMin")                              |
| [cpuAVX](#cpuAVX)                     | `boolean` | Optional | cannot be null | [Manifest schema](manifest-properties-computational-tool-resource-requirements-properties-advanced-vector-extensions-avx-cpu-capability-required.md "https&#x3A;//raw.githubusercontent.com/usnistgov/fair-chain-compute-container/master/schema/manifest.schema.json#/properties/resourceRequirements/properties/cpuAVX")     |
| [cpuAVX2](#cpuAVX2)                   | `boolean` | Optional | cannot be null | [Manifest schema](manifest-properties-computational-tool-resource-requirements-properties-advanced-vector-extensions-2-avx2-cpu-capability-required.md "https&#x3A;//raw.githubusercontent.com/usnistgov/fair-chain-compute-container/master/schema/manifest.schema.json#/properties/resourceRequirements/properties/cpuAVX2") |
| [gpu](#gpu)                           | `boolean` | Optional | cannot be null | [Manifest schema](manifest-properties-computational-tool-resource-requirements-properties-gpuaccelerator-required.md "https&#x3A;//raw.githubusercontent.com/usnistgov/fair-chain-compute-container/master/schema/manifest.schema.json#/properties/resourceRequirements/properties/gpu")                                       |
| [cudaRequirements](#cudaRequirements) | `object`  | Optional | cannot be null | [Manifest schema](manifest-properties-computational-tool-resource-requirements-properties-gpu-cuda-related-requirements.md "https&#x3A;//raw.githubusercontent.com/usnistgov/fair-chain-compute-container/master/schema/manifest.schema.json#/properties/resourceRequirements/properties/cudaRequirements")                    |

## ramMin




`ramMin`

-   is optional
-   Type: `number` ([Minimum RAM in mebibytes (Mi)](manifest-properties-computational-tool-resource-requirements-properties-minimum-ram-in-mebibytes-mi.md))
-   cannot be null
-   defined in: [Manifest schema](manifest-properties-computational-tool-resource-requirements-properties-minimum-ram-in-mebibytes-mi.md "https&#x3A;//raw.githubusercontent.com/usnistgov/fair-chain-compute-container/master/schema/manifest.schema.json#/properties/resourceRequirements/properties/ramMin")

### ramMin Type

`number` ([Minimum RAM in mebibytes (Mi)](manifest-properties-computational-tool-resource-requirements-properties-minimum-ram-in-mebibytes-mi.md))

### ramMin Examples

```json
2048
```

## coresMin




`coresMin`

-   is optional
-   Type: `number` ([Minimum number of CPU cores](manifest-properties-computational-tool-resource-requirements-properties-minimum-number-of-cpu-cores.md))
-   cannot be null
-   defined in: [Manifest schema](manifest-properties-computational-tool-resource-requirements-properties-minimum-number-of-cpu-cores.md "https&#x3A;//raw.githubusercontent.com/usnistgov/fair-chain-compute-container/master/schema/manifest.schema.json#/properties/resourceRequirements/properties/coresMin")

### coresMin Type

`number` ([Minimum number of CPU cores](manifest-properties-computational-tool-resource-requirements-properties-minimum-number-of-cpu-cores.md))

### coresMin Examples

```json
1
```

## cpuAVX




`cpuAVX`

-   is optional
-   Type: `boolean` ([Advanced Vector Extensions (AVX) CPU capability required](manifest-properties-computational-tool-resource-requirements-properties-advanced-vector-extensions-avx-cpu-capability-required.md))
-   cannot be null
-   defined in: [Manifest schema](manifest-properties-computational-tool-resource-requirements-properties-advanced-vector-extensions-avx-cpu-capability-required.md "https&#x3A;//raw.githubusercontent.com/usnistgov/fair-chain-compute-container/master/schema/manifest.schema.json#/properties/resourceRequirements/properties/cpuAVX")

### cpuAVX Type

`boolean` ([Advanced Vector Extensions (AVX) CPU capability required](manifest-properties-computational-tool-resource-requirements-properties-advanced-vector-extensions-avx-cpu-capability-required.md))

### cpuAVX Examples

```json
true
```

## cpuAVX2




`cpuAVX2`

-   is optional
-   Type: `boolean` ([Advanced Vector Extensions 2 (AVX2) CPU capability required](manifest-properties-computational-tool-resource-requirements-properties-advanced-vector-extensions-2-avx2-cpu-capability-required.md))
-   cannot be null
-   defined in: [Manifest schema](manifest-properties-computational-tool-resource-requirements-properties-advanced-vector-extensions-2-avx2-cpu-capability-required.md "https&#x3A;//raw.githubusercontent.com/usnistgov/fair-chain-compute-container/master/schema/manifest.schema.json#/properties/resourceRequirements/properties/cpuAVX2")

### cpuAVX2 Type

`boolean` ([Advanced Vector Extensions 2 (AVX2) CPU capability required](manifest-properties-computational-tool-resource-requirements-properties-advanced-vector-extensions-2-avx2-cpu-capability-required.md))

### cpuAVX2 Examples

```json
false
```

## gpu




`gpu`

-   is optional
-   Type: `boolean` ([GPU/accelerator required](manifest-properties-computational-tool-resource-requirements-properties-gpuaccelerator-required.md))
-   cannot be null
-   defined in: [Manifest schema](manifest-properties-computational-tool-resource-requirements-properties-gpuaccelerator-required.md "https&#x3A;//raw.githubusercontent.com/usnistgov/fair-chain-compute-container/master/schema/manifest.schema.json#/properties/resourceRequirements/properties/gpu")

### gpu Type

`boolean` ([GPU/accelerator required](manifest-properties-computational-tool-resource-requirements-properties-gpuaccelerator-required.md))

### gpu Examples

```json
true
```

## cudaRequirements




`cudaRequirements`

-   is optional
-   Type: `object` ([GPU Cuda-related requirements](manifest-properties-computational-tool-resource-requirements-properties-gpu-cuda-related-requirements.md))
-   cannot be null
-   defined in: [Manifest schema](manifest-properties-computational-tool-resource-requirements-properties-gpu-cuda-related-requirements.md "https&#x3A;//raw.githubusercontent.com/usnistgov/fair-chain-compute-container/master/schema/manifest.schema.json#/properties/resourceRequirements/properties/cudaRequirements")

### cudaRequirements Type

`object` ([GPU Cuda-related requirements](manifest-properties-computational-tool-resource-requirements-properties-gpu-cuda-related-requirements.md))

### cudaRequirements Default Value

The default value is:

```json
{}
```

### cudaRequirements Examples

```json
{
  "deviceMemoryMin": 100,
  "cudaComputeCapability": "8.0"
}
```
