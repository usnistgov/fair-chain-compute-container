# README

## Top-level Schemas

-   [WIPP Plugin manifest](./wipp-plugin.md) – `https://raw.githubusercontent.com/usnistgov/WIPP-Plugins-base-templates/master/plugin-manifest/schema/wipp-plugin-manifest-schema.json`

## Other Schemas

### Objects

-   [GPU Cuda-related requirements](./wipp-plugin-properties-plugin-resource-requirements-properties-gpu-cuda-related-requirements.md) – `https://raw.githubusercontent.com/usnistgov/WIPP-Plugins-base-templates/master/plugin-manifest/schema/wipp-plugin-manifest-schema.json#/properties/resourceRequirements/properties/cudaRequirements`
-   [Input](./wipp-plugin-properties-list-of-inputs-input.md "Plugin input") – `#/properties/inputs/items#/properties/inputs/items`
-   [Input options](./wipp-plugin-properties-list-of-inputs-input-allof-0-then-properties-input-options.md) – `#/properties/inputs/items/properties/options#/properties/inputs/items/allOf/0/then/properties/options`
-   [List of UI definitions](./wipp-plugin-properties-plugin-form-ui-definition-list-of-ui-definitions.md) – `#/properties/ui#/properties/ui/items`
-   [Plugin Resource Requirements](./wipp-plugin-properties-plugin-resource-requirements.md) – `https://raw.githubusercontent.com/usnistgov/WIPP-Plugins-base-templates/master/plugin-manifest/schema/wipp-plugin-manifest-schema.json#/properties/resourceRequirements`
-   [Plugin output](./wipp-plugin-properties-list-of-outputs-plugin-output.md) – `#/properties/outputs/items#/properties/outputs/items`
-   [Untitled object in WIPP Plugin manifest](./wipp-plugin-properties-plugin-form-ui-definition-list-of-ui-definitions-allof-1-then-properties-fieldsets-items.md "A section of input fields") – `#/properties/ui#/properties/ui/items/allOf/1/then/properties/fieldsets/items`

### Arrays

-   [Base command](./wipp-plugin-properties-base-command.md "Base command to use while running container image") – `#/properties/baseCommand#/properties/baseCommand`
-   [List of Inputs](./wipp-plugin-properties-list-of-inputs.md "Defines inputs to the plugin") – `#/properties/inputs#/properties/inputs`
-   [List of Outputs](./wipp-plugin-properties-list-of-outputs.md "Defines the outputs of the plugin") – `#/properties/outputs#/properties/outputs`
-   [Plugin form UI definition](./wipp-plugin-properties-plugin-form-ui-definition.md) – `#/properties/ui#/properties/ui`
-   [Untitled array in WIPP Plugin manifest](./wipp-plugin-properties-list-of-inputs-input-allof-0-then-properties-input-options-properties-values.md "List of possible values") – `#/properties/inputs/items/properties/options#/properties/inputs/items/allOf/0/then/properties/options/properties/values`
-   [Untitled array in WIPP Plugin manifest](./wipp-plugin-properties-plugin-form-ui-definition-list-of-ui-definitions-allof-1-then-properties-fieldsets.md "A list of definitions representing sections of input fields") – `#/properties/ui#/properties/ui/items/allOf/1/then/properties/fieldsets`
-   [Untitled array in WIPP Plugin manifest](./wipp-plugin-properties-plugin-form-ui-definition-list-of-ui-definitions-allof-1-then-properties-fieldsets-items-properties-fields.md "A list of input names representing input fields that belong to this section") – `#/properties/ui#/properties/ui/items/allOf/1/then/properties/fieldsets/items/properties/fields`

## Version Note

The schemas linked above follow the JSON Schema Spec version: `http://json-schema.org/draft-07/schema#`
