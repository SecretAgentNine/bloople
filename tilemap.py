import pygame
import re
from ast import literal_eval

class tilemap():
  def __init__(self, size):
    self.surface = pygame.Surface(size)

  def addlayer(self, mapfile):
    m = open(mapfile, 'r')
    mapstring = m.read()
    specs, mapstring = re.split(r'\*\*\*\n', mapstring)
    map_array = re.split(r'\n',mapstring)
    tileset = re.search(r"(?<=tileset\=).*(?=\n)", specs).group(0)
    tilesize = literal_eval(re.search(r'(?<=tilesize\=)\([0-9]+,[0-9]+\)', specs).group(0))

    self.tile_assignments = {}
    for i in re.findall(r'.:[0-9]+',specs):
      self.tile_assignments[i[0]] = int(i[2:len(i)])
    self.tiles = []

    image = pygame.image.load(tileset).convert_alpha()
    width, height = image.get_size()
    for y in range(0, height/tilesize[1]):
      for x in range(0, width/tilesize[0]):
        self.tiles.append(image.subsurface((x*tilesize[0],y*tilesize[1],tilesize[0],tilesize[1])))
    for y in range(0, len(map_array)-1):	#map_array winds up with a blank string at the end
      for x in range(0, len(map_array[0])):
        self.surface.blit(self.tiles[self.tile_assignments[map_array[y][x]]],(x*tilesize[0],y*tilesize[1]))

  def render(self, screen):
    screen.blit(self.surface,(0,0))
