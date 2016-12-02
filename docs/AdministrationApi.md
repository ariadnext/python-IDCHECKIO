# idcheckio_python_client.AdministrationApi

All URIs are relative to *https://localhost/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_health**](AdministrationApi.md#get_health) | **GET** /v0/admin/health | HTTP GET health
[**get_user**](AdministrationApi.md#get_user) | **GET** /v0/admin/user | HTTP GET user


# **get_health**
> HealthResponse get_health()

HTTP GET health

GET server health (OK 200)

### Example 
```python
import time
import idcheckio_python_client
from idcheckio_python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = idcheckio_python_client.AdministrationApi()

try: 
    # HTTP GET health
    api_response = api_instance.get_health()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AdministrationApi->get_health: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HealthResponse**](HealthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserResponse get_user(accept_language=accept_language)

HTTP GET user

Get user informations

### Example 
```python
import time
import idcheckio_python_client
from idcheckio_python_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
idcheckio_python_client.configuration.username = 'YOUR_USERNAME'
idcheckio_python_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = idcheckio_python_client.AdministrationApi()
accept_language = 'accept_language_example' # str | Accept language header (optional)

try: 
    # HTTP GET user
    api_response = api_instance.get_user(accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AdministrationApi->get_user: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_language** | **str**| Accept language header | [optional] 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

