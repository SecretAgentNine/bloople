import pygame
import player
import objects
import tilemap

class room():
  def __init__(self, mapsize, mapfiles, pos, player, objects):
    self.tilemap = tilemap.tilemap(mapsize)
    for mapfile in mapfiles:
      self.tilemap.addlayer(mapfile)
    self.surface = pygame.Surface(self.tilemap.surface.get_size())
    self.pos = pos
    self.player = player
    self.objects = objects
    self.renderlist = []
    for i in objects:
      self.renderlist.append(i)
    self.renderlist.append(self.player)

  def handle_keydown(self, key):
    if key==pygame.K_UP or key==pygame.K_DOWN or key==pygame.K_LEFT or key==pygame.K_RIGHT:
      self.player.move(key)

  def handle_keyup(self, key):
    if key==pygame.K_UP or key==pygame.K_DOWN or key==pygame.K_LEFT or key==pygame.K_RIGHT:
      self.player.stop(key)

  def update(self):
    self.renderlist = sorted(self.renderlist, key = lambda i: i.pos[1]+i.size[1])
    for i in self.objects:
      i.update(self.objects)
    self.player.update(self.objects)

  def render(self, screen, debug):
    self.surface.fill((255,255,255))
    self.tilemap.render(self.surface)
    for i in self.renderlist:
      i.render(self.surface, debug)
    screen.blit(self.surface, self.pos)
