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
    def post(self, end_point, json_obj=None, params=None, headers=None):
        """
        Purpose: Makes POST REST call and returns API response
         :end_point: Endpoint in the request
         :json_obj: JSON payload
         :params: Path parameters
         :headers: Any headers to make GET request
         :return: Dictionary object having response json and status code of the POST request
        """

        request_url = self.base_uri + self.base_path + end_point
        resp = requests.post(request_url, params=params,json=json_obj,verify=False)
        result = {
                "response_body": resp.json(),
                "status_code": resp.status_code,
                "headers":resp.headers
                  }
        logger.debug("The response of POST api {}".format(result))
        return result

    @exec_log
    def get(self, end_point, params=None,headers=None):
        """
        Purpose: Makes GET REST call based on the input arguments and returns API response
          :request_url: endpoint in request
          :params: Path parameters
          :headers: headers in request
          :return:Dictionary object having response json and status code of the request
        """
        request_url = self.base_uri + self.base_path + end_point
        resp = requests.get(request_url, params=params, headers=None, verify=False)
        result = {
                "response_body": resp.json(),
                "status_code": resp.status_code,
                "headers":resp.headers
                }
        logger.debug("The response of GET api {}".format(result))
        return result

    @exec_log
    def put(self, end_point, json_obj, headers=None):
        """
        Purpose: Makes PUT REST call based on the input arguments and returns API response
           :end_point: Endpoint in the request
           :param : Path parameters
           :headers: Any headers to make get request
           :return:Dictionary object having response json and status code of the GET request
         """
        request_url = self.base_uri + self.base_path + end_point
        resp = requests.put(request_url, data=json.dumps(json_obj), headers=headers, verify=False)
        result = {
                "response_body": resp.json(),
                "status_code": resp.status_code,
                "headers":resp.headers
                }
        logger.debug("The response of PUT api {}".format(result))
        return result

    @exec_log
    def delete(self, end_point, headers=None):
        """
            Purpose: Makes DELETE REST call based on the input arguments and returns API response
            :request_url: Endpoint in the request
            :headers: Any headers to make get request
            :return:dictionary having response json and status code of the GET request
          """
        request_url = self.base_uri + self.base_path + end_point
        resp = requests.delete(request_url, headers=headers, verify=False)
        result = {
                "status_code": resp.status_code,
                "headers":resp.headers
                }
        logger.debug("The response of DELETE api {}".format(result))
        return result

