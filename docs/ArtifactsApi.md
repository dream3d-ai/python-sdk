# dream3d.ArtifactsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_api_v1_artifacts_project_project_id_get**](ArtifactsApi.md#get_all_api_v1_artifacts_project_project_id_get) | **GET** /api/v1/artifacts/project/{project_id} | Get All
[**get_api_v1_artifacts_artifact_id_get**](ArtifactsApi.md#get_api_v1_artifacts_artifact_id_get) | **GET** /api/v1/artifacts/{artifact_id} | Get
[**get_children_artifacts_api_v1_artifacts_project_project_id_parent_id_get**](ArtifactsApi.md#get_children_artifacts_api_v1_artifacts_project_project_id_parent_id_get) | **GET** /api/v1/artifacts/project/{project_id}/{parent_id} | Get Children Artifacts
[**get_feed_api_v1_artifacts_feed_get**](ArtifactsApi.md#get_feed_api_v1_artifacts_feed_get) | **GET** /api/v1/artifacts/feed | Get Feed
[**get_opengraph_url_api_v1_artifacts_artifact_id_og_get**](ArtifactsApi.md#get_opengraph_url_api_v1_artifacts_artifact_id_og_get) | **GET** /api/v1/artifacts/{artifact_id}/og | Get Opengraph Url
[**get_public_url_api_v1_artifacts_artifact_id_public_get**](ArtifactsApi.md#get_public_url_api_v1_artifacts_artifact_id_public_get) | **GET** /api/v1/artifacts/{artifact_id}/public | Get Public Url
[**get_templates_api_v1_artifacts_templates_get**](ArtifactsApi.md#get_templates_api_v1_artifacts_templates_get) | **GET** /api/v1/artifacts/templates | Get Templates
[**get_url_api_v1_artifacts_artifact_id_url_get**](ArtifactsApi.md#get_url_api_v1_artifacts_artifact_id_url_get) | **GET** /api/v1/artifacts/{artifact_id}/url | Get Url
[**like_api_v1_artifacts_artifact_id_like_put**](ArtifactsApi.md#like_api_v1_artifacts_artifact_id_like_put) | **PUT** /api/v1/artifacts/{artifact_id}/like | Like
[**record_view_api_v1_artifacts_artifact_id_view_post**](ArtifactsApi.md#record_view_api_v1_artifacts_artifact_id_view_post) | **POST** /api/v1/artifacts/{artifact_id}/view | Record View
[**remix_api_v1_artifacts_artifact_id_remix_post**](ArtifactsApi.md#remix_api_v1_artifacts_artifact_id_remix_post) | **POST** /api/v1/artifacts/{artifact_id}/remix | Remix
[**toggle_like_api_v1_artifacts_artifact_id_toggle_like_put**](ArtifactsApi.md#toggle_like_api_v1_artifacts_artifact_id_toggle_like_put) | **PUT** /api/v1/artifacts/{artifact_id}/toggle-like | Toggle Like
[**unlike_api_v1_artifacts_artifact_id_unlike_put**](ArtifactsApi.md#unlike_api_v1_artifacts_artifact_id_unlike_put) | **PUT** /api/v1/artifacts/{artifact_id}/unlike | Unlike
[**update_api_v1_artifacts_artifact_id_put**](ArtifactsApi.md#update_api_v1_artifacts_artifact_id_put) | **PUT** /api/v1/artifacts/{artifact_id} | Update
[**upscale_api_v1_artifacts_artifact_id_upscale_post**](ArtifactsApi.md#upscale_api_v1_artifacts_artifact_id_upscale_post) | **POST** /api/v1/artifacts/{artifact_id}/upscale | Upscale


# **get_all_api_v1_artifacts_project_project_id_get**
> List[Artifact] get_all_api_v1_artifacts_project_project_id_get(project_id, skip=skip, limit=limit, type=type)

Get All

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import dream3d
from dream3d.models.artifact import Artifact
from dream3d.models.artifact_type import ArtifactType
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
    api_instance = dream3d.ArtifactsApi(api_client)
    project_id = 'project_id_example' # str | 
    skip = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)
    type = dream3d.ArtifactType() # ArtifactType |  (optional)

    try:
        # Get All
        api_response = await api_instance.get_all_api_v1_artifacts_project_project_id_get(project_id, skip=skip, limit=limit, type=type)
        print("The response of ArtifactsApi->get_all_api_v1_artifacts_project_project_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactsApi->get_all_api_v1_artifacts_project_project_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]
 **type** | [**ArtifactType**](.md)|  | [optional] 

### Return type

[**List[Artifact]**](Artifact.md)

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

# **get_api_v1_artifacts_artifact_id_get**
> Artifact get_api_v1_artifacts_artifact_id_get(artifact_id)

Get

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import dream3d
from dream3d.models.artifact import Artifact
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
    api_instance = dream3d.ArtifactsApi(api_client)
    artifact_id = 'artifact_id_example' # str | 

    try:
        # Get
        api_response = await api_instance.get_api_v1_artifacts_artifact_id_get(artifact_id)
        print("The response of ArtifactsApi->get_api_v1_artifacts_artifact_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactsApi->get_api_v1_artifacts_artifact_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifact_id** | **str**|  | 

### Return type

[**Artifact**](Artifact.md)

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

# **get_children_artifacts_api_v1_artifacts_project_project_id_parent_id_get**
> List[Artifact] get_children_artifacts_api_v1_artifacts_project_project_id_parent_id_get(project_id, parent_id, skip=skip, limit=limit, type=type)

Get Children Artifacts

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import dream3d
from dream3d.models.artifact import Artifact
from dream3d.models.artifact_type import ArtifactType
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
    api_instance = dream3d.ArtifactsApi(api_client)
    project_id = 'project_id_example' # str | 
    parent_id = 'parent_id_example' # str | 
    skip = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)
    type = dream3d.ArtifactType() # ArtifactType |  (optional)

    try:
        # Get Children Artifacts
        api_response = await api_instance.get_children_artifacts_api_v1_artifacts_project_project_id_parent_id_get(project_id, parent_id, skip=skip, limit=limit, type=type)
        print("The response of ArtifactsApi->get_children_artifacts_api_v1_artifacts_project_project_id_parent_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactsApi->get_children_artifacts_api_v1_artifacts_project_project_id_parent_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **parent_id** | **str**|  | 
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]
 **type** | [**ArtifactType**](.md)|  | [optional] 

### Return type

[**List[Artifact]**](Artifact.md)

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

# **get_feed_api_v1_artifacts_feed_get**
> List[Artifact] get_feed_api_v1_artifacts_feed_get(skip=skip, limit=limit)

Get Feed

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import dream3d
from dream3d.models.artifact import Artifact
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
    api_instance = dream3d.ArtifactsApi(api_client)
    skip = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Get Feed
        api_response = await api_instance.get_feed_api_v1_artifacts_feed_get(skip=skip, limit=limit)
        print("The response of ArtifactsApi->get_feed_api_v1_artifacts_feed_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactsApi->get_feed_api_v1_artifacts_feed_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**List[Artifact]**](Artifact.md)

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

# **get_opengraph_url_api_v1_artifacts_artifact_id_og_get**
> Image get_opengraph_url_api_v1_artifacts_artifact_id_og_get(artifact_id)

Get Opengraph Url

### Example

```python
import time
import os
import dream3d
from dream3d.models.image import Image
from dream3d.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dream3d.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with dream3d.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dream3d.ArtifactsApi(api_client)
    artifact_id = 'artifact_id_example' # str | 

    try:
        # Get Opengraph Url
        api_response = await api_instance.get_opengraph_url_api_v1_artifacts_artifact_id_og_get(artifact_id)
        print("The response of ArtifactsApi->get_opengraph_url_api_v1_artifacts_artifact_id_og_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactsApi->get_opengraph_url_api_v1_artifacts_artifact_id_og_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifact_id** | **str**|  | 

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_url_api_v1_artifacts_artifact_id_public_get**
> object get_public_url_api_v1_artifacts_artifact_id_public_get(artifact_id)

Get Public Url

### Example

```python
import time
import os
import dream3d
from dream3d.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dream3d.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with dream3d.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dream3d.ArtifactsApi(api_client)
    artifact_id = 'artifact_id_example' # str | 

    try:
        # Get Public Url
        api_response = await api_instance.get_public_url_api_v1_artifacts_artifact_id_public_get(artifact_id)
        print("The response of ArtifactsApi->get_public_url_api_v1_artifacts_artifact_id_public_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactsApi->get_public_url_api_v1_artifacts_artifact_id_public_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifact_id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_templates_api_v1_artifacts_templates_get**
> List[Artifact] get_templates_api_v1_artifacts_templates_get(skip=skip, limit=limit)

Get Templates

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import dream3d
from dream3d.models.artifact import Artifact
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
    api_instance = dream3d.ArtifactsApi(api_client)
    skip = 0 # int |  (optional) (default to 0)
    limit = 100 # int |  (optional) (default to 100)

    try:
        # Get Templates
        api_response = await api_instance.get_templates_api_v1_artifacts_templates_get(skip=skip, limit=limit)
        print("The response of ArtifactsApi->get_templates_api_v1_artifacts_templates_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactsApi->get_templates_api_v1_artifacts_templates_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**List[Artifact]**](Artifact.md)

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

# **get_url_api_v1_artifacts_artifact_id_url_get**
> Image get_url_api_v1_artifacts_artifact_id_url_get(artifact_id)

Get Url

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import dream3d
from dream3d.models.image import Image
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
    api_instance = dream3d.ArtifactsApi(api_client)
    artifact_id = 'artifact_id_example' # str | 

    try:
        # Get Url
        api_response = await api_instance.get_url_api_v1_artifacts_artifact_id_url_get(artifact_id)
        print("The response of ArtifactsApi->get_url_api_v1_artifacts_artifact_id_url_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactsApi->get_url_api_v1_artifacts_artifact_id_url_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifact_id** | **str**|  | 

### Return type

[**Image**](Image.md)

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

# **like_api_v1_artifacts_artifact_id_like_put**
> Artifact like_api_v1_artifacts_artifact_id_like_put(artifact_id)

Like

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import dream3d
from dream3d.models.artifact import Artifact
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
    api_instance = dream3d.ArtifactsApi(api_client)
    artifact_id = 'artifact_id_example' # str | 

    try:
        # Like
        api_response = await api_instance.like_api_v1_artifacts_artifact_id_like_put(artifact_id)
        print("The response of ArtifactsApi->like_api_v1_artifacts_artifact_id_like_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactsApi->like_api_v1_artifacts_artifact_id_like_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifact_id** | **str**|  | 

### Return type

[**Artifact**](Artifact.md)

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

# **record_view_api_v1_artifacts_artifact_id_view_post**
> Artifact record_view_api_v1_artifacts_artifact_id_view_post(artifact_id)

Record View

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import dream3d
from dream3d.models.artifact import Artifact
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
    api_instance = dream3d.ArtifactsApi(api_client)
    artifact_id = 'artifact_id_example' # str | 

    try:
        # Record View
        api_response = await api_instance.record_view_api_v1_artifacts_artifact_id_view_post(artifact_id)
        print("The response of ArtifactsApi->record_view_api_v1_artifacts_artifact_id_view_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactsApi->record_view_api_v1_artifacts_artifact_id_view_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifact_id** | **str**|  | 

### Return type

[**Artifact**](Artifact.md)

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

# **remix_api_v1_artifacts_artifact_id_remix_post**
> Project remix_api_v1_artifacts_artifact_id_remix_post(artifact_id)

Remix

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
    api_instance = dream3d.ArtifactsApi(api_client)
    artifact_id = 'artifact_id_example' # str | 

    try:
        # Remix
        api_response = await api_instance.remix_api_v1_artifacts_artifact_id_remix_post(artifact_id)
        print("The response of ArtifactsApi->remix_api_v1_artifacts_artifact_id_remix_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactsApi->remix_api_v1_artifacts_artifact_id_remix_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifact_id** | **str**|  | 

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

# **toggle_like_api_v1_artifacts_artifact_id_toggle_like_put**
> Artifact toggle_like_api_v1_artifacts_artifact_id_toggle_like_put(artifact_id)

Toggle Like

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import dream3d
from dream3d.models.artifact import Artifact
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
    api_instance = dream3d.ArtifactsApi(api_client)
    artifact_id = 'artifact_id_example' # str | 

    try:
        # Toggle Like
        api_response = await api_instance.toggle_like_api_v1_artifacts_artifact_id_toggle_like_put(artifact_id)
        print("The response of ArtifactsApi->toggle_like_api_v1_artifacts_artifact_id_toggle_like_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactsApi->toggle_like_api_v1_artifacts_artifact_id_toggle_like_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifact_id** | **str**|  | 

### Return type

[**Artifact**](Artifact.md)

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

# **unlike_api_v1_artifacts_artifact_id_unlike_put**
> Artifact unlike_api_v1_artifacts_artifact_id_unlike_put(artifact_id)

Unlike

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import dream3d
from dream3d.models.artifact import Artifact
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
    api_instance = dream3d.ArtifactsApi(api_client)
    artifact_id = 'artifact_id_example' # str | 

    try:
        # Unlike
        api_response = await api_instance.unlike_api_v1_artifacts_artifact_id_unlike_put(artifact_id)
        print("The response of ArtifactsApi->unlike_api_v1_artifacts_artifact_id_unlike_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactsApi->unlike_api_v1_artifacts_artifact_id_unlike_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifact_id** | **str**|  | 

### Return type

[**Artifact**](Artifact.md)

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

# **update_api_v1_artifacts_artifact_id_put**
> Artifact update_api_v1_artifacts_artifact_id_put(artifact_id, artifact_update)

Update

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import dream3d
from dream3d.models.artifact import Artifact
from dream3d.models.artifact_update import ArtifactUpdate
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
    api_instance = dream3d.ArtifactsApi(api_client)
    artifact_id = 'artifact_id_example' # str | 
    artifact_update = dream3d.ArtifactUpdate() # ArtifactUpdate | 

    try:
        # Update
        api_response = await api_instance.update_api_v1_artifacts_artifact_id_put(artifact_id, artifact_update)
        print("The response of ArtifactsApi->update_api_v1_artifacts_artifact_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactsApi->update_api_v1_artifacts_artifact_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifact_id** | **str**|  | 
 **artifact_update** | [**ArtifactUpdate**](ArtifactUpdate.md)|  | 

### Return type

[**Artifact**](Artifact.md)

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

# **upscale_api_v1_artifacts_artifact_id_upscale_post**
> Artifact upscale_api_v1_artifacts_artifact_id_upscale_post(artifact_id, render_payload)

Upscale

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
    api_instance = dream3d.ArtifactsApi(api_client)
    artifact_id = 'artifact_id_example' # str | 
    render_payload = dream3d.RenderPayload() # RenderPayload | 

    try:
        # Upscale
        api_response = await api_instance.upscale_api_v1_artifacts_artifact_id_upscale_post(artifact_id, render_payload)
        print("The response of ArtifactsApi->upscale_api_v1_artifacts_artifact_id_upscale_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ArtifactsApi->upscale_api_v1_artifacts_artifact_id_upscale_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifact_id** | **str**|  | 
 **render_payload** | [**RenderPayload**](RenderPayload.md)|  | 

### Return type

[**Artifact**](Artifact.md)

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

