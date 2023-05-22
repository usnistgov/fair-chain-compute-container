# Input options Schema

```txt
#/properties/inputs/items/properties/options#/properties/inputs/items/allOf/1/then/properties/options
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [manifest.schema.json\*](manifest.schema.json "open original schema") |

## options Type

`object` ([Input options](manifest-properties-list-of-inputs-input-allof-1-then-properties-input-options.md))

# Input options Properties

| Property          | Type    | Required | Nullable       | Defined by                                                                                                                                                                                                                                                |
| :---------------- | ------- | -------- | -------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [items](#values) | `object` | Optional | cannot be null | [Manifest schema](manifest-properties-list-of-inputs-input-allof-1-then-properties-input-options-properties-values.md "\#/properties/inputs/items/properties/options#/properties/inputs/items/allOf/1/then/properties/options/properties/items") |

## values

List of possible values


`values`

-   is optional
-   Type: `string[]`
-   cannot be null
-   defined in: [Manifest schema](manifest-properties-list-of-inputs-input-allof-0-then-properties-input-options-properties-values.md "\#/properties/inputs/items/properties/options#/properties/inputs/items/allOf/0/then/properties/options/properties/values")

### values Type

`string[]`

### values Constraints

**unique items**: all items in this array must be unique. Duplicates are not allowed.
