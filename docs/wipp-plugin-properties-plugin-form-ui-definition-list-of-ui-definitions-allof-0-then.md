# Untitled undefined type in WIPP Plugin manifest Schema

```txt
#/properties/ui#/properties/ui/items/allOf/0/then
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | --------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [wipp-plugin.schema.json\*](wipp-plugin.schema.json "open original schema") |

## then Type

unknown

# undefined Properties

| Property                    | Type         | Required | Nullable       | Defined by                                                                                                                                                                                                                                                 |
| :-------------------------- | ------------ | -------- | -------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [title](#title)             | `string`     | Required | cannot be null | [WIPP Plugin manifest](wipp-plugin-properties-plugin-form-ui-definition-list-of-ui-definitions-allof-0-then-properties-input-label.md "\#/properties/ui/items/properties/title#/properties/ui/items/allOf/0/then/properties/title")                        |
| [description](#description) | `string`     | Optional | cannot be null | [WIPP Plugin manifest](wipp-plugin-properties-plugin-form-ui-definition-list-of-ui-definitions-allof-0-then-properties-input-placeholder.md "\#/properties/ui/items/properties/description#/properties/ui/items/allOf/0/then/properties/description")      |
| [condition](#condition)     | `string`     | Optional | cannot be null | [WIPP Plugin manifest](wipp-plugin-properties-plugin-form-ui-definition-list-of-ui-definitions-allof-0-then-properties-input-visibility-condition.md "\#/properties/ui/items/properties/condition#/properties/ui/items/allOf/0/then/properties/condition") |
| [default](#default)         | Unknown Type | Optional | cannot be null | [WIPP Plugin manifest](wipp-plugin-properties-plugin-form-ui-definition-list-of-ui-definitions-allof-0-then-properties-input-default-value.md "\#/properties/ui/items/properties/default#/properties/ui/items/allOf/0/then/properties/default")            |
| [hidden](#hidden)           | `boolean`    | Optional | cannot be null | [WIPP Plugin manifest](wipp-plugin-properties-plugin-form-ui-definition-list-of-ui-definitions-allof-0-then-properties-hidden-input.md "\#/properties/ui/items/properties/hidden#/properties/ui/items/allOf/0/then/properties/hidden")                     |
| [bind](#bind)               | `string`     | Optional | cannot be null | [WIPP Plugin manifest](wipp-plugin-properties-plugin-form-ui-definition-list-of-ui-definitions-allof-0-then-properties-bind-input-value-to-another-input.md "\#/properties/ui/items/properties/bind#/properties/ui/items/allOf/0/then/properties/bind")    |

## title




`title`

-   is required
-   Type: `string` ([Input label](wipp-plugin-properties-plugin-form-ui-definition-list-of-ui-definitions-allof-0-then-properties-input-label.md))
-   cannot be null
-   defined in: [WIPP Plugin manifest](wipp-plugin-properties-plugin-form-ui-definition-list-of-ui-definitions-allof-0-then-properties-input-label.md "\#/properties/ui/items/properties/title#/properties/ui/items/allOf/0/then/properties/title")

### title Type

`string` ([Input label](wipp-plugin-properties-plugin-form-ui-definition-list-of-ui-definitions-allof-0-then-properties-input-label.md))

### title Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^(.*)$
```

[try pattern](https://regexr.com/?expression=%5E(.*)%24 "try regular expression with regexr.com")

### title Examples

```json
"Input images: "
```

## description




`description`

-   is optional
-   Type: `string` ([Input placeholder](wipp-plugin-properties-plugin-form-ui-definition-list-of-ui-definitions-allof-0-then-properties-input-placeholder.md))
-   cannot be null
-   defined in: [WIPP Plugin manifest](wipp-plugin-properties-plugin-form-ui-definition-list-of-ui-definitions-allof-0-then-properties-input-placeholder.md "\#/properties/ui/items/properties/description#/properties/ui/items/allOf/0/then/properties/description")

### description Type

`string` ([Input placeholder](wipp-plugin-properties-plugin-form-ui-definition-list-of-ui-definitions-allof-0-then-properties-input-placeholder.md))

### description Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^(.*)$
```

[try pattern](https://regexr.com/?expression=%5E(.*)%24 "try regular expression with regexr.com")

### description Examples

```json
"Pick a collection..."
```

## condition

Definition of when this field is visible or not, depending on the value of another input, the expected format for the condition is 'model.inputs.inputName==value'


`condition`

-   is optional
-   Type: `string` ([Input visibility condition](wipp-plugin-properties-plugin-form-ui-definition-list-of-ui-definitions-allof-0-then-properties-input-visibility-condition.md))
-   cannot be null
-   defined in: [WIPP Plugin manifest](wipp-plugin-properties-plugin-form-ui-definition-list-of-ui-definitions-allof-0-then-properties-input-visibility-condition.md "\#/properties/ui/items/properties/condition#/properties/ui/items/allOf/0/then/properties/condition")

### condition Type

`string` ([Input visibility condition](wipp-plugin-properties-plugin-form-ui-definition-list-of-ui-definitions-allof-0-then-properties-input-visibility-condition.md))

### condition Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^(.*)$
```

[try pattern](https://regexr.com/?expression=%5E(.*)%24 "try regular expression with regexr.com")

### condition Examples

```json
"model.inputs.thresholdtype=='Manual'"
```

## default




`default`

-   is optional
-   Type: any of the folllowing: `string` or `number` or `integer` or `boolean` ([Input default value](wipp-plugin-properties-plugin-form-ui-definition-list-of-ui-definitions-allof-0-then-properties-input-default-value.md))
-   cannot be null
-   defined in: [WIPP Plugin manifest](wipp-plugin-properties-plugin-form-ui-definition-list-of-ui-definitions-allof-0-then-properties-input-default-value.md "\#/properties/ui/items/properties/default#/properties/ui/items/allOf/0/then/properties/default")

### default Type

any of the folllowing: `string` or `number` or `integer` or `boolean` ([Input default value](wipp-plugin-properties-plugin-form-ui-definition-list-of-ui-definitions-allof-0-then-properties-input-default-value.md))

### default Examples

```json
5
```

```json
false
```

```json
".ome.tif"
```

## hidden

Hidden input will not be displayed on the form, but can be used in conjunction with the 'default' or 'bind' properties to define default or automatically set parameters


`hidden`

-   is optional
-   Type: `boolean` ([Hidden input](wipp-plugin-properties-plugin-form-ui-definition-list-of-ui-definitions-allof-0-then-properties-hidden-input.md))
-   cannot be null
-   defined in: [WIPP Plugin manifest](wipp-plugin-properties-plugin-form-ui-definition-list-of-ui-definitions-allof-0-then-properties-hidden-input.md "\#/properties/ui/items/properties/hidden#/properties/ui/items/allOf/0/then/properties/hidden")

### hidden Type

`boolean` ([Hidden input](wipp-plugin-properties-plugin-form-ui-definition-list-of-ui-definitions-allof-0-then-properties-hidden-input.md))

### hidden Examples

```json
true
```

```json
false
```

## bind




`bind`

-   is optional
-   Type: `string` ([Bind input value to another input](wipp-plugin-properties-plugin-form-ui-definition-list-of-ui-definitions-allof-0-then-properties-bind-input-value-to-another-input.md))
-   cannot be null
-   defined in: [WIPP Plugin manifest](wipp-plugin-properties-plugin-form-ui-definition-list-of-ui-definitions-allof-0-then-properties-bind-input-value-to-another-input.md "\#/properties/ui/items/properties/bind#/properties/ui/items/allOf/0/then/properties/bind")

### bind Type

`string` ([Bind input value to another input](wipp-plugin-properties-plugin-form-ui-definition-list-of-ui-definitions-allof-0-then-properties-bind-input-value-to-another-input.md))

### bind Examples

```json
"gridWidth"
```
