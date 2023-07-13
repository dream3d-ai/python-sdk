# dream3d.MeshesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_avatar_api_v1_meshes_avatar_post**](MeshesApi.md#create_avatar_api_v1_meshes_avatar_post) | **POST** /api/v1/meshes/avatar | Create Avatar
[**create_prompt_api_v1_meshes_prompt_post**](MeshesApi.md#create_prompt_api_v1_meshes_prompt_post) | **POST** /api/v1/meshes/prompt | Create Prompt
[**create_upload_api_v1_meshes_upload_post**](MeshesApi.md#create_upload_api_v1_meshes_upload_post) | **POST** /api/v1/meshes/upload | Create Upload
[**delete_api_v1_meshes_mesh_id_delete**](MeshesApi.md#delete_api_v1_meshes_mesh_id_delete) | **DELETE** /api/v1/meshes/{mesh_id} | Delete
[**get_all_api_v1_meshes_get**](MeshesApi.md#get_all_api_v1_meshes_get) | **GET** /api/v1/meshes/ | Get All
[**get_api_v1_meshes_mesh_id_get**](MeshesApi.md#get_api_v1_meshes_mesh_id_get) | **GET** /api/v1/meshes/{mesh_id} | Get
[**regenerate_prompt_api_v1_meshes_regenerate_mesh_id_put**](MeshesApi.md#regenerate_prompt_api_v1_meshes_regenerate_mesh_id_put) | **PUT** /api/v1/meshes/regenerate/{mesh_id} | Regenerate Prompt
[**search_api_v1_meshes_search_get**](MeshesApi.md#search_api_v1_meshes_search_get) | **GET** /api/v1/meshes/search | Search
[**update_api_v1_meshes_mesh_id_put**](MeshesApi.md#update_api_v1_meshes_mesh_id_put) | **PUT** /api/v1/meshes/{mesh_id} | Update


# **create_avatar_api_v1_meshes_avatar_post**
> Mesh create_avatar_api_v1_meshes_avatar_post(name, project_id, x, y, width, height, file)

Create Avatar

Generate a new avatar.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import dream3d
from dream3d.models.mesh import Mesh
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
    api_instance = dream3d.MeshesApi(api_client)
    name = 'name_example' # str | 
    project_id = 'project_id_example' # str | 
    x = 56 # int | 
    y = 56 # int | 
    width = 56 # int | 
    height = 56 # int | 
    file = None # bytearray | 

    try:
        # Create Avatar
        api_response = await api_instance.create_avatar_api_v1_meshes_avatar_post(name, project_id, x, y, width, height, file)
        print("The response of MeshesApi->create_avatar_api_v1_meshes_avatar_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeshesApi->create_avatar_api_v1_meshes_avatar_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **project_id** | **str**|  | 
 **x** | **int**|  | 
 **y** | **int**|  | 
 **width** | **int**|  | 
 **height** | **int**|  | 
 **file** | **bytearray**|  | 

### Return type

[**Mesh**](Mesh.md)

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

# **create_prompt_api_v1_meshes_prompt_post**
> Mesh create_prompt_api_v1_meshes_prompt_post(mesh_create_generate, project_id=project_id)

Create Prompt

Generate a new mesh.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import dream3d
from dream3d.models.mesh import Mesh
from dream3d.models.mesh_create_generate import MeshCreateGenerate
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
    api_instance = dream3d.MeshesApi(api_client)
    mesh_create_generate = dream3d.MeshCreateGenerate() # MeshCreateGenerate | 
    project_id = 'project_id_example' # str |  (optional)

    try:
        # Create Prompt
        api_response = await api_instance.create_prompt_api_v1_meshes_prompt_post(mesh_create_generate, project_id=project_id)
        print("The response of MeshesApi->create_prompt_api_v1_meshes_prompt_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeshesApi->create_prompt_api_v1_meshes_prompt_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mesh_create_generate** | [**MeshCreateGenerate**](MeshCreateGenerate.md)|  | 
 **project_id** | **str**|  | [optional] 

### Return type

[**Mesh**](Mesh.md)

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

# **create_upload_api_v1_meshes_upload_post**
> Mesh create_upload_api_v1_meshes_upload_post(file, project_id=project_id)

Create Upload

Upload a mesh.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import dream3d
from dream3d.models.mesh import Mesh
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
    api_instance = dream3d.MeshesApi(api_client)
    file = None # bytearray | 
    project_id = 'project_id_example' # str |  (optional)

    try:
        # Create Upload
        api_response = await api_instance.create_upload_api_v1_meshes_upload_post(file, project_id=project_id)
        print("The response of MeshesApi->create_upload_api_v1_meshes_upload_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeshesApi->create_upload_api_v1_meshes_upload_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | 
 **project_id** | **str**|  | [optional] 

### Return type

[**Mesh**](Mesh.md)

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

# **delete_api_v1_meshes_mesh_id_delete**
> Mesh delete_api_v1_meshes_mesh_id_delete(mesh_id)

Delete

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import dream3d
from dream3d.models.mesh import Mesh
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
    api_instance = dream3d.MeshesApi(api_client)
    mesh_id = 'mesh_id_example' # str | 

    try:
        # Delete
        api_response = await api_instance.delete_api_v1_meshes_mesh_id_delete(mesh_id)
        print("The response of MeshesApi->delete_api_v1_meshes_mesh_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeshesApi->delete_api_v1_meshes_mesh_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mesh_id** | **str**|  | 

### Return type

[**Mesh**](Mesh.md)

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

# **get_all_api_v1_meshes_get**
> List[Mesh] get_all_api_v1_meshes_get(skip=skip, limit=limit, public=public, name_filter=name_filter, project_id=project_id, category=category)

Get All

Get all meshes for user.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import dream3d
from dream3d.models.mesh import Mesh
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
    api_instance = dream3d.MeshesApi(api_client)
    skip = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)
    public = False # bool |  (optional) (default to False)
    name_filter = 'name_filter_example' # str |  (optional)
    project_id = 'project_id_example' # str |  (optional)
    category = dream3d.MeshCategory() # MeshCategory |  (optional)

    try:
        # Get All
        api_response = await api_instance.get_all_api_v1_meshes_get(skip=skip, limit=limit, public=public, name_filter=name_filter, project_id=project_id, category=category)
        print("The response of MeshesApi->get_all_api_v1_meshes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeshesApi->get_all_api_v1_meshes_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]
 **public** | **bool**|  | [optional] [default to False]
 **name_filter** | **str**|  | [optional] 
 **project_id** | **str**|  | [optional] 
 **category** | [**MeshCategory**](.md)|  | [optional] 

### Return type

[**List[Mesh]**](Mesh.md)

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

# **get_api_v1_meshes_mesh_id_get**
> Mesh get_api_v1_meshes_mesh_id_get(mesh_id)

Get

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import dream3d
from dream3d.models.mesh import Mesh
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
    api_instance = dream3d.MeshesApi(api_client)
    mesh_id = 'mesh_id_example' # str | 

    try:
        # Get
        api_response = await api_instance.get_api_v1_meshes_mesh_id_get(mesh_id)
        print("The response of MeshesApi->get_api_v1_meshes_mesh_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeshesApi->get_api_v1_meshes_mesh_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mesh_id** | **str**|  | 

### Return type

[**Mesh**](Mesh.md)

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

# **regenerate_prompt_api_v1_meshes_regenerate_mesh_id_put**
> Mesh regenerate_prompt_api_v1_meshes_regenerate_mesh_id_put(mesh_id)

Regenerate Prompt

Re-generate a mesh

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import dream3d
from dream3d.models.mesh import Mesh
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
    api_instance = dream3d.MeshesApi(api_client)
    mesh_id = 'mesh_id_example' # str | 

    try:
        # Regenerate Prompt
        api_response = await api_instance.regenerate_prompt_api_v1_meshes_regenerate_mesh_id_put(mesh_id)
        print("The response of MeshesApi->regenerate_prompt_api_v1_meshes_regenerate_mesh_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeshesApi->regenerate_prompt_api_v1_meshes_regenerate_mesh_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mesh_id** | **str**|  | 

### Return type

[**Mesh**](Mesh.md)

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

# **search_api_v1_meshes_search_get**
> List[Mesh] search_api_v1_meshes_search_get(query=query, skip=skip, limit=limit)

Search

Search public meshes

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import dream3d
from dream3d.models.mesh import Mesh
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
    api_instance = dream3d.MeshesApi(api_client)
    query = '' # str |  (optional) (default to '')
    skip = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Search
        api_response = await api_instance.search_api_v1_meshes_search_get(query=query, skip=skip, limit=limit)
        print("The response of MeshesApi->search_api_v1_meshes_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeshesApi->search_api_v1_meshes_search_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | [optional] [default to &#39;&#39;]
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**List[Mesh]**](Mesh.md)

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

# **update_api_v1_meshes_mesh_id_put**
> Mesh update_api_v1_meshes_mesh_id_put(mesh_id, mesh_update)

Update

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import dream3d
from dream3d.models.mesh import Mesh
from dream3d.models.mesh_update import MeshUpdate
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
    api_instance = dream3d.MeshesApi(api_client)
    mesh_id = 'mesh_id_example' # str | 
    mesh_update = dream3d.MeshUpdate() # MeshUpdate | 

    try:
        # Update
        api_response = await api_instance.update_api_v1_meshes_mesh_id_put(mesh_id, mesh_update)
        print("The response of MeshesApi->update_api_v1_meshes_mesh_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeshesApi->update_api_v1_meshes_mesh_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mesh_id** | **str**|  | 
 **mesh_update** | [**MeshUpdate**](MeshUpdate.md)|  | 

### Return type

[**Mesh**](Mesh.md)

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

