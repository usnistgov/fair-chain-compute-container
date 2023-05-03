# GPU Cuda-related requirements Schema

```txt
https://raw.githubusercontent.com/usnistgov/WIPP-Plugins-base-templates/master/plugin-manifest/schema/wipp-plugin-manifest-schema.json#/properties/resourceRequirements/properties/cudaRequirements
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [wipp-plugin.schema.json\*](wipp-plugin.schema.json "open original schema") |

## cudaRequirements Type

`object` ([GPU Cuda-related requirements](wipp-plugin-properties-plugin-resource-requirements-properties-gpu-cuda-related-requirements.md))

## cudaRequirements Default Value

The default value is:

```json
{}
```

## cudaRequirements Examples

```json
{
  "deviceMemoryMin": 100,
  "cudaComputeCapability": "8.0"
}
```

# GPU Cuda-related requirements Properties

| Property                                        | Type         | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                                      |
| :---------------------------------------------- | ------------ | -------- | -------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [deviceMemoryMin](#deviceMemoryMin)             | `number`     | Optional | cannot be null | [WIPP Plugin manifest](wipp-plugin-properties-plugin-resource-requirements-properties-gpu-cuda-related-requirements-properties-minimum-device-memory.md "https&#x3A;//raw.githubusercontent.com/usnistgov/WIPP-Plugins-base-templates/master/plugin-manifest/schema/wipp-plugin-manifest-schema.json#/properties/resourceRequirements/properties/cudaRequirements/properties/deviceMemoryMin")                  |
| [cudaComputeCapability](#cudaComputeCapability) | Unknown Type | Optional | cannot be null | [WIPP Plugin manifest](wipp-plugin-properties-plugin-resource-requirements-properties-gpu-cuda-related-requirements-properties-the-cudacomputecapability-schema.md "https&#x3A;//raw.githubusercontent.com/usnistgov/WIPP-Plugins-base-templates/master/plugin-manifest/schema/wipp-plugin-manifest-schema.json#/properties/resourceRequirements/properties/cudaRequirements/properties/cudaComputeCapability") |

## deviceMemoryMin




`deviceMemoryMin`

-   is optional
-   Type: `number` ([Minimum device memory](wipp-plugin-properties-plugin-resource-requirements-properties-gpu-cuda-related-requirements-properties-minimum-device-memory.md))
-   cannot be null
-   defined in: [WIPP Plugin manifest](wipp-plugin-properties-plugin-resource-requirements-properties-gpu-cuda-related-requirements-properties-minimum-device-memory.md "https&#x3A;//raw.githubusercontent.com/usnistgov/WIPP-Plugins-base-templates/master/plugin-manifest/schema/wipp-plugin-manifest-schema.json#/properties/resourceRequirements/properties/cudaRequirements/properties/deviceMemoryMin")

### deviceMemoryMin Type

`number` ([Minimum device memory](wipp-plugin-properties-plugin-resource-requirements-properties-gpu-cuda-related-requirements-properties-minimum-device-memory.md))

### deviceMemoryMin Examples

```json
100
```

## cudaComputeCapability

Specify either a single minimum value, or an array of valid values


`cudaComputeCapability`

-   is optional
-   Type: any of the folllowing: `string` or `array` ([The cudaComputeCapability Schema](wipp-plugin-properties-plugin-resource-requirements-properties-gpu-cuda-related-requirements-properties-the-cudacomputecapability-schema.md))
-   cannot be null
-   defined in: [WIPP Plugin manifest](wipp-plugin-properties-plugin-resource-requirements-properties-gpu-cuda-related-requirements-properties-the-cudacomputecapability-schema.md "https&#x3A;//raw.githubusercontent.com/usnistgov/WIPP-Plugins-base-templates/master/plugin-manifest/schema/wipp-plugin-manifest-schema.json#/properties/resourceRequirements/properties/cudaRequirements/properties/cudaComputeCapability")

### cudaComputeCapability Type

any of the folllowing: `string` or `array` ([The cudaComputeCapability Schema](wipp-plugin-properties-plugin-resource-requirements-properties-gpu-cuda-related-requirements-properties-the-cudacomputecapability-schema.md))

### cudaComputeCapability Examples

```json
"8.0"
```

```json
[
  "3.5",
  "5.0",
  "6.0",
  "7.0",
  "7.5",
  "8.0"
]
```
