import requests
import json
import urllib3

from conf.RelayrApiConstants import API_CONSTANTS
from libs.common.ExecTime import exec_log
from libs.common.Logger import logger

@exec_log
class ApiHelper:
    """ Core Utils for making REST calls - Allows to perform CRUD operation """
    def __init__(self, base_uri=API_CONSTANTS['URL'], base_path=API_CONSTANTS['BASE_PATH']):
        urllib3.disable_warnings()
        self.base_uri = base_uri
        self.base_path = base_path

    @exec_log
    def post(self, request_url, json_obj=None, params=None, headers=None):
        """
        Purpose: Makes POST REST call and returns API response
         :request_url: resource in endpoint
         :json_obj: json payload
         :params: Path parameters
         :headers: Any headers to make GET request
         :return: dictionary having response json and status code of the POST request
        """

        request_url = self.base_uri + self.base_path + request_url
        resp = requests.post(request_url, params=params,json=json_obj,verify=False)
        result = {
                "response_body": resp.json(),
                "status_code": resp.status_code,
                "headers":resp.headers
                  }
        logger.debug("The response of POST api {}".format(result))
        return result

    @exec_log
    def get(self, request_url, params=None,headers=None):
        """
        Purpose: Makes GET REST call based on the input arguments and returns API response
          :request_url: resource in endpoint
          :params: Path parameters
          :headers: headers in request
          :return:dictionary having response json and status code of the request
        """
        request_url = self.base_uri + self.base_path + request_url
        resp = requests.get(request_url, params=params, headers=None, verify=False)
        result = {
                "response_body": resp.json(),
                "status_code": resp.status_code,
                "headers":resp.headers
                }
        logger.debug("The response of GET api {}".format(result))
        return result

    @exec_log
    def put(self, request_url, json_obj, headers=None):
        """
        Purpose: Makes PUT REST call based on the input arguments and returns API response
           :request_url: This is the resource endpoint
           :param : Path parameters
           :headers: Any headers to make get request
           :return:dictionary having response json and status code of the GET request
         """
        request_url = self.base_uri + self.base_path + request_url
        resp = requests.put(request_url, data=json.dumps(json_obj), headers=headers, verify=False)
        result = {
                "response_body": resp.json(),
                "status_code": resp.status_code,
                "headers":resp.headers
                }
        logger.debug("The response of PUT api {}".format(result))
        return result

    @exec_log
    def delete(self, request_url, headers=None):
        """
            Purpose: Makes DELETE REST call based on the input arguments and returns API response
            :request_url: This is the resource endpoint
            :params: Path parameters
            :headers: Any headers to make get request
            :return:dictionary having response json and status code of the GET request
          """
        request_url = self.base_uri + self.base_path + request_url
        resp = requests.delete(request_url, headers=headers, verify=False)
        result = {
                "status_code": resp.status_code,
                "headers":resp.headers
                }
        logger.debug("The response of DELETE api {}".format(result))
        return result

