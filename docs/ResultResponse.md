# ResultResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | uid | 
**analysis_ref_uid** | **str** | analysisRefUid | 
**check_report_summary** | [**CheckSummaryOfTheSubmittedDocument**](CheckSummaryOfTheSubmittedDocument.md) |  | 
**document_classification** | [**ClassificationOfTheSubmittedDocument**](ClassificationOfTheSubmittedDocument.md) |  | 
**document_detail** | [**DetailedInformationOfTheSubmittedDocument**](DetailedInformationOfTheSubmittedDocument.md) |  | 
**holder_detail** | [**DetailedInformationOfTheHolderOfTheSubmittedDocument**](DetailedInformationOfTheHolderOfTheSubmittedDocument.md) |  | 
**mrz** | [**Mrz**](Mrz.md) |  | 
**controls** | [**list[ControlGroup]**](ControlGroup.md) | Performed controls on the submitted document | 
**image** | [**list[ExtractedImage]**](ExtractedImage.md) | Cropped image of the submitted document according request | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


