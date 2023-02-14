#! /usr/bin/env python3
"""
Request Module Wrapper class
"""
import json
import requests
from requests.auth import HTTPBasicAuth

class BaseInterface:
    '''
    BaseInterface: Provides a wrapper around the requests interface, storing the target
    server address and credentials so that they do not have to be passed in each call.
    '''
    def __init__(self, server_addr, user_name, access_key) -> None:
        self.m_creds = HTTPBasicAuth(user_name, access_key)
        self.m_server_addr = server_addr

    def __request(self,
                  query_method,
                  query_url,
                  payload = None,
                  in_file_name = None,
                  out_file_name = None):
        error = {}
        result = {}
        if in_file_name is None and out_file_name is None:
            response = requests.request(method= query_method,
                                    url= query_url,
                                    auth= self.m_creds,
                                    data = payload,
                                    stream= True,
                                    timeout=  None)
            if response.status_code >= 300:
                error["status_code"] = response.status_code
            else:
                result = json.loads(response.content)
        else:
            if in_file_name is not None:
                pass
            else:
                pass

        return result, error


    def _get(self, query_url, payload = None, file_name = None):
        return self.__request(query_method= "GET",
                              query_url= query_url,
                              payload= payload,
                              in_file_name= file_name)

    def _post(self, query_url, payload = None, file_name = None):
        return self.__request(query_method= "POST",
                              query_url= query_url,
                              payload= payload,
                              out_file_name= file_name)

    def _push(self, query_url, payload = None, file_name = None):
        return self.__request(query_method= "PUSH",
                              query_url= query_url,
                              payload= payload,
                              out_file_name= file_name)

    def _delete(self, query_url, payload = None):
        return self.__request(query_method= "DELETE",
                              query_url= query_url,
                              payload= payload)

    def _patch(self, query_url, payload = None):
        return self.__request(query_method= "PATCH",
                              query_url= query_url,
                              payload= payload)

    def _head(self, query_url, payload = None):
        return self.__request(query_method= "HEAD",
                              query_url= query_url,
                              payload= payload)

    def _options(self, query_url, payload = None):
        return self.__request(query_method= "OPTIONS",
                              query_url= query_url,
                              payload= payload)


if __name__ == '__main__':
    pass
