# Untitled object in Manifest schema Schema

```txt
#/properties/ui#/properties/ui/items/allOf/1/then/properties/fieldsets/items
```

A section of input fields.


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                            |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [manifest.schema.json\*](manifest.schema.json "open original schema") |

## items Type

`object` ([Details](manifest-properties-computational-tool-form-ui-definition-list-of-ui-definitions-allof-1-then-properties-fieldsets-items.md))

## items Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## items Default Value

The default value is:

```json
[]
```

# undefined Properties

| Property          | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                         |
| :---------------- | -------- | -------- | -------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [title](#title)   | `string` | Required | cannot be null | [Manifest schema](manifest-properties-computational-tool-form-ui-definition-list-of-ui-definitions-allof-1-then-properties-fieldsets-items-properties-title.md "\#/properties/ui#/properties/ui/items/allOf/1/then/properties/fieldsets/items/properties/title")   |
| [fields](#fields) | `array`  | Required | cannot be null | [Manifest schema](manifest-properties-computational-tool-form-ui-definition-list-of-ui-definitions-allof-1-then-properties-fieldsets-items-properties-fields.md "\#/properties/ui#/properties/ui/items/allOf/1/then/properties/fieldsets/items/properties/fields") |

## title

The label of the section.


`title`

-   is required
-   Type: `string`
-   cannot be null
-   defined in: [Manifest schema](manifest-properties-computational-tool-form-ui-definition-list-of-ui-definitions-allof-1-then-properties-fieldsets-items-properties-title.md "\#/properties/ui#/properties/ui/items/allOf/1/then/properties/fieldsets/items/properties/title")

### title Type

`string`

### title Examples

```json
"Input images selection"
```

## fields

A list of input names representing input fields that belong to this section.


`fields`

-   is required
-   Type: `string[]`
-   cannot be null
-   defined in: [Manifest schema](manifest-properties-computational-tool-form-ui-definition-list-of-ui-definitions-allof-1-then-properties-fieldsets-items-properties-fields.md "\#/properties/ui#/properties/ui/items/allOf/1/then/properties/fieldsets/items/properties/fields")

### fields Type

`string[]`

### fields Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

### fields Examples

```json
"inputImages, fileNamePattern"
```
