# Base command Schema

```txt
#/properties/baseCommand#/properties/baseCommand
```

Base command to use while running container image


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [wipp-plugin.schema.json\*](wipp-plugin.schema.json "open original schema") |

## baseCommand Type

`string[]`

## baseCommand Examples

```json
[
  "python3",
  "/opt/executable/main.py"
]
```
