# Computational Tool Resource Requirements Schema

```txt
https://raw.githubusercontent.com/usnistgov/fair-chain-compute-container/master/schema/manifest.schema.json#/properties/resourceRequirements
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                            |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [manifest.schema.json\*](manifest.schema.json "open original schema") |

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
