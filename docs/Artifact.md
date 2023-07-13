# Artifact


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**title** | **str** |  | 
**public** | **bool** |  | [optional] 
**status** | [**ArtifactStatus**](ArtifactStatus.md) |  | [optional] 
**type** | [**ArtifactType**](ArtifactType.md) |  | [optional] 
**views** | **int** |  | [optional] 
**project_id** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**is_template** | **bool** |  | [optional] 
**payload** | [**RenderPayload**](RenderPayload.md) |  | [optional] 
**user_id** | **int** |  | 
**prompt** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**url_4x** | **str** |  | [optional] 
**task_id** | **str** |  | [optional] 
**likes** | **int** |  | [optional] 
**user** | [**RelatedUser**](RelatedUser.md) |  | 
**liked** | **bool** |  | [optional] 
**upscaled** | **bool** |  | [optional] [default to False]

## Example

```python
from dream3d.models.artifact import Artifact

# TODO update the JSON string below
json = "{}"
# create an instance of Artifact from a JSON string
artifact_instance = Artifact.from_json(json)
# print the JSON string representation of the object
print Artifact.to_json()

# convert the object into a dict
artifact_dict = artifact_instance.to_dict()
# create an instance of Artifact from a dict
artifact_form_dict = artifact.from_dict(artifact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


