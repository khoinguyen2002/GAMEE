import game_object
import pygame
from addict import Dict
import json
def genarate_map(json_file_url):
    text = open(json_file_url,'r').read()
    map_dict = json.loads(text)
    map = Dict(map_dict)
    data = map['layer'][0]['data'      ]
    width = map_dict['width']
    height = map_dict['height']



if __name__== '__main__':
    genarate_map()
