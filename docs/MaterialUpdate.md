# MaterialUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**public** | **bool** |  | [optional] [default to False]

## Example

```python
from dream3d.models.material_update import MaterialUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of MaterialUpdate from a JSON string
material_update_instance = MaterialUpdate.from_json(json)
# print the JSON string representation of the object
print MaterialUpdate.to_json()

# convert the object into a dict
material_update_dict = material_update_instance.to_dict()
# create an instance of MaterialUpdate from a dict
material_update_form_dict = material_update.from_dict(material_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


