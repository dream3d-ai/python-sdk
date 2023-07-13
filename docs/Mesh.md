# Mesh


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**MeshType**](MeshType.md) |  | [optional] 
**category** | [**MeshCategory**](MeshCategory.md) |  | [optional] 
**name** | **str** |  | [optional] 
**prompt** | **str** |  | [optional] 
**status** | [**MeshStatus**](MeshStatus.md) |  | [optional] 
**public** | **bool** |  | [optional] 
**creator_id** | **int** |  | [optional] 
**format** | [**MeshFormat**](MeshFormat.md) |  | [optional] 
**embedding** | **List[float]** |  | [optional] 
**extents** | **List[float]** |  | [optional] 
**parent_mesh_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**avatar_image_url** | **str** |  | [optional] 
**glb_url** | **str** |  | [optional] 
**preview_url** | **str** |  | [optional] 
**obj_url** | **str** |  | [optional] 
**mtl_url** | **str** |  | [optional] 
**albedo_url** | **str** |  | [optional] 
**lora** | [**LoRA**](LoRA.md) |  | [optional] 

## Example

```python
from dream3d.models.mesh import Mesh

# TODO update the JSON string below
json = "{}"
# create an instance of Mesh from a JSON string
mesh_instance = Mesh.from_json(json)
# print the JSON string representation of the object
print Mesh.to_json()

# convert the object into a dict
mesh_dict = mesh_instance.to_dict()
# create an instance of Mesh from a dict
mesh_form_dict = mesh.from_dict(mesh_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


