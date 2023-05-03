# Output type Schema

```txt
#/properties/outputs/items/properties/type#/properties/outputs/items/properties/type
```




| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [wipp-plugin.schema.json\*](wipp-plugin.schema.json "open original schema") |

## type Type

`string` ([Output type](wipp-plugin-properties-list-of-outputs-plugin-output-properties-output-type.md))

## type Constraints

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

## type Examples

```json
"stitchingVector"
```

```json
"collection"
```
