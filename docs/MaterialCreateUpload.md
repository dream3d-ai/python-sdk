# MaterialCreateUpload


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**public** | **bool** |  | [optional] [default to False]
**user_id** | **int** |  | [optional] 

## Example

```python
from dream3d.models.material_create_upload import MaterialCreateUpload

# TODO update the JSON string below
json = "{}"
# create an instance of MaterialCreateUpload from a JSON string
material_create_upload_instance = MaterialCreateUpload.from_json(json)
# print the JSON string representation of the object
print MaterialCreateUpload.to_json()

# convert the object into a dict
material_create_upload_dict = material_create_upload_instance.to_dict()
# create an instance of MaterialCreateUpload from a dict
material_create_upload_form_dict = material_create_upload.from_dict(material_create_upload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


