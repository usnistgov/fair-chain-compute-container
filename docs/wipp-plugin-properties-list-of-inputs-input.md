# Input Schema

```txt
#/properties/inputs/items#/properties/inputs/items
```

Plugin input


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [wipp-plugin.schema.json\*](wipp-plugin.schema.json "open original schema") |

## items Type

`object` ([Input](wipp-plugin-properties-list-of-inputs-input.md))

all of

-   [Untitled undefined type in WIPP Plugin manifest](wipp-plugin-properties-list-of-inputs-input-allof-0.md "check type definition")
-   [Untitled undefined type in WIPP Plugin manifest](wipp-plugin-properties-list-of-inputs-input-allof-1.md "check type definition")

# Input Properties

| Property                    | Type      | Required | Nullable       | Defined by                                                                                                                                                                                              |
| :-------------------------- | --------- | -------- | -------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [name](#name)               | `string`  | Required | cannot be null | [WIPP Plugin manifest](wipp-plugin-properties-list-of-inputs-input-properties-input-name.md "\#/properties/inputs/items/properties/name#/properties/inputs/items/properties/name")                      |
| [type](#type)               | `string`  | Required | cannot be null | [WIPP Plugin manifest](wipp-plugin-properties-list-of-inputs-input-properties-input-type.md "\#/properties/inputs/items/properties/type#/properties/inputs/items/properties/type")                      |
| [description](#description) | `string`  | Required | cannot be null | [WIPP Plugin manifest](wipp-plugin-properties-list-of-inputs-input-properties-input-description.md "\#/properties/inputs/items/properties/description#/properties/inputs/items/properties/description") |
| [required](#required)       | `boolean` | Optional | cannot be null | [WIPP Plugin manifest](wipp-plugin-properties-list-of-inputs-input-properties-required-input.md "\#/properties/inputs/items/properties/required#/properties/inputs/items/properties/required")          |

## name

Input name as expected by the plugin CLI


`name`

-   is required
-   Type: `string` ([Input name](wipp-plugin-properties-list-of-inputs-input-properties-input-name.md))
-   cannot be null
-   defined in: [WIPP Plugin manifest](wipp-plugin-properties-list-of-inputs-input-properties-input-name.md "\#/properties/inputs/items/properties/name#/properties/inputs/items/properties/name")

### name Type

`string` ([Input name](wipp-plugin-properties-list-of-inputs-input-properties-input-name.md))

### name Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^[a-zA-Z0-9][-a-zA-Z0-9]*$
```

[try pattern](https://regexr.com/?expression=%5E%5Ba-zA-Z0-9%5D%5B-a-zA-Z0-9%5D*%24 "try regular expression with regexr.com")

### name Examples

```json
"inputImages"
```

```json
"fileNamePattern"
```

```json
"thresholdValue"
```

## type




`type`

-   is required
-   Type: `string` ([Input Type](wipp-plugin-properties-list-of-inputs-input-properties-input-type.md))
-   cannot be null
-   defined in: [WIPP Plugin manifest](wipp-plugin-properties-list-of-inputs-input-properties-input-type.md "\#/properties/inputs/items/properties/type#/properties/inputs/items/properties/type")

### type Type

`string` ([Input Type](wipp-plugin-properties-list-of-inputs-input-properties-input-type.md))

### type Constraints

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

### type Examples

```json
"collection"
```

```json
"string"
```

```json
"number"
```

## description




`description`

-   is required
-   Type: `string` ([Input description](wipp-plugin-properties-list-of-inputs-input-properties-input-description.md))
-   cannot be null
-   defined in: [WIPP Plugin manifest](wipp-plugin-properties-list-of-inputs-input-properties-input-description.md "\#/properties/inputs/items/properties/description#/properties/inputs/items/properties/description")

### description Type

`string` ([Input description](wipp-plugin-properties-list-of-inputs-input-properties-input-description.md))

### description Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^(.*)$
```

[try pattern](https://regexr.com/?expression=%5E(.*)%24 "try regular expression with regexr.com")

### description Examples

```json
"Input Images"
```

## required

Whether an input is required or not


`required`

-   is optional
-   Type: `boolean` ([Required input](wipp-plugin-properties-list-of-inputs-input-properties-required-input.md))
-   cannot be null
-   defined in: [WIPP Plugin manifest](wipp-plugin-properties-list-of-inputs-input-properties-required-input.md "\#/properties/inputs/items/properties/required#/properties/inputs/items/properties/required")

### required Type

`boolean` ([Required input](wipp-plugin-properties-list-of-inputs-input-properties-required-input.md))

### required Default Value

The default value is:

```json
true
```

### required Examples

```json
true
```
