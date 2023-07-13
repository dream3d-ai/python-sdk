# Project


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
**is_new** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**latest_artifact** | [**Artifact**](Artifact.md) |  | [optional] 
**scene** | **str** |  | [optional] 
**preview_url** | **str** |  | [optional] 

## Example

```python
from dream3d.models.project import Project

# TODO update the JSON string below
json = "{}"
# create an instance of Project from a JSON string
project_instance = Project.from_json(json)
# print the JSON string representation of the object
print Project.to_json()

# convert the object into a dict
project_dict = project_instance.to_dict()
# create an instance of Project from a dict
project_form_dict = project.from_dict(project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


