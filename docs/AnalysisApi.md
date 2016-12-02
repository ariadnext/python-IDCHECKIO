# idcheckio_python_client.AnalysisApi

All URIs are relative to *https://localhost/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_report**](AnalysisApi.md#get_report) | **GET** /v0/pdfreport/{analysisRefUid} | HTTP GET report (demo)
[**get_result**](AnalysisApi.md#get_result) | **GET** /v0/result/{analysisRefUid} | HTTP GET result
[**get_task**](AnalysisApi.md#get_task) | **GET** /v0/task/{analysisRefUid} | HTTP GET task
[**post_image**](AnalysisApi.md#post_image) | **POST** /v0/task/image | HTTP POST task image
[**post_mrz**](AnalysisApi.md#post_mrz) | **POST** /v0/task/mrz | HTTP POST task mrz


# **get_report**
> ReportResponse get_report(analysis_ref_uid, accept_language=accept_language)

HTTP GET report (demo)

Get a pdf report (base64 encoded) (demo)

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
api_instance = idcheckio_python_client.AnalysisApi()
analysis_ref_uid = 'analysis_ref_uid_example' # str | Report analysisRefUid
accept_language = 'accept_language_example' # str | Accept language header (optional)

try: 
    # HTTP GET report (demo)
    api_response = api_instance.get_report(analysis_ref_uid, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalysisApi->get_report: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_ref_uid** | **str**| Report analysisRefUid | 
 **accept_language** | **str**| Accept language header | [optional] 

### Return type

[**ReportResponse**](ReportResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_result**
> ResultResponse get_result(analysis_ref_uid, accept_language=accept_language, recto_image_cropped=recto_image_cropped, face_image_cropped=face_image_cropped, signature_image_cropped=signature_image_cropped)

HTTP GET result

Get result controls

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
api_instance = idcheckio_python_client.AnalysisApi()
analysis_ref_uid = 'analysis_ref_uid_example' # str | Result analysisRefUid
accept_language = 'accept_language_example' # str | Accept language header (optional)
recto_image_cropped = false # bool | True to obtain recto image cropped if applicable (optional) (default to false)
face_image_cropped = false # bool | True to obtain face image cropped if applicable (optional) (default to false)
signature_image_cropped = false # bool | True to obtain signature image cropped if applicable (optional) (default to false)

try: 
    # HTTP GET result
    api_response = api_instance.get_result(analysis_ref_uid, accept_language=accept_language, recto_image_cropped=recto_image_cropped, face_image_cropped=face_image_cropped, signature_image_cropped=signature_image_cropped)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalysisApi->get_result: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_ref_uid** | **str**| Result analysisRefUid | 
 **accept_language** | **str**| Accept language header | [optional] 
 **recto_image_cropped** | **bool**| True to obtain recto image cropped if applicable | [optional] [default to false]
 **face_image_cropped** | **bool**| True to obtain face image cropped if applicable | [optional] [default to false]
 **signature_image_cropped** | **bool**| True to obtain signature image cropped if applicable | [optional] [default to false]

### Return type

[**ResultResponse**](ResultResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task**
> TaskResponse get_task(analysis_ref_uid, accept_language=accept_language, wait=wait)

HTTP GET task

Get task status

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
api_instance = idcheckio_python_client.AnalysisApi()
analysis_ref_uid = 'analysis_ref_uid_example' # str | Task analysisRefUid
accept_language = 'accept_language_example' # str | Accept language header (optional)
wait = 789 # int | specify a maximum wait time in milliseconds (optional)

try: 
    # HTTP GET task
    api_response = api_instance.get_task(analysis_ref_uid, accept_language=accept_language, wait=wait)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalysisApi->get_task: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_ref_uid** | **str**| Task analysisRefUid | 
 **accept_language** | **str**| Accept language header | [optional] 
 **wait** | **int**| specify a maximum wait time in milliseconds | [optional] 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_image**
> ResultResponse post_image(body, async_mode=async_mode, accept_language=accept_language)

HTTP POST task image

POST an image check task

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
api_instance = idcheckio_python_client.AnalysisApi()
body = idcheckio_python_client.ImageRequest() # ImageRequest | Image request
async_mode = true # bool | true to activate asynchrone mode (optional)
accept_language = 'accept_language_example' # str | Accept language header (optional)

try: 
    # HTTP POST task image
    api_response = api_instance.post_image(body, async_mode=async_mode, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalysisApi->post_image: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImageRequest**](ImageRequest.md)| Image request | 
 **async_mode** | **bool**| true to activate asynchrone mode | [optional] 
 **accept_language** | **str**| Accept language header | [optional] 

### Return type

[**ResultResponse**](ResultResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_mrz**
> ResultResponse post_mrz(body, async_mode=async_mode, accept_language=accept_language)

HTTP POST task mrz

POST a mrz check task

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
api_instance = idcheckio_python_client.AnalysisApi()
body = idcheckio_python_client.MrzRequest() # MrzRequest | Mrz request
async_mode = true # bool | true to activate asynchrone mode (optional)
accept_language = 'accept_language_example' # str | Accept language header (optional)

try: 
    # HTTP POST task mrz
    api_response = api_instance.post_mrz(body, async_mode=async_mode, accept_language=accept_language)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AnalysisApi->post_mrz: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MrzRequest**](MrzRequest.md)| Mrz request | 
 **async_mode** | **bool**| true to activate asynchrone mode | [optional] 
 **accept_language** | **str**| Accept language header | [optional] 

### Return type

[**ResultResponse**](ResultResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

