# RelatedUser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**photo** | **str** |  | [optional] 

## Example

```python
from dream3d.models.related_user import RelatedUser

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedUser from a JSON string
related_user_instance = RelatedUser.from_json(json)
# print the JSON string representation of the object
print RelatedUser.to_json()

# convert the object into a dict
related_user_dict = related_user_instance.to_dict()
# create an instance of RelatedUser from a dict
related_user_form_dict = related_user.from_dict(related_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


