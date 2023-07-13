# dream3d.MaterialsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_v1_materials_post**](MaterialsApi.md#create_api_v1_materials_post) | **POST** /api/v1/materials/ | Create
[**get_api_v1_materials_material_id_get**](MaterialsApi.md#get_api_v1_materials_material_id_get) | **GET** /api/v1/materials/{material_id} | Get
[**update_api_v1_materials_material_id_put**](MaterialsApi.md#update_api_v1_materials_material_id_put) | **PUT** /api/v1/materials/{material_id} | Update


# **create_api_v1_materials_post**
> Material create_api_v1_materials_post(material_create_upload)

Create

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import dream3d
from dream3d.models.material import Material
from dream3d.models.material_create_upload import MaterialCreateUpload
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
    api_instance = dream3d.MaterialsApi(api_client)
    material_create_upload = dream3d.MaterialCreateUpload() # MaterialCreateUpload | 

    try:
        # Create
        api_response = await api_instance.create_api_v1_materials_post(material_create_upload)
        print("The response of MaterialsApi->create_api_v1_materials_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaterialsApi->create_api_v1_materials_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **material_create_upload** | [**MaterialCreateUpload**](MaterialCreateUpload.md)|  | 

### Return type

[**Material**](Material.md)

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

# **get_api_v1_materials_material_id_get**
> Material get_api_v1_materials_material_id_get(material_id)

Get

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import dream3d
from dream3d.models.material import Material
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
    api_instance = dream3d.MaterialsApi(api_client)
    material_id = 'material_id_example' # str | 

    try:
        # Get
        api_response = await api_instance.get_api_v1_materials_material_id_get(material_id)
        print("The response of MaterialsApi->get_api_v1_materials_material_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaterialsApi->get_api_v1_materials_material_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **material_id** | **str**|  | 

### Return type

[**Material**](Material.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_api_v1_materials_material_id_put**
> Material update_api_v1_materials_material_id_put(material_id, material_update)

Update

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import dream3d
from dream3d.models.material import Material
from dream3d.models.material_update import MaterialUpdate
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
    api_instance = dream3d.MaterialsApi(api_client)
    material_id = 'material_id_example' # str | 
    material_update = dream3d.MaterialUpdate() # MaterialUpdate | 

    try:
        # Update
        api_response = await api_instance.update_api_v1_materials_material_id_put(material_id, material_update)
        print("The response of MaterialsApi->update_api_v1_materials_material_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaterialsApi->update_api_v1_materials_material_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **material_id** | **str**|  | 
 **material_update** | [**MaterialUpdate**](MaterialUpdate.md)|  | 

### Return type

[**Material**](Material.md)

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

