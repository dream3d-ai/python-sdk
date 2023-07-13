# Camera


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'PERSPECTIVE']
**matrix** | **List[float]** |  | [optional] [default to [1,0,0,0,1,0,0,0,1]]
**fov** | **float** |  | [optional] [default to 20.0]
**near** | **float** |  | [optional] [default to 0.1]
**far** | **float** |  | [optional] [default to 1000.0]

## Example

```python
from dream3d.models.camera import Camera

# TODO update the JSON string below
json = "{}"
# create an instance of Camera from a JSON string
camera_instance = Camera.from_json(json)
# print the JSON string representation of the object
print Camera.to_json()

# convert the object into a dict
camera_dict = camera_instance.to_dict()
# create an instance of Camera from a dict
camera_form_dict = camera.from_dict(camera_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


