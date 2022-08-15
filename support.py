from csv import reader
from os import walk
import pygame

def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter = ',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map

def import_player_folder(path, x, y):
    surface_list = []
    paths = []

    for _, __, img_files in walk(path):
        for image in img_files:
            if image[:2] == '.DS':
                continue
            full_path = path + '/' + image
            paths.append(full_path)
        
        paths.sort(key = lambda x: x[-6:-4] )
        for element in paths:
            if element[-5:] == 'Store':
                continue
            image_surf = pygame.transform.scale(pygame.image.load(element).convert(), (x, y))
            surface_list.append(image_surf)
    
    return surface_list

def import_folder(path):
    surface_list = []
    paths = []

    for _, __, img_files in walk(path):
        for image in img_files:
            if image[:2] == '.DS':
                continue
            full_path = path + '/' + image
            paths.append(full_path)
        
        paths.sort(key = lambda x: x[-6:-4] )
        for element in paths:
            if element[-5:] == 'Store':
                continue
            image_surf = pygame.image.load(element).convert()
            surface_list.append(image_surf)
    
    return surface_list