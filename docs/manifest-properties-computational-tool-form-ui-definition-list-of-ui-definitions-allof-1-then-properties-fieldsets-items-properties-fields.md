# Untitled array in Manifest schema Schema

```txt
#/properties/ui#/properties/ui/items/allOf/1/then/properties/fieldsets/items/properties/fields
```

A list of input names representing input fields that belong to this section.


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                            |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [manifest.schema.json\*](manifest.schema.json "open original schema") |

## fields Type

`string[]`

## fields Constraints

**minimum number of items**: the minimum number of items for this array is: `1`

**unique items**: all items in this array must be unique. Duplicates are not allowed.

## fields Examples

```json
"inputImages, fileNamePattern"
```
