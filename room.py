import pygame
import player
import objects
import tilemap

class room():
  def __init__(self, mapsize, mapfiles, pos, player, controls, objects):
    self.tilemap = tilemap.tilemap(mapsize)
    for mapfile in mapfiles:
      self.tilemap.addlayer(mapfile)
    self.surface = pygame.Surface(self.tilemap.surface.get_size())
    self.pos = pos
    self.player = player
    self.controls = controls
    self.objects = objects
    self.renderlist = []
    for i in objects:
      self.renderlist.append(i)
    self.renderlist.append(self.player)
    self.radius = 100

  def handle_keydown(self, key):
    if self.controls['up'] or self.controls['down'] or self.controls['left'] or self.controls['right']:
      self.player.move(key, self.controls)

  def handle_keyup(self, key):
    if key==pygame.K_UP or key==pygame.K_DOWN or key==pygame.K_LEFT or key==pygame.K_RIGHT:
      self.player.stop(key,self.controls)

  def update(self, screen):
    self.renderlist = sorted(self.renderlist, key = lambda i: i.pos[1]+i.size[1])
    for i in self.objects:
      i.update(self.objects)
    self.player.update(self.objects)
    if (self.player.pos[0]+self.player.size[0]/2+self.pos[0]-screen.get_width()/2)**2 + (self.player.pos[1]+self.player.size[1]/2+self.pos[1]-screen.get_height()/2)**2 >= self.radius**2:
      if self.player.up and self.player.moving:
        self.pos = (self.pos[0], self.pos[1] + self.player.speed)
      elif self.player.down and self.player.moving:
        self.pos = (self.pos[0], self.pos[1] - self.player.speed)
      elif self.player.left and self.player.moving:
        self.pos = (self.pos[0] + self.player.speed, self.pos[1])
      elif self.player.right and self.player.moving:
        self.pos = (self.pos[0] - self.player.speed, self.pos[1])

  def render(self, screen, debug):
    self.surface.fill((255,255,255))
    self.tilemap.render(self.surface)
    for i in self.renderlist:
      i.render(self.surface, debug)     
    screen.blit(self.surface, self.pos)
