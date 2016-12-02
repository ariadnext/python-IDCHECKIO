# coding: utf-8

from __future__ import absolute_import

import os
import sys
import unittest

import idcheckio_python_client
from pprint import pprint
from idcheckio_python_client.rest import ApiException
from idcheckio_python_client.apis.analysis_api import AnalysisApi
from idcheckio_python_client.api_client import ApiClient
from idcheckio_python_client.configuration import Configuration
from idcheckio_python_client.models.mrz_request import MrzRequest

class PostMrz():

    def init(self):
        config = Configuration()
        config.username = "exemple@exemple.com"
        config.password = "exemple"
        api_client = ApiClient(host="http://api.idcheck.io/rest")
        self.api_analysis = AnalysisApi(api_client=api_client)


    def run(self):
        try:
            mrz_request = MrzRequest(line1="IDFRABERTHIER<<<<<<<<<<<<<<<<<<<<<<<", line2="9409923102854CORINNE<<<<<<<6512068F4")
            result_response = self.api_analysis.post_mrz(mrz_request)
            pprint(result_response.holder_detail)
        except ApiException as e:
            print("Exception when calling AnalysisApi->post_mrz: {}".format(e))
