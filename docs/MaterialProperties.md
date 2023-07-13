# MaterialProperties


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **object** |  | [optional] 
**color_tex** | [**ColorTex**](ColorTex.md) |  | [optional] 
**roughness** | **float** |  | [optional] [default to 0.0]
**roughness_tex** | [**RoughnessTex**](RoughnessTex.md) |  | [optional] 
**metalness** | **float** |  | [optional] [default to 0.0]
**metalness_tex** | [**MetalnessTex**](MetalnessTex.md) |  | [optional] 
**normal_tex** | [**NormalTex**](NormalTex.md) |  | [optional] 
**normaltilt_iar** | **float** |  | [optional] [default to 1.0]
**specular** | **float** |  | [optional] [default to 0.0]
**albedo_color** | **object** |  | [optional] 
**subsurface_color** | **object** |  | [optional] 
**radiation_length** | **float** |  | [optional] [default to 0.0]
**light_emission** | **float** |  | [optional] [default to 0.0]
**refraction_index** | **object** |  | [optional] 
**flags** | [**Flags**](Flags.md) |  | [optional] 

## Example

```python
from dream3d.models.material_properties import MaterialProperties

# TODO update the JSON string below
json = "{}"
# create an instance of MaterialProperties from a JSON string
material_properties_instance = MaterialProperties.from_json(json)
# print the JSON string representation of the object
print MaterialProperties.to_json()

# convert the object into a dict
material_properties_dict = material_properties_instance.to_dict()
# create an instance of MaterialProperties from a dict
material_properties_form_dict = material_properties.from_dict(material_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


