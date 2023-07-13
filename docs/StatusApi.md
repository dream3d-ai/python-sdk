# dream3d.StatusApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_status_get**](StatusApi.md#get_status_get) | **GET** / | Get Status


# **get_status_get**
> Msg get_status_get()

Get Status

### Example

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


# Enter a context with an instance of the API client
async with dream3d.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dream3d.StatusApi(api_client)

    try:
        # Get Status
        api_response = await api_instance.get_status_get()
        print("The response of StatusApi->get_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusApi->get_status_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Msg**](Msg.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

