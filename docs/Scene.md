# Scene


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**Dict[str, D3DObject]**](D3DObject.md) |  | [optional] 
**lights** | [**List[Light]**](Light.md) |  | [optional] [default to []]
**camera** | [**Camera**](Camera.md) |  | [optional] 
**hdri** | [**HDRI**](HDRI.md) |  | [optional] 

## Example

```python
from dream3d.models.scene import Scene

# TODO update the JSON string below
json = "{}"
# create an instance of Scene from a JSON string
scene_instance = Scene.from_json(json)
# print the JSON string representation of the object
print Scene.to_json()

# convert the object into a dict
scene_dict = scene_instance.to_dict()
# create an instance of Scene from a dict
scene_form_dict = scene.from_dict(scene_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


