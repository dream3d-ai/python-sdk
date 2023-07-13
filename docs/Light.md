# Light


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'DIRECTIONAL']
**color** | **List[float]** |  | 
**intensity** | **float** |  | 
**direction** | **List[float]** |  | 

## Example

```python
from dream3d.models.light import Light

# TODO update the JSON string below
json = "{}"
# create an instance of Light from a JSON string
light_instance = Light.from_json(json)
# print the JSON string representation of the object
print Light.to_json()

# convert the object into a dict
light_dict = light_instance.to_dict()
# create an instance of Light from a dict
light_form_dict = light.from_dict(light_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


