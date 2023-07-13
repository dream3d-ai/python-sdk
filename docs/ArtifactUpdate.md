# ArtifactUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**public** | **bool** |  | [optional] 
**status** | [**ArtifactStatus**](ArtifactStatus.md) |  | [optional] 
**type** | [**ArtifactType**](ArtifactType.md) |  | [optional] 
**views** | **int** |  | [optional] 
**project_id** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**is_template** | **bool** |  | [optional] 
**payload** | [**RenderPayload**](RenderPayload.md) |  | [optional] 

## Example

```python
from dream3d.models.artifact_update import ArtifactUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactUpdate from a JSON string
artifact_update_instance = ArtifactUpdate.from_json(json)
# print the JSON string representation of the object
print ArtifactUpdate.to_json()

# convert the object into a dict
artifact_update_dict = artifact_update_instance.to_dict()
# create an instance of ArtifactUpdate from a dict
artifact_update_form_dict = artifact_update.from_dict(artifact_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


