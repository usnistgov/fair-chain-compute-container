# UI key Schema

```txt
#/properties/ui/items/properties/key#/properties/ui/items/properties/key
```

Key of the input which this UI definition applies to, the expected format is 'inputs.inputName'. Special keyword 'fieldsets' can be used to define arrangement of inputs by sections.


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [wipp-plugin.schema.json\*](wipp-plugin.schema.json "open original schema") |

## key Type

`string` ([UI key](wipp-plugin-properties-plugin-form-ui-definition-list-of-ui-definitions-properties-ui-key.md))

one (and only one) of

-   [Untitled undefined type in WIPP Plugin manifest](wipp-plugin-properties-plugin-form-ui-definition-list-of-ui-definitions-properties-ui-key-oneof-0.md "check type definition")
-   [Untitled undefined type in WIPP Plugin manifest](wipp-plugin-properties-plugin-form-ui-definition-list-of-ui-definitions-properties-ui-key-oneof-1.md "check type definition")

## key Examples

```json
"inputs.inputImages"
```

```json
"inputs.fileNamPattern"
```

```json
"fieldsets"
```
