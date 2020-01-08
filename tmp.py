# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 19:39:59 2020

@author: Raz
"""

from bittrex import BittrexError
from bittrex import BittrexClient

NOTIFY_PAIR = "USD-BTC"

def main():
   client = BittrexClient()
   try:
       current_price = client.get_last_price(NOTIFY_PAIR)
       message = "{} = {}".format(NOTIFY_PAIR, current_price)
   except BittrexError:
       message = "Error"
       
   print(message)
   
   
if __name__ == "__main__":
    main()