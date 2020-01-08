# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 19:24:13 2020

@author: Raz
"""

import requests

from logging import getLogger

logger = getLogger(__name__)

class BittrexRequestError(Exception):
    """Unknown error API Bittrex
    """
class BittrexError(Exception):
    """Error, uncorrected request
    """
class BittrexClient(object):
    
    def __init__(self):
        self.base_url = "https://api.bittrex.com/api/v1.1"
        
    def __request(self, method, params):
        url = self.base_url + method
        try:
           r = requests.get(url = url, params=params)
           result = r.json()
        except Exception:
            logger.exception("Bitrex error")
            raise BittrexError
        
        if result.get("success"):
            return result
        else: 
           logger.error("Requests error: %s", result.get("message"))
           raise BittrexRequestError
        """r = requests.get(url = url, params=params)
        #r = requests.get(url = "https://api.bittrex.com/api/v1.1/public/getticker", params =  params)
        result = r.json()
        print(result)
        if result.get("success"):
           return result
        else: 
           print("Error")"""
         
        
        
    def get_ticker(self, pair):
        params = {
                "market": pair
                }
        return self.__request(method = "/public/getticker", params = params)
    
    def get_last_price(self, pair):
        res = self.get_ticker(pair = pair)
        return res["result"]["Last"]
            