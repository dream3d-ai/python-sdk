# D3DObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**geometry** | [**GeometryType**](GeometryType.md) |  | 
**position** | **List[float]** |  | 
**scale** | **List[float]** |  | 
**scale_linked** | **bool** |  | [optional] [default to True]
**rotation** | **List[float]** |  | 
**color** | **str** |  | 
**matrix_world** | **List[float]** |  | [optional] 
**prompt** | **str** |  | [optional] 
**mesh_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**mesh_url** | **str** |  | [optional] 
**args** | **List[float]** |  | [optional] 
**visible** | **bool** |  | [optional] [default to True]
**url** | **str** |  | [optional] 
**root_id** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**children** | **List[str]** |  | [optional] [default to []]
**material_strength** | **float** |  | [optional] [default to 0.0]
**detail_strength** | **float** |  | [optional] [default to 1.0]
**material_id** | **str** |  | [optional] 
**material_preset** | [**MaterialPreset**](MaterialPreset.md) |  | [optional] 
**material_shader** | [**MaterialShader**](MaterialShader.md) |  | [optional] 
**material_properties** | [**MaterialProperties**](MaterialProperties.md) |  | [optional] 

## Example

```python
from dream3d.models.d3_d_object import D3DObject

# TODO update the JSON string below
json = "{}"
# create an instance of D3DObject from a JSON string
d3_d_object_instance = D3DObject.from_json(json)
# print the JSON string representation of the object
print D3DObject.to_json()

# convert the object into a dict
d3_d_object_dict = d3_d_object_instance.to_dict()
# create an instance of D3DObject from a dict
d3_d_object_form_dict = d3_d_object.from_dict(d3_d_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


