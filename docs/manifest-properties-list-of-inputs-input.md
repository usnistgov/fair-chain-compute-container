# Input Schema

```txt
#/properties/inputs/items#/properties/inputs/items
```

Computational tool input


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                            |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [manifest.schema.json\*](manifest.schema.json "open original schema") |

## items Type

`object` ([Input](manifest-properties-list-of-inputs-input.md))

all of

-   [Untitled undefined type in Manifest schema](manifest-properties-list-of-inputs-input-allof-0.md "check type definition")
-   [Untitled undefined type in Manifest schema](manifest-properties-list-of-inputs-input-allof-1.md "check type definition")

# Input Properties

| Property                    | Type      | Required | Nullable       | Defined by                                                                                                                                                                                      |
| :-------------------------- | --------- | -------- | -------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name)               | `string`  | Required | cannot be null | [Manifest schema](manifest-properties-list-of-inputs-input-properties-input-name.md "\#/properties/inputs/items/properties/name#/properties/inputs/items/properties/name")                      |
| [type](#type)               | `string`  | Required | cannot be null | [Manifest schema](manifest-properties-list-of-inputs-input-properties-input-type.md "\#/properties/inputs/items/properties/type#/properties/inputs/items/properties/type")                      |
| [description](#description) | `string`  | Required | cannot be null | [Manifest schema](manifest-properties-list-of-inputs-input-properties-input-description.md "\#/properties/inputs/items/properties/description#/properties/inputs/items/properties/description") |
| [required](#required)       | `boolean` | Optional | cannot be null | [Manifest schema](manifest-properties-list-of-inputs-input-properties-required-input.md "\#/properties/inputs/items/properties/required#/properties/inputs/items/properties/required")          |
| [options](#options)       | `object` | Optional | cannot be null | [[Manifest schema](#/properties/inputs/items/properties/required#/properties/inputs/items/properties/options)          |


## name

Input name as expected by the computational tool CLI


`name`

-   is required
-   Type: `string` ([Input name](manifest-properties-list-of-inputs-input-properties-input-name.md))
-   cannot be null
-   defined in: [Manifest schema](manifest-properties-list-of-inputs-input-properties-input-name.md "\#/properties/inputs/items/properties/name#/properties/inputs/items/properties/name")

### name Type

`string` ([Input name](manifest-properties-list-of-inputs-input-properties-input-name.md))

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
-   Type: `string` ([Input Type](manifest-properties-list-of-inputs-input-properties-input-type.md))
-   cannot be null
-   defined in: [Manifest schema](manifest-properties-list-of-inputs-input-properties-input-type.md "\#/properties/inputs/items/properties/type#/properties/inputs/items/properties/type")

### type Type

`string` ([Input Type](manifest-properties-list-of-inputs-input-properties-input-type.md))

### type Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value                 | Explanation |
| :-------------------- | ----------- |
| `"collection"`        |  Path to a collection of images           |
| `"stitchingVector"`   |  Path to a time series of stitching vectors           |
| `"tensorflowModel"`   |  Path to an AI model           |
| `"csvCollection"`     |  Path to a collection of CSV files           |
| `"pyramid"`           |  Path to a time series of image pyramids         |
| `"pyramidAnnotation"` |  Path to a time series of pyramid annotations           |
| `"notebook"`          |  Path to a Jupyter notebook           |
| `"genericData"`       |  Path to a folder containing unstructured data           |
| `"string"`            |  String           |
| `"number"`            |  Number           |
| `"integer"`           |  Integer           |
| `"enum"`              |  Enum           |
| `"array"`             |  Array of strings           |
| `"boolean"`           |  Boolean           |

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
-   Type: `string` ([Input description](manifest-properties-list-of-inputs-input-properties-input-description.md))
-   cannot be null
-   defined in: [Manifest schema](manifest-properties-list-of-inputs-input-properties-input-description.md "\#/properties/inputs/items/properties/description#/properties/inputs/items/properties/description")

### description Type

`string` ([Input description](manifest-properties-list-of-inputs-input-properties-input-description.md))

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
-   Type: `boolean` ([Required input](manifest-properties-list-of-inputs-input-properties-required-input.md))
-   cannot be null
-   defined in: [Manifest schema](manifest-properties-list-of-inputs-input-properties-required-input.md "\#/properties/inputs/items/properties/required#/properties/inputs/items/properties/required")

### required Type

`boolean` ([Required input](manifest-properties-list-of-inputs-input-properties-required-input.md))

### required Default Value

The default value is:

```json
true
```

### required Examples

```json
true
```

## options

Input options (used when input type is `enum` or `array`)


`options`

-   is optional
-   Type: `object` ([Enum Options input](wipp-plugin-properties-list-of-inputs-input-allof-0-then-properties-input-options.md), [Array Options input](wipp-plugin-properties-list-of-inputs-input-allof-1-then-properties-input-options.md))
-   cannot be null
-   defined in: [WIPP Plugin manifest](wipp-plugin-properties-list-of-inputs-input-properties-required-input.md "\#/properties/inputs/items/properties/required#/properties/inputs/items/properties/options")

### options Type

`object` ([Options input](wipp-plugin-properties-list-of-inputs-input-properties-required-input.md))

### options Default Value

The default value is:

```json
{}
```

### options Examples

#### Enum options example

```json
{
    "values": [
        "Manual",
        "IJDefault",
        "Huang",
        "Otsu",
        "Percentile"
    ]
}
```

#### Array options example

```json
{ "items": 
    {
        "type": "string",
        "widget": "select",
        "uniqueItems": "true",
        "default": "Feature2DJava_Area",
        "minItems": 1,
        "title": "Select feature",
        "oneOf": [
            {
                "description": "Area",
                "enum": [
                    "Feature2DJava_Area"
                ]
            },
            {
                "description": "Mean",
                "enum": [
                    "Feature2DJava_Mean"
                ]
            }
        ]
    }
}
```

