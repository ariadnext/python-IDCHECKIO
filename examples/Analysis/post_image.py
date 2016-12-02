# coding: utf-8

from __future__ import absolute_import

import os
import sys
import unittest
import base64

import idcheckio_python_client
from pprint import pprint
from idcheckio_python_client.rest import ApiException
from idcheckio_python_client.apis.analysis_api import AnalysisApi
from idcheckio_python_client.api_client import ApiClient
from idcheckio_python_client.configuration import Configuration
from idcheckio_python_client.models.image_request import ImageRequest

class PostImage():

    def init(self):
        config = Configuration()
        config.username = "exemple@exemple.com"
        config.password = "exemple"
        api_client = ApiClient(host="http://api.idcheck.io/rest")
        self.api_analysis = AnalysisApi(api_client=api_client)


    def run(self):
        try:
            with open("/tmp/berthier_recto.jpg", "rb") as recto_file:
                if(sys.version_info[0] == 2):
                    encoded_recto = base64.b64encode(recto_file.read())
                if(sys.version_info[0] == 3):
                    encoded_recto = base64.b64encode(recto_file.read()).decode('ascii')
            image_resquest = ImageRequest(front_image=encoded_recto)
            result_response = self.api_analysis.post_image(image_resquest)
            pprint(result_response.mrz)
        except ApiException as e:
            print("Exception when calling AnalysisApi->post_image: {}".format(e))
