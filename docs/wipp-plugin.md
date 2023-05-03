# WIPP Plugin manifest Schema

```txt
https://raw.githubusercontent.com/usnistgov/WIPP-Plugins-base-templates/master/plugin-manifest/schema/wipp-plugin-manifest-schema.json
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [wipp-plugin.schema.json](wipp-plugin.schema.json "open original schema") |

## WIPP Plugin manifest Type

`object` ([WIPP Plugin manifest](wipp-plugin.md))

# WIPP Plugin manifest Properties

| Property                                      | Type         | Required | Nullable       | Defined by                                                                                                                                                                                                                                                    |
| :-------------------------------------------- | ------------ | -------- | -------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [name](#name)                                 | `string`     | Required | cannot be null | [WIPP Plugin manifest](wipp-plugin-properties-plugin-name.md "\#/properties/name#/properties/name")                                                                                                                                                           |
| [version](#version)                           | `string`     | Required | cannot be null | [WIPP Plugin manifest](wipp-plugin-properties-plugin-version.md "\#/properties/version#/properties/version")                                                                                                                                                  |
| [title](#title)                               | `string`     | Required | cannot be null | [WIPP Plugin manifest](wipp-plugin-properties-plugin-title.md "\#/properties/title#/properties/title")                                                                                                                                                        |
| [description](#description)                   | `string`     | Required | cannot be null | [WIPP Plugin manifest](wipp-plugin-properties-short-description-of-the-plugin.md "\#/properties/description#/properties/description")                                                                                                                         |
| [author](#author)                             | Unknown Type | Optional | can be null    | [WIPP Plugin manifest](wipp-plugin-properties-authors.md "\#/properties/author#/properties/author")                                                                                                                                                           |
| [institution](#institution)                   | Unknown Type | Optional | can be null    | [WIPP Plugin manifest](wipp-plugin-properties-institution.md "\#/properties/institution#/properties/institution")                                                                                                                                             |
| [repository](#repository)                     | Unknown Type | Optional | can be null    | [WIPP Plugin manifest](wipp-plugin-properties-source-code-repository.md "\#/properties/repository#/properties/repository")                                                                                                                                    |
| [website](#website)                           | Unknown Type | Optional | can be null    | [WIPP Plugin manifest](wipp-plugin-properties-website.md "\#/properties/website#/properties/website")                                                                                                                                                         |
| [citation](#citation)                         | Unknown Type | Optional | can be null    | [WIPP Plugin manifest](wipp-plugin-properties-citation.md "\#/properties/citation#/properties/citation")                                                                                                                                                      |
| [containerId](#containerId)                   | `string`     | Required | cannot be null | [WIPP Plugin manifest](wipp-plugin-properties-containerid.md "\#/properties/containerId#/properties/containerId")                                                                                                                                             |
| [baseCommand](#baseCommand)                   | `array`      | Optional | cannot be null | [WIPP Plugin manifest](wipp-plugin-properties-base-command.md "\#/properties/baseCommand#/properties/baseCommand")                                                                                                                                            |
| [inputs](#inputs)                             | `array`      | Required | cannot be null | [WIPP Plugin manifest](wipp-plugin-properties-list-of-inputs.md "\#/properties/inputs#/properties/inputs")                                                                                                                                                    |
| [outputs](#outputs)                           | `array`      | Required | cannot be null | [WIPP Plugin manifest](wipp-plugin-properties-list-of-outputs.md "\#/properties/outputs#/properties/outputs")                                                                                                                                                 |
| [ui](#ui)                                     | `array`      | Required | cannot be null | [WIPP Plugin manifest](wipp-plugin-properties-plugin-form-ui-definition.md "\#/properties/ui#/properties/ui")                                                                                                                                                 |
| [resourceRequirements](#resourceRequirements) | `object`     | Optional | cannot be null | [WIPP Plugin manifest](wipp-plugin-properties-plugin-resource-requirements.md "https&#x3A;//raw.githubusercontent.com/usnistgov/WIPP-Plugins-base-templates/master/plugin-manifest/schema/wipp-plugin-manifest-schema.json#/properties/resourceRequirements") |

## name

Name of the plugin (format: org/name)


`name`

-   is required
-   Type: `string` ([Plugin name](wipp-plugin-properties-plugin-name.md))
-   cannot be null
-   defined in: [WIPP Plugin manifest](wipp-plugin-properties-plugin-name.md "\#/properties/name#/properties/name")

### name Type

`string` ([Plugin name](wipp-plugin-properties-plugin-name.md))

### name Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression: 

```regexp
^(.*)$
```

[try pattern](https://regexr.com/?expression=%5E(.*)%24 "try regular expression with regexr.com")

### name Examples

```json
"wipp/plugin-example"
```

## version

Version of the plugin (semantic versioning preferred)


`version`

-   is required
-   Type: `string` ([Plugin version](wipp-plugin-properties-plugin-version.md))
-   cannot be null
-   defined in: [WIPP Plugin manifest](wipp-plugin-properties-plugin-version.md "\#/properties/version#/properties/version")

### version Type

`string` ([Plugin version](wipp-plugin-properties-plugin-version.md))

### version Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression: 

```regexp
^(.*)$
```

[try pattern](https://regexr.com/?expression=%5E(.*)%24 "try regular expression with regexr.com")

### version Examples

```json
"1.0.0"
```

## title

Plugin title to display in WIPP forms


`title`

-   is required
-   Type: `string` ([Plugin title](wipp-plugin-properties-plugin-title.md))
-   cannot be null
-   defined in: [WIPP Plugin manifest](wipp-plugin-properties-plugin-title.md "\#/properties/title#/properties/title")

### title Type

`string` ([Plugin title](wipp-plugin-properties-plugin-title.md))

### title Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression: 

```regexp
^(.*)$
```

[try pattern](https://regexr.com/?expression=%5E(.*)%24 "try regular expression with regexr.com")

### title Examples

```json
"WIPP Plugin example"
```

## description




`description`

-   is required
-   Type: `string` ([Short description of the plugin](wipp-plugin-properties-short-description-of-the-plugin.md))
-   cannot be null
-   defined in: [WIPP Plugin manifest](wipp-plugin-properties-short-description-of-the-plugin.md "\#/properties/description#/properties/description")

### description Type

`string` ([Short description of the plugin](wipp-plugin-properties-short-description-of-the-plugin.md))

### description Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression: 

```regexp
^(.*)$
```

[try pattern](https://regexr.com/?expression=%5E(.*)%24 "try regular expression with regexr.com")

### description Examples

```json
"Custom image segmentation plugin"
```

## author




`author`

-   is optional
-   Type: `string` ([Author(s)](wipp-plugin-properties-authors.md))
-   can be null
-   defined in: [WIPP Plugin manifest](wipp-plugin-properties-authors.md "\#/properties/author#/properties/author")

### author Type

`string` ([Author(s)](wipp-plugin-properties-authors.md))

### author Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^(.*)$
```

[try pattern](https://regexr.com/?expression=%5E(.*)%24 "try regular expression with regexr.com")

### author Examples

```json
"FirstName LastName"
```

## institution




`institution`

-   is optional
-   Type: `string` ([Institution](wipp-plugin-properties-institution.md))
-   can be null
-   defined in: [WIPP Plugin manifest](wipp-plugin-properties-institution.md "\#/properties/institution#/properties/institution")

### institution Type

`string` ([Institution](wipp-plugin-properties-institution.md))

### institution Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^(.*)$
```

[try pattern](https://regexr.com/?expression=%5E(.*)%24 "try regular expression with regexr.com")

### institution Examples

```json
"National Institute of Standards and Technology"
```

## repository




`repository`

-   is optional
-   Type: `string` ([Source code repository](wipp-plugin-properties-source-code-repository.md))
-   can be null
-   defined in: [WIPP Plugin manifest](wipp-plugin-properties-source-code-repository.md "\#/properties/repository#/properties/repository")

### repository Type

`string` ([Source code repository](wipp-plugin-properties-source-code-repository.md))

### repository Constraints

**URI**: the string must be a URI, according to [RFC 3986](https://tools.ietf.org/html/rfc4291 "check the specification")

### repository Examples

```json
"https://github.com/usnistgov/WIPP"
```

## website




`website`

-   is optional
-   Type: `string` ([Website](wipp-plugin-properties-website.md))
-   can be null
-   defined in: [WIPP Plugin manifest](wipp-plugin-properties-website.md "\#/properties/website#/properties/website")

### website Type

`string` ([Website](wipp-plugin-properties-website.md))

### website Constraints

**URI**: the string must be a URI, according to [RFC 3986](https://tools.ietf.org/html/rfc4291 "check the specification")

### website Examples

```json
"http://usnistgov.github.io/WIPP"
```

## citation




`citation`

-   is optional
-   Type: `string` ([Citation](wipp-plugin-properties-citation.md))
-   can be null
-   defined in: [WIPP Plugin manifest](wipp-plugin-properties-citation.md "\#/properties/citation#/properties/citation")

### citation Type

`string` ([Citation](wipp-plugin-properties-citation.md))

### citation Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^(.*)$
```

[try pattern](https://regexr.com/?expression=%5E(.*)%24 "try regular expression with regexr.com")

### citation Examples

```json
"Peter Bajcsy, Joe Chalfoun, and Mylene Simon (2018). Web Microanalysis of Big Image Data. Springer-Verlag International"
```

## containerId

Docker image ID


`containerId`

-   is required
-   Type: `string` ([ContainerId](wipp-plugin-properties-containerid.md))
-   cannot be null
-   defined in: [WIPP Plugin manifest](wipp-plugin-properties-containerid.md "\#/properties/containerId#/properties/containerId")

### containerId Type

`string` ([ContainerId](wipp-plugin-properties-containerid.md))

### containerId Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^(.*)$
```

[try pattern](https://regexr.com/?expression=%5E(.*)%24 "try regular expression with regexr.com")

### containerId Examples

```json
"docker.io/wipp/plugin-example:1.0.0"
```

## baseCommand

Base command to use while running container image


`baseCommand`

-   is optional
-   Type: `string[]`
-   cannot be null
-   defined in: [WIPP Plugin manifest](wipp-plugin-properties-base-command.md "\#/properties/baseCommand#/properties/baseCommand")

### baseCommand Type

`string[]`

### baseCommand Examples

```json
[
  "python3",
  "/opt/executable/main.py"
]
```

## inputs

Defines inputs to the plugin


`inputs`

-   is required
-   Type: `object[]` ([Input](wipp-plugin-properties-list-of-inputs-input.md))
-   cannot be null
-   defined in: [WIPP Plugin manifest](wipp-plugin-properties-list-of-inputs.md "\#/properties/inputs#/properties/inputs")

### inputs Type

`object[]` ([Input](wipp-plugin-properties-list-of-inputs-input.md))

### inputs Constraints

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## outputs

Defines the outputs of the plugin


`outputs`

-   is required
-   Type: `object[]` ([Plugin output](wipp-plugin-properties-list-of-outputs-plugin-output.md))
-   cannot be null
-   defined in: [WIPP Plugin manifest](wipp-plugin-properties-list-of-outputs.md "\#/properties/outputs#/properties/outputs")

### outputs Type

`object[]` ([Plugin output](wipp-plugin-properties-list-of-outputs-plugin-output.md))

## ui




`ui`

-   is required
-   Type: `object[]` ([List of UI definitions](wipp-plugin-properties-plugin-form-ui-definition-list-of-ui-definitions.md))
-   cannot be null
-   defined in: [WIPP Plugin manifest](wipp-plugin-properties-plugin-form-ui-definition.md "\#/properties/ui#/properties/ui")

### ui Type

`object[]` ([List of UI definitions](wipp-plugin-properties-plugin-form-ui-definition-list-of-ui-definitions.md))

## resourceRequirements




`resourceRequirements`

-   is optional
-   Type: `object` ([Plugin Resource Requirements](wipp-plugin-properties-plugin-resource-requirements.md))
-   cannot be null
-   defined in: [WIPP Plugin manifest](wipp-plugin-properties-plugin-resource-requirements.md "https&#x3A;//raw.githubusercontent.com/usnistgov/WIPP-Plugins-base-templates/master/plugin-manifest/schema/wipp-plugin-manifest-schema.json#/properties/resourceRequirements")

### resourceRequirements Type

`object` ([Plugin Resource Requirements](wipp-plugin-properties-plugin-resource-requirements.md))

### resourceRequirements Default Value

The default value is:

```json
{}
```

### resourceRequirements Examples

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
