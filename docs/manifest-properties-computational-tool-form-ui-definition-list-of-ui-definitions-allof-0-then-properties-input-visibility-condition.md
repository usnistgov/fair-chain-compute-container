# Input visibility condition Schema

```txt
#/properties/ui/items/properties/condition#/properties/ui/items/allOf/0/then/properties/condition
```

Definition of when this field is visible or not, depending on the value of another input, the expected format for the condition is 'model.inputs.inputName==value'


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                            |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [manifest.schema.json\*](manifest.schema.json "open original schema") |

## condition Type

`string` ([Input visibility condition](manifest-properties-computational-tool-form-ui-definition-list-of-ui-definitions-allof-0-then-properties-input-visibility-condition.md))

## condition Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^(.*)$
```

[try pattern](https://regexr.com/?expression=%5E(.*)%24 "try regular expression with regexr.com")

## condition Examples

```json
"model.inputs.thresholdtype=='Manual'"
```
