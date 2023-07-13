# MeshCreateGenerate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**prompt** | **str** |  | 
**public** | **bool** |  | [optional] [default to False]

## Example

```python
from dream3d.models.mesh_create_generate import MeshCreateGenerate

# TODO update the JSON string below
json = "{}"
# create an instance of MeshCreateGenerate from a JSON string
mesh_create_generate_instance = MeshCreateGenerate.from_json(json)
# print the JSON string representation of the object
print MeshCreateGenerate.to_json()

# convert the object into a dict
mesh_create_generate_dict = mesh_create_generate_instance.to_dict()
# create an instance of MeshCreateGenerate from a dict
mesh_create_generate_form_dict = mesh_create_generate.from_dict(mesh_create_generate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


