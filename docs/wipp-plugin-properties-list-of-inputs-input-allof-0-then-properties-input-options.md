# Input options Schema

```txt
#/properties/inputs/items/properties/options#/properties/inputs/items/allOf/0/then/properties/options
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [wipp-plugin.schema.json\*](wipp-plugin.schema.json "open original schema") |

## options Type

`object` ([Input options](wipp-plugin-properties-list-of-inputs-input-allof-0-then-properties-input-options.md))

# Input options Properties

| Property          | Type    | Required | Nullable       | Defined by                                                                                                                                                                                                                                                |
| :---------------- | ------- | -------- | -------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [values](#values) | `array` | Optional | cannot be null | [WIPP Plugin manifest](wipp-plugin-properties-list-of-inputs-input-allof-0-then-properties-input-options-properties-values.md "\#/properties/inputs/items/properties/options#/properties/inputs/items/allOf/0/then/properties/options/properties/values") |

## values

List of possible values


`values`

-   is optional
-   Type: `string[]`
-   cannot be null
-   defined in: [WIPP Plugin manifest](wipp-plugin-properties-list-of-inputs-input-allof-0-then-properties-input-options-properties-values.md "\#/properties/inputs/items/properties/options#/properties/inputs/items/allOf/0/then/properties/options/properties/values")

### values Type

`string[]`

### values Constraints

**unique items**: all items in this array must be unique. Duplicates are not allowed.
