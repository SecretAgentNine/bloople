import pygame

def box_overlap(i, j):
  if i.pos[0]+i.col_offset[0]<j.pos[0]+j.col_offset[0]+j.col_box[0] and i.pos[0]+i.col_offset[0]+i.col_box[0]>j.pos[0]+j.col_offset[0]:
    if i.pos[1]+i.col_offset[1]<j.pos[1]+j.col_offset[1]+j.col_box[1] and i.pos[1]+i.col_offset[1]+i.col_box[1]>j.pos[1]+j.col_offset[1]:
      return True
  return False

class player():
  def __init__(self, pos, size, collisionbox, collision_offset, speed):
    self.pos = pos
    self.size = size
    self.col_box = collisionbox
    self.col_offset = collision_offset
    self.speed = speed
    self.right = True
    self.up = self.down = self.left = self.moving = False
    self.key_stack = []

  def move(self, key, controls, flags=0):
    if not flags:
      self.key_stack.append(key)		#only add to the stack if the user actually pressed the key
    if key == controls['up']:
      self.moving = self.up = True
      self.down = self.left = self.right = False
    elif key == controls['down']:
      self.down = self.moving = True
      self.up = self.left = self.right = False
    elif key == controls['left']:
      self.left = self.moving = True
      self.up = self.down = self.right = False
    elif key == controls['right']:
      self.right = self.moving = True
      self.up = self.left = self.down = False

  def stop(self, key, controls):
    for i in self.key_stack:
      if i == key:
        self.key_stack.remove(i)
    if len(self.key_stack) != 0:
      self.move(self.key_stack[len(self.key_stack)-1],controls,1)
    else:
      self.moving = False    

  def update(self, collidelist):
    if self.moving:
      if self.up:
        self.pos = (self.pos[0], self.pos[1]-self.speed)
        for i in collidelist:
          if box_overlap(i, self):
	    self.pos = (self.pos[0], self.pos[1]+self.speed)
            self.moving = False
      elif self.down:
        self.pos = (self.pos[0], self.pos[1]+self.speed)        
        for i in collidelist:
          if box_overlap(i, self):
	    self.pos = (self.pos[0], self.pos[1]-self.speed)
            self.moving = False
      elif self.left:
        self.pos = (self.pos[0]-self.speed, self.pos[1])
        for i in collidelist:
          if box_overlap(i, self):
	    self.pos = (self.pos[0]+self.speed, self.pos[1])
            self.moving = False
      elif self.right:
        self.pos = (self.pos[0]+self.speed, self.pos[1])
        for i in collidelist:
          if box_overlap(i, self):
	    self.pos = (self.pos[0]-self.speed, self.pos[1])
            self.moving = False


  def render(self, screen, debug):
    screen.fill((255,0,0),(self.pos[0],self.pos[1],self.size[0],self.size[1]))
    if debug:
      screen.fill((0,255,0),(self.pos[0]+self.col_offset[0],self.pos[1]+self.col_offset[1],self.col_box[0],self.col_box[1]))
