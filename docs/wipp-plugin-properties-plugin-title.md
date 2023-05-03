# Plugin title Schema

```txt
#/properties/title#/properties/title
```

Plugin title to display in WIPP forms


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [wipp-plugin.schema.json\*](wipp-plugin.schema.json "open original schema") |

## title Type

`string` ([Plugin title](wipp-plugin-properties-plugin-title.md))

## title Constraints

**minimum length**: the minimum number of characters for this string is: `1`

**pattern**: the string must match the following regular expression: 

```regexp
^(.*)$
```

[try pattern](https://regexr.com/?expression=%5E(.*)%24 "try regular expression with regexr.com")

## title Examples

```json
"WIPP Plugin example"
```
