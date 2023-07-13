# MeterUsage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usage** | **int** |  | 
**limit** | **int** |  | 
**subscription** | [**SubscriptionType**](SubscriptionType.md) |  | 

## Example

```python
from dream3d.models.meter_usage import MeterUsage

# TODO update the JSON string below
json = "{}"
# create an instance of MeterUsage from a JSON string
meter_usage_instance = MeterUsage.from_json(json)
# print the JSON string representation of the object
print MeterUsage.to_json()

# convert the object into a dict
meter_usage_dict = meter_usage_instance.to_dict()
# create an instance of MeterUsage from a dict
meter_usage_form_dict = meter_usage.from_dict(meter_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


