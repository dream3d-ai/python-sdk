# dream3d.RenderApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_v1_render_project_id_post**](RenderApi.md#create_api_v1_render_project_id_post) | **POST** /api/v1/render/{project_id} | Create
[**extract_prompt_api_v1_render_extract_prompt_post**](RenderApi.md#extract_prompt_api_v1_render_extract_prompt_post) | **POST** /api/v1/render/extract-prompt | Extract Prompt


# **create_api_v1_render_project_id_post**
> List[Artifact] create_api_v1_render_project_id_post(project_id, render_payload)

Create

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import dream3d
from dream3d.models.artifact import Artifact
from dream3d.models.render_payload import RenderPayload
from dream3d.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dream3d.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with dream3d.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dream3d.RenderApi(api_client)
    project_id = 'project_id_example' # str | 
    render_payload = dream3d.RenderPayload() # RenderPayload | 

    try:
        # Create
        api_response = await api_instance.create_api_v1_render_project_id_post(project_id, render_payload)
        print("The response of RenderApi->create_api_v1_render_project_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RenderApi->create_api_v1_render_project_id_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **render_payload** | [**RenderPayload**](RenderPayload.md)|  | 

### Return type

[**List[Artifact]**](Artifact.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extract_prompt_api_v1_render_extract_prompt_post**
> ExtractPromptOut extract_prompt_api_v1_render_extract_prompt_post(image_in)

Extract Prompt

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import dream3d
from dream3d.models.extract_prompt_out import ExtractPromptOut
from dream3d.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dream3d.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with dream3d.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dream3d.RenderApi(api_client)
    image_in = None # bytearray | 

    try:
        # Extract Prompt
        api_response = await api_instance.extract_prompt_api_v1_render_extract_prompt_post(image_in)
        print("The response of RenderApi->extract_prompt_api_v1_render_extract_prompt_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RenderApi->extract_prompt_api_v1_render_extract_prompt_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_in** | **bytearray**|  | 

### Return type

[**ExtractPromptOut**](ExtractPromptOut.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

