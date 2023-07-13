# dream3d.UtilsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_opengraph_api_v1_utils_opengraph_get**](UtilsApi.md#get_opengraph_api_v1_utils_opengraph_get) | **GET** /api/v1/utils/opengraph | Get Opengraph
[**get_opengraph_url_api_v1_utils_opengraph_url_get**](UtilsApi.md#get_opengraph_url_api_v1_utils_opengraph_url_get) | **GET** /api/v1/utils/opengraph-url | Get Opengraph Url
[**test_celery_api_v1_utils_test_celery_post**](UtilsApi.md#test_celery_api_v1_utils_test_celery_post) | **POST** /api/v1/utils/test-celery/ | Test Celery
[**test_email_api_v1_utils_test_email_post**](UtilsApi.md#test_email_api_v1_utils_test_email_post) | **POST** /api/v1/utils/test-email/ | Test Email
[**test_posthog_api_v1_utils_test_posthog_post**](UtilsApi.md#test_posthog_api_v1_utils_test_posthog_post) | **POST** /api/v1/utils/test/posthog | Test Posthog
[**test_sentry_api_v1_utils_test_sentry_post**](UtilsApi.md#test_sentry_api_v1_utils_test_sentry_post) | **POST** /api/v1/utils/test/sentry | Test Sentry
[**test_sms_api_v1_utils_test_sms_post**](UtilsApi.md#test_sms_api_v1_utils_test_sms_post) | **POST** /api/v1/utils/test/sms | Test Sms
[**update_mesh_index_api_v1_utils_search_update_mesh_post**](UtilsApi.md#update_mesh_index_api_v1_utils_search_update_mesh_post) | **POST** /api/v1/utils/search/update-mesh | Update Mesh Index


# **get_opengraph_api_v1_utils_opengraph_get**
> OpenGraph get_opengraph_api_v1_utils_opengraph_get(path)

Get Opengraph

### Example

```python
import time
import os
import dream3d
from dream3d.models.open_graph import OpenGraph
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
    api_instance = dream3d.UtilsApi(api_client)
    path = 'path_example' # str | 

    try:
        # Get Opengraph
        api_response = await api_instance.get_opengraph_api_v1_utils_opengraph_get(path)
        print("The response of UtilsApi->get_opengraph_api_v1_utils_opengraph_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->get_opengraph_api_v1_utils_opengraph_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 

### Return type

[**OpenGraph**](OpenGraph.md)

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

# **get_opengraph_url_api_v1_utils_opengraph_url_get**
> object get_opengraph_url_api_v1_utils_opengraph_url_get(path)

Get Opengraph Url

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
    api_instance = dream3d.UtilsApi(api_client)
    path = 'path_example' # str | 

    try:
        # Get Opengraph Url
        api_response = await api_instance.get_opengraph_url_api_v1_utils_opengraph_url_get(path)
        print("The response of UtilsApi->get_opengraph_url_api_v1_utils_opengraph_url_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->get_opengraph_url_api_v1_utils_opengraph_url_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | 

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

# **test_celery_api_v1_utils_test_celery_post**
> Msg test_celery_api_v1_utils_test_celery_post(msg)

Test Celery

Test Celery worker.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import dream3d
from dream3d.models.msg import Msg
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
    api_instance = dream3d.UtilsApi(api_client)
    msg = dream3d.Msg() # Msg | 

    try:
        # Test Celery
        api_response = await api_instance.test_celery_api_v1_utils_test_celery_post(msg)
        print("The response of UtilsApi->test_celery_api_v1_utils_test_celery_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->test_celery_api_v1_utils_test_celery_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **msg** | [**Msg**](Msg.md)|  | 

### Return type

[**Msg**](Msg.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_email_api_v1_utils_test_email_post**
> Msg test_email_api_v1_utils_test_email_post(email_to)

Test Email

Test emails.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import dream3d
from dream3d.models.msg import Msg
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
    api_instance = dream3d.UtilsApi(api_client)
    email_to = 'email_to_example' # str | 

    try:
        # Test Email
        api_response = await api_instance.test_email_api_v1_utils_test_email_post(email_to)
        print("The response of UtilsApi->test_email_api_v1_utils_test_email_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->test_email_api_v1_utils_test_email_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_to** | **str**|  | 

### Return type

[**Msg**](Msg.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_posthog_api_v1_utils_test_posthog_post**
> Msg test_posthog_api_v1_utils_test_posthog_post()

Test Posthog

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import dream3d
from dream3d.models.msg import Msg
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
    api_instance = dream3d.UtilsApi(api_client)

    try:
        # Test Posthog
        api_response = await api_instance.test_posthog_api_v1_utils_test_posthog_post()
        print("The response of UtilsApi->test_posthog_api_v1_utils_test_posthog_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->test_posthog_api_v1_utils_test_posthog_post: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Msg**](Msg.md)

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

# **test_sentry_api_v1_utils_test_sentry_post**
> test_sentry_api_v1_utils_test_sentry_post()

Test Sentry

### Example

* OAuth Authentication (OAuth2PasswordBearer):
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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with dream3d.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dream3d.UtilsApi(api_client)

    try:
        # Test Sentry
        await api_instance.test_sentry_api_v1_utils_test_sentry_post()
    except Exception as e:
        print("Exception when calling UtilsApi->test_sentry_api_v1_utils_test_sentry_post: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_sms_api_v1_utils_test_sms_post**
> Msg test_sms_api_v1_utils_test_sms_post(to, msg)

Test Sms

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import dream3d
from dream3d.models.msg import Msg
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
    api_instance = dream3d.UtilsApi(api_client)
    to = 'to_example' # str | 
    msg = 'msg_example' # str | 

    try:
        # Test Sms
        api_response = await api_instance.test_sms_api_v1_utils_test_sms_post(to, msg)
        print("The response of UtilsApi->test_sms_api_v1_utils_test_sms_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->test_sms_api_v1_utils_test_sms_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **to** | **str**|  | 
 **msg** | **str**|  | 

### Return type

[**Msg**](Msg.md)

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

# **update_mesh_index_api_v1_utils_search_update_mesh_post**
> Msg update_mesh_index_api_v1_utils_search_update_mesh_post()

Update Mesh Index

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import dream3d
from dream3d.models.msg import Msg
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
    api_instance = dream3d.UtilsApi(api_client)

    try:
        # Update Mesh Index
        api_response = await api_instance.update_mesh_index_api_v1_utils_search_update_mesh_post()
        print("The response of UtilsApi->update_mesh_index_api_v1_utils_search_update_mesh_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UtilsApi->update_mesh_index_api_v1_utils_search_update_mesh_post: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Msg**](Msg.md)

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

