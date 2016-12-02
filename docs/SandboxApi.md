# idcheckio_python_client.SandboxApi

All URIs are relative to *https://localhost/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_image**](SandboxApi.md#get_image) | **GET** /v0/sandbox/image/{imageUid} | HTTP GET image
[**get_image_list**](SandboxApi.md#get_image_list) | **GET** /v0/sandbox/imagelist | HTTP GET images list
[**get_mrz**](SandboxApi.md#get_mrz) | **GET** /v0/sandbox/mrz/{mrzUid} | HTTP GET mrz
[**get_mrz_list**](SandboxApi.md#get_mrz_list) | **GET** /v0/sandbox/mrzlist | HTTP GET mrz list


# **get_image**
> list[str] get_image(image_uid, raw_type=raw_type, face=face, light=light)

HTTP GET image

GET image

### Example 
```python
import time
import idcheckio_python_client
from idcheckio_python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = idcheckio_python_client.SandboxApi()
image_uid = 'image_uid_example' # str | EnumDemoDocsImage
raw_type = 'raw_type_example' # str | Image raw type (optional)
face = 'face_example' # str | Image face (optional)
light = 'light_example' # str | Image light (optional)

try: 
    # HTTP GET image
    api_response = api_instance.get_image(image_uid, raw_type=raw_type, face=face, light=light)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SandboxApi->get_image: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_uid** | **str**| EnumDemoDocsImage | 
 **raw_type** | **str**| Image raw type | [optional] 
 **face** | **str**| Image face | [optional] 
 **light** | **str**| Image light | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_list**
> ImageListResponse get_image_list()

HTTP GET images list

GET images list

### Example 
```python
import time
import idcheckio_python_client
from idcheckio_python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = idcheckio_python_client.SandboxApi()

try: 
    # HTTP GET images list
    api_response = api_instance.get_image_list()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SandboxApi->get_image_list: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ImageListResponse**](ImageListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mrz**
> MrzResponse get_mrz(mrz_uid)

HTTP GET mrz

GET mrz

### Example 
```python
import time
import idcheckio_python_client
from idcheckio_python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = idcheckio_python_client.SandboxApi()
mrz_uid = 'mrz_uid_example' # str | EnumDemoDocsMrz

try: 
    # HTTP GET mrz
    api_response = api_instance.get_mrz(mrz_uid)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SandboxApi->get_mrz: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mrz_uid** | **str**| EnumDemoDocsMrz | 

### Return type

[**MrzResponse**](MrzResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mrz_list**
> MrzListResponse get_mrz_list()

HTTP GET mrz list

GET mrz list

### Example 
```python
import time
import idcheckio_python_client
from idcheckio_python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = idcheckio_python_client.SandboxApi()

try: 
    # HTTP GET mrz list
    api_response = api_instance.get_mrz_list()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SandboxApi->get_mrz_list: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MrzListResponse**](MrzListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

