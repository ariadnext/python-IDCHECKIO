#!/usr/bin/python2.7

import sys
import base64
import json
import requests


def b64_encode(data):
    """Adapt base64 encoding for an compatible code between python 2 and 3.

    Arguments:
        data (): data to encode.
    """

    if(sys.version_info[0] == 2 or isinstance(data, bytes)):
        return base64.b64encode(data) 
    else:
        return base64.b64encode(data.encode()).decode()

def b64_decode(data):
     """Adapt base64 decoding for an compatible code between python 2 and 3.

     Arguments:
         data (): data to decode.
     """

     if(isinstance(data, bytes)):
         return data.decode()
     else:
         return base64.b64decode(data)

def schemeCompliant(dic, scheme):
    """Return a dict without keys who aren't in a scheme.
    Arguments:
        dic (dict): Dictionnary to transform.
        scheme (dict): Dictionnary scheme.
    """
    result = {}
    if(sys.version_info[0] == 2):
        for key,value in dic.iteritems():
            if isinstance(value, str) or isinstance(value, int) or isinstance(
                    value, unicode):
                if scheme.has_key(key):
                    result[key] = value
            elif isinstance(value, dict):
                if scheme.has_key(key):
                    result[key] = schemeCompliant(value, scheme[key])
            elif isinstance(value, list):
                if scheme.has_key(key):
                    result[key] = value
    else:
        for key,value in dic.items():
            if isinstance(value, str) or isinstance(value, int):
                if key in scheme:
                    result[key] = value
            elif isinstance(value, dict):
                if key in scheme:
                    result[key] = schemeCompliant(value, scheme[key])
            elif isinstance(value, list):
                if key in scheme:
                    result[key] = value
    return result

class ResponseIDCIO:
    """Class describe a IDCheckIO response.

    This class return a status of the response, the current uid of the
    demand and the response's content in JSON format.

    ResponseIDCIO object is just return by IDCheckIO, it is not necessary
    to create this.

    Attributes:
        status (int): The http's code of the current request.
        uid (int): The uid code reference the current request.
        body (dict): The response's content in JSON format.

    Note;
        The uid can be retrieve in the body element (body['uid']).
    """
    
    def __init__(self, status, uid, body):
        """Initiation function to create a ResponseIDCIO object.

        Create a ResponseIDCIO describe by a status of the response, the
        current uid of the demand and the response's content in JSON format.

        Arguments:
            status (int): The http's code of the current request.
            uid (int): The uid code reference the current request.
            body (dict): The response's content in JSON format.
        """

        defaultScheme = { 'analysisRefUid': '',
                      'uid': '',
                      'mrz': {
                          'line2': '',
                          'line1': ''},
                      'holderDetail': {
                          'birthPlace': '',
                          'firstName': [''],
                          'lastName': [''],
                          'address': '',
                          'birthDate': {
                              'year': '',
                              'day': '',
                              'month': ''},
                          'gender': '',
                          'nationality': ''},
                      'documentDetail': {
                          'emitCountry': '',
                          'extraInfos': [{
                              'dataKey': '',
                              'dataValue': '',
                              'title': ''}],
                          'documentNumber': '',
                          'emitDate': {
                              'year': '',
                              'month': '',
                              'day': ''},
                          'expirationDate': {
                              'year': '',
                              'month': '',
                              'day': ''}},
                      'checkReportSummary': {
                          'check': [{
                              'titleMsg': '',
                              'identifier': '',
                              'result': '',
                              'resultMsg': ''}]},
                      'documentClassification': {
                          'idType': ''},
                      'report': '',
                      'accepted': '',
                      'started': '',
                      'ended': '',
                      'redirectUrl': ''} # Specific get_report
        self._status = status
        self._uid = uid
        self._body = schemeCompliant(body, defaultScheme)


    def _get_status(self):
        """Get the status of the ResponseIDCIO.
        """

        return self._status
    status = property(_get_status)


    def _get_uid(self):
        """Get the uid of the ResponseIDCIO.
        """

        return self._uid
    uid = property(_get_uid)


    def _get_body(self):
        """Get the body of the ResponseIDCIO, in JSON format.
        """

        return self._body
    body = property(_get_body)


class IDCheckIO:
    """Class to use the API IDCheckIO.

    This class create a connection to the API IDCheckIO, with an user's login
    and password.

    On this connection, it is possible to execute analysis, status and report
    functions.

    Attributes:
        user (str): The user's login, create on the website idcheck.io.
        pwd (str): The password associate to the user's login.
        language (optional[str]): The language use for the responses. Only
            'fr' or 'en' supported. Default is 'en'.
        host (optional[str]): The server to use (IP or FQDN). Do not modify
            on the idcheck.io server. Default is 'idcheck.io'.
        protocol (optional[str]): The procotol to use for the connection. Do
            not modify on the idcheck.io server. Default is 'https'.
        port (optional[str]): The port to use for the connection. Do not
            modify on the idcheck.io server. Default is '443'.
        verify (optional[bool]): If verify the SSL certificate of the server.
            Do not modify on the idcheck.io server. Default is 'True'.
    
    Note:
        It is juste necessary to use the user and pwd attributes. For initiate
        a connection : conn = idcheckio.IDCheckIO("user@login.com","password")
    """


    def __init__(self, user, pwd, language="en", host="api.idcheck.io",
                 protocol="https", port="443", verify=True):
        """Initialisation function to create the connection on the idcheck.io
        server.

        Create a connection objet, necessary to use the API.

        Arguments:
            user (str): The user's login, create on the website idcheck.io.
            pwd (str): The password associate to the user's login.
            language (optional[str]): The language use for the responses. Only
                'fr' or 'en' supported. Default is 'en'.
            host (optional[str]): The server to use (IP or FQDN). Do not modify
                on the idcheck.io server. Default is 'idcheck.io'.
            protocol (optional[str]): The procotol to use for the connection. Do
                not modify on the idcheck.io server. Default is 'https'.
            port (optional[str]): The port to use for the connection. Do not
                modify on the idcheck.io server. Default is '443'.
            verify (optional[bool]): If verify the SSL certificate of the server.
                Do not modify on the idcheck.io server. Default is 'True'.
        """

        self.user = user
        self.pwd = pwd
        self.host = host
        self.protocol = protocol
        self.port = port
        self.verify = verify
        self.language = language
        self.url = protocol + "://" + host + ":" + port
        concat = user + ":" + pwd
        auth = b64_encode(concat)
        self.headers = {'Content-Type': 'application/json',
                        'Authorization': "Basic " + auth,
                        'Accept-Language': language}


    def analyse_mrz(self, line1, line2="", line3="", async=False):
        """Analyse a MRZ (Machine Readable Zone) from an identity card.

        Return a ResponseIDCIO with the status (http code), the uid of the
        request and the body with the server response in JSON format.

        Note:
            Return the value "-1" for status and the value "0" for uid if
            the server is unreachable.

        In synchronous mode, the server response contains a control report
        about the MRZ sent.

        In asynchronous mode, the server returns directly the uid,
        necessary to get the status of the demand. This mode don't have an
        interest with a MRZ.

        Arguments:
            line1 (str): The first line of a MRZ.
            line2 (optional[str]): The second line of a MRZ.
            line3 (optional[str]): The third line of a MRZ.
            async (optional[bool]): If use the asynchronous mode. Default is
                'False'.
        """

        methode = "/rest/v0/task/mrz"
        arguments = "?asyncMode=" + str(async)

        data = {'line1': line1, 'line2': line2, 'line3': line3}
        url = self.url + methode + arguments

        try:
            response = requests.post(url, data=json.dumps(data), headers=self.headers,
                                 verify=self.verify)
            result = ResponseIDCIO(response.status_code, response.json()["uid"],
                                   response.json())
        except requests.exceptions.ConnectionError:
            result = ResponseIDCIO(-1, 0,
                                   {"errorMessage": "Error: Unable to acess server"})
        except KeyError:
            result = ResponseIDCIO(response.status_code, 0, response.json())

        return result


    def analyse_image(self, recto, verso="", async=False, path=False):
        """Analyse an identity card from image (recto and verso).

        Return a ResponseIDCIO with the status (http code), the uid of the request
        and the body with the server response in JSON format.

        Note:
            Return the value "-1" for status and the value "0" for uid if
            the server is unreachable.

        In synchronous mode, the server response contains a control report
        about the MRZ sent.

        In asynchronous mode, the server returns directly the uid,
        necessary to get the status of the demand.

        Arguments:
            recto (str): The image of the identity card with the MRZ encodes in 
                base64.
            verso (optional[str]): The other side of the identity card encodes in
                base64.
            async (optional[bool]): If use the asynchronous mode. Default is
                'False'.
            path (optional[bool]): If use path to get a file on the FS in place of
                an image in base64. Default is 'False'.
        """

        methode = "/rest/v0/task/image"
        arguments = "?asyncMode=" + str(async)

        url = self.url + methode + arguments

        if path:
            try:
                with open(recto, "rb") as recto_file:
                    encoded_recto = b64_encode(recto_file.read())
            except IOError:
                print("Error: access recto file : {}".format(recto))
                return ResponseIDCIO(-1, 0,
                                     {"errorMessage": "Error: access recto file"})
 
            if verso:
                try:
                    with open(verso, "rb") as verso_file: 
                        encoded_verso = b64_encode(verso_file.read())
                except IOError:
                    print("Warn: access verso file : {}".format(verso))
                    encoded_verso = ""
            else:
                encoded_verso = ""
        else:
            encoded_recto = recto
            encoded_verso = verso

        data = {'frontImage': b64_decode(encoded_recto)}
        if encoded_verso:
            data['backImage'] = b64_decode(encoded_verso)
        else:
            data['backImage'] = ""

        try:
            print("{}".format(json.dumps(data)))
            response = requests.post(url, data=json.dumps(data), headers=self.headers,
                                 verify=self.verify)
            result = ResponseIDCIO(response.status_code, response.json()["uid"],
                                   response.json())
        except requests.exceptions.ConnectionError:
            result = ResponseIDCIO(-1, 0, 
                                   {"errorMessage": "Error: Unable to acess server"})
        except KeyError:
            result = ResponseIDCIO(response.status_code, 0, response.json())

        return result


    def get_result(self, uid, rectoImageCropped=False, faceImageCropped=False,
                  signatureImageCropped=False):
        """Get a detail result of an analysis.

        Return a ResponseIDCIO with the status (http code), the uid of the request
        and the body with the server response in JSON format.

        Note:
            This function must be called only on an analysis finished by the server
            (asynchronous mode).
            Return the value "-1" for status and the value "0" for uid if
            the server is unreachable.

        Arguments:
            uid (str): The uid of the request, retrieved on the response of an
                analysis demand.
            rectoImageCropped (optional[bool]): If get the cropped image (in base64)
                from recto into the response. Default is 'False'.
            faceImageCropped (optional[bool]): If get the cropped face (in base64)
                from recto or verso (depend on the identity card) into the response.
                Default is 'False'.
            signatureImageCropped (optional[bool]): If get the cropped signature (in
                base64) from recto or verso (depend on the identity card) into the
                response. Default is 'False'.
        """

        methode = "/rest/v0/result/"
        arguments = "?rectoImageCropped=" + str(rectoImageCropped) + \
               "&faceImageCropped=" + str(faceImageCropped) + \
               "&signatureImageCropped=" + str(signatureImageCropped)

        url = self.url + methode + str(uid) + arguments

        try:
            response = requests.get(url, headers=self.headers, verify=self.verify)
            result = ResponseIDCIO(response.status_code, response.json()["uid"],
                                   response.json())
        except requests.exceptions.ConnectionError:
            result = ResponseIDCIO(-1, 0, 
                                   {"errorMessage": "Error: Unable to acess server"})
        except KeyError:
            result = ResponseIDCIO(response.status_code, 0, response.json())

        return result


    def get_report(self, uid, path=""):
        """Get a report in PDF format with a detail result of an analysis.

        Return a ResponseIDCIO with the status (http code), the uid of the request
        and the body with the server response in JSON format.

        Note:
            Return the value "-1" for status and the value "0" for uid if
            the server is unreachable.

        The PDF report is encoded in base64, retrievable in the field "report".

        Note:
            This function must be called only on an analysis finished by the server
            (asynchronous mode).

        Arguments:
            uid (str): The uid of the request, retrieved on the response of an
                analysis demand.
            path (optional[str]): The path on the FS where write the PDF report.
                Be careful with the access rights.
        """

        methode = "/rest/v0/pdfreport/"
        arguments = ""

        url = self.url + methode + str(uid) + arguments

        try:
            response = requests.get(url, headers=self.headers, verify=self.verify)
            result = ResponseIDCIO(response.status_code, response.json()["uid"],
                                   response.json())
            if path:
                report = response.json()["report"]
                with open(path, "wb") as report_file:
                    report_file.write(b64_decode(report))
        except KeyError:
            result = ResponseIDCIO(response.status_code, uid,
                                   {"errorMessage": "No report available"})
        except  requests.exceptions.ConnectionError:
            result = ResponseIDCIO(-1, 0, 
                                   {"errorMessage": "Error: Unable to acess server"})
        except IOError:
            print("Warn: writin file to {}".format(path))

        return result


    def get_status(self, uid, wait=0):
        """Get the current status of an analysis (useful in asynchronous mode).

        Return a ResponseIDCIO with the status (http code), the uid of the request
        and the body with the server response in JSON format.

        Note:
            Return the value "-1" for status and the value "0" for uid if
            the server is unreachable.

        Arguments:
            uid (str): The uid of the request, retrieved on the response of an
                analysis demand.
            wait (optional[int]): Specify the maximum wait time (in ms) to wait for
                task completion before returning.

        Note:
            The wait parameter can be used to reduce the number of time that the user
            will have to poll the server before detecting task completion.
        """

        methode = "/rest/v0/task/"
        arguments = "?wait=" + str(wait)

        url = self.url + methode + str(uid) + arguments

        try:
            response = requests.get(url, headers=self.headers, verify=self.verify,
                                    allow_redirects=False)
            try:
                end = response.json()["ended"]
                result = ResponseIDCIO(response.status_code, response.json()["uid"],
                                       {"result": "OK"})
            except KeyError:
                try:
                    result = ResponseIDCIO(response.status_code, response.json()["uid"],
                                           {"result": "Waiting"})
                except KeyError:
                    result = ResponseIDCIO(response.status_code, uid,
                                           {"errorMessage": "Error with the image"})
        except  requests.exceptions.ConnectionError:
            result = ResponseIDCIO(-1, 0, 
                                   {"errorMessage": "Error: Unable to acess server"})

        return result
