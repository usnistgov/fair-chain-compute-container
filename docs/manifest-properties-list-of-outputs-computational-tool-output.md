# Computational tool output Schema

```txt
#/properties/outputs/items#/properties/outputs/items
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                            |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [manifest.schema.json\*](manifest.schema.json "open original schema") |

## items Type

`object` ([Computational tool output](manifest-properties-list-of-outputs-computational-tool-output.md))

# Computational tool output Properties

| Property                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                              |
| :-------------------------- | -------- | -------- | -------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name)               | `string` | Required | cannot be null | [Manifest schema](manifest-properties-list-of-outputs-computational-tool-output-properties-output-name.md "\#/properties/outputs/items/properties/name#/properties/outputs/items/properties/name")                      |
| [type](#type)               | `string` | Required | cannot be null | [Manifest schema](manifest-properties-list-of-outputs-computational-tool-output-properties-output-type.md "\#/properties/outputs/items/properties/type#/properties/outputs/items/properties/type")                      |
| [description](#description) | `string` | Required | cannot be null | [Manifest schema](manifest-properties-list-of-outputs-computational-tool-output-properties-output-description.md "\#/properties/outputs/items/properties/description#/properties/outputs/items/properties/description") |

## name




`name`

-   is required
-   Type: `string` ([Output name](manifest-properties-list-of-outputs-computational-tool-output-properties-output-name.md))
-   cannot be null
-   defined in: [Manifest schema](manifest-properties-list-of-outputs-computational-tool-output-properties-output-name.md "\#/properties/outputs/items/properties/name#/properties/outputs/items/properties/name")

### name Type

`string` ([Output name](manifest-properties-list-of-outputs-computational-tool-output-properties-output-name.md))

### name Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^[a-zA-Z0-9][-a-zA-Z0-9]*$
```

[try pattern](https://regexr.com/?expression=%5E%5Ba-zA-Z0-9%5D%5B-a-zA-Z0-9%5D*%24 "try regular expression with regexr.com")

### name Examples

```json
"outputCollection"
```

## type




`type`

-   is required
-   Type: `string` ([Output type](manifest-properties-list-of-outputs-computational-tool-output-properties-output-type.md))
-   cannot be null
-   defined in: [Manifest schema](manifest-properties-list-of-outputs-computational-tool-output-properties-output-type.md "\#/properties/outputs/items/properties/type#/properties/outputs/items/properties/type")

### type Type

`string` ([Output type](manifest-properties-list-of-outputs-computational-tool-output-properties-output-type.md))

### type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                 | Explanation |
| :-------------------- | ----------- |
| `"collection"`        |             |
| `"stitchingVector"`   |             |
| `"tensorflowModel"`   |             |
| `"tensorboardLogs"`   |             |
| `"csvCollection"`     |             |
| `"pyramid"`           |             |
| `"pyramidAnnotation"` |             |
| `"genericData"`       |             |

### type Examples

```json
"stitchingVector"
```

```json
"collection"
```

## description




`description`

-   is required
-   Type: `string` ([Output description](manifest-properties-list-of-outputs-computational-tool-output-properties-output-description.md))
-   cannot be null
-   defined in: [Manifest schema](manifest-properties-list-of-outputs-computational-tool-output-properties-output-description.md "\#/properties/outputs/items/properties/description#/properties/outputs/items/properties/description")

### description Type

`string` ([Output description](manifest-properties-list-of-outputs-computational-tool-output-properties-output-description.md))

### description Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^(.*)$
```

[try pattern](https://regexr.com/?expression=%5E(.*)%24 "try regular expression with regexr.com")

### description Examples

```json
"Output collection"
```
