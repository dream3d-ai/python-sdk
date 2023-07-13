# dream3d.TasksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_v1_tasks_task_id_get**](TasksApi.md#get_api_v1_tasks_task_id_get) | **GET** /api/v1/tasks/{task_id} | Get


# **get_api_v1_tasks_task_id_get**
> TaskStatus get_api_v1_tasks_task_id_get(task_id)

Get

Get task status.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import time
import os
import dream3d
from dream3d.models.task_status import TaskStatus
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
    api_instance = dream3d.TasksApi(api_client)
    task_id = 'task_id_example' # str | 

    try:
        # Get
        api_response = await api_instance.get_api_v1_tasks_task_id_get(task_id)
        print("The response of TasksApi->get_api_v1_tasks_task_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_api_v1_tasks_task_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 

### Return type

[**TaskStatus**](TaskStatus.md)

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

