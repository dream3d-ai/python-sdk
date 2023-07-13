# TaskStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**step** | **int** |  | [optional] 
**total_steps** | **int** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**end_time** | **datetime** |  | [optional] 

## Example

```python
from dream3d.models.task_status import TaskStatus

# TODO update the JSON string below
json = "{}"
# create an instance of TaskStatus from a JSON string
task_status_instance = TaskStatus.from_json(json)
# print the JSON string representation of the object
print TaskStatus.to_json()

# convert the object into a dict
task_status_dict = task_status_instance.to_dict()
# create an instance of TaskStatus from a dict
task_status_form_dict = task_status.from_dict(task_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


