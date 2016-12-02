# ImageRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | API version (for backward compatibility purpose) | [optional] 
**front_image** | **str** | frontImage containing front daylight image of the identity document (base64 encoded, no wrap, jpg/png/tiff/pdf format) | 
**front_image_ir** | **str** | frontImage containing front infrared image of the identity document (base64 encoded, no wrap, jpg/png/tiff/pdf format) | 
**front_image_uv** | **str** | frontImage containing front ultraviolet image of the identity document (base64 encoded, no wrap, jpg/png/tiff/pdf format) | 
**back_image** | **str** | backImage containing daylight back image of the identity document (base64 encoded, no wrap, jpg/png/tiff/pdf format) | [optional] 
**back_image_ir** | **str** | backImage containing infrared back image of the identity document (base64 encoded, no wrap, jpg/png/tiff/pdf format) | [optional] 
**back_image_uv** | **str** | backImage containing ultraviolet back image of the identity document (base64 encoded, no wrap, jpg/png/tiff/pdf format) | [optional] 
**recto_image_cropped** | **bool** | rectoImageCropped true to obtain recto image cropped if applicable | [optional] [default to False]
**face_image_cropped** | **bool** | faceImageCropped true to obtain recto image cropped if applicable | [optional] [default to False]
**signature_image_cropped** | **bool** | signatureImageCropped true to obtain recto image cropped if applicable | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


