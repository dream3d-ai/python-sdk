# ProjectCreate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**owner_id** | **int** |  | 
**s3_uri** | **str** |  | [optional] 
**preview_uri** | **str** |  | [optional] 
**edited_at** | **datetime** |  | [optional] 
**latest_artifact_id** | **str** |  | [optional] 
**public** | **bool** |  | [optional] 
**payload** | [**Payload**](Payload.md) |  | [optional] 
**is_new** | **bool** |  | [optional] [default to True]

## Example

```python
from dream3d.models.project_create import ProjectCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectCreate from a JSON string
project_create_instance = ProjectCreate.from_json(json)
# print the JSON string representation of the object
print ProjectCreate.to_json()

# convert the object into a dict
project_create_dict = project_create_instance.to_dict()
# create an instance of ProjectCreate from a dict
project_create_form_dict = project_create.from_dict(project_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


