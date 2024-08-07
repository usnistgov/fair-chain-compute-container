# Manifest Schema

```txt
https://raw.githubusercontent.com/usnistgov/fair-chain-compute-container/master/schema/manifest.schema.json
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                          |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | ------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [manifest.schema.json](manifest.schema.json "open original schema") |

## Manifest schema Type

`object` ([Manifest schema](manifest.md))

# Manifest schema Properties

| Property                                      | Type         | Required | Nullable       | Defined by                                                                                                                                                                                                                             |
| :-------------------------------------------- | ------------ | -------- | -------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name)                                 | `string`     | Required | cannot be null | [Manifest schema](manifest-properties-computational-tool-name.md "\#/properties/name#/properties/name")                                                                                                                                |
| [operationType](#operationType)               | `array`      | Required | cannot be null | [Manifest schema](manifest-properties-computational-tool-operationType.md "\#/properties/operationType#/properties/operationType")                                                                                                        |
| [version](#version)                           | `string`     | Required | cannot be null | [Manifest schema](manifest-properties-computational-tool-version.md "\#/properties/version#/properties/version")                                                                                                                       |
| [title](#title)                               | `string`     | Required | cannot be null | [Manifest schema](manifest-properties-computational-tool-title.md "\#/properties/title#/properties/title")                                                                                                                             |
| [description](#description)                   | `string`     | Required | cannot be null | [Manifest schema](manifest-properties-short-description-of-the-computational-tool.md "\#/properties/description#/properties/description")                                                                                              |
| [author](#author)                             | Unknown Type | Optional | can be null    | [Manifest schema](manifest-properties-authors.md "\#/properties/author#/properties/author")                                                                                                                                            |
| [institution](#institution)                   | Unknown Type | Optional | can be null    | [Manifest schema](manifest-properties-institution.md "\#/properties/institution#/properties/institution")                                                                                                                              |
| [repository](#repository)                     | Unknown Type | Optional | can be null    | [Manifest schema](manifest-properties-source-code-repository.md "\#/properties/repository#/properties/repository")                                                                                                                     |
| [website](#website)                           | Unknown Type | Optional | can be null    | [Manifest schema](manifest-properties-website.md "\#/properties/website#/properties/website")                                                                                                                                          |
| [citation](#citation)                         | Unknown Type | Optional | can be null    | [Manifest schema](manifest-properties-citation.md "\#/properties/citation#/properties/citation")                                                                                                                                       |
| [containerId](#containerId)                   | `string`     | Required | cannot be null | [Manifest schema](manifest-properties-containerid.md "\#/properties/containerId#/properties/containerId")                                                                                                                              |
| [baseCommand](#baseCommand)                   | `array`      | Optional | cannot be null | [Manifest schema](manifest-properties-base-command.md "\#/properties/baseCommand#/properties/baseCommand")                                                                                                                             |
| [inputs](#inputs)                             | `array`      | Required | cannot be null | [Manifest schema](manifest-properties-list-of-inputs.md "\#/properties/inputs#/properties/inputs")                                                                                                                                     |
| [outputs](#outputs)                           | `array`      | Required | cannot be null | [Manifest schema](manifest-properties-list-of-outputs.md "\#/properties/outputs#/properties/outputs")                                                                                                                                  |
| [ui](#ui)                                     | `array`      | Required | cannot be null | [Manifest schema](manifest-properties-computational-tool-form-ui-definition.md "\#/properties/ui#/properties/ui")                                                                                                                      |
| [resourceRequirements](#resourceRequirements) | `object`     | Optional | cannot be null | [Manifest schema](manifest-properties-computational-tool-resource-requirements.md "https&#x3A;//raw.githubusercontent.com/usnistgov/fair-chain-compute-container/master/schema/manifest.schema.json#/properties/resourceRequirements") |

## name

Name of the computational tool (format: org/name)


`name`

-   is required
-   Type: `string` ([Computational tool name](manifest-properties-computational-tool-name.md))
-   cannot be null
-   defined in: [Manifest schema](manifest-properties-computational-tool-name.md "\#/properties/name#/properties/name")

### name Type

`string` ([Computational tool name](manifest-properties-computational-tool-name.md))

### name Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression: 

```regexp
^(.*)$
```

[try pattern](https://regexr.com/?expression=%5E(.*)%24 "try regular expression with regexr.com")

### name Examples

```json
"wipp/computational-tool-example"
```

## operationType

Type of the computational tool (format: org/type)

`operationType`

-   is required
-   Type: `string[]` ([Computational tool type](manifest-properties-computational-tool-operationType.md))
-   cannot be null
-   defined in: [Manifest schema](manifest-properties-computational-tool-operationType.md "\#/properties/operationType#/properties/operationType")

### operationType Examples

```json
["segmentation"]
```

## version

Version of the computational tool (semantic versioning preferred)


`version`

-   is required
-   Type: `string` ([Computational tool version](manifest-properties-computational-tool-version.md))
-   cannot be null
-   defined in: [Manifest schema](manifest-properties-computational-tool-version.md "\#/properties/version#/properties/version")

### version Type

`string` ([Computational tool version](manifest-properties-computational-tool-version.md))

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

Computational tool title to display in UI forms


`title`

-   is required
-   Type: `string` ([Computational tool title](manifest-properties-computational-tool-title.md))
-   cannot be null
-   defined in: [Manifest schema](manifest-properties-computational-tool-title.md "\#/properties/title#/properties/title")

### title Type

`string` ([Computational tool title](manifest-properties-computational-tool-title.md))

### title Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression: 

```regexp
^(.*)$
```

[try pattern](https://regexr.com/?expression=%5E(.*)%24 "try regular expression with regexr.com")

### title Examples

```json
"WIPP Example Tool"
```

## description




`description`

-   is required
-   Type: `string` ([Short description of the computational tool](manifest-properties-short-description-of-the-computational-tool.md))
-   cannot be null
-   defined in: [Manifest schema](manifest-properties-short-description-of-the-computational-tool.md "\#/properties/description#/properties/description")

### description Type

`string` ([Short description of the computational tool](manifest-properties-short-description-of-the-computational-tool.md))

### description Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression: 

```regexp
^(.*)$
```

[try pattern](https://regexr.com/?expression=%5E(.*)%24 "try regular expression with regexr.com")

### description Examples

```json
"Custom image segmentation tool"
```

## author




`author`

-   is optional
-   Type: `string` ([Author(s)](manifest-properties-authors.md))
-   can be null
-   defined in: [Manifest schema](manifest-properties-authors.md "\#/properties/author#/properties/author")

### author Type

`string` ([Author(s)](manifest-properties-authors.md))

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
-   Type: `string` ([Institution](manifest-properties-institution.md))
-   can be null
-   defined in: [Manifest schema](manifest-properties-institution.md "\#/properties/institution#/properties/institution")

### institution Type

`string` ([Institution](manifest-properties-institution.md))

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
-   Type: `string` ([Source code repository](manifest-properties-source-code-repository.md))
-   can be null
-   defined in: [Manifest schema](manifest-properties-source-code-repository.md "\#/properties/repository#/properties/repository")

### repository Type

`string` ([Source code repository](manifest-properties-source-code-repository.md))

### repository Constraints

**URI**: the string must be a URI, according to [RFC 3986](https://tools.ietf.org/html/rfc4291 "check the specification")

### repository Examples

```json
"https://github.com/usnistgov/WIPP"
```

## website




`website`

-   is optional
-   Type: `string` ([Website](manifest-properties-website.md))
-   can be null
-   defined in: [Manifest schema](manifest-properties-website.md "\#/properties/website#/properties/website")

### website Type

`string` ([Website](manifest-properties-website.md))

### website Constraints

**URI**: the string must be a URI, according to [RFC 3986](https://tools.ietf.org/html/rfc4291 "check the specification")

### website Examples

```json
"http://usnistgov.github.io/WIPP"
```

## citation




`citation`

-   is optional
-   Type: `string` ([Citation](manifest-properties-citation.md))
-   can be null
-   defined in: [Manifest schema](manifest-properties-citation.md "\#/properties/citation#/properties/citation")

### citation Type

`string` ([Citation](manifest-properties-citation.md))

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
-   Type: `string` ([ContainerId](manifest-properties-containerid.md))
-   cannot be null
-   defined in: [Manifest schema](manifest-properties-containerid.md "\#/properties/containerId#/properties/containerId")

### containerId Type

`string` ([ContainerId](manifest-properties-containerid.md))

### containerId Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^(.*)$
```

[try pattern](https://regexr.com/?expression=%5E(.*)%24 "try regular expression with regexr.com")

### containerId Examples

```json
"docker.io/wipp/tool-example:1.0.0"
```

## baseCommand

Base command to use while running container image


`baseCommand`

-   is optional
-   Type: `string[]`
-   cannot be null
-   defined in: [Manifest schema](manifest-properties-base-command.md "\#/properties/baseCommand#/properties/baseCommand")

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

Defines inputs to the computational tool


`inputs`

-   is required
-   Type: `object[]` ([Input](manifest-properties-list-of-inputs-input.md))
-   cannot be null
-   defined in: [Manifest schema](manifest-properties-list-of-inputs.md "\#/properties/inputs#/properties/inputs")

### inputs Type

`object[]` ([Input](manifest-properties-list-of-inputs-input.md))

### inputs Constraints

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## outputs

Defines the outputs of the computational tool


`outputs`

-   is required
-   Type: `object[]` ([Computational tool output](manifest-properties-list-of-outputs-computational-tool-output.md))
-   cannot be null
-   defined in: [Manifest schema](manifest-properties-list-of-outputs.md "\#/properties/outputs#/properties/outputs")

### outputs Type

`object[]` ([Computational tool output](manifest-properties-list-of-outputs-computational-tool-output.md))

## ui




`ui`

-   is required
-   Type: `object[]` ([List of UI definitions](manifest-properties-computational-tool-form-ui-definition-list-of-ui-definitions.md))
-   cannot be null
-   defined in: [Manifest schema](manifest-properties-computational-tool-form-ui-definition.md "\#/properties/ui#/properties/ui")

### ui Type

`object[]` ([List of UI definitions](manifest-properties-computational-tool-form-ui-definition-list-of-ui-definitions.md))

## resourceRequirements




`resourceRequirements`

-   is optional
-   Type: `object` ([Computational Tool Resource Requirements](manifest-properties-computational-tool-resource-requirements.md))
-   cannot be null
-   defined in: [Manifest schema](manifest-properties-computational-tool-resource-requirements.md "https&#x3A;//raw.githubusercontent.com/usnistgov/fair-chain-compute-container/master/schema/manifest.schema.json#/properties/resourceRequirements")

### resourceRequirements Type

`object` ([Computational Tool Resource Requirements](manifest-properties-computational-tool-resource-requirements.md))

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

## Version Note

The schemas linked above follow the JSON Schema Spec version: `http://json-schema.org/draft-07/schema#`
