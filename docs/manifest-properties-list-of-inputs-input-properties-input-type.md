# Input Type Schema

```txt
#/properties/inputs/items/properties/type#/properties/inputs/items/properties/type
```




| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                            |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [manifest.schema.json\*](manifest.schema.json "open original schema") |

## type Type

`string` ([Input Type](manifest-properties-list-of-inputs-input-properties-input-type.md))

## type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                 | Explanation |
| :-------------------- | ----------- |
| `"collection"`        |             |
| `"stitchingVector"`   |             |
| `"tensorflowModel"`   |             |
| `"csvCollection"`     |             |
| `"pyramid"`           |             |
| `"pyramidAnnotation"` |             |
| `"notebook"`          |             |
| `"genericData"`       |             |
| `"string"`            |             |
| `"number"`            |             |
| `"integer"`           |             |
| `"enum"`              |             |
| `"array"`             |             |
| `"boolean"`           |             |

## type Examples

```json
"collection"
```

```json
"string"
```

```json
"number"
```
