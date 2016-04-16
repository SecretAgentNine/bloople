import pygame

class menu_item():
  def __init__(self):
    self.title = "Creative text"
    self.value = 'nah'
    self.box = (150,50)
    self.color = (100,100,100)
    self.color_select = (100,255,100)

class menu():
  def __init__(self, font, fontsize, title, items):
    self.background = pygame.image.load('resources/menu.png').convert_alpha()
    self.surface = pygame.Surface((256,256),pygame.SRCALPHA)
    self.items = items
    self.font = pygame.font.Font(font,fontsize)
    self.renderbox = False
    self.pos = (100,100)
    self.selected = None
    self.x_offset = 25
    self.y_offset = 25

  def update(self, mousepos, mousebutton):
    self.selected = None
    y_offset = self.y_offset
    mousepos = (mousepos[0]-self.pos[0],mousepos[1]-self.pos[1])
    for i in self.items:
      if self.x_offset <= mousepos[0] <= i.box[0]+self.x_offset:
        if y_offset <= mousepos[1] <= i.box[1]+y_offset:
          self.selected = i
      y_offset += self.y_offset + i.box[1]
      

  def render(self, screen):
    self.surface.fill((0,0,0))
    self.surface.blit(self.background,(0,0))
    y_offset = self.y_offset
    for i in self.items:
      if self.selected == i:
        self.surface.fill(i.color_select, (self.x_offset, y_offset, i.box[0], i.box[1]))
      else:
        self.surface.fill(i.color, (self.x_offset, y_offset, i.box[0], i.box[1]))
      self.surface.blit(self.font.render(i.title,0,(255,0,0)),(self.x_offset+25, y_offset+25))
      y_offset += self.y_offset + i.box[1]
    screen.blit(self.surface,self.pos)
