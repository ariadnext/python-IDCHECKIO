# coding: utf-8

from __future__ import absolute_import

import os
import sys
import unittest

import idcheckio_python_client
from pprint import pprint
from idcheckio_python_client.rest import ApiException
from idcheckio_python_client.apis.administration_api import AdministrationApi
from idcheckio_python_client.api_client import ApiClient
from idcheckio_python_client.configuration import Configuration

class GetUser():

    def init(self):
        config = Configuration()
        config.username = "exemple@exemple.com"
        config.password = "exemple"
        api_client = ApiClient(host="https://api.idcheck.io/rest")
        self.api_admin = AdministrationApi(api_client=api_client)

    def run(self):
        try:
            response = self.api_admin.get_user()
            pprint(response)
        except ApiException as e:
            print("Exception when calling AdministrationApi->get_user: {}".format(e))
