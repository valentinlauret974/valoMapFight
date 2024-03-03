# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 16:19:26 2024

@author: valen
"""
import requests 
#languages supported -> en-US OR fr-FR
#link to genrate key : https://developer.riotgames.com/

key = "RGAPI-2a4bb28c-f658-4bf1-bf09-ef17f343b7c5"

def get_PUUID(tagLine,gameName):
    request_url = "https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/"+gameName+"/"+tagLine+"?api_key="+key
    return request_url


    

req = requests.get(get_PUUID("EUW","MKfive974"))
player_info = req.json()

x= requests.get("https://valorant-api.com/v1/maps/7eaecc1b-4337-bbf6-6ab9-04b8f06b3319")
print(x.json())
