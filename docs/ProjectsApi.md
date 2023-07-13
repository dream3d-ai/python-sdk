# dream3d.ProjectsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_mesh_api_v1_projects_project_id_meshes_mesh_id_put**](ProjectsApi.md#add_mesh_api_v1_projects_project_id_meshes_mesh_id_put) | **PUT** /api/v1/projects/{project_id}/meshes/{mesh_id} | Add Mesh
[**create_api_v1_projects_post**](ProjectsApi.md#create_api_v1_projects_post) | **POST** /api/v1/projects/ | Create
[**delete_api_v1_projects_project_id_delete**](ProjectsApi.md#delete_api_v1_projects_project_id_delete) | **DELETE** /api/v1/projects/{project_id} | Delete
[**get_all_api_v1_projects_get**](ProjectsApi.md#get_all_api_v1_projects_get) | **GET** /api/v1/projects/ | Get All
[**get_api_v1_projects_project_id_get**](ProjectsApi.md#get_api_v1_projects_project_id_get) | **GET** /api/v1/projects/{project_id} | Get
[**get_meshes_api_v1_projects_project_id_meshes_get**](ProjectsApi.md#get_meshes_api_v1_projects_project_id_meshes_get) | **GET** /api/v1/projects/{project_id}/meshes | Get Meshes
[**remove_mesh_api_v1_projects_project_id_meshes_mesh_id_delete**](ProjectsApi.md#remove_mesh_api_v1_projects_project_id_meshes_mesh_id_delete) | **DELETE** /api/v1/projects/{project_id}/meshes/{mesh_id} | Remove Mesh
[**update_api_v1_projects_project_id_put**](ProjectsApi.md#update_api_v1_projects_project_id_put) | **PUT** /api/v1/projects/{project_id} | Update


# **add_mesh_api_v1_projects_project_id_meshes_mesh_id_put**
> Project add_mesh_api_v1_projects_project_id_meshes_mesh_id_put(project_id, mesh_id)

Add Mesh

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import dream3d
from dream3d.models.project import Project
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
    api_instance = dream3d.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    mesh_id = 'mesh_id_example' # str | 

    try:
        # Add Mesh
        api_response = await api_instance.add_mesh_api_v1_projects_project_id_meshes_mesh_id_put(project_id, mesh_id)
        print("The response of ProjectsApi->add_mesh_api_v1_projects_project_id_meshes_mesh_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->add_mesh_api_v1_projects_project_id_meshes_mesh_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **mesh_id** | **str**|  | 

### Return type

[**Project**](Project.md)

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

# **create_api_v1_projects_post**
> Project create_api_v1_projects_post(project_create)

Create

Create new project.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import dream3d
from dream3d.models.project import Project
from dream3d.models.project_create import ProjectCreate
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
    api_instance = dream3d.ProjectsApi(api_client)
    project_create = dream3d.ProjectCreate() # ProjectCreate | 

    try:
        # Create
        api_response = await api_instance.create_api_v1_projects_post(project_create)
        print("The response of ProjectsApi->create_api_v1_projects_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->create_api_v1_projects_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_create** | [**ProjectCreate**](ProjectCreate.md)|  | 

### Return type

[**Project**](Project.md)

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

# **delete_api_v1_projects_project_id_delete**
> Project delete_api_v1_projects_project_id_delete(project_id)

Delete

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import dream3d
from dream3d.models.project import Project
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
    api_instance = dream3d.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        # Delete
        api_response = await api_instance.delete_api_v1_projects_project_id_delete(project_id)
        print("The response of ProjectsApi->delete_api_v1_projects_project_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->delete_api_v1_projects_project_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**Project**](Project.md)

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

# **get_all_api_v1_projects_get**
> List[Project] get_all_api_v1_projects_get()

Get All

Get all projects for user.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import dream3d
from dream3d.models.project import Project
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
    api_instance = dream3d.ProjectsApi(api_client)

    try:
        # Get All
        api_response = await api_instance.get_all_api_v1_projects_get()
        print("The response of ProjectsApi->get_all_api_v1_projects_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_all_api_v1_projects_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**List[Project]**](Project.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_projects_project_id_get**
> Project get_api_v1_projects_project_id_get(project_id)

Get

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import dream3d
from dream3d.models.project import Project
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
    api_instance = dream3d.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        # Get
        api_response = await api_instance.get_api_v1_projects_project_id_get(project_id)
        print("The response of ProjectsApi->get_api_v1_projects_project_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_api_v1_projects_project_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**Project**](Project.md)

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

# **get_meshes_api_v1_projects_project_id_meshes_get**
> List[Mesh] get_meshes_api_v1_projects_project_id_meshes_get(project_id)

Get Meshes

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
    api_instance = dream3d.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        # Get Meshes
        api_response = await api_instance.get_meshes_api_v1_projects_project_id_meshes_get(project_id)
        print("The response of ProjectsApi->get_meshes_api_v1_projects_project_id_meshes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_meshes_api_v1_projects_project_id_meshes_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

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

# **remove_mesh_api_v1_projects_project_id_meshes_mesh_id_delete**
> Project remove_mesh_api_v1_projects_project_id_meshes_mesh_id_delete(project_id, mesh_id)

Remove Mesh

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import dream3d
from dream3d.models.project import Project
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
    api_instance = dream3d.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    mesh_id = 'mesh_id_example' # str | 

    try:
        # Remove Mesh
        api_response = await api_instance.remove_mesh_api_v1_projects_project_id_meshes_mesh_id_delete(project_id, mesh_id)
        print("The response of ProjectsApi->remove_mesh_api_v1_projects_project_id_meshes_mesh_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->remove_mesh_api_v1_projects_project_id_meshes_mesh_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **mesh_id** | **str**|  | 

### Return type

[**Project**](Project.md)

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

# **update_api_v1_projects_project_id_put**
> Project update_api_v1_projects_project_id_put(project_id, project_update)

Update

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import dream3d
from dream3d.models.project import Project
from dream3d.models.project_update import ProjectUpdate
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
    api_instance = dream3d.ProjectsApi(api_client)
    project_id = 'project_id_example' # str | 
    project_update = dream3d.ProjectUpdate() # ProjectUpdate | 

    try:
        # Update
        api_response = await api_instance.update_api_v1_projects_project_id_put(project_id, project_update)
        print("The response of ProjectsApi->update_api_v1_projects_project_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->update_api_v1_projects_project_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **project_update** | [**ProjectUpdate**](ProjectUpdate.md)|  | 

### Return type

[**Project**](Project.md)

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

