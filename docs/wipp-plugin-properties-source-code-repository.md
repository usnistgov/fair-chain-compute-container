# Source code repository Schema

```txt
#/properties/repository#/properties/repository
```




| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [wipp-plugin.schema.json\*](wipp-plugin.schema.json "open original schema") |

## repository Type

`string` ([Source code repository](wipp-plugin-properties-source-code-repository.md))

## repository Constraints

**URI**: the string must be a URI, according to [RFC 3986](https://tools.ietf.org/html/rfc4291 "check the specification")

## repository Examples

```json
"https://github.com/usnistgov/WIPP"
```
