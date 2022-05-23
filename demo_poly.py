#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 19:58:58 2021

@author:  Malika
"""


import requests

def prediction(y):
    
    
    x = list(range(len(y)))
    
    predict = 'last+1'
    print(y[-1])
    degrees = list(range(17))
    print(degrees)
    subsets = 100
    sampling_param = 2
    params = {"degrees": degrees, "predict": predict, "x": x, "subsets": subsets, "sampling_param": sampling_param, "y": y}
   
  
    rest_url= 'https://chariot-maria.space/api/v1.0/validating_pol'
    headers = {}
    headers["Content-Type"] = "application/json; charset=UTF-8"
    headers["Accept"] = "application/json; charset=UTF-8"
    
    rest_response = requests.request("POST", rest_url, headers=headers, json=params)
    return rest_response.json()

y = [1,2,3,4,5]

print(prediction(y))
