import pygame

class obj():
  def __init__(self, pos, size, collisionbox, collision_offset):
    self.pos = pos
    self.size = size
    self.col_box = collisionbox
    self.col_offset = collision_offset

  def update(self, collidelist):
    if 0:
      print "oops"

  def render(self, screen, debug):
    screen.fill((0,0,255),(self.pos[0],self.pos[1],self.size[0],self.size[1]))
    if debug:
      screen.fill((0,255,0,128),(self.pos[0]+self.col_offset[0],self.pos[1]+self.col_offset[1],self.col_box[0], self.col_box[1]))
