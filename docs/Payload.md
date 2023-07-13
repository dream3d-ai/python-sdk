# Payload


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt** | **str** |  | [optional] [default to '']
**negative_prompt** | **str** |  | [optional] 
**scene** | [**Scene**](Scene.md) |  | [optional] 
**aspect_ratio** | [**RenderAspectRatio**](RenderAspectRatio.md) |  | [optional] 
**num_images_per_prompt** | **int** |  | [optional] [default to 1]
**strength** | **float** |  | [optional] [default to 0.75]
**material_alpha** | **float** |  | [optional] [default to 1.0]
**num_inference_steps** | **int** |  | [optional] [default to 20]
**num_reference_free_steps** | **int** |  | [optional] [default to 0]
**num_control_free_steps** | **int** |  | [optional] [default to 0]
**guidance_scale** | **float** |  | [optional] [default to 7.5]
**blur_radius** | **float** |  | [optional] [default to 0.0]
**seed** | **int** |  | [optional] 
**floor** | **bool** |  | [optional] [default to True]
**use_seed** | **bool** |  | [optional] [default to False]
**control_ranges** | **List[List[object]]** |  | [optional] 
**lora_ids** | **List[str]** |  | [optional] [default to []]
**lora_scales** | **List[float]** |  | [optional] [default to []]
**model_type** | [**WysiwygVersion**](WysiwygVersion.md) |  | [optional] 
**style_reference_id** | **str** |  | [optional] 

## Example

```python
from dream3d.models.payload import Payload

# TODO update the JSON string below
json = "{}"
# create an instance of Payload from a JSON string
payload_instance = Payload.from_json(json)
# print the JSON string representation of the object
print Payload.to_json()

# convert the object into a dict
payload_dict = payload_instance.to_dict()
# create an instance of Payload from a dict
payload_form_dict = payload.from_dict(payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


