# The cudaComputeCapability Schema Schema

```txt
https://raw.githubusercontent.com/usnistgov/WIPP-Plugins-base-templates/master/plugin-manifest/schema/wipp-plugin-manifest-schema.json#/properties/resourceRequirements/properties/cudaRequirements/properties/cudaComputeCapability
```

Specify either a single minimum value, or an array of valid values


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [wipp-plugin.schema.json\*](wipp-plugin.schema.json "open original schema") |

## cudaComputeCapability Type

any of the folllowing: `string` or `array` ([The cudaComputeCapability Schema](wipp-plugin-properties-plugin-resource-requirements-properties-gpu-cuda-related-requirements-properties-the-cudacomputecapability-schema.md))

## cudaComputeCapability Examples

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
