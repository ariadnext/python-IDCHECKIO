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

class GetReport():

    def init(self):
        config = Configuration()
        config.username = "exemple@exemple.com"
        config.password = "exemple"
        api_client = ApiClient(host="http://api.idcheck.io/rest")
        self.api_analysis = AnalysisApi(api_client=api_client)


    def run(self, uid):
        try:
            report_response = self.api_analysis.get_report(uid)
            pprint(report_response)
        except ApiException as e:
            print("Exception when calling AnalysisApi->get_report: {}".format(e))
        try:
            report = report_response.report
            with open("/tmp/report.pdf", "wb") as report_file:
                if(sys.version_info[0] == 2):
                    report_file.write(report.decode())
                if(sys.version_info[0] == 3):
                    report_file.write(base64.b64decode(report))
        except IOError:
            print("Unable to write pdf report")
