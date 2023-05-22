# List of UI definitions Schema

```txt
#/properties/ui#/properties/ui/items
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                            |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [manifest.schema.json\*](manifest.schema.json "open original schema") |

## items Type

`object` ([List of UI definitions](manifest-properties-computational-tool-form-ui-definition-list-of-ui-definitions.md))

all of

-   [Untitled undefined type in Manifest schema](manifest-properties-computational-tool-form-ui-definition-list-of-ui-definitions-allof-0.md "check type definition")
-   [Untitled undefined type in Manifest schema](manifest-properties-computational-tool-form-ui-definition-list-of-ui-definitions-allof-1.md "check type definition")

# List of UI definitions Properties

| Property    | Type   | Required | Nullable       | Defined by                                                                                                                                                                                           |
| :---------- | ------ | -------- | -------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [key](#key) | Merged | Required | cannot be null | [Manifest schema](manifest-properties-computational-tool-form-ui-definition-list-of-ui-definitions-properties-ui-key.md "\#/properties/ui/items/properties/key#/properties/ui/items/properties/key") |

## key

Key of the input which this UI definition applies to, the expected format is 'inputs.inputName'. Special keyword 'fieldsets' can be used to define arrangement of inputs by sections.


`key`

-   is required
-   Type: `string` ([UI key](manifest-properties-computational-tool-form-ui-definition-list-of-ui-definitions-properties-ui-key.md))
-   cannot be null
-   defined in: [Manifest schema](manifest-properties-computational-tool-form-ui-definition-list-of-ui-definitions-properties-ui-key.md "\#/properties/ui/items/properties/key#/properties/ui/items/properties/key")

### key Type

`string` ([UI key](manifest-properties-computational-tool-form-ui-definition-list-of-ui-definitions-properties-ui-key.md))

one (and only one) of

-   [Untitled undefined type in Manifest schema](manifest-properties-computational-tool-form-ui-definition-list-of-ui-definitions-properties-ui-key-oneof-0.md "check type definition")
-   [Untitled undefined type in Manifest schema](manifest-properties-computational-tool-form-ui-definition-list-of-ui-definitions-properties-ui-key-oneof-1.md "check type definition")

### key Examples

```json
"inputs.inputImages"
```

```json
"inputs.fileNamPattern"
```

```json
"fieldsets"
```
