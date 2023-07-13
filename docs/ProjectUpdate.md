# ProjectUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**owner_id** | **int** |  | [optional] 
**s3_uri** | **str** |  | [optional] 
**preview_uri** | **str** |  | [optional] 
**edited_at** | **datetime** |  | [optional] 
**latest_artifact_id** | **str** |  | [optional] 
**public** | **bool** |  | [optional] 
**payload** | [**RenderPayload**](RenderPayload.md) |  | [optional] 
**is_new** | **bool** |  | [optional] [default to False]

## Example

```python
from dream3d.models.project_update import ProjectUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectUpdate from a JSON string
project_update_instance = ProjectUpdate.from_json(json)
# print the JSON string representation of the object
print ProjectUpdate.to_json()

# convert the object into a dict
project_update_dict = project_update_instance.to_dict()
# create an instance of ProjectUpdate from a dict
project_update_form_dict = project_update.from_dict(project_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


