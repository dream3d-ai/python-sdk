# MeshUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**prompt** | **str** |  | [optional] 
**public** | **bool** |  | [optional] 
**status** | [**MeshStatus**](MeshStatus.md) |  | [optional] 
**extents** | **List[float]** |  | [optional] 

## Example

```python
from dream3d.models.mesh_update import MeshUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of MeshUpdate from a JSON string
mesh_update_instance = MeshUpdate.from_json(json)
# print the JSON string representation of the object
print MeshUpdate.to_json()

# convert the object into a dict
mesh_update_dict = mesh_update_instance.to_dict()
# create an instance of MeshUpdate from a dict
mesh_update_form_dict = mesh_update.from_dict(mesh_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


