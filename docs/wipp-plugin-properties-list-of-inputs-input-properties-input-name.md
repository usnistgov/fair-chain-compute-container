# Input name Schema

```txt
#/properties/inputs/items/properties/name#/properties/inputs/items/properties/name
```

Input name as expected by the plugin CLI


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [wipp-plugin.schema.json\*](wipp-plugin.schema.json "open original schema") |

## name Type

`string` ([Input name](wipp-plugin-properties-list-of-inputs-input-properties-input-name.md))

## name Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^[a-zA-Z0-9][-a-zA-Z0-9]*$
```

[try pattern](https://regexr.com/?expression=%5E%5Ba-zA-Z0-9%5D%5B-a-zA-Z0-9%5D*%24 "try regular expression with regexr.com")

## name Examples

```json
"inputImages"
```

```json
"fileNamePattern"
```

```json
"thresholdValue"
```
